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


class VolumeForRunInstancesInput(object):
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
        'delete_with_instance': 'str',
        'extra_performance_iops': 'int',
        'extra_performance_throughput_mb': 'int',
        'extra_performance_type_id': 'str',
        'size': 'int',
        'snapshot_id': 'str',
        'volume_type': 'str'
    }

    attribute_map = {
        'delete_with_instance': 'DeleteWithInstance',
        'extra_performance_iops': 'ExtraPerformanceIOPS',
        'extra_performance_throughput_mb': 'ExtraPerformanceThroughputMB',
        'extra_performance_type_id': 'ExtraPerformanceTypeId',
        'size': 'Size',
        'snapshot_id': 'SnapshotId',
        'volume_type': 'VolumeType'
    }

    def __init__(self, delete_with_instance=None, extra_performance_iops=None, extra_performance_throughput_mb=None, extra_performance_type_id=None, size=None, snapshot_id=None, volume_type=None, _configuration=None):  # noqa: E501
        """VolumeForRunInstancesInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delete_with_instance = None
        self._extra_performance_iops = None
        self._extra_performance_throughput_mb = None
        self._extra_performance_type_id = None
        self._size = None
        self._snapshot_id = None
        self._volume_type = None
        self.discriminator = None

        if delete_with_instance is not None:
            self.delete_with_instance = delete_with_instance
        if extra_performance_iops is not None:
            self.extra_performance_iops = extra_performance_iops
        if extra_performance_throughput_mb is not None:
            self.extra_performance_throughput_mb = extra_performance_throughput_mb
        if extra_performance_type_id is not None:
            self.extra_performance_type_id = extra_performance_type_id
        self.size = size
        if snapshot_id is not None:
            self.snapshot_id = snapshot_id
        if volume_type is not None:
            self.volume_type = volume_type

    @property
    def delete_with_instance(self):
        """Gets the delete_with_instance of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The delete_with_instance of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._delete_with_instance

    @delete_with_instance.setter
    def delete_with_instance(self, delete_with_instance):
        """Sets the delete_with_instance of this VolumeForRunInstancesInput.


        :param delete_with_instance: The delete_with_instance of this VolumeForRunInstancesInput.  # noqa: E501
        :type: str
        """

        self._delete_with_instance = delete_with_instance

    @property
    def extra_performance_iops(self):
        """Gets the extra_performance_iops of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The extra_performance_iops of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: int
        """
        return self._extra_performance_iops

    @extra_performance_iops.setter
    def extra_performance_iops(self, extra_performance_iops):
        """Sets the extra_performance_iops of this VolumeForRunInstancesInput.


        :param extra_performance_iops: The extra_performance_iops of this VolumeForRunInstancesInput.  # noqa: E501
        :type: int
        """

        self._extra_performance_iops = extra_performance_iops

    @property
    def extra_performance_throughput_mb(self):
        """Gets the extra_performance_throughput_mb of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The extra_performance_throughput_mb of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: int
        """
        return self._extra_performance_throughput_mb

    @extra_performance_throughput_mb.setter
    def extra_performance_throughput_mb(self, extra_performance_throughput_mb):
        """Sets the extra_performance_throughput_mb of this VolumeForRunInstancesInput.


        :param extra_performance_throughput_mb: The extra_performance_throughput_mb of this VolumeForRunInstancesInput.  # noqa: E501
        :type: int
        """

        self._extra_performance_throughput_mb = extra_performance_throughput_mb

    @property
    def extra_performance_type_id(self):
        """Gets the extra_performance_type_id of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The extra_performance_type_id of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._extra_performance_type_id

    @extra_performance_type_id.setter
    def extra_performance_type_id(self, extra_performance_type_id):
        """Sets the extra_performance_type_id of this VolumeForRunInstancesInput.


        :param extra_performance_type_id: The extra_performance_type_id of this VolumeForRunInstancesInput.  # noqa: E501
        :type: str
        """

        self._extra_performance_type_id = extra_performance_type_id

    @property
    def size(self):
        """Gets the size of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The size of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeForRunInstancesInput.


        :param size: The size of this VolumeForRunInstancesInput.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def snapshot_id(self):
        """Gets the snapshot_id of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The snapshot_id of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """Sets the snapshot_id of this VolumeForRunInstancesInput.


        :param snapshot_id: The snapshot_id of this VolumeForRunInstancesInput.  # noqa: E501
        :type: str
        """

        self._snapshot_id = snapshot_id

    @property
    def volume_type(self):
        """Gets the volume_type of this VolumeForRunInstancesInput.  # noqa: E501


        :return: The volume_type of this VolumeForRunInstancesInput.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this VolumeForRunInstancesInput.


        :param volume_type: The volume_type of this VolumeForRunInstancesInput.  # noqa: E501
        :type: str
        """

        self._volume_type = volume_type

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
        if issubclass(VolumeForRunInstancesInput, dict):
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
        if not isinstance(other, VolumeForRunInstancesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeForRunInstancesInput):
            return True

        return self.to_dict() != other.to_dict()
