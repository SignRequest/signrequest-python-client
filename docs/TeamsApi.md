# signrequest_client.TeamsApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_create**](TeamsApi.md#teams_create) | **POST** /teams/ | Create a Team
[**teams_delete**](TeamsApi.md#teams_delete) | **DELETE** /teams/{subdomain}/ | Delete a Team
[**teams_invite_member**](TeamsApi.md#teams_invite_member) | **POST** /teams/{subdomain}/invite_member/ | Invite a Team Member
[**teams_list**](TeamsApi.md#teams_list) | **GET** /teams/ | Retrieve a list of Teams
[**teams_partial_update**](TeamsApi.md#teams_partial_update) | **PATCH** /teams/{subdomain}/ | Update a Team
[**teams_read**](TeamsApi.md#teams_read) | **GET** /teams/{subdomain}/ | Retrieve a Team


# **teams_create**
> Team teams_create(data)

Create a Team

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
data = signrequest_client.Team() # Team | 

try:
    # Create a Team
    api_response = api_instance.teams_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Team**](Team.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_delete**
> teams_delete(subdomain)

Delete a Team

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
subdomain = 'subdomain_example' # str | 

try:
    # Delete a Team
    api_instance.teams_delete(subdomain)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_invite_member**
> InviteMember teams_invite_member(subdomain, data)

Invite a Team Member

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
subdomain = 'subdomain_example' # str | 
data = signrequest_client.InviteMember() # InviteMember | 

try:
    # Invite a Team Member
    api_response = api_instance.teams_invite_member(subdomain, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_invite_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 
 **data** | [**InviteMember**](InviteMember.md)|  | 

### Return type

[**InviteMember**](InviteMember.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list**
> InlineResponse2007 teams_list(page=page, limit=limit)

Retrieve a list of Teams

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)

try:
    # Retrieve a list of Teams
    api_response = api_instance.teams_list(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_partial_update**
> Team teams_partial_update(subdomain, data)

Update a Team

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
subdomain = 'subdomain_example' # str | 
data = signrequest_client.Team() # Team | 

try:
    # Update a Team
    api_response = api_instance.teams_partial_update(subdomain, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 
 **data** | [**Team**](Team.md)|  | 

### Return type

[**Team**](Team.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_read**
> Team teams_read(subdomain)

Retrieve a Team

Required fields are **name** and **subdomain** where the subdomain is globally unique. Use **POST** to create a Team. To update a field on a Team use **PATCH**.  To use the API on behalf of a particular team change the endpoint to: *https://**{{ subdomain }}**.signrequest.com/api/v1/...*  To invite new team members you can use **POST** {\"email\":\"**email-of-member-to-invite@example.com**\",\"is_admin\":false,\"is_owner\":false} to: *https://signrequest.com/api/v1/teams/**{{ subdomain }}**/invite_member/*

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
api_instance = signrequest_client.TeamsApi(signrequest_client.ApiClient(configuration))
subdomain = 'subdomain_example' # str | 

try:
    # Retrieve a Team
    api_response = api_instance.teams_read(subdomain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->teams_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomain** | **str**|  | 

### Return type

[**Team**](Team.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

