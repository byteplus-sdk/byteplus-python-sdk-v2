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


class ScheduleSecretDeletionRequest(object):
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
        'force_delete': 'bool',
        'pending_window_in_days': 'int',
        'secret_name': 'str'
    }

    attribute_map = {
        'force_delete': 'ForceDelete',
        'pending_window_in_days': 'PendingWindowInDays',
        'secret_name': 'SecretName'
    }

    def __init__(self, force_delete=None, pending_window_in_days=None, secret_name=None, _configuration=None):  # noqa: E501
        """ScheduleSecretDeletionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._force_delete = None
        self._pending_window_in_days = None
        self._secret_name = None
        self.discriminator = None

        if force_delete is not None:
            self.force_delete = force_delete
        if pending_window_in_days is not None:
            self.pending_window_in_days = pending_window_in_days
        self.secret_name = secret_name

    @property
    def force_delete(self):
        """Gets the force_delete of this ScheduleSecretDeletionRequest.  # noqa: E501


        :return: The force_delete of this ScheduleSecretDeletionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this ScheduleSecretDeletionRequest.


        :param force_delete: The force_delete of this ScheduleSecretDeletionRequest.  # noqa: E501
        :type: bool
        """

        self._force_delete = force_delete

    @property
    def pending_window_in_days(self):
        """Gets the pending_window_in_days of this ScheduleSecretDeletionRequest.  # noqa: E501


        :return: The pending_window_in_days of this ScheduleSecretDeletionRequest.  # noqa: E501
        :rtype: int
        """
        return self._pending_window_in_days

    @pending_window_in_days.setter
    def pending_window_in_days(self, pending_window_in_days):
        """Sets the pending_window_in_days of this ScheduleSecretDeletionRequest.


        :param pending_window_in_days: The pending_window_in_days of this ScheduleSecretDeletionRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                pending_window_in_days is not None and pending_window_in_days > 30):  # noqa: E501
            raise ValueError("Invalid value for `pending_window_in_days`, must be a value less than or equal to `30`")  # noqa: E501
        if (self._configuration.client_side_validation and
                pending_window_in_days is not None and pending_window_in_days < 7):  # noqa: E501
            raise ValueError("Invalid value for `pending_window_in_days`, must be a value greater than or equal to `7`")  # noqa: E501

        self._pending_window_in_days = pending_window_in_days

    @property
    def secret_name(self):
        """Gets the secret_name of this ScheduleSecretDeletionRequest.  # noqa: E501


        :return: The secret_name of this ScheduleSecretDeletionRequest.  # noqa: E501
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this ScheduleSecretDeletionRequest.


        :param secret_name: The secret_name of this ScheduleSecretDeletionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and secret_name is None:
            raise ValueError("Invalid value for `secret_name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                secret_name is not None and len(secret_name) > 128):
            raise ValueError("Invalid value for `secret_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                secret_name is not None and len(secret_name) < 2):
            raise ValueError("Invalid value for `secret_name`, length must be greater than or equal to `2`")  # noqa: E501

        self._secret_name = secret_name

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
        if issubclass(ScheduleSecretDeletionRequest, dict):
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
        if not isinstance(other, ScheduleSecretDeletionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduleSecretDeletionRequest):
            return True

        return self.to_dict() != other.to_dict()
