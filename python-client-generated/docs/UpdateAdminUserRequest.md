# UpdateAdminUserRequest

Request body for updating user metadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Updated email address | [optional] 
**name** | **str** | Updated display name | [optional] 
**email_verified** | **bool** | Updated email verification status | [optional] 

## Example

```python
from tmi_client.models.update_admin_user_request import UpdateAdminUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdminUserRequest from a JSON string
update_admin_user_request_instance = UpdateAdminUserRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAdminUserRequest.to_json())

# convert the object into a dict
update_admin_user_request_dict = update_admin_user_request_instance.to_dict()
# create an instance of UpdateAdminUserRequest from a dict
update_admin_user_request_from_dict = UpdateAdminUserRequest.from_dict(update_admin_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


