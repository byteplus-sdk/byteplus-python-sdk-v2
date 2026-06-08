[← Overview](0-Overview.md) | Credentials[(中文)](1-Credentials-zh.md) | [Endpoint →](2-Endpoint.md)

---

## Credentials

The BytePlus Python SDK supports explicit credentials and `CredentialProvider`-based automatic resolution.

### Credential Providers Overview

| Provider | Purpose | Refresh Support | Typical Scenario |
| --- | --- | --- | --- |
| `StaticCredentialProvider` | Static AK/SK(/Token) | No | Long-lived server-side credentials |
| `StsCredentialProvider` | STS AssumeRole | Yes | Role-based temporary credentials |
| `StsOidcCredentialProvider` | STS AssumeRoleWithOIDC | Yes | OIDC federation |
| `StsSamlCredentialProvider` | STS AssumeRoleWithSAML | Yes | SAML federation |
| `EnvironmentVariableCredentialProvider` | Read from env vars | No | CI/CD and container env injection |
| `CLIConfigCredentialProvider` | Read from `~/.byteplus/config.json` | Depends on mode | Reuse CLI login/profile |
| `EcsRoleCredentialProvider` | Read from ECS IMDS | Yes | ECS instance role credentials |
| `DefaultCredentialProvider` | Chain wrapper | Depends on delegated provider | No AK/SK in application code |

### AK/SK

AK/SK is a pair of permanent access keys created in the BytePlus console. The SDK signs each request to authenticate.

> ⚠️ **Notes**
>
> 1. Do not embed or expose AK/SK in client-side applications.
> 2. Use a configuration center or environment variables.
> 3. Follow least privilege principles.

The SDK supports both global `configuration` and per-request runtime options (`RuntimeOption`). Runtime options override global configuration.

```python
import byteplussdkcore, byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption

# Global configuration
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)

# Per-request runtime options (override global configuration)
runtime_options = RuntimeOption(
  ak="Your ak",
  sk="Your sk",
  client_side_validation=True,
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
except ApiException:
    pass
```

### STS Token

STS (Security Token Service) provides temporary credentials (temporary AK/SK and Token).

> ⚠️ **Notes**
>
> 1. Least privilege.
> 2. Use a reasonable TTL. Shorter is safer; avoid exceeding 1 hour.

```python
import byteplussdkcore, byteplussdkecs
from byteplussdkcore.rest import ApiException
from byteplussdkcore.interceptor import RuntimeOption

# Global configuration
configuration = byteplussdkcore.Configuration()
configuration.ak = "Your ak"
configuration.sk = "Your sk"
configuration.session_token = "Your session token"
configuration.debug = True
byteplussdkcore.Configuration.set_default(configuration)

# Per-request runtime options
runtime_options = RuntimeOption(
  ak="Your ak",
  sk="Your sk",
  session_token="Your session token",
  client_side_validation=True,
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
except ApiException:
    pass
```

### STS AssumeRole

STS AssumeRole obtains temporary credentials by assuming an IAM role. Use the role credentials to perform actual API calls.

```python
from __future__ import print_function
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_provider import StsCredentialProvider

if __name__ == '__main__':
    # Do NOT leak credentials in example code.
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-singapore-1"

    configuration.credential_provider = StsCredentialProvider(
        ak="Your ak",
        sk="Your sk",
        role_name="Your role name",
        account_id="Your account id",
        duration_seconds=3600,
        scheme="https",
        host="open.byteplusapi.com",
        region="ap-singapore-1",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"byteplus:RequestedRegion":["ap-singapore-1"]}}}]}'
    )

    byteplussdkcore.Configuration.set_default(configuration)
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

### STS AssumeRoleWithOidc

STS AssumeRoleWithOidc obtains temporary credentials via an OIDC token.

The SDK has a single OIDC implementation: `StsOidcCredentialProvider`.

- Backward-compatible mode: `role_name + account_id + oidc_token` (all optional; missing values do NOT read env vars)
- Env-aware mode: `role_trn + oidc_token_file` (all optional; missing values fall back to env vars)
- All parameters are optional. When none are provided, the provider reads entirely from environment variables.

Supported OIDC env vars:

- `BYTEPLUS_OIDC_ROLE_TRN`
- `BYTEPLUS_OIDC_TOKEN_FILE`
- `BYTEPLUS_OIDC_ROLE_SESSION_NAME`
- `BYTEPLUS_OIDC_ROLE_POLICY`
- `BYTEPLUS_OIDC_STS_ENDPOINT`

Backward-compatible example:

```python
from __future__ import print_function
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

if __name__ == '__main__':
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-southeast-1"

    configuration.credential_provider = StsOidcCredentialProvider(
        role_name="Your role name",
        account_id="Your account id",
        # Alternatively, pass the full role_trn directly (overrides role_name + account_id):
        # role_trn="trn:iam::2110400000:role/role123",
        oidc_token="your oidc token",
        duration_seconds=3600,
        scheme="https",
        host="sts.byteplusapi.com",
        region="ap-southeast-1",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"byteplus:RequestedRegion":["ap-southeast-1"]}}}]}',
        max_retries=3,     # optional, HTTP retry attempts (min 1), defaults to 3
        retry_interval=1,  # optional, seconds between retries, defaults to 1
    )

    byteplussdkcore.Configuration.set_default(configuration)
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

