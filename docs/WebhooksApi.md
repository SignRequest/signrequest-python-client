# signrequest_client.WebhooksApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooks_create**](WebhooksApi.md#webhooks_create) | **POST** /webhooks/ | Create a Webhook
[**webhooks_delete**](WebhooksApi.md#webhooks_delete) | **DELETE** /webhooks/{uuid}/ | Delete a Webhook
[**webhooks_list**](WebhooksApi.md#webhooks_list) | **GET** /webhooks/ | Retrieve a list of Webhooks
[**webhooks_partial_update**](WebhooksApi.md#webhooks_partial_update) | **PATCH** /webhooks/{uuid}/ | Partially update a Webhook
[**webhooks_read**](WebhooksApi.md#webhooks_read) | **GET** /webhooks/{uuid}/ | Retrieve a Webhook
[**webhooks_update**](WebhooksApi.md#webhooks_update) | **PUT** /webhooks/{uuid}/ | Update a Webhook


# **webhooks_create**
> WebhookSubscription webhooks_create(data)

Create a Webhook



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.WebhookSubscription() # WebhookSubscription | 

try:
    # Create a Webhook
    api_response = api_instance.webhooks_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WebhookSubscription**](WebhookSubscription.md)|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_delete**
> webhooks_delete(uuid)

Delete a Webhook



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Delete a Webhook
    api_instance.webhooks_delete(uuid)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_delete: %s\n" % e)
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

# **webhooks_list**
> InlineResponse2009 webhooks_list(page=page, limit=limit)

Retrieve a list of Webhooks



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Webhooks
    api_response = api_instance.webhooks_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_partial_update**
> WebhookSubscription webhooks_partial_update(uuid, data)

Partially update a Webhook



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 
data = signrequest_client.WebhookSubscription() # WebhookSubscription | 

try:
    # Partially update a Webhook
    api_response = api_instance.webhooks_partial_update(uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **data** | [**WebhookSubscription**](WebhookSubscription.md)|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_read**
> WebhookSubscription webhooks_read(uuid)

Retrieve a Webhook



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Retrieve a Webhook
    api_response = api_instance.webhooks_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooks_update**
> WebhookSubscription webhooks_update(uuid, data)

Update a Webhook



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
api_instance = signrequest_client.WebhooksApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 
data = signrequest_client.WebhookSubscription() # WebhookSubscription | 

try:
    # Update a Webhook
    api_response = api_instance.webhooks_update(uuid, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->webhooks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **data** | [**WebhookSubscription**](WebhookSubscription.md)|  | 

### Return type

[**WebhookSubscription**](WebhookSubscription.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

