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


class FilterForListModelCustomizationJobsInput(object):
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
        'create_time_after': 'str',
        'create_time_before': 'str',
        'custom_model_ids': 'list[str]',
        'customization_types': 'list[str]',
        'foundation_models': 'list[FoundationModelForListModelCustomizationJobsInput]',
        'ids': 'list[str]',
        'name': 'str',
        'phases': 'list[str]'
    }

    attribute_map = {
        'create_time_after': 'CreateTimeAfter',
        'create_time_before': 'CreateTimeBefore',
        'custom_model_ids': 'CustomModelIds',
        'customization_types': 'CustomizationTypes',
        'foundation_models': 'FoundationModels',
        'ids': 'Ids',
        'name': 'Name',
        'phases': 'Phases'
    }

    def __init__(self, create_time_after=None, create_time_before=None, custom_model_ids=None, customization_types=None, foundation_models=None, ids=None, name=None, phases=None, _configuration=None):  # noqa: E501
        """FilterForListModelCustomizationJobsInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time_after = None
        self._create_time_before = None
        self._custom_model_ids = None
        self._customization_types = None
        self._foundation_models = None
        self._ids = None
        self._name = None
        self._phases = None
        self.discriminator = None

        if create_time_after is not None:
            self.create_time_after = create_time_after
        if create_time_before is not None:
            self.create_time_before = create_time_before
        if custom_model_ids is not None:
            self.custom_model_ids = custom_model_ids
        if customization_types is not None:
            self.customization_types = customization_types
        if foundation_models is not None:
            self.foundation_models = foundation_models
        if ids is not None:
            self.ids = ids
        if name is not None:
            self.name = name
        if phases is not None:
            self.phases = phases

    @property
    def create_time_after(self):
        """Gets the create_time_after of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The create_time_after of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: str
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        """Sets the create_time_after of this FilterForListModelCustomizationJobsInput.


        :param create_time_after: The create_time_after of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: str
        """

        self._create_time_after = create_time_after

    @property
    def create_time_before(self):
        """Gets the create_time_before of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The create_time_before of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: str
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        """Sets the create_time_before of this FilterForListModelCustomizationJobsInput.


        :param create_time_before: The create_time_before of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: str
        """

        self._create_time_before = create_time_before

    @property
    def custom_model_ids(self):
        """Gets the custom_model_ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The custom_model_ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._custom_model_ids

    @custom_model_ids.setter
    def custom_model_ids(self, custom_model_ids):
        """Sets the custom_model_ids of this FilterForListModelCustomizationJobsInput.


        :param custom_model_ids: The custom_model_ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[str]
        """

        self._custom_model_ids = custom_model_ids

    @property
    def customization_types(self):
        """Gets the customization_types of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The customization_types of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._customization_types

    @customization_types.setter
    def customization_types(self, customization_types):
        """Sets the customization_types of this FilterForListModelCustomizationJobsInput.


        :param customization_types: The customization_types of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[str]
        """

        self._customization_types = customization_types

    @property
    def foundation_models(self):
        """Gets the foundation_models of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The foundation_models of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[FoundationModelForListModelCustomizationJobsInput]
        """
        return self._foundation_models

    @foundation_models.setter
    def foundation_models(self, foundation_models):
        """Sets the foundation_models of this FilterForListModelCustomizationJobsInput.


        :param foundation_models: The foundation_models of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[FoundationModelForListModelCustomizationJobsInput]
        """

        self._foundation_models = foundation_models

    @property
    def ids(self):
        """Gets the ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this FilterForListModelCustomizationJobsInput.


        :param ids: The ids of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[str]
        """

        self._ids = ids

    @property
    def name(self):
        """Gets the name of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The name of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FilterForListModelCustomizationJobsInput.


        :param name: The name of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phases(self):
        """Gets the phases of this FilterForListModelCustomizationJobsInput.  # noqa: E501


        :return: The phases of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._phases

    @phases.setter
    def phases(self, phases):
        """Sets the phases of this FilterForListModelCustomizationJobsInput.


        :param phases: The phases of this FilterForListModelCustomizationJobsInput.  # noqa: E501
        :type: list[str]
        """

        self._phases = phases

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
        if issubclass(FilterForListModelCustomizationJobsInput, dict):
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
        if not isinstance(other, FilterForListModelCustomizationJobsInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilterForListModelCustomizationJobsInput):
            return True

        return self.to_dict() != other.to_dict()
