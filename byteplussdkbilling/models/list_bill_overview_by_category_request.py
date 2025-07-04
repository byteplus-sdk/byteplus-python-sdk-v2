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


class ListBillOverviewByCategoryRequest(object):
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
        'bill_category_parent': 'list[str]',
        'bill_period': 'str',
        'billing_mode': 'list[str]',
        'owner_id': 'list[int]',
        'payer_id': 'list[int]'
    }

    attribute_map = {
        'bill_category_parent': 'BillCategoryParent',
        'bill_period': 'BillPeriod',
        'billing_mode': 'BillingMode',
        'owner_id': 'OwnerID',
        'payer_id': 'PayerID'
    }

    def __init__(self, bill_category_parent=None, bill_period=None, billing_mode=None, owner_id=None, payer_id=None, _configuration=None):  # noqa: E501
        """ListBillOverviewByCategoryRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bill_category_parent = None
        self._bill_period = None
        self._billing_mode = None
        self._owner_id = None
        self._payer_id = None
        self.discriminator = None

        if bill_category_parent is not None:
            self.bill_category_parent = bill_category_parent
        self.bill_period = bill_period
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if owner_id is not None:
            self.owner_id = owner_id
        if payer_id is not None:
            self.payer_id = payer_id

    @property
    def bill_category_parent(self):
        """Gets the bill_category_parent of this ListBillOverviewByCategoryRequest.  # noqa: E501


        :return: The bill_category_parent of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bill_category_parent

    @bill_category_parent.setter
    def bill_category_parent(self, bill_category_parent):
        """Sets the bill_category_parent of this ListBillOverviewByCategoryRequest.


        :param bill_category_parent: The bill_category_parent of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :type: list[str]
        """

        self._bill_category_parent = bill_category_parent

    @property
    def bill_period(self):
        """Gets the bill_period of this ListBillOverviewByCategoryRequest.  # noqa: E501


        :return: The bill_period of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :rtype: str
        """
        return self._bill_period

    @bill_period.setter
    def bill_period(self, bill_period):
        """Sets the bill_period of this ListBillOverviewByCategoryRequest.


        :param bill_period: The bill_period of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bill_period is None:
            raise ValueError("Invalid value for `bill_period`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bill_period is not None and len(bill_period) > 7):
            raise ValueError("Invalid value for `bill_period`, length must be less than or equal to `7`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bill_period is not None and len(bill_period) < 7):
            raise ValueError("Invalid value for `bill_period`, length must be greater than or equal to `7`")  # noqa: E501

        self._bill_period = bill_period

    @property
    def billing_mode(self):
        """Gets the billing_mode of this ListBillOverviewByCategoryRequest.  # noqa: E501


        :return: The billing_mode of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this ListBillOverviewByCategoryRequest.


        :param billing_mode: The billing_mode of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :type: list[str]
        """

        self._billing_mode = billing_mode

    @property
    def owner_id(self):
        """Gets the owner_id of this ListBillOverviewByCategoryRequest.  # noqa: E501


        :return: The owner_id of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ListBillOverviewByCategoryRequest.


        :param owner_id: The owner_id of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :type: list[int]
        """

        self._owner_id = owner_id

    @property
    def payer_id(self):
        """Gets the payer_id of this ListBillOverviewByCategoryRequest.  # noqa: E501


        :return: The payer_id of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """Sets the payer_id of this ListBillOverviewByCategoryRequest.


        :param payer_id: The payer_id of this ListBillOverviewByCategoryRequest.  # noqa: E501
        :type: list[int]
        """

        self._payer_id = payer_id

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
        if issubclass(ListBillOverviewByCategoryRequest, dict):
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
        if not isinstance(other, ListBillOverviewByCategoryRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListBillOverviewByCategoryRequest):
            return True

        return self.to_dict() != other.to_dict()
