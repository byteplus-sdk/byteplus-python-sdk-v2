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


class CancelInvitationRequest(object):
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
        'invitation_type': 'int',
        'relation': 'int',
        'relation_id': 'str',
        'sub_account_id': 'int'
    }

    attribute_map = {
        'invitation_type': 'InvitationType',
        'relation': 'Relation',
        'relation_id': 'RelationID',
        'sub_account_id': 'SubAccountID'
    }

    def __init__(self, invitation_type=None, relation=None, relation_id=None, sub_account_id=None, _configuration=None):  # noqa: E501
        """CancelInvitationRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invitation_type = None
        self._relation = None
        self._relation_id = None
        self._sub_account_id = None
        self.discriminator = None

        self.invitation_type = invitation_type
        if relation is not None:
            self.relation = relation
        self.relation_id = relation_id
        if sub_account_id is not None:
            self.sub_account_id = sub_account_id

    @property
    def invitation_type(self):
        """Gets the invitation_type of this CancelInvitationRequest.  # noqa: E501


        :return: The invitation_type of this CancelInvitationRequest.  # noqa: E501
        :rtype: int
        """
        return self._invitation_type

    @invitation_type.setter
    def invitation_type(self, invitation_type):
        """Sets the invitation_type of this CancelInvitationRequest.


        :param invitation_type: The invitation_type of this CancelInvitationRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and invitation_type is None:
            raise ValueError("Invalid value for `invitation_type`, must not be `None`")  # noqa: E501

        self._invitation_type = invitation_type

    @property
    def relation(self):
        """Gets the relation of this CancelInvitationRequest.  # noqa: E501


        :return: The relation of this CancelInvitationRequest.  # noqa: E501
        :rtype: int
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this CancelInvitationRequest.


        :param relation: The relation of this CancelInvitationRequest.  # noqa: E501
        :type: int
        """

        self._relation = relation

    @property
    def relation_id(self):
        """Gets the relation_id of this CancelInvitationRequest.  # noqa: E501


        :return: The relation_id of this CancelInvitationRequest.  # noqa: E501
        :rtype: str
        """
        return self._relation_id

    @relation_id.setter
    def relation_id(self, relation_id):
        """Sets the relation_id of this CancelInvitationRequest.


        :param relation_id: The relation_id of this CancelInvitationRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and relation_id is None:
            raise ValueError("Invalid value for `relation_id`, must not be `None`")  # noqa: E501

        self._relation_id = relation_id

    @property
    def sub_account_id(self):
        """Gets the sub_account_id of this CancelInvitationRequest.  # noqa: E501


        :return: The sub_account_id of this CancelInvitationRequest.  # noqa: E501
        :rtype: int
        """
        return self._sub_account_id

    @sub_account_id.setter
    def sub_account_id(self, sub_account_id):
        """Sets the sub_account_id of this CancelInvitationRequest.


        :param sub_account_id: The sub_account_id of this CancelInvitationRequest.  # noqa: E501
        :type: int
        """

        self._sub_account_id = sub_account_id

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
        if issubclass(CancelInvitationRequest, dict):
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
        if not isinstance(other, CancelInvitationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CancelInvitationRequest):
            return True

        return self.to_dict() != other.to_dict()
