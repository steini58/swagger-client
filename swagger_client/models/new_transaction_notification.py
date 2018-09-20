# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.amount import Amount  # noqa: F401,E501
from swagger_client.models.notification import Notification  # noqa: F401,E501


class NewTransactionNotification(object):
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
        'account_id': 'str',
        'lower_threshold': 'Amount',
        'upper_threshold': 'Amount',
        'search_keyword': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'lower_threshold': 'lowerThreshold',
        'upper_threshold': 'upperThreshold',
        'search_keyword': 'searchKeyword'
    }

    def __init__(self, account_id=None, lower_threshold=None, upper_threshold=None, search_keyword=None):  # noqa: E501
        """NewTransactionNotification - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._lower_threshold = None
        self._upper_threshold = None
        self._search_keyword = None
        self.discriminator = None

        self.account_id = account_id
        if lower_threshold is not None:
            self.lower_threshold = lower_threshold
        if upper_threshold is not None:
            self.upper_threshold = upper_threshold
        if search_keyword is not None:
            self.search_keyword = search_keyword

    @property
    def account_id(self):
        """Gets the account_id of this NewTransactionNotification.  # noqa: E501

        Identifier of the account to which this notification belongs  # noqa: E501

        :return: The account_id of this NewTransactionNotification.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewTransactionNotification.

        Identifier of the account to which this notification belongs  # noqa: E501

        :param account_id: The account_id of this NewTransactionNotification.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def lower_threshold(self):
        """Gets the lower_threshold of this NewTransactionNotification.  # noqa: E501

        Optional limitation; lower threshold of the amount (negative values allowed) above which notifications will be sent  # noqa: E501

        :return: The lower_threshold of this NewTransactionNotification.  # noqa: E501
        :rtype: Amount
        """
        return self._lower_threshold

    @lower_threshold.setter
    def lower_threshold(self, lower_threshold):
        """Sets the lower_threshold of this NewTransactionNotification.

        Optional limitation; lower threshold of the amount (negative values allowed) above which notifications will be sent  # noqa: E501

        :param lower_threshold: The lower_threshold of this NewTransactionNotification.  # noqa: E501
        :type: Amount
        """

        self._lower_threshold = lower_threshold

    @property
    def upper_threshold(self):
        """Gets the upper_threshold of this NewTransactionNotification.  # noqa: E501

        Optional limitation; upper threshold of the amount (negative values allowed) below which notifications will be sent  # noqa: E501

        :return: The upper_threshold of this NewTransactionNotification.  # noqa: E501
        :rtype: Amount
        """
        return self._upper_threshold

    @upper_threshold.setter
    def upper_threshold(self, upper_threshold):
        """Sets the upper_threshold of this NewTransactionNotification.

        Optional limitation; upper threshold of the amount (negative values allowed) below which notifications will be sent  # noqa: E501

        :param upper_threshold: The upper_threshold of this NewTransactionNotification.  # noqa: E501
        :type: Amount
        """

        self._upper_threshold = upper_threshold

    @property
    def search_keyword(self):
        """Gets the search_keyword of this NewTransactionNotification.  # noqa: E501

        Optional limitation on transactions for given keywords (e.g., owner \"Hans Muster\" or purpose \"Salary\")  # noqa: E501

        :return: The search_keyword of this NewTransactionNotification.  # noqa: E501
        :rtype: str
        """
        return self._search_keyword

    @search_keyword.setter
    def search_keyword(self, search_keyword):
        """Sets the search_keyword of this NewTransactionNotification.

        Optional limitation on transactions for given keywords (e.g., owner \"Hans Muster\" or purpose \"Salary\")  # noqa: E501

        :param search_keyword: The search_keyword of this NewTransactionNotification.  # noqa: E501
        :type: str
        """
        if search_keyword is not None and len(search_keyword) > 255:
            raise ValueError("Invalid value for `search_keyword`, length must be less than or equal to `255`")  # noqa: E501

        self._search_keyword = search_keyword

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewTransactionNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
