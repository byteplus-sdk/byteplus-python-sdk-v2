# coding=utf-8
import calendar
import hashlib
import json
import os
import threading
import time

from datetime import datetime

from .provider import Provider, CredentialValue

try:
    string_types = (basestring,)
except NameError:  # pragma: no cover - Python 3
    string_types = (str,)

_DEFAULT_CONSOLE_ENDPOINT = "https://signin.byteplus.com"
_CONSOLE_TOKEN_PATH = "/authorize/oauth/token"
_HTTP_TIMEOUT = 30
_EXPIRATION_BUFFER_SECONDS = 60


def _login_cache_filename(login_session):
    digest = hashlib.sha1(login_session.encode("utf-8")).hexdigest()
    return "{}.json".format(digest)


def _parse_rfc3339(value):
    value = (value or "").strip()
    if not value:
        raise ValueError("timestamp is empty")
    if value.endswith("Z"):
        for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%fZ"):
            try:
                return datetime.strptime(value, fmt)
            except ValueError:
                continue
    if len(value) >= 6 and value[-3] == ":" and value[-6] in ("+", "-"):
        value = value[:-3] + value[-2:]
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
    raise ValueError("cannot parse timestamp: {}".format(value))


def _rfc3339_to_epoch(value):
    dt = _parse_rfc3339(value)
    if dt.tzinfo:
        utc_dt = dt - dt.utcoffset()
        return calendar.timegm(utc_dt.timetuple())
    return calendar.timegm(dt.timetuple())


def _console_login_cache_expiration(cache):
    issued_at = cache.get("issued_at")
    issued_at = issued_at.strip() if isinstance(issued_at, string_types) else ""
    if not issued_at:
        return None
    try:
        expires_in = int(cache.get("expires_in", 0))
    except (TypeError, ValueError):
        expires_in = 0
    if expires_in <= 0:
        return None
    try:
        return _rfc3339_to_epoch(issued_at) + expires_in
    except ValueError:
        return None


def _parse_sts_credentials_from_access_token(access_token):
    if isinstance(access_token, dict):
        creds = access_token
    elif isinstance(access_token, string_types):
        try:
            creds = json.loads(access_token)
        except ValueError as e:
            raise RuntimeError(
                "failed to parse STS credentials from console-login access_token: {}".format(e)
            )
    else:
        raise RuntimeError("console-login access_token is missing or has unexpected type")

    if not isinstance(creds, dict):
        raise RuntimeError("console-login access_token did not decode to a JSON object")

    ak = creds.get("access_key_id")
    ak = ak.strip() if isinstance(ak, string_types) else ""
    sk = creds.get("secret_access_key")
    sk = sk.strip() if isinstance(sk, string_types) else ""
    token = creds.get("session_token")
    token = token.strip() if isinstance(token, string_types) else ""

    if not ak or not sk or not token:
        raise RuntimeError("console-login STS credentials missing required fields")
    return ak, sk, token


