# WebhookQuotaUpdate

Configuration update for webhook subscription quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_subscriptions** | **int** | Maximum webhook subscriptions | 
**max_events_per_minute** | **int** | Maximum webhook events per minute | 
**max_subscription_requests_per_minute** | **int** | Maximum subscription requests per minute | 
**max_subscription_requests_per_day** | **int** | Maximum subscription requests per day | 

## Example

```python
from tmi_client.models.webhook_quota_update import WebhookQuotaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookQuotaUpdate from a JSON string
webhook_quota_update_instance = WebhookQuotaUpdate.from_json(json)
# print the JSON string representation of the object
print(WebhookQuotaUpdate.to_json())

# convert the object into a dict
webhook_quota_update_dict = webhook_quota_update_instance.to_dict()
# create an instance of WebhookQuotaUpdate from a dict
webhook_quota_update_from_dict = WebhookQuotaUpdate.from_dict(webhook_quota_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


