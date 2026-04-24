# coding=utf-8
import abc
import json
import logging
import time

logger = logging.getLogger(__name__)


class CredentialValue:
    def __init__(self, ak, sk, session_token, provider_name):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.provider_name = provider_name


class Provider(object):
    PROVIDER_NAME = "Provider"

    @abc.abstractmethod
    def retrieve(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def is_expired(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def refresh(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_credentials(self):
        raise NotImplementedError()

    def _sts_call(self, action, version, params,
                  host=None, scheme='https', region='ap-singapore-1',
                  timeout=30, service='sts',
                  max_retries=3, retry_interval=1):
        """Invoke an STS federation endpoint."""
        from byteplussdkcore import ApiClient, Configuration

        fresh = Configuration()
        fresh.credential_provider = None
        fresh.ak = "_sts_bootstrap_unsigned"
        fresh.sk = "_sts_bootstrap_unsigned"
        fresh.session_token = ""
        if host:
            fresh.host = host
        fresh.scheme = scheme
        fresh.region = region
        fresh.read_timeout = timeout

        import copy
        fresh._Configuration__retryer = copy.deepcopy(fresh.retryer)
        fresh.num_max_retries = max(max_retries - 1, 0)
        delay_ms = int(retry_interval * 1000)
        fresh.min_retry_delay_ms = delay_ms
        fresh.max_retry_delay_ms = delay_ms

        client = ApiClient(fresh)
        resource_path = '/{}/{}/{}/post/'.format(action, version, service)
        return client.call_api(
            resource_path,
            'POST',
            path_params={},
            query_params=[],
            header_params={
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body=params,
            post_params=[],
            files={},
            response_type=object,
            auth_settings=None,
            async_req=False,
            _return_http_data_only=True,
            _preload_content=True,
            collection_formats={},
        )

    def _do_http_request(self, url, method="GET", data=None, headers=None, timeout=None,
                         max_retries=1, retry_interval=0, request_name=None,
                         retry_on_5xx=True):
        from byteplussdkcore import Configuration
        from byteplussdkcore.rest import RESTClientObject, ApiException
        import urllib3

        attempts = max(max_retries, 1)
        rest_client = RESTClientObject(Configuration())

        last_error = None
        for attempt in range(attempts):
            try:
                logger.debug(
                    "%s: RESTClient attempt %d/%d %s %s",
                    self.PROVIDER_NAME, attempt + 1, attempts, method, url,
                )
                r = rest_client.request(
                    method=method,
                    url=url,
                    body=data,
                    headers=headers,
                    _request_timeout=timeout,
                )
                body = r.data
                if isinstance(body, bytes):
                    try:
                        body = body.decode('utf-8')
                    except (UnicodeDecodeError, AttributeError):
                        pass
                return body
            except ApiException as e:
                status = e.status or 0
                err_body = e.body
                if isinstance(err_body, bytes):
                    try:
                        err_body = err_body.decode('utf-8')
                    except (UnicodeDecodeError, AttributeError):
                        err_body = repr(err_body)
                if status == 0:
                    raise RuntimeError(
                        "{}: {} failed at '{}' (transport error): {}".format(
                            self.PROVIDER_NAME, request_name or "request", url, e.reason,
                        )
                    )
                if retry_on_5xx and status >= 500:
                    last_error = RuntimeError(
                        "HTTP {}: {}".format(status, err_body)
                    )
                    logger.debug(
                        "%s: HTTP %s on attempt %d/%d: %s",
                        self.PROVIDER_NAME, status, attempt + 1, attempts, err_body,
                    )
                    if attempt < attempts - 1:
                        time.sleep(retry_interval)
                    continue
                raise RuntimeError(
                    "{}: {} failed with HTTP {}: {}".format(
                        self.PROVIDER_NAME, request_name or "request", status, err_body,
                    )
                )
            except (urllib3.exceptions.HTTPError, IOError, OSError) as e:
                last_error = e
                logger.debug(
                    "%s: transport error on attempt %d/%d: %r",
                    self.PROVIDER_NAME, attempt + 1, attempts, e,
                )
                if attempt < attempts - 1:
                    time.sleep(retry_interval)

        raise RuntimeError(
            "{}: failed to call {} at '{}' after {} retries: {}".format(
                self.PROVIDER_NAME, request_name or "request", url, attempts, last_error,
            )
        )

    def _parse_json_response(self, content, response_name="response"):
        try:
            resp = json.loads(content)
        except ValueError as e:
            raise RuntimeError(
                "{}: failed to parse {} as JSON: {}. raw={}".format(
                    self.PROVIDER_NAME, response_name, e, content
                )
            )

        if not isinstance(resp, dict):
            raise RuntimeError(
                "{}: unexpected {} type: {}".format(
                    self.PROVIDER_NAME, response_name, type(resp).__name__
                )
            )

        return resp

    def _unwrap_result(self, resp, response_name="response"):
        if 'Result' not in resp:
            return resp

        result = resp['Result']
        if not isinstance(result, dict):
            raise RuntimeError(
                "{}: unexpected {}.Result type: {}".format(
                    self.PROVIDER_NAME, response_name, type(result).__name__
                )
            )

        return result
