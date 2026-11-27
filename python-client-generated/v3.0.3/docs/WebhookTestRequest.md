# WebhookTestRequest

Request to test a webhook subscription with a sample event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** | Webhook event type following {resource}.{action} pattern | [optional] 

## Example

```python
from tmi_client.models.webhook_test_request import WebhookTestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTestRequest from a JSON string
webhook_test_request_instance = WebhookTestRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookTestRequest.to_json())

# convert the object into a dict
webhook_test_request_dict = webhook_test_request_instance.to_dict()
# create an instance of WebhookTestRequest from a dict
webhook_test_request_from_dict = WebhookTestRequest.from_dict(webhook_test_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


