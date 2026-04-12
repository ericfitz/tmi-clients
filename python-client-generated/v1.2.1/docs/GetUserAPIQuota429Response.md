# GetUserAPIQuota429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message | 
**retry_after** | **int** | Seconds until rate limit resets | [optional] 

## Example

```python
from tmi_client.models.get_user_api_quota429_response import GetUserAPIQuota429Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserAPIQuota429Response from a JSON string
get_user_api_quota429_response_instance = GetUserAPIQuota429Response.from_json(json)
# print the JSON string representation of the object
print(GetUserAPIQuota429Response.to_json())

# convert the object into a dict
get_user_api_quota429_response_dict = get_user_api_quota429_response_instance.to_dict()
# create an instance of GetUserAPIQuota429Response from a dict
get_user_api_quota429_response_from_dict = GetUserAPIQuota429Response.from_dict(get_user_api_quota429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


