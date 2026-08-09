# AdminUserIdentitiesResponse

A user's primary sign-in identity plus any linked identities, as seen by an administrator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**AdminUserIdentitiesResponsePrimary**](AdminUserIdentitiesResponsePrimary.md) |  | 
**linked** | [**List[LinkedIdentity]**](LinkedIdentity.md) | Linked sign-in identities; the primary identity is not deletable and does not appear here | [optional] 

## Example

```python
from tmi_client.models.admin_user_identities_response import AdminUserIdentitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserIdentitiesResponse from a JSON string
admin_user_identities_response_instance = AdminUserIdentitiesResponse.from_json(json)
# print the JSON string representation of the object
print(AdminUserIdentitiesResponse.to_json())

# convert the object into a dict
admin_user_identities_response_dict = admin_user_identities_response_instance.to_dict()
# create an instance of AdminUserIdentitiesResponse from a dict
admin_user_identities_response_from_dict = AdminUserIdentitiesResponse.from_dict(admin_user_identities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


