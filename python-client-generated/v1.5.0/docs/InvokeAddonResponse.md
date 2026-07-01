# InvokeAddonResponse

Response from addon invocation including delivery ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_id** | **UUID** | Delivery identifier for tracking | 
**status** | **str** | Current invocation status | 
**created_at** | **datetime** | Invocation creation timestamp | 

## Example

```python
from tmi_client.models.invoke_addon_response import InvokeAddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAddonResponse from a JSON string
invoke_addon_response_instance = InvokeAddonResponse.from_json(json)
# print the JSON string representation of the object
print(InvokeAddonResponse.to_json())

# convert the object into a dict
invoke_addon_response_dict = invoke_addon_response_instance.to_dict()
# create an instance of InvokeAddonResponse from a dict
invoke_addon_response_from_dict = InvokeAddonResponse.from_dict(invoke_addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


