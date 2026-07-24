[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)

---

## Endpoint Configuration

> **Default**
>
> If `host` is not specified, the SDK uses [Automatic Endpoint Resolution](#automatic-endpoint-resolution).

### Custom Endpoint

You can specify a custom endpoint when initializing the client:

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.byteplusapi.com" # Custom Endpoint
byteplussdkcore.Configuration.set_default(configuration)
```

An explicitly configured `host` has the highest priority and skips every subsequent resolution step (including any custom endpoint provider).

### Custom RegionId

**Code Example:**

Supports both `configuration`-level global settings and API-level runtime parameter settings via `RuntimeOption`. `RuntimeOption` settings override the `configuration` global settings.

```python
import byteplussdkcore, byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-southeast-1" # Custom RegionId
byteplussdkcore.Configuration.set_default(configuration)

# API-level runtime parameter settings, overrides global configuration
runtime_options = RuntimeOption(
    region="ap-southeast-1",
    client_side_validation=True, # Enable client-side validation, enabled by default
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

### Automatic Endpoint Resolution

BytePlus provides a flexible endpoint resolution mechanism. The SDK automatically builds the endpoint based on the service name, region and the service's Go China flag, and supports DualStack.

#### Default Endpoint Resolution

##### Resolution Logic

1. **Service registration check**

    Every service in the built-in map carries an `is_global` and a `go_china_enabled` bool. The SDK builds the endpoint following the rules below.

    - Service missing from the map: `DefaultEndpointProvider.get_default_endpoint` raises `byteplussdkcore.endpoint.providers.default_provider.ServiceEndpointInfoMissingError` with a message like `byteplussdkcore: service endpoint info missing: service '<xxx>' not registered`; `ResolveEndpointInterceptor` propagates it up the call chain. See [Error handling](#error-handling).

    Built-in service map: `default_endpoint` in [`./byteplussdkcore/endpoint/providers/default_provider.py`](./byteplussdkcore/endpoint/providers/default_provider.py).

2. **DualStack support (IPv6)**

    Enable via the `use_dual_stack=True` parameter or env var `BYTEPLUS_ENABLE_DUALSTACK=true`. Priority: `use_dual_stack` > `BYTEPLUS_ENABLE_DUALSTACK`.

    When enabled, the suffix changes from `byteplusapi.com` to `byteplus-api.com`.

3. **Go China suffix**

    When a service entry has `go_china_enabled=True` and the request region is in the Chinese mainland (a `cn-*` prefix but not one of the non-mainland regions such as `cn-hongkong`), the resolver appends the `.cn` suffix.

    Whether Go China applies is decided by the service itself and cannot be overridden. Regions are normalized with `strip().lower()` before matching, so `CN-Beijing`, `  cn-beijing  ` and `cn-beijing` are treated identically.

4. **Endpoint construction**

    - **Global services (e.g., `IAM`, `Billing`)**: `<service>.byteplusapi.com` (or `byteplus-api.com` when DualStack is enabled; `.cn` is appended when Go China applies).
    - **Regional services (e.g., `ECS`, `RDS`)**: `<service>.<region>.byteplusapi.com` (DualStack / Go China rules identical to global services).

##### Decision Table

The table lists every effective combination. `RegionType` is derived from the service's `is_global` flag; "Region is Go China" refers to the request region.

| RegionType | go_china_enabled | Region is Go China | Endpoint | Region embedded |
|---|---|---|---|---|
| Global | True | yes | `{service}.byteplusapi.com.cn` | no |
| Global | True | no | `{service}.byteplusapi.com` | no |
| Global | False | any | `{service}.byteplusapi.com` | no |
| Regional | True | yes | `{service}.{region}.byteplusapi.com.cn` | yes |
| Regional | True | no | `{service}.{region}.byteplusapi.com` | yes |
| Regional | False | any | `{service}.{region}.byteplusapi.com` | yes |

When DualStack is enabled, replace every occurrence of `byteplusapi.com` in the table with `byteplus-api.com`.

##### `custom_bootstrap_region` / `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF` (Deprecated)

> **⚠️ Deprecated**: the `custom_bootstrap_region` keyword argument on `DefaultEndpointProvider.endpoint_for(...)` and the `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF` environment variable are **deprecated** and **no longer participate** in the default addressing pipeline. The argument is retained only for API-source compatibility and is treated as a no-op at runtime (a `DeprecationWarning` is emitted when a non-empty value is supplied). **Do not use it in new code.** Existing callers should switch to `configuration.region` + `configuration.use_dual_stack` and let the SDK auto-resolve the endpoint, or override it explicitly via `configuration.host`.

##### Code Example

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-southeast-1"
configuration.use_dual_stack = True # enable dual stack; also honors env BYTEPLUS_ENABLE_DUALSTACK=true
byteplussdkcore.Configuration.set_default(configuration)
```

##### Error handling

If the requested service is not registered in `default_endpoint`, the SDK raises `ServiceEndpointInfoMissingError` on the first default endpoint resolution triggered by `ResolveEndpointInterceptor`, with a message like `byteplussdkcore: service endpoint info missing: service '<xxx>' not registered`. Detect it with:

```python
from byteplussdkcore.endpoint.providers.default_provider import ServiceEndpointInfoMissingError

try:
    # ... SDK call that triggers default endpoint resolution
    pass
except ServiceEndpointInfoMissingError as e:
    # e.service carries the offending service name
    # The installed SDK likely does not know this service.
    # Upgrade the dependency or set the endpoint explicitly.
    raise
```

When you hit this error, first try upgrading the SDK. If the service is genuinely not carried by the SDK yet, set the endpoint explicitly via `configuration.host = ...` or supply a custom endpoint provider.

#### Standard Endpoint Resolution

##### Resolution Rules

| Global Service | DualStack | Format |
|---|---|---|
| Yes | Yes | `{Service}.byteplus-api.com` |
| Yes | No | `{Service}.byteplusapi.com` |
| No | Yes | `{Service}.{region}.byteplus-api.com` |
| No | No | `{Service}.{region}.byteplusapi.com` |

Standard resolution never appends the Go China `.cn` suffix. If you need `.cn`, use the default resolver (or set the endpoint explicitly).

Whether a service is global is determined by the service itself and cannot be modified. Reference list: [`./byteplussdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](./byteplussdkcore/endpoint/providers/standard_provider.py#L51).

##### Code Example

```python
import byteplussdkcore
from byteplussdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver() # Configure standard resolution
configuration.use_dual_stack = True # Configure dual-stack
configuration.region = "ap-southeast-1" # Configure region
byteplussdkcore.Configuration.set_default(configuration)
```

---

[← Credentials](1-Credentials.md) | Endpoint[(中文)](2-Endpoint-zh.md) | [Transport →](3-Transport.md)
