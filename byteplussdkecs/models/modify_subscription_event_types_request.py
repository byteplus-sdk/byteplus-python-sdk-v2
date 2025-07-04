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


class ModifySubscriptionEventTypesRequest(object):
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
        'event_types': 'list[str]',
        'subscription_id': 'str'
    }

    attribute_map = {
        'event_types': 'EventTypes',
        'subscription_id': 'SubscriptionId'
    }

    def __init__(self, event_types=None, subscription_id=None, _configuration=None):  # noqa: E501
        """ModifySubscriptionEventTypesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._event_types = None
        self._subscription_id = None
        self.discriminator = None

        if event_types is not None:
            self.event_types = event_types
        self.subscription_id = subscription_id

    @property
    def event_types(self):
        """Gets the event_types of this ModifySubscriptionEventTypesRequest.  # noqa: E501


        :return: The event_types of this ModifySubscriptionEventTypesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this ModifySubscriptionEventTypesRequest.


        :param event_types: The event_types of this ModifySubscriptionEventTypesRequest.  # noqa: E501
        :type: list[str]
        """

        self._event_types = event_types

    @property
    def subscription_id(self):
        """Gets the subscription_id of this ModifySubscriptionEventTypesRequest.  # noqa: E501


        :return: The subscription_id of this ModifySubscriptionEventTypesRequest.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this ModifySubscriptionEventTypesRequest.


        :param subscription_id: The subscription_id of this ModifySubscriptionEventTypesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and subscription_id is None:
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

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
        if issubclass(ModifySubscriptionEventTypesRequest, dict):
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
        if not isinstance(other, ModifySubscriptionEventTypesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifySubscriptionEventTypesRequest):
            return True

        return self.to_dict() != other.to_dict()
