# TmiJsClient.WebhookDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Unique identifier (UUIDv7) | 
**subscriptionId** | **String** | Subscription that triggered this delivery | 
**eventType** | [**WebhookEventType**](WebhookEventType.md) |  | 
**payload** | **Object** | Event payload (JSON) | [optional] 
**status** | **String** | Delivery status | 
**attempts** | **Number** | Number of delivery attempts | 
**nextRetryAt** | **Date** | Next retry timestamp | [optional] 
**lastError** | **String** | Last error message | [optional] 
**createdAt** | **Date** | Creation timestamp | 
**deliveredAt** | **Date** | Successful delivery timestamp | [optional] 

<a name="StatusEnum"></a>
## Enum: StatusEnum

* `pending` (value: `"pending"`)
* `delivered` (value: `"delivered"`)
* `failed` (value: `"failed"`)

