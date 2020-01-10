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


class Event(object):
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
        'status': 'str',
        'event_type': 'str',
        'delivered': 'bool',
        'delivered_on': 'datetime',
        'callback_status_code': 'int',
        'timestamp': 'datetime',
        'team': 'DocumentTeam',
        'document': 'Document',
        'signer': 'Signer'
    }

    attribute_map = {
        'uuid': 'uuid',
        'status': 'status',
        'event_type': 'event_type',
        'delivered': 'delivered',
        'delivered_on': 'delivered_on',
        'callback_status_code': 'callback_status_code',
        'timestamp': 'timestamp',
        'team': 'team',
        'document': 'document',
        'signer': 'signer'
    }

    def __init__(self, uuid=None, status=None, event_type=None, delivered=None, delivered_on=None, callback_status_code=None, timestamp=None, team=None, document=None, signer=None):  # noqa: E501
        """Event - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._status = None
        self._event_type = None
        self._delivered = None
        self._delivered_on = None
        self._callback_status_code = None
        self._timestamp = None
        self._team = None
        self._document = None
        self._signer = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if status is not None:
            self.status = status
        if event_type is not None:
            self.event_type = event_type
        if delivered is not None:
            self.delivered = delivered
        if delivered_on is not None:
            self.delivered_on = delivered_on
        if callback_status_code is not None:
            self.callback_status_code = callback_status_code
        if timestamp is not None:
            self.timestamp = timestamp
        if team is not None:
            self.team = team
        if document is not None:
            self.document = document
        if signer is not None:
            self.signer = signer

    @property
    def uuid(self):
        """Gets the uuid of this Event.  # noqa: E501


        :return: The uuid of this Event.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Event.


        :param uuid: The uuid of this Event.  # noqa: E501
        :type: str
        """
        if uuid is not None and len(uuid) < 1:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uuid = uuid

    @property
    def status(self):
        """Gets the status of this Event.  # noqa: E501


        :return: The status of this Event.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Event.


        :param status: The status of this Event.  # noqa: E501
        :type: str
        """
        allowed_values = ["ok", "error"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def event_type(self):
        """Gets the event_type of this Event.  # noqa: E501


        :return: The event_type of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.


        :param event_type: The event_type of this Event.  # noqa: E501
        :type: str
        """
        allowed_values = ["convert_error", "converted", "sending_error", "sent", "declined", "cancelled", "expired", "signed", "viewed", "downloaded", "signer_signed", "signer_email_bounced", "signer_viewed_email", "signer_viewed", "signer_forwarded", "signer_downloaded", "signrequest_received"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def delivered(self):
        """Gets the delivered of this Event.  # noqa: E501


        :return: The delivered of this Event.  # noqa: E501
        :rtype: bool
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this Event.


        :param delivered: The delivered of this Event.  # noqa: E501
        :type: bool
        """

        self._delivered = delivered

    @property
    def delivered_on(self):
        """Gets the delivered_on of this Event.  # noqa: E501


        :return: The delivered_on of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._delivered_on

    @delivered_on.setter
    def delivered_on(self, delivered_on):
        """Sets the delivered_on of this Event.


        :param delivered_on: The delivered_on of this Event.  # noqa: E501
        :type: datetime
        """

        self._delivered_on = delivered_on

    @property
    def callback_status_code(self):
        """Gets the callback_status_code of this Event.  # noqa: E501


        :return: The callback_status_code of this Event.  # noqa: E501
        :rtype: int
        """
        return self._callback_status_code

    @callback_status_code.setter
    def callback_status_code(self, callback_status_code):
        """Sets the callback_status_code of this Event.


        :param callback_status_code: The callback_status_code of this Event.  # noqa: E501
        :type: int
        """

        self._callback_status_code = callback_status_code

    @property
    def timestamp(self):
        """Gets the timestamp of this Event.  # noqa: E501


        :return: The timestamp of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Event.


        :param timestamp: The timestamp of this Event.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def team(self):
        """Gets the team of this Event.  # noqa: E501


        :return: The team of this Event.  # noqa: E501
        :rtype: DocumentTeam
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Event.


        :param team: The team of this Event.  # noqa: E501
        :type: DocumentTeam
        """

        self._team = team

    @property
    def document(self):
        """Gets the document of this Event.  # noqa: E501


        :return: The document of this Event.  # noqa: E501
        :rtype: Document
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Event.


        :param document: The document of this Event.  # noqa: E501
        :type: Document
        """

        self._document = document

    @property
    def signer(self):
        """Gets the signer of this Event.  # noqa: E501


        :return: The signer of this Event.  # noqa: E501
        :rtype: Signer
        """
        return self._signer

    @signer.setter
    def signer(self, signer):
        """Sets the signer of this Event.


        :param signer: The signer of this Event.  # noqa: E501
        :type: Signer
        """

        self._signer = signer

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
        if issubclass(Event, dict):
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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
