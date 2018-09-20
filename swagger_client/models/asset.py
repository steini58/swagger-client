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


class Asset(object):
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
        'id': 'str',
        'wkn': 'str',
        'isin': 'str',
        'name': 'str',
        'price_type': 'str',
        'value': 'str',
        'amount': 'Amount',
        'amount_alt_curr': 'Amount'
    }

    attribute_map = {
        'id': 'id',
        'wkn': 'wkn',
        'isin': 'isin',
        'name': 'name',
        'price_type': 'priceType',
        'value': 'value',
        'amount': 'amount',
        'amount_alt_curr': 'amountAltCurr'
    }

    def __init__(self, id=None, wkn=None, isin=None, name=None, price_type=None, value=None, amount=None, amount_alt_curr=None):  # noqa: E501
        """Asset - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._wkn = None
        self._isin = None
        self._name = None
        self._price_type = None
        self._value = None
        self._amount = None
        self._amount_alt_curr = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if wkn is not None:
            self.wkn = wkn
        if isin is not None:
            self.isin = isin
        if name is not None:
            self.name = name
        if price_type is not None:
            self.price_type = price_type
        if value is not None:
            self.value = value
        if amount is not None:
            self.amount = amount
        if amount_alt_curr is not None:
            self.amount_alt_curr = amount_alt_curr

    @property
    def id(self):
        """Gets the id of this Asset.  # noqa: E501


        :return: The id of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Asset.


        :param id: The id of this Asset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wkn(self):
        """Gets the wkn of this Asset.  # noqa: E501


        :return: The wkn of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn):
        """Sets the wkn of this Asset.


        :param wkn: The wkn of this Asset.  # noqa: E501
        :type: str
        """

        self._wkn = wkn

    @property
    def isin(self):
        """Gets the isin of this Asset.  # noqa: E501


        :return: The isin of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this Asset.


        :param isin: The isin of this Asset.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def name(self):
        """Gets the name of this Asset.  # noqa: E501


        :return: The name of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Asset.


        :param name: The name of this Asset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def price_type(self):
        """Gets the price_type of this Asset.  # noqa: E501


        :return: The price_type of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this Asset.


        :param price_type: The price_type of this Asset.  # noqa: E501
        :type: str
        """
        allowed_values = ["MRKT", "INDC"]  # noqa: E501
        if price_type not in allowed_values:
            raise ValueError(
                "Invalid value for `price_type` ({0}), must be one of {1}"  # noqa: E501
                .format(price_type, allowed_values)
            )

        self._price_type = price_type

    @property
    def value(self):
        """Gets the value of this Asset.  # noqa: E501


        :return: The value of this Asset.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Asset.


        :param value: The value of this Asset.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def amount(self):
        """Gets the amount of this Asset.  # noqa: E501


        :return: The amount of this Asset.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Asset.


        :param amount: The amount of this Asset.  # noqa: E501
        :type: Amount
        """

        self._amount = amount

    @property
    def amount_alt_curr(self):
        """Gets the amount_alt_curr of this Asset.  # noqa: E501


        :return: The amount_alt_curr of this Asset.  # noqa: E501
        :rtype: Amount
        """
        return self._amount_alt_curr

    @amount_alt_curr.setter
    def amount_alt_curr(self, amount_alt_curr):
        """Sets the amount_alt_curr of this Asset.


        :param amount_alt_curr: The amount_alt_curr of this Asset.  # noqa: E501
        :type: Amount
        """

        self._amount_alt_curr = amount_alt_curr

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
        if not isinstance(other, Asset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other