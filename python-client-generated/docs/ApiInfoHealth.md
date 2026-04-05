# ApiInfoHealth

Detailed health status of system components. Only present when status is DEGRADED.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | [**ComponentHealth**](ComponentHealth.md) |  | [optional] 
**redis** | [**ComponentHealth**](ComponentHealth.md) |  | [optional] 

## Example

```python
from tmi_client.models.api_info_health import ApiInfoHealth

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoHealth from a JSON string
api_info_health_instance = ApiInfoHealth.from_json(json)
# print the JSON string representation of the object
print(ApiInfoHealth.to_json())

# convert the object into a dict
api_info_health_dict = api_info_health_instance.to_dict()
# create an instance of ApiInfoHealth from a dict
api_info_health_from_dict = ApiInfoHealth.from_dict(api_info_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


