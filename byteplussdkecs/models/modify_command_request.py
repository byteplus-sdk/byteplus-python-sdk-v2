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


class ModifyCommandRequest(object):
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
        'command_content': 'str',
        'command_id': 'str',
        'content_encoding': 'str',
        'description': 'str',
        'enable_parameter': 'bool',
        'name': 'str',
        'parameter_definitions': 'list[ParameterDefinitionForModifyCommandInput]',
        'timeout': 'int',
        'type': 'str',
        'username': 'str',
        'working_dir': 'str'
    }

    attribute_map = {
        'command_content': 'CommandContent',
        'command_id': 'CommandId',
        'content_encoding': 'ContentEncoding',
        'description': 'Description',
        'enable_parameter': 'EnableParameter',
        'name': 'Name',
        'parameter_definitions': 'ParameterDefinitions',
        'timeout': 'Timeout',
        'type': 'Type',
        'username': 'Username',
        'working_dir': 'WorkingDir'
    }

    def __init__(self, command_content=None, command_id=None, content_encoding=None, description=None, enable_parameter=None, name=None, parameter_definitions=None, timeout=None, type=None, username=None, working_dir=None, _configuration=None):  # noqa: E501
        """ModifyCommandRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_content = None
        self._command_id = None
        self._content_encoding = None
        self._description = None
        self._enable_parameter = None
        self._name = None
        self._parameter_definitions = None
        self._timeout = None
        self._type = None
        self._username = None
        self._working_dir = None
        self.discriminator = None

        if command_content is not None:
            self.command_content = command_content
        if command_id is not None:
            self.command_id = command_id
        if content_encoding is not None:
            self.content_encoding = content_encoding
        if description is not None:
            self.description = description
        if enable_parameter is not None:
            self.enable_parameter = enable_parameter
        if name is not None:
            self.name = name
        if parameter_definitions is not None:
            self.parameter_definitions = parameter_definitions
        if timeout is not None:
            self.timeout = timeout
        if type is not None:
            self.type = type
        if username is not None:
            self.username = username
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def command_content(self):
        """Gets the command_content of this ModifyCommandRequest.  # noqa: E501


        :return: The command_content of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_content

    @command_content.setter
    def command_content(self, command_content):
        """Sets the command_content of this ModifyCommandRequest.


        :param command_content: The command_content of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._command_content = command_content

    @property
    def command_id(self):
        """Gets the command_id of this ModifyCommandRequest.  # noqa: E501


        :return: The command_id of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this ModifyCommandRequest.


        :param command_id: The command_id of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._command_id = command_id

    @property
    def content_encoding(self):
        """Gets the content_encoding of this ModifyCommandRequest.  # noqa: E501


        :return: The content_encoding of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """Sets the content_encoding of this ModifyCommandRequest.


        :param content_encoding: The content_encoding of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._content_encoding = content_encoding

    @property
    def description(self):
        """Gets the description of this ModifyCommandRequest.  # noqa: E501


        :return: The description of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyCommandRequest.


        :param description: The description of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enable_parameter(self):
        """Gets the enable_parameter of this ModifyCommandRequest.  # noqa: E501


        :return: The enable_parameter of this ModifyCommandRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_parameter

    @enable_parameter.setter
    def enable_parameter(self, enable_parameter):
        """Sets the enable_parameter of this ModifyCommandRequest.


        :param enable_parameter: The enable_parameter of this ModifyCommandRequest.  # noqa: E501
        :type: bool
        """

        self._enable_parameter = enable_parameter

    @property
    def name(self):
        """Gets the name of this ModifyCommandRequest.  # noqa: E501


        :return: The name of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModifyCommandRequest.


        :param name: The name of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parameter_definitions(self):
        """Gets the parameter_definitions of this ModifyCommandRequest.  # noqa: E501


        :return: The parameter_definitions of this ModifyCommandRequest.  # noqa: E501
        :rtype: list[ParameterDefinitionForModifyCommandInput]
        """
        return self._parameter_definitions

    @parameter_definitions.setter
    def parameter_definitions(self, parameter_definitions):
        """Sets the parameter_definitions of this ModifyCommandRequest.


        :param parameter_definitions: The parameter_definitions of this ModifyCommandRequest.  # noqa: E501
        :type: list[ParameterDefinitionForModifyCommandInput]
        """

        self._parameter_definitions = parameter_definitions

    @property
    def timeout(self):
        """Gets the timeout of this ModifyCommandRequest.  # noqa: E501


        :return: The timeout of this ModifyCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this ModifyCommandRequest.


        :param timeout: The timeout of this ModifyCommandRequest.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def type(self):
        """Gets the type of this ModifyCommandRequest.  # noqa: E501


        :return: The type of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModifyCommandRequest.


        :param type: The type of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def username(self):
        """Gets the username of this ModifyCommandRequest.  # noqa: E501


        :return: The username of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ModifyCommandRequest.


        :param username: The username of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def working_dir(self):
        """Gets the working_dir of this ModifyCommandRequest.  # noqa: E501


        :return: The working_dir of this ModifyCommandRequest.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this ModifyCommandRequest.


        :param working_dir: The working_dir of this ModifyCommandRequest.  # noqa: E501
        :type: str
        """

        self._working_dir = working_dir

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
        if issubclass(ModifyCommandRequest, dict):
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
        if not isinstance(other, ModifyCommandRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyCommandRequest):
            return True

        return self.to_dict() != other.to_dict()
