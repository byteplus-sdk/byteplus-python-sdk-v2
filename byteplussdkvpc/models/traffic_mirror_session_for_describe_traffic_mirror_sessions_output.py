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


class TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput(object):
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
        'business_status': 'str',
        'created_at': 'str',
        'description': 'str',
        'lock_reason': 'str',
        'packet_length': 'int',
        'priority': 'int',
        'project_name': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeTrafficMirrorSessionsOutput]',
        'traffic_mirror_filter_id': 'str',
        'traffic_mirror_session_id': 'str',
        'traffic_mirror_session_name': 'str',
        'traffic_mirror_source_ids': 'list[str]',
        'traffic_mirror_target_id': 'str',
        'virtual_network_id': 'int'
    }

    attribute_map = {
        'business_status': 'BusinessStatus',
        'created_at': 'CreatedAt',
        'description': 'Description',
        'lock_reason': 'LockReason',
        'packet_length': 'PacketLength',
        'priority': 'Priority',
        'project_name': 'ProjectName',
        'status': 'Status',
        'tags': 'Tags',
        'traffic_mirror_filter_id': 'TrafficMirrorFilterId',
        'traffic_mirror_session_id': 'TrafficMirrorSessionId',
        'traffic_mirror_session_name': 'TrafficMirrorSessionName',
        'traffic_mirror_source_ids': 'TrafficMirrorSourceIds',
        'traffic_mirror_target_id': 'TrafficMirrorTargetId',
        'virtual_network_id': 'VirtualNetworkId'
    }

    def __init__(self, business_status=None, created_at=None, description=None, lock_reason=None, packet_length=None, priority=None, project_name=None, status=None, tags=None, traffic_mirror_filter_id=None, traffic_mirror_session_id=None, traffic_mirror_session_name=None, traffic_mirror_source_ids=None, traffic_mirror_target_id=None, virtual_network_id=None, _configuration=None):  # noqa: E501
        """TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._business_status = None
        self._created_at = None
        self._description = None
        self._lock_reason = None
        self._packet_length = None
        self._priority = None
        self._project_name = None
        self._status = None
        self._tags = None
        self._traffic_mirror_filter_id = None
        self._traffic_mirror_session_id = None
        self._traffic_mirror_session_name = None
        self._traffic_mirror_source_ids = None
        self._traffic_mirror_target_id = None
        self._virtual_network_id = None
        self.discriminator = None

        if business_status is not None:
            self.business_status = business_status
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if lock_reason is not None:
            self.lock_reason = lock_reason
        if packet_length is not None:
            self.packet_length = packet_length
        if priority is not None:
            self.priority = priority
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if traffic_mirror_filter_id is not None:
            self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if traffic_mirror_session_id is not None:
            self.traffic_mirror_session_id = traffic_mirror_session_id
        if traffic_mirror_session_name is not None:
            self.traffic_mirror_session_name = traffic_mirror_session_name
        if traffic_mirror_source_ids is not None:
            self.traffic_mirror_source_ids = traffic_mirror_source_ids
        if traffic_mirror_target_id is not None:
            self.traffic_mirror_target_id = traffic_mirror_target_id
        if virtual_network_id is not None:
            self.virtual_network_id = virtual_network_id

    @property
    def business_status(self):
        """Gets the business_status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The business_status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param business_status: The business_status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def created_at(self):
        """Gets the created_at of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The created_at of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param created_at: The created_at of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The description of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param description: The description of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def lock_reason(self):
        """Gets the lock_reason of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The lock_reason of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._lock_reason

    @lock_reason.setter
    def lock_reason(self, lock_reason):
        """Sets the lock_reason of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param lock_reason: The lock_reason of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._lock_reason = lock_reason

    @property
    def packet_length(self):
        """Gets the packet_length of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The packet_length of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param packet_length: The packet_length of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: int
        """

        self._packet_length = packet_length

    @property
    def priority(self):
        """Gets the priority of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The priority of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param priority: The priority of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def project_name(self):
        """Gets the project_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The project_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param project_name: The project_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param status: The status of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The tags of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: list[TagForDescribeTrafficMirrorSessionsOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param tags: The tags of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: list[TagForDescribeTrafficMirrorSessionsOutput]
        """

        self._tags = tags

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The traffic_mirror_filter_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_session_id(self):
        """Gets the traffic_mirror_session_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The traffic_mirror_session_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_session_id

    @traffic_mirror_session_id.setter
    def traffic_mirror_session_id(self, traffic_mirror_session_id):
        """Sets the traffic_mirror_session_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param traffic_mirror_session_id: The traffic_mirror_session_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_session_id = traffic_mirror_session_id

    @property
    def traffic_mirror_session_name(self):
        """Gets the traffic_mirror_session_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The traffic_mirror_session_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_session_name

    @traffic_mirror_session_name.setter
    def traffic_mirror_session_name(self, traffic_mirror_session_name):
        """Sets the traffic_mirror_session_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param traffic_mirror_session_name: The traffic_mirror_session_name of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_session_name = traffic_mirror_session_name

    @property
    def traffic_mirror_source_ids(self):
        """Gets the traffic_mirror_source_ids of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The traffic_mirror_source_ids of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._traffic_mirror_source_ids

    @traffic_mirror_source_ids.setter
    def traffic_mirror_source_ids(self, traffic_mirror_source_ids):
        """Sets the traffic_mirror_source_ids of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param traffic_mirror_source_ids: The traffic_mirror_source_ids of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: list[str]
        """

        self._traffic_mirror_source_ids = traffic_mirror_source_ids

    @property
    def traffic_mirror_target_id(self):
        """Gets the traffic_mirror_target_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The traffic_mirror_target_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_target_id

    @traffic_mirror_target_id.setter
    def traffic_mirror_target_id(self, traffic_mirror_target_id):
        """Sets the traffic_mirror_target_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param traffic_mirror_target_id: The traffic_mirror_target_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_target_id = traffic_mirror_target_id

    @property
    def virtual_network_id(self):
        """Gets the virtual_network_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501


        :return: The virtual_network_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :rtype: int
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, virtual_network_id):
        """Sets the virtual_network_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.


        :param virtual_network_id: The virtual_network_id of this TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput.  # noqa: E501
        :type: int
        """

        self._virtual_network_id = virtual_network_id

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
        if issubclass(TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput, dict):
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
        if not isinstance(other, TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrafficMirrorSessionForDescribeTrafficMirrorSessionsOutput):
            return True

        return self.to_dict() != other.to_dict()
