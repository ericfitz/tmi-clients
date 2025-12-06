# WebhookDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier (UUIDv7) | 
**subscription_id** | **str** | Subscription that triggered this delivery | 
**event_type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**payload** | **object** | Event payload (JSON) | [optional] 
**status** | **str** | Delivery status | 
**attempts** | **int** | Number of delivery attempts | 
**next_retry_at** | **datetime** | Next retry timestamp | [optional] 
**last_error** | **str** | Last error message | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**delivered_at** | **datetime** | Successful delivery timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

