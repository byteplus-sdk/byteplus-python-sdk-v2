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


class ConfigListForQueryPriceForPayAsYouGoInput(object):
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
        'charge_item_code': 'str',
        'configuration_code': 'str',
        'count': 'str',
        'quantity': 'int',
        'use_duration': 'int'
    }

    attribute_map = {
        'charge_item_code': 'ChargeItemCode',
        'configuration_code': 'ConfigurationCode',
        'count': 'Count',
        'quantity': 'Quantity',
        'use_duration': 'UseDuration'
    }

    def __init__(self, charge_item_code=None, configuration_code=None, count=None, quantity=None, use_duration=None, _configuration=None):  # noqa: E501
        """ConfigListForQueryPriceForPayAsYouGoInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._charge_item_code = None
        self._configuration_code = None
        self._count = None
        self._quantity = None
        self._use_duration = None
        self.discriminator = None

        if charge_item_code is not None:
            self.charge_item_code = charge_item_code
        if configuration_code is not None:
            self.configuration_code = configuration_code
        if count is not None:
            self.count = count
        if quantity is not None:
            self.quantity = quantity
        if use_duration is not None:
            self.use_duration = use_duration

    @property
    def charge_item_code(self):
        """Gets the charge_item_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501


        :return: The charge_item_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :rtype: str
        """
        return self._charge_item_code

    @charge_item_code.setter
    def charge_item_code(self, charge_item_code):
        """Sets the charge_item_code of this ConfigListForQueryPriceForPayAsYouGoInput.


        :param charge_item_code: The charge_item_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :type: str
        """

        self._charge_item_code = charge_item_code

    @property
    def configuration_code(self):
        """Gets the configuration_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501


        :return: The configuration_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :rtype: str
        """
        return self._configuration_code

    @configuration_code.setter
    def configuration_code(self, configuration_code):
        """Sets the configuration_code of this ConfigListForQueryPriceForPayAsYouGoInput.


        :param configuration_code: The configuration_code of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :type: str
        """

        self._configuration_code = configuration_code

    @property
    def count(self):
        """Gets the count of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501


        :return: The count of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ConfigListForQueryPriceForPayAsYouGoInput.


        :param count: The count of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def quantity(self):
        """Gets the quantity of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501


        :return: The quantity of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ConfigListForQueryPriceForPayAsYouGoInput.


        :param quantity: The quantity of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def use_duration(self):
        """Gets the use_duration of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501


        :return: The use_duration of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :rtype: int
        """
        return self._use_duration

    @use_duration.setter
    def use_duration(self, use_duration):
        """Sets the use_duration of this ConfigListForQueryPriceForPayAsYouGoInput.


        :param use_duration: The use_duration of this ConfigListForQueryPriceForPayAsYouGoInput.  # noqa: E501
        :type: int
        """

        self._use_duration = use_duration

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
        if issubclass(ConfigListForQueryPriceForPayAsYouGoInput, dict):
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
        if not isinstance(other, ConfigListForQueryPriceForPayAsYouGoInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConfigListForQueryPriceForPayAsYouGoInput):
            return True

        return self.to_dict() != other.to_dict()
