# TmiJsClient.UserWithAdminStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isAdmin** | **Boolean** | Whether the user has administrator privileges (computed dynamically based on Administrators group membership) | 
**isSecurityReviewer** | **Boolean** | Whether the user is a security reviewer (computed dynamically based on Security Reviewers group membership) | 
**groups** | [**[UserGroupMembership]**](UserGroupMembership.md) | TMI-managed groups that the user belongs to (direct membership only, excludes the implicit everyone pseudo-group) | 
