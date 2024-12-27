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


class ModifyImageSharePermissionRequest(object):
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
        'add_accounts': 'list[str]',
        'image_id': 'str',
        'remove_accounts': 'list[str]'
    }

    attribute_map = {
        'add_accounts': 'AddAccounts',
        'image_id': 'ImageId',
        'remove_accounts': 'RemoveAccounts'
    }

    def __init__(self, add_accounts=None, image_id=None, remove_accounts=None, _configuration=None):  # noqa: E501
        """ModifyImageSharePermissionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._add_accounts = None
        self._image_id = None
        self._remove_accounts = None
        self.discriminator = None

        if add_accounts is not None:
            self.add_accounts = add_accounts
        if image_id is not None:
            self.image_id = image_id
        if remove_accounts is not None:
            self.remove_accounts = remove_accounts

    @property
    def add_accounts(self):
        """Gets the add_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501


        :return: The add_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_accounts

    @add_accounts.setter
    def add_accounts(self, add_accounts):
        """Sets the add_accounts of this ModifyImageSharePermissionRequest.


        :param add_accounts: The add_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501
        :type: list[str]
        """

        self._add_accounts = add_accounts

    @property
    def image_id(self):
        """Gets the image_id of this ModifyImageSharePermissionRequest.  # noqa: E501


        :return: The image_id of this ModifyImageSharePermissionRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ModifyImageSharePermissionRequest.


        :param image_id: The image_id of this ModifyImageSharePermissionRequest.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def remove_accounts(self):
        """Gets the remove_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501


        :return: The remove_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_accounts

    @remove_accounts.setter
    def remove_accounts(self, remove_accounts):
        """Sets the remove_accounts of this ModifyImageSharePermissionRequest.


        :param remove_accounts: The remove_accounts of this ModifyImageSharePermissionRequest.  # noqa: E501
        :type: list[str]
        """

        self._remove_accounts = remove_accounts

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
        if issubclass(ModifyImageSharePermissionRequest, dict):
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
        if not isinstance(other, ModifyImageSharePermissionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyImageSharePermissionRequest):
            return True

        return self.to_dict() != other.to_dict()
