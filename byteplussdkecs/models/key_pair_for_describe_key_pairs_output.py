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


class KeyPairForDescribeKeyPairsOutput(object):
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
        'created_at': 'str',
        'description': 'str',
        'finger_print': 'str',
        'key_pair_id': 'str',
        'key_pair_name': 'str',
        'project_name': 'str',
        'tags': 'list[TagForDescribeKeyPairsOutput]',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'CreatedAt',
        'description': 'Description',
        'finger_print': 'FingerPrint',
        'key_pair_id': 'KeyPairId',
        'key_pair_name': 'KeyPairName',
        'project_name': 'ProjectName',
        'tags': 'Tags',
        'updated_at': 'UpdatedAt'
    }

    def __init__(self, created_at=None, description=None, finger_print=None, key_pair_id=None, key_pair_name=None, project_name=None, tags=None, updated_at=None, _configuration=None):  # noqa: E501
        """KeyPairForDescribeKeyPairsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_at = None
        self._description = None
        self._finger_print = None
        self._key_pair_id = None
        self._key_pair_name = None
        self._project_name = None
        self._tags = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if finger_print is not None:
            self.finger_print = finger_print
        if key_pair_id is not None:
            self.key_pair_id = key_pair_id
        if key_pair_name is not None:
            self.key_pair_name = key_pair_name
        if project_name is not None:
            self.project_name = project_name
        if tags is not None:
            self.tags = tags
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The created_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this KeyPairForDescribeKeyPairsOutput.


        :param created_at: The created_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The description of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeyPairForDescribeKeyPairsOutput.


        :param description: The description of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def finger_print(self):
        """Gets the finger_print of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The finger_print of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._finger_print

    @finger_print.setter
    def finger_print(self, finger_print):
        """Sets the finger_print of this KeyPairForDescribeKeyPairsOutput.


        :param finger_print: The finger_print of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._finger_print = finger_print

    @property
    def key_pair_id(self):
        """Gets the key_pair_id of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The key_pair_id of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_id

    @key_pair_id.setter
    def key_pair_id(self, key_pair_id):
        """Sets the key_pair_id of this KeyPairForDescribeKeyPairsOutput.


        :param key_pair_id: The key_pair_id of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._key_pair_id = key_pair_id

    @property
    def key_pair_name(self):
        """Gets the key_pair_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The key_pair_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_pair_name

    @key_pair_name.setter
    def key_pair_name(self, key_pair_name):
        """Sets the key_pair_name of this KeyPairForDescribeKeyPairsOutput.


        :param key_pair_name: The key_pair_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._key_pair_name = key_pair_name

    @property
    def project_name(self):
        """Gets the project_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The project_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this KeyPairForDescribeKeyPairsOutput.


        :param project_name: The project_name of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tags(self):
        """Gets the tags of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The tags of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: list[TagForDescribeKeyPairsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this KeyPairForDescribeKeyPairsOutput.


        :param tags: The tags of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: list[TagForDescribeKeyPairsOutput]
        """

        self._tags = tags

    @property
    def updated_at(self):
        """Gets the updated_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501


        :return: The updated_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this KeyPairForDescribeKeyPairsOutput.


        :param updated_at: The updated_at of this KeyPairForDescribeKeyPairsOutput.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(KeyPairForDescribeKeyPairsOutput, dict):
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
        if not isinstance(other, KeyPairForDescribeKeyPairsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyPairForDescribeKeyPairsOutput):
            return True

        return self.to_dict() != other.to_dict()
