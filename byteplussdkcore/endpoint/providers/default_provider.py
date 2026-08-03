# coding=utf-8
import os
import warnings

from byteplussdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint
from byteplussdkcore.observability.debugger import sdk_core_logger

open_prefix = 'open'
endpoint_suffix = '.byteplusapi.com'
dualstack_endpoint_suffix = '.byteplus-api.com'


class ServiceEndpointInfoMissingError(Exception):
    """Raised when a service is not registered in ``default_endpoint``.

    Mirrors Go's ``ErrServiceEndpointInfoMissing`` and Java's ``ApiException``
    thrown by ``DefaultEndpointProvider.getDefaultEndpointByServiceInfo`` for
    the same condition.
    """

    def __init__(self, service):
        self.service = service
        super(ServiceEndpointInfoMissingError, self).__init__(
            "byteplussdkcore: service endpoint info missing: service {!r} "
            "not registered".format(service)
        )

region_code_cn_beijing_auto_driving = "cn-beijing-autodriving"
region_code_ap_southeast2 = "ap-southeast-2"
region_code_ap_southeast3 = "ap-southeast-3"
region_code_cn_hongkong = 'cn-hongkong'

# Region-level whitelist of cn-* regions that should resolve to the
# international ``.byteplusapi.com`` suffix rather than the Chinese mainland
# ``.byteplusapi.com.cn`` suffix.
_cn_non_mainland_region_set = {region_code_cn_hongkong}


def _normalize_region(region):
    if region is None:
        return ''
    return region.strip().lower()


def _is_cn_mainland_region(region):
    """Returns whether ``region`` is a mainland cn-* region resolving to the
    ``.byteplusapi.com.cn`` suffix. Regions in :data:`_cn_non_mainland_region_set`
    (for example ``cn-hongkong``) are treated as international.
    """
    if not region.startswith('cn-'):
        return False
    return region not in _cn_non_mainland_region_set


class ServiceEndpointInfo:

    def __init__(self, service, is_global, go_china_enabled=False,
                 global_endpoint='', region_endpoint_map=None):
        self.service = service
        self.is_global = is_global
        self.go_china_enabled = go_china_enabled
        # Optional overrides retained for ``custom_endpoints`` callers. The
        # built-in ``default_endpoint`` table intentionally leaves them empty
        # and drives resolution off ``is_global`` + ``go_china_enabled``, in
        # line with the Go/Java ``ServiceEndpointInfo`` shape.
        self.global_endpoint = global_endpoint
        self.region_endpoint_map = region_endpoint_map or {}

    @property
    def __standardize_domain_service_code(self):
        return self.service.lower().replace('_', '-')

    def get_endpoint_for(self, region, suffix=endpoint_suffix):
        sdk_core_logger.debug_endpoint(
            "get_endpoint_for start: service=%s, region=%s, suffix=%s",
            self.service, region, suffix
        )

        normalized_region = _normalize_region(region)
        cn_suffix = '.cn' if (self.go_china_enabled
                              and _is_cn_mainland_region(normalized_region)) else ''

        if self.is_global:
            if self.global_endpoint:
                sdk_core_logger.debug_endpoint(
                    "use global endpoint: service=%s, endpoint=%s",
                    self.service, self.global_endpoint
                )
                return self.global_endpoint
            endpoint = self.__standardize_domain_service_code + suffix + cn_suffix
            sdk_core_logger.debug_endpoint(
                "build global endpoint from service code: %s", endpoint
            )
            return endpoint

        if normalized_region in self.region_endpoint_map:
            endpoint = self.region_endpoint_map[normalized_region]
            sdk_core_logger.debug_endpoint(
                "use region endpoint from map: service=%s, region=%s, endpoint=%s",
                self.service, region, endpoint
            )
            return endpoint

        endpoint = (self.__standardize_domain_service_code + '.'
                    + normalized_region + suffix + cn_suffix)
        sdk_core_logger.debug_endpoint(
            "build region endpoint by default rule: %s", endpoint
        )
        return endpoint


