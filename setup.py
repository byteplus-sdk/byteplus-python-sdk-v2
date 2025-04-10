# coding: utf-8

from setuptools import setup, find_packages  # noqa: H301

NAME = "byteplus-python-sdk-v2"
VERSION = "1.0.9"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    description='Byteplus SDK for Python',
    license="Apache License 2.0",
    platforms='any',
    extras_require={
        "ark": [
            "cryptography>=43.0.3, <43.0.4"
        ]
    },
)
