# signrequest_client.SignrequestQuickCreateApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signrequest_quick_create_create**](SignrequestQuickCreateApi.md#signrequest_quick_create_create) | **POST** /signrequest-quick-create/ | Quick create a SignRequest


# **signrequest_quick_create_create**
> SignRequestQuickCreate signrequest_quick_create_create(data)

Quick create a SignRequest



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
api_instance = signrequest_client.SignrequestQuickCreateApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.SignRequestQuickCreate() # SignRequestQuickCreate | 

try:
    # Quick create a SignRequest
    api_response = api_instance.signrequest_quick_create_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestQuickCreateApi->signrequest_quick_create_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SignRequestQuickCreate**](SignRequestQuickCreate.md)|  | 

### Return type

[**SignRequestQuickCreate**](SignRequestQuickCreate.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

