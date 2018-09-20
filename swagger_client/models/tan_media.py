# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TanMedia(object):
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
        'tan_media_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'tan_media_id': 'tanMediaId',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, tan_media_id=None, name=None, description=None):  # noqa: E501
        """TanMedia - a model defined in Swagger"""  # noqa: E501

        self._tan_media_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.tan_media_id = tan_media_id
        self.name = name
        self.description = description

    @property
    def tan_media_id(self):
        """Gets the tan_media_id of this TanMedia.  # noqa: E501

        ID of this TAN media  # noqa: E501

        :return: The tan_media_id of this TanMedia.  # noqa: E501
        :rtype: str
        """
        return self._tan_media_id

    @tan_media_id.setter
    def tan_media_id(self, tan_media_id):
        """Sets the tan_media_id of this TanMedia.

        ID of this TAN media  # noqa: E501

        :param tan_media_id: The tan_media_id of this TanMedia.  # noqa: E501
        :type: str
        """
        if tan_media_id is None:
            raise ValueError("Invalid value for `tan_media_id`, must not be `None`")  # noqa: E501

        self._tan_media_id = tan_media_id

    @property
    def name(self):
        """Gets the name of this TanMedia.  # noqa: E501

        Name of TANMedia (e.g., \"iTan\")  # noqa: E501

        :return: The name of this TanMedia.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TanMedia.

        Name of TANMedia (e.g., \"iTan\")  # noqa: E501

        :param name: The name of this TanMedia.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TanMedia.  # noqa: E501

        Description of TANMedia (e.g., phone number or card number used for given type)  # noqa: E501

        :return: The description of this TanMedia.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TanMedia.

        Description of TANMedia (e.g., phone number or card number used for given type)  # noqa: E501

        :param description: The description of this TanMedia.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, TanMedia):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
