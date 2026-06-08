[← Overview](0-Overview.md) | Environment Variables[(中文)](EnvironmentVariables-zh.md)

---

## Environment Variables

This page consolidates all credential-related environment variables supported by the SDK, for easy deployment / CI injection. Other categories (Region, TLS, etc.) can be appended here as new sections later.

### How to Set

#### Linux / macOS

Temporary (current shell only):

```shell
export BYTEPLUS_ACCESS_KEY=your-ak
export BYTEPLUS_SECRET_KEY=your-sk
export BYTEPLUS_SESSION_TOKEN=your-session-token
```

To persist, put the `export` lines in `~/.bashrc`, `~/.zshrc`, or your shell's startup file.

Verify with `echo $BYTEPLUS_ACCESS_KEY`.

#### Windows

Command line (run as Administrator):

```cmd
setx BYTEPLUS_ACCESS_KEY your-ak /M
setx BYTEPLUS_SECRET_KEY your-sk /M
setx BYTEPLUS_SESSION_TOKEN your-session-token /M
```

## Credentials

#### Basic AK/SK/Token

| Variable | Description | Required |
|---|---|:-:|
| `BYTEPLUS_ACCESS_KEY` | Access Key | ✅ |
| `BYTEPLUS_SECRET_KEY` | Secret Key | ✅ |
| `BYTEPLUS_SESSION_TOKEN` | STS session token | ❌ |

#### OIDC (AssumeRoleWithOIDC)

| Variable | Description | Required |
|---|---|:-:|
| `BYTEPLUS_OIDC_ROLE_TRN` | OIDC role TRN | ✅ |
| `BYTEPLUS_OIDC_TOKEN_FILE` | OIDC token file path | ✅ |
| `BYTEPLUS_OIDC_ROLE_SESSION_NAME` | Session name | ❌ |
| `BYTEPLUS_OIDC_ROLE_POLICY` | Session policy JSON | ❌ |
| `BYTEPLUS_OIDC_STS_ENDPOINT` | STS endpoint host | ❌ |

#### ECS IMDS

| Variable | Description |
|---|---|
| `BYTEPLUS_ECS_METADATA` | ECS instance role name; if unset, auto-discovered from IMDS |
| `BYTEPLUS_ECS_METADATA_DISABLED` | Set to `true` to disable IMDS credential retrieval |

#### CLI Config File

| Variable | Description |
|---|---|
| `BYTEPLUS_CLI_CONFIG_FILE` | Config file path; defaults to `~/.byteplus/config.json` |
| `BYTEPLUS_PROFILE` | Profile name to use |
| `BYTEPLUS_LOGIN_CACHE_DIRECTORY` | Console-login token cache directory; defaults to `<cli-config-dir>/login/cache` |

### Default Credential Chain

When no credentials are explicitly configured, all four SDKs try the following providers in order; the first one that succeeds is used:

1. Environment Variable Provider (`BYTEPLUS_ACCESS_KEY` / `BYTEPLUS_SECRET_KEY`[/`BYTEPLUS_SESSION_TOKEN`])
2. OIDC Provider (reads `BYTEPLUS_OIDC_*`)
3. CLI Config Provider (`~/.byteplus/config.json`)
4. ECS IMDS Provider

#### Priority Summary

| Item | Priority (high → low) |
|---|---|
| CLI config file path | constructor arg > `BYTEPLUS_CLI_CONFIG_FILE` > `~/.byteplus/config.json` |
| Profile | constructor arg > `BYTEPLUS_PROFILE` > `current` field in config > `default` |
| Console-login cache path | constructor `cache_path` > `BYTEPLUS_LOGIN_CACHE_DIRECTORY` + `<sha1(login_session)>.json` > `<cli-config-dir>/login/cache/<sha1(login_session)>.json` |
| ECS role name | constructor arg > `BYTEPLUS_ECS_METADATA` > IMDS auto-discovery |

### See Also

- [Credentials](1-Credentials.md) — Per-provider code-level usage

---

[← Overview](0-Overview.md) | Environment Variables[(中文)](EnvironmentVariables-zh.md)
