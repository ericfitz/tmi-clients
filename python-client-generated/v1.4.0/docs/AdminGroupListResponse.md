# AdminGroupListResponse

Paginated list of groups for administrative management

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[AdminGroup]**](AdminGroup.md) | List of groups | 
**total** | **int** | Total number of groups matching the filter | 
**limit** | **int** | Maximum number of results returned | 
**offset** | **int** | Number of results skipped | 

## Example

```python
from tmi_client.models.admin_group_list_response import AdminGroupListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGroupListResponse from a JSON string
admin_group_list_response_instance = AdminGroupListResponse.from_json(json)
# print the JSON string representation of the object
print(AdminGroupListResponse.to_json())

# convert the object into a dict
admin_group_list_response_dict = admin_group_list_response_instance.to_dict()
# create an instance of AdminGroupListResponse from a dict
admin_group_list_response_from_dict = AdminGroupListResponse.from_dict(admin_group_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


