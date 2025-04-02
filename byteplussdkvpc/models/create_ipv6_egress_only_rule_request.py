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


class CreateIpv6EgressOnlyRuleRequest(object):
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
        'client_token': 'str',
        'description': 'str',
        'instance_id': 'str',
        'ipv6_gateway_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'client_token': 'ClientToken',
        'description': 'Description',
        'instance_id': 'InstanceId',
        'ipv6_gateway_id': 'Ipv6GatewayId',
        'name': 'Name'
    }

    def __init__(self, client_token=None, description=None, instance_id=None, ipv6_gateway_id=None, name=None, _configuration=None):  # noqa: E501
        """CreateIpv6EgressOnlyRuleRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_token = None
        self._description = None
        self._instance_id = None
        self._ipv6_gateway_id = None
        self._name = None
        self.discriminator = None

        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        self.instance_id = instance_id
        self.ipv6_gateway_id = ipv6_gateway_id
        if name is not None:
            self.name = name

    @property
    def client_token(self):
        """Gets the client_token of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501


        :return: The client_token of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this CreateIpv6EgressOnlyRuleRequest.


        :param client_token: The client_token of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501


        :return: The description of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIpv6EgressOnlyRuleRequest.


        :param description: The description of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501


        :return: The instance_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateIpv6EgressOnlyRuleRequest.


        :param instance_id: The instance_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and instance_id is None:
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def ipv6_gateway_id(self):
        """Gets the ipv6_gateway_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501


        :return: The ipv6_gateway_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_gateway_id

    @ipv6_gateway_id.setter
    def ipv6_gateway_id(self, ipv6_gateway_id):
        """Sets the ipv6_gateway_id of this CreateIpv6EgressOnlyRuleRequest.


        :param ipv6_gateway_id: The ipv6_gateway_id of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and ipv6_gateway_id is None:
            raise ValueError("Invalid value for `ipv6_gateway_id`, must not be `None`")  # noqa: E501

        self._ipv6_gateway_id = ipv6_gateway_id

    @property
    def name(self):
        """Gets the name of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501


        :return: The name of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIpv6EgressOnlyRuleRequest.


        :param name: The name of this CreateIpv6EgressOnlyRuleRequest.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(CreateIpv6EgressOnlyRuleRequest, dict):
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
        if not isinstance(other, CreateIpv6EgressOnlyRuleRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateIpv6EgressOnlyRuleRequest):
            return True

        return self.to_dict() != other.to_dict()
