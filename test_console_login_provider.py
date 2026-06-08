# coding=utf-8
import json
import os
import tempfile
import time
import unittest

from byteplussdkcore import ApiClient
from byteplussdkcore.auth.providers.console_login_provider import ConsoleLoginCredentialProvider


class ConsoleLoginCredentialProviderTest(unittest.TestCase):
    def test_refresh_uses_form_post_params(self):
        temp_dir = tempfile.mkdtemp()
        cache_path = os.path.join(temp_dir, "console-cache.json")
        with open(cache_path, "w") as f:
            json.dump({
                "login_session": "sess-python",
                "access_token": {
                    "access_key_id": "OLD",
                    "secret_access_key": "OLD",
                    "session_token": "OLD",
                },
                "refresh_token": "old-refresh",
                "scope": "Console:All:All",
                "client_id": "trn:signin:::devtools/same-device",
                "endpoint_url": "https://signin.byteplus.com",
                "issued_at": time.strftime(
                    "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 3600)
                ),
                "expires_in": 1,
                "token_type": "urn:ietf:params:oauth:token-type:access_token_sts",
            }, f)

        captured = {}
        original = ApiClient._do_http_request

        def fake_do_http_request(self, url, method="GET", data=None, post_params=None,
                                 headers=None, timeout=None, max_retries=1,
                                 retry_interval=0, request_name=None,
                                 retry_on_5xx=True, provider_name="ApiClient"):
            captured["url"] = url
            captured["method"] = method
            captured["data"] = data
            captured["post_params"] = post_params
            captured["headers"] = headers
            return json.dumps({
                "access_token": json.dumps({
                    "access_key_id": "NEW",
                    "secret_access_key": "SECRET",
                    "session_token": "TOKEN",
                }),
                "refresh_token": "new-refresh",
                "id_token": "new-id-token",
                "token_type": "urn:ietf:params:oauth:token-type:access_token_sts",
                "expires_in": 900,
                "scope": "Console:All:All",
            })

        ApiClient._do_http_request = fake_do_http_request
        try:
            provider = ConsoleLoginCredentialProvider(
                login_session="sess-python",
                cache_path=cache_path,
            )
            value = provider.retrieve()
        finally:
            ApiClient._do_http_request = original

        self.assertEqual("NEW", value.ak)
        self.assertEqual("SECRET", value.sk)
        self.assertEqual("TOKEN", value.session_token)
        self.assertIsNone(captured["data"])
        self.assertEqual("POST", captured["method"])
        self.assertEqual(
            "application/x-www-form-urlencoded",
            captured["headers"]["Content-Type"],
        )
        self.assertEqual("refresh_token", captured["post_params"]["grant_type"])
        self.assertEqual("old-refresh", captured["post_params"]["refresh_token"])
        self.assertEqual(
            "trn:signin:::devtools/same-device",
            captured["post_params"]["client_id"],
        )
        self.assertEqual("Console:All:All", captured["post_params"]["scope"])


if __name__ == "__main__":
    unittest.main()
