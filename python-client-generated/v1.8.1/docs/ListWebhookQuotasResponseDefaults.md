# ListWebhookQuotasResponseDefaults

Server default quota values applied when a user has no quota row

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_subscriptions** | **int** | Default max subscriptions limit | 
**max_events_per_minute** | **int** | Default max events-per-minute limit | 
**max_subscription_requests_per_minute** | **int** | Default max subscription requests-per-minute limit | 
**max_subscription_requests_per_day** | **int** | Default max subscription requests-per-day limit | 

## Example

```python
from tmi_client.models.list_webhook_quotas_response_defaults import ListWebhookQuotasResponseDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookQuotasResponseDefaults from a JSON string
list_webhook_quotas_response_defaults_instance = ListWebhookQuotasResponseDefaults.from_json(json)
# print the JSON string representation of the object
print(ListWebhookQuotasResponseDefaults.to_json())

# convert the object into a dict
list_webhook_quotas_response_defaults_dict = list_webhook_quotas_response_defaults_instance.to_dict()
# create an instance of ListWebhookQuotasResponseDefaults from a dict
list_webhook_quotas_response_defaults_from_dict = ListWebhookQuotasResponseDefaults.from_dict(list_webhook_quotas_response_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


