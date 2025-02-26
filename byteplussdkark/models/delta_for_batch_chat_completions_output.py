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


class DeltaForBatchChatCompletionsOutput(object):
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
        'content': 'str',
        'role': 'str',
        'tool_calls': 'list[ToolCallForBatchChatCompletionsOutput]'
    }

    attribute_map = {
        'content': 'content',
        'role': 'role',
        'tool_calls': 'tool_calls'
    }

    def __init__(self, content=None, role=None, tool_calls=None, _configuration=None):  # noqa: E501
        """DeltaForBatchChatCompletionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._role = None
        self._tool_calls = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if role is not None:
            self.role = role
        if tool_calls is not None:
            self.tool_calls = tool_calls

    @property
    def content(self):
        """Gets the content of this DeltaForBatchChatCompletionsOutput.  # noqa: E501


        :return: The content of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DeltaForBatchChatCompletionsOutput.


        :param content: The content of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def role(self):
        """Gets the role of this DeltaForBatchChatCompletionsOutput.  # noqa: E501


        :return: The role of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DeltaForBatchChatCompletionsOutput.


        :param role: The role of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def tool_calls(self):
        """Gets the tool_calls of this DeltaForBatchChatCompletionsOutput.  # noqa: E501


        :return: The tool_calls of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :rtype: list[ToolCallForBatchChatCompletionsOutput]
        """
        return self._tool_calls

    @tool_calls.setter
    def tool_calls(self, tool_calls):
        """Sets the tool_calls of this DeltaForBatchChatCompletionsOutput.


        :param tool_calls: The tool_calls of this DeltaForBatchChatCompletionsOutput.  # noqa: E501
        :type: list[ToolCallForBatchChatCompletionsOutput]
        """

        self._tool_calls = tool_calls

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
        if issubclass(DeltaForBatchChatCompletionsOutput, dict):
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
        if not isinstance(other, DeltaForBatchChatCompletionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeltaForBatchChatCompletionsOutput):
            return True

        return self.to_dict() != other.to_dict()
