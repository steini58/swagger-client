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


class Transfer(object):
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
        'iban': 'str',
        'bic': 'str',
        'name': 'str',
        'amount': 'Amount',
        'purpose': 'str',
        'tan_media_id': 'str',
        'tan_scheme': 'str'
    }

    attribute_map = {
        'iban': 'iban',
        'bic': 'bic',
        'name': 'name',
        'amount': 'amount',
        'purpose': 'purpose',
        'tan_media_id': 'tanMediaId',
        'tan_scheme': 'tanScheme'
    }

    def __init__(self, iban=None, bic=None, name=None, amount=None, purpose=None, tan_media_id=None, tan_scheme=None):  # noqa: E501
        """Transfer - a model defined in Swagger"""  # noqa: E501

        self._iban = None
        self._bic = None
        self._name = None
        self._amount = None
        self._purpose = None
        self._tan_media_id = None
        self._tan_scheme = None
        self.discriminator = None

        self.iban = iban
        if bic is not None:
            self.bic = bic
        self.name = name
        self.amount = amount
        if purpose is not None:
            self.purpose = purpose
        self.tan_media_id = tan_media_id
        self.tan_scheme = tan_scheme

    @property
    def iban(self):
        """Gets the iban of this Transfer.  # noqa: E501

        IBAN - International Bank Account Number (defined in ISO 13616-1)  # noqa: E501

        :return: The iban of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this Transfer.

        IBAN - International Bank Account Number (defined in ISO 13616-1)  # noqa: E501

        :param iban: The iban of this Transfer.  # noqa: E501
        :type: str
        """
        if iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501
        if iban is not None and len(iban) > 34:
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `34`")  # noqa: E501
        if iban is not None and len(iban) < 15:
            raise ValueError("Invalid value for `iban`, length must be greater than or equal to `15`")  # noqa: E501

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this Transfer.  # noqa: E501

        BIC - Business Identifier Code (defined in ISO-9362)  # noqa: E501

        :return: The bic of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this Transfer.

        BIC - Business Identifier Code (defined in ISO-9362)  # noqa: E501

        :param bic: The bic of this Transfer.  # noqa: E501
        :type: str
        """
        if bic is not None and len(bic) > 11:
            raise ValueError("Invalid value for `bic`, length must be less than or equal to `11`")  # noqa: E501
        if bic is not None and len(bic) < 8:
            raise ValueError("Invalid value for `bic`, length must be greater than or equal to `8`")  # noqa: E501

        self._bic = bic

    @property
    def name(self):
        """Gets the name of this Transfer.  # noqa: E501

        Name - Name of the creditor  # noqa: E501

        :return: The name of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Transfer.

        Name - Name of the creditor  # noqa: E501

        :param name: The name of this Transfer.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 70:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `70`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def amount(self):
        """Gets the amount of this Transfer.  # noqa: E501

        Amount to be transfered  # noqa: E501

        :return: The amount of this Transfer.  # noqa: E501
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transfer.

        Amount to be transfered  # noqa: E501

        :param amount: The amount of this Transfer.  # noqa: E501
        :type: Amount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def purpose(self):
        """Gets the purpose of this Transfer.  # noqa: E501

        Purpose  # noqa: E501

        :return: The purpose of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this Transfer.

        Purpose  # noqa: E501

        :param purpose: The purpose of this Transfer.  # noqa: E501
        :type: str
        """
        if purpose is not None and len(purpose) > 140:
            raise ValueError("Invalid value for `purpose`, length must be less than or equal to `140`")  # noqa: E501

        self._purpose = purpose

    @property
    def tan_media_id(self):
        """Gets the tan_media_id of this Transfer.  # noqa: E501

        TANMediaId - The identifying ID of the TANMedia.  # noqa: E501

        :return: The tan_media_id of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._tan_media_id

    @tan_media_id.setter
    def tan_media_id(self, tan_media_id):
        """Sets the tan_media_id of this Transfer.

        TANMediaId - The identifying ID of the TANMedia.  # noqa: E501

        :param tan_media_id: The tan_media_id of this Transfer.  # noqa: E501
        :type: str
        """
        if tan_media_id is None:
            raise ValueError("Invalid value for `tan_media_id`, must not be `None`")  # noqa: E501
        if tan_media_id is not None and len(tan_media_id) > 255:
            raise ValueError("Invalid value for `tan_media_id`, length must be less than or equal to `255`")  # noqa: E501

        self._tan_media_id = tan_media_id

    @property
    def tan_scheme(self):
        """Gets the tan_scheme of this Transfer.  # noqa: E501

        TANScheme - The scheme **id** that is used to verify this payment (e.g. \"901\")  # noqa: E501

        :return: The tan_scheme of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._tan_scheme

    @tan_scheme.setter
    def tan_scheme(self, tan_scheme):
        """Sets the tan_scheme of this Transfer.

        TANScheme - The scheme **id** that is used to verify this payment (e.g. \"901\")  # noqa: E501

        :param tan_scheme: The tan_scheme of this Transfer.  # noqa: E501
        :type: str
        """
        if tan_scheme is None:
            raise ValueError("Invalid value for `tan_scheme`, must not be `None`")  # noqa: E501
        if tan_scheme is not None and len(tan_scheme) > 255:
            raise ValueError("Invalid value for `tan_scheme`, length must be less than or equal to `255`")  # noqa: E501

        self._tan_scheme = tan_scheme

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
        if not isinstance(other, Transfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
