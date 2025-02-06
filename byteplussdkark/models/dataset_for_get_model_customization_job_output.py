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


class DatasetForGetModelCustomizationJobOutput(object):
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
        'dataset_id': 'str',
        'dataset_version_id': 'str',
        'multiplier': 'float',
        'sample_count': 'int'
    }

    attribute_map = {
        'dataset_id': 'DatasetId',
        'dataset_version_id': 'DatasetVersionId',
        'multiplier': 'Multiplier',
        'sample_count': 'SampleCount'
    }

    def __init__(self, dataset_id=None, dataset_version_id=None, multiplier=None, sample_count=None, _configuration=None):  # noqa: E501
        """DatasetForGetModelCustomizationJobOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._dataset_id = None
        self._dataset_version_id = None
        self._multiplier = None
        self._sample_count = None
        self.discriminator = None

        if dataset_id is not None:
            self.dataset_id = dataset_id
        if dataset_version_id is not None:
            self.dataset_version_id = dataset_version_id
        if multiplier is not None:
            self.multiplier = multiplier
        if sample_count is not None:
            self.sample_count = sample_count

    @property
    def dataset_id(self):
        """Gets the dataset_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The dataset_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this DatasetForGetModelCustomizationJobOutput.


        :param dataset_id: The dataset_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def dataset_version_id(self):
        """Gets the dataset_version_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The dataset_version_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: str
        """
        return self._dataset_version_id

    @dataset_version_id.setter
    def dataset_version_id(self, dataset_version_id):
        """Sets the dataset_version_id of this DatasetForGetModelCustomizationJobOutput.


        :param dataset_version_id: The dataset_version_id of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: str
        """

        self._dataset_version_id = dataset_version_id

    @property
    def multiplier(self):
        """Gets the multiplier of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The multiplier of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this DatasetForGetModelCustomizationJobOutput.


        :param multiplier: The multiplier of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def sample_count(self):
        """Gets the sample_count of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501


        :return: The sample_count of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :rtype: int
        """
        return self._sample_count

    @sample_count.setter
    def sample_count(self, sample_count):
        """Sets the sample_count of this DatasetForGetModelCustomizationJobOutput.


        :param sample_count: The sample_count of this DatasetForGetModelCustomizationJobOutput.  # noqa: E501
        :type: int
        """

        self._sample_count = sample_count

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
        if issubclass(DatasetForGetModelCustomizationJobOutput, dict):
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
        if not isinstance(other, DatasetForGetModelCustomizationJobOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatasetForGetModelCustomizationJobOutput):
            return True

        return self.to_dict() != other.to_dict()
