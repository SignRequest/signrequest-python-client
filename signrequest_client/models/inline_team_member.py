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


class InlineTeamMember(object):
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
        'uuid': 'str',
        'url': 'str',
        'user': 'User',
        'is_admin': 'bool',
        'is_active': 'bool',
        'is_owner': 'bool'
    }

    attribute_map = {
        'uuid': 'uuid',
        'url': 'url',
        'user': 'user',
        'is_admin': 'is_admin',
        'is_active': 'is_active',
        'is_owner': 'is_owner'
    }

    def __init__(self, uuid=None, url=None, user=None, is_admin=None, is_active=None, is_owner=None):  # noqa: E501
        """InlineTeamMember - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._url = None
        self._user = None
        self._is_admin = None
        self._is_active = None
        self._is_owner = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if url is not None:
            self.url = url
        if user is not None:
            self.user = user
        if is_admin is not None:
            self.is_admin = is_admin
        if is_active is not None:
            self.is_active = is_active
        if is_owner is not None:
            self.is_owner = is_owner

    @property
    def uuid(self):
        """Gets the uuid of this InlineTeamMember.  # noqa: E501


        :return: The uuid of this InlineTeamMember.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineTeamMember.


        :param uuid: The uuid of this InlineTeamMember.  # noqa: E501
        :type: str
        """
        if uuid is not None and len(uuid) < 1:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uuid = uuid

    @property
    def url(self):
        """Gets the url of this InlineTeamMember.  # noqa: E501


        :return: The url of this InlineTeamMember.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineTeamMember.


        :param url: The url of this InlineTeamMember.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def user(self):
        """Gets the user of this InlineTeamMember.  # noqa: E501


        :return: The user of this InlineTeamMember.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InlineTeamMember.


        :param user: The user of this InlineTeamMember.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def is_admin(self):
        """Gets the is_admin of this InlineTeamMember.  # noqa: E501


        :return: The is_admin of this InlineTeamMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this InlineTeamMember.


        :param is_admin: The is_admin of this InlineTeamMember.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_active(self):
        """Gets the is_active of this InlineTeamMember.  # noqa: E501


        :return: The is_active of this InlineTeamMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this InlineTeamMember.


        :param is_active: The is_active of this InlineTeamMember.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_owner(self):
        """Gets the is_owner of this InlineTeamMember.  # noqa: E501


        :return: The is_owner of this InlineTeamMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_owner

    @is_owner.setter
    def is_owner(self, is_owner):
        """Sets the is_owner of this InlineTeamMember.


        :param is_owner: The is_owner of this InlineTeamMember.  # noqa: E501
        :type: bool
        """

        self._is_owner = is_owner

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
        if issubclass(InlineTeamMember, dict):
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
        if not isinstance(other, InlineTeamMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
