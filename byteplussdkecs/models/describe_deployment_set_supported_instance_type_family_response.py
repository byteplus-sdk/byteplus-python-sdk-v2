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


class DescribeDeploymentSetSupportedInstanceTypeFamilyResponse(object):
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
        'deployment_set_create_instance_type_families': 'list[str]',
        'deployment_set_modify_instance_type_families': 'list[str]'
    }

    attribute_map = {
        'deployment_set_create_instance_type_families': 'DeploymentSetCreateInstanceTypeFamilies',
        'deployment_set_modify_instance_type_families': 'DeploymentSetModifyInstanceTypeFamilies'
    }

    def __init__(self, deployment_set_create_instance_type_families=None, deployment_set_modify_instance_type_families=None, _configuration=None):  # noqa: E501
        """DescribeDeploymentSetSupportedInstanceTypeFamilyResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deployment_set_create_instance_type_families = None
        self._deployment_set_modify_instance_type_families = None
        self.discriminator = None

        if deployment_set_create_instance_type_families is not None:
            self.deployment_set_create_instance_type_families = deployment_set_create_instance_type_families
        if deployment_set_modify_instance_type_families is not None:
            self.deployment_set_modify_instance_type_families = deployment_set_modify_instance_type_families

    @property
    def deployment_set_create_instance_type_families(self):
        """Gets the deployment_set_create_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501


        :return: The deployment_set_create_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._deployment_set_create_instance_type_families

    @deployment_set_create_instance_type_families.setter
    def deployment_set_create_instance_type_families(self, deployment_set_create_instance_type_families):
        """Sets the deployment_set_create_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.


        :param deployment_set_create_instance_type_families: The deployment_set_create_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501
        :type: list[str]
        """

        self._deployment_set_create_instance_type_families = deployment_set_create_instance_type_families

    @property
    def deployment_set_modify_instance_type_families(self):
        """Gets the deployment_set_modify_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501


        :return: The deployment_set_modify_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._deployment_set_modify_instance_type_families

    @deployment_set_modify_instance_type_families.setter
    def deployment_set_modify_instance_type_families(self, deployment_set_modify_instance_type_families):
        """Sets the deployment_set_modify_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.


        :param deployment_set_modify_instance_type_families: The deployment_set_modify_instance_type_families of this DescribeDeploymentSetSupportedInstanceTypeFamilyResponse.  # noqa: E501
        :type: list[str]
        """

        self._deployment_set_modify_instance_type_families = deployment_set_modify_instance_type_families

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
        if issubclass(DescribeDeploymentSetSupportedInstanceTypeFamilyResponse, dict):
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
        if not isinstance(other, DescribeDeploymentSetSupportedInstanceTypeFamilyResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeDeploymentSetSupportedInstanceTypeFamilyResponse):
            return True

        return self.to_dict() != other.to_dict()
