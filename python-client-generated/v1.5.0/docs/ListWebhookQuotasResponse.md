# ListWebhookQuotasResponse

Paginated list of webhook quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**List[WebhookQuota]**](WebhookQuota.md) |  | 
**total** | **int** | Total number of quotas matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_webhook_quotas_response import ListWebhookQuotasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookQuotasResponse from a JSON string
list_webhook_quotas_response_instance = ListWebhookQuotasResponse.from_json(json)
# print the JSON string representation of the object
print(ListWebhookQuotasResponse.to_json())

# convert the object into a dict
list_webhook_quotas_response_dict = list_webhook_quotas_response_instance.to_dict()
# create an instance of ListWebhookQuotasResponse from a dict
list_webhook_quotas_response_from_dict = ListWebhookQuotasResponse.from_dict(list_webhook_quotas_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


