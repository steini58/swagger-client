# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.additional_information import AdditionalInformation  # noqa: F401,E501


class Contractor(object):
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
        'contractor_id': 'int'
    }

    attribute_map = {
        'contractor_id': 'contractorId'
    }

    def __init__(self, contractor_id=None):  # noqa: E501
        """Contractor - a model defined in Swagger"""  # noqa: E501

        self._contractor_id = None
        self.discriminator = None

        if contractor_id is not None:
            self.contractor_id = contractor_id

    @property
    def contractor_id(self):
        """Gets the contractor_id of this Contractor.  # noqa: E501


        :return: The contractor_id of this Contractor.  # noqa: E501
        :rtype: int
        """
        return self._contractor_id

    @contractor_id.setter
    def contractor_id(self, contractor_id):
        """Sets the contractor_id of this Contractor.


        :param contractor_id: The contractor_id of this Contractor.  # noqa: E501
        :type: int
        """

        self._contractor_id = contractor_id

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
        if not isinstance(other, Contractor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other