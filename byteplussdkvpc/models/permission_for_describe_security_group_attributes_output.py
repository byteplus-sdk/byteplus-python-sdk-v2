# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class PermissionForDescribeSecurityGroupAttributesOutput(object):
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
        'cidr_ip': 'str',
        'creation_time': 'str',
        'description': 'str',
        'direction': 'str',
        'policy': 'str',
        'port_end': 'int',
        'port_start': 'int',
        'prefix_list_cidrs': 'list[str]',
        'prefix_list_id': 'str',
        'priority': 'int',
        'protocol': 'str',
        'source_group_id': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'cidr_ip': 'CidrIp',
        'creation_time': 'CreationTime',
        'description': 'Description',
        'direction': 'Direction',
        'policy': 'Policy',
        'port_end': 'PortEnd',
        'port_start': 'PortStart',
        'prefix_list_cidrs': 'PrefixListCidrs',
        'prefix_list_id': 'PrefixListId',
        'priority': 'Priority',
        'protocol': 'Protocol',
        'source_group_id': 'SourceGroupId',
        'update_time': 'UpdateTime'
    }

    def __init__(self, cidr_ip=None, creation_time=None, description=None, direction=None, policy=None, port_end=None, port_start=None, prefix_list_cidrs=None, prefix_list_id=None, priority=None, protocol=None, source_group_id=None, update_time=None, _configuration=None):  # noqa: E501
        """PermissionForDescribeSecurityGroupAttributesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cidr_ip = None
        self._creation_time = None
        self._description = None
        self._direction = None
        self._policy = None
        self._port_end = None
        self._port_start = None
        self._prefix_list_cidrs = None
        self._prefix_list_id = None
        self._priority = None
        self._protocol = None
        self._source_group_id = None
        self._update_time = None
        self.discriminator = None

        if cidr_ip is not None:
            self.cidr_ip = cidr_ip
        if creation_time is not None:
            self.creation_time = creation_time
        if description is not None:
            self.description = description
        if direction is not None:
            self.direction = direction
        if policy is not None:
            self.policy = policy
        if port_end is not None:
            self.port_end = port_end
        if port_start is not None:
            self.port_start = port_start
        if prefix_list_cidrs is not None:
            self.prefix_list_cidrs = prefix_list_cidrs
        if prefix_list_id is not None:
            self.prefix_list_id = prefix_list_id
        if priority is not None:
            self.priority = priority
        if protocol is not None:
            self.protocol = protocol
        if source_group_id is not None:
            self.source_group_id = source_group_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def cidr_ip(self):
        """Gets the cidr_ip of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The cidr_ip of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cidr_ip

    @cidr_ip.setter
    def cidr_ip(self, cidr_ip):
        """Sets the cidr_ip of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param cidr_ip: The cidr_ip of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._cidr_ip = cidr_ip

    @property
    def creation_time(self):
        """Gets the creation_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The creation_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param creation_time: The creation_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def description(self):
        """Gets the description of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The description of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param description: The description of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def direction(self):
        """Gets the direction of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The direction of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param direction: The direction of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._direction = direction

    @property
    def policy(self):
        """Gets the policy of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The policy of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param policy: The policy of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def port_end(self):
        """Gets the port_end of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The port_end of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: int
        """
        return self._port_end

    @port_end.setter
    def port_end(self, port_end):
        """Sets the port_end of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param port_end: The port_end of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: int
        """

        self._port_end = port_end

    @property
    def port_start(self):
        """Gets the port_start of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The port_start of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: int
        """
        return self._port_start

    @port_start.setter
    def port_start(self, port_start):
        """Sets the port_start of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param port_start: The port_start of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: int
        """

        self._port_start = port_start

    @property
    def prefix_list_cidrs(self):
        """Gets the prefix_list_cidrs of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The prefix_list_cidrs of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._prefix_list_cidrs

    @prefix_list_cidrs.setter
    def prefix_list_cidrs(self, prefix_list_cidrs):
        """Sets the prefix_list_cidrs of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param prefix_list_cidrs: The prefix_list_cidrs of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: list[str]
        """

        self._prefix_list_cidrs = prefix_list_cidrs

    @property
    def prefix_list_id(self):
        """Gets the prefix_list_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The prefix_list_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._prefix_list_id

    @prefix_list_id.setter
    def prefix_list_id(self, prefix_list_id):
        """Sets the prefix_list_id of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param prefix_list_id: The prefix_list_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._prefix_list_id = prefix_list_id

    @property
    def priority(self):
        """Gets the priority of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The priority of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param priority: The priority of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def protocol(self):
        """Gets the protocol of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The protocol of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param protocol: The protocol of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def source_group_id(self):
        """Gets the source_group_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The source_group_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_group_id

    @source_group_id.setter
    def source_group_id(self, source_group_id):
        """Sets the source_group_id of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param source_group_id: The source_group_id of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._source_group_id = source_group_id

    @property
    def update_time(self):
        """Gets the update_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501


        :return: The update_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PermissionForDescribeSecurityGroupAttributesOutput.


        :param update_time: The update_time of this PermissionForDescribeSecurityGroupAttributesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(PermissionForDescribeSecurityGroupAttributesOutput, dict):
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
        if not isinstance(other, PermissionForDescribeSecurityGroupAttributesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PermissionForDescribeSecurityGroupAttributesOutput):
            return True

        return self.to_dict() != other.to_dict()
