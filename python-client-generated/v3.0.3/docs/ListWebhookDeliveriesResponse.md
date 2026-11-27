# ListWebhookDeliveriesResponse

Paginated list of webhook deliveries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deliveries** | [**List[WebhookDelivery]**](WebhookDelivery.md) |  | 
**total** | **int** | Total number of deliveries matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_webhook_deliveries_response import ListWebhookDeliveriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListWebhookDeliveriesResponse from a JSON string
list_webhook_deliveries_response_instance = ListWebhookDeliveriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListWebhookDeliveriesResponse.to_json())

# convert the object into a dict
list_webhook_deliveries_response_dict = list_webhook_deliveries_response_instance.to_dict()
# create an instance of ListWebhookDeliveriesResponse from a dict
list_webhook_deliveries_response_from_dict = ListWebhookDeliveriesResponse.from_dict(list_webhook_deliveries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


