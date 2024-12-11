class ServiceEndpointInfo(object):
    def __init__(self, service_name, is_global, global_endpoint, default_endpoint, region_endpoint_map):
        self.service_name = service_name
        self.is_global = is_global
        self.global_endpoint = global_endpoint
        self.default_endpoint = default_endpoint
        self.region_endpoint_map = region_endpoint_map


class DefaultEndpointResolver(object):
    global_endpoint = "open.ap-southeast-1.byteplusapi.com"
    default_endpoint_map = {
        "billing": ServiceEndpointInfo("billing",
                                       True,
                                       "",
                                       "open.byteplusapi.com",
                                       None)
    }

    @staticmethod
    def get_default_endpoint_by_service_info(service, region):
        if service in DefaultEndpointResolver.default_endpoint_map:
            service_endpoint_info = DefaultEndpointResolver.default_endpoint_map[service]
            if service_endpoint_info.is_global:
                if len(service_endpoint_info.global_endpoint) > 0:
                    return service_endpoint_info.global_endpoint
            else:
                if service_endpoint_info.region_endpoint_map is not None and region in service_endpoint_info.region_endpoint_map:
                    return service_endpoint_info.region_endpoint_map[region]
            if service_endpoint_info.default_endpoint is not None and len(service_endpoint_info.default_endpoint) > 0:
                return service_endpoint_info.default_endpoint
        return DefaultEndpointResolver.global_endpoint
