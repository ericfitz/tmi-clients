# GetProviderGroups200ResponseGroupsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group name | 
**display_name** | **str** | Display name for the group | [optional] 
**used_in_authorizations** | **bool** | Whether this group is used in any threat model authorizations | [optional] 

## Example

```python
from tmi_client.models.get_provider_groups200_response_groups_inner import GetProviderGroups200ResponseGroupsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetProviderGroups200ResponseGroupsInner from a JSON string
get_provider_groups200_response_groups_inner_instance = GetProviderGroups200ResponseGroupsInner.from_json(json)
# print the JSON string representation of the object
print(GetProviderGroups200ResponseGroupsInner.to_json())

# convert the object into a dict
get_provider_groups200_response_groups_inner_dict = get_provider_groups200_response_groups_inner_instance.to_dict()
# create an instance of GetProviderGroups200ResponseGroupsInner from a dict
get_provider_groups200_response_groups_inner_from_dict = GetProviderGroups200ResponseGroupsInner.from_dict(get_provider_groups200_response_groups_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


