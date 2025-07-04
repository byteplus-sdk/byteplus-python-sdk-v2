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


class NetworkInterfaceForDescribeInstancesOutput(object):
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
        'ipv6_addresses': 'list[str]',
        'mac_address': 'str',
        'network_interface_id': 'str',
        'primary_ip_address': 'str',
        'security_group_ids': 'list[str]',
        'subnet_id': 'str',
        'type': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'ipv6_addresses': 'Ipv6Addresses',
        'mac_address': 'MacAddress',
        'network_interface_id': 'NetworkInterfaceId',
        'primary_ip_address': 'PrimaryIpAddress',
        'security_group_ids': 'SecurityGroupIds',
        'subnet_id': 'SubnetId',
        'type': 'Type',
        'vpc_id': 'VpcId'
    }

    def __init__(self, ipv6_addresses=None, mac_address=None, network_interface_id=None, primary_ip_address=None, security_group_ids=None, subnet_id=None, type=None, vpc_id=None, _configuration=None):  # noqa: E501
        """NetworkInterfaceForDescribeInstancesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ipv6_addresses = None
        self._mac_address = None
        self._network_interface_id = None
        self._primary_ip_address = None
        self._security_group_ids = None
        self._subnet_id = None
        self._type = None
        self._vpc_id = None
        self.discriminator = None

        if ipv6_addresses is not None:
            self.ipv6_addresses = ipv6_addresses
        if mac_address is not None:
            self.mac_address = mac_address
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if primary_ip_address is not None:
            self.primary_ip_address = primary_ip_address
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def ipv6_addresses(self):
        """Gets the ipv6_addresses of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The ipv6_addresses of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ipv6_addresses

    @ipv6_addresses.setter
    def ipv6_addresses(self, ipv6_addresses):
        """Sets the ipv6_addresses of this NetworkInterfaceForDescribeInstancesOutput.


        :param ipv6_addresses: The ipv6_addresses of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: list[str]
        """

        self._ipv6_addresses = ipv6_addresses

    @property
    def mac_address(self):
        """Gets the mac_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The mac_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetworkInterfaceForDescribeInstancesOutput.


        :param mac_address: The mac_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The network_interface_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this NetworkInterfaceForDescribeInstancesOutput.


        :param network_interface_id: The network_interface_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def primary_ip_address(self):
        """Gets the primary_ip_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The primary_ip_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip_address

    @primary_ip_address.setter
    def primary_ip_address(self, primary_ip_address):
        """Sets the primary_ip_address of this NetworkInterfaceForDescribeInstancesOutput.


        :param primary_ip_address: The primary_ip_address of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._primary_ip_address = primary_ip_address

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The security_group_ids of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this NetworkInterfaceForDescribeInstancesOutput.


        :param security_group_ids: The security_group_ids of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def subnet_id(self):
        """Gets the subnet_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The subnet_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this NetworkInterfaceForDescribeInstancesOutput.


        :param subnet_id: The subnet_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def type(self):
        """Gets the type of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The type of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkInterfaceForDescribeInstancesOutput.


        :param type: The type of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501


        :return: The vpc_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this NetworkInterfaceForDescribeInstancesOutput.


        :param vpc_id: The vpc_id of this NetworkInterfaceForDescribeInstancesOutput.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

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
        if issubclass(NetworkInterfaceForDescribeInstancesOutput, dict):
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
        if not isinstance(other, NetworkInterfaceForDescribeInstancesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkInterfaceForDescribeInstancesOutput):
            return True

        return self.to_dict() != other.to_dict()
