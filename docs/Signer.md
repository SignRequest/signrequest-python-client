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
**needs_to_sign** | **bool** | When &#x60;false&#x60; user does not need to sign, but will receive a copy of the signed document and signing log, see: [Copy only](#section/Additional-signing-methods/Copy-only) | [optional] [default to True]
**approve_only** | **bool** | Require user to approve the document (without adding a signature), see: [Approve only](#section/Additional-signing-methods/Approve-only) | [optional] 
**notify_only** | **bool** | Send notifications about the document and a copy of the signed document and signing log, but don&#39;t require them to take any action, see: [Notify only](#section/Additional-signing-methods/Notify-only) | [optional] 
**in_person** | **bool** | When used in combination with an embed url on the sender, after sender has signed, they will be redirected to the next &#x60;in_person&#x60; signer, see: [In person signing](#section/Additional-signing-methods/In-person-signing) | [optional] 
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


