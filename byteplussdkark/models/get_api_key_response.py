# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class GetApiKeyResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_key': 'str',
        'expired_time': 'int'
    }

    attribute_map = {
        'api_key': 'ApiKey',
        'expired_time': 'ExpiredTime'
    }

    def __init__(self, api_key=None, expired_time=None, _configuration=None):  # noqa: E501
        """GetApiKeyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_key = None
        self._expired_time = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def api_key(self):
        """Gets the api_key of this GetApiKeyResponse.  # noqa: E501


        :return: The api_key of this GetApiKeyResponse.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this GetApiKeyResponse.


        :param api_key: The api_key of this GetApiKeyResponse.  # noqa: E501
        :type: str
        """

        self._api_key = api_key

    @property
    def expired_time(self):
        """Gets the expired_time of this GetApiKeyResponse.  # noqa: E501


        :return: The expired_time of this GetApiKeyResponse.  # noqa: E501
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        """Sets the expired_time of this GetApiKeyResponse.


        :param expired_time: The expired_time of this GetApiKeyResponse.  # noqa: E501
        :type: int
        """

        self._expired_time = expired_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GetApiKeyResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GetApiKeyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetApiKeyResponse):
            return True

        return self.to_dict() != other.to_dict()
