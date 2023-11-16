# byteplus SDK for Python

## Table of Contents

* Requirements
* Install
* Usage

### Requirements ###

Python版本需要不低于2.7。

### Install ###

Install via pip
```sh
pip install byteplus-python-sdk
```

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)


### Usage ###
步骤一：启动时初始化，配置 Configuration 全局默认参数
```python
configuration = byteplussdkcore.Configuration()
configuration.client_side_validation = True  # 客户端是否进行参数校验
configuration.schema = "http"  # https or http
configuration.debug = False  # 是否开启调试
configuration.logger_file = "sdk.log"

byteplussdkcore.Configuration.set_default(configuration)
```
步骤二：获取 Client
```python
def get_client(ak, sk, region):
    # 包含默认属性
    configuration = byteplussdkcore.Configuration()
    configuration.ak = ak
    configuration.sk = sk
    configuration.region = region
    client = byteplussdkautoscaling.AUTOSCALINGApi(byteplussdkcore.ApiClient(configuration))
    return client
```
