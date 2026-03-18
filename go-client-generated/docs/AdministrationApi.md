# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddGroupMember**](AdministrationApi.md#AddGroupMember) | **Post** /admin/groups/{internal_uuid}/members | Add member to group
[**CreateAdminGroup**](AdministrationApi.md#CreateAdminGroup) | **Post** /admin/groups | Create provider-independent group
[**DeleteAddonInvocationQuota**](AdministrationApi.md#DeleteAddonInvocationQuota) | **Delete** /admin/quotas/addons/{user_id} | Delete addon invocation quota
[**DeleteAdminGroup**](AdministrationApi.md#DeleteAdminGroup) | **Delete** /admin/groups/{internal_uuid} | Delete group
[**DeleteAdminUser**](AdministrationApi.md#DeleteAdminUser) | **Delete** /admin/users/{internal_uuid} | Delete user
[**DeleteSystemSetting**](AdministrationApi.md#DeleteSystemSetting) | **Delete** /admin/settings/{key} | Delete system setting
[**DeleteUserAPIQuota**](AdministrationApi.md#DeleteUserAPIQuota) | **Delete** /admin/quotas/users/{user_id} | Delete user API quota
[**DeleteWebhookQuota**](AdministrationApi.md#DeleteWebhookQuota) | **Delete** /admin/quotas/webhooks/{user_id} | Delete webhook quota
[**GetAddonInvocationQuota**](AdministrationApi.md#GetAddonInvocationQuota) | **Get** /admin/quotas/addons/{user_id} | Get addon invocation quota
[**GetAdminGroup**](AdministrationApi.md#GetAdminGroup) | **Get** /admin/groups/{internal_uuid} | Get group details
[**GetAdminUser**](AdministrationApi.md#GetAdminUser) | **Get** /admin/users/{internal_uuid} | Get user details
[**GetSystemSetting**](AdministrationApi.md#GetSystemSetting) | **Get** /admin/settings/{key} | Get system setting
[**GetUserAPIQuota**](AdministrationApi.md#GetUserAPIQuota) | **Get** /admin/quotas/users/{user_id} | Get user API quota
[**GetWebhookQuota**](AdministrationApi.md#GetWebhookQuota) | **Get** /admin/quotas/webhooks/{user_id} | Get webhook quota
[**ListAddonInvocationQuotas**](AdministrationApi.md#ListAddonInvocationQuotas) | **Get** /admin/quotas/addons | List all addon invocation quotas
[**ListAdminGroups**](AdministrationApi.md#ListAdminGroups) | **Get** /admin/groups | List groups
[**ListAdminUsers**](AdministrationApi.md#ListAdminUsers) | **Get** /admin/users | List users
[**ListGroupMembers**](AdministrationApi.md#ListGroupMembers) | **Get** /admin/groups/{internal_uuid}/members | List group members
[**ListSystemSettings**](AdministrationApi.md#ListSystemSettings) | **Get** /admin/settings | List system settings
[**ListUserAPIQuotas**](AdministrationApi.md#ListUserAPIQuotas) | **Get** /admin/quotas/users | List all user API quotas
[**ListWebhookQuotas**](AdministrationApi.md#ListWebhookQuotas) | **Get** /admin/quotas/webhooks | List all webhook quotas
[**MigrateSystemSettings**](AdministrationApi.md#MigrateSystemSettings) | **Post** /admin/settings/migrate | Migrate settings from configuration
[**ReencryptSystemSettings**](AdministrationApi.md#ReencryptSystemSettings) | **Post** /admin/settings/reencrypt | Re-encrypt all system settings
[**RemoveGroupMember**](AdministrationApi.md#RemoveGroupMember) | **Delete** /admin/groups/{internal_uuid}/members/{member_uuid} | Remove member from group
[**TransferAdminUserOwnership**](AdministrationApi.md#TransferAdminUserOwnership) | **Post** /admin/users/{internal_uuid}/transfer | Transfer user ownership to another user
[**UpdateAddonInvocationQuota**](AdministrationApi.md#UpdateAddonInvocationQuota) | **Put** /admin/quotas/addons/{user_id} | Update addon invocation quota
[**UpdateAdminGroup**](AdministrationApi.md#UpdateAdminGroup) | **Patch** /admin/groups/{internal_uuid} | Update group metadata
[**UpdateAdminUser**](AdministrationApi.md#UpdateAdminUser) | **Patch** /admin/users/{internal_uuid} | Update user metadata
[**UpdateSystemSetting**](AdministrationApi.md#UpdateSystemSetting) | **Put** /admin/settings/{key} | Update system setting
[**UpdateUserAPIQuota**](AdministrationApi.md#UpdateUserAPIQuota) | **Put** /admin/quotas/users/{user_id} | Update user API quota
[**UpdateWebhookQuota**](AdministrationApi.md#UpdateWebhookQuota) | **Put** /admin/quotas/webhooks/{user_id} | Update webhook quota

# **AddGroupMember**
> GroupMember AddGroupMember(ctx, body, internalUuid)
Add member to group

Adds a user to a group. The user must exist in the system. Cannot add members to the special 'everyone' pseudo-group.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md)| Group membership update | 
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateAdminGroup**
> AdminGroup CreateAdminGroup(ctx, body)
Create provider-independent group

Creates a new provider-independent group (provider=\"*\"). These groups can be used across all providers for authorization and administration.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateAdminGroupRequest**](CreateAdminGroupRequest.md)| Group creation request | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAddonInvocationQuota**
> DeleteAddonInvocationQuota(ctx, userId)
Delete addon invocation quota

Deletes the custom addon invocation quota for a user, reverting to system defaults

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAdminGroup**
> DeleteAdminGroup(ctx, internalUuid)
Delete group

Deletes a TMI-managed group and handles threat model cleanup. Protected groups like 'everyone' cannot be deleted.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAdminUser**
> DeleteAdminUser(ctx, internalUuid)
Delete user

Deletes a user and all associated data. Transfers sole-owned threat models or deletes them if no other owners exist.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteSystemSetting**
> DeleteSystemSetting(ctx, key)
Delete system setting

Deletes a system setting. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **key** | **string**| The setting key | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteUserAPIQuota**
> DeleteUserAPIQuota(ctx, userId)
Delete user API quota

Deletes the custom API quota for a user, reverting to system defaults

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteWebhookQuota**
> DeleteWebhookQuota(ctx, userId)
Delete webhook quota

Deletes the custom webhook quota for a user, reverting to system defaults

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAddonInvocationQuota**
> AddonInvocationQuota GetAddonInvocationQuota(ctx, userId)
Get addon invocation quota

Retrieves the addon invocation quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminGroup**
> AdminGroup GetAdminGroup(ctx, internalUuid)
Get group details

Returns detailed information about a specific group, including enriched data (usage in authorizations and admin grants).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetAdminUser**
> AdminUser GetAdminUser(ctx, internalUuid)
Get user details

Returns detailed information about a specific user, including enriched data (admin status, groups, threat model counts).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetSystemSetting**
> SystemSetting GetSystemSetting(ctx, key)
Get system setting

Returns a specific system setting by key. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **key** | **string**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetUserAPIQuota**
> UserApiQuota GetUserAPIQuota(ctx, userId)
Get user API quota

Retrieves the API rate limit quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

[**UserApiQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **GetWebhookQuota**
> WebhookQuota GetWebhookQuota(ctx, userId)
Get webhook quota

Retrieves the webhook quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **userId** | [**string**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAddonInvocationQuotas**
> ListAddonQuotasResponse ListAddonInvocationQuotas(ctx, optional)
List all addon invocation quotas

Retrieves all custom addon invocation quotas (users with non-default quotas)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiListAddonInvocationQuotasOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListAddonInvocationQuotasOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListAddonQuotasResponse**](ListAddonQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAdminGroups**
> AdminGroupListResponse ListAdminGroups(ctx, optional)
List groups

Returns a paginated list of groups with optional filtering by provider, name, and usage. Includes enriched data (usage in authorizations and admin grants).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiListAdminGroupsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListAdminGroupsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **optional.String**| Filter by OAuth/SAML provider | 
 **groupName** | **optional.String**| Filter by group name (case-insensitive substring match) | 
 **usedInAuthorizations** | **optional.Bool**| Filter groups used (true) or not used (false) in authorizations | 
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **sortBy** | **optional.String**| Field to sort by | [default to created_at]
 **sortOrder** | **optional.String**| Sort direction | [default to desc]

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAdminUsers**
> AdminUserListResponse ListAdminUsers(ctx, optional)
List users

Returns a paginated list of users with optional filtering by provider, email, and date ranges. Includes enriched data (admin status, groups, threat model counts).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiListAdminUsersOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListAdminUsersOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **optional.String**| Filter by OAuth/SAML provider | 
 **email** | **optional.String**| Filter by email (case-insensitive substring match) | 
 **createdAfter** | **optional.Time**| Filter users created after this timestamp (RFC3339) | 
 **createdBefore** | **optional.Time**| Filter users created before this timestamp (RFC3339) | 
 **lastLoginAfter** | **optional.Time**| Filter users who logged in after this timestamp (RFC3339) | 
 **lastLoginBefore** | **optional.Time**| Filter users who logged in before this timestamp (RFC3339) | 
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]
 **sortBy** | **optional.String**| Field to sort by | [default to created_at]
 **sortOrder** | **optional.String**| Sort direction | [default to desc]

### Return type

[**AdminUserListResponse**](AdminUserListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListGroupMembers**
> GroupMemberListResponse ListGroupMembers(ctx, internalUuid, optional)
List group members

Returns a paginated list of users who are members of the specified group. Includes user details (email, name, provider information).

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 
 **optional** | ***AdministrationApiListGroupMembersOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListGroupMembersOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListSystemSettings**
> []SystemSetting ListSystemSettings(ctx, )
List system settings

Returns all system settings. Requires administrator privileges.

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**[]SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListUserAPIQuotas**
> ListUserQuotasResponse ListUserAPIQuotas(ctx, optional)
List all user API quotas

Retrieves all custom API rate limit quotas (users with non-default quotas)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiListUserAPIQuotasOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListUserAPIQuotasOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListUserQuotasResponse**](ListUserQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListWebhookQuotas**
> ListWebhookQuotasResponse ListWebhookQuotas(ctx, optional)
List all webhook quotas

Retrieves all custom webhook quotas (users with non-default quotas)

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiListWebhookQuotasOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiListWebhookQuotasOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListWebhookQuotasResponse**](ListWebhookQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **MigrateSystemSettings**
> InlineResponse20010 MigrateSystemSettings(ctx, optional)
Migrate settings from configuration

Migrates settings from the server configuration (config file or environment variables) to the database. When overwrite is false (default), only settings that don't already exist in the database are added. When overwrite is true, all settings are imported, overwriting existing values. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***AdministrationApiMigrateSystemSettingsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiMigrateSystemSettingsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overwrite** | **optional.Bool**| If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don&#x27;t already exist. | [default to false]

### Return type

[**InlineResponse20010**](inline_response_200_10.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ReencryptSystemSettings**
> InlineResponse20011 ReencryptSystemSettings(ctx, )
Re-encrypt all system settings

Re-encrypts all system settings with the current encryption key. Use this after rotating the encryption key or when first enabling encryption on existing settings. Requires administrator privileges. Settings that cannot be decrypted are reported as errors but do not prevent other settings from being processed.

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20011**](inline_response_200_11.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **RemoveGroupMember**
> RemoveGroupMember(ctx, internalUuid, memberUuid, optional)
Remove member from group

Removes a user or nested group from a group. Use the subject_type query parameter to specify whether the member is a user (default) or a group. Cannot remove members from the special 'everyone' pseudo-group.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 
  **memberUuid** | [**string**](.md)| Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group) | 
 **optional** | ***AdministrationApiRemoveGroupMemberOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdministrationApiRemoveGroupMemberOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **subjectType** | **optional.String**| Type of member to remove: &#x27;user&#x27; (default) for a user member, &#x27;group&#x27; for a nested group member | [default to user]

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **TransferAdminUserOwnership**
> TransferOwnershipResult TransferAdminUserOwnership(ctx, body, internalUuid)
Transfer user ownership to another user

Transfers ownership of all threat models and survey responses owned by the specified user to the target user. The source user is downgraded to writer role on all transferred items. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)| Ownership transfer request specifying the target user | 
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateAddonInvocationQuota**
> AddonInvocationQuota UpdateAddonInvocationQuota(ctx, body, userId)
Update addon invocation quota

Creates or updates the addon invocation quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**AddonQuotaUpdate**](AddonQuotaUpdate.md)| Addon quota update configuration | 
  **userId** | [**string**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateAdminGroup**
> AdminGroup UpdateAdminGroup(ctx, body, internalUuid)
Update group metadata

Updates group metadata fields (name, description). Only provided fields are updated.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**UpdateAdminGroupRequest**](UpdateAdminGroupRequest.md)| Group update details | 
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateAdminUser**
> AdminUser UpdateAdminUser(ctx, body, internalUuid)
Update user metadata

Updates user metadata fields (email, name, email_verified). Only provided fields are updated.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**UpdateAdminUserRequest**](UpdateAdminUserRequest.md)| User profile update | 
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateSystemSetting**
> SystemSetting UpdateSystemSetting(ctx, body, key)
Update system setting

Creates or updates a system setting. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**SystemSettingUpdate**](SystemSettingUpdate.md)| The system setting value to create or update | 
  **key** | **string**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateUserAPIQuota**
> UserApiQuota UpdateUserAPIQuota(ctx, body, userId)
Update user API quota

Creates or updates the API rate limit quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**UserQuotaUpdate**](UserQuotaUpdate.md)| User quota update configuration | 
  **userId** | [**string**](.md)| User ID | 

### Return type

[**UserApiQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **UpdateWebhookQuota**
> WebhookQuota UpdateWebhookQuota(ctx, body, userId)
Update webhook quota

Creates or updates the webhook quota for a specific user

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**WebhookQuotaUpdate**](WebhookQuotaUpdate.md)| Webhook quota update configuration | 
  **userId** | [**string**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

