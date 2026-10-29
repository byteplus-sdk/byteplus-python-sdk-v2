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

An explicitly configured `host` has the highest priority at the configuration level and skips every subsequent resolution step (including any custom endpoint provider). However, a request-level `RuntimeOption.endpoint_provider` overrides the configuration-level `host`, per the general "request-level > configuration-level" rule.

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

    Built-in service map: `default_endpoint` in [`byteplussdkcore/endpoint/providers/default_provider.py`](../byteplussdkcore/endpoint/providers/default_provider.py).

2. **DualStack support (IPv6)**

    Enable via the `use_dual_stack=True` parameter or env var `BYTEPLUS_ENABLE_DUALSTACK=true`. Priority: `use_dual_stack` > `BYTEPLUS_ENABLE_DUALSTACK`.

    When enabled, the suffix changes from `byteplusapi.com` to `byteplus-api.com`.

3. **Go China suffix**

    When a service entry has `go_china_enabled=True` and the request region is in the Chinese mainland (a `cn-*` prefix but not one of the non-mainland regions such as `cn-hongkong`), the resolver appends the `.cn` suffix.

    Whether Go China applies is decided by the service itself and cannot be overridden. Regions are normalized with `strip().lower()` before matching, so `CN-Beijing` and `cn-beijing` are treated identically. A region with leading or trailing whitespace (e.g., `  cn-beijing  `) is rejected by [region and service validation](#region-and-service-validation) before normalization.

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

Note: if the service name itself is not a valid label (e.g., `ecs/x`), the `EndpointValidationError` (`InvalidService`) described below is raised first instead of `ServiceEndpointInfoMissingError`.

##### Region and service validation

The region and service are concatenated into the endpoint host name (e.g., `{service}.{region}.byteplusapi.com`) and are part of the signature. To prevent values such as `ap-southeast-1@127.0.0.1` or `evil.com#` from changing the host the request is actually sent to (SSRF), the SDK checks, before resolving the endpoint, signing or sending the request, that the region and service are each a valid single host name label:

- only ASCII letters, digits, `-` and `_`;
- starts with a letter;
- does not end with `-` or `_`.

The rule is equivalent to the regular expression `^[A-Za-z]([A-Za-z0-9_-]*[A-Za-z0-9])?$` matched against the **whole** string (`re.fullmatch`, or `\A...\Z`; note that `re.match` with `$` would wrongly accept a trailing newline such as `"ap-southeast-1\n"`, the SDK rejects it). An empty string `''` or `None` is not rejected here and is left to the caller's existing handling of missing values; a non-string value (e.g., `42`, `b'ap-southeast-1'`) is always invalid. The service is validated before the region.

**Where it is checked:**

- Regular API calls: `ResolveEndpointInterceptor` validates the service and region before calling any endpoint provider (the region is the final value after any `RuntimeOption` override);
- Universal calls via `UniversalApi.do_call`: `UniversalInfo.service` is validated before the internal request path is built;
- Default resolution `DefaultEndpointProvider` (`endpoint_for`, `get_default_endpoint`), `ServiceEndpointInfo.get_endpoint_for` and standard resolution `StandardEndpointResolver.endpoint_for`: also validate when called directly;
- RDS auth token `build_auth_token`: validates the region before building the presigned token when `configuration.host` is not set;
- SSO credentials from the CLI config file (`SsoCredentialProvider`): validates the SSO region before building the OAuth refresh and Portal URLs and sending the request.

**When it is skipped:** regular API calls and universal calls skip the check when:

- `configuration.host` is set. For regular API calls, a request-level `RuntimeOption.endpoint_provider` clears the host, so the check still runs in that case. Universal calls do not support `RuntimeOption` (the request body of `UniversalApi.do_call` must be a plain `dict`), so only the configuration decides whether the check is skipped;
- the endpoint provider's type is **exactly** `HostEndpointProvider`. The code checks `type(provider) is not HostEndpointProvider`, so **subclasses of `HostEndpointProvider` are not skipped** and are still validated.

**Error type:**

A failed check raises `byteplussdkcore.endpoint.validation.EndpointValidationError`, a subclass of `ValueError`:

- `e.code`: the error code, `InvalidRegion` (constant `ERR_CODE_INVALID_REGION`) or `InvalidService` (constant `ERR_CODE_INVALID_SERVICE`);
- `e.message`: the error description;
- `str(e)` is formatted as `Code: Message`, e.g., `InvalidRegion: invalid region "ap-southeast-1 ": illegal character at index 14, region must start with a letter, end with a letter or digit, and contain only letters, digits, '-' and '_'`.

A non-string value raises the subclass `EndpointValidationTypeError` (also a `TypeError`) with the same `code` values.

On API calls the exception is raised as is before any request is sent; it is **not** wrapped in `ApiException`. When SSO credentials are obtained through the default credential chain `DefaultCredentialProvider`, the chain catches the exception and tries the next provider; if all providers fail, it raises `RuntimeError` (whose message includes this error).

```python
from byteplussdkcore.endpoint.validation import EndpointValidationError
from byteplussdkcore.rest import ApiException

try:
    api_instance.create_command(create_command_request)
except EndpointValidationError as e:
    # e.code is "InvalidRegion" or "InvalidService"
    print(e.code, e.message)
except ApiException as e:
    pass
```

**Behavior change:**

- A region with leading or trailing whitespace (e.g., `"ap-southeast-1 "`, `"ap-southeast-1\n"`) is no longer accepted and raises `InvalidRegion`. Default resolution used to `strip()` the region before building the host, but the signature used the raw value, so the request was already rejected: a value with a trailing space is rejected by the server with `InvalidAuthorization`, while a value containing a newline (such as `"ap-southeast-1\n"`) never leaves the process, because the HTTP client refuses the resulting invalid header value (`Invalid header value`). Call `strip()` yourself before setting `configuration.region` or `RuntimeOption.region`. Regions read from the CLI config file (`region` of a RamRoleArn / OIDC profile, `region` of an `sso-session`) are already `strip()`ped before use and are not affected.
- Subclasses of `HostEndpointProvider` are validated too (see above).
- `StandardEndpointResolver` raises `EndpointValidationError` instead of `StandProviderError` for an invalid label (e.g., `"ap southeast-1"`); a valid label that is not a supported region still raises `StandProviderError` (`InvalidRegion`).
- New public validation functions `validate_region`, `validate_service` and `validate_service_and_region`, importable from `byteplussdkcore.endpoint.validation`. They return nothing on success, raise `EndpointValidationError` on failure, and accept empty values (`''`, `None`).

#### Standard Endpoint Resolution

##### Resolution Rules

| Global Service | DualStack | Format |
|---|---|---|
| Yes | Yes | `{Service}.byteplus-api.com` |
| Yes | No | `{Service}.byteplusapi.com` |
| No | Yes | `{Service}.{region}.byteplus-api.com` (for mainland China regions, `{Service}.{region}.byteplus-api.com.cn`) |
| No | No | `{Service}.{region}.byteplusapi.com` (for mainland China regions, `{Service}.{region}.byteplusapi.com.cn`) |

Whether a service is global is determined by the service itself and cannot be modified. Reference list: [`byteplussdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](../byteplussdkcore/endpoint/providers/standard_provider.py#L51).

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
