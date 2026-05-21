import json
import threading

from byteplussdkcore.signv4 import SignerV4
from .interceptor import RequestInterceptor

_DEFAULT_PROVIDER_INIT_LOCK = threading.Lock()


class SignRequestInterceptor(RequestInterceptor):

    def name(self):
        return 'byteplus-sign-request-interceptor'

    def intercept(self, context):
        # Auto-inject DefaultCredentialProvider when no credentials are configured
        if context.request.credential_provider is None and not context.request.ak and not context.request.sk:
            from byteplussdkcore.auth.providers.default_provider import DefaultCredentialProvider
            provider = getattr(self, '_default_credential_provider', None)
            if provider is None:
                with _DEFAULT_PROVIDER_INIT_LOCK:
                    provider = getattr(self, '_default_credential_provider', None)
                    if provider is None:
                        provider = DefaultCredentialProvider()
                        self._default_credential_provider = provider
            context.request.credential_provider = provider

        # Resolve credentials from provider (STS AssumeRole / OIDC / SAML / default chain)
        if context.request.credential_provider is not None:
            credentials = context.request.credential_provider.get_credentials()
            context.request.ak = credentials.ak
            context.request.sk = credentials.sk
            context.request.session_token = credentials.session_token

        if context.request.is_presign:
            context.request.signed_query = SignerV4.sign_url(
                path=context.request.true_path,
                method=context.request.method,
                query=context.request.query_params,
                ak=context.request.ak,
                sk=context.request.sk,
                region=context.request.region,
                service=context.request.service,
                session_token=context.request.session_token,
                host=context.request.host,
            )
        else:
            self.update_params_for_auth(host=context.request.host, path=context.request.true_path,
                                        method=context.request.method,
                                        headers=context.request.header_params,
                                        querys=context.request.query_params,
                                        auth_settings=context.request.auth_settings,
                                        body=context.request.body,
                                        post_params=context.request.post_params,
                                        service=context.request.service,
                                        ak=context.request.ak,
                                        sk=context.request.sk,
                                        session_token=context.request.session_token,
                                        region=context.request.region)
        return context

    @staticmethod
    def update_params_for_auth(host, path, method, headers, querys, auth_settings, body, post_params, service, ak,
                               sk, session_token, region):
        if not auth_settings:
            return

        for auth in auth_settings:
            headers["Host"] = host
            if method in ["POST", "PUT", "DELETE", "PATCH"] and body is not None:
                body = json.dumps(body)
            else:
                body = ""
            SignerV4.sign(path, method, headers, body, post_params, querys,
                          ak, sk,
                          region, service, session_token)
