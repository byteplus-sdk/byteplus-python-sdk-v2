# coding=utf-8
import hashlib
import json
import os
import tempfile
import threading
import time

from datetime import datetime

from .provider import Provider, CredentialValue

_DEFAULT_CONSOLE_ENDPOINT = "https://signin.byteplus.com"
_CONSOLE_TOKEN_PATH = "/authorize/oauth/token"
_HTTP_TIMEOUT = 30
_HTTP_MAX_RETRIES = 3
_HTTP_RETRY_INTERVAL = 1
_LOGIN_CACHE_DIR_ENV = "BYTEPLUS_LOGIN_CACHE_DIRECTORY"
_EXPIRATION_BUFFER_SECONDS = 60


def _login_cache_filename(login_session):
    digest = hashlib.sha1(login_session.encode("utf-8")).hexdigest()
    return "{}.json".format(digest)


def _resolve_login_cache_dir(config_path):
    custom_dir = os.environ.get(_LOGIN_CACHE_DIR_ENV)
    if custom_dir:
        return custom_dir
    base_dir = os.path.dirname(config_path) if config_path else os.path.expanduser("~/.byteplus")
    return os.path.join(base_dir, "login", "cache")


def _login_cache_file_path(login_session, config_path):
    cache_dir = _resolve_login_cache_dir(config_path)
    return os.path.join(cache_dir, _login_cache_filename(login_session))


def _parse_rfc3339(value):
    value = (value or "").strip()
    if not value:
        raise ValueError("issued_at is empty")
    if value.endswith("Z"):
        for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    if len(value) >= 6 and value[-3] == ":" and value[-6] in ("+", "-"):
        # Python 3.6's strptime cannot parse RFC3339 offsets with a colon
        # (for example +00:00), while bp login writes RFC3339 timestamps.
        value = value[:-3] + value[-2:]
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(value)
    except (ValueError, AttributeError):
        pass
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f%z",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError("cannot parse issued_at: {}".format(value))


def _rfc3339_to_epoch(value):
    import calendar
    dt = _parse_rfc3339(value)
    if dt.tzinfo:
        utc_dt = dt - dt.utcoffset()
        return calendar.timegm(utc_dt.timetuple())
    return calendar.timegm(dt.timetuple())


def _write_json_file_atomic(path, data):
    dir_name = os.path.dirname(path)
    if dir_name and not os.path.exists(dir_name):
        try:
            os.makedirs(dir_name)
        except OSError:
            pass
    fd, tmp_path = tempfile.mkstemp(dir=dir_name or None, prefix=".tmp-login-cache-", suffix=".json")
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(data, f)
        os.chmod(tmp_path, 0o600)
        os.rename(tmp_path, path)
    except Exception:
        try:
            os.remove(tmp_path)
        except OSError:
            pass
        raise


def _parse_sts_credentials_from_access_token(access_token):
    """
    The console-login access_token is a JSON string carrying the STS triple:
      {
        "access_key_id": "...",
        "secret_access_key": "...",
        "session_token": "..."
      }
    The cache file may store it either as a JSON string ("{\"access_key_id\": ...}")
    or as an inline JSON object. Handle both.
    """
    if access_token is None:
        raise RuntimeError("console-login access_token is missing")

    if isinstance(access_token, (dict,)):
        creds = access_token
    else:
        token_str = access_token
        if isinstance(token_str, bytes):
            token_str = token_str.decode("utf-8")
        token_str = token_str.strip() if isinstance(token_str, str) else token_str
        if not token_str:
            raise RuntimeError("console-login access_token is empty")
        try:
            creds = json.loads(token_str)
        except (TypeError, ValueError) as e:
            raise RuntimeError(
                "failed to parse STS credentials from console-login access_token: {}".format(e)
            )

    if not isinstance(creds, dict):
        raise RuntimeError(
            "console-login access_token did not decode to a JSON object"
        )

    ak = (creds.get("access_key_id") or "").strip()
    sk = (creds.get("secret_access_key") or "").strip()
    token = (creds.get("session_token") or "").strip()

    if not ak:
        raise RuntimeError("console-login STS credentials missing access_key_id")
    if not sk:
        raise RuntimeError("console-login STS credentials missing secret_access_key")
    if not token:
        raise RuntimeError("console-login STS credentials missing session_token")

    return ak, sk, token


