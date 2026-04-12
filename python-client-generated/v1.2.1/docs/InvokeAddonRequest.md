# InvokeAddonRequest

Request to invoke an addon with parameters and payload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_model_id** | **UUID** | Threat model context for invocation | 
**object_type** | **str** | Optional: Specific object type to operate on | [optional] 
**object_id** | **UUID** | Optional: Specific object ID to operate on | [optional] 
**payload** | **Dict[str, object]** | User-provided data for the add-on (max 1KB JSON-serialized) | [optional] 

## Example

```python
from tmi_client.models.invoke_addon_request import InvokeAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeAddonRequest from a JSON string
invoke_addon_request_instance = InvokeAddonRequest.from_json(json)
# print the JSON string representation of the object
print(InvokeAddonRequest.to_json())

# convert the object into a dict
invoke_addon_request_dict = invoke_addon_request_instance.to_dict()
# create an instance of InvokeAddonRequest from a dict
invoke_addon_request_from_dict = InvokeAddonRequest.from_dict(invoke_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


