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


class InlineTeam(object):
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
        'name': 'str',
        'subdomain': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'subdomain': 'subdomain',
        'url': 'url'
    }

    def __init__(self, name=None, subdomain=None, url=None):  # noqa: E501
        """InlineTeam - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._subdomain = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if subdomain is not None:
            self.subdomain = subdomain
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this InlineTeam.  # noqa: E501


        :return: The name of this InlineTeam.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineTeam.


        :param name: The name of this InlineTeam.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def subdomain(self):
        """Gets the subdomain of this InlineTeam.  # noqa: E501


        :return: The subdomain of this InlineTeam.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this InlineTeam.


        :param subdomain: The subdomain of this InlineTeam.  # noqa: E501
        :type: str
        """
        if subdomain is not None and len(subdomain) < 1:
            raise ValueError("Invalid value for `subdomain`, length must be greater than or equal to `1`")  # noqa: E501
        if subdomain is not None and not re.search('^[-a-zA-Z0-9_]+$', subdomain):  # noqa: E501
            raise ValueError("Invalid value for `subdomain`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._subdomain = subdomain

    @property
    def url(self):
        """Gets the url of this InlineTeam.  # noqa: E501


        :return: The url of this InlineTeam.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineTeam.


        :param url: The url of this InlineTeam.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, InlineTeam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other