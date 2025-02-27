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


class BatchChatCompletionsRequest(object):
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
        'frequency_penalty': 'float',
        'logit_bias': 'LogitBiasForBatchChatCompletionsInput',
        'logprobs': 'bool',
        'max_tokens': 'int',
        'messages': 'list[MessageForBatchChatCompletionsInput]',
        'model': 'str',
        'presence_penalty': 'float',
        'stop': 'list[str]',
        'stream': 'bool',
        'stream_options': 'StreamOptionsForBatchChatCompletionsInput',
        'temperature': 'float',
        'tools': 'list[ToolForBatchChatCompletionsInput]',
        'top_logprobs': 'int',
        'top_p': 'float'
    }

    attribute_map = {
        'frequency_penalty': 'frequency_penalty',
        'logit_bias': 'logit_bias',
        'logprobs': 'logprobs',
        'max_tokens': 'max_tokens',
        'messages': 'messages',
        'model': 'model',
        'presence_penalty': 'presence_penalty',
        'stop': 'stop',
        'stream': 'stream',
        'stream_options': 'stream_options',
        'temperature': 'temperature',
        'tools': 'tools',
        'top_logprobs': 'top_logprobs',
        'top_p': 'top_p'
    }

    def __init__(self, frequency_penalty=None, logit_bias=None, logprobs=None, max_tokens=None, messages=None, model=None, presence_penalty=None, stop=None, stream=None, stream_options=None, temperature=None, tools=None, top_logprobs=None, top_p=None, _configuration=None):  # noqa: E501
        """BatchChatCompletionsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._frequency_penalty = None
        self._logit_bias = None
        self._logprobs = None
        self._max_tokens = None
        self._messages = None
        self._model = None
        self._presence_penalty = None
        self._stop = None
        self._stream = None
        self._stream_options = None
        self._temperature = None
        self._tools = None
        self._top_logprobs = None
        self._top_p = None
        self.discriminator = None

        if frequency_penalty is not None:
            self.frequency_penalty = frequency_penalty
        if logit_bias is not None:
            self.logit_bias = logit_bias
        if logprobs is not None:
            self.logprobs = logprobs
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if messages is not None:
            self.messages = messages
        self.model = model
        if presence_penalty is not None:
            self.presence_penalty = presence_penalty
        if stop is not None:
            self.stop = stop
        if stream is not None:
            self.stream = stream
        if stream_options is not None:
            self.stream_options = stream_options
        if temperature is not None:
            self.temperature = temperature
        if tools is not None:
            self.tools = tools
        if top_logprobs is not None:
            self.top_logprobs = top_logprobs
        if top_p is not None:
            self.top_p = top_p

    @property
    def frequency_penalty(self):
        """Gets the frequency_penalty of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The frequency_penalty of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._frequency_penalty

    @frequency_penalty.setter
    def frequency_penalty(self, frequency_penalty):
        """Sets the frequency_penalty of this BatchChatCompletionsRequest.


        :param frequency_penalty: The frequency_penalty of this BatchChatCompletionsRequest.  # noqa: E501
        :type: float
        """

        self._frequency_penalty = frequency_penalty

    @property
    def logit_bias(self):
        """Gets the logit_bias of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The logit_bias of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: LogitBiasForBatchChatCompletionsInput
        """
        return self._logit_bias

    @logit_bias.setter
    def logit_bias(self, logit_bias):
        """Sets the logit_bias of this BatchChatCompletionsRequest.


        :param logit_bias: The logit_bias of this BatchChatCompletionsRequest.  # noqa: E501
        :type: LogitBiasForBatchChatCompletionsInput
        """

        self._logit_bias = logit_bias

    @property
    def logprobs(self):
        """Gets the logprobs of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The logprobs of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._logprobs

    @logprobs.setter
    def logprobs(self, logprobs):
        """Sets the logprobs of this BatchChatCompletionsRequest.


        :param logprobs: The logprobs of this BatchChatCompletionsRequest.  # noqa: E501
        :type: bool
        """

        self._logprobs = logprobs

    @property
    def max_tokens(self):
        """Gets the max_tokens of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The max_tokens of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """Sets the max_tokens of this BatchChatCompletionsRequest.


        :param max_tokens: The max_tokens of this BatchChatCompletionsRequest.  # noqa: E501
        :type: int
        """

        self._max_tokens = max_tokens

    @property
    def messages(self):
        """Gets the messages of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The messages of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: list[MessageForBatchChatCompletionsInput]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this BatchChatCompletionsRequest.


        :param messages: The messages of this BatchChatCompletionsRequest.  # noqa: E501
        :type: list[MessageForBatchChatCompletionsInput]
        """

        self._messages = messages

    @property
    def model(self):
        """Gets the model of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The model of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this BatchChatCompletionsRequest.


        :param model: The model of this BatchChatCompletionsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and model is None:
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def presence_penalty(self):
        """Gets the presence_penalty of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The presence_penalty of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty):
        """Sets the presence_penalty of this BatchChatCompletionsRequest.


        :param presence_penalty: The presence_penalty of this BatchChatCompletionsRequest.  # noqa: E501
        :type: float
        """

        self._presence_penalty = presence_penalty

    @property
    def stop(self):
        """Gets the stop of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The stop of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this BatchChatCompletionsRequest.


        :param stop: The stop of this BatchChatCompletionsRequest.  # noqa: E501
        :type: list[str]
        """

        self._stop = stop

    @property
    def stream(self):
        """Gets the stream of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The stream of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this BatchChatCompletionsRequest.


        :param stream: The stream of this BatchChatCompletionsRequest.  # noqa: E501
        :type: bool
        """

        self._stream = stream

    @property
    def stream_options(self):
        """Gets the stream_options of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The stream_options of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: StreamOptionsForBatchChatCompletionsInput
        """
        return self._stream_options

    @stream_options.setter
    def stream_options(self, stream_options):
        """Sets the stream_options of this BatchChatCompletionsRequest.


        :param stream_options: The stream_options of this BatchChatCompletionsRequest.  # noqa: E501
        :type: StreamOptionsForBatchChatCompletionsInput
        """

        self._stream_options = stream_options

    @property
    def temperature(self):
        """Gets the temperature of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The temperature of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this BatchChatCompletionsRequest.


        :param temperature: The temperature of this BatchChatCompletionsRequest.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def tools(self):
        """Gets the tools of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The tools of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: list[ToolForBatchChatCompletionsInput]
        """
        return self._tools

    @tools.setter
    def tools(self, tools):
        """Sets the tools of this BatchChatCompletionsRequest.


        :param tools: The tools of this BatchChatCompletionsRequest.  # noqa: E501
        :type: list[ToolForBatchChatCompletionsInput]
        """

        self._tools = tools

    @property
    def top_logprobs(self):
        """Gets the top_logprobs of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The top_logprobs of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: int
        """
        return self._top_logprobs

    @top_logprobs.setter
    def top_logprobs(self, top_logprobs):
        """Sets the top_logprobs of this BatchChatCompletionsRequest.


        :param top_logprobs: The top_logprobs of this BatchChatCompletionsRequest.  # noqa: E501
        :type: int
        """

        self._top_logprobs = top_logprobs

    @property
    def top_p(self):
        """Gets the top_p of this BatchChatCompletionsRequest.  # noqa: E501


        :return: The top_p of this BatchChatCompletionsRequest.  # noqa: E501
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        """Sets the top_p of this BatchChatCompletionsRequest.


        :param top_p: The top_p of this BatchChatCompletionsRequest.  # noqa: E501
        :type: float
        """

        self._top_p = top_p

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
        if issubclass(BatchChatCompletionsRequest, dict):
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
        if not isinstance(other, BatchChatCompletionsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchChatCompletionsRequest):
            return True

        return self.to_dict() != other.to_dict()
