# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class ContextCreateResponse(object):
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
        'id': 'str',
        'model': 'str',
        'truncation_strategy': 'TruncationStrategyForContextCreateOutput',
        'ttl': 'int',
        'usage': 'UsageForContextCreateOutput'
    }

    attribute_map = {
        'id': 'id',
        'model': 'model',
        'truncation_strategy': 'truncation_strategy',
        'ttl': 'ttl',
        'usage': 'usage'
    }

    def __init__(self, id=None, model=None, truncation_strategy=None, ttl=None, usage=None, _configuration=None):  # noqa: E501
        """ContextCreateResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._model = None
        self._truncation_strategy = None
        self._ttl = None
        self._usage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if model is not None:
            self.model = model
        if truncation_strategy is not None:
            self.truncation_strategy = truncation_strategy
        if ttl is not None:
            self.ttl = ttl
        if usage is not None:
            self.usage = usage

    @property
    def id(self):
        """Gets the id of this ContextCreateResponse.  # noqa: E501


        :return: The id of this ContextCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContextCreateResponse.


        :param id: The id of this ContextCreateResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this ContextCreateResponse.  # noqa: E501


        :return: The model of this ContextCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ContextCreateResponse.


        :param model: The model of this ContextCreateResponse.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def truncation_strategy(self):
        """Gets the truncation_strategy of this ContextCreateResponse.  # noqa: E501


        :return: The truncation_strategy of this ContextCreateResponse.  # noqa: E501
        :rtype: TruncationStrategyForContextCreateOutput
        """
        return self._truncation_strategy

    @truncation_strategy.setter
    def truncation_strategy(self, truncation_strategy):
        """Sets the truncation_strategy of this ContextCreateResponse.


        :param truncation_strategy: The truncation_strategy of this ContextCreateResponse.  # noqa: E501
        :type: TruncationStrategyForContextCreateOutput
        """

        self._truncation_strategy = truncation_strategy

    @property
    def ttl(self):
        """Gets the ttl of this ContextCreateResponse.  # noqa: E501


        :return: The ttl of this ContextCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this ContextCreateResponse.


        :param ttl: The ttl of this ContextCreateResponse.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def usage(self):
        """Gets the usage of this ContextCreateResponse.  # noqa: E501


        :return: The usage of this ContextCreateResponse.  # noqa: E501
        :rtype: UsageForContextCreateOutput
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this ContextCreateResponse.


        :param usage: The usage of this ContextCreateResponse.  # noqa: E501
        :type: UsageForContextCreateOutput
        """

        self._usage = usage

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
        if issubclass(ContextCreateResponse, dict):
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
        if not isinstance(other, ContextCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContextCreateResponse):
            return True

        return self.to_dict() != other.to_dict()
