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


class GetConsoleOutputResponse(object):
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
        'instance_id': 'str',
        'last_update_at': 'str',
        'output': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'last_update_at': 'LastUpdateAt',
        'output': 'Output'
    }

    def __init__(self, instance_id=None, last_update_at=None, output=None, _configuration=None):  # noqa: E501
        """GetConsoleOutputResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._last_update_at = None
        self._output = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if last_update_at is not None:
            self.last_update_at = last_update_at
        if output is not None:
            self.output = output

    @property
    def instance_id(self):
        """Gets the instance_id of this GetConsoleOutputResponse.  # noqa: E501


        :return: The instance_id of this GetConsoleOutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this GetConsoleOutputResponse.


        :param instance_id: The instance_id of this GetConsoleOutputResponse.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def last_update_at(self):
        """Gets the last_update_at of this GetConsoleOutputResponse.  # noqa: E501


        :return: The last_update_at of this GetConsoleOutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_update_at

    @last_update_at.setter
    def last_update_at(self, last_update_at):
        """Sets the last_update_at of this GetConsoleOutputResponse.


        :param last_update_at: The last_update_at of this GetConsoleOutputResponse.  # noqa: E501
        :type: str
        """

        self._last_update_at = last_update_at

    @property
    def output(self):
        """Gets the output of this GetConsoleOutputResponse.  # noqa: E501


        :return: The output of this GetConsoleOutputResponse.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this GetConsoleOutputResponse.


        :param output: The output of this GetConsoleOutputResponse.  # noqa: E501
        :type: str
        """

        self._output = output

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
        if issubclass(GetConsoleOutputResponse, dict):
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
        if not isinstance(other, GetConsoleOutputResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetConsoleOutputResponse):
            return True

        return self.to_dict() != other.to_dict()
