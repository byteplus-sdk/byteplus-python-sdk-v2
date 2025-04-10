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


class DescribeTrafficMirrorSessionsRequest(object):
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
        'max_results': 'int',
        'network_interface_id': 'str',
        'next_token': 'str',
        'packet_length': 'int',
        'priority': 'int',
        'project_name': 'str',
        'tag_filters': 'list[TagFilterForDescribeTrafficMirrorSessionsInput]',
        'traffic_mirror_filter_id': 'str',
        'traffic_mirror_session_ids': 'str',
        'traffic_mirror_session_names': 'str',
        'traffic_mirror_target_id': 'str',
        'virtual_network_id': 'int'
    }

    attribute_map = {
        'max_results': 'MaxResults',
        'network_interface_id': 'NetworkInterfaceId',
        'next_token': 'NextToken',
        'packet_length': 'PacketLength',
        'priority': 'Priority',
        'project_name': 'ProjectName',
        'tag_filters': 'TagFilters',
        'traffic_mirror_filter_id': 'TrafficMirrorFilterId',
        'traffic_mirror_session_ids': 'TrafficMirrorSessionIds',
        'traffic_mirror_session_names': 'TrafficMirrorSessionNames',
        'traffic_mirror_target_id': 'TrafficMirrorTargetId',
        'virtual_network_id': 'VirtualNetworkId'
    }

    def __init__(self, max_results=None, network_interface_id=None, next_token=None, packet_length=None, priority=None, project_name=None, tag_filters=None, traffic_mirror_filter_id=None, traffic_mirror_session_ids=None, traffic_mirror_session_names=None, traffic_mirror_target_id=None, virtual_network_id=None, _configuration=None):  # noqa: E501
        """DescribeTrafficMirrorSessionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_results = None
        self._network_interface_id = None
        self._next_token = None
        self._packet_length = None
        self._priority = None
        self._project_name = None
        self._tag_filters = None
        self._traffic_mirror_filter_id = None
        self._traffic_mirror_session_ids = None
        self._traffic_mirror_session_names = None
        self._traffic_mirror_target_id = None
        self._virtual_network_id = None
        self.discriminator = None

        if max_results is not None:
            self.max_results = max_results
        if network_interface_id is not None:
            self.network_interface_id = network_interface_id
        if next_token is not None:
            self.next_token = next_token
        if packet_length is not None:
            self.packet_length = packet_length
        if priority is not None:
            self.priority = priority
        if project_name is not None:
            self.project_name = project_name
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if traffic_mirror_filter_id is not None:
            self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if traffic_mirror_session_ids is not None:
            self.traffic_mirror_session_ids = traffic_mirror_session_ids
        if traffic_mirror_session_names is not None:
            self.traffic_mirror_session_names = traffic_mirror_session_names
        if traffic_mirror_target_id is not None:
            self.traffic_mirror_target_id = traffic_mirror_target_id
        if virtual_network_id is not None:
            self.virtual_network_id = virtual_network_id

    @property
    def max_results(self):
        """Gets the max_results of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The max_results of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeTrafficMirrorSessionsRequest.


        :param max_results: The max_results of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def network_interface_id(self):
        """Gets the network_interface_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The network_interface_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._network_interface_id

    @network_interface_id.setter
    def network_interface_id(self, network_interface_id):
        """Sets the network_interface_id of this DescribeTrafficMirrorSessionsRequest.


        :param network_interface_id: The network_interface_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._network_interface_id = network_interface_id

    @property
    def next_token(self):
        """Gets the next_token of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The next_token of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeTrafficMirrorSessionsRequest.


        :param next_token: The next_token of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def packet_length(self):
        """Gets the packet_length of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The packet_length of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._packet_length

    @packet_length.setter
    def packet_length(self, packet_length):
        """Sets the packet_length of this DescribeTrafficMirrorSessionsRequest.


        :param packet_length: The packet_length of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: int
        """

        self._packet_length = packet_length

    @property
    def priority(self):
        """Gets the priority of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The priority of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DescribeTrafficMirrorSessionsRequest.


        :param priority: The priority of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def project_name(self):
        """Gets the project_name of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The project_name of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeTrafficMirrorSessionsRequest.


        :param project_name: The project_name of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeTrafficMirrorSessionsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeTrafficMirrorSessionsRequest.


        :param tag_filters: The tag_filters of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeTrafficMirrorSessionsInput]
        """

        self._tag_filters = tag_filters

    @property
    def traffic_mirror_filter_id(self):
        """Gets the traffic_mirror_filter_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The traffic_mirror_filter_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        """Sets the traffic_mirror_filter_id of this DescribeTrafficMirrorSessionsRequest.


        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def traffic_mirror_session_ids(self):
        """Gets the traffic_mirror_session_ids of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The traffic_mirror_session_ids of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_session_ids

    @traffic_mirror_session_ids.setter
    def traffic_mirror_session_ids(self, traffic_mirror_session_ids):
        """Sets the traffic_mirror_session_ids of this DescribeTrafficMirrorSessionsRequest.


        :param traffic_mirror_session_ids: The traffic_mirror_session_ids of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_session_ids = traffic_mirror_session_ids

    @property
    def traffic_mirror_session_names(self):
        """Gets the traffic_mirror_session_names of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The traffic_mirror_session_names of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_session_names

    @traffic_mirror_session_names.setter
    def traffic_mirror_session_names(self, traffic_mirror_session_names):
        """Sets the traffic_mirror_session_names of this DescribeTrafficMirrorSessionsRequest.


        :param traffic_mirror_session_names: The traffic_mirror_session_names of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_session_names = traffic_mirror_session_names

    @property
    def traffic_mirror_target_id(self):
        """Gets the traffic_mirror_target_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The traffic_mirror_target_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_target_id

    @traffic_mirror_target_id.setter
    def traffic_mirror_target_id(self, traffic_mirror_target_id):
        """Sets the traffic_mirror_target_id of this DescribeTrafficMirrorSessionsRequest.


        :param traffic_mirror_target_id: The traffic_mirror_target_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_target_id = traffic_mirror_target_id

    @property
    def virtual_network_id(self):
        """Gets the virtual_network_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501


        :return: The virtual_network_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._virtual_network_id

    @virtual_network_id.setter
    def virtual_network_id(self, virtual_network_id):
        """Sets the virtual_network_id of this DescribeTrafficMirrorSessionsRequest.


        :param virtual_network_id: The virtual_network_id of this DescribeTrafficMirrorSessionsRequest.  # noqa: E501
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
        if issubclass(DescribeTrafficMirrorSessionsRequest, dict):
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
        if not isinstance(other, DescribeTrafficMirrorSessionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTrafficMirrorSessionsRequest):
            return True

        return self.to_dict() != other.to_dict()
