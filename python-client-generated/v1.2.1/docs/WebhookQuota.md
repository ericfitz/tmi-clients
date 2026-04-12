# WebhookQuota

Webhook subscription quota configuration for a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **UUID** | Owner ID | 
**max_subscriptions** | **int** | Maximum number of webhook subscriptions | 
**max_events_per_minute** | **int** | Maximum webhook events per minute | 
**max_subscription_requests_per_minute** | **int** | Maximum subscription requests per minute | 
**max_subscription_requests_per_day** | **int** | Maximum subscription requests per day | 
**created_at** | **datetime** | Timestamp when the quota was created | [optional] 
**modified_at** | **datetime** | Timestamp when the quota was last modified | [optional] 

## Example

```python
from tmi_client.models.webhook_quota import WebhookQuota

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookQuota from a JSON string
webhook_quota_instance = WebhookQuota.from_json(json)
# print the JSON string representation of the object
print(WebhookQuota.to_json())

# convert the object into a dict
webhook_quota_dict = webhook_quota_instance.to_dict()
# create an instance of WebhookQuota from a dict
webhook_quota_from_dict = WebhookQuota.from_dict(webhook_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


