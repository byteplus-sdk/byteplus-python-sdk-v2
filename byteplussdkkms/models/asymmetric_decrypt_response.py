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


class AsymmetricDecryptResponse(object):
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
        'key_id': 'str',
        'plaintext': 'str'
    }

    attribute_map = {
        'key_id': 'KeyID',
        'plaintext': 'Plaintext'
    }

    def __init__(self, key_id=None, plaintext=None, _configuration=None):  # noqa: E501
        """AsymmetricDecryptResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._key_id = None
        self._plaintext = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if plaintext is not None:
            self.plaintext = plaintext

    @property
    def key_id(self):
        """Gets the key_id of this AsymmetricDecryptResponse.  # noqa: E501


        :return: The key_id of this AsymmetricDecryptResponse.  # noqa: E501
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this AsymmetricDecryptResponse.


        :param key_id: The key_id of this AsymmetricDecryptResponse.  # noqa: E501
        :type: str
        """

        self._key_id = key_id

    @property
    def plaintext(self):
        """Gets the plaintext of this AsymmetricDecryptResponse.  # noqa: E501


        :return: The plaintext of this AsymmetricDecryptResponse.  # noqa: E501
        :rtype: str
        """
        return self._plaintext

    @plaintext.setter
    def plaintext(self, plaintext):
        """Sets the plaintext of this AsymmetricDecryptResponse.


        :param plaintext: The plaintext of this AsymmetricDecryptResponse.  # noqa: E501
        :type: str
        """

        self._plaintext = plaintext

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
        if issubclass(AsymmetricDecryptResponse, dict):
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
        if not isinstance(other, AsymmetricDecryptResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AsymmetricDecryptResponse):
            return True

        return self.to_dict() != other.to_dict()
