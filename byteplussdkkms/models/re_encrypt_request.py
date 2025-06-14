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


class ReEncryptRequest(object):
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
        'ciphertext_blob': 'str',
        'new_encryption_context': 'dict(str, str)',
        'new_key_id': 'str',
        'new_key_name': 'str',
        'new_keyring_name': 'str',
        'old_encryption_context': 'dict(str, str)'
    }

    attribute_map = {
        'ciphertext_blob': 'CiphertextBlob',
        'new_encryption_context': 'NewEncryptionContext',
        'new_key_id': 'NewKeyID',
        'new_key_name': 'NewKeyName',
        'new_keyring_name': 'NewKeyringName',
        'old_encryption_context': 'OldEncryptionContext'
    }

    def __init__(self, ciphertext_blob=None, new_encryption_context=None, new_key_id=None, new_key_name=None, new_keyring_name=None, old_encryption_context=None, _configuration=None):  # noqa: E501
        """ReEncryptRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._ciphertext_blob = None
        self._new_encryption_context = None
        self._new_key_id = None
        self._new_key_name = None
        self._new_keyring_name = None
        self._old_encryption_context = None
        self.discriminator = None

        self.ciphertext_blob = ciphertext_blob
        if new_encryption_context is not None:
            self.new_encryption_context = new_encryption_context
        if new_key_id is not None:
            self.new_key_id = new_key_id
        if new_key_name is not None:
            self.new_key_name = new_key_name
        if new_keyring_name is not None:
            self.new_keyring_name = new_keyring_name
        if old_encryption_context is not None:
            self.old_encryption_context = old_encryption_context

    @property
    def ciphertext_blob(self):
        """Gets the ciphertext_blob of this ReEncryptRequest.  # noqa: E501


        :return: The ciphertext_blob of this ReEncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._ciphertext_blob

    @ciphertext_blob.setter
    def ciphertext_blob(self, ciphertext_blob):
        """Sets the ciphertext_blob of this ReEncryptRequest.


        :param ciphertext_blob: The ciphertext_blob of this ReEncryptRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ciphertext_blob is None:
            raise ValueError("Invalid value for `ciphertext_blob`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                ciphertext_blob is not None and len(ciphertext_blob) < 19):
            raise ValueError("Invalid value for `ciphertext_blob`, length must be greater than or equal to `19`")  # noqa: E501

        self._ciphertext_blob = ciphertext_blob

    @property
    def new_encryption_context(self):
        """Gets the new_encryption_context of this ReEncryptRequest.  # noqa: E501


        :return: The new_encryption_context of this ReEncryptRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._new_encryption_context

    @new_encryption_context.setter
    def new_encryption_context(self, new_encryption_context):
        """Sets the new_encryption_context of this ReEncryptRequest.


        :param new_encryption_context: The new_encryption_context of this ReEncryptRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._new_encryption_context = new_encryption_context

    @property
    def new_key_id(self):
        """Gets the new_key_id of this ReEncryptRequest.  # noqa: E501


        :return: The new_key_id of this ReEncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_key_id

    @new_key_id.setter
    def new_key_id(self, new_key_id):
        """Sets the new_key_id of this ReEncryptRequest.


        :param new_key_id: The new_key_id of this ReEncryptRequest.  # noqa: E501
        :type: str
        """

        self._new_key_id = new_key_id

    @property
    def new_key_name(self):
        """Gets the new_key_name of this ReEncryptRequest.  # noqa: E501


        :return: The new_key_name of this ReEncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_key_name

    @new_key_name.setter
    def new_key_name(self, new_key_name):
        """Sets the new_key_name of this ReEncryptRequest.


        :param new_key_name: The new_key_name of this ReEncryptRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                new_key_name is not None and len(new_key_name) > 31):
            raise ValueError("Invalid value for `new_key_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                new_key_name is not None and len(new_key_name) < 2):
            raise ValueError("Invalid value for `new_key_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._new_key_name = new_key_name

    @property
    def new_keyring_name(self):
        """Gets the new_keyring_name of this ReEncryptRequest.  # noqa: E501


        :return: The new_keyring_name of this ReEncryptRequest.  # noqa: E501
        :rtype: str
        """
        return self._new_keyring_name

    @new_keyring_name.setter
    def new_keyring_name(self, new_keyring_name):
        """Sets the new_keyring_name of this ReEncryptRequest.


        :param new_keyring_name: The new_keyring_name of this ReEncryptRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                new_keyring_name is not None and len(new_keyring_name) > 31):
            raise ValueError("Invalid value for `new_keyring_name`, length must be less than or equal to `31`")  # noqa: E501
        if (self._configuration.client_side_validation and
                new_keyring_name is not None and len(new_keyring_name) < 2):
            raise ValueError("Invalid value for `new_keyring_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._new_keyring_name = new_keyring_name

    @property
    def old_encryption_context(self):
        """Gets the old_encryption_context of this ReEncryptRequest.  # noqa: E501


        :return: The old_encryption_context of this ReEncryptRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._old_encryption_context

    @old_encryption_context.setter
    def old_encryption_context(self, old_encryption_context):
        """Sets the old_encryption_context of this ReEncryptRequest.


        :param old_encryption_context: The old_encryption_context of this ReEncryptRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._old_encryption_context = old_encryption_context

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
        if issubclass(ReEncryptRequest, dict):
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
        if not isinstance(other, ReEncryptRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReEncryptRequest):
            return True

        return self.to_dict() != other.to_dict()
