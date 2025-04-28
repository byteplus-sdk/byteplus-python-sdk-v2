# byteplus SDK for Python

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
