# WebhookSubscriptionInput

Input schema for creating or updating a webhook subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_model_id** | **UUID** | Optional threat model filter | [optional] 
**name** | **str** | Descriptive name for the subscription | 
**url** | **str** | Webhook endpoint URL (must be HTTPS) | 
**events** | **List[str]** | List of event types to subscribe to | 
**secret** | **str** | Optional HMAC secret for signing payloads (auto-generated if not provided) | [optional] 

## Example

```python
from tmi_client.models.webhook_subscription_input import WebhookSubscriptionInput

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSubscriptionInput from a JSON string
webhook_subscription_input_instance = WebhookSubscriptionInput.from_json(json)
# print the JSON string representation of the object
print(WebhookSubscriptionInput.to_json())

# convert the object into a dict
webhook_subscription_input_dict = webhook_subscription_input_instance.to_dict()
# create an instance of WebhookSubscriptionInput from a dict
webhook_subscription_input_from_dict = WebhookSubscriptionInput.from_dict(webhook_subscription_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