Env-aware example:

```python
import os
import byteplussdkcore
from byteplussdkcore.auth.providers.sts_oidc_provider import StsOidcCredentialProvider

os.environ["BYTEPLUS_OIDC_ROLE_TRN"] = "trn:iam::1234567890:role/oidc-role"
os.environ["BYTEPLUS_OIDC_TOKEN_FILE"] = "/var/run/secrets/oidc/token"

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = StsOidcCredentialProvider()
byteplussdkcore.Configuration.set_default(configuration)
```

### STS AssumeRoleWithSaml

STS AssumeRoleWithSaml obtains temporary credentials via a SAML assertion.

Role TRN resolution (same style as OIDC):

- `role_trn` (explicit) takes priority.
- Otherwise `role_name + account_id` is assembled into `trn:iam::{account_id}:role/{role_name}`.

SAML Provider TRN resolution:

- `saml_provider_trn` (explicit) takes priority.
- Otherwise `account_id + provider_name` is assembled into `trn:iam::{account_id}:saml-provider/{provider_name}`.
- When only `role_trn + provider_name` are passed, `account_id` is parsed out of `role_trn` and combined with `provider_name`.

```python
from __future__ import print_function
import byteplussdkcore
import byteplussdkvpc
from byteplussdkcore.rest import ApiException
from byteplussdkcore.auth.providers.sts_saml_provider import StsSamlCredentialProvider

if __name__ == '__main__':
    configuration = byteplussdkcore.Configuration()
    configuration.region = "ap-southeast-1"

    configuration.credential_provider = StsSamlCredentialProvider(
        role_name="Your role name",
        account_id="Your account id",
        # Alternatively, pass the full role_trn directly (overrides role_name + account_id):
        # role_trn="trn:iam::2110400000:role/role123",
        provider_name="your provider name",
        # Alternatively, pass the full saml_provider_trn directly (overrides account_id + provider_name):
        # saml_provider_trn="trn:iam::2110400000:saml-provider/provider123",
        saml_resp="your saml resp",
        duration_seconds=3600,
        scheme="https",
        host="sts.byteplusapi.com",
        region="ap-southeast-1",
        timeout=30,
        expired_buffer_seconds=60,
        policy='{"Statement":[{"Effect":"Allow","Action":["vpc:CreateVpc"],"Resource":["*"],"Condition":{"StringEquals":{"byteplus:RequestedRegion":["ap-southeast-1"]}}}]}',
        max_retries=3,     # optional, HTTP retry attempts (min 1), defaults to 3
        retry_interval=1,  # optional, seconds between retries, defaults to 1
    )

    byteplussdkcore.Configuration.set_default(configuration)
    api_instance = byteplussdkvpc.VPCApi()
    create_vpc_request = byteplussdkvpc.CreateVpcRequest(
        cidr_block="192.168.0.0/16",
        dns_servers=["10.0.0.1", "10.1.1.2"],
    )

    try:
        api_instance.create_vpc(create_vpc_request)
    except ApiException:
        pass
```

### Environment Variable Credential Provider

`EnvironmentVariableCredentialProvider` reads credentials from:

- `BYTEPLUS_ACCESSKEY` / `BYTEPLUS_ACCESS_KEY`
- `BYTEPLUS_SECRETKEY` / `BYTEPLUS_SECRET_KEY`
- `BYTEPLUS_SESSION_TOKEN` (optional)

```python
import os
import byteplussdkcore
from byteplussdkcore.auth.providers.env_provider import EnvironmentVariableCredentialProvider

os.environ["BYTEPLUS_ACCESSKEY"] = "YourAK"
os.environ["BYTEPLUS_SECRETKEY"] = "YourSK"

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = EnvironmentVariableCredentialProvider()
byteplussdkcore.Configuration.set_default(configuration)
```

### CLI Config Credential Provider

`CLIConfigCredentialProvider` reads `~/.byteplus/config.json` by default.

- Config path priority: constructor `config_path` > `BYTEPLUS_CLI_CONFIG_FILE` > `~/.byteplus/config.json`
- Profile priority: constructor `profile_name` > `BYTEPLUS_PROFILE` > `current` in config > `default`

Supported modes in profile (case-insensitive):

- `AK` / empty
- `StsToken`
- `RamRoleArn` (delegates to `StsCredentialProvider`)
- `OIDC` (delegates to `StsOidcCredentialProvider`)
- `EcsRole` (delegates to `EcsRoleCredentialProvider`)
- `SSO` (delegates to `SsoCredentialProvider`)
- `console-login` (delegates to `ConsoleLoginCredentialProvider`)
  - Required: `login-session`
  - Run `bp login` first so the CLI writes `mode: "console-login"` and `login-session` into the selected profile.
  - Reads the cache written by the `bp login` CLI command at `<cli-config-dir>/login/cache/<sha1(login_session)>.json`. Refresh is performed automatically via the OAuth `refresh_token` grant when the cached STS credentials are near expiry; the SDK updates its in-memory state only and never writes the cache file.

