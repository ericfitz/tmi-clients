# WebhookDelivery

Record of a webhook delivery attempt including status and response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier (UUIDv7) | 
**subscription_id** | **UUID** | Subscription that triggered this delivery | 
**event_type** | [**WebhookEventType**](WebhookEventType.md) |  | 
**payload** | **Dict[str, object]** | Event payload (JSON) | [optional] 
**status** | **str** | Delivery status | 
**attempts** | **int** | Number of delivery attempts | 
**next_retry_at** | **datetime** | Next retry timestamp | [optional] 
**last_error** | **str** | Last error message | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**delivered_at** | **datetime** | Successful delivery timestamp | [optional] 
**status_percent** | **int** | Progress percentage | [optional] 
**status_message** | **str** | Human-readable status description | [optional] 
**last_activity_at** | **datetime** | Last status update or delivery attempt | [optional] 
**addon_id** | **UUID** | Add-on ID (for addon invocations only) | [optional] 
**invoked_by** | [**User**](User.md) | User who invoked the add-on (for addon invocations only) | [optional] 

## Example

```python
from tmi_client.models.webhook_delivery import WebhookDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelivery from a JSON string
webhook_delivery_instance = WebhookDelivery.from_json(json)
# print the JSON string representation of the object
print(WebhookDelivery.to_json())

# convert the object into a dict
webhook_delivery_dict = webhook_delivery_instance.to_dict()
# create an instance of WebhookDelivery from a dict
webhook_delivery_from_dict = WebhookDelivery.from_dict(webhook_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


