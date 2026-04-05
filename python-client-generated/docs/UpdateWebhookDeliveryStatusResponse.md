# UpdateWebhookDeliveryStatusResponse

Response confirming webhook delivery status update

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**status** | **str** |  | 
**status_percent** | **int** |  | 
**status_updated_at** | **datetime** |  | 

## Example

```python
from tmi_client.models.update_webhook_delivery_status_response import UpdateWebhookDeliveryStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhookDeliveryStatusResponse from a JSON string
update_webhook_delivery_status_response_instance = UpdateWebhookDeliveryStatusResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhookDeliveryStatusResponse.to_json())

# convert the object into a dict
update_webhook_delivery_status_response_dict = update_webhook_delivery_status_response_instance.to_dict()
# create an instance of UpdateWebhookDeliveryStatusResponse from a dict
update_webhook_delivery_status_response_from_dict = UpdateWebhookDeliveryStatusResponse.from_dict(update_webhook_delivery_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


