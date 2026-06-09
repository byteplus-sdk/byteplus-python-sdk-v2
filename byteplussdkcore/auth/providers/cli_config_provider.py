# coding=utf-8
import calendar
import hashlib
import json
import os
import threading
import time

import dateutil.parser
import six

from .provider import Provider, CredentialValue

_DEFAULT_REGION = "ap-southeast-1"
_OAUTH_BASE_URL_TEMPLATE = "https://cloudidentity-oauth.{}.bytepluses.com"
_PORTAL_BASE_URL_TEMPLATE = "https://cloudidentity-portal.{}.bytepluses.com"
_PORTAL_ACCESS_TOKEN_HEADER = "x-bd-cloudidentity-bearer-token"
_HTTP_TIMEOUT = 30
_HTTP_MAX_RETRIES = 3
_HTTP_RETRY_INTERVAL = 1
_LOGIN_CACHE_DIRECTORY_ENV = "BYTEPLUS_LOGIN_CACHE_DIRECTORY"
_DEFAULT_CONSOLE_LOGIN_ENDPOINT = "https://signin.byteplus.com"
_CONSOLE_LOGIN_TOKEN_PATH = "/authorize/oauth/token"


class CLIConfigCredentialProvider(Provider):
    PROVIDER_NAME = "CLIConfigCredentialProvider"

    def __init__(self, profile_name=None, config_path=None):
        self._profile_name = profile_name
        self._config_path = config_path
        self._delegate = None
        self._static_cred = None
        self._initialized = False
        self._init_lock = threading.Lock()
        self._resolved_config_path = None

    def _init_delegate(self):
        profile, profile_name, config = self._load_profile()
        raw_mode = profile.get("mode", "") or ""
        mode = raw_mode.lower().strip()

        if mode in ("ak", ""):
            self._static_cred = self._read_ak_mode(profile, profile_name)
        elif mode == "ramrolearn":
            self._static_cred = None
            self._delegate = self._create_ram_role_arn_delegate(profile, profile_name)
        elif mode == "oidc":
            self._static_cred = None
            self._delegate = self._create_oidc_delegate(profile, profile_name)
        elif mode == "ecsrole":
            self._static_cred = None
            self._delegate = self._create_ecs_role_delegate(profile, profile_name)
        elif mode == "sso":
            self._static_cred = None
            self._delegate = self._create_sso_delegate(profile, profile_name, config)
        elif mode == "console-login":
            self._static_cred = None
            self._delegate = self._create_console_login_delegate(profile, profile_name)
        else:
            raise RuntimeError(
                "{}: unsupported mode: {}".format(self.PROVIDER_NAME, mode)
            )

    def _load_profile(self):
        config_path = (
            self._config_path
            or os.environ.get("BYTEPLUS_CLI_CONFIG_FILE")
            or os.path.expanduser("~/.byteplus/config.json")
        )
        self._resolved_config_path = config_path

        if not os.path.isfile(config_path):
            raise RuntimeError(
                "{}: config file not found at '{}'.".format(self.PROVIDER_NAME, config_path)
            )

        with open(config_path, 'r') as f:
            try:
                config = json.load(f)
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse config file '{}': {}".format(
                        self.PROVIDER_NAME, config_path, e
                    )
                )

        profile_name = (self._profile_name
                        or os.environ.get("BYTEPLUS_PROFILE")
                        or config.get("current"))

        if not profile_name:
            profile_name = "default"

        profiles = config.get("profiles", {})
        profile = profiles.get(profile_name)

        if profile is None:
            raise RuntimeError(
                "{}: profile '{}' not found in config file.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return profile, profile_name, config

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        if not self._initialized:
            return True
        if self._delegate is not None:
            return self._delegate.is_expired()
        return False

    def refresh(self):
        if self._delegate is not None:
            return self._delegate.refresh()
        return

    def get_credentials(self):
        if not self._initialized:
            with self._init_lock:
                if not self._initialized:
                    self._init_delegate()
                    self._initialized = True
        if self._delegate is not None:
            return self._delegate.get_credentials()
        return self._static_cred

    def _read_ak_mode(self, profile, profile_name):
        ak = profile.get("access-key", "").strip()
        sk = profile.get("secret-key", "").strip()

        if not ak or not sk:
            raise RuntimeError(
                "{}: profile '{}' does not contain valid access-key and secret-key.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        session_token = profile.get("session-token", "").strip() or None

        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )

    def _create_ram_role_arn_delegate(self, profile, profile_name):
        from .sts_provider import StsCredentialProvider

        ak = profile.get("access-key", "").strip()
        sk = profile.get("secret-key", "").strip()
        role_name = profile.get("role-name", "").strip()
        account_id = profile.get("account-id", "").strip()

        if not ak or not sk:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but access-key/secret-key is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not account_id:
            raise RuntimeError(
                "{}: profile '{}' mode is RamRoleArn but account-id is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        kwargs = dict(ak=ak, sk=sk, role_name=role_name, account_id=account_id)
        region = (profile.get("region") or "").strip()
        if region:
            kwargs["region"] = region
        return StsCredentialProvider(**kwargs)

    def _create_oidc_delegate(self, profile, profile_name):
        from .sts_oidc_provider import StsOidcCredentialProvider

        role_trn = (profile.get("role-trn") or "").strip()
        oidc_token_file = (profile.get("oidc-token-file") or "").strip()
        policy = (profile.get("policy") or "").strip() or None

        if not role_trn:
            raise RuntimeError(
                "{}: profile '{}' mode is OIDC but role-trn is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )
        if not oidc_token_file:
            raise RuntimeError(
                "{}: profile '{}' mode is OIDC but oidc-token-file is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        kwargs = dict(role_trn=role_trn, oidc_token_file=oidc_token_file, policy=policy)
        region = (profile.get("region") or "").strip()
        if region:
            kwargs["region"] = region
        return StsOidcCredentialProvider(**kwargs)

    def _create_ecs_role_delegate(self, profile, profile_name):
        from .ecs_role_provider import EcsRoleCredentialProvider

        role_name = profile.get("role-name", "").strip()

        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is EcsRole but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        return EcsRoleCredentialProvider(role_name=role_name)

    def _create_console_login_delegate(self, profile, profile_name):
        login_session = (profile.get("login-session") or "").strip()
        if not login_session:
            raise RuntimeError(
                "{}: profile '{}' mode is console-login but login-session is not set. "
                "Please run 'bp login' first.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        config_path = self._resolved_config_path or (
            self._config_path
            or os.environ.get("BYTEPLUS_CLI_CONFIG_FILE")
            or os.path.expanduser("~/.byteplus/config.json")
        )

        cache_dir = (
            os.environ.get(_LOGIN_CACHE_DIRECTORY_ENV)
            or os.path.join(os.path.dirname(config_path), "login", "cache")
        )
        return ConsoleLoginCredentialProvider(
            login_session=login_session,
            cache_dir=cache_dir,
        )

    def _create_sso_delegate(self, profile, profile_name, config):
        session_name = (profile.get("sso-session-name") or "").strip()
        if not session_name:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but sso-session-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        sso_sessions = config.get("sso-session", {}) or {}
        session = sso_sessions.get(session_name)
        if session is None:
            raise RuntimeError(
                "{}: sso-session '{}' not found in config file.".format(
                    self.PROVIDER_NAME, session_name
                )
            )

        start_url = (session.get("start-url") or "").strip()
        if not start_url:
            raise RuntimeError(
                "{}: sso-session '{}' does not contain start-url.".format(
                    self.PROVIDER_NAME, session_name
                )
            )

        region = (session.get("region") or "").strip() or _DEFAULT_REGION

        account_id = (profile.get("account-id") or "").strip()
        if not account_id:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but account-id is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        role_name = (profile.get("role-name") or "").strip()
        if not role_name:
            raise RuntimeError(
                "{}: profile '{}' mode is sso but role-name is not set.".format(
                    self.PROVIDER_NAME, profile_name
                )
            )

        config_path = self._resolved_config_path or (
            self._config_path
            or os.environ.get("BYTEPLUS_CLI_CONFIG_FILE")
            or os.path.expanduser("~/.byteplus/config.json")
        )
        cache_dir = os.path.join(os.path.dirname(config_path), "sso", "cache")

        return SsoCredentialProvider(
            profile=profile,
            start_url=start_url,
            session_name=session_name,
            region=region,
            account_id=account_id,
            role_name=role_name,
            cache_dir=cache_dir,
        )


def _unix_timestamp_to_epoch(ts):
    if ts >= 1e18:
        return ts / 1e9
    elif ts >= 1e15:
        return ts / 1e6
    elif ts >= 1e12:
        return ts / 1e3
    else:
        return float(ts)


def _token_cache_filename(start_url, session_name):
    payload = json.dumps({"start_url": start_url, "session_name": session_name},
                         separators=(',', ':'), sort_keys=False)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()
    return "{}.json".format(digest)


def _parse_rfc3339(value):
    """Parse RFC3339 timestamps consistently across supported Python versions."""
    value = value.strip()
    if not value:
        raise ValueError("expires_at is empty")
    try:
        return dateutil.parser.parse(value)
    except (ValueError, OverflowError, TypeError) as e:
        raise ValueError("cannot parse expires_at: {}: {}".format(value, e))


def _rfc3339_to_epoch(value):
    exp_dt = _parse_rfc3339(value)
    if exp_dt.tzinfo:
        utc_dt = exp_dt - exp_dt.utcoffset()
        return calendar.timegm(utc_dt.timetuple())
    return calendar.timegm(exp_dt.timetuple())


def _login_cache_filename(login_session):
    return "{}.json".format(hashlib.sha1(login_session.encode("utf-8")).hexdigest())


def _console_login_cache_expiration(token_cache, cache_path, provider_name):
    raw_issued_at = token_cache.get("issued_at")
    issued_at = raw_issued_at.strip() if isinstance(raw_issued_at, six.string_types) else ""
    if not issued_at:
        raise RuntimeError(
            "{}: console-login token cache '{}' does not contain issued_at.".format(
                provider_name, cache_path
            )
        )
    try:
        expires_in = int(token_cache.get("expires_in", 0))
    except (TypeError, ValueError):
        expires_in = 0
    if expires_in <= 0:
        raise RuntimeError(
            "{}: console-login token cache '{}' does not contain valid expires_in.".format(
                provider_name, cache_path
            )
        )
    try:
        issued_at_epoch = _rfc3339_to_epoch(issued_at)
    except ValueError as e:
        raise RuntimeError(
            "{}: failed to parse console-login issued_at in '{}': {}".format(
                provider_name, cache_path, e
            )
        )
    return issued_at_epoch + expires_in


def _parse_console_login_access_token(access_token, cache_path, provider_name):
    if isinstance(access_token, dict):
        sts_creds = access_token
    elif isinstance(access_token, six.string_types):
        try:
            sts_creds = json.loads(access_token)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse console-login access_token in '{}': {}".format(
                    provider_name, cache_path, e
                )
            )
    else:
        raise RuntimeError(
            "{}: console-login token cache '{}' does not contain valid access_token.".format(
                provider_name, cache_path
            )
        )

    if not isinstance(sts_creds, dict):
        raise RuntimeError(
            "{}: console-login access_token in '{}' is not an object.".format(
                provider_name, cache_path
            )
        )

    raw_ak = sts_creds.get("access_key_id")
    ak = raw_ak.strip() if isinstance(raw_ak, six.string_types) else ""
    raw_sk = sts_creds.get("secret_access_key")
    sk = raw_sk.strip() if isinstance(raw_sk, six.string_types) else ""
    raw_token = sts_creds.get("session_token")
    token = raw_token.strip() if isinstance(raw_token, six.string_types) else ""
    if not ak or not sk or not token:
        raise RuntimeError(
            "{}: console-login access_token in '{}' is missing STS credential fields.".format(
                provider_name, cache_path
            )
        )

    return {
        "access_key_id": ak,
        "secret_access_key": sk,
        "session_token": token,
    }


class ConsoleLoginCredentialProvider(Provider):
    """Reads and refreshes STS credentials for the CLI 'bp login' flow.

    The SDK reads disk only on bootstrap and on the invalid_grant fallback. It
    never writes the login cache; byteplus-cli remains the sole cache writer.
    """

    PROVIDER_NAME = "ConsoleLoginCredentialProvider"

    def __init__(self, login_session, cache_dir):
        self._login_session = login_session
        self._cache_dir = cache_dir
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
            return time.time() >= self._expiration - 60
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

        cache_path = os.path.join(
            self._cache_dir, _login_cache_filename(self._login_session)
        )

        if self._try_apply_from_cache(self._cache, cache_path):
            return

        try:
            self._refresh_with_oauth(self._cache, cache_path)
            return
        except _ConsoleLoginInvalidGrantError as exc:
            invalid_grant_exc = exc

        try:
            disk_cache = self._load_cache_from_disk()
        except (RuntimeError, IOError, OSError) as e:
            raise RuntimeError(
                "{}: failed to reload console-login cache from disk; "
                "please run 'bp login' to re-authenticate. "
                "underlying error: {}".format(self.PROVIDER_NAME, e)
            )

        disk_rt = disk_cache.get("refresh_token")
        if not (isinstance(disk_rt, six.string_types) and disk_rt.strip()):
            raise RuntimeError(
                "{}: console-login refresh token rejected and disk cache lacks "
                "refresh_token; please run 'bp login' to re-authenticate.".format(
                    self.PROVIDER_NAME
                )
            )
        if disk_cache.get("refresh_token") == self._cache.get("refresh_token"):
            raise RuntimeError(
                "{}: console-login refresh token rejected by signin service "
                "(disk cache has the same RT); please run 'bp login' to "
                "re-authenticate. underlying error: {}".format(
                    self.PROVIDER_NAME, invalid_grant_exc
                )
            )

        self._cache = disk_cache
        if self._try_apply_from_cache(self._cache, cache_path):
            return
        try:
            self._refresh_with_oauth(self._cache, cache_path)
        except _ConsoleLoginInvalidGrantError as exc2:
            raise RuntimeError(
                "{}: console-login refresh token rejected; reloaded disk cache "
                "but new RT also failed; please run 'bp login'. underlying error: {}".format(
                    self.PROVIDER_NAME, exc2
                )
            )

    def _load_cache_from_disk(self):
        cache_path = os.path.join(
            self._cache_dir, _login_cache_filename(self._login_session)
        )
        if not os.path.isfile(cache_path):
            raise RuntimeError(
                "{}: console-login token cache file '{}' does not exist; "
                "please run 'bp login' to re-authenticate.".format(
                    self.PROVIDER_NAME, cache_path
                )
            )
        try:
            with open(cache_path, 'r') as f:
                try:
                    return json.load(f)
                except ValueError as e:
                    raise RuntimeError(
                        "{}: failed to parse console-login token cache '{}': {}; "
                        "please run 'bp login' to re-authenticate.".format(
                            self.PROVIDER_NAME, cache_path, e
                        )
                    )
        except (IOError, OSError) as e:
            raise RuntimeError(
                "{}: failed to read console-login token cache '{}': {}; "
                "please run 'bp login' to re-authenticate.".format(
                    self.PROVIDER_NAME, cache_path, e
                )
            )

    def _try_apply_from_cache(self, cache, cache_path):
        try:
            exp_epoch = _console_login_cache_expiration(
                cache, cache_path, self.PROVIDER_NAME
            )
        except RuntimeError:
            return False
        if time.time() >= exp_epoch - 60:
            return False
        try:
            sts_creds = _parse_console_login_access_token(
                cache.get("access_token"), cache_path, self.PROVIDER_NAME
            )
        except RuntimeError:
            return False
        self._credentials = CredentialValue(
            ak=sts_creds["access_key_id"],
            sk=sts_creds["secret_access_key"],
            session_token=sts_creds["session_token"],
            provider_name=self.PROVIDER_NAME,
        )
        self._expiration = exp_epoch
        return True

    def _refresh_with_oauth(self, cache, cache_path):
        raw_rt = cache.get("refresh_token")
        refresh_token = raw_rt.strip() if isinstance(raw_rt, six.string_types) else ""
        if not refresh_token:
            raise RuntimeError(
                "{}: console-login cache lacks refresh_token; please run 'bp login' first.".format(
                    self.PROVIDER_NAME
                )
            )
        raw_client_id = cache.get("client_id")
        client_id = raw_client_id.strip() if isinstance(raw_client_id, six.string_types) else ""
        if not client_id:
            raise RuntimeError(
                "{}: console-login cache lacks client_id; please run 'bp login' to regenerate.".format(
                    self.PROVIDER_NAME
                )
            )
        raw_endpoint = cache.get("endpoint_url")
        endpoint = (
            raw_endpoint.strip() if isinstance(raw_endpoint, six.string_types) else ""
        ) or _DEFAULT_CONSOLE_LOGIN_ENDPOINT
        raw_scope = cache.get("scope")
        scope = raw_scope.strip() if isinstance(raw_scope, six.string_types) else ""
        url = "{}{}".format(endpoint.rstrip("/"), _CONSOLE_LOGIN_TOKEN_PATH)
        body = {
            "grant_type": "refresh_token",
            "client_id": client_id,
            "refresh_token": refresh_token,
        }
        if scope:
            body["scope"] = scope

        try:
            from urllib.parse import urlencode
        except ImportError:
            from urllib import urlencode
        encoded_bytes = urlencode(body).encode("utf-8")

        try:
            import urllib.request as urlreq
            import urllib.error as urlerr
        except ImportError:
            import urllib2 as urlreq
            urlerr = urlreq

        req = urlreq.Request(
            url, encoded_bytes,
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
                err_code = (json.loads(err_body or "{}").get("error") or "")
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

        try:
            payload = json.loads(resp_bytes)
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

        raw_access = payload.get("access_token")
        new_access = raw_access.strip() if isinstance(raw_access, six.string_types) else ""
        try:
            new_expires = int(payload.get("expires_in", 0))
        except (TypeError, ValueError) as e:
            raise RuntimeError(
                "{}: console-login refresh response has invalid expires_in: {}".format(
                    self.PROVIDER_NAME, e
                )
            )
        if not new_access or new_expires <= 0:
            raise RuntimeError(
                "{}: console-login refresh response missing access_token or expires_in".format(
                    self.PROVIDER_NAME
                )
            )

        cache["access_token"] = new_access
        raw_new_rt = payload.get("refresh_token")
        new_rt = raw_new_rt.strip() if isinstance(raw_new_rt, six.string_types) else ""
        if new_rt:
            cache["refresh_token"] = new_rt
        raw_id = payload.get("id_token")
        new_id = raw_id.strip() if isinstance(raw_id, six.string_types) else ""
        if new_id:
            cache["id_token"] = new_id
        raw_token_type = payload.get("token_type")
        if isinstance(raw_token_type, six.string_types) and raw_token_type.strip():
            cache["token_type"] = raw_token_type
        cache["issued_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        cache["expires_in"] = new_expires

        if not self._try_apply_from_cache(cache, cache_path):
            raise RuntimeError(
                "{}: console-login refresh succeeded but the new access_token "
                "could not be parsed into STS credentials".format(self.PROVIDER_NAME)
            )


class _ConsoleLoginInvalidGrantError(Exception):
    """Sentinel raised when the signin OAuth endpoint returns invalid_grant."""


class SsoCredentialProvider(Provider):
    """Obtains temporary credentials via the BytePlus SSO flow.

    The SDK reads the SSO token cache from disk only to bootstrap its
    in-memory state. Refreshing OAuth tokens mutates that in-memory state and
    never writes the cache file; bp cli remains the single writer.
    """

    PROVIDER_NAME = "SsoCredentialProvider"

    def __init__(self, profile, start_url, session_name, region,
                 account_id, role_name, cache_dir):
        self._profile = profile
        self._start_url = start_url
        self._session_name = session_name
        self._region = region
        self._account_id = account_id
        self._role_name = role_name
        self._cache_dir = cache_dir

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
            return time.time() >= self._expiration - 60
        return False

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._do_refresh()

    def get_credentials(self):
        self.refresh()
        return self._credentials

    def _do_refresh(self):
        cred = self._try_cached_sts_credentials()
        if cred is not None:
            self._credentials = cred
            return

        token_path = os.path.join(
            self._cache_dir,
            _token_cache_filename(self._start_url, self._session_name),
        )

        if self._cache is None:
            if not os.path.isfile(token_path):
                raise RuntimeError(
                    "{}: SSO token cache file not found at '{}'; "
                    "please run 'bp sso login' to re-authenticate.".format(
                        self.PROVIDER_NAME, token_path
                    )
                )
            try:
                with open(token_path, 'r') as f:
                    self._cache = json.load(f)
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse SSO token cache '{}': {}; "
                    "please run 'bp sso login' to re-authenticate.".format(
                        self.PROVIDER_NAME, token_path, e
                    )
                )
            except (IOError, OSError) as e:
                raise RuntimeError(
                    "{}: failed to read SSO token cache '{}': {}; "
                    "please run 'bp sso login' to re-authenticate.".format(
                        self.PROVIDER_NAME, token_path, e
                    )
                )

        raw_access_token = self._cache.get("access_token")
        access_token = raw_access_token.strip() if isinstance(raw_access_token, six.string_types) else ""
        if not access_token:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain access_token; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        raw_expires_at = self._cache.get("expires_at")
        expires_at = raw_expires_at.strip() if isinstance(raw_expires_at, six.string_types) else ""
        token_expired = False
        if expires_at:
            try:
                exp_epoch = _rfc3339_to_epoch(expires_at)
                token_expired = time.time() > exp_epoch
            except ValueError as e:
                raise RuntimeError(
                    "{}: failed to parse expires_at in '{}': {}; "
                    "please run 'bp sso login' to re-authenticate.".format(
                        self.PROVIDER_NAME, token_path, e
                    )
                )

        if token_expired:
            access_token = self._refresh_access_token(token_path)

        self._fetch_role_credentials(access_token)

    def _try_cached_sts_credentials(self):
        sts_expiration = self._profile.get("sts-expiration", 0)
        if not sts_expiration or sts_expiration <= 0:
            return None

        exp_epoch = _unix_timestamp_to_epoch(sts_expiration)
        if time.time() >= exp_epoch:
            return None

        ak = (self._profile.get("access-key") or "").strip()
        sk = (self._profile.get("secret-key") or "").strip()
        if not ak or not sk:
            return None

        session_token = (self._profile.get("session-token") or "").strip() or None

        self._expiration = exp_epoch
        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token,
            provider_name=self.PROVIDER_NAME,
        )

    def _refresh_access_token(self, token_path):
        token_cache = self._cache
        raw_refresh_token = token_cache.get("refresh_token")
        refresh_token = raw_refresh_token.strip() if isinstance(raw_refresh_token, six.string_types) else ""
        if not refresh_token:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain refresh_token; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        client_secret_expires_at = token_cache.get("client_secret_expires_at", 0)
        if client_secret_expires_at and client_secret_expires_at > 0:
            exp_epoch = _unix_timestamp_to_epoch(client_secret_expires_at)
            if time.time() >= exp_epoch:
                raise RuntimeError(
                    "{}: refresh token in '{}' has expired; "
                    "please run 'bp sso login' to re-authenticate.".format(
                        self.PROVIDER_NAME, token_path
                    )
                )

        raw_client_id = token_cache.get("client_id")
        client_id = raw_client_id.strip() if isinstance(raw_client_id, six.string_types) else ""
        raw_client_secret = token_cache.get("client_secret")
        client_secret = raw_client_secret.strip() if isinstance(raw_client_secret, six.string_types) else ""
        if not client_id or not client_secret:
            raise RuntimeError(
                "{}: SSO token cache '{}' does not contain client_id/client_secret; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME, token_path
                )
            )

        oauth_url = "{}/token".format(
            _OAUTH_BASE_URL_TEMPLATE.format(self._region)
        )

        # Late imports to avoid circular deps (auth.providers is imported
        # indirectly by byteplussdkcore/__init__.py).
        from byteplussdkcore import ApiClient, Configuration
        # Pass a dict body; RESTClient auto-serializes with Content-Type:
        # application/json (see byteplussdkcore/rest.py). Do NOT json.dumps
        # here or it will be double-encoded.
        try:
            resp_body = ApiClient(Configuration())._do_http_request(
                oauth_url,
                method="POST",
                data={
                    "grant_type": "refresh_token",
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "refresh_token": refresh_token,
                },
                headers={"Content-Type": "application/json"},
                timeout=_HTTP_TIMEOUT,
                max_retries=_HTTP_MAX_RETRIES,
                retry_interval=_HTTP_RETRY_INTERVAL,
                request_name="OAuth token refresh",
                # OAuth refresh_token grants may rotate the refresh token on use;
                # replaying a successful-but-response-lost POST would invalidate
                # the local refresh_token. Fail fast on 5xx instead.
                retry_on_5xx=False,
                provider_name=self.PROVIDER_NAME,
            )
        except RuntimeError as e:
            raise RuntimeError(
                "{}: SSO OAuth token refresh failed; "
                "please run 'bp sso login' to re-authenticate. "
                "underlying error: {}".format(self.PROVIDER_NAME, e)
            )

        try:
            resp_data = json.loads(resp_body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse OAuth token response: {}; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME, e
                )
            )

        if not isinstance(resp_data, dict):
            raise RuntimeError(
                "{}: OAuth token response is not a JSON object; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME
                )
            )

        raw_access_token = resp_data.get("access_token")
        new_access_token = raw_access_token.strip() if isinstance(raw_access_token, six.string_types) else ""
        if not new_access_token:
            raise RuntimeError(
                "{}: OAuth token response did not contain access_token; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME
                )
            )

        try:
            expires_in = int(resp_data.get("expires_in", 0))
        except (TypeError, ValueError) as e:
            raise RuntimeError(
                "{}: OAuth token response has invalid expires_in: {}; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME, e
                )
            )
        if expires_in <= 0:
            raise RuntimeError(
                "{}: OAuth token response did not contain valid expires_in; "
                "please run 'bp sso login' to re-authenticate.".format(
                    self.PROVIDER_NAME
                )
            )

        token_cache["access_token"] = new_access_token
        raw_new_refresh = resp_data.get("refresh_token")
        new_refresh = raw_new_refresh.strip() if isinstance(raw_new_refresh, six.string_types) else ""
        if new_refresh:
            token_cache["refresh_token"] = new_refresh
        token_cache["expires_at"] = time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() + expires_in)
        )

        # SDK never writes the SSO cache file; bp cli remains the single writer.
        return new_access_token

    def _fetch_role_credentials(self, access_token):
        try:
            from urllib.parse import urlencode
        except ImportError:
            from urllib import urlencode

        portal_url = "{}/federation/credentials?{}".format(
            _PORTAL_BASE_URL_TEMPLATE.format(self._region),
            urlencode({"account_id": self._account_id, "role_name": self._role_name}),
        )

        # Late imports to avoid circular deps (auth.providers is imported
        # indirectly by byteplussdkcore/__init__.py).
        from byteplussdkcore import ApiClient, Configuration
        resp_body = ApiClient(Configuration())._do_http_request(
            portal_url,
            method="GET",
            headers={
                "Accept": "application/json",
                _PORTAL_ACCESS_TOKEN_HEADER: access_token,
            },
            timeout=_HTTP_TIMEOUT,
            max_retries=_HTTP_MAX_RETRIES,
            retry_interval=_HTTP_RETRY_INTERVAL,
            request_name="Portal GetRoleCredentials",
            provider_name=self.PROVIDER_NAME,
        )

        try:
            resp_data = json.loads(resp_body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse Portal response: {}".format(
                    self.PROVIDER_NAME, e
                )
            )

        result = resp_data.get("Result") or resp_data.get("result") or {}
        role_creds = result.get("RoleCredentials") or result.get("roleCredentials") or {}

        ak = (role_creds.get("AccessKeyId") or "").strip()
        sk = (role_creds.get("SecretAccessKey") or "").strip()
        token = (role_creds.get("sessionToken") or role_creds.get("SessionToken") or "").strip()

        if not ak or not sk:
            meta = resp_data.get("ResponseMetadata", {})
            err = meta.get("Error", {})
            if err:
                raise RuntimeError(
                    "{}: Portal API error: {} - {}".format(
                        self.PROVIDER_NAME,
                        err.get("Code", ""),
                        err.get("Message", ""),
                    )
                )
            raise RuntimeError(
                "{}: Portal response missing AccessKeyId/SecretAccessKey.".format(
                    self.PROVIDER_NAME
                )
            )

        expiration = role_creds.get("Expiration", 0)
        if expiration and expiration > 0:
            self._expiration = _unix_timestamp_to_epoch(expiration)
        else:
            self._expiration = None

        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=token or None,
            provider_name=self.PROVIDER_NAME,
        )
