# -*- coding: utf-8 -*-
import hashlib
import hmac
from signrequest_client import __version__ as version

__author__ = "Michaël Krens"
__copyright__ = "Copyright 2015, SignRequest B.V."
import json
try:
    import requests
except ImportError:
    pass


class SignRequestClientException(Exception):
    pass


class SignRequestClient(object):

    def __init__(self, subdomain, token=None, api_base_endpoint='https://signrequest.com/api/v1/',
                 username=None, password=None):
        self.subdomain = subdomain
        self.token = token
        self.api_base_endpoint = api_base_endpoint
        if username and password:
            self.authenticate(username, password)
        if not self.token:
            raise SignRequestClientException(
                "Please authenticate by providing a valid token or by username and password")

    def get_headers(self, is_json=False):
        headers = {'Authorization': 'Token %s' % self.token, 'X-Client-Version': version}
        if is_json:
            headers['Content-Type'] = 'application/json'
        return headers

    def authenticate(self, username, password):
        resp = requests.post(
            self.api_base_endpoint + 'api-tokens/',
            data={'subdomain': self.subdomain}, auth=(username, password)
        )
        if resp.ok:
            self.token = json.loads(resp.content)['token']
        else:
            raise SignRequestClientException("Could not authenticate, response: %s " % resp.content)
        return self.token

    def create_document_from_file(self, file_object):
        resp = requests.post(
            self.api_base_endpoint + 'documents/', files={'file': file_object},
            headers=self.get_headers())
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not create document, response: %s " % resp.content)

    def create_document_from_url(self, url):
        resp = requests.post(
            self.api_base_endpoint + 'documents/', data={'file_from_url': url},
            headers=self.get_headers(is_json=True))
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not create document, response: %s " % resp.content)

    def create_signrequest(self, uuid, from_email, signers=None, who='o', message='', subject='',
                           required_attachments=None, disable_attachments=False):
        signers = signers or []
        required_attachments = required_attachments or []
        if not isinstance(signers, list):
            raise SignRequestClientException("`signers` must be a list")
        if not isinstance(required_attachments, list):
            raise SignRequestClientException("`required_attachments` must be a list")
        # all other invalid posts will be returned by the API with an error
        data = {
            'document': self.api_base_endpoint + 'documents/' + uuid + '/',
            'from_email': from_email,
            'who': who,
            'message': message,
            'subject': subject,
            'disable_attachments': disable_attachments,
            'required_attachments': required_attachments,
            'signers': signers,
        }
        resp = requests.post(
            self.api_base_endpoint + 'signrequests/',
            data=json.dumps(data),
            headers=self.get_headers(is_json=True))
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not create document, response: %s " % resp.content)

    def get_document(self, uuid):
        resp = requests.get(
            self.api_base_endpoint + 'documents/' + uuid + '/',
            headers=self.get_headers())
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not get document, response: %s " % resp.content)

    def get_documents(self, filter_params=''):
        filter_params = filter_params.strip('?').strip('&')
        endpoint = self.api_base_endpoint + 'documents/?' + filter_params
        resp = requests.get(
            endpoint,
            headers=self.get_headers())
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not get documents, response: %s " % resp.content)

    def get_events(self, doc_uuid=None, filter_params=''):
        endpoint = self.api_base_endpoint + 'events/'
        filter_params = filter_params.strip('?').strip('&')
        if doc_uuid or filter_params:
            endpoint += '?'
        if filter_params:
            endpoint += filter_params
        if doc_uuid:
            if not endpoint.endswith('?'):
                endpoint += '&' if not endpoint.endswith('&') else ''
            endpoint += 'document__uuid=' + doc_uuid
        resp = requests.get(
            endpoint,
            headers=self.get_headers())
        if resp.ok:
            return json.loads(resp.content)
        else:
            raise SignRequestClientException("Could not get event(s), response: %s " % resp.content)

    def confirm_callback_authenticity(self, event_time, event_type, event_hash):
        return event_hash == hmac.new(self.token, (event_time + event_type),
                                      hashlib.sha256).hexdigest()
