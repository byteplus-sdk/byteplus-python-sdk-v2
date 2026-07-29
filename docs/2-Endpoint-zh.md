[← 访问凭据](1-Credentials-zh.md) | Endpoint 配置[(English)](2-Endpoint.md) | [Transport →](3-Transport-zh.md)

---

## EndPoint 配置

> **默认**
>
> 不指定 `host` 时，走 [自动化 Endpoint 寻址](#自动化-endpoint-寻址)。

### 自定义 Endpoint

用户可以通过在初始化客户端时指定 Endpoint：

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.byteplusapi.com" # 自定义Endpoint
byteplussdkcore.Configuration.set_default(configuration)
```

显式设置的 `host` 在配置级优先级最高，会跳过后续所有寻址逻辑（包括自定义 Endpoint Provider）。但请求级 `RuntimeOption.endpoint_provider` 会覆盖配置级 `host`，遵循"请求级 > 配置级"的总规则。

### 自定义 RegionId

**代码示例：**

支持 `configuration` 级别全局配置和接口级别的运行时参数设置 `RuntimeOption`；`RuntimeOption` 设置会覆盖 `configuration` 全局配置。

```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-southeast-1" # 自定义RegionId
byteplussdkcore.Configuration.set_default(configuration)

# 接口级别运行时参数设置,会覆盖全局配置
runtime_options = RuntimeOption(
    region="ap-southeast-1",
    client_side_validation=True, # 开启客户端校验,默认开启
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # 配置运行时参数
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

### 自动化 Endpoint 寻址

> **默认**
>
> 默认支持自动寻址，无需手动指定 Endpoint。

为了简化用户配置，Byteplus 提供了灵活的 Endpoint 自动寻址机制。用户无需手动指定服务地址，SDK 会根据服务名称、区域（Region）、服务是否标记为 Go China 等信息自动拼接出合理的访问地址，并支持用户自定义 DualStack（双栈）。

#### Endpoint 默认寻址

##### 寻址逻辑

1. **服务注册判定**

    每个服务在内置映射中都会登记 `is_global` 和 `go_china_enabled` 两个 bool 字段，SDK 按下方"标准寻址规则"构造 Endpoint。

    - 服务未在映射中登记：`DefaultEndpointProvider.get_default_endpoint` 会抛出 `byteplussdkcore.endpoint.providers.default_provider.ServiceEndpointInfoMissingError`，错误消息形如 `byteplussdkcore: service endpoint info missing: service '<xxx>' not registered`；`ResolveEndpointInterceptor` 将其直接向上传播。参见 [错误处理](#错误处理)。

    内置服务映射：[`byteplussdkcore/endpoint/providers/default_provider.py`](../byteplussdkcore/endpoint/providers/default_provider.py) 中的 `default_endpoint`。

2. **DualStack 支持（IPv6）**

    SDK 支持双栈网络（IPv4 + IPv6）访问地址，自动启用条件如下：显式传入参数 `use_dual_stack=True`，或设置环境变量 `BYTEPLUS_ENABLE_DUALSTACK=true`。优先级：`use_dual_stack` > `BYTEPLUS_ENABLE_DUALSTACK`。

    启用后，域名后缀将从 `byteplusapi.com` 切换为 `byteplus-api.com`。

3. **Go China 后缀**

    当服务在内置映射中标记 `go_china_enabled=True`，并且请求 Region 属于中国大陆（`cn-*` 前缀且不属于 `cn-hongkong` 等非大陆港澳台 Region）时，在域名后追加 `.cn` 后缀。

    是否 GoChina 由服务侧决定，不可修改。匹配前会先对 region 做 `strip().lower()` 归一化，因此 `CN-Beijing`、`  cn-beijing  ` 与 `cn-beijing` 等价。

4. **根据服务名和区域自动构造 Endpoint 地址**

    - **Global 服务（如 `IAM`、`Billing`）**：使用 `<服务名>.byteplusapi.com`（DualStack 时使用 `byteplus-api.com`；命中 Go China 时追加 `.cn`）。
    - **Regional 服务（如 `ECS`、`RDS`）**：使用 `<服务名>.<区域名>.byteplusapi.com` 作为默认 Endpoint（DualStack / Go China 规则同上）。

##### 寻址决策表

下表列出所有生效组合。左侧列的 "RegionType" 由服务的 `is_global` 决定；"Region 是否 GoChina" 指请求 Region 是否属于中国大陆。

| RegionType | go_china_enabled | 请求 Region 是否 Go China | Endpoint | 是否包含 Region |
|---|---|---|---|---|
| Global | True | 是 | `{service}.byteplusapi.com.cn` | 否 |
| Global | True | 否 | `{service}.byteplusapi.com` | 否 |
| Global | False | 任意 | `{service}.byteplusapi.com` | 否 |
| Regional | True | 是 | `{service}.{region}.byteplusapi.com.cn` | 是 |
| Regional | True | 否 | `{service}.{region}.byteplusapi.com` | 是 |
| Regional | False | 任意 | `{service}.{region}.byteplusapi.com` | 是 |

启用 DualStack 时，将上表中的 `byteplusapi.com` 整体替换为 `byteplus-api.com`。

##### `custom_bootstrap_region` / `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF`（已废弃）

> **⚠️ Deprecated**：`DefaultEndpointProvider.endpoint_for(...)` 上的 `custom_bootstrap_region` 关键字参数以及 `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF` 环境变量已被标记为**废弃**，**不再参与**默认寻址链路。该参数仅为 API 源码兼容而保留，运行时视为 no-op（传入非空值时会产生 `DeprecationWarning`）。请**勿在新代码中使用**，已有代码建议改用 `configuration.region` + `configuration.use_dual_stack` 让 SDK 自动寻址，或用 `configuration.host` 显式覆盖。

##### 代码示例

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-southeast-1"
configuration.use_dual_stack = True # 定义是否启用双栈网络（IPv4 + IPv6）访问地址，默认false；也可以使用环境变量 BYTEPLUS_ENABLE_DUALSTACK=true
byteplussdkcore.Configuration.set_default(configuration)
```

##### 错误处理

如果请求的服务名不在内置 `default_endpoint` 映射中，SDK 在第一次触发默认寻址时就会抛出 `ServiceEndpointInfoMissingError`，错误消息形如 `byteplussdkcore: service endpoint info missing: service '<xxx>' not registered`。可用如下方式识别：

```python
from byteplussdkcore.endpoint.providers.default_provider import ServiceEndpointInfoMissingError

try:
    # ... SDK call that triggers default endpoint resolution
    pass
except ServiceEndpointInfoMissingError as e:
    # e.service 携带缺失的服务名
    # SDK 版本可能不识别该服务，请升级依赖或显式指定 Endpoint。
    raise
```

遇到该错误时，建议先升级 SDK 版本；若确认 SDK 尚未内置该服务的寻址元数据，可通过 `configuration.host = ...` 或自定义 Endpoint Provider 显式指定。

#### Endpoint 标准寻址

##### 标准寻址规则

| Global 服务 | 双栈 | 格式 |
|---|---|---|
| 是 | 是 | `{Service}.byteplus-api.com` |
| 是 | 否 | `{Service}.byteplusapi.com` |
| 否 | 是 | `{Service}.{region}.byteplus-api.com` |
| 否 | 否 | `{Service}.{region}.byteplusapi.com` |

服务是否为 Global 由具体服务决定，不可修改。可以参考列表：[`byteplussdkcore/endpoint/providers/standard_provider.py#ServiceInfos`](../byteplussdkcore/endpoint/providers/standard_provider.py#L51)。

##### 代码示例

```python
import byteplussdkcore
from byteplussdkcore.endpoint.providers.standard_provider import StandardEndpointResolver
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.endpoint_provider = StandardEndpointResolver() # 配置标准寻址
configuration.use_dual_stack = True # 配置是否双栈
configuration.region = "ap-southeast-1" # 配置region
byteplussdkcore.Configuration.set_default(configuration)
```

---

[← 访问凭据](1-Credentials-zh.md) | Endpoint 配置[(English)](2-Endpoint.md) | [Transport →](3-Transport-zh.md)
