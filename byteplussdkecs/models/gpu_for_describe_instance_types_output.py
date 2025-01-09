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


class GpuForDescribeInstanceTypesOutput(object):
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
        'gpu_devices': 'list[GpuDeviceForDescribeInstanceTypesOutput]'
    }

    attribute_map = {
        'gpu_devices': 'GpuDevices'
    }

    def __init__(self, gpu_devices=None, _configuration=None):  # noqa: E501
        """GpuForDescribeInstanceTypesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._gpu_devices = None
        self.discriminator = None

        if gpu_devices is not None:
            self.gpu_devices = gpu_devices

    @property
    def gpu_devices(self):
        """Gets the gpu_devices of this GpuForDescribeInstanceTypesOutput.  # noqa: E501


        :return: The gpu_devices of this GpuForDescribeInstanceTypesOutput.  # noqa: E501
        :rtype: list[GpuDeviceForDescribeInstanceTypesOutput]
        """
        return self._gpu_devices

    @gpu_devices.setter
    def gpu_devices(self, gpu_devices):
        """Sets the gpu_devices of this GpuForDescribeInstanceTypesOutput.


        :param gpu_devices: The gpu_devices of this GpuForDescribeInstanceTypesOutput.  # noqa: E501
        :type: list[GpuDeviceForDescribeInstanceTypesOutput]
        """

        self._gpu_devices = gpu_devices

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
        if issubclass(GpuForDescribeInstanceTypesOutput, dict):
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
        if not isinstance(other, GpuForDescribeInstanceTypesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GpuForDescribeInstanceTypesOutput):
            return True

        return self.to_dict() != other.to_dict()
