# byteplus SDK for Python

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
