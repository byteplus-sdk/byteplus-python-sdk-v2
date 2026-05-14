[← 概览](0-Overview-zh.md) | 环境变量[(English)](EnvironmentVariables.md)

---

## 环境变量

本页集中列出 SDK 支持的所有 credential 相关环境变量，便于部署/CI 环境注入。后续如需新增其他类别（Region、TLS 等），可直接追加章节。

### 设置方法

#### Linux / macOS

临时（当前 shell 生效）：

```shell
export BYTEPLUS_ACCESS_KEY=your-ak
export BYTEPLUS_SECRET_KEY=your-sk
export BYTEPLUS_SESSION_TOKEN=your-session-token
```

持久化：将 `export` 写入 `~/.bashrc`、`~/.zshrc` 等 shell 启动文件。

校验：`echo $BYTEPLUS_ACCESS_KEY` 返回预期值即设置成功。

#### Windows

命令行（以管理员身份运行）：

```cmd
setx BYTEPLUS_ACCESS_KEY your-ak /M
setx BYTEPLUS_SECRET_KEY your-sk /M
setx BYTEPLUS_SESSION_TOKEN your-session-token /M
```

`/M` 表示系统级；省略 `/M` 为用户级变量。

图形界面：**此电脑** 右键 → **属性** → **高级系统设置** → **环境变量** → **新建**。

校验：新开命令提示符执行 `echo %BYTEPLUS_ACCESS_KEY%`。

### Credentials

#### 基础 AK/SK/Token

| 变量 | 说明 | 必填 |
|---|---|:-:|
| `BYTEPLUS_ACCESS_KEY` | Access Key | ✅ |
| `BYTEPLUS_SECRET_KEY` | Secret Key | ✅ |
| `BYTEPLUS_SESSION_TOKEN` | STS 临时凭证 Session Token | ❌ |

#### OIDC（AssumeRoleWithOIDC）

| 变量 | 说明 | 必填 |
|---|---|:-:|
| `BYTEPLUS_OIDC_ROLE_TRN` | OIDC 扮演角色 TRN | ✅ |
| `BYTEPLUS_OIDC_TOKEN_FILE` | OIDC Token 文件路径 | ✅ |
| `BYTEPLUS_OIDC_ROLE_SESSION_NAME` | Session 名 | ❌ |
| `BYTEPLUS_OIDC_ROLE_POLICY` | 会话权限策略 JSON | ❌ |
| `BYTEPLUS_OIDC_STS_ENDPOINT` | STS 域名 | ❌ |

#### ECS IMDS

| 变量 | 说明 |
|---|---|
| `BYTEPLUS_ECS_METADATA` | 指定 ECS 实例角色名；不设置则从 IMDS 自动探测 |
| `BYTEPLUS_ECS_METADATA_DISABLED` | 设为 `true` 禁用 IMDS 凭证获取 |

#### CLI 配置文件

| 变量 | 说明 |
|---|---|
| `BYTEPLUS_CLI_CONFIG_FILE` | 配置文件路径，默认 `~/.byteplus/config.json` |
| `BYTEPLUS_PROFILE` | 使用的 profile 名 |

#### 历史兼容变量（`BYTEPLUS_*`）

早期 SDK 使用 `BYTEPLUS_*` 前缀。当同名 `BYTEPLUS_*` 变量未设置时，下列变量会作为 fallback 生效。**新代码请统一使用 `BYTEPLUS_*`。**

| 变量 | 等价的 `BYTEPLUS_*` | Go | Java | PHP | Python |
|---|---|:-:|:-:|:-:|:-:|
| `BYTEPLUS_ACCESS_KEY_ID` / `BYTEPLUS_ACCESS_KEY` | `BYTEPLUS_ACCESS_KEY` | ✅ | ❌ | ✅ | ❌ |
| `BYTEPLUS_SECRET_ACCESS_KEY` / `BYTEPLUS_SECRET_KEY` | `BYTEPLUS_SECRET_KEY` | ✅ | ❌ | ✅ | ❌ |
| `BYTEPLUS_SESSION_TOKEN` | `BYTEPLUS_SESSION_TOKEN` | ✅ | ❌ | ✅ | ❌ |
| `BYTEPLUS_PROFILE` | `BYTEPLUS_PROFILE` | ✅ | ❌ | ✅ | ❌ |

> Go SDK 另有少量历史遗留 `BYTEPLUS_*` 变量（共享凭证文件路径、AssumeRole 角色等），未列入本页；建议迁移到本页列出的 `BYTEPLUS_*` 接口。

#### 默认凭证链顺序

未显式配置凭证时，四端 SDK 均按以下顺序依次尝试，首个成功的 Provider 生效：

1. 环境变量 Provider（`BYTEPLUS_ACCESS_KEY` / `BYTEPLUS_SECRET_KEY`[/`BYTEPLUS_SESSION_TOKEN`]）
2. OIDC Provider（从 `BYTEPLUS_OIDC_*` 读取）
3. CLI 配置 Provider（`~/.byteplus/config.json`）
4. ECS IMDS Provider

#### 优先级总表

| 项 | 优先级（高 → 低） |
|---|---|
| CLI 配置文件路径 | 构造参数 > `BYTEPLUS_CLI_CONFIG_FILE` > `~/.byteplus/config.json` |
| Profile | 构造参数 > `BYTEPLUS_PROFILE` > `BYTEPLUS_PROFILE`（仅 Go/PHP）> 配置中的 `current` > `default` |
| ECS Role 名称 | 构造参数 > `BYTEPLUS_ECS_METADATA` > IMDS 自动探测 |

### 相关文档

- [访问凭据](1-Credentials-zh.md) — 各 Provider 的代码级用法

---

[← 概览](0-Overview-zh.md) | 环境变量[(English)](EnvironmentVariables.md)
