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


class IngressAclEntryForUpdateNetworkAclEntriesInput(object):
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
        'description': 'str',
        'network_acl_entry_id': 'str',
        'network_acl_entry_name': 'str',
        'policy': 'str',
        'port': 'str',
        'protocol': 'str',
        'source_cidr_ip': 'str'
    }

    attribute_map = {
        'description': 'Description',
        'network_acl_entry_id': 'NetworkAclEntryId',
        'network_acl_entry_name': 'NetworkAclEntryName',
        'policy': 'Policy',
        'port': 'Port',
        'protocol': 'Protocol',
        'source_cidr_ip': 'SourceCidrIp'
    }

    def __init__(self, description=None, network_acl_entry_id=None, network_acl_entry_name=None, policy=None, port=None, protocol=None, source_cidr_ip=None, _configuration=None):  # noqa: E501
        """IngressAclEntryForUpdateNetworkAclEntriesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._network_acl_entry_id = None
        self._network_acl_entry_name = None
        self._policy = None
        self._port = None
        self._protocol = None
        self._source_cidr_ip = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if network_acl_entry_id is not None:
            self.network_acl_entry_id = network_acl_entry_id
        if network_acl_entry_name is not None:
            self.network_acl_entry_name = network_acl_entry_name
        if policy is not None:
            self.policy = policy
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if source_cidr_ip is not None:
            self.source_cidr_ip = source_cidr_ip

    @property
    def description(self):
        """Gets the description of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The description of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param description: The description of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def network_acl_entry_id(self):
        """Gets the network_acl_entry_id of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The network_acl_entry_id of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_entry_id

    @network_acl_entry_id.setter
    def network_acl_entry_id(self, network_acl_entry_id):
        """Sets the network_acl_entry_id of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param network_acl_entry_id: The network_acl_entry_id of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._network_acl_entry_id = network_acl_entry_id

    @property
    def network_acl_entry_name(self):
        """Gets the network_acl_entry_name of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The network_acl_entry_name of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._network_acl_entry_name

    @network_acl_entry_name.setter
    def network_acl_entry_name(self, network_acl_entry_name):
        """Sets the network_acl_entry_name of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param network_acl_entry_name: The network_acl_entry_name of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._network_acl_entry_name = network_acl_entry_name

    @property
    def policy(self):
        """Gets the policy of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The policy of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param policy: The policy of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def port(self):
        """Gets the port of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The port of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param port: The port of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The protocol of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param protocol: The protocol of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def source_cidr_ip(self):
        """Gets the source_cidr_ip of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501


        :return: The source_cidr_ip of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :rtype: str
        """
        return self._source_cidr_ip

    @source_cidr_ip.setter
    def source_cidr_ip(self, source_cidr_ip):
        """Sets the source_cidr_ip of this IngressAclEntryForUpdateNetworkAclEntriesInput.


        :param source_cidr_ip: The source_cidr_ip of this IngressAclEntryForUpdateNetworkAclEntriesInput.  # noqa: E501
        :type: str
        """

        self._source_cidr_ip = source_cidr_ip

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
        if issubclass(IngressAclEntryForUpdateNetworkAclEntriesInput, dict):
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
        if not isinstance(other, IngressAclEntryForUpdateNetworkAclEntriesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngressAclEntryForUpdateNetworkAclEntriesInput):
            return True

        return self.to_dict() != other.to_dict()
