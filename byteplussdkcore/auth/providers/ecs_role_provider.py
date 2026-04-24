# coding=utf-8
import json
import logging
import os
import threading
import time
from datetime import datetime

import dateutil.parser
import dateutil.tz

from .provider import Provider, CredentialValue

logger = logging.getLogger(__name__)

# ECS IMDSv2 endpoint and protocol
_IMDS_ENDPOINT = "http://100.96.0.96"
_IMDS_CREDENTIALS_PATH = "/volcstack/latest/iam/security_credentials/{role_name}"  # POST
_IMDS_ROLE_NAME_PATH = "/volcstack/latest/iam/security_credentials?type=user"  # GET
_IMDS_TOKEN_PATH = "/latest/api/token"  # GET

# ECS IMDSv2 headers
_IMDS_TOKEN_TTL_HEADER = "X-volc-ecs-metadata-token-ttl-seconds"
_IMDS_TOKEN_HEADER = "X-volc-ecs-metadata-token"
_IMDS_TOKEN_TTL_SECONDS = "21600"  # 6 hours

# ECS IMDSv2 response field names
_FIELD_AK = "AccessKeyId"
_FIELD_SK = "SecretAccessKey"
_FIELD_TOKEN = "SessionToken"
_FIELD_EXPIRATION = "ExpiredTime"


class EcsRoleCredentialProvider(Provider):
    PROVIDER_NAME = "EcsRoleCredentialProvider"

    def __init__(self, role_name=None, connect_timeout=1, read_timeout=1,
                 max_retries=3, retry_interval=1, expired_buffer_seconds=300):
        self._role_name = role_name
        self._connect_timeout = connect_timeout
        self._read_timeout = read_timeout
        self._max_retries = max(max_retries, 1)
        self._retry_interval = retry_interval
        self._expired_buffer_seconds = expired_buffer_seconds

        self._credentials = None
        self._expired_time = None
        self._lock = threading.Lock()

    def retrieve(self):
        return self._credentials

    def is_expired(self):
        return (self._credentials is None or
                (self._expired_time is not None
                 and self._expired_time < time.time() + self._expired_buffer_seconds))

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._refresh_credentials()

    def get_credentials(self):
        disabled = os.environ.get("BYTEPLUS_ECS_METADATA_DISABLED", "").lower()
        if disabled == "true":
            raise RuntimeError(
                "{}: IMDS is disabled via BYTEPLUS_ECS_METADATA_DISABLED=true.".format(
                    self.PROVIDER_NAME
                )
            )
        self.refresh()
        return self._credentials

    def _get_imdsv2_token(self):
        url = _IMDS_ENDPOINT + _IMDS_TOKEN_PATH
        headers = {_IMDS_TOKEN_TTL_HEADER: _IMDS_TOKEN_TTL_SECONDS}
        body = self._do_request(url, method="GET", extra_headers=headers)
        token = body.strip()
        if not token:
            raise RuntimeError(
                "{}: IMDSv2 token endpoint returned empty response.".format(
                    self.PROVIDER_NAME
                )
            )
        return token

    def _resolve_role_name(self, imds_token):
        if self._role_name:
            return self._role_name

        env_role = os.environ.get("BYTEPLUS_ECS_METADATA", "").strip()
        if env_role:
            return env_role

        return self._auto_detect_role_name(imds_token)

    def _auto_detect_role_name(self, imds_token):
        url = _IMDS_ENDPOINT + _IMDS_ROLE_NAME_PATH
        headers = {_IMDS_TOKEN_HEADER: imds_token}
        body = self._do_request(url, method="GET", extra_headers=headers)

        try:
            roles = json.loads(body)
        except ValueError:
            roles = [r.strip() for r in body.strip().split('\n') if r.strip()]

        if isinstance(roles, list):
            roles = [r.strip() if isinstance(r, str) else str(r) for r in roles if r]
        else:
            raise RuntimeError(
                "{}: unexpected role list response format: {}".format(
                    self.PROVIDER_NAME, type(roles).__name__
                )
            )

        if not roles:
            raise RuntimeError(
                "{}: no IAM roles found via IMDS.".format(self.PROVIDER_NAME)
            )

        if len(roles) > 1:
            logger.warning(
                "%s: multiple IAM roles found via IMDS: %s. Using the first one '%s'. "
                "Set BYTEPLUS_ECS_METADATA or pass role_name explicitly to avoid ambiguity.",
                self.PROVIDER_NAME, roles, roles[0],
            )

        return roles[0]

    def _refresh_credentials(self):
        imds_token = self._get_imdsv2_token()
        role_name = self._resolve_role_name(imds_token)

        url = _IMDS_ENDPOINT + _IMDS_CREDENTIALS_PATH.format(role_name=role_name)
        headers = {_IMDS_TOKEN_HEADER: imds_token}
        body = self._do_request(url, method="POST", extra_headers=headers)

        try:
            data = json.loads(body)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse IMDS response: {}".format(self.PROVIDER_NAME, e)
            )

        ak = data.get(_FIELD_AK)
        sk = data.get(_FIELD_SK)
        token = data.get(_FIELD_TOKEN)
        expiration_str = data.get(_FIELD_EXPIRATION)

        if not ak or not sk:
            raise RuntimeError(
                "{}: IMDS response missing required credential fields.".format(
                    self.PROVIDER_NAME
                )
            )

        if expiration_str:
            dt = dateutil.parser.parse(expiration_str)
            self._expired_time = (
                dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())
            ).total_seconds()
        else:
            self._expired_time = None

        self._credentials = CredentialValue(
            ak=ak,
            sk=sk,
            session_token=token,
            provider_name=self.PROVIDER_NAME,
        )

    def _do_request(self, url, method="GET", extra_headers=None):
        timeout = self._connect_timeout + self._read_timeout
        return self._do_http_request(
            url=url,
            method=method,
            headers=extra_headers,
            timeout=timeout,
            max_retries=self._max_retries,
            retry_interval=self._retry_interval,
            request_name="IMDS request",
        )
