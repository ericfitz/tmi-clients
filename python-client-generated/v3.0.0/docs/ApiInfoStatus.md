# ApiInfoStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Status code indicating system health: OK (all components healthy), DEGRADED (server up but database or Redis unhealthy), ERROR (critical failure) | 
**time** | **datetime** | Current server time in UTC, formatted as RFC 3339 | 

## Example

```python
from tmi_client.models.api_info_status import ApiInfoStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoStatus from a JSON string
api_info_status_instance = ApiInfoStatus.from_json(json)
# print the JSON string representation of the object
print(ApiInfoStatus.to_json())

# convert the object into a dict
api_info_status_dict = api_info_status_instance.to_dict()
# create an instance of ApiInfoStatus from a dict
api_info_status_from_dict = ApiInfoStatus.from_dict(api_info_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


