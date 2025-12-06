# WebhookSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier | 
**owner_id** | **str** | Owner user ID | 
**threat_model_id** | **str** | Optional threat model filter (null means all threat models) | [optional] 
**name** | **str** | Descriptive name | 
**url** | **str** | Webhook endpoint URL (must be HTTPS) | 
**events** | [**list[WebhookEventType]**](WebhookEventType.md) | List of event types to subscribe to. See WebhookEventType for available events. | 
**secret** | **str** | HMAC secret for signing payloads (not returned in GET responses) | [optional] 
**status** | **str** | Subscription status | 
**challenges_sent** | **int** | Number of verification challenges sent | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 
**last_successful_use** | **datetime** | Last successful delivery timestamp | [optional] 
**publication_failures** | **int** | Count of consecutive failed deliveries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

