# CreateAdminGroupRequest

Request body for creating a provider-independent group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** | Group identifier (alphanumeric, hyphens, underscores only) | 
**name** | **str** | Human-readable group name | 
**description** | **str** | Optional group description | [optional] 

## Example

```python
from tmi_client.models.create_admin_group_request import CreateAdminGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdminGroupRequest from a JSON string
create_admin_group_request_instance = CreateAdminGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAdminGroupRequest.to_json())

# convert the object into a dict
create_admin_group_request_dict = create_admin_group_request_instance.to_dict()
# create an instance of CreateAdminGroupRequest from a dict
create_admin_group_request_from_dict = CreateAdminGroupRequest.from_dict(create_admin_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


