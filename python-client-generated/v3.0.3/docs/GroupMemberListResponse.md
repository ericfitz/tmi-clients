# GroupMemberListResponse

List of members in a group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[GroupMember]**](GroupMember.md) |  | 
**total** | **int** | Total number of members in the group | 
**limit** | **int** | Maximum number of results per page | 
**offset** | **int** | Number of results skipped | 

## Example

```python
from tmi_client.models.group_member_list_response import GroupMemberListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberListResponse from a JSON string
group_member_list_response_instance = GroupMemberListResponse.from_json(json)
# print the JSON string representation of the object
print(GroupMemberListResponse.to_json())

# convert the object into a dict
group_member_list_response_dict = group_member_list_response_instance.to_dict()
# create an instance of GroupMemberListResponse from a dict
group_member_list_response_from_dict = GroupMemberListResponse.from_dict(group_member_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


