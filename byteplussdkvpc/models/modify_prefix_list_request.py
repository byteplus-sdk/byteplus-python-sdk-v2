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


class ModifyPrefixListRequest(object):
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
        'add_prefix_list_entries': 'list[AddPrefixListEntryForModifyPrefixListInput]',
        'client_token': 'str',
        'description': 'str',
        'dry_run': 'bool',
        'max_entries': 'int',
        'prefix_list_id': 'str',
        'prefix_list_name': 'str',
        'remove_prefix_list_entries': 'list[RemovePrefixListEntryForModifyPrefixListInput]'
    }

    attribute_map = {
        'add_prefix_list_entries': 'AddPrefixListEntries',
        'client_token': 'ClientToken',
        'description': 'Description',
        'dry_run': 'DryRun',
        'max_entries': 'MaxEntries',
        'prefix_list_id': 'PrefixListId',
        'prefix_list_name': 'PrefixListName',
        'remove_prefix_list_entries': 'RemovePrefixListEntries'
    }

    def __init__(self, add_prefix_list_entries=None, client_token=None, description=None, dry_run=None, max_entries=None, prefix_list_id=None, prefix_list_name=None, remove_prefix_list_entries=None, _configuration=None):  # noqa: E501
        """ModifyPrefixListRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._add_prefix_list_entries = None
        self._client_token = None
        self._description = None
        self._dry_run = None
        self._max_entries = None
        self._prefix_list_id = None
        self._prefix_list_name = None
        self._remove_prefix_list_entries = None
        self.discriminator = None

        if add_prefix_list_entries is not None:
            self.add_prefix_list_entries = add_prefix_list_entries
        if client_token is not None:
            self.client_token = client_token
        if description is not None:
            self.description = description
        if dry_run is not None:
            self.dry_run = dry_run
        if max_entries is not None:
            self.max_entries = max_entries
        self.prefix_list_id = prefix_list_id
        if prefix_list_name is not None:
            self.prefix_list_name = prefix_list_name
        if remove_prefix_list_entries is not None:
            self.remove_prefix_list_entries = remove_prefix_list_entries

    @property
    def add_prefix_list_entries(self):
        """Gets the add_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501


        :return: The add_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: list[AddPrefixListEntryForModifyPrefixListInput]
        """
        return self._add_prefix_list_entries

    @add_prefix_list_entries.setter
    def add_prefix_list_entries(self, add_prefix_list_entries):
        """Sets the add_prefix_list_entries of this ModifyPrefixListRequest.


        :param add_prefix_list_entries: The add_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501
        :type: list[AddPrefixListEntryForModifyPrefixListInput]
        """

        self._add_prefix_list_entries = add_prefix_list_entries

    @property
    def client_token(self):
        """Gets the client_token of this ModifyPrefixListRequest.  # noqa: E501


        :return: The client_token of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyPrefixListRequest.


        :param client_token: The client_token of this ModifyPrefixListRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def description(self):
        """Gets the description of this ModifyPrefixListRequest.  # noqa: E501


        :return: The description of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyPrefixListRequest.


        :param description: The description of this ModifyPrefixListRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def dry_run(self):
        """Gets the dry_run of this ModifyPrefixListRequest.  # noqa: E501


        :return: The dry_run of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ModifyPrefixListRequest.


        :param dry_run: The dry_run of this ModifyPrefixListRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def max_entries(self):
        """Gets the max_entries of this ModifyPrefixListRequest.  # noqa: E501


        :return: The max_entries of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_entries

    @max_entries.setter
    def max_entries(self, max_entries):
        """Sets the max_entries of this ModifyPrefixListRequest.


        :param max_entries: The max_entries of this ModifyPrefixListRequest.  # noqa: E501
        :type: int
        """

        self._max_entries = max_entries

    @property
    def prefix_list_id(self):
        """Gets the prefix_list_id of this ModifyPrefixListRequest.  # noqa: E501


        :return: The prefix_list_id of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: str
        """
        return self._prefix_list_id

    @prefix_list_id.setter
    def prefix_list_id(self, prefix_list_id):
        """Sets the prefix_list_id of this ModifyPrefixListRequest.


        :param prefix_list_id: The prefix_list_id of this ModifyPrefixListRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and prefix_list_id is None:
            raise ValueError("Invalid value for `prefix_list_id`, must not be `None`")  # noqa: E501

        self._prefix_list_id = prefix_list_id

    @property
    def prefix_list_name(self):
        """Gets the prefix_list_name of this ModifyPrefixListRequest.  # noqa: E501


        :return: The prefix_list_name of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: str
        """
        return self._prefix_list_name

    @prefix_list_name.setter
    def prefix_list_name(self, prefix_list_name):
        """Sets the prefix_list_name of this ModifyPrefixListRequest.


        :param prefix_list_name: The prefix_list_name of this ModifyPrefixListRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                prefix_list_name is not None and len(prefix_list_name) > 128):
            raise ValueError("Invalid value for `prefix_list_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                prefix_list_name is not None and len(prefix_list_name) < 1):
            raise ValueError("Invalid value for `prefix_list_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._prefix_list_name = prefix_list_name

    @property
    def remove_prefix_list_entries(self):
        """Gets the remove_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501


        :return: The remove_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501
        :rtype: list[RemovePrefixListEntryForModifyPrefixListInput]
        """
        return self._remove_prefix_list_entries

    @remove_prefix_list_entries.setter
    def remove_prefix_list_entries(self, remove_prefix_list_entries):
        """Sets the remove_prefix_list_entries of this ModifyPrefixListRequest.


        :param remove_prefix_list_entries: The remove_prefix_list_entries of this ModifyPrefixListRequest.  # noqa: E501
        :type: list[RemovePrefixListEntryForModifyPrefixListInput]
        """

        self._remove_prefix_list_entries = remove_prefix_list_entries

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
        if issubclass(ModifyPrefixListRequest, dict):
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
        if not isinstance(other, ModifyPrefixListRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyPrefixListRequest):
            return True

        return self.to_dict() != other.to_dict()
