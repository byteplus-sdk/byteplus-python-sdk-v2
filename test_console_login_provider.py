# coding=utf-8
import json
import os
import tempfile
import threading
import time
import unittest

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import parse_qs
except ImportError:  # pragma: no cover - Python 2 compatibility
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    from urlparse import parse_qs

from byteplussdkcore.auth.providers.console_login_provider import ConsoleLoginCredentialProvider


class _TokenHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8")
        form = dict((k, v[0]) for k, v in parse_qs(body).items())
        self.server.requests.append({
            "path": self.path,
            "content_type": self.headers.get("Content-Type"),
            "form": form,
        })
        status, payload = self.server.on_request(form)
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        return


def _start_token_server(on_request):
    server = HTTPServer(("127.0.0.1", 0), _TokenHandler)
    server.on_request = on_request
    server.requests = []
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    return server


def _cache_payload(login_session, access_key, refresh_token, endpoint_url):
    return {
        "login_session": login_session,
        "access_token": {
            "access_key_id": access_key,
            "secret_access_key": access_key,
            "session_token": access_key,
        },
        "refresh_token": refresh_token,
        "scope": "Console:All:All",
        "client_id": "trn:signin:::devtools/same-device",
        "endpoint_url": endpoint_url,
        "issued_at": time.strftime(
            "%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - 3600)
        ),
        "expires_in": 1,
        "token_type": "urn:ietf:params:oauth:token-type:access_token_sts",
    }


def _write_cache(path, payload):
    with open(path, "w") as f:
        json.dump(payload, f, separators=(",", ":"))


class ConsoleLoginCredentialProviderTest(unittest.TestCase):
    def setUp(self):
        self._old_no_proxy = os.environ.get("NO_PROXY")
        os.environ["NO_PROXY"] = "127.0.0.1,localhost"

    def tearDown(self):
        if self._old_no_proxy is None:
            os.environ.pop("NO_PROXY", None)
        else:
            os.environ["NO_PROXY"] = self._old_no_proxy

    def test_refresh_uses_form_post_without_rewriting_cache(self):
        temp_dir = tempfile.mkdtemp()
        cache_path = os.path.join(temp_dir, "console-cache.json")

        def on_request(form):
            self.assertEqual("refresh_token", form.get("grant_type"))
            self.assertEqual("old-refresh", form.get("refresh_token"))
            self.assertEqual(
                "trn:signin:::devtools/same-device", form.get("client_id")
            )
            self.assertEqual("Console:All:All", form.get("scope"))
            return 200, {
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
            }

        server = _start_token_server(on_request)
        try:
            endpoint_url = "http://127.0.0.1:{}".format(server.server_port)
            _write_cache(
                cache_path,
                _cache_payload("sess-python", "OLD", "old-refresh", endpoint_url),
            )
            with open(cache_path, "r") as f:
                before = f.read()

            provider = ConsoleLoginCredentialProvider(
                login_session="sess-python",
                cache_path=cache_path,
            )
            value = provider.retrieve()

            self.assertEqual("NEW", value.ak)
            self.assertEqual("SECRET", value.sk)
            self.assertEqual("TOKEN", value.session_token)
            self.assertEqual(1, len(server.requests))
            self.assertEqual("/authorize/oauth/token", server.requests[0]["path"])
            self.assertEqual(
                "application/x-www-form-urlencoded",
                server.requests[0]["content_type"],
            )
            with open(cache_path, "r") as f:
                self.assertEqual(before, f.read())
        finally:
            server.shutdown()
            server.server_close()

    def test_invalid_grant_reloads_disk_cache(self):
        temp_dir = tempfile.mkdtemp()
        cache_path = os.path.join(temp_dir, "console-cache.json")
        login_session = "sess-python-invalid-grant"

        def on_request(form):
            endpoint_url = "http://127.0.0.1:{}".format(server.server_port)
            if form.get("refresh_token") == "old-refresh":
                _write_cache(
                    cache_path,
                    _cache_payload(login_session, "OLD", "new-refresh", endpoint_url),
                )
                return 400, {
                    "error": "invalid_grant",
                    "error_description": "refresh token expired",
                }
            if form.get("refresh_token") == "new-refresh":
                return 200, {
                    "access_token": json.dumps({
                        "access_key_id": "FALLBACKAK",
                        "secret_access_key": "FALLBACKSK",
                        "session_token": "FALLBACKTOKEN",
                    }),
                    "refresh_token": "rotated-refresh",
                    "token_type": "urn:ietf:params:oauth:token-type:access_token_sts",
                    "expires_in": 900,
                    "scope": "Console:All:All",
                }
            self.fail("unexpected refresh_token: {}".format(form.get("refresh_token")))

        server = _start_token_server(on_request)
        try:
            endpoint_url = "http://127.0.0.1:{}".format(server.server_port)
            _write_cache(
                cache_path,
                _cache_payload(login_session, "OLD", "old-refresh", endpoint_url),
            )

            provider = ConsoleLoginCredentialProvider(
                login_session=login_session,
                cache_path=cache_path,
            )
            value = provider.retrieve()

            self.assertEqual("FALLBACKAK", value.ak)
            self.assertEqual("FALLBACKSK", value.sk)
            self.assertEqual("FALLBACKTOKEN", value.session_token)
            self.assertEqual(2, len(server.requests))
            with open(cache_path, "r") as f:
                disk = f.read()
            self.assertIn('"refresh_token":"new-refresh"', disk)
            self.assertNotIn("rotated-refresh", disk)
            self.assertNotIn("FALLBACKAK", disk)
        finally:
            server.shutdown()
            server.server_close()


if __name__ == "__main__":
    unittest.main()
