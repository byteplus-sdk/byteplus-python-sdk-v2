# coding=utf-8
import json
import os
import tempfile
import time
import unittest

import byteplussdkcore
from byteplussdkcore.auth.providers.cli_config_provider import (
    SsoCredentialProvider,
    _token_cache_filename,
)


def _write_json(path, payload):
    with open(path, "w") as f:
        json.dump(payload, f, separators=(",", ":"))


class _FakeApiClient(object):
    requests = []

    def __init__(self, configuration):
        self.configuration = configuration

    def _do_http_request(self, url, method="GET", data=None, headers=None, **kwargs):
        self.requests.append({
            "url": url,
            "method": method,
            "data": data,
            "headers": headers or {},
        })
        if "cloudidentity-oauth" in url and method == "POST":
            if data.get("grant_type") != "refresh_token":
                raise AssertionError("unexpected grant_type: {}".format(data))
            if data.get("refresh_token") != "old-refresh":
                raise AssertionError("unexpected refresh_token: {}".format(data))
            return json.dumps({
                "access_token": "new-sso-access",
                "refresh_token": "new-refresh",
                "expires_in": 900,
            })
        if "cloudidentity-portal" in url and method == "GET":
            token = (headers or {}).get("x-bd-cloudidentity-bearer-token")
            if token != "new-sso-access":
                raise AssertionError("portal did not use refreshed access token")
            return json.dumps({
                "ResponseMetadata": {"RequestId": "req-sso"},
                "Result": {
                    "RoleCredentials": {
                        "AccessKeyId": "AKIA_SSO",
                        "SecretAccessKey": "SECRET_SSO",
                        "SessionToken": "SESSION_SSO",
                        "Expiration": int(time.time()) + 900,
                    }
                },
            })
        raise AssertionError("unexpected request: {} {}".format(method, url))


class SsoCredentialProviderTest(unittest.TestCase):
    def test_refresh_does_not_rewrite_token_cache(self):
        temp_dir = tempfile.mkdtemp()
        start_url = "https://signin.byteplus.com/sso/start"
        session_name = "default"
        token_path = os.path.join(temp_dir, _token_cache_filename(start_url, session_name))
        payload = {
            "start_url": start_url,
            "session_name": session_name,
            "region": "ap-southeast-1",
            "client_id": "client-id",
            "client_secret": "client-secret",
            "client_secret_expires_at": int(time.time()) + 3600,
            "access_token": "old-access",
            "refresh_token": "old-refresh",
            "expires_at": time.strftime(
                "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 60)
            ),
        }
        _write_json(token_path, payload)
        with open(token_path, "r") as f:
            before = f.read()

        old_client = byteplussdkcore.ApiClient
        _FakeApiClient.requests = []
        byteplussdkcore.ApiClient = _FakeApiClient
        try:
            provider = SsoCredentialProvider(
                profile={},
                start_url=start_url,
                session_name=session_name,
                region="ap-southeast-1",
                account_id="2100000000",
                role_name="Admin",
                cache_dir=temp_dir,
            )
            value = provider.retrieve()
        finally:
            byteplussdkcore.ApiClient = old_client

        self.assertEqual("AKIA_SSO", value.ak)
        self.assertEqual("SECRET_SSO", value.sk)
        self.assertEqual("SESSION_SSO", value.session_token)
        self.assertEqual(2, len(_FakeApiClient.requests))
        with open(token_path, "r") as f:
            self.assertEqual(before, f.read())


if __name__ == "__main__":
    unittest.main()
