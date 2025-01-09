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


class DescribeCloudAssistantStatusRequest(object):
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
        'client_version': 'str',
        'instance_ids': 'list[str]',
        'os_type': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'status': 'str'
    }

    attribute_map = {
        'client_version': 'ClientVersion',
        'instance_ids': 'InstanceIds',
        'os_type': 'OSType',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'status': 'Status'
    }

    def __init__(self, client_version=None, instance_ids=None, os_type=None, page_number=None, page_size=None, status=None, _configuration=None):  # noqa: E501
        """DescribeCloudAssistantStatusRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_version = None
        self._instance_ids = None
        self._os_type = None
        self._page_number = None
        self._page_size = None
        self._status = None
        self.discriminator = None

        if client_version is not None:
            self.client_version = client_version
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if os_type is not None:
            self.os_type = os_type
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if status is not None:
            self.status = status

    @property
    def client_version(self):
        """Gets the client_version of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The client_version of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_version

    @client_version.setter
    def client_version(self, client_version):
        """Sets the client_version of this DescribeCloudAssistantStatusRequest.


        :param client_version: The client_version of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: str
        """

        self._client_version = client_version

    @property
    def instance_ids(self):
        """Gets the instance_ids of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The instance_ids of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this DescribeCloudAssistantStatusRequest.


        :param instance_ids: The instance_ids of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def os_type(self):
        """Gets the os_type of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The os_type of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this DescribeCloudAssistantStatusRequest.


        :param os_type: The os_type of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: str
        """

        self._os_type = os_type

    @property
    def page_number(self):
        """Gets the page_number of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The page_number of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeCloudAssistantStatusRequest.


        :param page_number: The page_number of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The page_size of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeCloudAssistantStatusRequest.


        :param page_size: The page_size of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def status(self):
        """Gets the status of this DescribeCloudAssistantStatusRequest.  # noqa: E501


        :return: The status of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DescribeCloudAssistantStatusRequest.


        :param status: The status of this DescribeCloudAssistantStatusRequest.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(DescribeCloudAssistantStatusRequest, dict):
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
        if not isinstance(other, DescribeCloudAssistantStatusRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeCloudAssistantStatusRequest):
            return True

        return self.to_dict() != other.to_dict()
