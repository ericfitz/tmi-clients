# WebhookDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier (UUIDv7) | [default to null]
**SubscriptionId** | **string** | Subscription that triggered this delivery | [default to null]
**EventType** | [***WebhookEventType**](WebhookEventType.md) |  | [default to null]
**Payload** | [***interface{}**](interface{}.md) | Event payload (JSON) | [optional] [default to null]
**Status** | **string** | Delivery status | [default to null]
**Attempts** | **int32** | Number of delivery attempts | [default to null]
**NextRetryAt** | [**time.Time**](time.Time.md) | Next retry timestamp | [optional] [default to null]
**LastError** | **string** | Last error message | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp | [default to null]
**DeliveredAt** | [**time.Time**](time.Time.md) | Successful delivery timestamp | [optional] [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

