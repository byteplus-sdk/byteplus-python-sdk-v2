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


class DescribeSpotPriceHistoryRequest(object):
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
        'instance_type_id': 'str',
        'max_results': 'int',
        'next_token': 'str',
        'timestamp_end': 'str',
        'timestamp_start': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'instance_type_id': 'InstanceTypeId',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'timestamp_end': 'TimestampEnd',
        'timestamp_start': 'TimestampStart',
        'zone_id': 'ZoneId'
    }

    def __init__(self, instance_type_id=None, max_results=None, next_token=None, timestamp_end=None, timestamp_start=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeSpotPriceHistoryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_type_id = None
        self._max_results = None
        self._next_token = None
        self._timestamp_end = None
        self._timestamp_start = None
        self._zone_id = None
        self.discriminator = None

        self.instance_type_id = instance_type_id
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if timestamp_end is not None:
            self.timestamp_end = timestamp_end
        if timestamp_start is not None:
            self.timestamp_start = timestamp_start
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def instance_type_id(self):
        """Gets the instance_type_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The instance_type_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_id

    @instance_type_id.setter
    def instance_type_id(self, instance_type_id):
        """Sets the instance_type_id of this DescribeSpotPriceHistoryRequest.


        :param instance_type_id: The instance_type_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_type_id is None:
            raise ValueError("Invalid value for `instance_type_id`, must not be `None`")  # noqa: E501

        self._instance_type_id = instance_type_id

    @property
    def max_results(self):
        """Gets the max_results of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The max_results of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeSpotPriceHistoryRequest.


        :param max_results: The max_results of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The next_token of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeSpotPriceHistoryRequest.


        :param next_token: The next_token of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def timestamp_end(self):
        """Gets the timestamp_end of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The timestamp_end of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._timestamp_end

    @timestamp_end.setter
    def timestamp_end(self, timestamp_end):
        """Sets the timestamp_end of this DescribeSpotPriceHistoryRequest.


        :param timestamp_end: The timestamp_end of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :type: str
        """

        self._timestamp_end = timestamp_end

    @property
    def timestamp_start(self):
        """Gets the timestamp_start of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The timestamp_start of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._timestamp_start

    @timestamp_start.setter
    def timestamp_start(self, timestamp_start):
        """Sets the timestamp_start of this DescribeSpotPriceHistoryRequest.


        :param timestamp_start: The timestamp_start of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :type: str
        """

        self._timestamp_start = timestamp_start

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501


        :return: The zone_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeSpotPriceHistoryRequest.


        :param zone_id: The zone_id of this DescribeSpotPriceHistoryRequest.  # noqa: E501
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
        if issubclass(DescribeSpotPriceHistoryRequest, dict):
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
        if not isinstance(other, DescribeSpotPriceHistoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSpotPriceHistoryRequest):
            return True

        return self.to_dict() != other.to_dict()
