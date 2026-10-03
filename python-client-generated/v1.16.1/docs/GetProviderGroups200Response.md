# GetProviderGroups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idp** | **str** | Identity provider ID | 
**groups** | [**List[GetProviderGroups200ResponseGroupsInner]**](GetProviderGroups200ResponseGroupsInner.md) |  | 

## Example

```python
from tmi_client.models.get_provider_groups200_response import GetProviderGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProviderGroups200Response from a JSON string
get_provider_groups200_response_instance = GetProviderGroups200Response.from_json(json)
# print the JSON string representation of the object
print(GetProviderGroups200Response.to_json())

# convert the object into a dict
get_provider_groups200_response_dict = get_provider_groups200_response_instance.to_dict()
# create an instance of GetProviderGroups200Response from a dict
get_provider_groups200_response_from_dict = GetProviderGroups200Response.from_dict(get_provider_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


