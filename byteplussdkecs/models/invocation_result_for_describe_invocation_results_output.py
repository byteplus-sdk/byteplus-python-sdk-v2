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


class InvocationResultForDescribeInvocationResultsOutput(object):
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
        'command_id': 'str',
        'end_time': 'str',
        'error_code': 'str',
        'error_message': 'str',
        'exit_code': 'int',
        'instance_id': 'str',
        'invocation_id': 'str',
        'invocation_result_id': 'str',
        'invocation_result_status': 'str',
        'output': 'str',
        'start_time': 'str',
        'username': 'str'
    }

    attribute_map = {
        'command_id': 'CommandId',
        'end_time': 'EndTime',
        'error_code': 'ErrorCode',
        'error_message': 'ErrorMessage',
        'exit_code': 'ExitCode',
        'instance_id': 'InstanceId',
        'invocation_id': 'InvocationId',
        'invocation_result_id': 'InvocationResultId',
        'invocation_result_status': 'InvocationResultStatus',
        'output': 'Output',
        'start_time': 'StartTime',
        'username': 'Username'
    }

    def __init__(self, command_id=None, end_time=None, error_code=None, error_message=None, exit_code=None, instance_id=None, invocation_id=None, invocation_result_id=None, invocation_result_status=None, output=None, start_time=None, username=None, _configuration=None):  # noqa: E501
        """InvocationResultForDescribeInvocationResultsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_id = None
        self._end_time = None
        self._error_code = None
        self._error_message = None
        self._exit_code = None
        self._instance_id = None
        self._invocation_id = None
        self._invocation_result_id = None
        self._invocation_result_status = None
        self._output = None
        self._start_time = None
        self._username = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if exit_code is not None:
            self.exit_code = exit_code
        if instance_id is not None:
            self.instance_id = instance_id
        if invocation_id is not None:
            self.invocation_id = invocation_id
        if invocation_result_id is not None:
            self.invocation_result_id = invocation_result_id
        if invocation_result_status is not None:
            self.invocation_result_status = invocation_result_status
        if output is not None:
            self.output = output
        if start_time is not None:
            self.start_time = start_time
        if username is not None:
            self.username = username

    @property
    def command_id(self):
        """Gets the command_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The command_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this InvocationResultForDescribeInvocationResultsOutput.


        :param command_id: The command_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._command_id = command_id

    @property
    def end_time(self):
        """Gets the end_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The end_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InvocationResultForDescribeInvocationResultsOutput.


        :param end_time: The end_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The error_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this InvocationResultForDescribeInvocationResultsOutput.


        :param error_code: The error_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The error_message of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this InvocationResultForDescribeInvocationResultsOutput.


        :param error_message: The error_message of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def exit_code(self):
        """Gets the exit_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The exit_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this InvocationResultForDescribeInvocationResultsOutput.


        :param exit_code: The exit_code of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: int
        """

        self._exit_code = exit_code

    @property
    def instance_id(self):
        """Gets the instance_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The instance_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InvocationResultForDescribeInvocationResultsOutput.


        :param instance_id: The instance_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def invocation_id(self):
        """Gets the invocation_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The invocation_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        """Sets the invocation_id of this InvocationResultForDescribeInvocationResultsOutput.


        :param invocation_id: The invocation_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_id = invocation_id

    @property
    def invocation_result_id(self):
        """Gets the invocation_result_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The invocation_result_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_result_id

    @invocation_result_id.setter
    def invocation_result_id(self, invocation_result_id):
        """Sets the invocation_result_id of this InvocationResultForDescribeInvocationResultsOutput.


        :param invocation_result_id: The invocation_result_id of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_result_id = invocation_result_id

    @property
    def invocation_result_status(self):
        """Gets the invocation_result_status of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The invocation_result_status of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._invocation_result_status

    @invocation_result_status.setter
    def invocation_result_status(self, invocation_result_status):
        """Sets the invocation_result_status of this InvocationResultForDescribeInvocationResultsOutput.


        :param invocation_result_status: The invocation_result_status of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._invocation_result_status = invocation_result_status

    @property
    def output(self):
        """Gets the output of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The output of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this InvocationResultForDescribeInvocationResultsOutput.


        :param output: The output of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._output = output

    @property
    def start_time(self):
        """Gets the start_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The start_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InvocationResultForDescribeInvocationResultsOutput.


        :param start_time: The start_time of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def username(self):
        """Gets the username of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501


        :return: The username of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InvocationResultForDescribeInvocationResultsOutput.


        :param username: The username of this InvocationResultForDescribeInvocationResultsOutput.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(InvocationResultForDescribeInvocationResultsOutput, dict):
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
        if not isinstance(other, InvocationResultForDescribeInvocationResultsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvocationResultForDescribeInvocationResultsOutput):
            return True

        return self.to_dict() != other.to_dict()
