# coding=utf-8
import os

from .provider import Provider, CredentialValue


class EnvironmentVariableCredentialProvider(Provider):
    PROVIDER_NAME = "EnvironmentVariableCredentialProvider"

    def retrieve(self):
        return self.get_credentials()

    def is_expired(self):
        return False

    def refresh(self):
        return

    def get_credentials(self):
        ak = os.environ.get("BYTEPLUS_ACCESSKEY") or os.environ.get("BYTEPLUS_ACCESS_KEY")
        sk = os.environ.get("BYTEPLUS_SECRETKEY") or os.environ.get("BYTEPLUS_SECRET_KEY")

        if not ak or not sk:
            raise RuntimeError(
                "{}: unable to resolve credentials from environment variables. "
                "Please set BYTEPLUS_ACCESSKEY and BYTEPLUS_SECRETKEY.".format(
                    self.PROVIDER_NAME
                )
            )

        session_token = os.environ.get("BYTEPLUS_SESSION_TOKEN")

        return CredentialValue(
            ak=ak,
            sk=sk,
            session_token=session_token if session_token else None,
            provider_name=self.PROVIDER_NAME,
        )
