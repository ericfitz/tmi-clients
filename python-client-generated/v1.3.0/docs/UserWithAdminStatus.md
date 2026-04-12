# UserWithAdminStatus

User profile with role status and group memberships (only returned by GET /me)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** | Always \&quot;user\&quot; for User objects | 
**provider** | **str** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;*\&quot; for provider-independent groups. | 
**provider_id** | **str** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**display_name** | **str** | User full name for display | 
**email** | **str** | User email address (required) | 
**is_admin** | **bool** | Whether the user has administrator privileges (computed dynamically based on Administrators group membership) | 
**is_security_reviewer** | **bool** | Whether the user is a security reviewer (computed dynamically based on Security Reviewers group membership) | 
**groups** | [**List[UserGroupMembership]**](UserGroupMembership.md) | TMI-managed groups that the user belongs to (direct membership only, excludes the implicit everyone pseudo-group) | 

## Example

```python
from tmi_client.models.user_with_admin_status import UserWithAdminStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UserWithAdminStatus from a JSON string
user_with_admin_status_instance = UserWithAdminStatus.from_json(json)
# print the JSON string representation of the object
print(UserWithAdminStatus.to_json())

# convert the object into a dict
user_with_admin_status_dict = user_with_admin_status_instance.to_dict()
# create an instance of UserWithAdminStatus from a dict
user_with_admin_status_from_dict = UserWithAdminStatus.from_dict(user_with_admin_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


