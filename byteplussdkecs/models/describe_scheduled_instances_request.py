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


class DescribeScheduledInstancesRequest(object):
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
        'elastic_scheduled_instance_type': 'str',
        'image_id': 'str',
        'instance_type_ids': 'list[str]',
        'key_pair_name': 'str',
        'max_results': 'int',
        'next_token': 'str',
        'project_name': 'str',
        'scheduled_instance_ids': 'list[str]',
        'scheduled_instance_name': 'str',
        'status': 'str',
        'tag_filters': 'list[TagFilterForDescribeScheduledInstancesInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'delivery_type': 'DeliveryType',
        'elastic_scheduled_instance_type': 'ElasticScheduledInstanceType',
        'image_id': 'ImageId',
        'instance_type_ids': 'InstanceTypeIds',
        'key_pair_name': 'KeyPairName',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'project_name': 'ProjectName',
        'scheduled_instance_ids': 'ScheduledInstanceIds',
        'scheduled_instance_name': 'ScheduledInstanceName',
        'status': 'Status',
        'tag_filters': 'TagFilters',
        'zone_id': 'ZoneId'
    }

    def __init__(self, delivery_type=None, elastic_scheduled_instance_type=None, image_id=None, instance_type_ids=None, key_pair_name=None, max_results=None, next_token=None, project_name=None, scheduled_instance_ids=None, scheduled_instance_name=None, status=None, tag_filters=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeScheduledInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delivery_type = None
        self._elastic_scheduled_instance_type = None
        self._image_id = None
        self._instance_type_ids = None
        self._key_pair_name = None
        self._max_results = None
        self._next_token = None
        self._project_name = None
        self._scheduled_instance_ids = None
        self._scheduled_instance_name = None
        self._status = None
        self._tag_filters = None
        self._zone_id = None
        self.discriminator = None

        if delivery_type is not None:
            self.delivery_type = delivery_type
        if elastic_scheduled_instance_type is not None:
            self.elastic_scheduled_instance_type = elastic_scheduled_instance_type
        if image_id is not None:
            self.image_id = image_id
        if instance_type_ids is not None:
            self.instance_type_ids = instance_type_ids
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if project_name is not None:
            self.project_name = project_name
        if scheduled_instance_ids is not None:
            self.scheduled_instance_ids = scheduled_instance_ids
        if scheduled_instance_name is not None:
            self.scheduled_instance_name = scheduled_instance_name
        if status is not None:
            self.status = status
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def delivery_type(self):
        """Gets the delivery_type of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The delivery_type of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._delivery_type

    @delivery_type.setter
    def delivery_type(self, delivery_type):
        """Sets the delivery_type of this DescribeScheduledInstancesRequest.


        :param delivery_type: The delivery_type of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._delivery_type = delivery_type

    @property
    def elastic_scheduled_instance_type(self):
        """Gets the elastic_scheduled_instance_type of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The elastic_scheduled_instance_type of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._elastic_scheduled_instance_type

    @elastic_scheduled_instance_type.setter
    def elastic_scheduled_instance_type(self, elastic_scheduled_instance_type):
        """Sets the elastic_scheduled_instance_type of this DescribeScheduledInstancesRequest.


        :param elastic_scheduled_instance_type: The elastic_scheduled_instance_type of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._elastic_scheduled_instance_type = elastic_scheduled_instance_type

    @property
    def image_id(self):
        """Gets the image_id of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The image_id of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this DescribeScheduledInstancesRequest.


        :param image_id: The image_id of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def instance_type_ids(self):
        """Gets the instance_type_ids of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The instance_type_ids of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_ids

    @instance_type_ids.setter
    def instance_type_ids(self, instance_type_ids):
        """Sets the instance_type_ids of this DescribeScheduledInstancesRequest.


        :param instance_type_ids: The instance_type_ids of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_ids = instance_type_ids

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The key_pair_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this DescribeScheduledInstancesRequest.


        :param key_pair_name: The key_pair_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def max_results(self):
        """Gets the max_results of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The max_results of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeScheduledInstancesRequest.


        :param max_results: The max_results of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The next_token of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeScheduledInstancesRequest.


        :param next_token: The next_token of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def project_name(self):
        """Gets the project_name of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The project_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeScheduledInstancesRequest.


        :param project_name: The project_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def scheduled_instance_ids(self):
        """Gets the scheduled_instance_ids of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The scheduled_instance_ids of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scheduled_instance_ids

    @scheduled_instance_ids.setter
    def scheduled_instance_ids(self, scheduled_instance_ids):
        """Sets the scheduled_instance_ids of this DescribeScheduledInstancesRequest.


        :param scheduled_instance_ids: The scheduled_instance_ids of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._scheduled_instance_ids = scheduled_instance_ids

    @property
    def scheduled_instance_name(self):
        """Gets the scheduled_instance_name of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The scheduled_instance_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_instance_name

    @scheduled_instance_name.setter
    def scheduled_instance_name(self, scheduled_instance_name):
        """Sets the scheduled_instance_name of this DescribeScheduledInstancesRequest.


        :param scheduled_instance_name: The scheduled_instance_name of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scheduled_instance_name = scheduled_instance_name

    @property
    def status(self):
        """Gets the status of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The status of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeScheduledInstancesRequest.


        :param status: The status of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeScheduledInstancesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeScheduledInstancesRequest.


        :param tag_filters: The tag_filters of this DescribeScheduledInstancesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeScheduledInstancesInput]
        """

        self._tag_filters = tag_filters

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeScheduledInstancesRequest.  # noqa: E501


        :return: The zone_id of this DescribeScheduledInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeScheduledInstancesRequest.


        :param zone_id: The zone_id of this DescribeScheduledInstancesRequest.  # noqa: E501
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
        if issubclass(DescribeScheduledInstancesRequest, dict):
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
        if not isinstance(other, DescribeScheduledInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeScheduledInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
