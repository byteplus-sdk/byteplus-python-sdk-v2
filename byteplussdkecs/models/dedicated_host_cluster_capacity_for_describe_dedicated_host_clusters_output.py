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


class DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput(object):
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
        'available_instance_types': 'list[AvailableInstanceTypeForDescribeDedicatedHostClustersOutput]',
        'available_memory': 'int',
        'available_vcpus': 'int',
        'local_volume_capacities': 'list[LocalVolumeCapacityForDescribeDedicatedHostClustersOutput]',
        'total_memory': 'int',
        'total_vcpus': 'int'
    }

    attribute_map = {
        'available_instance_types': 'AvailableInstanceTypes',
        'available_memory': 'AvailableMemory',
        'available_vcpus': 'AvailableVcpus',
        'local_volume_capacities': 'LocalVolumeCapacities',
        'total_memory': 'TotalMemory',
        'total_vcpus': 'TotalVcpus'
    }

    def __init__(self, available_instance_types=None, available_memory=None, available_vcpus=None, local_volume_capacities=None, total_memory=None, total_vcpus=None, _configuration=None):  # noqa: E501
        """DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._available_instance_types = None
        self._available_memory = None
        self._available_vcpus = None
        self._local_volume_capacities = None
        self._total_memory = None
        self._total_vcpus = None
        self.discriminator = None

        if available_instance_types is not None:
            self.available_instance_types = available_instance_types
        if available_memory is not None:
            self.available_memory = available_memory
        if available_vcpus is not None:
            self.available_vcpus = available_vcpus
        if local_volume_capacities is not None:
            self.local_volume_capacities = local_volume_capacities
        if total_memory is not None:
            self.total_memory = total_memory
        if total_vcpus is not None:
            self.total_vcpus = total_vcpus

    @property
    def available_instance_types(self):
        """Gets the available_instance_types of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The available_instance_types of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: list[AvailableInstanceTypeForDescribeDedicatedHostClustersOutput]
        """
        return self._available_instance_types

    @available_instance_types.setter
    def available_instance_types(self, available_instance_types):
        """Sets the available_instance_types of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param available_instance_types: The available_instance_types of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: list[AvailableInstanceTypeForDescribeDedicatedHostClustersOutput]
        """

        self._available_instance_types = available_instance_types

    @property
    def available_memory(self):
        """Gets the available_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The available_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: int
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        """Sets the available_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param available_memory: The available_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: int
        """

        self._available_memory = available_memory

    @property
    def available_vcpus(self):
        """Gets the available_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The available_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: int
        """
        return self._available_vcpus

    @available_vcpus.setter
    def available_vcpus(self, available_vcpus):
        """Sets the available_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param available_vcpus: The available_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: int
        """

        self._available_vcpus = available_vcpus

    @property
    def local_volume_capacities(self):
        """Gets the local_volume_capacities of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The local_volume_capacities of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: list[LocalVolumeCapacityForDescribeDedicatedHostClustersOutput]
        """
        return self._local_volume_capacities

    @local_volume_capacities.setter
    def local_volume_capacities(self, local_volume_capacities):
        """Sets the local_volume_capacities of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param local_volume_capacities: The local_volume_capacities of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: list[LocalVolumeCapacityForDescribeDedicatedHostClustersOutput]
        """

        self._local_volume_capacities = local_volume_capacities

    @property
    def total_memory(self):
        """Gets the total_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The total_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """Sets the total_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param total_memory: The total_memory of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: int
        """

        self._total_memory = total_memory

    @property
    def total_vcpus(self):
        """Gets the total_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501


        :return: The total_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :rtype: int
        """
        return self._total_vcpus

    @total_vcpus.setter
    def total_vcpus(self, total_vcpus):
        """Sets the total_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.


        :param total_vcpus: The total_vcpus of this DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput.  # noqa: E501
        :type: int
        """

        self._total_vcpus = total_vcpus

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
        if issubclass(DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput, dict):
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
        if not isinstance(other, DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DedicatedHostClusterCapacityForDescribeDedicatedHostClustersOutput):
            return True

        return self.to_dict() != other.to_dict()
