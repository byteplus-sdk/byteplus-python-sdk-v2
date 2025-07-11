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


class GetScheduledInstanceLatestReleaseAtRequest(object):
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
        'delivery_type': 'str',
        'instance_type_id': 'str',
        'start_delivery_at': 'str',
        'volume_type': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'delivery_type': 'DeliveryType',
        'instance_type_id': 'InstanceTypeId',
        'start_delivery_at': 'StartDeliveryAt',
        'volume_type': 'VolumeType',
        'zone_id': 'ZoneId'
    }

    def __init__(self, delivery_type=None, instance_type_id=None, start_delivery_at=None, volume_type=None, zone_id=None, _configuration=None):  # noqa: E501
        """GetScheduledInstanceLatestReleaseAtRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delivery_type = None
        self._instance_type_id = None
        self._start_delivery_at = None
        self._volume_type = None
        self._zone_id = None
        self.discriminator = None

        if delivery_type is not None:
            self.delivery_type = delivery_type
        self.instance_type_id = instance_type_id
        if start_delivery_at is not None:
            self.start_delivery_at = start_delivery_at
        self.volume_type = volume_type
        self.zone_id = zone_id

    @property
    def delivery_type(self):
        """Gets the delivery_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501


        :return: The delivery_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this GetScheduledInstanceLatestReleaseAtRequest.


        :param delivery_type: The delivery_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :type: str
        """

        self._delivery_type = delivery_type

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501


        :return: The instance_type_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this GetScheduledInstanceLatestReleaseAtRequest.


        :param instance_type_id: The instance_type_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_type_id is None:
            raise ValueError("Invalid value for `instance_type_id`, must not be `None`")  # noqa: E501

        self._instance_type_id = instance_type_id

    @property
    def start_delivery_at(self):
        """Gets the start_delivery_at of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501


        :return: The start_delivery_at of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_delivery_at

    @start_delivery_at.setter
    def start_delivery_at(self, start_delivery_at):
        """Sets the start_delivery_at of this GetScheduledInstanceLatestReleaseAtRequest.


        :param start_delivery_at: The start_delivery_at of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :type: str
        """

        self._start_delivery_at = start_delivery_at

    @property
    def volume_type(self):
        """Gets the volume_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501


        :return: The volume_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this GetScheduledInstanceLatestReleaseAtRequest.


        :param volume_type: The volume_type of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and volume_type is None:
            raise ValueError("Invalid value for `volume_type`, must not be `None`")  # noqa: E501

        self._volume_type = volume_type

    @property
    def zone_id(self):
        """Gets the zone_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501


        :return: The zone_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this GetScheduledInstanceLatestReleaseAtRequest.


        :param zone_id: The zone_id of this GetScheduledInstanceLatestReleaseAtRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and zone_id is None:
            raise ValueError("Invalid value for `zone_id`, must not be `None`")  # noqa: E501

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
        if issubclass(GetScheduledInstanceLatestReleaseAtRequest, dict):
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
        if not isinstance(other, GetScheduledInstanceLatestReleaseAtRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetScheduledInstanceLatestReleaseAtRequest):
            return True

        return self.to_dict() != other.to_dict()
