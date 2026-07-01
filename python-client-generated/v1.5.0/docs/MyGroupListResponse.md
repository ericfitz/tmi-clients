# MyGroupListResponse

List of TMI-managed groups that the authenticated user belongs to

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[UserGroupMembership]**](UserGroupMembership.md) | List of groups the user is a direct member of | 
**total** | **int** | Total number of groups | 

## Example

```python
from tmi_client.models.my_group_list_response import MyGroupListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MyGroupListResponse from a JSON string
my_group_list_response_instance = MyGroupListResponse.from_json(json)
# print the JSON string representation of the object
print(MyGroupListResponse.to_json())

# convert the object into a dict
my_group_list_response_dict = my_group_list_response_instance.to_dict()
# create an instance of MyGroupListResponse from a dict
my_group_list_response_from_dict = MyGroupListResponse.from_dict(my_group_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


