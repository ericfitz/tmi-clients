# AdminUserListResponse

Paginated list of users for administrative management

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[AdminUser]**](AdminUser.md) | List of users | 
**total** | **int** | Total number of users matching the filter | 
**limit** | **int** | Maximum number of results returned | 
**offset** | **int** | Number of results skipped | 

## Example

```python
from tmi_client.models.admin_user_list_response import AdminUserListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserListResponse from a JSON string
admin_user_list_response_instance = AdminUserListResponse.from_json(json)
# print the JSON string representation of the object
print(AdminUserListResponse.to_json())

# convert the object into a dict
admin_user_list_response_dict = admin_user_list_response_instance.to_dict()
# create an instance of AdminUserListResponse from a dict
admin_user_list_response_from_dict = AdminUserListResponse.from_dict(admin_user_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


