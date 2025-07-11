# coding: utf-8

"""
    kms

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class CreateKeyRequest(object):
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
        'description': 'str',
        'key_name': 'str',
        'key_spec': 'str',
        'key_usage': 'str',
        'keyring_name': 'str',
        'multi_region': 'bool',
        'origin': 'str',
        'protection_level': 'str',
        'rotate_state': 'str',
        'tags': 'list[TagForCreateKeyInput]'
    }

    attribute_map = {
        'description': 'Description',
        'key_name': 'KeyName',
        'key_spec': 'KeySpec',
        'key_usage': 'KeyUsage',
        'keyring_name': 'KeyringName',
        'multi_region': 'MultiRegion',
        'origin': 'Origin',
        'protection_level': 'ProtectionLevel',
        'rotate_state': 'RotateState',
        'tags': 'Tags'
    }

    def __init__(self, description=None, key_name=None, key_spec=None, key_usage=None, keyring_name=None, multi_region=None, origin=None, protection_level=None, rotate_state=None, tags=None, _configuration=None):  # noqa: E501
        """CreateKeyRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._key_name = None
        self._key_spec = None
        self._key_usage = None
        self._keyring_name = None
        self._multi_region = None
        self._origin = None
        self._protection_level = None
        self._rotate_state = None
        self._tags = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.key_name = key_name
        if key_spec is not None:
            self.key_spec = key_spec
        if key_usage is not None:
            self.key_usage = key_usage
        self.keyring_name = keyring_name
        if multi_region is not None:
            self.multi_region = multi_region
        if origin is not None:
            self.origin = origin
        if protection_level is not None:
            self.protection_level = protection_level
        if rotate_state is not None:
            self.rotate_state = rotate_state
        if tags is not None:
            self.tags = tags

    @property
    def description(self):
        """Gets the description of this CreateKeyRequest.  # noqa: E501


        :return: The description of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateKeyRequest.


        :param description: The description of this CreateKeyRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 8192):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `8192`")  # noqa: E501

        self._description = description

    @property
    def key_name(self):
        """Gets the key_name of this CreateKeyRequest.  # noqa: E501


        :return: The key_name of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this CreateKeyRequest.


        :param key_name: The key_name of this CreateKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and key_name is None:
            raise ValueError("Invalid value for `key_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key_name is not None and len(key_name) > 31):
            raise ValueError("Invalid value for `key_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                key_name is not None and len(key_name) < 2):
            raise ValueError("Invalid value for `key_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._key_name = key_name

    @property
    def key_spec(self):
        """Gets the key_spec of this CreateKeyRequest.  # noqa: E501


        :return: The key_spec of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        """Sets the key_spec of this CreateKeyRequest.


        :param key_spec: The key_spec of this CreateKeyRequest.  # noqa: E501
        :type: str
        """

        self._key_spec = key_spec

    @property
    def key_usage(self):
        """Gets the key_usage of this CreateKeyRequest.  # noqa: E501


        :return: The key_usage of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this CreateKeyRequest.


        :param key_usage: The key_usage of this CreateKeyRequest.  # noqa: E501
        :type: str
        """

        self._key_usage = key_usage

    @property
    def keyring_name(self):
        """Gets the keyring_name of this CreateKeyRequest.  # noqa: E501


        :return: The keyring_name of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyring_name

    @keyring_name.setter
    def keyring_name(self, keyring_name):
        """Sets the keyring_name of this CreateKeyRequest.


        :param keyring_name: The keyring_name of this CreateKeyRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and keyring_name is None:
            raise ValueError("Invalid value for `keyring_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                keyring_name is not None and len(keyring_name) > 31):
            raise ValueError("Invalid value for `keyring_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                keyring_name is not None and len(keyring_name) < 2):
            raise ValueError("Invalid value for `keyring_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._keyring_name = keyring_name

    @property
    def multi_region(self):
        """Gets the multi_region of this CreateKeyRequest.  # noqa: E501


        :return: The multi_region of this CreateKeyRequest.  # noqa: E501
        :rtype: bool
        """
        return self._multi_region

    @multi_region.setter
    def multi_region(self, multi_region):
        """Sets the multi_region of this CreateKeyRequest.


        :param multi_region: The multi_region of this CreateKeyRequest.  # noqa: E501
        :type: bool
        """

        self._multi_region = multi_region

    @property
    def origin(self):
        """Gets the origin of this CreateKeyRequest.  # noqa: E501


        :return: The origin of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this CreateKeyRequest.


        :param origin: The origin of this CreateKeyRequest.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def protection_level(self):
        """Gets the protection_level of this CreateKeyRequest.  # noqa: E501


        :return: The protection_level of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._protection_level

    @protection_level.setter
    def protection_level(self, protection_level):
        """Sets the protection_level of this CreateKeyRequest.


        :param protection_level: The protection_level of this CreateKeyRequest.  # noqa: E501
        :type: str
        """

        self._protection_level = protection_level

    @property
    def rotate_state(self):
        """Gets the rotate_state of this CreateKeyRequest.  # noqa: E501


        :return: The rotate_state of this CreateKeyRequest.  # noqa: E501
        :rtype: str
        """
        return self._rotate_state

    @rotate_state.setter
    def rotate_state(self, rotate_state):
        """Sets the rotate_state of this CreateKeyRequest.


        :param rotate_state: The rotate_state of this CreateKeyRequest.  # noqa: E501
        :type: str
        """

        self._rotate_state = rotate_state

    @property
    def tags(self):
        """Gets the tags of this CreateKeyRequest.  # noqa: E501


        :return: The tags of this CreateKeyRequest.  # noqa: E501
        :rtype: list[TagForCreateKeyInput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateKeyRequest.


        :param tags: The tags of this CreateKeyRequest.  # noqa: E501
        :type: list[TagForCreateKeyInput]
        """

        self._tags = tags

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
        if issubclass(CreateKeyRequest, dict):
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
        if not isinstance(other, CreateKeyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateKeyRequest):
            return True

        return self.to_dict() != other.to_dict()
