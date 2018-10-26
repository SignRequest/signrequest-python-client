# signrequest_client.TeamMembersApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**team_members_list**](TeamMembersApi.md#team_members_list) | **GET** /team-members/ | Retrieve a list of Team Members
[**team_members_read**](TeamMembersApi.md#team_members_read) | **GET** /team-members/{uuid}/ | Retrieve a Team Member


# **team_members_list**
> InlineResponse2006 team_members_list(is_active=is_active, is_owner=is_owner, is_admin=is_admin, user__email=user__email, user__first_name=user__first_name, user__last_name=user__last_name, page=page, limit=limit)

Retrieve a list of Team Members



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
api_instance = signrequest_client.TeamMembersApi(signrequest_client.ApiClient(configuration))
is_active = 'is_active_example' # str |  (optional)
is_owner = 'is_owner_example' # str |  (optional)
is_admin = 'is_admin_example' # str |  (optional)
user__email = 'user__email_example' # str |  (optional)
user__first_name = 'user__first_name_example' # str |  (optional)
user__last_name = 'user__last_name_example' # str |  (optional)
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Team Members
    api_response = api_instance.team_members_list(is_active=is_active, is_owner=is_owner, is_admin=is_admin, user__email=user__email, user__first_name=user__first_name, user__last_name=user__last_name, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->team_members_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **str**|  | [optional] 
 **is_owner** | **str**|  | [optional] 
 **is_admin** | **str**|  | [optional] 
 **user__email** | **str**|  | [optional] 
 **user__first_name** | **str**|  | [optional] 
 **user__last_name** | **str**|  | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_members_read**
> TeamMember team_members_read(uuid)

Retrieve a Team Member



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
api_instance = signrequest_client.TeamMembersApi(signrequest_client.ApiClient(configuration))
uuid = 'uuid_example' # str | 

try:
    # Retrieve a Team Member
    api_response = api_instance.team_members_read(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->team_members_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**TeamMember**](TeamMember.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

