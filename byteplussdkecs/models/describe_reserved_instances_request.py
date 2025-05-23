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


class DescribeReservedInstancesRequest(object):
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
        'instance_type_families': 'list[str]',
        'instance_type_ids': 'list[str]',
        'max_results': 'int',
        'next_token': 'str',
        'project_name': 'str',
        'reserved_instance_ids': 'list[str]',
        'reserved_instance_name': 'str',
        'scope': 'str',
        'status': 'str',
        'support_modify': 'str',
        'tag_filters': 'list[TagFilterForDescribeReservedInstancesInput]',
        'zone_id': 'str'
    }

    attribute_map = {
        'hpc_cluster_id': 'HpcClusterId',
        'instance_type_families': 'InstanceTypeFamilies',
        'instance_type_ids': 'InstanceTypeIds',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'project_name': 'ProjectName',
        'reserved_instance_ids': 'ReservedInstanceIds',
        'reserved_instance_name': 'ReservedInstanceName',
        'scope': 'Scope',
        'status': 'Status',
        'support_modify': 'SupportModify',
        'tag_filters': 'TagFilters',
        'zone_id': 'ZoneId'
    }

    def __init__(self, hpc_cluster_id=None, instance_type_families=None, instance_type_ids=None, max_results=None, next_token=None, project_name=None, reserved_instance_ids=None, reserved_instance_name=None, scope=None, status=None, support_modify=None, tag_filters=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeReservedInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._hpc_cluster_id = None
        self._instance_type_families = None
        self._instance_type_ids = None
        self._max_results = None
        self._next_token = None
        self._project_name = None
        self._reserved_instance_ids = None
        self._reserved_instance_name = None
        self._scope = None
        self._status = None
        self._support_modify = None
        self._tag_filters = None
        self._zone_id = None
        self.discriminator = None

        if hpc_cluster_id is not None:
            self.hpc_cluster_id = hpc_cluster_id
        if instance_type_families is not None:
            self.instance_type_families = instance_type_families
        if instance_type_ids is not None:
            self.instance_type_ids = instance_type_ids
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if project_name is not None:
            self.project_name = project_name
        if reserved_instance_ids is not None:
            self.reserved_instance_ids = reserved_instance_ids
        if reserved_instance_name is not None:
            self.reserved_instance_name = reserved_instance_name
        if scope is not None:
            self.scope = scope
        if status is not None:
            self.status = status
        if support_modify is not None:
            self.support_modify = support_modify
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def hpc_cluster_id(self):
        """Gets the hpc_cluster_id of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The hpc_cluster_id of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._hpc_cluster_id

    @hpc_cluster_id.setter
    def hpc_cluster_id(self, hpc_cluster_id):
        """Sets the hpc_cluster_id of this DescribeReservedInstancesRequest.


        :param hpc_cluster_id: The hpc_cluster_id of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._hpc_cluster_id = hpc_cluster_id

    @property
    def instance_type_families(self):
        """Gets the instance_type_families of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The instance_type_families of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_families

    @instance_type_families.setter
    def instance_type_families(self, instance_type_families):
        """Sets the instance_type_families of this DescribeReservedInstancesRequest.


        :param instance_type_families: The instance_type_families of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_families = instance_type_families

    @property
    def instance_type_ids(self):
        """Gets the instance_type_ids of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The instance_type_ids of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_type_ids

    @instance_type_ids.setter
    def instance_type_ids(self, instance_type_ids):
        """Sets the instance_type_ids of this DescribeReservedInstancesRequest.


        :param instance_type_ids: The instance_type_ids of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_type_ids = instance_type_ids

    @property
    def max_results(self):
        """Gets the max_results of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The max_results of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeReservedInstancesRequest.


        :param max_results: The max_results of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The next_token of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeReservedInstancesRequest.


        :param next_token: The next_token of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def project_name(self):
        """Gets the project_name of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The project_name of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeReservedInstancesRequest.


        :param project_name: The project_name of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def reserved_instance_ids(self):
        """Gets the reserved_instance_ids of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The reserved_instance_ids of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._reserved_instance_ids

    @reserved_instance_ids.setter
    def reserved_instance_ids(self, reserved_instance_ids):
        """Sets the reserved_instance_ids of this DescribeReservedInstancesRequest.


        :param reserved_instance_ids: The reserved_instance_ids of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._reserved_instance_ids = reserved_instance_ids

    @property
    def reserved_instance_name(self):
        """Gets the reserved_instance_name of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The reserved_instance_name of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._reserved_instance_name

    @reserved_instance_name.setter
    def reserved_instance_name(self, reserved_instance_name):
        """Sets the reserved_instance_name of this DescribeReservedInstancesRequest.


        :param reserved_instance_name: The reserved_instance_name of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._reserved_instance_name = reserved_instance_name

    @property
    def scope(self):
        """Gets the scope of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The scope of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DescribeReservedInstancesRequest.


        :param scope: The scope of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def status(self):
        """Gets the status of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The status of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeReservedInstancesRequest.


        :param status: The status of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def support_modify(self):
        """Gets the support_modify of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The support_modify of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._support_modify

    @support_modify.setter
    def support_modify(self, support_modify):
        """Sets the support_modify of this DescribeReservedInstancesRequest.


        :param support_modify: The support_modify of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: str
        """

        self._support_modify = support_modify

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The tag_filters of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeReservedInstancesInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeReservedInstancesRequest.


        :param tag_filters: The tag_filters of this DescribeReservedInstancesRequest.  # noqa: E501
        :type: list[TagFilterForDescribeReservedInstancesInput]
        """

        self._tag_filters = tag_filters

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeReservedInstancesRequest.  # noqa: E501


        :return: The zone_id of this DescribeReservedInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeReservedInstancesRequest.


        :param zone_id: The zone_id of this DescribeReservedInstancesRequest.  # noqa: E501
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
        if issubclass(DescribeReservedInstancesRequest, dict):
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
        if not isinstance(other, DescribeReservedInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeReservedInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
