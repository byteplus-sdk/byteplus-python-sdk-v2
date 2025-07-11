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


class ReplicaKeyForReplicateKeyOutput(object):
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
        'region': 'str',
        'trn': 'str'
    }

    attribute_map = {
        'region': 'Region',
        'trn': 'Trn'
    }

    def __init__(self, region=None, trn=None, _configuration=None):  # noqa: E501
        """ReplicaKeyForReplicateKeyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._region = None
        self._trn = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if trn is not None:
            self.trn = trn

    @property
    def region(self):
        """Gets the region of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501


        :return: The region of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ReplicaKeyForReplicateKeyOutput.


        :param region: The region of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def trn(self):
        """Gets the trn of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501


        :return: The trn of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this ReplicaKeyForReplicateKeyOutput.


        :param trn: The trn of this ReplicaKeyForReplicateKeyOutput.  # noqa: E501
        :type: str
        """

        self._trn = trn

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
        if issubclass(ReplicaKeyForReplicateKeyOutput, dict):
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
        if not isinstance(other, ReplicaKeyForReplicateKeyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReplicaKeyForReplicateKeyOutput):
            return True

        return self.to_dict() != other.to_dict()
