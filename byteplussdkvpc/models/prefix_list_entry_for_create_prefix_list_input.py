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


class PrefixListEntryForCreatePrefixListInput(object):
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
        'cidr': 'str',
        'description': 'str'
    }

    attribute_map = {
        'cidr': 'Cidr',
        'description': 'Description'
    }

    def __init__(self, cidr=None, description=None, _configuration=None):  # noqa: E501
        """PrefixListEntryForCreatePrefixListInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cidr = None
        self._description = None
        self.discriminator = None

        if cidr is not None:
            self.cidr = cidr
        if description is not None:
            self.description = description

    @property
    def cidr(self):
        """Gets the cidr of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501


        :return: The cidr of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this PrefixListEntryForCreatePrefixListInput.


        :param cidr: The cidr of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501
        :type: str
        """

        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501


        :return: The description of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PrefixListEntryForCreatePrefixListInput.


        :param description: The description of this PrefixListEntryForCreatePrefixListInput.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(PrefixListEntryForCreatePrefixListInput, dict):
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
        if not isinstance(other, PrefixListEntryForCreatePrefixListInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrefixListEntryForCreatePrefixListInput):
            return True

        return self.to_dict() != other.to_dict()