default_endpoint = {
    'vpc': ServiceEndpointInfo('vpc', False, True),
    'vke': ServiceEndpointInfo('vke', False, True),
    'auto_scaling': ServiceEndpointInfo('auto_scaling', False, True),
    'storage_ebs': ServiceEndpointInfo('storage_ebs', False, True),
    'vedbm': ServiceEndpointInfo('vedbm', False, True),
    'privatelink': ServiceEndpointInfo('privatelink', False, True),
    'clb': ServiceEndpointInfo('clb', False, True),
    'transitrouter': ServiceEndpointInfo('transitrouter', False, True),
    'directconnect': ServiceEndpointInfo('directconnect', False, True),
    'vpn': ServiceEndpointInfo('vpn', False, True),
    'natgateway': ServiceEndpointInfo('natgateway', False, True),
    'rds_mysql': ServiceEndpointInfo('rds_mysql', False, True),
    'smc': ServiceEndpointInfo('smc', True, False),
    'iam': ServiceEndpointInfo('iam', True, True),
    'vepfs': ServiceEndpointInfo('vepfs', False, True),
    'kms': ServiceEndpointInfo('kms', False, True),
    'ecs': ServiceEndpointInfo('ecs', False, True),
    'mongodb': ServiceEndpointInfo('mongodb', False, True),
    'private_zone': ServiceEndpointInfo('private_zone', True, True),
    'rds_postgresql': ServiceEndpointInfo('rds_postgresql', False, True),
    'resource_share': ServiceEndpointInfo('resource_share', True, False),
    'vmp': ServiceEndpointInfo('vmp', False, True),
    'tag': ServiceEndpointInfo('tag', True, False),
    'cr': ServiceEndpointInfo('cr', False, True),
    'alb': ServiceEndpointInfo('alb', False, True),
    'sts': ServiceEndpointInfo('sts', False, True),
    'hbase': ServiceEndpointInfo('hbase', False, True),
    'rds_mssql': ServiceEndpointInfo('rds_mssql', False, True),
    'ml_platform': ServiceEndpointInfo('ml_platform', False, False),
    'apig': ServiceEndpointInfo('apig', False, False),
    'ark': ServiceEndpointInfo('ark', False, False),
    'waf': ServiceEndpointInfo('waf', True, False),
    'quota': ServiceEndpointInfo('quota', True, False),
    'dms': ServiceEndpointInfo('dms', False, True),
    'vefaas': ServiceEndpointInfo('vefaas', False, False),
    'cen': ServiceEndpointInfo('cen', True, False),
    'cp': ServiceEndpointInfo('cp', False, False),
    'cloudmonitor': ServiceEndpointInfo('cloudmonitor', False, True),
    'eco_partner': ServiceEndpointInfo('eco_partner', True, False),
    'milvus': ServiceEndpointInfo('milvus', False, False),
    'llmshield': ServiceEndpointInfo('llmshield', False, False),
    'billing': ServiceEndpointInfo('billing', True, True),
    'id': ServiceEndpointInfo('id', False, False),
    'clawsentry': ServiceEndpointInfo('clawsentry', False, False),
    'resourcecenter': ServiceEndpointInfo('resourcecenter', True, False),
    'escloud': ServiceEndpointInfo('escloud', False, False),
    'cpaas': ServiceEndpointInfo('cpaas', True, False),
    'filenas': ServiceEndpointInfo('filenas', False, True),
    'kafka': ServiceEndpointInfo('kafka', False, True),
    'kickart': ServiceEndpointInfo('kickart', True, False),
    'rabbitmq': ServiceEndpointInfo('rabbitmq', False, False),
    'redis': ServiceEndpointInfo('redis', False, True),
    'vod': ServiceEndpointInfo('vod', False, False),
    'vs': ServiceEndpointInfo('vs', True, False),
}


class DefaultEndpointProvider(EndpointProvider):

    def __init__(self, custom_endpoints=None):
        self.custom_endpoints = custom_endpoints or {}

    def get_default_endpoint(self, service, region, suffix=endpoint_suffix):
        sdk_core_logger.debug_endpoint(
            "get_default_endpoint: service=%s, region=%s, suffix=%s",
            service, region, suffix
        )
        if service not in default_endpoint:
            sdk_core_logger.debug_endpoint(
                "service %s not registered in default_endpoint", service
            )
            raise ServiceEndpointInfoMissingError(service)

        e = default_endpoint[service]
        endpoint = e.get_endpoint_for(region, suffix)
        sdk_core_logger.debug_endpoint(
            "resolved default endpoint: service=%s, endpoint=%s",
            service, endpoint
        )
        return endpoint

    @staticmethod
    def __has_enabled_dualstack(use_dual_stack):
        if use_dual_stack is None:
            return os.getenv("BYTEPLUS_ENABLE_DUALSTACK") == 'true'
        return use_dual_stack

    def endpoint_for(self, service, region, custom_bootstrap_region=None, use_dual_stack=None, **kwargs):
        sdk_core_logger.debug_endpoint(
            "endpoint_for called: service=%s, region=%s, custom_bootstrap_region=%s, use_dual_stack=%s",
            service, region, custom_bootstrap_region, use_dual_stack
        )

        # custom_bootstrap_region is deprecated and no longer participates in
        # addressing. Retained in the signature for API compatibility.
        if custom_bootstrap_region:
            warnings.warn(
                'custom_bootstrap_region is deprecated and no longer affects '
                'endpoint resolution; the value is ignored.',
                DeprecationWarning,
                stacklevel=2,
            )

        if service in self.custom_endpoints:
            conf = self.custom_endpoints[service]
            host = conf.get_endpoint_for(region)
            sdk_core_logger.debug_endpoint(
                "use custom endpoint: service=%s, region=%s, host=%s",
                service, region, host
            )
            return ResolvedEndpoint(host)

        suffix = dualstack_endpoint_suffix if self.__has_enabled_dualstack(use_dual_stack) else endpoint_suffix

        host = self.get_default_endpoint(service=service, region=region, suffix=suffix)

        sdk_core_logger.debug_endpoint(
            "final resolved endpoint: service=%s, region=%s, host=%s",
            service, region, host
        )

        return ResolvedEndpoint(host)


class HostEndpointProvider(EndpointProvider):
    def __init__(self, host):
        self.host = host

    def endpoint_for(self, service, region, **kwargs):
        sdk_core_logger.debug_endpoint(
            "HostEndpointProvider.endpoint_for: service=%s, region=%s, host=%s",
            service, region, self.host
        )
        return ResolvedEndpoint(self.host)
