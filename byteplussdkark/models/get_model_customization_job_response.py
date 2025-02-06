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


class GetModelCustomizationJobResponse(object):
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
        'create_time': 'str',
        'customization_type': 'str',
        'data': 'DataForGetModelCustomizationJobOutput',
        'description': 'str',
        'hyperparameters': 'list[HyperparameterForGetModelCustomizationJobOutput]',
        'id': 'str',
        'model_reference': 'ModelReferenceForGetModelCustomizationJobOutput',
        'name': 'str',
        'outputs': 'list[OutputForGetModelCustomizationJobOutput]',
        'project_name': 'str',
        'published_output_count': 'int',
        'reason': 'str',
        'save_model_limit': 'int',
        'status': 'StatusForGetModelCustomizationJobOutput',
        'tags': 'list[TagForGetModelCustomizationJobOutput]',
        'total_output_count': 'int',
        'update_time': 'str'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'customization_type': 'CustomizationType',
        'data': 'Data',
        'description': 'Description',
        'hyperparameters': 'Hyperparameters',
        'id': 'Id',
        'model_reference': 'ModelReference',
        'name': 'Name',
        'outputs': 'Outputs',
        'project_name': 'ProjectName',
        'published_output_count': 'PublishedOutputCount',
        'reason': 'Reason',
        'save_model_limit': 'SaveModelLimit',
        'status': 'Status',
        'tags': 'Tags',
        'total_output_count': 'TotalOutputCount',
        'update_time': 'UpdateTime'
    }

    def __init__(self, create_time=None, customization_type=None, data=None, description=None, hyperparameters=None, id=None, model_reference=None, name=None, outputs=None, project_name=None, published_output_count=None, reason=None, save_model_limit=None, status=None, tags=None, total_output_count=None, update_time=None, _configuration=None):  # noqa: E501
        """GetModelCustomizationJobResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._customization_type = None
        self._data = None
        self._description = None
        self._hyperparameters = None
        self._id = None
        self._model_reference = None
        self._name = None
        self._outputs = None
        self._project_name = None
        self._published_output_count = None
        self._reason = None
        self._save_model_limit = None
        self._status = None
        self._tags = None
        self._total_output_count = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if customization_type is not None:
            self.customization_type = customization_type
        if data is not None:
            self.data = data
        if description is not None:
            self.description = description
        if hyperparameters is not None:
            self.hyperparameters = hyperparameters
        if id is not None:
            self.id = id
        if model_reference is not None:
            self.model_reference = model_reference
        if name is not None:
            self.name = name
        if outputs is not None:
            self.outputs = outputs
        if project_name is not None:
            self.project_name = project_name
        if published_output_count is not None:
            self.published_output_count = published_output_count
        if reason is not None:
            self.reason = reason
        if save_model_limit is not None:
            self.save_model_limit = save_model_limit
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if total_output_count is not None:
            self.total_output_count = total_output_count
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The create_time of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetModelCustomizationJobResponse.


        :param create_time: The create_time of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def customization_type(self):
        """Gets the customization_type of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The customization_type of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._customization_type

    @customization_type.setter
    def customization_type(self, customization_type):
        """Sets the customization_type of this GetModelCustomizationJobResponse.


        :param customization_type: The customization_type of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._customization_type = customization_type

    @property
    def data(self):
        """Gets the data of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The data of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: DataForGetModelCustomizationJobOutput
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this GetModelCustomizationJobResponse.


        :param data: The data of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: DataForGetModelCustomizationJobOutput
        """

        self._data = data

    @property
    def description(self):
        """Gets the description of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The description of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetModelCustomizationJobResponse.


        :param description: The description of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hyperparameters(self):
        """Gets the hyperparameters of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The hyperparameters of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: list[HyperparameterForGetModelCustomizationJobOutput]
        """
        return self._hyperparameters

    @hyperparameters.setter
    def hyperparameters(self, hyperparameters):
        """Sets the hyperparameters of this GetModelCustomizationJobResponse.


        :param hyperparameters: The hyperparameters of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: list[HyperparameterForGetModelCustomizationJobOutput]
        """

        self._hyperparameters = hyperparameters

    @property
    def id(self):
        """Gets the id of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The id of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetModelCustomizationJobResponse.


        :param id: The id of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model_reference(self):
        """Gets the model_reference of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The model_reference of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: ModelReferenceForGetModelCustomizationJobOutput
        """
        return self._model_reference

    @model_reference.setter
    def model_reference(self, model_reference):
        """Sets the model_reference of this GetModelCustomizationJobResponse.


        :param model_reference: The model_reference of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: ModelReferenceForGetModelCustomizationJobOutput
        """

        self._model_reference = model_reference

    @property
    def name(self):
        """Gets the name of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The name of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetModelCustomizationJobResponse.


        :param name: The name of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The outputs of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: list[OutputForGetModelCustomizationJobOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this GetModelCustomizationJobResponse.


        :param outputs: The outputs of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: list[OutputForGetModelCustomizationJobOutput]
        """

        self._outputs = outputs

    @property
    def project_name(self):
        """Gets the project_name of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The project_name of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this GetModelCustomizationJobResponse.


        :param project_name: The project_name of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def published_output_count(self):
        """Gets the published_output_count of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The published_output_count of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._published_output_count

    @published_output_count.setter
    def published_output_count(self, published_output_count):
        """Sets the published_output_count of this GetModelCustomizationJobResponse.


        :param published_output_count: The published_output_count of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: int
        """

        self._published_output_count = published_output_count

    @property
    def reason(self):
        """Gets the reason of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The reason of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this GetModelCustomizationJobResponse.


        :param reason: The reason of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def save_model_limit(self):
        """Gets the save_model_limit of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The save_model_limit of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._save_model_limit

    @save_model_limit.setter
    def save_model_limit(self, save_model_limit):
        """Sets the save_model_limit of this GetModelCustomizationJobResponse.


        :param save_model_limit: The save_model_limit of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: int
        """

        self._save_model_limit = save_model_limit

    @property
    def status(self):
        """Gets the status of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The status of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: StatusForGetModelCustomizationJobOutput
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetModelCustomizationJobResponse.


        :param status: The status of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: StatusForGetModelCustomizationJobOutput
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The tags of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: list[TagForGetModelCustomizationJobOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetModelCustomizationJobResponse.


        :param tags: The tags of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: list[TagForGetModelCustomizationJobOutput]
        """

        self._tags = tags

    @property
    def total_output_count(self):
        """Gets the total_output_count of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The total_output_count of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_output_count

    @total_output_count.setter
    def total_output_count(self, total_output_count):
        """Sets the total_output_count of this GetModelCustomizationJobResponse.


        :param total_output_count: The total_output_count of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: int
        """

        self._total_output_count = total_output_count

    @property
    def update_time(self):
        """Gets the update_time of this GetModelCustomizationJobResponse.  # noqa: E501


        :return: The update_time of this GetModelCustomizationJobResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetModelCustomizationJobResponse.


        :param update_time: The update_time of this GetModelCustomizationJobResponse.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(GetModelCustomizationJobResponse, dict):
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
        if not isinstance(other, GetModelCustomizationJobResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetModelCustomizationJobResponse):
            return True

        return self.to_dict() != other.to_dict()
