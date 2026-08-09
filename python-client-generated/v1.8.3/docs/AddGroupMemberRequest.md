# AddGroupMemberRequest

Request to add a user or group to a group. Provide user_internal_uuid for user members or member_group_internal_uuid for group members.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_internal_uuid** | **UUID** | Internal UUID of the user to add to the group | [optional] 
**notes** | **str** | Optional notes about this membership | [optional] 
**subject_type** | **str** | Type of member to add: user or group | [optional] [default to 'user']
**member_group_internal_uuid** | **UUID** | Internal UUID of the group to add as a member (required when subject_type is group) | [optional] 

## Example

```python
from tmi_client.models.add_group_member_request import AddGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupMemberRequest from a JSON string
add_group_member_request_instance = AddGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupMemberRequest.to_json())

# convert the object into a dict
add_group_member_request_dict = add_group_member_request_instance.to_dict()
# create an instance of AddGroupMemberRequest from a dict
add_group_member_request_from_dict = AddGroupMemberRequest.from_dict(add_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


