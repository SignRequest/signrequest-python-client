# Signer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**display_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email_viewed** | **bool** |  | [optional] 
**viewed** | **bool** |  | [optional] 
**signed** | **bool** |  | [optional] 
**downloaded** | **bool** |  | [optional] 
**signed_on** | **datetime** |  | [optional] 
**needs_to_sign** | **bool** |  | [optional] [default to True]
**approve_only** | **bool** |  | [optional] 
**notify_only** | **bool** |  | [optional] 
**in_person** | **bool** |  | [optional] 
**order** | **int** |  | [optional] 
**language** | **str** |  | [optional] 
**force_language** | **bool** |  | [optional] 
**emailed** | **bool** |  | [optional] 
**verify_phone_number** | **str** |  | [optional] 
**verify_bank_account** | **str** |  | [optional] 
**declined** | **bool** |  | [optional] 
**declined_on** | **datetime** |  | [optional] 
**forwarded** | **str** |  | [optional] 
**forwarded_on** | **datetime** |  | [optional] 
**forwarded_to_email** | **str** |  | [optional] 
**forwarded_reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**embed_url_user_id** | **str** |  | [optional] 
**inputs** | [**list[SignerInputs]**](SignerInputs.md) |  | [optional] 
**use_stamp_for_approve_only** | **bool** | Place an approval stamp on a document when a signer approves a document | [optional] 
**embed_url** | **str** |  | [optional] 
**attachments** | [**list[SignerAttachment]**](SignerAttachment.md) |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**redirect_url_declined** | **str** |  | [optional] 
**after_document** | **str** |  | [optional] 
**integrations** | [**list[InlineDocumentSignerIntegrationData]**](InlineDocumentSignerIntegrationData.md) |  | [optional] 
**password** | **str** | Require the signer to enter this password before signing a document. This field is write only. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


