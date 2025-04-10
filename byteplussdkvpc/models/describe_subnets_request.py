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


class DescribeSubnetsRequest(object):
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
        'is_default': 'bool',
        'max_results': 'int',
        'next_token': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'route_table_id': 'str',
        'subnet_ids': 'list[str]',
        'subnet_name': 'str',
        'subnet_owner_id': 'str',
        'tag_filters': 'list[TagFilterForDescribeSubnetsInput]',
        'vpc_id': 'str',
        'zone_id': 'str'
    }

    attribute_map = {
        'is_default': 'IsDefault',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'route_table_id': 'RouteTableId',
        'subnet_ids': 'SubnetIds',
        'subnet_name': 'SubnetName',
        'subnet_owner_id': 'SubnetOwnerId',
        'tag_filters': 'TagFilters',
        'vpc_id': 'VpcId',
        'zone_id': 'ZoneId'
    }

    def __init__(self, is_default=None, max_results=None, next_token=None, page_number=None, page_size=None, project_name=None, route_table_id=None, subnet_ids=None, subnet_name=None, subnet_owner_id=None, tag_filters=None, vpc_id=None, zone_id=None, _configuration=None):  # noqa: E501
        """DescribeSubnetsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_default = None
        self._max_results = None
        self._next_token = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._route_table_id = None
        self._subnet_ids = None
        self._subnet_name = None
        self._subnet_owner_id = None
        self._tag_filters = None
        self._vpc_id = None
        self._zone_id = None
        self.discriminator = None

        if is_default is not None:
            self.is_default = is_default
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if route_table_id is not None:
            self.route_table_id = route_table_id
        if subnet_ids is not None:
            self.subnet_ids = subnet_ids
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_owner_id is not None:
            self.subnet_owner_id = subnet_owner_id
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone_id is not None:
            self.zone_id = zone_id

    @property
    def is_default(self):
        """Gets the is_default of this DescribeSubnetsRequest.  # noqa: E501


        :return: The is_default of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this DescribeSubnetsRequest.


        :param is_default: The is_default of this DescribeSubnetsRequest.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def max_results(self):
        """Gets the max_results of this DescribeSubnetsRequest.  # noqa: E501


        :return: The max_results of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeSubnetsRequest.


        :param max_results: The max_results of this DescribeSubnetsRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeSubnetsRequest.  # noqa: E501


        :return: The next_token of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeSubnetsRequest.


        :param next_token: The next_token of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def page_number(self):
        """Gets the page_number of this DescribeSubnetsRequest.  # noqa: E501


        :return: The page_number of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeSubnetsRequest.


        :param page_number: The page_number of this DescribeSubnetsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeSubnetsRequest.  # noqa: E501


        :return: The page_size of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeSubnetsRequest.


        :param page_size: The page_size of this DescribeSubnetsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeSubnetsRequest.  # noqa: E501


        :return: The project_name of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeSubnetsRequest.


        :param project_name: The project_name of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def route_table_id(self):
        """Gets the route_table_id of this DescribeSubnetsRequest.  # noqa: E501


        :return: The route_table_id of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """Sets the route_table_id of this DescribeSubnetsRequest.


        :param route_table_id: The route_table_id of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._route_table_id = route_table_id

    @property
    def subnet_ids(self):
        """Gets the subnet_ids of this DescribeSubnetsRequest.  # noqa: E501


        :return: The subnet_ids of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """Sets the subnet_ids of this DescribeSubnetsRequest.


        :param subnet_ids: The subnet_ids of this DescribeSubnetsRequest.  # noqa: E501
        :type: list[str]
        """

        self._subnet_ids = subnet_ids

    @property
    def subnet_name(self):
        """Gets the subnet_name of this DescribeSubnetsRequest.  # noqa: E501


        :return: The subnet_name of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this DescribeSubnetsRequest.


        :param subnet_name: The subnet_name of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._subnet_name = subnet_name

    @property
    def subnet_owner_id(self):
        """Gets the subnet_owner_id of this DescribeSubnetsRequest.  # noqa: E501


        :return: The subnet_owner_id of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._subnet_owner_id

    @subnet_owner_id.setter
    def subnet_owner_id(self, subnet_owner_id):
        """Sets the subnet_owner_id of this DescribeSubnetsRequest.


        :param subnet_owner_id: The subnet_owner_id of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._subnet_owner_id = subnet_owner_id

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeSubnetsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeSubnetsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeSubnetsRequest.


        :param tag_filters: The tag_filters of this DescribeSubnetsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeSubnetsInput]
        """

        self._tag_filters = tag_filters

    @property
    def vpc_id(self):
        """Gets the vpc_id of this DescribeSubnetsRequest.  # noqa: E501


        :return: The vpc_id of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this DescribeSubnetsRequest.


        :param vpc_id: The vpc_id of this DescribeSubnetsRequest.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def zone_id(self):
        """Gets the zone_id of this DescribeSubnetsRequest.  # noqa: E501


        :return: The zone_id of this DescribeSubnetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DescribeSubnetsRequest.


        :param zone_id: The zone_id of this DescribeSubnetsRequest.  # noqa: E501
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
        if issubclass(DescribeSubnetsRequest, dict):
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
        if not isinstance(other, DescribeSubnetsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeSubnetsRequest):
            return True

        return self.to_dict() != other.to_dict()
