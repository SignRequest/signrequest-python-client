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


class DocumentSearch(object):
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
        'created': 'datetime',
        'status': 'str',
        'who': 'str',
        'name': 'str',
        'autocomplete': 'str',
        'from_email': 'str',
        'nr_extra_docs': 'int',
        'signer_emails': 'list[str]',
        'status_display': 'str',
        'created_timestamp': 'int',
        'finished_on_timestamp': 'int',
        'parent_doc': 'str',
        'finished_on': 'datetime',
        'subdomain': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'created': 'created',
        'status': 'status',
        'who': 'who',
        'name': 'name',
        'autocomplete': 'autocomplete',
        'from_email': 'from_email',
        'nr_extra_docs': 'nr_extra_docs',
        'signer_emails': 'signer_emails',
        'status_display': 'status_display',
        'created_timestamp': 'created_timestamp',
        'finished_on_timestamp': 'finished_on_timestamp',
        'parent_doc': 'parent_doc',
        'finished_on': 'finished_on',
        'subdomain': 'subdomain'
    }

    def __init__(self, uuid=None, created=None, status=None, who=None, name=None, autocomplete=None, from_email=None, nr_extra_docs=None, signer_emails=None, status_display=None, created_timestamp=None, finished_on_timestamp=None, parent_doc=None, finished_on=None, subdomain=None):  # noqa: E501
        """DocumentSearch - a model defined in Swagger"""  # noqa: E501

        self._uuid = None
        self._created = None
        self._status = None
        self._who = None
        self._name = None
        self._autocomplete = None
        self._from_email = None
        self._nr_extra_docs = None
        self._signer_emails = None
        self._status_display = None
        self._created_timestamp = None
        self._finished_on_timestamp = None
        self._parent_doc = None
        self._finished_on = None
        self._subdomain = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if created is not None:
            self.created = created
        if status is not None:
            self.status = status
        self.who = who
        if name is not None:
            self.name = name
        self.autocomplete = autocomplete
        self.from_email = from_email
        self.nr_extra_docs = nr_extra_docs
        if signer_emails is not None:
            self.signer_emails = signer_emails
        if status_display is not None:
            self.status_display = status_display
        if created_timestamp is not None:
            self.created_timestamp = created_timestamp
        if finished_on_timestamp is not None:
            self.finished_on_timestamp = finished_on_timestamp
        if parent_doc is not None:
            self.parent_doc = parent_doc
        if finished_on is not None:
            self.finished_on = finished_on
        if subdomain is not None:
            self.subdomain = subdomain

    @property
    def uuid(self):
        """Gets the uuid of this DocumentSearch.  # noqa: E501


        :return: The uuid of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DocumentSearch.


        :param uuid: The uuid of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if uuid is not None and len(uuid) < 1:
            raise ValueError("Invalid value for `uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._uuid = uuid

    @property
    def created(self):
        """Gets the created of this DocumentSearch.  # noqa: E501


        :return: The created of this DocumentSearch.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DocumentSearch.


        :param created: The created of this DocumentSearch.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def status(self):
        """Gets the status of this DocumentSearch.  # noqa: E501

        `co`: converting, `ne`: new, `se`: sent, `vi`: viewed, `si`: signed, `do`: downloaded, `sd`: signed and downloaded, `ca`: cancelled, `de`: declined, `ec`: error converting, `es`: error sending, `xp`: expired  # noqa: E501

        :return: The status of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentSearch.

        `co`: converting, `ne`: new, `se`: sent, `vi`: viewed, `si`: signed, `do`: downloaded, `sd`: signed and downloaded, `ca`: cancelled, `de`: declined, `ec`: error converting, `es`: error sending, `xp`: expired  # noqa: E501

        :param status: The status of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if status is not None and len(status) > 2:
            raise ValueError("Invalid value for `status`, length must be less than or equal to `2`")  # noqa: E501
        if status is not None and len(status) < 1:
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def who(self):
        """Gets the who of this DocumentSearch.  # noqa: E501


        :return: The who of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._who

    @who.setter
    def who(self, who):
        """Sets the who of this DocumentSearch.


        :param who: The who of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if who is None:
            raise ValueError("Invalid value for `who`, must not be `None`")  # noqa: E501
        if who is not None and len(who) < 1:
            raise ValueError("Invalid value for `who`, length must be greater than or equal to `1`")  # noqa: E501

        self._who = who

    @property
    def name(self):
        """Gets the name of this DocumentSearch.  # noqa: E501

        Defaults to filename  # noqa: E501

        :return: The name of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentSearch.

        Defaults to filename  # noqa: E501

        :param name: The name of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def autocomplete(self):
        """Gets the autocomplete of this DocumentSearch.  # noqa: E501


        :return: The autocomplete of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._autocomplete

    @autocomplete.setter
    def autocomplete(self, autocomplete):
        """Sets the autocomplete of this DocumentSearch.


        :param autocomplete: The autocomplete of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if autocomplete is None:
            raise ValueError("Invalid value for `autocomplete`, must not be `None`")  # noqa: E501
        if autocomplete is not None and len(autocomplete) < 1:
            raise ValueError("Invalid value for `autocomplete`, length must be greater than or equal to `1`")  # noqa: E501

        self._autocomplete = autocomplete

    @property
    def from_email(self):
        """Gets the from_email of this DocumentSearch.  # noqa: E501


        :return: The from_email of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this DocumentSearch.


        :param from_email: The from_email of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if from_email is None:
            raise ValueError("Invalid value for `from_email`, must not be `None`")  # noqa: E501
        if from_email is not None and len(from_email) < 1:
            raise ValueError("Invalid value for `from_email`, length must be greater than or equal to `1`")  # noqa: E501

        self._from_email = from_email

    @property
    def nr_extra_docs(self):
        """Gets the nr_extra_docs of this DocumentSearch.  # noqa: E501


        :return: The nr_extra_docs of this DocumentSearch.  # noqa: E501
        :rtype: int
        """
        return self._nr_extra_docs

    @nr_extra_docs.setter
    def nr_extra_docs(self, nr_extra_docs):
        """Sets the nr_extra_docs of this DocumentSearch.


        :param nr_extra_docs: The nr_extra_docs of this DocumentSearch.  # noqa: E501
        :type: int
        """
        if nr_extra_docs is None:
            raise ValueError("Invalid value for `nr_extra_docs`, must not be `None`")  # noqa: E501

        self._nr_extra_docs = nr_extra_docs

    @property
    def signer_emails(self):
        """Gets the signer_emails of this DocumentSearch.  # noqa: E501


        :return: The signer_emails of this DocumentSearch.  # noqa: E501
        :rtype: list[str]
        """
        return self._signer_emails

    @signer_emails.setter
    def signer_emails(self, signer_emails):
        """Sets the signer_emails of this DocumentSearch.


        :param signer_emails: The signer_emails of this DocumentSearch.  # noqa: E501
        :type: list[str]
        """

        self._signer_emails = signer_emails

    @property
    def status_display(self):
        """Gets the status_display of this DocumentSearch.  # noqa: E501


        :return: The status_display of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._status_display

    @status_display.setter
    def status_display(self, status_display):
        """Sets the status_display of this DocumentSearch.


        :param status_display: The status_display of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if status_display is not None and len(status_display) < 1:
            raise ValueError("Invalid value for `status_display`, length must be greater than or equal to `1`")  # noqa: E501

        self._status_display = status_display

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this DocumentSearch.  # noqa: E501


        :return: The created_timestamp of this DocumentSearch.  # noqa: E501
        :rtype: int
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this DocumentSearch.


        :param created_timestamp: The created_timestamp of this DocumentSearch.  # noqa: E501
        :type: int
        """

        self._created_timestamp = created_timestamp

    @property
    def finished_on_timestamp(self):
        """Gets the finished_on_timestamp of this DocumentSearch.  # noqa: E501


        :return: The finished_on_timestamp of this DocumentSearch.  # noqa: E501
        :rtype: int
        """
        return self._finished_on_timestamp

    @finished_on_timestamp.setter
    def finished_on_timestamp(self, finished_on_timestamp):
        """Sets the finished_on_timestamp of this DocumentSearch.


        :param finished_on_timestamp: The finished_on_timestamp of this DocumentSearch.  # noqa: E501
        :type: int
        """

        self._finished_on_timestamp = finished_on_timestamp

    @property
    def parent_doc(self):
        """Gets the parent_doc of this DocumentSearch.  # noqa: E501


        :return: The parent_doc of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._parent_doc

    @parent_doc.setter
    def parent_doc(self, parent_doc):
        """Sets the parent_doc of this DocumentSearch.


        :param parent_doc: The parent_doc of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if parent_doc is not None and len(parent_doc) < 1:
            raise ValueError("Invalid value for `parent_doc`, length must be greater than or equal to `1`")  # noqa: E501

        self._parent_doc = parent_doc

    @property
    def finished_on(self):
        """Gets the finished_on of this DocumentSearch.  # noqa: E501


        :return: The finished_on of this DocumentSearch.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_on

    @finished_on.setter
    def finished_on(self, finished_on):
        """Sets the finished_on of this DocumentSearch.


        :param finished_on: The finished_on of this DocumentSearch.  # noqa: E501
        :type: datetime
        """

        self._finished_on = finished_on

    @property
    def subdomain(self):
        """Gets the subdomain of this DocumentSearch.  # noqa: E501


        :return: The subdomain of this DocumentSearch.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this DocumentSearch.


        :param subdomain: The subdomain of this DocumentSearch.  # noqa: E501
        :type: str
        """
        if subdomain is not None and len(subdomain) < 1:
            raise ValueError("Invalid value for `subdomain`, length must be greater than or equal to `1`")  # noqa: E501

        self._subdomain = subdomain

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
        if issubclass(DocumentSearch, dict):
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
        if not isinstance(other, DocumentSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
