# SignRequest API Client
API for [SignRequest.com](https://signrequest.com/)

[![PyPI version](https://badge.fury.io/py/signrequest-python-client.svg)](https://badge.fury.io/py/signrequest-python-client)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install signrequest-python-client
```
(you may need to run `pip` with root permission: `sudo pip install signrequest_python_client`)

Then import the package:
```python
import signrequest_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import signrequest_client
```

## API Documentation
Full API documentation, including code samples, can be found here:
https://signrequest.com/api/v1/docs/

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import signrequest_client
from signrequest_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
signrequest_client.configuration = signrequest_client.Configuration()
signrequest_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
signrequest_client.configuration.api_key_prefix['Authorization'] = 'Token'
# create an instance of the API class
api_instance = signrequest_client.DocumentsApi()
data = signrequest_client.Document(
    file_from_url='https://docs.google.com/document/d/1oI2R1SxfMNZXiz3jCQvorpoklF9xq_dCJnOpkI-zo80/edit?usp=sharing'
)


try:
    # Create a Document
    api_response = api_instance.documents_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://signrequest.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiTokensApi* | [**api_tokens_create**](docs/ApiTokensApi.md#api_tokens_create) | **POST** /api-tokens/ | Create an API token
*ApiTokensApi* | [**api_tokens_delete**](docs/ApiTokensApi.md#api_tokens_delete) | **DELETE** /api-tokens/{key}/ | Delete an API token
*ApiTokensApi* | [**api_tokens_list**](docs/ApiTokensApi.md#api_tokens_list) | **GET** /api-tokens/ | Retrieve a list of API tokens
*ApiTokensApi* | [**api_tokens_read**](docs/ApiTokensApi.md#api_tokens_read) | **GET** /api-tokens/{key}/ | Retrieve an API token
*DocumentAttachmentsApi* | [**document_attachments_create**](docs/DocumentAttachmentsApi.md#document_attachments_create) | **POST** /document-attachments/ | Create a Document Attachment
*DocumentAttachmentsApi* | [**document_attachments_list**](docs/DocumentAttachmentsApi.md#document_attachments_list) | **GET** /document-attachments/ | Retrieve a list of Document Attachments
*DocumentAttachmentsApi* | [**document_attachments_read**](docs/DocumentAttachmentsApi.md#document_attachments_read) | **GET** /document-attachments/{uuid}/ | Retrieve a Document Attachment
*DocumentsApi* | [**documents_create**](docs/DocumentsApi.md#documents_create) | **POST** /documents/ | Create a Document
*DocumentsApi* | [**documents_delete**](docs/DocumentsApi.md#documents_delete) | **DELETE** /documents/{uuid}/ | Delete a Document
*DocumentsApi* | [**documents_list**](docs/DocumentsApi.md#documents_list) | **GET** /documents/ | Retrieve a list of Documents
*DocumentsApi* | [**documents_read**](docs/DocumentsApi.md#documents_read) | **GET** /documents/{uuid}/ | Retrieve a Document
*DocumentsSearchApi* | [**documents_search_list**](docs/DocumentsSearchApi.md#documents_search_list) | **GET** /documents-search/ | Search documents
*EventsApi* | [**events_list**](docs/EventsApi.md#events_list) | **GET** /events/ | Retrieve a list of Events
*EventsApi* | [**events_read**](docs/EventsApi.md#events_read) | **GET** /events/{id}/ | Retrieve an Event
*SignrequestQuickCreateApi* | [**signrequest_quick_create_create**](docs/SignrequestQuickCreateApi.md#signrequest_quick_create_create) | **POST** /signrequest-quick-create/ | Quick create a SignRequest
*SignrequestsApi* | [**signrequests_cancel_signrequest**](docs/SignrequestsApi.md#signrequests_cancel_signrequest) | **POST** /signrequests/{uuid}/cancel_signrequest/ | Cancel a SignRequest
*SignrequestsApi* | [**signrequests_create**](docs/SignrequestsApi.md#signrequests_create) | **POST** /signrequests/ | Create a SignRequest
*SignrequestsApi* | [**signrequests_list**](docs/SignrequestsApi.md#signrequests_list) | **GET** /signrequests/ | Retrieve a list of SignRequests
*SignrequestsApi* | [**signrequests_read**](docs/SignrequestsApi.md#signrequests_read) | **GET** /signrequests/{uuid}/ | Retrieve a SignRequest
*SignrequestsApi* | [**signrequests_resend_signrequest_email**](docs/SignrequestsApi.md#signrequests_resend_signrequest_email) | **POST** /signrequests/{uuid}/resend_signrequest_email/ | Resend a SignRequest
*TeamMembersApi* | [**team_members_list**](docs/TeamMembersApi.md#team_members_list) | **GET** /team-members/ | Retrieve a list of Team Members
*TeamMembersApi* | [**team_members_read**](docs/TeamMembersApi.md#team_members_read) | **GET** /team-members/{uuid}/ | Retrieve a Team Member
*TeamsApi* | [**teams_create**](docs/TeamsApi.md#teams_create) | **POST** /teams/ | Create a Team
*TeamsApi* | [**teams_invite_member**](docs/TeamsApi.md#teams_invite_member) | **POST** /teams/{subdomain}/invite_member/ | Invite a Team Member
*TeamsApi* | [**teams_list**](docs/TeamsApi.md#teams_list) | **GET** /teams/ | Retrieve a list of Teams
*TeamsApi* | [**teams_partial_update**](docs/TeamsApi.md#teams_partial_update) | **PATCH** /teams/{subdomain}/ | Update a Team
*TeamsApi* | [**teams_read**](docs/TeamsApi.md#teams_read) | **GET** /teams/{subdomain}/ | Retrieve a Team
*TemplatesApi* | [**templates_list**](docs/TemplatesApi.md#templates_list) | **GET** /templates/ | Retrieve a list of Templates
*TemplatesApi* | [**templates_read**](docs/TemplatesApi.md#templates_read) | **GET** /templates/{uuid}/ | Retrieve a Template
*WebhooksApi* | [**webhooks_create**](docs/WebhooksApi.md#webhooks_create) | **POST** /webhooks/ | Create a Webhook
*WebhooksApi* | [**webhooks_delete**](docs/WebhooksApi.md#webhooks_delete) | **DELETE** /webhooks/{uuid}/ | Delete a Webhook
*WebhooksApi* | [**webhooks_list**](docs/WebhooksApi.md#webhooks_list) | **GET** /webhooks/ | Retrieve a list of Webhooks
*WebhooksApi* | [**webhooks_partial_update**](docs/WebhooksApi.md#webhooks_partial_update) | **PATCH** /webhooks/{uuid}/ | Partially update a Webhook
*WebhooksApi* | [**webhooks_read**](docs/WebhooksApi.md#webhooks_read) | **GET** /webhooks/{uuid}/ | Retrieve a Webhook
*WebhooksApi* | [**webhooks_update**](docs/WebhooksApi.md#webhooks_update) | **PUT** /webhooks/{uuid}/ | Update a Webhook


## Documentation For Models

 - [AuthToken](docs/AuthToken.md)
 - [Document](docs/Document.md)
 - [DocumentAttachment](docs/DocumentAttachment.md)
 - [DocumentSearch](docs/DocumentSearch.md)
 - [DocumentSignerTemplateConf](docs/DocumentSignerTemplateConf.md)
 - [Event](docs/Event.md)
 - [FileFromSf](docs/FileFromSf.md)
 - [InlineDocumentSignerIntegrationData](docs/InlineDocumentSignerIntegrationData.md)
 - [InlineIntegrationData](docs/InlineIntegrationData.md)
 - [InlinePrefillTags](docs/InlinePrefillTags.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineSignRequest](docs/InlineSignRequest.md)
 - [InlineTeam](docs/InlineTeam.md)
 - [InlineTeamMember](docs/InlineTeamMember.md)
 - [InviteMember](docs/InviteMember.md)
 - [Placeholder](docs/Placeholder.md)
 - [RequiredAttachment](docs/RequiredAttachment.md)
 - [SignRequest](docs/SignRequest.md)
 - [SignRequestQuickCreate](docs/SignRequestQuickCreate.md)
 - [Signer](docs/Signer.md)
 - [SignerAttachment](docs/SignerAttachment.md)
 - [SignerInputs](docs/SignerInputs.md)
 - [SigningLog](docs/SigningLog.md)
 - [Team](docs/Team.md)
 - [TeamMember](docs/TeamMember.md)
 - [Template](docs/Template.md)
 - [User](docs/User.md)
 - [WebhookSubscription](docs/WebhookSubscription.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

tech-support@signrequest.com

