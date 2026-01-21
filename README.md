# byteplus SDK for Python

## ⚠️ 已知缺陷说明（历史版本）

在 **byteplus-python-sdk-v2** 的部分历史版本（**3.0.1 ～ 3.0.23，含**）中，发现 SDK 内置的重试机制存在缺陷。

当请求过程中出现异常（如网络抖动、接口返回错误等）时，SDK 虽会触发重试逻辑，但由于该缺陷，重试未能实际生效，客户端仍可能直接感知到首次请求异常，导致重试机制无法有效提升请求成功率。

### 影响范围

- **SDK**：byteplus-python-sdk-v2  
- **受影响版本**：3.0.1 ～ 3.0.23（含）

### 影响说明

对于依赖 SDK 内置重试机制来应对瞬时异常或网络不稳定场景的业务：

- 实际请求可用性可能低于预期  
- 重试相关配置无法发挥应有的保障作用  

### 解决方案与建议

该问题已在 **3.0.24 及以上版本**中修复。  
**强烈建议所有用户升级至 byteplus-python-sdk-v2 ≥ 3.0.24**，以确保请求重试机制在异常场景下能够正常生效。

## 非兼容升级通知

Byteplus SDK for Python 非兼容升级通知

影响版本：`2.0.1` 以及后续版本

变更描述:

从 `2.0.1` 版本开始，发起请求将默认从使用 `HTTP` 协议变成使用 `HTTPS` 协议，请升级到新版本的用户注意是否会产生兼容性风险，做好充分测试。如需继续使用
`HTTP` 协议，请在发起请求时指定 `scheme` 参数为 `http`(不推荐):

```python
import byteplussdkcore

configuration = byteplussdkcore.Configuration()
configuration.scheme = 'http'
```

## Table of Contents

* Requirements
* Install
* Usage

### Requirements ###

Python version >=2.7。

### Install ###

Install via pip

```sh
pip install byteplus-python-sdk-v2
```

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

### Usage ###

1：config Configuration

```python
configuration = byteplussdkcore.Configuration()
configuration.client_side_validation = True
configuration.schema = "http"
configuration.debug = False
configuration.logger_file = "sdk.log"

byteplussdkcore.Configuration.set_default(configuration)
```
