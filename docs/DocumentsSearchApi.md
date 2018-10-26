# signrequest_client.DocumentsSearchApi

All URIs are relative to *https://signrequest.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_search_list**](DocumentsSearchApi.md#documents_search_list) | **GET** /documents-search/ | Search documents


# **documents_search_list**
> InlineResponse2002 documents_search_list(page=page, limit=limit, q=q, autocomplete=autocomplete, name=name, subdomain=subdomain, signer_emails=signer_emails, status=status, who=who, format=format, signer_data=signer_data)

Search documents

Search interface for fast (autocomplete) searching of documents.  This can be useful to have your users search for a document in your interface.  Document names are tokenized on whitespace, hyphens and underscores to also match partial document names.  *Normal search:*  - ?**q**={{query}}  *Autocomplete search:*  - ?**autocomplete**={{partial query}}  *Search in document name:*  - ?**name**={{query}}  *Available (extra) filters:*  - ?**subdomain**={{ team_subdomain }} or use this endpoint with team_subdomain.signrequest.com (when not provided only personal documents are shown) - ?**signer_emails**={{ signer@email.com }} (will filter documents that an email needed to sign/approve) - ?**status**={{ si }} - ?**who**={{ mo }}  To include multiple values for a filter field separate the values with a pipe (|). For example to only search for completed documents use **status=se|vi** (sent and viewed).  *Pagination:*  - ?**page**={{ page_number: default 1 }} - ?**limit**={{ limit results: default 10, max 100 }}  *Format:*  By default json is returned, to export data as csv or xls use the format parameter.  - ?**format**=csv - ?**format**=xls  For csv and xls the data can also be exported with each signer on a separate row. In this mode also the signer inputs that have an *external_id* specified on a tag will be exported. All external_id's found will be exported as columns. To use this mode add the **signer_data** parameter.  - ?**format**=csv&**signer_data**=1 - ?**format**=xls&**signer_data**=1  Note that all documents are only ordered by **created** (newest first) when **q**, **autocomplete** or **name** are not used, else they are ordered by the strenght of the match.

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
api_instance = signrequest_client.DocumentsSearchApi(signrequest_client.ApiClient(configuration))
page = 56 # int | A page number within the paginated result set. (optional)
limit = 56 # int | Number of results to return per page. (optional)
q = 'q_example' # str | Normal search query (optional)
autocomplete = 'autocomplete_example' # str | Partial search query (optional)
name = 'name_example' # str | Document name (optional)
subdomain = 'subdomain_example' # str |  (optional)
signer_emails = 'signer_emails_example' # str | Email needed to sign/approve (optional)
status = 'status_example' # str | `co`: converting, `ne`: new, `se`: sent, `vi`: viewed, `si`: signed, `do`: downloaded, `sd`: signed and downloaded, `ca`: cancelled, `de`: declined, `ec`: error converting, `es`: error sending, `xp`: expired (optional)
who = 'who_example' # str | `m`: only me, `mo`: me and others, `o`: only others (optional)
format = 'format_example' # str | Export format, can be `json` (default), `csv`, or `xls` (optional)
signer_data = 8.14 # float | Set to `1` to export with each signer on a separate row (optional)

try:
    # Search documents
    api_response = api_instance.documents_search_list(page=page, limit=limit, q=q, autocomplete=autocomplete, name=name, subdomain=subdomain, signer_emails=signer_emails, status=status, who=who, format=format, signer_data=signer_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsSearchApi->documents_search_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **q** | **str**| Normal search query | [optional] 
 **autocomplete** | **str**| Partial search query | [optional] 
 **name** | **str**| Document name | [optional] 
 **subdomain** | **str**|  | [optional] 
 **signer_emails** | **str**| Email needed to sign/approve | [optional] 
 **status** | **str**| &#x60;co&#x60;: converting, &#x60;ne&#x60;: new, &#x60;se&#x60;: sent, &#x60;vi&#x60;: viewed, &#x60;si&#x60;: signed, &#x60;do&#x60;: downloaded, &#x60;sd&#x60;: signed and downloaded, &#x60;ca&#x60;: cancelled, &#x60;de&#x60;: declined, &#x60;ec&#x60;: error converting, &#x60;es&#x60;: error sending, &#x60;xp&#x60;: expired | [optional] 
 **who** | **str**| &#x60;m&#x60;: only me, &#x60;mo&#x60;: me and others, &#x60;o&#x60;: only others | [optional] 
 **format** | **str**| Export format, can be &#x60;json&#x60; (default), &#x60;csv&#x60;, or &#x60;xls&#x60; | [optional] 
 **signer_data** | **float**| Set to &#x60;1&#x60; to export with each signer on a separate row | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/csv, application/vnd.ms-excel

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