Example: explicitly use CLI provider with a specified profile and config path.

```python
import os

import byteplussdkcore
from byteplussdkcore.auth.providers.cli_config_provider import CLIConfigCredentialProvider

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = CLIConfigCredentialProvider(
    profile_name="prod",
    config_path=os.path.expanduser("~/.byteplus/config.json"),
)
byteplussdkcore.Configuration.set_default(configuration)
```

### Console Login Credential Provider

`ConsoleLoginCredentialProvider` consumes the token cache produced by the
`bp login` command. The CLI runs the interactive OAuth 2.0 Authorization Code +
PKCE flow against `https://signin.byteplus.com` and writes a cache JSON file
containing STS temporary credentials. This provider parses the cache, returns the
embedded STS credentials, and refreshes them via the `refresh_token` grant before
they expire. The SDK never writes the cache file; `bp login` remains the only
disk writer.

- Cache path priority: constructor `cache_path` > constructor `cache_dir` + `<sha1(login_session)>.json` > `BYTEPLUS_LOGIN_CACHE_DIRECTORY` + `<sha1(login_session)>.json` > `<config-dir>/login/cache/<sha1(login_session)>.json`
- Cache file name: `sha1(login_session).hex + ".json"`
- Endpoint URL priority: cache file's `endpoint_url` > `https://signin.byteplus.com`
- Expire buffer: 60 seconds

```python
import os

import byteplussdkcore
from byteplussdkcore.auth.providers.console_login_provider import ConsoleLoginCredentialProvider

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = ConsoleLoginCredentialProvider(
    login_session="trn:signin:::user/your-login-session",
    config_path=os.path.expanduser("~/.byteplus/config.json"),
)
byteplussdkcore.Configuration.set_default(configuration)
```

> Note: Most users do not need to instantiate `ConsoleLoginCredentialProvider` directly. Run `bp login` to set `mode = console-login` in your CLI profile and use `CLIConfigCredentialProvider` (or the default chain) instead.

#### Runtime Refresh Behavior (console-login)

For `console-login` mode the SDK owns refresh in memory and never writes any
local file. Key invariants:

- **Read-only on disk**: `config.json` and
  `~/.byteplus/login/cache/*.json` are read on bootstrap and once more if the
  signin service rejects the in-memory refresh token (`invalid_grant`
  fallback). They are never written by the SDK.
- **In-memory refresh**: when the cached `access_token` is past its expiry
  buffer (60 seconds), the SDK exchanges the cached `refresh_token` at
  `https://signin.byteplus.com/authorize/oauth/token` and updates its
  in-memory state only.
- **Invalid-grant fallback**: on HTTP 400 `invalid_grant`, the SDK re-reads
  the cache file once. If the disk `refresh_token` differs from the in-memory
  one (i.e. `bp login` rotated it under the SDK), the SDK retries with the disk
  refresh token; otherwise it reports an actionable error pointing at
  `bp login`.
- **Refresh-token expiry**: when the SDK exhausts both the in-memory and disk
  refresh tokens, it raises a clear error instructing the user to run
  `bp login`.
- **Concurrency**: a per-process lock serializes refreshes so concurrent
  callers share a single in-flight refresh.

### ECS Role Credential Provider

> 🚨 **Current version limitation**
>
> **Auto-detection of the role name from IMDS is not yet supported in the current release.** You must pass the role name explicitly via the constructor argument or the `BYTEPLUS_ECS_METADATA` environment variable. Auto-detection will be supported in a future version — please watch the release notes.

`EcsRoleCredentialProvider` reads temporary credentials from ECS IMDS.

- `role_name` priority: constructor arg > `BYTEPLUS_ECS_METADATA` > auto-detect from IMDS
- disable switch: `BYTEPLUS_ECS_METADATA_DISABLED=true`

```python
import byteplussdkcore
from byteplussdkcore.auth.providers.ecs_role_provider import EcsRoleCredentialProvider

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = EcsRoleCredentialProvider(role_name="your-ecs-role-name")
byteplussdkcore.Configuration.set_default(configuration)
```

### Default Credential Provider

When `ak`, `sk`, and `credential_provider` are all unset, the SDK automatically uses `DefaultCredentialProvider` — no manual configuration is needed.

You can also explicitly set it if you need to customize options (e.g., `role_name`).

Default chain order:

1. `EnvironmentVariableCredentialProvider`
2. `StsOidcCredentialProvider`
3. `CLIConfigCredentialProvider`
4. `EcsRoleCredentialProvider`

By default, `reuse_last_provider_enabled=True`, so the last successful provider is reused first on later calls.

```python
import byteplussdkcore
from byteplussdkcore.auth.providers.default_provider import DefaultCredentialProvider

configuration = byteplussdkcore.Configuration()
configuration.region = "ap-southeast-1"
configuration.credential_provider = DefaultCredentialProvider()
byteplussdkcore.Configuration.set_default(configuration)
```

---

[← Overview](0-Overview.md) | Credentials[(中文)](1-Credentials-zh.md) | [Endpoint →](2-Endpoint.md)
