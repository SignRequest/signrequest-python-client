# signrequest_client.SignrequestsApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**signrequests_cancel_signrequest**](SignrequestsApi.md#signrequests_cancel_signrequest) | **POST** /signrequests/{uuid}/cancel_signrequest/ | Cancel a SignRequest
[**signrequests_create**](SignrequestsApi.md#signrequests_create) | **POST** /signrequests/ | Create a SignRequest
[**signrequests_list**](SignrequestsApi.md#signrequests_list) | **GET** /signrequests/ | Retrieve a list of SignRequests
[**signrequests_read**](SignrequestsApi.md#signrequests_read) | **GET** /signrequests/{uuid}/ | Retrieve a SignRequest
[**signrequests_resend_signrequest_email**](SignrequestsApi.md#signrequests_resend_signrequest_email) | **POST** /signrequests/{uuid}/resend_signrequest_email/ | Resend a SignRequest


# **signrequests_cancel_signrequest**
> InlineResponse201 signrequests_cancel_signrequest(uuid)

Cancel a SignRequest



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
api_instance = signrequest_client.SignrequestsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Cancel a SignRequest
    api_response = api_instance.signrequests_cancel_signrequest(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestsApi->signrequests_cancel_signrequest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signrequests_create**
> SignRequest signrequests_create(data)

Create a SignRequest



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
api_instance = signrequest_client.SignrequestsApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.SignRequest() # SignRequest | 

try:
    # Create a SignRequest
    api_response = api_instance.signrequests_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestsApi->signrequests_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SignRequest**](SignRequest.md)|  | 

### Return type

[**SignRequest**](SignRequest.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signrequests_list**
> InlineResponse2005 signrequests_list(who=who, from_email=from_email, page=page, limit=limit)

Retrieve a list of SignRequests



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
api_instance = signrequest_client.SignrequestsApi(signrequest_client.ApiClient(configuration))
who = 'who_example' # str |  (optional)
from_email = 'from_email_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of SignRequests
    api_response = api_instance.signrequests_list(who=who, from_email=from_email, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestsApi->signrequests_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **who** | **str**|  | [optional] 
 **from_email** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signrequests_read**
> SignRequest signrequests_read(uuid)

Retrieve a SignRequest



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
api_instance = signrequest_client.SignrequestsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Retrieve a SignRequest
    api_response = api_instance.signrequests_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestsApi->signrequests_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**SignRequest**](SignRequest.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signrequests_resend_signrequest_email**
> InlineResponse2011 signrequests_resend_signrequest_email(uuid)

Resend a SignRequest



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
api_instance = signrequest_client.SignrequestsApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Resend a SignRequest
    api_response = api_instance.signrequests_resend_signrequest_email(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SignrequestsApi->signrequests_resend_signrequest_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**InlineResponse2011**](InlineResponse2011.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

