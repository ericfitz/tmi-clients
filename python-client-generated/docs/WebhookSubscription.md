# WebhookSubscription

Webhook subscription configuration for event notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier | 
**owner_id** | **UUID** | Owner user ID | 
**threat_model_id** | **UUID** | Optional threat model filter (null means all threat models) | [optional] 
**name** | **str** | Descriptive name | 
**url** | **str** | Webhook endpoint URL (must be HTTPS) | 
**events** | [**List[WebhookEventType]**](WebhookEventType.md) | List of event types to subscribe to. See WebhookEventType for available events. | 
**secret** | **str** | HMAC secret for signing payloads (not returned in GET responses) | [optional] 
**status** | **str** | Subscription status | 
**challenges_sent** | **int** | Number of verification challenges sent | [optional] 
**created_at** | **datetime** | Creation timestamp | 
**modified_at** | **datetime** | Last modification timestamp | 
**last_successful_use** | **datetime** | Last successful delivery timestamp | [optional] 
**publication_failures** | **int** | Count of consecutive failed deliveries | [optional] 

## Example

```python
from tmi_client.models.webhook_subscription import WebhookSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscription from a JSON string
webhook_subscription_instance = WebhookSubscription.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscription.to_json())

# convert the object into a dict
webhook_subscription_dict = webhook_subscription_instance.to_dict()
# create an instance of WebhookSubscription from a dict
webhook_subscription_from_dict = WebhookSubscription.from_dict(webhook_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


