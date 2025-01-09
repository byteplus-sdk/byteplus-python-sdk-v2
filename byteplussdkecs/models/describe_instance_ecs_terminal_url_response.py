# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class DescribeInstanceECSTerminalUrlResponse(object):
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
        'ecs_terminal_url': 'str'
    }

    attribute_map = {
        'ecs_terminal_url': 'EcsTerminalUrl'
    }

    def __init__(self, ecs_terminal_url=None, _configuration=None):  # noqa: E501
        """DescribeInstanceECSTerminalUrlResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ecs_terminal_url = None
        self.discriminator = None

        if ecs_terminal_url is not None:
            self.ecs_terminal_url = ecs_terminal_url

    @property
    def ecs_terminal_url(self):
        """Gets the ecs_terminal_url of this DescribeInstanceECSTerminalUrlResponse.  # noqa: E501


        :return: The ecs_terminal_url of this DescribeInstanceECSTerminalUrlResponse.  # noqa: E501
        :rtype: str
        """
        return self._ecs_terminal_url

    @ecs_terminal_url.setter
    def ecs_terminal_url(self, ecs_terminal_url):
        """Sets the ecs_terminal_url of this DescribeInstanceECSTerminalUrlResponse.


        :param ecs_terminal_url: The ecs_terminal_url of this DescribeInstanceECSTerminalUrlResponse.  # noqa: E501
        :type: str
        """

        self._ecs_terminal_url = ecs_terminal_url

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
        if issubclass(DescribeInstanceECSTerminalUrlResponse, dict):
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
        if not isinstance(other, DescribeInstanceECSTerminalUrlResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceECSTerminalUrlResponse):
            return True

        return self.to_dict() != other.to_dict()