class ConsoleLoginCredentialProvider(Provider):
    """Reads and refreshes STS credentials for the CLI 'bp login' flow.

    Disk reads happen on bootstrap and on the invalid_grant fallback only. The
    provider never writes the login cache; byteplus-cli remains the sole writer.
    OAuth refresh updates the in-memory cache so rotated refresh_token values
    are reused inside the current process.
    """

    PROVIDER_NAME = "ConsoleLoginCredentialProvider"

    def __init__(self, login_session, cache_dir):
        if not login_session:
            raise RuntimeError(
                "{}: login_session is required.".format(self.PROVIDER_NAME)
            )
        self._login_session = login_session
        self._cache_dir = cache_dir
        self._cache_path = os.path.join(
            self._cache_dir, _login_cache_filename(login_session)
        )

        self._credentials = None
        self._expiration = None
        self._cache = None
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

    def _do_refresh(self):
        if self._cache is None:
            self._cache = self._load_cache_from_disk()

        if self._try_apply_from_cache(self._cache):
            return

        invalid_grant_error = None
        try:
            self._refresh_with_oauth(self._cache)
            return
        except _ConsoleLoginInvalidGrantError as exc:
            invalid_grant_error = exc
        except Exception as e:
            raise RuntimeError(
                "{}: console-login refresh failed; please run 'bp login'. "
                "underlying error: {}".format(self.PROVIDER_NAME, e)
            )

        try:
            disk_cache = self._load_cache_from_disk()
        except Exception as e:
            raise RuntimeError(
                "{}: console-login refresh token rejected ({}); failed to reload "
                "cache from disk: {}; please run 'bp login'".format(
                    self.PROVIDER_NAME, invalid_grant_error, e
                )
            )

        disk_rt = _strip_string(disk_cache.get("refresh_token"))
        memory_rt = _strip_string(self._cache.get("refresh_token"))
        if not disk_rt or disk_rt == memory_rt:
            raise RuntimeError(
                "{}: console-login refresh token rejected by signin service; "
                "please run 'bp login' to re-authenticate. underlying error: {}".format(
                    self.PROVIDER_NAME, invalid_grant_error
                )
            )

        self._cache = disk_cache
        if self._try_apply_from_cache(self._cache):
            return
        try:
            self._refresh_with_oauth(self._cache)
        except _ConsoleLoginInvalidGrantError as e:
            raise RuntimeError(
                "{}: console-login refresh token rejected; reloaded disk cache "
                "but new RT also failed; please run 'bp login'. underlying error: {}".format(
                    self.PROVIDER_NAME, e
                )
            )
        except Exception as e:
            raise RuntimeError(
                "{}: console-login refresh failed after disk reload; "
                "please run 'bp login'. underlying error: {}".format(
                    self.PROVIDER_NAME, e
                )
            )

    def _try_apply_from_cache(self, cache):
        expiration = _console_login_cache_expiration(cache)
        if expiration is None or time.time() >= expiration - _EXPIRATION_BUFFER_SECONDS:
            return False
        try:
            ak, sk, session_token = _parse_sts_credentials_from_access_token(
                cache.get("access_token")
            )
        except RuntimeError:
            return False

        self._expiration = expiration
        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )
        return True

    def _refresh_with_oauth(self, cache):
        refresh_token = _strip_string(cache.get("refresh_token"))
        if not refresh_token:
            raise RuntimeError(
                "{}: console-login cache '{}' does not contain refresh_token; "
                "please run 'bp login' first.".format(self.PROVIDER_NAME, self._cache_path)
            )

        client_id = _strip_string(cache.get("client_id"))
        if not client_id:
            raise RuntimeError(
                "{}: console-login cache '{}' does not contain client_id; "
                "please run 'bp login' to regenerate.".format(self.PROVIDER_NAME, self._cache_path)
            )

        endpoint = (
            _strip_string(cache.get("endpoint_url"))
            or _DEFAULT_CONSOLE_ENDPOINT
        )
        scope = _strip_string(cache.get("scope"))
        url = "{}{}".format(endpoint.rstrip("/"), _CONSOLE_TOKEN_PATH)
        body = {
            "grant_type": "refresh_token",
            "client_id": client_id,
            "refresh_token": refresh_token,
        }
        if scope:
            body["scope"] = scope

        try:
            from urllib.parse import urlencode
            import urllib.request as urlreq
            import urllib.error as urlerr
        except ImportError:  # pragma: no cover - Python 2 compatibility
            from urllib import urlencode
            import urllib2 as urlreq
            urlerr = urlreq

        encoded = urlencode(body).encode("utf-8")
        req = urlreq.Request(
            url, encoded,
            {"Content-Type": "application/x-www-form-urlencoded"},
        )
        try:
            resp = urlreq.urlopen(req, timeout=_HTTP_TIMEOUT)
            try:
                resp_bytes = resp.read()
            finally:
                resp.close()
        except urlerr.HTTPError as e:
            err_body = e.read().decode("utf-8", "replace") if hasattr(e, "read") else ""
            err_code = ""
            try:
                err_code = json.loads(err_body or "{}").get("error") or ""
            except ValueError:
                pass
            if e.code == 400 and err_code == "invalid_grant":
                raise _ConsoleLoginInvalidGrantError(
                    "console-login refresh_token rejected (invalid_grant): {}".format(err_body)
                )
            raise RuntimeError(
                "{}: console-login refresh failed with HTTP {}: {}".format(
                    self.PROVIDER_NAME, e.code, err_body
                )
            )
        except Exception as e:
            raise RuntimeError(
                "{}: console-login refresh request failed: {}".format(self.PROVIDER_NAME, e)
            )

        if not isinstance(resp_bytes, string_types):
            resp_text = resp_bytes.decode("utf-8")
        else:
            resp_text = resp_bytes
        try:
            payload = json.loads(resp_text)
        except ValueError as e:
            raise RuntimeError(
                "{}: console-login refresh response not JSON: {}".format(
                    self.PROVIDER_NAME, e
                )
            )
        if not isinstance(payload, dict):
            raise RuntimeError(
                "{}: console-login refresh response is not a JSON object.".format(
                    self.PROVIDER_NAME
                )
            )

        access_token = payload.get("access_token")
        if isinstance(access_token, dict):
            new_access = access_token
        else:
            new_access = _strip_string(access_token)
        try:
            expires_in = int(payload.get("expires_in", 0))
        except (TypeError, ValueError) as e:
            raise RuntimeError(
                "{}: console-login refresh response has invalid expires_in: {}".format(
                    self.PROVIDER_NAME, e
                )
            )
        if not new_access or expires_in <= 0:
            raise RuntimeError(
                "{}: console-login refresh response missing access_token or expires_in".format(
                    self.PROVIDER_NAME
                )
            )

        cache["access_token"] = new_access
        new_rt = _strip_string(payload.get("refresh_token"))
        if new_rt:
            cache["refresh_token"] = new_rt
        new_id = _strip_string(payload.get("id_token"))
        if new_id:
            cache["id_token"] = new_id
        new_token_type = _strip_string(payload.get("token_type"))
        if new_token_type:
            cache["token_type"] = new_token_type
        new_scope = _strip_string(payload.get("scope"))
        if new_scope:
            cache["scope"] = new_scope
        cache["issued_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        cache["expires_in"] = expires_in

        if not self._try_apply_from_cache(cache):
            raise RuntimeError(
                "{}: console-login refresh succeeded but the new access_token "
                "could not be parsed into STS credentials".format(self.PROVIDER_NAME)
            )

    def _load_cache_from_disk(self):
        if not os.path.isfile(self._cache_path):
            raise RuntimeError(
                "{}: console-login cache file not found at '{}'. "
                "Please run 'bp login' first.".format(self.PROVIDER_NAME, self._cache_path)
            )
        try:
            with open(self._cache_path, 'r') as f:
                return json.load(f)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse console-login cache '{}': {}".format(
                    self.PROVIDER_NAME, self._cache_path, e
                )
            )
        except (IOError, OSError) as e:
            raise RuntimeError(
                "{}: failed to read console-login cache '{}': {}".format(
                    self.PROVIDER_NAME, self._cache_path, e
                )
            )


def _strip_string(value):
    return value.strip() if isinstance(value, string_types) else ""


class _ConsoleLoginInvalidGrantError(Exception):
    """Raised when signin returns OAuth 400 invalid_grant."""
