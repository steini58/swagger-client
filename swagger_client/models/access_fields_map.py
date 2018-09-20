# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AccessFieldsMap(object):
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
        'username': 'str',
        'customernumber': 'str',
        'pin': 'str'
    }

    attribute_map = {
        'username': 'USERNAME',
        'customernumber': 'CUSTOMERNUMBER',
        'pin': 'PIN'
    }

    def __init__(self, username=None, customernumber=None, pin=None):  # noqa: E501
        """AccessFieldsMap - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._customernumber = None
        self._pin = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if customernumber is not None:
            self.customernumber = customernumber
        if pin is not None:
            self.pin = pin

    @property
    def username(self):
        """Gets the username of this AccessFieldsMap.  # noqa: E501

        Should be filled with the username if the Provider object signals this as mandatory.  # noqa: E501

        :return: The username of this AccessFieldsMap.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AccessFieldsMap.

        Should be filled with the username if the Provider object signals this as mandatory.  # noqa: E501

        :param username: The username of this AccessFieldsMap.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def customernumber(self):
        """Gets the customernumber of this AccessFieldsMap.  # noqa: E501

        Should be filled with the customer number if the Provider object signals this as mandatory.  # noqa: E501

        :return: The customernumber of this AccessFieldsMap.  # noqa: E501
        :rtype: str
        """
        return self._customernumber

    @customernumber.setter
    def customernumber(self, customernumber):
        """Sets the customernumber of this AccessFieldsMap.

        Should be filled with the customer number if the Provider object signals this as mandatory.  # noqa: E501

        :param customernumber: The customernumber of this AccessFieldsMap.  # noqa: E501
        :type: str
        """

        self._customernumber = customernumber

    @property
    def pin(self):
        """Gets the pin of this AccessFieldsMap.  # noqa: E501

        Should be filled with the PIN if the Provider object signals this as mandatory.  # noqa: E501

        :return: The pin of this AccessFieldsMap.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this AccessFieldsMap.

        Should be filled with the PIN if the Provider object signals this as mandatory.  # noqa: E501

        :param pin: The pin of this AccessFieldsMap.  # noqa: E501
        :type: str
        """

        self._pin = pin

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
        if not isinstance(other, AccessFieldsMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other