# signrequest_client.DocumentAttachmentsApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**document_attachments_create**](DocumentAttachmentsApi.md#document_attachments_create) | **POST** /document-attachments/ | Create a Document Attachment
[**document_attachments_list**](DocumentAttachmentsApi.md#document_attachments_list) | **GET** /document-attachments/ | Retrieve a list of Document Attachments
[**document_attachments_read**](DocumentAttachmentsApi.md#document_attachments_read) | **GET** /document-attachments/{uuid}/ | Retrieve a Document Attachment


# **document_attachments_create**
> DocumentAttachment document_attachments_create(data)

Create a Document Attachment



### Example
```python
from __future__ import print_function
import time
import signrequest_client
from signrequest_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = signrequest_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = signrequest_client.DocumentAttachmentsApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.DocumentAttachment() # DocumentAttachment | 

try:
    # Create a Document Attachment
    api_response = api_instance.document_attachments_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAttachmentsApi->document_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DocumentAttachment**](DocumentAttachment.md)|  | 

### Return type

[**DocumentAttachment**](DocumentAttachment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_attachments_list**
> InlineResponse2001 document_attachments_list(document__uuid=document__uuid, document__external_id=document__external_id, created=created, page=page, limit=limit)

Retrieve a list of Document Attachments



### Example
```python
from __future__ import print_function
import time
import signrequest_client
from signrequest_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = signrequest_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = signrequest_client.DocumentAttachmentsApi(signrequest_client.ApiClient(configuration))
document__uuid = 'document__uuid_example' # str |  (optional)
document__external_id = 'document__external_id_example' # str |  (optional)
created = 'created_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Document Attachments
    api_response = api_instance.document_attachments_list(document__uuid=document__uuid, document__external_id=document__external_id, created=created, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAttachmentsApi->document_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document__uuid** | **str**|  | [optional] 
 **document__external_id** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_attachments_read**
> DocumentAttachment document_attachments_read(uuid)

Retrieve a Document Attachment



### Example
```python
from __future__ import print_function
import time
import signrequest_client
from signrequest_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = signrequest_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
configuration.api_key_prefix['Authorization'] = 'Token'

# create an instance of the API class
api_instance = signrequest_client.DocumentAttachmentsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Retrieve a Document Attachment
    api_response = api_instance.document_attachments_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentAttachmentsApi->document_attachments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**DocumentAttachment**](DocumentAttachment.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

