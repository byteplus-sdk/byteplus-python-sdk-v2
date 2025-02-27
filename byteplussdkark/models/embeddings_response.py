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


class EmbeddingsResponse(object):
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
        'created': 'int',
        'data': 'list[DataForEmbeddingsOutput]',
        'id': 'str',
        'model': 'str',
        'object': 'str',
        'usage': 'UsageForEmbeddingsOutput'
    }

    attribute_map = {
        'created': 'created',
        'data': 'data',
        'id': 'id',
        'model': 'model',
        'object': 'object',
        'usage': 'usage'
    }

    def __init__(self, created=None, data=None, id=None, model=None, object=None, usage=None, _configuration=None):  # noqa: E501
        """EmbeddingsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._data = None
        self._id = None
        self._model = None
        self._object = None
        self._usage = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if data is not None:
            self.data = data
        if id is not None:
            self.id = id
        if model is not None:
            self.model = model
        if object is not None:
            self.object = object
        if usage is not None:
            self.usage = usage

    @property
    def created(self):
        """Gets the created of this EmbeddingsResponse.  # noqa: E501


        :return: The created of this EmbeddingsResponse.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EmbeddingsResponse.


        :param created: The created of this EmbeddingsResponse.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def data(self):
        """Gets the data of this EmbeddingsResponse.  # noqa: E501


        :return: The data of this EmbeddingsResponse.  # noqa: E501
        :rtype: list[DataForEmbeddingsOutput]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EmbeddingsResponse.


        :param data: The data of this EmbeddingsResponse.  # noqa: E501
        :type: list[DataForEmbeddingsOutput]
        """

        self._data = data

    @property
    def id(self):
        """Gets the id of this EmbeddingsResponse.  # noqa: E501


        :return: The id of this EmbeddingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmbeddingsResponse.


        :param id: The id of this EmbeddingsResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model(self):
        """Gets the model of this EmbeddingsResponse.  # noqa: E501


        :return: The model of this EmbeddingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this EmbeddingsResponse.


        :param model: The model of this EmbeddingsResponse.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def object(self):
        """Gets the object of this EmbeddingsResponse.  # noqa: E501


        :return: The object of this EmbeddingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this EmbeddingsResponse.


        :param object: The object of this EmbeddingsResponse.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def usage(self):
        """Gets the usage of this EmbeddingsResponse.  # noqa: E501


        :return: The usage of this EmbeddingsResponse.  # noqa: E501
        :rtype: UsageForEmbeddingsOutput
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this EmbeddingsResponse.


        :param usage: The usage of this EmbeddingsResponse.  # noqa: E501
        :type: UsageForEmbeddingsOutput
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
        if issubclass(EmbeddingsResponse, dict):
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
        if not isinstance(other, EmbeddingsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmbeddingsResponse):
            return True

        return self.to_dict() != other.to_dict()
