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


class InlineIntegrationData(object):
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
        'integration': 'str',
        'integration_data': 'str'
    }

    attribute_map = {
        'integration': 'integration',
        'integration_data': 'integration_data'
    }

    def __init__(self, integration=None, integration_data=None):  # noqa: E501
        """InlineIntegrationData - a model defined in Swagger"""  # noqa: E501

        self._integration = None
        self._integration_data = None
        self.discriminator = None

        if integration is not None:
            self.integration = integration
        if integration_data is not None:
            self.integration_data = integration_data

    @property
    def integration(self):
        """Gets the integration of this InlineIntegrationData.  # noqa: E501


        :return: The integration of this InlineIntegrationData.  # noqa: E501
        :rtype: str
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this InlineIntegrationData.


        :param integration: The integration of this InlineIntegrationData.  # noqa: E501
        :type: str
        """
        allowed_values = ["mfiles", "salesforce", "formdesk", "zapier", "txhash"]  # noqa: E501
        if integration not in allowed_values:
            raise ValueError(
                "Invalid value for `integration` ({0}), must be one of {1}"  # noqa: E501
                .format(integration, allowed_values)
            )

        self._integration = integration

    @property
    def integration_data(self):
        """Gets the integration_data of this InlineIntegrationData.  # noqa: E501


        :return: The integration_data of this InlineIntegrationData.  # noqa: E501
        :rtype: str
        """
        return self._integration_data

    @integration_data.setter
    def integration_data(self, integration_data):
        """Sets the integration_data of this InlineIntegrationData.


        :param integration_data: The integration_data of this InlineIntegrationData.  # noqa: E501
        :type: str
        """

        self._integration_data = integration_data

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
        if issubclass(InlineIntegrationData, dict):
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
        if not isinstance(other, InlineIntegrationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
