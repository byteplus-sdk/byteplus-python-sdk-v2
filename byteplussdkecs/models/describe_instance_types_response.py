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


class DescribeInstanceTypesResponse(object):
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
        'instance_types': 'list[InstanceTypeForDescribeInstanceTypesOutput]',
        'next_token': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'instance_types': 'InstanceTypes',
        'next_token': 'NextToken',
        'total_count': 'TotalCount'
    }

    def __init__(self, instance_types=None, next_token=None, total_count=None, _configuration=None):  # noqa: E501
        """DescribeInstanceTypesResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_types = None
        self._next_token = None
        self._total_count = None
        self.discriminator = None

        if instance_types is not None:
            self.instance_types = instance_types
        if next_token is not None:
            self.next_token = next_token
        if total_count is not None:
            self.total_count = total_count

    @property
    def instance_types(self):
        """Gets the instance_types of this DescribeInstanceTypesResponse.  # noqa: E501


        :return: The instance_types of this DescribeInstanceTypesResponse.  # noqa: E501
        :rtype: list[InstanceTypeForDescribeInstanceTypesOutput]
        """
        return self._instance_types

    @instance_types.setter
    def instance_types(self, instance_types):
        """Sets the instance_types of this DescribeInstanceTypesResponse.


        :param instance_types: The instance_types of this DescribeInstanceTypesResponse.  # noqa: E501
        :type: list[InstanceTypeForDescribeInstanceTypesOutput]
        """

        self._instance_types = instance_types

    @property
    def next_token(self):
        """Gets the next_token of this DescribeInstanceTypesResponse.  # noqa: E501


        :return: The next_token of this DescribeInstanceTypesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeInstanceTypesResponse.


        :param next_token: The next_token of this DescribeInstanceTypesResponse.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def total_count(self):
        """Gets the total_count of this DescribeInstanceTypesResponse.  # noqa: E501


        :return: The total_count of this DescribeInstanceTypesResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this DescribeInstanceTypesResponse.


        :param total_count: The total_count of this DescribeInstanceTypesResponse.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(DescribeInstanceTypesResponse, dict):
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
        if not isinstance(other, DescribeInstanceTypesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceTypesResponse):
            return True

        return self.to_dict() != other.to_dict()
