# coding=utf-8
import os
import warnings

from byteplussdkcore.endpoint.endpoint_provider import EndpointProvider, ResolvedEndpoint
from byteplussdkcore.observability.debugger import sdk_core_logger

open_prefix = 'open'
endpoint_suffix = '.byteplusapi.com'
dualstack_endpoint_suffix = '.byteplus-api.com'
fallback_endpoint = open_prefix + '.ap-southeast-1.byteplusapi.com'

region_code_cn_beijing_auto_driving = "cn-beijing-autodriving"
region_code_ap_southeast2 = "ap-southeast-2"
region_code_ap_southeast3 = "ap-southeast-3"
region_code_cn_hongkong = 'cn-hongkong'

bootstrap_region = {
    region_code_ap_southeast2: {},
    region_code_ap_southeast3: {},
}


class ServiceEndpointInfo:

    def __init__(self, service, is_global, global_endpoint,
                 region_endpoint_map, fallback_endpoint=fallback_endpoint):
        self.service = service
        self.is_global = is_global
        self.global_endpoint = global_endpoint
        self.region_endpoint_map = region_endpoint_map
        self.fallback_endpoint = fallback_endpoint

    @property
    def __standardize_domain_service_code(self):
        return self.service.lower().replace('_', '-')

    @staticmethod
    def __is_cn_region(region):
        has_cn_prefix = region.startswith('cn-')
        if not has_cn_prefix:
            return False

        cn_none_mainland_region = [region_code_cn_hongkong]
        return region not in cn_none_mainland_region

    def get_endpoint_for(self, region, suffix=endpoint_suffix):
        sdk_core_logger.debug_endpoint(
            "get_endpoint_for start: service=%s, region=%s, suffix=%s",
            self.service, region, suffix
        )
        if self.is_global:
            if self.global_endpoint:
                sdk_core_logger.debug_endpoint(
                    "use global endpoint: service=%s, endpoint=%s",
                    self.service, self.global_endpoint
                )
                return self.global_endpoint
            endpoint = self.__standardize_domain_service_code + suffix
            sdk_core_logger.debug_endpoint(
                "build global endpoint from service code: %s", endpoint
            )
            return endpoint
        if region in self.region_endpoint_map:
            endpoint = self.region_endpoint_map[region]
            sdk_core_logger.debug_endpoint(
                "use region endpoint from map: service=%s, region=%s, endpoint=%s",
                self.service, region, endpoint
            )
            return endpoint

        endpoint = self.__standardize_domain_service_code + '.' + region + suffix + \
            ('.cn' if self.__is_cn_region(region) else '')
        sdk_core_logger.debug_endpoint(
            "build region endpoint by default rule: %s", endpoint
        )

        return endpoint


default_endpoint = {
    'ark': ServiceEndpointInfo(
        service='ark',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=open_prefix + endpoint_suffix,
    ),
    'billing': ServiceEndpointInfo(
        service='billing',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=open_prefix + endpoint_suffix,
    ),
    'ecs': ServiceEndpointInfo(
        service='ecs',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=fallback_endpoint,
    ),
    'vpc': ServiceEndpointInfo(
        service='vpc',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=fallback_endpoint,
    ),
    'kms': ServiceEndpointInfo(
        service='kms',
        is_global=False,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=fallback_endpoint,
    ),
    'eco_partner': ServiceEndpointInfo(
        service='eco_partner',
        is_global=True,
        global_endpoint='',
        region_endpoint_map={},
        fallback_endpoint=fallback_endpoint,
    ),
}


class DefaultEndpointProvider(EndpointProvider):

    def __init__(self, custom_endpoints=None):
        self.custom_endpoints = custom_endpoints or {}

    def get_default_endpoint(self, service, region, suffix=endpoint_suffix):
        sdk_core_logger.debug_endpoint(
            "get_default_endpoint: service=%s, region=%s, suffix=%s",
            service, region, suffix
        )
        if service in default_endpoint:
            e = default_endpoint[service]
            endpoint = e.get_endpoint_for(region, suffix)
            sdk_core_logger.debug_endpoint(
                "resolved default endpoint: service=%s, endpoint=%s",
                service, endpoint
            )
            return endpoint

        sdk_core_logger.debug_endpoint(
            "service not found in default_endpoint, use fallback=%s", fallback_endpoint
        )
        return fallback_endpoint

    def __in_bootstrap_region_list(self, region, custom_bootstrap_region):
        region_code = region.strip()
        bs_region_list_path = os.getenv('BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF')
        if bs_region_list_path:
            try:
                with open(bs_region_list_path, 'r') as f:
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        if line == region_code:
                            return True
            except Exception as e:
                warnings.warn(
                    'failed to read bootstrap region list from file ' + bs_region_list_path + ': ' + str(e),
                    Warning,
                    stacklevel=2
                )

        if bootstrap_region:
            if region_code in bootstrap_region:
                return True

        if custom_bootstrap_region:
            return region_code in custom_bootstrap_region

        return False

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
        if service in self.custom_endpoints:
            conf = self.custom_endpoints[service]
            host = conf.get_endpoint_for(region)
            sdk_core_logger.debug_endpoint(
                "use custom endpoint: service=%s, region=%s, host=%s",
                service, region, host
            )
            return ResolvedEndpoint(host)

        if custom_bootstrap_region is None:
            custom_bootstrap_region = {}

        if not self.__in_bootstrap_region_list(region, custom_bootstrap_region):
            if service not in default_endpoint:
                sdk_core_logger.debug_endpoint(
                    "region=%s not in bootstrap list, service not in default endpoint fallback=%s",
                    region, fallback_endpoint
                )
                return ResolvedEndpoint(fallback_endpoint)
            host = default_endpoint[service].fallback_endpoint
            sdk_core_logger.debug_endpoint(
                "region=%s not in bootstrap list, service in default endpoint fallback=%s",
                region, host
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
