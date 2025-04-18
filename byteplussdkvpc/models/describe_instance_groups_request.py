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


class DescribeInstanceGroupsRequest(object):
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
        'instance_group_ids': 'list[str]',
        'instance_group_name': 'str',
        'max_results': 'int',
        'next_token': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'vpc_id': 'str'
    }

    attribute_map = {
        'instance_group_ids': 'InstanceGroupIds',
        'instance_group_name': 'InstanceGroupName',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'vpc_id': 'VpcId'
    }

    def __init__(self, instance_group_ids=None, instance_group_name=None, max_results=None, next_token=None, page_number=None, page_size=None, vpc_id=None, _configuration=None):  # noqa: E501
        """DescribeInstanceGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_group_ids = None
        self._instance_group_name = None
        self._max_results = None
        self._next_token = None
        self._page_number = None
        self._page_size = None
        self._vpc_id = None
        self.discriminator = None

        if instance_group_ids is not None:
            self.instance_group_ids = instance_group_ids
        if instance_group_name is not None:
            self.instance_group_name = instance_group_name
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def instance_group_ids(self):
        """Gets the instance_group_ids of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The instance_group_ids of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_group_ids

    @instance_group_ids.setter
    def instance_group_ids(self, instance_group_ids):
        """Sets the instance_group_ids of this DescribeInstanceGroupsRequest.


        :param instance_group_ids: The instance_group_ids of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_group_ids = instance_group_ids

    @property
    def instance_group_name(self):
        """Gets the instance_group_name of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The instance_group_name of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_group_name

    @instance_group_name.setter
    def instance_group_name(self, instance_group_name):
        """Sets the instance_group_name of this DescribeInstanceGroupsRequest.


        :param instance_group_name: The instance_group_name of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: str
        """

        self._instance_group_name = instance_group_name

    @property
    def max_results(self):
        """Gets the max_results of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The max_results of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeInstanceGroupsRequest.


        :param max_results: The max_results of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The next_token of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeInstanceGroupsRequest.


        :param next_token: The next_token of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def page_number(self):
        """Gets the page_number of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The page_number of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeInstanceGroupsRequest.


        :param page_number: The page_number of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The page_size of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeInstanceGroupsRequest.


        :param page_size: The page_size of this DescribeInstanceGroupsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeInstanceGroupsRequest.  # noqa: E501


        :return: The vpc_id of this DescribeInstanceGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeInstanceGroupsRequest.


        :param vpc_id: The vpc_id of this DescribeInstanceGroupsRequest.  # noqa: E501
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
        if issubclass(DescribeInstanceGroupsRequest, dict):
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
        if not isinstance(other, DescribeInstanceGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInstanceGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
