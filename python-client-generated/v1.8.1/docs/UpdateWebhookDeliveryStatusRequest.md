# UpdateWebhookDeliveryStatusRequest

Request to update the status of a webhook delivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | New delivery status | 
**status_percent** | **int** | Progress percentage (0-100) | [optional] 
**status_message** | **str** | Human-readable status description | [optional] 

## Example

```python
from tmi_client.models.update_webhook_delivery_status_request import UpdateWebhookDeliveryStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookDeliveryStatusRequest from a JSON string
update_webhook_delivery_status_request_instance = UpdateWebhookDeliveryStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookDeliveryStatusRequest.to_json())

# convert the object into a dict
update_webhook_delivery_status_request_dict = update_webhook_delivery_status_request_instance.to_dict()
# create an instance of UpdateWebhookDeliveryStatusRequest from a dict
update_webhook_delivery_status_request_from_dict = UpdateWebhookDeliveryStatusRequest.from_dict(update_webhook_delivery_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


