# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class ListAvailableInstancesRequest(object):
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
        'begin_time_end': 'str',
        'begin_time_start': 'str',
        'expired_time_end': 'str',
        'expired_time_start': 'str',
        'instance_i_ds': 'list[str]',
        'max_results': 'int',
        'next_token': 'str',
        'product': 'str',
        'renew_type': 'str'
    }

    attribute_map = {
        'begin_time_end': 'BeginTimeEnd',
        'begin_time_start': 'BeginTimeStart',
        'expired_time_end': 'ExpiredTimeEnd',
        'expired_time_start': 'ExpiredTimeStart',
        'instance_i_ds': 'InstanceIDs',
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'product': 'Product',
        'renew_type': 'RenewType'
    }

    def __init__(self, begin_time_end=None, begin_time_start=None, expired_time_end=None, expired_time_start=None, instance_i_ds=None, max_results=None, next_token=None, product=None, renew_type=None, _configuration=None):  # noqa: E501
        """ListAvailableInstancesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_time_end = None
        self._begin_time_start = None
        self._expired_time_end = None
        self._expired_time_start = None
        self._instance_i_ds = None
        self._max_results = None
        self._next_token = None
        self._product = None
        self._renew_type = None
        self.discriminator = None

        if begin_time_end is not None:
            self.begin_time_end = begin_time_end
        if begin_time_start is not None:
            self.begin_time_start = begin_time_start
        if expired_time_end is not None:
            self.expired_time_end = expired_time_end
        if expired_time_start is not None:
            self.expired_time_start = expired_time_start
        if instance_i_ds is not None:
            self.instance_i_ds = instance_i_ds
        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if product is not None:
            self.product = product
        if renew_type is not None:
            self.renew_type = renew_type

    @property
    def begin_time_end(self):
        """Gets the begin_time_end of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The begin_time_end of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._begin_time_end

    @begin_time_end.setter
    def begin_time_end(self, begin_time_end):
        """Sets the begin_time_end of this ListAvailableInstancesRequest.


        :param begin_time_end: The begin_time_end of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._begin_time_end = begin_time_end

    @property
    def begin_time_start(self):
        """Gets the begin_time_start of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The begin_time_start of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._begin_time_start

    @begin_time_start.setter
    def begin_time_start(self, begin_time_start):
        """Sets the begin_time_start of this ListAvailableInstancesRequest.


        :param begin_time_start: The begin_time_start of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._begin_time_start = begin_time_start

    @property
    def expired_time_end(self):
        """Gets the expired_time_end of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The expired_time_end of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._expired_time_end

    @expired_time_end.setter
    def expired_time_end(self, expired_time_end):
        """Sets the expired_time_end of this ListAvailableInstancesRequest.


        :param expired_time_end: The expired_time_end of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._expired_time_end = expired_time_end

    @property
    def expired_time_start(self):
        """Gets the expired_time_start of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The expired_time_start of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._expired_time_start

    @expired_time_start.setter
    def expired_time_start(self, expired_time_start):
        """Sets the expired_time_start of this ListAvailableInstancesRequest.


        :param expired_time_start: The expired_time_start of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._expired_time_start = expired_time_start

    @property
    def instance_i_ds(self):
        """Gets the instance_i_ds of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The instance_i_ds of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_i_ds

    @instance_i_ds.setter
    def instance_i_ds(self, instance_i_ds):
        """Sets the instance_i_ds of this ListAvailableInstancesRequest.


        :param instance_i_ds: The instance_i_ds of this ListAvailableInstancesRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_i_ds = instance_i_ds

    @property
    def max_results(self):
        """Gets the max_results of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The max_results of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this ListAvailableInstancesRequest.


        :param max_results: The max_results of this ListAvailableInstancesRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The next_token of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this ListAvailableInstancesRequest.


        :param next_token: The next_token of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def product(self):
        """Gets the product of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The product of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ListAvailableInstancesRequest.


        :param product: The product of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def renew_type(self):
        """Gets the renew_type of this ListAvailableInstancesRequest.  # noqa: E501


        :return: The renew_type of this ListAvailableInstancesRequest.  # noqa: E501
        :rtype: str
        """
        return self._renew_type

    @renew_type.setter
    def renew_type(self, renew_type):
        """Sets the renew_type of this ListAvailableInstancesRequest.


        :param renew_type: The renew_type of this ListAvailableInstancesRequest.  # noqa: E501
        :type: str
        """

        self._renew_type = renew_type

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
        if issubclass(ListAvailableInstancesRequest, dict):
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
        if not isinstance(other, ListAvailableInstancesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAvailableInstancesRequest):
            return True

        return self.to_dict() != other.to_dict()
