# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**file_as_pdf** | **str** | Temporary URL to original file as PDF, expires in five minutes | [optional] 
**name** | **str** | Defaults to filename, including extension | [optional] 
**external_id** | **str** | ID used to reference document in external system | [optional] 
**frontend_id** | **str** | Shared secret used in conjunction with &lt;a href&#x3D;\&quot;#section/Frontend-API/SignRequest-js-client-(beta)\&quot;&gt;SignRequest-js client&lt;/a&gt; to grant user access to a document that&#39;s not a member of the document&#39;s team | [optional] 
**file** | **str** | Temporary URL to original file, expires in five minutes | [optional] 
**file_from_url** | **str** | Publicly accessible URL of document to be downloaded by SignRequest | [optional] 
**events_callback_url** | **str** | URL at which to receive [event callbacks](#section/Events/Events-callback) for this document | [optional] 
**file_from_content** | **str** | Base64 encoded document content | [optional] 
**file_from_content_name** | **str** | Filename, including extension. Required when using &#x60;file_from_content&#x60;. | [optional] 
**template** | **str** |  | [optional] 
**prefill_tags** | [**list[InlinePrefillTags]**](InlinePrefillTags.md) | Prefill signer input data, see [prefill tags](#section/Preparing-a-document/Prefill-tags-templates) | [optional] 
**integrations** | [**list[InlineIntegrationData]**](InlineIntegrationData.md) |  | [optional] 
**file_from_sf** | [**FileFromSf**](FileFromSf.md) |  | [optional] 
**auto_delete_days** | **int** | Number of days after which a finished document (signed/cancelled/declined) will be automatically deleted | [optional] 
**pdf** | **str** | Temporary URL to signed document as PDF, expires in five minutes | [optional] 
**status** | **str** | &#x60;co&#x60;: converting, &#x60;ne&#x60;: new, &#x60;se&#x60;: sent, &#x60;vi&#x60;: viewed, &#x60;si&#x60;: signed, &#x60;do&#x60;: downloaded, &#x60;sd&#x60;: signed and downloaded, &#x60;ca&#x60;: cancelled, &#x60;de&#x60;: declined, &#x60;ec&#x60;: error converting, &#x60;es&#x60;: error sending, &#x60;xp&#x60;: expired | [optional] 
**api_used** | **bool** | Indicates whether document was created using the API | [optional] 
**security_hash** | **str** | SHA256 hash of PDF contents | [optional] 
**attachments** | [**list[DocumentAttachment]**](DocumentAttachment.md) |  | [optional] 
**auto_delete_after** | **datetime** | Date and time calculated using &#x60;auto_delete_days&#x60; after which a finished document (signed/cancelled/declined) will be automatically deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


