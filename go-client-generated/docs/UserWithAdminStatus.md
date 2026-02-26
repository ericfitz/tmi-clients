# UserWithAdminStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IsAdmin** | **bool** | Whether the user has administrator privileges (computed dynamically based on Administrators group membership) | [default to null]
**IsSecurityReviewer** | **bool** | Whether the user is a security reviewer (computed dynamically based on Security Reviewers group membership) | [default to null]
**Groups** | [**[]UserGroupMembership**](UserGroupMembership.md) | TMI-managed groups that the user belongs to (direct membership only, excludes the implicit everyone pseudo-group) | [default to null]
**PrincipalType** | **string** | Always \&quot;user\&quot; for User objects | [optional] [default to null]
**Email** | **string** | User email address (required) | [default to null]
**DisplayName** | **string** | User full name for display | [default to null]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

