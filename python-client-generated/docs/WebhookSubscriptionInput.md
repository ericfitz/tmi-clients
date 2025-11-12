# WebhookSubscriptionInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_model_id** | **str** | Optional threat model filter | [optional] 
**name** | **str** | Descriptive name for the subscription | 
**url** | **str** | Webhook endpoint URL (must be HTTPS) | 
**events** | **list[str]** | List of event types to subscribe to | 
**secret** | **str** | Optional HMAC secret for signing payloads (auto-generated if not provided) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

