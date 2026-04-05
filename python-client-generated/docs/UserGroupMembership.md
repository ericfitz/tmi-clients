# UserGroupMembership

TMI-managed group that a user belongs to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_uuid** | **UUID** | Group internal UUID | 
**group_name** | **str** | Group name (e.g. administrators, security-reviewers) | 
**name** | **str** | Display name for the group | [optional] 

## Example

```python
from tmi_client.models.user_group_membership import UserGroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupMembership from a JSON string
user_group_membership_instance = UserGroupMembership.from_json(json)
# print the JSON string representation of the object
print(UserGroupMembership.to_json())

# convert the object into a dict
user_group_membership_dict = user_group_membership_instance.to_dict()
# create an instance of UserGroupMembership from a dict
user_group_membership_from_dict = UserGroupMembership.from_dict(user_group_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


