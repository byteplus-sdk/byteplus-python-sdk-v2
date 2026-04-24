[← Debugging](7-Debugging.md)

---

# Environment Variables

This page consolidates all credential-related environment variables supported by the SDK, for easy deployment / CI injection.

## How to Set

### Linux / macOS

Temporary (current shell only):

```shell
export BYTEPLUS_ACCESSKEY=your-ak
export BYTEPLUS_SECRETKEY=your-sk
export BYTEPLUS_SESSION_TOKEN=your-session-token
```

To persist, put the `export` lines in `~/.bashrc`, `~/.zshrc`, or your shell's startup file.

Verify with `echo $BYTEPLUS_ACCESSKEY`.

### Windows

Command line (run as Administrator):

```cmd
setx BYTEPLUS_ACCESSKEY your-ak /M
setx BYTEPLUS_SECRETKEY your-sk /M
setx BYTEPLUS_SESSION_TOKEN your-session-token /M
```

## Credentials

### Basic AK/SK/Token

| Variable | Description | Required |
|---|---|:-:|
| `BYTEPLUS_ACCESSKEY` | Access Key | ✅ |
| `BYTEPLUS_SECRETKEY` | Secret Key | ✅ |
| `BYTEPLUS_SESSION_TOKEN` | STS session token | ❌ |

### OIDC (AssumeRoleWithOIDC)

| Variable | Description | Required |
|---|---|:-:|
| `BYTEPLUS_OIDC_ROLE_TRN` | OIDC role TRN | ✅ |
| `BYTEPLUS_OIDC_TOKEN_FILE` | OIDC token file path | ✅ |
| `BYTEPLUS_OIDC_ROLE_SESSION_NAME` | Session name | ❌ |
| `BYTEPLUS_OIDC_ROLE_POLICY` | Session policy JSON | ❌ |
| `BYTEPLUS_OIDC_STS_ENDPOINT` | STS endpoint host | ❌ |

### ECS IMDS

| Variable | Description |
|---|---|
| `BYTEPLUS_ECS_METADATA` | ECS instance role name; if unset, auto-discovered from IMDS |
| `BYTEPLUS_ECS_METADATA_DISABLED` | Set to `true` to disable IMDS credential retrieval |

### CLI Config File

| Variable | Description |
|---|---|
| `BYTEPLUS_CLI_CONFIG_FILE` | Config file path; defaults to `~/.byteplus/config.json` |
| `BYTEPLUS_PROFILE` | Profile name to use |

### Default Credential Chain

When no credentials are explicitly configured, all four SDKs try the following providers in order; the first one that succeeds is used:

1. Environment Variable Provider (`BYTEPLUS_ACCESSKEY` / `BYTEPLUS_SECRETKEY`[/`BYTEPLUS_SESSION_TOKEN`])
2. OIDC Provider (reads `BYTEPLUS_OIDC_*`)
3. CLI Config Provider (`~/.byteplus/config.json`)
4. ECS IMDS Provider

## See Also

- [Credentials](1-Credentials.md) — Per-provider code-level usage

---

[← Debugging](7-Debugging.md)
