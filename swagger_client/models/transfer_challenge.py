# coding: utf-8

"""
    

    [AHOI cookbook](/ahoi/docs/cookbook/index.html)  [Data Privacy](/sandboxmanager/#/privacy)  [Terms of Service](/sandboxmanager/#/terms)  [Imprint](https://sparkassen-hub.com/impressum/)  &copy; 2016&dash;2017 Starfinanz - Ein Unternehmen der Finanz Informatik  # noqa: E501

    OpenAPI spec version: 2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.input_field_description import InputFieldDescription  # noqa: F401,E501
from swagger_client.models.response_object_map import ResponseObjectMap  # noqa: F401,E501


class TransferChallenge(object):
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
        'transfer_task_id': 'str',
        'field_descriptions': 'list[InputFieldDescription]',
        'challenge': 'str',
        'response_objects': 'ResponseObjectMap'
    }

    attribute_map = {
        'transfer_task_id': 'transferTaskId',
        'field_descriptions': 'fieldDescriptions',
        'challenge': 'challenge',
        'response_objects': 'responseObjects'
    }

    def __init__(self, transfer_task_id=None, field_descriptions=None, challenge=None, response_objects=None):  # noqa: E501
        """TransferChallenge - a model defined in Swagger"""  # noqa: E501

        self._transfer_task_id = None
        self._field_descriptions = None
        self._challenge = None
        self._response_objects = None
        self.discriminator = None

        if transfer_task_id is not None:
            self.transfer_task_id = transfer_task_id
        if field_descriptions is not None:
            self.field_descriptions = field_descriptions
        self.challenge = challenge
        self.response_objects = response_objects

    @property
    def transfer_task_id(self):
        """Gets the transfer_task_id of this TransferChallenge.  # noqa: E501

        TranferTaskID - The referenced task for that payment — challenge  # noqa: E501

        :return: The transfer_task_id of this TransferChallenge.  # noqa: E501
        :rtype: str
        """
        return self._transfer_task_id

    @transfer_task_id.setter
    def transfer_task_id(self, transfer_task_id):
        """Sets the transfer_task_id of this TransferChallenge.

        TranferTaskID - The referenced task for that payment — challenge  # noqa: E501

        :param transfer_task_id: The transfer_task_id of this TransferChallenge.  # noqa: E501
        :type: str
        """

        self._transfer_task_id = transfer_task_id

    @property
    def field_descriptions(self):
        """Gets the field_descriptions of this TransferChallenge.  # noqa: E501

        Information to describe and facilitate validation of an transfer.  # noqa: E501

        :return: The field_descriptions of this TransferChallenge.  # noqa: E501
        :rtype: list[InputFieldDescription]
        """
        return self._field_descriptions

    @field_descriptions.setter
    def field_descriptions(self, field_descriptions):
        """Sets the field_descriptions of this TransferChallenge.

        Information to describe and facilitate validation of an transfer.  # noqa: E501

        :param field_descriptions: The field_descriptions of this TransferChallenge.  # noqa: E501
        :type: list[InputFieldDescription]
        """

        self._field_descriptions = field_descriptions

    @property
    def challenge(self):
        """Gets the challenge of this TransferChallenge.  # noqa: E501

        Challenge — challenge text  # noqa: E501

        :return: The challenge of this TransferChallenge.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this TransferChallenge.

        Challenge — challenge text  # noqa: E501

        :param challenge: The challenge of this TransferChallenge.  # noqa: E501
        :type: str
        """
        if challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def response_objects(self):
        """Gets the response_objects of this TransferChallenge.  # noqa: E501

        FieldSet — The required InputFields for that challenge  # noqa: E501

        :return: The response_objects of this TransferChallenge.  # noqa: E501
        :rtype: ResponseObjectMap
        """
        return self._response_objects

    @response_objects.setter
    def response_objects(self, response_objects):
        """Sets the response_objects of this TransferChallenge.

        FieldSet — The required InputFields for that challenge  # noqa: E501

        :param response_objects: The response_objects of this TransferChallenge.  # noqa: E501
        :type: ResponseObjectMap
        """
        if response_objects is None:
            raise ValueError("Invalid value for `response_objects`, must not be `None`")  # noqa: E501

        self._response_objects = response_objects

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
        if not isinstance(other, TransferChallenge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other