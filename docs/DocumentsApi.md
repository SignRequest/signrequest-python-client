# signrequest_client.DocumentsApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_create**](DocumentsApi.md#documents_create) | **POST** /documents/ | Create a Document
[**documents_delete**](DocumentsApi.md#documents_delete) | **DELETE** /documents/{uuid}/ | Delete a Document
[**documents_list**](DocumentsApi.md#documents_list) | **GET** /documents/ | Retrieve a list of Documents
[**documents_read**](DocumentsApi.md#documents_read) | **GET** /documents/{uuid}/ | Retrieve a Document


# **documents_create**
> Document documents_create(data)

Create a Document



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
api_instance = signrequest_client.DocumentsApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.Document() # Document | 

try:
    # Create a Document
    api_response = api_instance.documents_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_delete**
> documents_delete(uuid)

Delete a Document



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
api_instance = signrequest_client.DocumentsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Delete a Document
    api_instance.documents_delete(uuid)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_list**
> InlineResponse2003 documents_list(external_id=external_id, signrequest__who=signrequest__who, signrequest__from_email=signrequest__from_email, status=status, user__email=user__email, user__first_name=user__first_name, user__last_name=user__last_name, created=created, modified=modified, page=page, limit=limit)

Retrieve a list of Documents



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
api_instance = signrequest_client.DocumentsApi(signrequest_client.ApiClient(configuration))
external_id = 'external_id_example' # str |  (optional)
signrequest__who = 'signrequest__who_example' # str |  (optional)
signrequest__from_email = 'signrequest__from_email_example' # str |  (optional)
status = 'status_example' # str |  (optional)
user__email = 'user__email_example' # str |  (optional)
user__first_name = 'user__first_name_example' # str |  (optional)
user__last_name = 'user__last_name_example' # str |  (optional)
created = 'created_example' # str |  (optional)
modified = 'modified_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Documents
    api_response = api_instance.documents_list(external_id=external_id, signrequest__who=signrequest__who, signrequest__from_email=signrequest__from_email, status=status, user__email=user__email, user__first_name=user__first_name, user__last_name=user__last_name, created=created, modified=modified, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_id** | **str**|  | [optional] 
 **signrequest__who** | **str**|  | [optional] 
 **signrequest__from_email** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **user__email** | **str**|  | [optional] 
 **user__first_name** | **str**|  | [optional] 
 **user__last_name** | **str**|  | [optional] 
 **created** | **str**|  | [optional] 
 **modified** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_read**
> Document documents_read(uuid)

Retrieve a Document



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
api_instance = signrequest_client.DocumentsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Retrieve a Document
    api_response = api_instance.documents_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

