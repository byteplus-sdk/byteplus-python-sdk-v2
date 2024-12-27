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


class ModifyInstanceChargeTypeRequest(object):
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
        'auto_pay': 'bool',
        'auto_renew': 'bool',
        'auto_renew_period': 'int',
        'client_token': 'str',
        'dry_run': 'bool',
        'include_data_volumes': 'bool',
        'instance_charge_type': 'str',
        'instance_ids': 'list[str]',
        'period': 'int',
        'period_unit': 'str'
    }

    attribute_map = {
        'auto_pay': 'AutoPay',
        'auto_renew': 'AutoRenew',
        'auto_renew_period': 'AutoRenewPeriod',
        'client_token': 'ClientToken',
        'dry_run': 'DryRun',
        'include_data_volumes': 'IncludeDataVolumes',
        'instance_charge_type': 'InstanceChargeType',
        'instance_ids': 'InstanceIds',
        'period': 'Period',
        'period_unit': 'PeriodUnit'
    }

    def __init__(self, auto_pay=None, auto_renew=None, auto_renew_period=None, client_token=None, dry_run=None, include_data_volumes=None, instance_charge_type=None, instance_ids=None, period=None, period_unit=None, _configuration=None):  # noqa: E501
        """ModifyInstanceChargeTypeRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_pay = None
        self._auto_renew = None
        self._auto_renew_period = None
        self._client_token = None
        self._dry_run = None
        self._include_data_volumes = None
        self._instance_charge_type = None
        self._instance_ids = None
        self._period = None
        self._period_unit = None
        self.discriminator = None

        if auto_pay is not None:
            self.auto_pay = auto_pay
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if auto_renew_period is not None:
            self.auto_renew_period = auto_renew_period
        if client_token is not None:
            self.client_token = client_token
        if dry_run is not None:
            self.dry_run = dry_run
        if include_data_volumes is not None:
            self.include_data_volumes = include_data_volumes
        if instance_charge_type is not None:
            self.instance_charge_type = instance_charge_type
        if instance_ids is not None:
            self.instance_ids = instance_ids
        if period is not None:
            self.period = period
        if period_unit is not None:
            self.period_unit = period_unit

    @property
    def auto_pay(self):
        """Gets the auto_pay of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The auto_pay of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this ModifyInstanceChargeTypeRequest.


        :param auto_pay: The auto_pay of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def auto_renew(self):
        """Gets the auto_renew of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The auto_renew of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this ModifyInstanceChargeTypeRequest.


        :param auto_renew: The auto_renew of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: bool
        """

        self._auto_renew = auto_renew

    @property
    def auto_renew_period(self):
        """Gets the auto_renew_period of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The auto_renew_period of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: int
        """
        return self._auto_renew_period

    @auto_renew_period.setter
    def auto_renew_period(self, auto_renew_period):
        """Sets the auto_renew_period of this ModifyInstanceChargeTypeRequest.


        :param auto_renew_period: The auto_renew_period of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: int
        """

        self._auto_renew_period = auto_renew_period

    @property
    def client_token(self):
        """Gets the client_token of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The client_token of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this ModifyInstanceChargeTypeRequest.


        :param client_token: The client_token of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def dry_run(self):
        """Gets the dry_run of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The dry_run of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ModifyInstanceChargeTypeRequest.


        :param dry_run: The dry_run of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def include_data_volumes(self):
        """Gets the include_data_volumes of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The include_data_volumes of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_data_volumes

    @include_data_volumes.setter
    def include_data_volumes(self, include_data_volumes):
        """Sets the include_data_volumes of this ModifyInstanceChargeTypeRequest.


        :param include_data_volumes: The include_data_volumes of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: bool
        """

        self._include_data_volumes = include_data_volumes

    @property
    def instance_charge_type(self):
        """Gets the instance_charge_type of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The instance_charge_type of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_charge_type

    @instance_charge_type.setter
    def instance_charge_type(self, instance_charge_type):
        """Sets the instance_charge_type of this ModifyInstanceChargeTypeRequest.


        :param instance_charge_type: The instance_charge_type of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: str
        """

        self._instance_charge_type = instance_charge_type

    @property
    def instance_ids(self):
        """Gets the instance_ids of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The instance_ids of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this ModifyInstanceChargeTypeRequest.


        :param instance_ids: The instance_ids of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: list[str]
        """

        self._instance_ids = instance_ids

    @property
    def period(self):
        """Gets the period of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The period of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: int
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ModifyInstanceChargeTypeRequest.


        :param period: The period of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: int
        """

        self._period = period

    @property
    def period_unit(self):
        """Gets the period_unit of this ModifyInstanceChargeTypeRequest.  # noqa: E501


        :return: The period_unit of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._period_unit

    @period_unit.setter
    def period_unit(self, period_unit):
        """Sets the period_unit of this ModifyInstanceChargeTypeRequest.


        :param period_unit: The period_unit of this ModifyInstanceChargeTypeRequest.  # noqa: E501
        :type: str
        """

        self._period_unit = period_unit

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
        if issubclass(ModifyInstanceChargeTypeRequest, dict):
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
        if not isinstance(other, ModifyInstanceChargeTypeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyInstanceChargeTypeRequest):
            return True

        return self.to_dict() != other.to_dict()
