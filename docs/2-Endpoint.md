[← Credentials](1-Credentials.md) | [Transport →](3-Transport.md)

---

# Endpoint Configuration

## Custom Endpoint

> **Default**
> * When no endpoint is specified, the SDK uses [Automatic Endpoint Resolution](#automatic-endpoint-resolution).

You can specify a custom endpoint when initializing the client:

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.byteplusapi.com" # Custom Endpoint
byteplussdkcore.Configuration.set_default(configuration)
```

## Custom RegionId

**Code Example:**

Supports both `configuration`-level global settings and API-level runtime parameter settings via `RuntimeOption`. `RuntimeOption` settings override the `configuration` global settings.

```python
import byteplussdkcore, byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-singapore-1" # Custom RegionId
byteplussdkcore.Configuration.set_default(configuration)

# API-level runtime parameter settings, overrides global configuration
runtime_options = RuntimeOption(
  region =  "ap-singapore-1",
  client_side_validation = True, # Enable client-side validation, enabled by default
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Set runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

## Automatic Endpoint Resolution

> **Default**
> * Automatic resolution is enabled by default; no manual endpoint specification is needed.

To simplify user configuration, BytePlus provides a flexible automatic Endpoint resolution mechanism. Users do not need to manually specify service addresses; the SDK automatically constructs a reasonable access address based on the service name, region, and other information, and supports user-defined DualStack (dual-stack) settings.

### Default Endpoint Resolution

**Default Endpoint Resolution Logic**

1. **Whether to auto-resolve the Region**
The SDK only performs automatic resolution for certain preset regions or user-configured regions; other regions default to the endpoint: `open.byteplusapi.com`.
Users can extend the region list via the environment variable `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF` or by specifying `custom_bootstrap_region` in code.

2. **DualStack Support (IPv6)**
The SDK supports dual-stack network (IPv4 + IPv6) access addresses. Automatic enabling conditions:
Explicitly pass the `use_dual_stack` parameter, or set the environment variable `BYTEPLUS_ENABLE_DUALSTACK`. Priority: `use_dual_stack` > `BYTEPLUS_ENABLE_DUALSTACK`.
When enabled, the domain suffix switches from `byteplusapi.com` to `byteplus-api.com`.

3. **Endpoint construction based on service name and region**, with the following rules:
**Global services (e.g., CDN, IAM)**
Use `<ServiceName>.byteplusapi.com` (or `byteplus-api.com` when dual-stack is enabled).
Example: `cdn.byteplusapi.com`
**Regional services (e.g., ECS, RDS)**
Use `<ServiceName>.<Region>.byteplusapi.com` as the default endpoint.
Example: `ecs.ap-singapore-1.byteplusapi.com`

**Code Example:**

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.use_dual_stack = True # Enable dual-stack network (IPv4 + IPv6) access, default is False
configuration.custom_bootstrap_region = {
  "custom_example_region1": {},
  "custom_example_region2": {},
} # Custom auto-resolution region list
byteplussdkcore.Configuration.set_default(configuration)
```

### Standard Endpoint Resolution

**Standard Resolution Rules**

| Global Service | DualStack | Format |
|---|---|---|
| Yes | Yes | `{Service}.byteplus-api.com` |
| Yes | No | `{Service}.byteplusapi.com` |
| No | Yes | `{Service}.{region}.byteplus-api.com` |
| No | No | `{Service}.{region}.byteplusapi.com` |

**Code Example:**

Whether a service is global depends on the specific service being called and cannot be modified.

```python
import byteplussdkcore
from byteplussdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver() # Configure standard resolution
configuration.use_dual_stack = True # Configure dual-stack
configuration.region = "ap-singapore-1" # Configure region
byteplussdkcore.Configuration.set_default(configuration)
```

---

[← Credentials](1-Credentials.md) | [Transport →](3-Transport.md)
