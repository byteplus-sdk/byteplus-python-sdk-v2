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


class KeyForDescribeKeyOutput(object):
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
        'creation_date': 'int',
        'description': 'str',
        'id': 'str',
        'key_material_expire_time': 'str',
        'key_name': 'str',
        'key_spec': 'str',
        'key_state': 'str',
        'key_usage': 'str',
        'last_rotation_time': 'str',
        'multi_region': 'bool',
        'multi_region_configuration': 'MultiRegionConfigurationForDescribeKeyOutput',
        'origin': 'str',
        'protection_level': 'str',
        'rotation_state': 'str',
        'schedule_delete_time': 'str',
        'schedule_rotation_time': 'str',
        'tags': 'list[TagForDescribeKeyOutput]',
        'trn': 'str',
        'update_date': 'int'
    }

    attribute_map = {
        'creation_date': 'CreationDate',
        'description': 'Description',
        'id': 'ID',
        'key_material_expire_time': 'KeyMaterialExpireTime',
        'key_name': 'KeyName',
        'key_spec': 'KeySpec',
        'key_state': 'KeyState',
        'key_usage': 'KeyUsage',
        'last_rotation_time': 'LastRotationTime',
        'multi_region': 'MultiRegion',
        'multi_region_configuration': 'MultiRegionConfiguration',
        'origin': 'Origin',
        'protection_level': 'ProtectionLevel',
        'rotation_state': 'RotationState',
        'schedule_delete_time': 'ScheduleDeleteTime',
        'schedule_rotation_time': 'ScheduleRotationTime',
        'tags': 'Tags',
        'trn': 'Trn',
        'update_date': 'UpdateDate'
    }

    def __init__(self, creation_date=None, description=None, id=None, key_material_expire_time=None, key_name=None, key_spec=None, key_state=None, key_usage=None, last_rotation_time=None, multi_region=None, multi_region_configuration=None, origin=None, protection_level=None, rotation_state=None, schedule_delete_time=None, schedule_rotation_time=None, tags=None, trn=None, update_date=None, _configuration=None):  # noqa: E501
        """KeyForDescribeKeyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation_date = None
        self._description = None
        self._id = None
        self._key_material_expire_time = None
        self._key_name = None
        self._key_spec = None
        self._key_state = None
        self._key_usage = None
        self._last_rotation_time = None
        self._multi_region = None
        self._multi_region_configuration = None
        self._origin = None
        self._protection_level = None
        self._rotation_state = None
        self._schedule_delete_time = None
        self._schedule_rotation_time = None
        self._tags = None
        self._trn = None
        self._update_date = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if key_material_expire_time is not None:
            self.key_material_expire_time = key_material_expire_time
        if key_name is not None:
            self.key_name = key_name
        if key_spec is not None:
            self.key_spec = key_spec
        if key_state is not None:
            self.key_state = key_state
        if key_usage is not None:
            self.key_usage = key_usage
        if last_rotation_time is not None:
            self.last_rotation_time = last_rotation_time
        if multi_region is not None:
            self.multi_region = multi_region
        if multi_region_configuration is not None:
            self.multi_region_configuration = multi_region_configuration
        if origin is not None:
            self.origin = origin
        if protection_level is not None:
            self.protection_level = protection_level
        if rotation_state is not None:
            self.rotation_state = rotation_state
        if schedule_delete_time is not None:
            self.schedule_delete_time = schedule_delete_time
        if schedule_rotation_time is not None:
            self.schedule_rotation_time = schedule_rotation_time
        if tags is not None:
            self.tags = tags
        if trn is not None:
            self.trn = trn
        if update_date is not None:
            self.update_date = update_date

    @property
    def creation_date(self):
        """Gets the creation_date of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The creation_date of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this KeyForDescribeKeyOutput.


        :param creation_date: The creation_date of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def description(self):
        """Gets the description of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The description of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeyForDescribeKeyOutput.


        :param description: The description of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The id of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeyForDescribeKeyOutput.


        :param id: The id of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def key_material_expire_time(self):
        """Gets the key_material_expire_time of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The key_material_expire_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_material_expire_time

    @key_material_expire_time.setter
    def key_material_expire_time(self, key_material_expire_time):
        """Sets the key_material_expire_time of this KeyForDescribeKeyOutput.


        :param key_material_expire_time: The key_material_expire_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._key_material_expire_time = key_material_expire_time

    @property
    def key_name(self):
        """Gets the key_name of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The key_name of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this KeyForDescribeKeyOutput.


        :param key_name: The key_name of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

    @property
    def key_spec(self):
        """Gets the key_spec of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The key_spec of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_spec

    @key_spec.setter
    def key_spec(self, key_spec):
        """Sets the key_spec of this KeyForDescribeKeyOutput.


        :param key_spec: The key_spec of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._key_spec = key_spec

    @property
    def key_state(self):
        """Gets the key_state of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The key_state of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this KeyForDescribeKeyOutput.


        :param key_state: The key_state of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._key_state = key_state

    @property
    def key_usage(self):
        """Gets the key_usage of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The key_usage of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_usage

    @key_usage.setter
    def key_usage(self, key_usage):
        """Sets the key_usage of this KeyForDescribeKeyOutput.


        :param key_usage: The key_usage of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._key_usage = key_usage

    @property
    def last_rotation_time(self):
        """Gets the last_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The last_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._last_rotation_time

    @last_rotation_time.setter
    def last_rotation_time(self, last_rotation_time):
        """Sets the last_rotation_time of this KeyForDescribeKeyOutput.


        :param last_rotation_time: The last_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._last_rotation_time = last_rotation_time

    @property
    def multi_region(self):
        """Gets the multi_region of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The multi_region of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: bool
        """
        return self._multi_region

    @multi_region.setter
    def multi_region(self, multi_region):
        """Sets the multi_region of this KeyForDescribeKeyOutput.


        :param multi_region: The multi_region of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: bool
        """

        self._multi_region = multi_region

    @property
    def multi_region_configuration(self):
        """Gets the multi_region_configuration of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The multi_region_configuration of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: MultiRegionConfigurationForDescribeKeyOutput
        """
        return self._multi_region_configuration

    @multi_region_configuration.setter
    def multi_region_configuration(self, multi_region_configuration):
        """Sets the multi_region_configuration of this KeyForDescribeKeyOutput.


        :param multi_region_configuration: The multi_region_configuration of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: MultiRegionConfigurationForDescribeKeyOutput
        """

        self._multi_region_configuration = multi_region_configuration

    @property
    def origin(self):
        """Gets the origin of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The origin of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this KeyForDescribeKeyOutput.


        :param origin: The origin of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def protection_level(self):
        """Gets the protection_level of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The protection_level of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._protection_level

    @protection_level.setter
    def protection_level(self, protection_level):
        """Sets the protection_level of this KeyForDescribeKeyOutput.


        :param protection_level: The protection_level of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._protection_level = protection_level

    @property
    def rotation_state(self):
        """Gets the rotation_state of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The rotation_state of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._rotation_state

    @rotation_state.setter
    def rotation_state(self, rotation_state):
        """Sets the rotation_state of this KeyForDescribeKeyOutput.


        :param rotation_state: The rotation_state of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._rotation_state = rotation_state

    @property
    def schedule_delete_time(self):
        """Gets the schedule_delete_time of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The schedule_delete_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_delete_time

    @schedule_delete_time.setter
    def schedule_delete_time(self, schedule_delete_time):
        """Sets the schedule_delete_time of this KeyForDescribeKeyOutput.


        :param schedule_delete_time: The schedule_delete_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._schedule_delete_time = schedule_delete_time

    @property
    def schedule_rotation_time(self):
        """Gets the schedule_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The schedule_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._schedule_rotation_time

    @schedule_rotation_time.setter
    def schedule_rotation_time(self, schedule_rotation_time):
        """Sets the schedule_rotation_time of this KeyForDescribeKeyOutput.


        :param schedule_rotation_time: The schedule_rotation_time of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._schedule_rotation_time = schedule_rotation_time

    @property
    def tags(self):
        """Gets the tags of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The tags of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: list[TagForDescribeKeyOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this KeyForDescribeKeyOutput.


        :param tags: The tags of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: list[TagForDescribeKeyOutput]
        """

        self._tags = tags

    @property
    def trn(self):
        """Gets the trn of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The trn of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this KeyForDescribeKeyOutput.


        :param trn: The trn of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: str
        """

        self._trn = trn

    @property
    def update_date(self):
        """Gets the update_date of this KeyForDescribeKeyOutput.  # noqa: E501


        :return: The update_date of this KeyForDescribeKeyOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this KeyForDescribeKeyOutput.


        :param update_date: The update_date of this KeyForDescribeKeyOutput.  # noqa: E501
        :type: int
        """

        self._update_date = update_date

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
        if issubclass(KeyForDescribeKeyOutput, dict):
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
        if not isinstance(other, KeyForDescribeKeyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeyForDescribeKeyOutput):
            return True

        return self.to_dict() != other.to_dict()
