# coding: utf-8

"""
    SignRequest API

    API for SignRequest.com

    OpenAPI spec version: v1
    Contact: tech-support@signrequest.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileFromSf(object):
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
        'object_type': 'str',
        'object_id': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'object_type': 'object_type',
        'object_id': 'object_id',
        'uid': 'uid'
    }

    def __init__(self, object_type=None, object_id=None, uid=None):  # noqa: E501
        """FileFromSf - a model defined in Swagger"""  # noqa: E501

        self._object_type = None
        self._object_id = None
        self._uid = None
        self.discriminator = None

        self.object_type = object_type
        self.object_id = object_id
        if uid is not None:
            self.uid = uid

    @property
    def object_type(self):
        """Gets the object_type of this FileFromSf.  # noqa: E501


        :return: The object_type of this FileFromSf.  # noqa: E501
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this FileFromSf.


        :param object_type: The object_type of this FileFromSf.  # noqa: E501
        :type: str
        """
        if object_type is None:
            raise ValueError("Invalid value for `object_type`, must not be `None`")  # noqa: E501
        if object_type is not None and len(object_type) < 1:
            raise ValueError("Invalid value for `object_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._object_type = object_type

    @property
    def object_id(self):
        """Gets the object_id of this FileFromSf.  # noqa: E501


        :return: The object_id of this FileFromSf.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this FileFromSf.


        :param object_id: The object_id of this FileFromSf.  # noqa: E501
        :type: str
        """
        if object_id is None:
            raise ValueError("Invalid value for `object_id`, must not be `None`")  # noqa: E501
        if object_id is not None and len(object_id) < 1:
            raise ValueError("Invalid value for `object_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._object_id = object_id

    @property
    def uid(self):
        """Gets the uid of this FileFromSf.  # noqa: E501


        :return: The uid of this FileFromSf.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this FileFromSf.


        :param uid: The uid of this FileFromSf.  # noqa: E501
        :type: str
        """
        if uid is not None and len(uid) < 1:
            raise ValueError("Invalid value for `uid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uid = uid

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
        if issubclass(FileFromSf, dict):
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
        if not isinstance(other, FileFromSf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
