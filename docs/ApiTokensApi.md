# signrequest_client.ApiTokensApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tokens_list**](ApiTokensApi.md#api_tokens_list) | **GET** /api-tokens/ | Retrieve a list of API tokens


# **api_tokens_list**
> InlineResponse200 api_tokens_list(page=page, limit=limit)

Retrieve a list of API tokens



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
api_instance = signrequest_client.ApiTokensApi(signrequest_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of API tokens
    api_response = api_instance.api_tokens_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokensApi->api_tokens_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

