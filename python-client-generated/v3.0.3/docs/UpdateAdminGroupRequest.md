# UpdateAdminGroupRequest

Request body for updating group metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated human-readable group name | [optional] 
**description** | **str** | Updated group description | [optional] 

## Example

```python
from tmi_client.models.update_admin_group_request import UpdateAdminGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminGroupRequest from a JSON string
update_admin_group_request_instance = UpdateAdminGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminGroupRequest.to_json())

# convert the object into a dict
update_admin_group_request_dict = update_admin_group_request_instance.to_dict()
# create an instance of UpdateAdminGroupRequest from a dict
update_admin_group_request_from_dict = UpdateAdminGroupRequest.from_dict(update_admin_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


