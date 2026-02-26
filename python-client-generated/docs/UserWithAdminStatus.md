# UserWithAdminStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_admin** | **bool** | Whether the user has administrator privileges (computed dynamically based on Administrators group membership) | 
**is_security_reviewer** | **bool** | Whether the user is a security reviewer (computed dynamically based on Security Reviewers group membership) | 
**groups** | [**list[UserGroupMembership]**](UserGroupMembership.md) | TMI-managed groups that the user belongs to (direct membership only, excludes the implicit everyone pseudo-group) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