class ConsoleLoginCredentialProvider(Provider):
    """
    Reads the on-disk token cache written by 'bp login' (byteplus-cli console
    login flow) and exposes the embedded STS credentials. When the token is
    near expiration, refreshes it via the OAuth refresh_token grant against
    the signin endpoint and persists the rotated cache back to disk.

    The provider is intentionally *read/refresh-only* on the SDK side: it does
    not perform the interactive PKCE login flow (that is the CLI's job).
    """

    PROVIDER_NAME = "ConsoleLoginCredentialProvider"

    def __init__(self, login_session, config_path=None, cache_path=None):
        if not login_session:
            raise RuntimeError(
                "{}: login_session is required.".format(self.PROVIDER_NAME)
            )
        self._login_session = login_session
        self._config_path = config_path
        self._cache_path = cache_path or _login_cache_file_path(login_session, config_path)

        self._credentials = None
        self._expiration = None
        self._lock = threading.Lock()

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        if self._credentials is None:
            return True
        if self._expiration is not None:
            return time.time() >= self._expiration - _EXPIRATION_BUFFER_SECONDS
        return False

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._do_refresh()

    def get_credentials(self):
        self.refresh()
        return self._credentials

    # ---------------------------------------------------------------
    # internals
    # ---------------------------------------------------------------
    def _do_refresh(self):
        cache = self._load_cache()
        access_token = cache.get("access_token")
        issued_at = (cache.get("issued_at") or "").strip()
        expires_in = cache.get("expires_in") or 0

        try:
            issued_epoch = _rfc3339_to_epoch(issued_at)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse issued_at in '{}': {}".format(
                    self.PROVIDER_NAME, self._cache_path, e
                )
            )
        expiration_epoch = issued_epoch + int(expires_in or 0)

        # Token still good: just hand back the cached STS triple.
        if time.time() < expiration_epoch - _EXPIRATION_BUFFER_SECONDS:
            ak, sk, session_token = _parse_sts_credentials_from_access_token(access_token)
            self._expiration = expiration_epoch
            self._credentials = CredentialValue(
                ak=ak,
                sk=sk,
                session_token=session_token,
                provider_name=self.PROVIDER_NAME,
            )
            return

        # Token expired (or about to). Refresh via OAuth refresh_token grant.
        refresh_token = (cache.get("refresh_token") or "").strip()
        if not refresh_token:
            raise RuntimeError(
                "{}: cached console-login session has expired and no refresh_token "
                "is available. Please run 'bp login' to re-authenticate.".format(
                    self.PROVIDER_NAME
                )
            )

        client_id = (cache.get("client_id") or "").strip()
        if not client_id:
            raise RuntimeError(
                "{}: console-login cache '{}' does not contain client_id.".format(
                    self.PROVIDER_NAME, self._cache_path
                )
            )

        scope = (cache.get("scope") or "").strip() or None
        endpoint_url = (cache.get("endpoint_url") or "").strip() or _DEFAULT_CONSOLE_ENDPOINT
        token_url = endpoint_url.rstrip("/") + _CONSOLE_TOKEN_PATH

        # Late imports to avoid circular deps (auth.providers is imported
        # indirectly by byteplussdkcore/__init__.py).
        from byteplussdkcore import ApiClient, Configuration

        form = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
        }
        if scope:
            form["scope"] = scope

        resp_body = ApiClient(Configuration())._do_http_request(
            token_url,
            method="POST",
            post_params=form,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=_HTTP_TIMEOUT,
            max_retries=_HTTP_MAX_RETRIES,
            retry_interval=_HTTP_RETRY_INTERVAL,
            request_name="Console refresh_token",
            # OAuth refresh_token grants may rotate the refresh token on use;
            # replaying a successful-but-response-lost POST would invalidate
            # the local refresh_token. Fail fast on 5xx instead.
            retry_on_5xx=False,
            provider_name=self.PROVIDER_NAME,
        )

        try:
            resp_data = json.loads(resp_body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse refresh_token response: {}".format(
                    self.PROVIDER_NAME, e
                )
            )

        new_access_token = resp_data.get("access_token")
        if not new_access_token:
            raise RuntimeError(
                "{}: refresh_token response did not contain access_token.".format(
                    self.PROVIDER_NAME
                )
            )

        new_expires_in = resp_data.get("expires_in", 0)
        if not new_expires_in or new_expires_in <= 0:
            raise RuntimeError(
                "{}: refresh_token response did not contain valid expires_in.".format(
                    self.PROVIDER_NAME
                )
            )

        ak, sk, session_token = _parse_sts_credentials_from_access_token(new_access_token)

        # Update the on-disk cache so subsequent processes / reloads benefit.
        cache["access_token"] = new_access_token
        new_refresh = (resp_data.get("refresh_token") or "").strip()
        if new_refresh:
            cache["refresh_token"] = new_refresh
        new_id_token = (resp_data.get("id_token") or "").strip()
        if new_id_token:
            cache["id_token"] = new_id_token
        new_token_type = (resp_data.get("token_type") or "").strip()
        if new_token_type:
            cache["token_type"] = new_token_type
        cache["issued_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time())
        )
        cache["expires_in"] = new_expires_in

        try:
            _write_json_file_atomic(self._cache_path, cache)
        except Exception:
            # Best-effort: in-memory credentials are still usable even if the
            # cache file cannot be persisted.
            pass

        self._expiration = time.time() + int(new_expires_in)
        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )

    def _load_cache(self):
        if not os.path.isfile(self._cache_path):
            raise RuntimeError(
                "{}: console-login cache file not found at '{}'. "
                "Please run 'bp login' first.".format(
                    self.PROVIDER_NAME, self._cache_path
                )
            )
        with open(self._cache_path, 'r') as f:
            try:
                return json.load(f)
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse console-login cache '{}': {}".format(
                        self.PROVIDER_NAME, self._cache_path, e
                    )
                )
