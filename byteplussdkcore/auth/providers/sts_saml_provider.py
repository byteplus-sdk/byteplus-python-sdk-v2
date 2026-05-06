import threading
import time
import uuid
from datetime import datetime

import dateutil.parser
import dateutil.tz

from .provider import Provider, CredentialValue


class AssumeRoleSamlCredentials:
    def __init__(self, ak, sk, session_token, current_time, expired_time):
        self.ak = ak
        self.sk = sk
        self.session_token = session_token
        self.current_time = current_time
        self.expired_time = expired_time


class StsSamlCredentialProvider(Provider):
    PROVIDER_NAME = "StsSamlCredentialProvider"

    def __init__(self, role_name=None, account_id=None, provider_name=None, saml_resp=None,
                 duration_seconds=3600, scheme='https',
                 host='sts.ap-southeast-1.byteplusapi.com', region='.ap-southeast-1', timeout=30, expired_buffer_seconds=60,
                 policy=None, role_trn=None, saml_provider_trn=None, max_retries=3, retry_interval=1):
        self.role_name = role_name
        self.account_id = account_id
        self.provider_name = provider_name
        self.saml_resp = saml_resp

        if role_trn:
            self._role_trn = role_trn
        elif role_name and account_id:
            self._role_trn = 'trn:iam::' + account_id + ':role/' + role_name
        else:
            self._role_trn = None

        if saml_provider_trn:
            self._saml_provider_trn = saml_provider_trn
        elif provider_name:
            resolved_account_id = account_id or self._extract_account_id_from_role_trn(self._role_trn)
            if resolved_account_id:
                self._saml_provider_trn = 'trn:iam::' + resolved_account_id + ':saml-provider/' + provider_name
            else:
                self._saml_provider_trn = None
        else:
            self._saml_provider_trn = None

        self.timeout = timeout
        self.max_retries = max(max_retries, 1)
        self.retry_interval = retry_interval
        self.duration_seconds = duration_seconds

        self.host = host
        self.region = region
        self.scheme = scheme
        self.policy = policy

        self.expired_time = None
        if expired_buffer_seconds > 600:
            raise ValueError('expired_buffer_seconds must be less than or equal to 600')
        self.expired_buffer_seconds = expired_buffer_seconds

        self.credentials = None

        self._lock = threading.Lock()

    def retrieve(self):
        return self.credentials

    def is_expired(self):
        return (self.credentials is None or
                (self.expired_time and self.expired_time < time.time() + self.expired_buffer_seconds))

    def refresh(self):
        with self._lock:
            if self.is_expired():
                self._assume_role_saml()

    def get_credentials(self):
        self.refresh()
        return self.credentials

    @staticmethod
    def _extract_account_id_from_role_trn(role_trn):
        if not role_trn:
            return None
        parts = role_trn.split(':')
        if len(parts) >= 4 and parts[0] == 'trn' and parts[1] == 'iam' and parts[3]:
            return parts[3]
        return None

    def _assume_role_saml(self):
        if not self._role_trn:
            raise RuntimeError(
                "{}: role_trn not provided. Set role_trn or (role_name + account_id).".format(self.PROVIDER_NAME)
            )
        if not self._saml_provider_trn:
            raise RuntimeError(
                "{}: saml_provider_trn not provided. "
                "Set saml_provider_trn, or (account_id + provider_name), "
                "or (role_trn + provider_name).".format(self.PROVIDER_NAME)
            )
        if not self.saml_resp:
            raise RuntimeError(
                "{}: saml_resp is required.".format(self.PROVIDER_NAME)
            )

        params = {
            'DurationSeconds': self.duration_seconds,
            'RoleSessionName': uuid.uuid4().hex,
            'RoleTrn': self._role_trn,
            'SAMLProviderTrn': self._saml_provider_trn,
            'SAMLResp': self.saml_resp,
        }
        if self.policy is not None:
            params['Policy'] = self.policy
        from byteplussdkcore import ApiClient, Configuration
        resp_result = ApiClient(Configuration())._sts_call(
            action='AssumeRoleWithSAML',
            version='2018-01-01',
            params=params,
            host=self.host,
            scheme=self.scheme,
            region=self.region,
            timeout=self.timeout,
            max_retries=self.max_retries,
            retry_interval=self.retry_interval,
            provider_name=self.PROVIDER_NAME,
        )
        if 'Credentials' not in resp_result:
            raise RuntimeError(
                'failed to retrieve credentials from sts: {}:{}'.format(
                    self.PROVIDER_NAME, str(resp_result)
                )
            )
        resp_cred = resp_result['Credentials']

        dt = dateutil.parser.parse(resp_cred.get('Expiration', resp_cred.get('ExpiredTime')))
        self.expired_time = (dt - datetime(1970, 1, 1, tzinfo=dateutil.tz.tzutc())).total_seconds()

        self.credentials = CredentialValue(ak=resp_cred['AccessKeyId'],
                                           sk=resp_cred['SecretAccessKey'],
                                           session_token=resp_cred['SessionToken'],
                                           provider_name='StsSamlCredentialProvider')
