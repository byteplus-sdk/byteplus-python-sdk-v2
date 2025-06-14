# coding: utf-8

"""
    billing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from byteplussdkcore.configuration import Configuration


class OrderProductInfoForListOrderProductDetailsOutput(object):
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
        'begin_time': 'str',
        'configuration_code': 'str',
        'coupon_amount': 'str',
        'discount_amount': 'str',
        'end_time': 'str',
        'instance_id': 'str',
        'order_fail_refund_info': 'OrderFailRefundInfoForListOrderProductDetailsOutput',
        'original_amount': 'str',
        'paid_amount': 'str',
        'payable_amount': 'str',
        'payer_customer_name': 'str',
        'payer_id': 'int',
        'payment_method': 'str',
        'period': 'str',
        'product': 'str',
        'status': 'str',
        'times': 'str'
    }

    attribute_map = {
        'begin_time': 'BeginTime',
        'configuration_code': 'ConfigurationCode',
        'coupon_amount': 'CouponAmount',
        'discount_amount': 'DiscountAmount',
        'end_time': 'EndTime',
        'instance_id': 'InstanceID',
        'order_fail_refund_info': 'OrderFailRefundInfo',
        'original_amount': 'OriginalAmount',
        'paid_amount': 'PaidAmount',
        'payable_amount': 'PayableAmount',
        'payer_customer_name': 'PayerCustomerName',
        'payer_id': 'PayerID',
        'payment_method': 'PaymentMethod',
        'period': 'Period',
        'product': 'Product',
        'status': 'Status',
        'times': 'Times'
    }

    def __init__(self, begin_time=None, configuration_code=None, coupon_amount=None, discount_amount=None, end_time=None, instance_id=None, order_fail_refund_info=None, original_amount=None, paid_amount=None, payable_amount=None, payer_customer_name=None, payer_id=None, payment_method=None, period=None, product=None, status=None, times=None, _configuration=None):  # noqa: E501
        """OrderProductInfoForListOrderProductDetailsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._begin_time = None
        self._configuration_code = None
        self._coupon_amount = None
        self._discount_amount = None
        self._end_time = None
        self._instance_id = None
        self._order_fail_refund_info = None
        self._original_amount = None
        self._paid_amount = None
        self._payable_amount = None
        self._payer_customer_name = None
        self._payer_id = None
        self._payment_method = None
        self._period = None
        self._product = None
        self._status = None
        self._times = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if configuration_code is not None:
            self.configuration_code = configuration_code
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if end_time is not None:
            self.end_time = end_time
        if instance_id is not None:
            self.instance_id = instance_id
        if order_fail_refund_info is not None:
            self.order_fail_refund_info = order_fail_refund_info
        if original_amount is not None:
            self.original_amount = original_amount
        if paid_amount is not None:
            self.paid_amount = paid_amount
        if payable_amount is not None:
            self.payable_amount = payable_amount
        if payer_customer_name is not None:
            self.payer_customer_name = payer_customer_name
        if payer_id is not None:
            self.payer_id = payer_id
        if payment_method is not None:
            self.payment_method = payment_method
        if period is not None:
            self.period = period
        if product is not None:
            self.product = product
        if status is not None:
            self.status = status
        if times is not None:
            self.times = times

    @property
    def begin_time(self):
        """Gets the begin_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The begin_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this OrderProductInfoForListOrderProductDetailsOutput.


        :param begin_time: The begin_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._begin_time = begin_time

    @property
    def configuration_code(self):
        """Gets the configuration_code of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The configuration_code of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._configuration_code

    @configuration_code.setter
    def configuration_code(self, configuration_code):
        """Sets the configuration_code of this OrderProductInfoForListOrderProductDetailsOutput.


        :param configuration_code: The configuration_code of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._configuration_code = configuration_code

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The coupon_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this OrderProductInfoForListOrderProductDetailsOutput.


        :param coupon_amount: The coupon_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._coupon_amount = coupon_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The discount_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this OrderProductInfoForListOrderProductDetailsOutput.


        :param discount_amount: The discount_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._discount_amount = discount_amount

    @property
    def end_time(self):
        """Gets the end_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The end_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this OrderProductInfoForListOrderProductDetailsOutput.


        :param end_time: The end_time of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def instance_id(self):
        """Gets the instance_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The instance_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this OrderProductInfoForListOrderProductDetailsOutput.


        :param instance_id: The instance_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def order_fail_refund_info(self):
        """Gets the order_fail_refund_info of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The order_fail_refund_info of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: OrderFailRefundInfoForListOrderProductDetailsOutput
        """
        return self._order_fail_refund_info

    @order_fail_refund_info.setter
    def order_fail_refund_info(self, order_fail_refund_info):
        """Sets the order_fail_refund_info of this OrderProductInfoForListOrderProductDetailsOutput.


        :param order_fail_refund_info: The order_fail_refund_info of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: OrderFailRefundInfoForListOrderProductDetailsOutput
        """

        self._order_fail_refund_info = order_fail_refund_info

    @property
    def original_amount(self):
        """Gets the original_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The original_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        """Sets the original_amount of this OrderProductInfoForListOrderProductDetailsOutput.


        :param original_amount: The original_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._original_amount = original_amount

    @property
    def paid_amount(self):
        """Gets the paid_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The paid_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._paid_amount

    @paid_amount.setter
    def paid_amount(self, paid_amount):
        """Sets the paid_amount of this OrderProductInfoForListOrderProductDetailsOutput.


        :param paid_amount: The paid_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._paid_amount = paid_amount

    @property
    def payable_amount(self):
        """Gets the payable_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The payable_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, payable_amount):
        """Sets the payable_amount of this OrderProductInfoForListOrderProductDetailsOutput.


        :param payable_amount: The payable_amount of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._payable_amount = payable_amount

    @property
    def payer_customer_name(self):
        """Gets the payer_customer_name of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The payer_customer_name of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._payer_customer_name

    @payer_customer_name.setter
    def payer_customer_name(self, payer_customer_name):
        """Sets the payer_customer_name of this OrderProductInfoForListOrderProductDetailsOutput.


        :param payer_customer_name: The payer_customer_name of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._payer_customer_name = payer_customer_name

    @property
    def payer_id(self):
        """Gets the payer_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The payer_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: int
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """Sets the payer_id of this OrderProductInfoForListOrderProductDetailsOutput.


        :param payer_id: The payer_id of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: int
        """

        self._payer_id = payer_id

    @property
    def payment_method(self):
        """Gets the payment_method of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The payment_method of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this OrderProductInfoForListOrderProductDetailsOutput.


        :param payment_method: The payment_method of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._payment_method = payment_method

    @property
    def period(self):
        """Gets the period of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The period of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this OrderProductInfoForListOrderProductDetailsOutput.


        :param period: The period of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._period = period

    @property
    def product(self):
        """Gets the product of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The product of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this OrderProductInfoForListOrderProductDetailsOutput.


        :param product: The product of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def status(self):
        """Gets the status of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The status of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrderProductInfoForListOrderProductDetailsOutput.


        :param status: The status of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def times(self):
        """Gets the times of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501


        :return: The times of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :rtype: str
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this OrderProductInfoForListOrderProductDetailsOutput.


        :param times: The times of this OrderProductInfoForListOrderProductDetailsOutput.  # noqa: E501
        :type: str
        """

        self._times = times

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
        if issubclass(OrderProductInfoForListOrderProductDetailsOutput, dict):
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
        if not isinstance(other, OrderProductInfoForListOrderProductDetailsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrderProductInfoForListOrderProductDetailsOutput):
            return True

        return self.to_dict() != other.to_dict()
