# signrequest_client.EventsApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_list**](EventsApi.md#events_list) | **GET** /events/ | Retrieve a list of Events
[**events_read**](EventsApi.md#events_read) | **GET** /events/{id}/ | Retrieve an Event


# **events_list**
> InlineResponse2004 events_list(document__uuid=document__uuid, document__external_id=document__external_id, document__signrequest__who=document__signrequest__who, document__signrequest__from_email=document__signrequest__from_email, document__status=document__status, document__user__email=document__user__email, document__user__first_name=document__user__first_name, document__user__last_name=document__user__last_name, delivered=delivered, delivered_on=delivered_on, timestamp=timestamp, status=status, event_type=event_type, page=page, limit=limit)

Retrieve a list of Events



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
api_instance = signrequest_client.EventsApi(signrequest_client.ApiClient(configuration))
document__uuid = 'document__uuid_example' # str |  (optional)
document__external_id = 'document__external_id_example' # str |  (optional)
document__signrequest__who = 'document__signrequest__who_example' # str |  (optional)
document__signrequest__from_email = 'document__signrequest__from_email_example' # str |  (optional)
document__status = 'document__status_example' # str |  (optional)
document__user__email = 'document__user__email_example' # str |  (optional)
document__user__first_name = 'document__user__first_name_example' # str |  (optional)
document__user__last_name = 'document__user__last_name_example' # str |  (optional)
delivered = 'delivered_example' # str |  (optional)
delivered_on = 'delivered_on_example' # str |  (optional)
timestamp = 'timestamp_example' # str |  (optional)
status = 'status_example' # str |  (optional)
event_type = 'event_type_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Events
    api_response = api_instance.events_list(document__uuid=document__uuid, document__external_id=document__external_id, document__signrequest__who=document__signrequest__who, document__signrequest__from_email=document__signrequest__from_email, document__status=document__status, document__user__email=document__user__email, document__user__first_name=document__user__first_name, document__user__last_name=document__user__last_name, delivered=delivered, delivered_on=delivered_on, timestamp=timestamp, status=status, event_type=event_type, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document__uuid** | **str**|  | [optional] 
 **document__external_id** | **str**|  | [optional] 
 **document__signrequest__who** | **str**|  | [optional] 
 **document__signrequest__from_email** | **str**|  | [optional] 
 **document__status** | **str**|  | [optional] 
 **document__user__email** | **str**|  | [optional] 
 **document__user__first_name** | **str**|  | [optional] 
 **document__user__last_name** | **str**|  | [optional] 
 **delivered** | **str**|  | [optional] 
 **delivered_on** | **str**|  | [optional] 
 **timestamp** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **event_type** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_read**
> Event events_read(id)

Retrieve an Event



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
api_instance = signrequest_client.EventsApi(signrequest_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this event.

try:
    # Retrieve an Event
    api_response = api_instance.events_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this event. | 

### Return type

[**Event**](Event.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

