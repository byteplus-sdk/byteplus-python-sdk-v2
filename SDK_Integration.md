English | [简体中文](./SDK_Integration_zh.md)

# Table of Contents

- [Table of Contents](#table-of-contents)
- [Integrate the SDK](#integrate-the-sdk)
- [Environment Requirements](#environment-requirements)
- [Credentials](#credentials)
  - [AK/SK](#aksk)
  - [STS Token Settings](#sts-token-settings)
  - [STS AssumeRole Settings](#sts-assumerole-settings)
  - [STS AssumeRoleWithOidc Settings](#sts-assumerolewithoidc-settings)
  - [STS AssumeRoleWithSaml Settings](#sts-assumerolewithsaml-settings)
- [Endpoint Configuration](#endpoint-configuration)
  - [Custom Endpoint](#custom-endpoint)
  - [Custom RegionId](#custom-regionid)
  - [Automatic Endpoint Resolution](#automatic-endpoint-resolution)
    - [Default Endpoint Resolution](#default-endpoint-resolution)
- [HTTP Connection-Pool Settings](#http-connection-pool-settings)
- [HTTPS Request Settings](#https-request-settings)
  - [Specify the Scheme](#specify-the-scheme)
  - [Skip SSL Verification](#skip-ssl-verification)
- [Http(s) Proxy Configuration](#https-proxy-configuration)
  - [Set Http(s) Proxy](#set-https-proxy)
  - [Notice](#notice)
- [Timeouts](#timeouts)
- [Retry Mechanism](#retry-mechanism)
  - [Retry code configuration](#retry-code-configuration)
  - [Retry conditions](#retry-conditions)
    - [Default retry conditions](#default-retry-conditions)
    - [Custom retry conditions](#custom-retry-conditions)
  - [Backoff strategy](#backoff-strategy)
    - [Built-in backoff strategy](#built-in-backoff-strategy)
    - [Custom backoff strategy](#custom-backoff-strategy)
- [Error Handling](#error-handling)
- [Debugging](#debugging)
- [Custom Logger](#custom-logger)

---

# Integrate the SDK

When calling BytePlus APIs, we recommend integrating the official SDK into your project.
Using the SDK simplifies development, speeds up integration, and significantly reduces long-term maintenance costs.
SDK integration generally involves three steps:

1. **Add the SDK** to your project.
2. **Configure access credentials**.
3. **Write the API-calling code**.

This guide explains each step in detail, with tips for common scenarios.

---

# Environment Requirements

1. **Python 2.7+ is required.**
2. If you use the `byteplussdkarkruntime` , Python 3.6+ is required.

---
# Credentials

So far, BytePlus Python SDK supports `AK/SK` and `STS Token` settings.

## AK/SK

AK (AccessKey) and SK (SecretKey) are permanent credentials created in the BytePlus console.

> ⚠️ **Best Practices**
>
> 1. **Never** embed AK/SK in client apps.
> 2. Store keys in a **configuration service** or **environment variables**.
> 3. Apply the **principle of least privilege**.

Supports `configuration`-level global configuration and interface-level runtime parameter settings `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.

```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption

# Global settings
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)

#Interface level runtime parameter settings will override Global Configuration
runtime_options = RuntimeOption(
  ak =  "Your ak", 
  sk = "Your sk",
  client_side_validation = True, # Client-side validation  
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Configuring runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```
---

## STS Token Settings

STS (Security Token Service) is a temporary access credential mechanism provided by Volcano Engine. Developers call the STS interface through the server to obtain temporary credentials (temporary AK, SK and Token). The validity period is configurable and suitable for scenarios with high security requirements.

> ⚠️ Notes
>
> 1. Minimum permissions: Only grant the caller the minimum permissions to access the required resources, and avoid using the * wildcard to grant full resource and full operation permissions.
> 2. Set a reasonable validity period: Please set a reasonable validity period according to the actual situation. The shorter the better. It is recommended not to exceed 1 hour.

Supports `configuration` level global configuration and interface level runtime parameter setting `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.

```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption

# Global settings
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.session_token = "Your sts token"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)

# Interface-level runtime parameter settings, will override global configuration
runtime_options = RuntimeOption(
ak = "Your ak",
sk = "Your sk",
session_token = "Your sts token",
client_side_validation = True, # Enable client-side validation, enabled by default
)
api_instance = byteplussdkecs.ECCSApi()
create_command_request = byteplussdkecs.CreateCommandRequest( 
command_content="ls -l", 
description="Your command description", 
name="Your command name", 
type="command", 
_configuration=runtime_options, # Configure runtime parameters
)
try: 
    api_instance.create_command(create_command_request)
except ApiException as e: 
    pass
```
## STS AssumeRole Settings
STS AssumeRole(Security Token Service) is a temporary access credential mechanism provided by Volcano Engine. Developers call the STS interface through the server to obtain temporary credentials (temporary AK, SK and Token). The validity period is configurable and suitable for scenarios with high security requirements.

> ⚠️ Notes
>
> 1. Minimum permissions: Only grant the caller the minimum permissions to access the required resources, and avoid using the * wildcard to grant full resource and full operation permissions.
> 2. Set a reasonable validity period: Please set a reasonable validity period according to the actual situation. The shorter the better. It is recommended not to exceed 1 hour.

Supports `configuration` level global configuration and interface level runtime parameter setting `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.
```python
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_provider import StsCredentialProvider

if __name__ == '__main__':
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-singapore-1"

    configuration.credential_provider = StsCredentialProvider(
        ak="Your ak",  
        sk="Your sk",  
        role_name="Your role name",  
        account_id="Your account id",  
        duration_seconds=3600,  
        scheme="https",  
        host="sts.volcengineapi.com",  
        region="ap-singapore-1",  
        timeout=30,  
        expired_buffer_seconds=60, 
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["ap-singapore-1"]}}}]}' 
    )

    # set default configuration
    byteplussdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # print("Exception when calling api: %s\n" % e)
        pass
```

## STS AssumeRoleWithOidc Settings
STS AssumeRole Oidc(Security Token Service) is a temporary access credential mechanism provided by Volcano Engine. Developers call the STS interface through the server to obtain temporary credentials (temporary AK, SK and Token). The validity period is configurable and suitable for scenarios with high security requirements.

> ⚠️ Notes
>
> 1. Minimum permissions: Only grant the caller the minimum permissions to access the required resources, and avoid using the * wildcard to grant full resource and full operation permissions.
> 2. Set a reasonable validity period: Please set a reasonable validity period according to the actual situation. The shorter the better. It is recommended not to exceed 1 hour.

Supports `configuration` level global configuration and interface level runtime parameter setting `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.
```python
# Example Code generated by Beijing Volcanoengine Technology.
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

if __name__ == '__main__':
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-singapore-1"

    configuration.credential_provider = StsOidcCredentialProvider(
        role_name="Your role name",  
        account_id="Your account id", 
        oidc_token="your oidc token", 
        duration_seconds=3600,  
        scheme="https", 
        host="sts.volcengineapi.com",  
        region="ap-singapore-1",  
        timeout=30,  
        expired_buffer_seconds=60,  
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["ap-singapore-1"]}}}]}' 
    )

    # set default configuration
    byteplussdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # print("Exception when calling api: %s\n" % e)
        pass

```

## STS AssumeRoleWithSaml Settings
STS AssumeRole Saml(Security Token Service) is a temporary access credential mechanism provided by Volcano Engine. Developers call the STS interface through the server to obtain temporary credentials (temporary AK, SK and Token). The validity period is configurable and suitable for scenarios with high security requirements.

> ⚠️ Notes
>
> 1. Minimum permissions: Only grant the caller the minimum permissions to access the required resources, and avoid using the * wildcard to grant full resource and full operation permissions.
> 2. Set a reasonable validity period: Please set a reasonable validity period according to the actual situation. The shorter the better. It is recommended not to exceed 1 hour.

Supports `configuration` level global configuration and interface level runtime parameter setting `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.
```python
# Example Code generated by Beijing Volcanoengine Technology.
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_saml_provider import StsSamlCredentialProvider

if __name__ == '__main__':
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-singapore-1"

    configuration.credential_provider = StsSamlCredentialProvider(
        role_name="Your role name",  
        account_id="Your account id",  
        provider_name="your provider name",
        saml_resp="your saml resp",  
        duration_seconds=3600,  
        scheme="https",  
        host="sts.volcengineapi.com", 
        region="ap-singapore-1", 
        timeout=30,  
        expired_buffer_seconds=60,  
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"volc:RequestedRegion":["ap-singapore-1"]}}}]}' 
    )

    # set default configuration
    byteplussdkcore.Configuration.set_default(configuration)
    # use global default configuration
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException as e:
        # print("Exception when calling api: %s\n" % e)
        pass

```
---

# Endpoint Configuration

## Custom Endpoint

> **Default**
> * if no endpoint is specified, the SDK falls back to [Automatic Endpoint Resolution](#automatic-endpoint-resolution).

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.host = "<example>.<regionId>.byteplusapi.com" # Custom Endpoint
byteplussdkcore.Configuration.set_default(configuration)
```

## Custom RegionId
Supports `configuration`-level global configuration and interface-level runtime parameter settings `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.

```python
import byteplussdkcore, byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption

# global configration
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.region = "ap-southeast-1"  # Custom RegionId
byteplussdkcore.Configuration.set_default(configuration)

# Interface-level runtime parameter settings will override global configurations
runtime_options = RuntimeOption(
    region="ap-southeast-1",
    client_side_validation=True,  # Client-side validation  
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Configuring runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

## Automatic Endpoint Resolution

> **Default**  
> * enabled; no manual configuration required.

BytePlus constructs the endpoint from service name and region, and supports IPv6 “DualStack”.

### Default Endpoint Resolution

1. **Auto-discoverable Regions**  
   Built-in automatic addressing Region list code:[./byteplussdkcore/endpoint/providers/default_provider.py#bootstrap_region](./byteplussdkcore/endpoint/providers/default_provider.py#L17)   
   Automatic resolution applies only to predefined regions (e.g. `ap-southeast-2`).
   Extend the list via the `BYTEPLUS_BOOTSTRAP_REGION_LIST_CONF` env var or `custom_bootstrap_region`.
2. **DualStack (IPv6)**
   Enable with `use_dual_stack` or `BYTEPLUS_ENABLE_DUALSTACK`.
   The domain suffix changes from `byteplusapi.com` to `byteplus-api.com`.
3. **Address Format**

   * **Global services** (e.g. `BILLING`, `IAM`): `service.byteplusapi.com`
   * **Regional services** (e.g. `ECS`, `VPC`): `service.region.byteplusapi.com`

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.use_dual_stack = True # Defines whether to enable dual stack network (IPv4 + IPv6) access address, default is false
configuration.custom_bootstrap_region = {
  "custom_example_region1": {},
  "custom_example_region2": {},
} # Customize the automatic addressing region list
byteplussdkcore.Configuration.set_default(configuration)
```

---

# HTTP Connection-Pool Settings

> **Defaults**  
> * `num_pools` - 4 The maximum number of hosts supported; applicable scenario: when you make multiple concurrent requests to the same host, you should increase this value
> * `connection_pool_maxsize` - `multiprocessing.cpu_count() * 5` Maximum number of connections per host; Applicable scenario: When you need to connect to multiple different hosts at the same time, you should increase this value

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.num_pools=10 # Maximum number of hosts supported
configuration.connection_pool_maxsize=10 # Maximum number of connections per host
byteplussdkcore.Configuration.set_default(configuration)
```

---

# HTTPS Request Settings

## Specify the Scheme

> **Default**  
> * `scheme` - `https`

Supports `configuration`-level global configuration and interface-level runtime parameter settings `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.

```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
# Global Configuration
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.scheme="http" # Specify scheme
byteplussdkcore.Configuration.set_default(configuration)

# Interface-level runtime parameter settings will override global configurations
runtime_options = RuntimeOption(
  scheme =  "http",
  client_side_validation = True, # Client-side validation  
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Configuring runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```

## Skip SSL Verification
> **Default**  
> * `verify_ssl` - `True`

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.verify_ssl=False # Ignore SSL Verification
byteplussdkcore.Configuration.set_default(configuration)
```
---

# Http(s) Proxy Configuration

> - **default** 
>   no proxy

## Set Http(s) Proxy

```python
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.http_proxy = "http://your_proxy:8080"
configuration.https_proxy = "http://your_proxy:8080"

byteplussdkcore.Configuration.set_default(configuration)

```

## Notice

You can set environment variables below:

http_proxy/HTTP_PROXY, https_proxy/HTTPS_PROXY

Priority: Code > Environment variables

# Timeouts

> **Defaults**  
> * `connect_timeout` - `30s`  
> * `read_timeout` - `30s`

Supports `configuration`-level global configuration and interface-level runtime parameter settings `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.

```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
# global configurations
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.connect_timeout=10 # set connect_timeout,Unit: Seconds
configuration.read_timeout=10 # set read_timeout,Unit: Seconds
byteplussdkcore.Configuration.set_default(configuration)

# Interface-level runtime parameter settings will override global configurations
runtime_options = RuntimeOption(
  connect_timeout=10, # set connect_timeout,Unit: Seconds
  read_timeout=20, # set read_timeout,Unit: Seconds
  client_side_validation = True, # Client-side validation  
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,  # Configuring runtime parameters
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass
```


---

# Retry Mechanism

The request handling logic includes built-in retry mechanisms for network-related exceptions. When a network failure or throttling error occurs, the system will automatically retry the request to ensure service stability and reliability. However, if the request fails due to business logic errors—such as invalid parameters or missing resources—the SDK will not perform a retry. This is because business-level errors typically require the application to handle them based on specific error details, rather than retrying the request blindly.

## Retry code configuration
Supports `configuration`-level global configuration and interface-level runtime parameter settings `RuntimeOption`; `RuntimeOption` settings will override `configuration` global configuration.
```python
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption
from byteplussdkcore.retryer.backoff_strategy import ExponentialWithRandomJitterBackoffStrategy
from byteplussdkcore.retryer.retry_condition import DefaultRetryCondition
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
# Global Configuration
configuration.auto_retry = True # Enable automatic retry, enabled by default
configuration.num_max_retries = 4 # The maximum number of retries is 3 by default.
configuration.min_retry_delay_ms = 200 # Minimum retry delay in milliseconds, default 30 milliseconds
configuration.max_retry_delay_ms = 6000 # Maximum retry delay in milliseconds, default 300000 milliseconds
configuration.backoff_strategy = ExponentialWithRandomJitterBackoffStrategy() # Retry strategy, default ExponentialWithRandomJitterBackoffStrategy
configuration.retry_condition = DefaultRetryCondition() # Retry condition, default DefaultRetryCondition
configuration.retry_error_codes = {"AccessDenied"} # Retry error code, the default is an empty set, which needs to be customized by the user
byteplussdkcore.Configuration.set_default(configuration)

# Interface level configuration
runtime_options = RuntimeOption(
  auto_retry = True, # Enable automatic retry, enabled by default
  num_max_retries = 4, # The maximum number of retries is 3 by default.
  min_retry_delay_ms = 200, # Minimum retry delay in milliseconds, default 30 milliseconds
  max_retry_delay_ms = 6000, # Maximum retry delay in milliseconds, default 300000 milliseconds
  backoff_strategy = ExponentialWithRandomJitterBackoffStrategy(), # Retry strategy, default ExponentialWithRandomJitterBackoffStrategy
  retry_condition = DefaultRetryCondition(), # Retry condition, default DefaultRetryCondition
  retry_error_codes = {"AccessDenied"}, # Retry error code, the default is an empty set, which needs to be customized by the user
  client_side_validation = True, # Client-side validation  
)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
    _configuration=runtime_options,
)
try:
    api_instance.create_command(create_command_request)
except ApiException as e:
    pass

```

## Retry conditions
Retry conditions define the circumstances under which a retry is required. The SDK has built-in default retry conditions, and users can also customize retry conditions based on their business needs.
### Default retry conditions
Default retry condition`DefaultRetryCondition`,Contains the following retry conditions：
1. Network errors will be retried
2. Server-side current limiting errors will be retried
3. Includes customer-defined error codes `retry_error_codes`

### Custom retry conditions
Users can customize retry conditions according to their business needs.  

1. Inherit the base class `RetryCondition` and implement `def should_retry(self, response, err)`
```python
from byteplussdkcore.retryer.retry_condition import RetryCondition
class CustomRetryCondition(RetryCondition):
  def should_retry(
          self,
          response,
          err
  ):
      # type: (RESTResponse, Exception) -> bool
      retry_error_codes = self.retry_error_codes # You can get user-defined error codes
      #................Implement your own logic

      return False
```
2. Reuse the default `DefaultRetryCondition` logic
```python
from byteplussdkcore.retryer.retry_condition import DefaultRetryCondition
class CustomRetryCondition(DefaultRetryCondition):
  def should_retry(
          self,
          response,
          err
  ):
      # type: (RESTResponse, Exception) -> bool
      should_retry = super(CustomRetryCondition, self).should_retry(response, err)  
      #..................Implement your own logic

      return False
```

## Backoff strategy
The backoff strategy defines the delay time between each retry. The SDK has a built-in default backoff strategy, and users can also customize the backoff strategy according to their business needs.
>**Default**  
> * `ExponentialWithRandomJitterBackoffStrategy`
### Built-in backoff strategy
| Backoff strategy name                      | description | Formula (boundary values: `min_retry_delay` minimum delay time, `max_retry_delay` maximum delay time)                                                     |
|--------------------------------------------| -- |-------------------------------------------------------------------------------------|
| `NoBackoffStrategy`                          | No backoff is used. Each retry is executed immediately with zero delay. | `delay=0.0`                                                                           |
| `ExponentialBackoffStrategy`                 | Each retry delay increases by 2ⁿ, subject to the minimum/maximum delay constraints. The request frequency can be quickly reduced. | `delay=min(min_retry_delay*2ⁿ, max_retry_delay)`                                      |
| `ExponentialWithRandomJitterBackoffStrategy` | The value is between [base, 2·base]: always ≥ base, the jitter amplitude is the same width as the baseline. | `base = min(min_retry_delay · 2ⁿ,  max_retry_delay )`  <br/>`delay = base + U(0, base)` |

### Custom backoff strategy
Users can customize the backoff strategy according to their needs.  

1. Inherit the base class `BackoffStrategy` and implement the function `def compute_delay(self, retry_count)` 
```python
from byteplussdkcore.retryer.backoff_strategy import BackoffStrategy
class CustomBackoffStrategy(BackoffStrategy):
    def compute_delay(self, retry_count):
        # type: (int) -> float
        
        min_retry_delay = self.min_retry_delay
        max_retry_delay = self.max_retry_delay
        #.....Implement your own logic
        return 0.0
```
2. You can also reuse the built-in backoff strategy `ExponentialBackoffStrategy` or `ExponentialWithRandomJitterBackoffStrategy`
```python
from byteplussdkcore.retryer.backoff_strategy import ExponentialBackoffStrategy
class CustomBackoffStrategy(ExponentialBackoffStrategy):
    def compute_delay(self, retry_count):
        # type: (int) -> float
        delay = super(CustomBackoffStrategy, self).compute_delay(retry_count)
        #.....Implement your own logic
        return 0.0
```

---

# Error Handling

| Type                      | Scenario | Returns                                                                                                                                                                                                | description |
|---------------------------|-|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-|
| **`1.Network / Timeout`** | DNS failure, deadline | (`urllib3.exceptions.NewConnectionError`, `urllib3.exceptions.ConnectTimeoutError`,<br/>`urllib3.exceptions.ReadTimeoutError`, `urllib3.exceptions.ProtocolError`,`socket.timeout`, `socket.gaierror`) |Errors included in the tuple indicate network errors|
| **`2.Client Error`**      | The request did not reach some parameter authentication of the server| `byteplussdkcore.rest.ApiException``ValueError`                                                                                                                                                        | Client parameter validation|
| **`3.Server Error`**      | The request successfully reaches the server and returns a business logic error | `byteplussdkcore.rest.ApiException`                                                                                                                                                                    | status!=0 indicates a server error |
| **`4.Other Error`**       | catch-all error | `Exception`                                                                                                                                                                                            | catch-all error |


(See the full sample code for detailed handling.)

```python
import json
import socket
import urllib3
import byteplussdkcore,byteplussdkecs
from byteplussdkcore.rest import ApiException
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
byteplussdkcore.Configuration.set_default(configuration)
api_instance = byteplussdkecs.ECSApi()
create_command_request = byteplussdkecs.CreateCommandRequest(
    command_content="ls -l",
    description="Your command description",
    name="Your command name",
    type="command",
)
network_error_exceptions = (urllib3.exceptions.NewConnectionError, urllib3.exceptions.ConnectTimeoutError,
                                    urllib3.exceptions.ReadTimeoutError, urllib3.exceptions.ProtocolError,
                                    socket.timeout, socket.gaierror)

try:
    api_instance.create_command(create_command_request)
except network_error_exceptions as e:
    print("1.Network / Timeout:{}".format(e))
except ValueError as e:
    print("2.Client Error(parameter validation fails):{}".format(e))
except ApiException as e:
    if e.status == 0:
        print("2.Client Error(SSL certificate fails):{}".format(e.reason))
    else:
        print("3.Server Error:")
        if e.body is not None:
            response_meta_data = json.loads(e.body).get("ResponseMetadata")
            print("RequestId:{}".format(response_meta_data.get("RequestId")))
            print("Error Code: {}".format(response_meta_data.get("Error").get("Code")))
            print("Error Message: {}".format(response_meta_data.get("Error").get("Message")))
except Exception as e:
    print("4.Other Error:%s", e)
```

---

# Debugging
To facilitate customers to troubleshoot and debug when processing requests, the SDK supports logging and provides multiple log level settings. Customers can configure the log level according to actual needs and obtain detailed request and response information to improve troubleshooting efficiency and system observability.

>**Default**      
> * `debug` - `False`

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.debug = True  # Enable debug mode
byteplussdkcore.Configuration.set_default(configuration)
```

---

# Custom Logger

> **Defaults**   
> * `logger_file` - `None` (Default, no output is sent to the file, but to the console.)
> * `logger_format` - `%(asctime)s %(levelname)s %(message)s` (Default log format)

```python
import byteplussdkcore
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your AK"
configuration.sk = "Your SK"
configuration.logger_file = "app.log" # Specify the log path
configuration.logger_format = "%(asctime)s %(levelname)s %(message)s" # Specifying the log format
byteplussdkcore.Configuration.set_default(configuration)

