# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.tan_media import TanMedia  # noqa: F401,E501


class TanScheme(object):
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
        'scheme_id': 'str',
        'name': 'str',
        'tan_media_list': 'list[TanMedia]'
    }

    attribute_map = {
        'scheme_id': 'schemeId',
        'name': 'name',
        'tan_media_list': 'tanMediaList'
    }

    def __init__(self, scheme_id=None, name=None, tan_media_list=None):  # noqa: E501
        """TanScheme - a model defined in Swagger"""  # noqa: E501

        self._scheme_id = None
        self._name = None
        self._tan_media_list = None
        self.discriminator = None

        if scheme_id is not None:
            self.scheme_id = scheme_id
        if name is not None:
            self.name = name
        if tan_media_list is not None:
            self.tan_media_list = tan_media_list

    @property
    def scheme_id(self):
        """Gets the scheme_id of this TanScheme.  # noqa: E501

        Internal ID of this TAN scheme (generated value)  # noqa: E501

        :return: The scheme_id of this TanScheme.  # noqa: E501
        :rtype: str
        """
        return self._scheme_id

    @scheme_id.setter
    def scheme_id(self, scheme_id):
        """Sets the scheme_id of this TanScheme.

        Internal ID of this TAN scheme (generated value)  # noqa: E501

        :param scheme_id: The scheme_id of this TanScheme.  # noqa: E501
        :type: str
        """

        self._scheme_id = scheme_id

    @property
    def name(self):
        """Gets the name of this TanScheme.  # noqa: E501

        Name of the used TAN scheme  # noqa: E501

        :return: The name of this TanScheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TanScheme.

        Name of the used TAN scheme  # noqa: E501

        :param name: The name of this TanScheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tan_media_list(self):
        """Gets the tan_media_list of this TanScheme.  # noqa: E501

        List of available TAN media for this scheme  # noqa: E501

        :return: The tan_media_list of this TanScheme.  # noqa: E501
        :rtype: list[TanMedia]
        """
        return self._tan_media_list

    @tan_media_list.setter
    def tan_media_list(self, tan_media_list):
        """Sets the tan_media_list of this TanScheme.

        List of available TAN media for this scheme  # noqa: E501

        :param tan_media_list: The tan_media_list of this TanScheme.  # noqa: E501
        :type: list[TanMedia]
        """

        self._tan_media_list = tan_media_list

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
        if not isinstance(other, TanScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other