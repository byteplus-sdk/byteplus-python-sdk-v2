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


class ConfigurationForModifyReservedInstancesInput(object):
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
        'hpc_cluster_id': 'str',
        'instance_count': 'int',
        'instance_type_id': 'str',
        'reserved_instance_name': 'str',
        'scope': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'hpc_cluster_id': 'HpcClusterId',
        'instance_count': 'InstanceCount',
        'instance_type_id': 'InstanceTypeId',
        'reserved_instance_name': 'ReservedInstanceName',
        'scope': 'Scope',
        'zone_id': 'ZoneId'
    }

    def __init__(self, hpc_cluster_id=None, instance_count=None, instance_type_id=None, reserved_instance_name=None, scope=None, zone_id=None, _configuration=None):  # noqa: E501
        """ConfigurationForModifyReservedInstancesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hpc_cluster_id = None
        self._instance_count = None
        self._instance_type_id = None
        self._reserved_instance_name = None
        self._scope = None
        self._zone_id = None
        self.discriminator = None

        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if instance_count is not None:
            self.instance_count = instance_count
        if instance_type_id is not None:
            self.instance_type_id = instance_type_id
        self.reserved_instance_name = reserved_instance_name
        if scope is not None:
            self.scope = scope
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The hpc_cluster_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this ConfigurationForModifyReservedInstancesInput.


        :param hpc_cluster_id: The hpc_cluster_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def instance_count(self):
        """Gets the instance_count of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The instance_count of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: int
        """
        return self._instance_count

    @instance_count.setter
    def instance_count(self, instance_count):
        """Sets the instance_count of this ConfigurationForModifyReservedInstancesInput.


        :param instance_count: The instance_count of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: int
        """

        self._instance_count = instance_count

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The instance_type_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this ConfigurationForModifyReservedInstancesInput.


        :param instance_type_id: The instance_type_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: str
        """

        self._instance_type_id = instance_type_id

    @property
    def reserved_instance_name(self):
        """Gets the reserved_instance_name of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The reserved_instance_name of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._reserved_instance_name

    @reserved_instance_name.setter
    def reserved_instance_name(self, reserved_instance_name):
        """Sets the reserved_instance_name of this ConfigurationForModifyReservedInstancesInput.


        :param reserved_instance_name: The reserved_instance_name of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reserved_instance_name is None:
            raise ValueError("Invalid value for `reserved_instance_name`, must not be `None`")  # noqa: E501

        self._reserved_instance_name = reserved_instance_name

    @property
    def scope(self):
        """Gets the scope of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The scope of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ConfigurationForModifyReservedInstancesInput.


        :param scope: The scope of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def zone_id(self):
        """Gets the zone_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501


        :return: The zone_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this ConfigurationForModifyReservedInstancesInput.


        :param zone_id: The zone_id of this ConfigurationForModifyReservedInstancesInput.  # noqa: E501
        :type: str
        """

        self._zone_id = zone_id

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
        if issubclass(ConfigurationForModifyReservedInstancesInput, dict):
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
        if not isinstance(other, ConfigurationForModifyReservedInstancesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigurationForModifyReservedInstancesInput):
            return True

        return self.to_dict() != other.to_dict()
