# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Notification(object):
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
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'BalanceChangeNotification': 'BalanceChangeNotification',
        'BudgetNotification': 'BudgetNotification',
        'NewTransactionNotification': 'NewTransactionNotification',
        'DailySummaryNotification': 'DailySummaryNotification'
    }

    def __init__(self, id=None, type=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self.discriminator = 'type'

        if id is not None:
            self.id = id
        self.type = type

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501

        Internal ID of this notification (generated value)  # noqa: E501

        :return: The id of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.

        Internal ID of this notification (generated value)  # noqa: E501

        :param id: The id of this Notification.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Notification.  # noqa: E501

        Discriminator for subtypes. At the moment `BalanceChangeNotification`, `BudgetNotification`, `DailySummaryNotification` and `NewTransactionNotification` are supported.  # noqa: E501

        :return: The type of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Notification.

        Discriminator for subtypes. At the moment `BalanceChangeNotification`, `BudgetNotification`, `DailySummaryNotification` and `NewTransactionNotification` are supported.  # noqa: E501

        :param type: The type of this Notification.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
