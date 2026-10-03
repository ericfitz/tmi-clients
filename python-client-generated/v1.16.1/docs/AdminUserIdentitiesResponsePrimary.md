# AdminUserIdentitiesResponsePrimary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Identity provider of the primary sign-in identity | 
**email** | **str** | Email on the user record | 
**name** | **str** | Display name on the user record | 

## Example

```python
from tmi_client.models.admin_user_identities_response_primary import AdminUserIdentitiesResponsePrimary

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserIdentitiesResponsePrimary from a JSON string
admin_user_identities_response_primary_instance = AdminUserIdentitiesResponsePrimary.from_json(json)
# print the JSON string representation of the object
print(AdminUserIdentitiesResponsePrimary.to_json())

# convert the object into a dict
admin_user_identities_response_primary_dict = admin_user_identities_response_primary_instance.to_dict()
# create an instance of AdminUserIdentitiesResponsePrimary from a dict
admin_user_identities_response_primary_from_dict = AdminUserIdentitiesResponsePrimary.from_dict(admin_user_identities_response_primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


