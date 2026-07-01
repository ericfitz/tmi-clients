# ComponentHealth

Health status of a system component

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Component health status | 
**latency_ms** | **int** | Response latency in milliseconds | [optional] 
**message** | **str** | Human-readable status message or error description | [optional] 

## Example

```python
from tmi_client.models.component_health import ComponentHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentHealth from a JSON string
component_health_instance = ComponentHealth.from_json(json)
# print the JSON string representation of the object
print(ComponentHealth.to_json())

# convert the object into a dict
component_health_dict = component_health_instance.to_dict()
# create an instance of ComponentHealth from a dict
component_health_from_dict = ComponentHealth.from_dict(component_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


