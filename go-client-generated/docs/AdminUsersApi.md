# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAdminUserClientCredential**](AdminUsersApi.md#CreateAdminUserClientCredential) | **Post** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
[**CreateAutomationAccount**](AdminUsersApi.md#CreateAutomationAccount) | **Post** /admin/users/automation | Create an automation (service) account
[**DeleteAdminUserClientCredential**](AdminUsersApi.md#DeleteAdminUserClientCredential) | **Delete** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
[**ListAdminUserClientCredentials**](AdminUsersApi.md#ListAdminUserClientCredentials) | **Get** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user

# **CreateAdminUserClientCredential**
> ClientCredentialResponse CreateAdminUserClientCredential(ctx, body, internalUuid)
Create a client credential for an automation user

Creates a new client credential for the specified automation user. Only accessible for users with automation=true. The client_secret is returned only once. Admin operations bypass quota limits.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**InternalUuidClientCredentialsBody**](InternalUuidClientCredentialsBody.md)|  | 
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **CreateAutomationAccount**
> CreateAutomationAccountResponse CreateAutomationAccount(ctx, body)
Create an automation (service) account

Creates a new automation account with the TMI provider, sets the automation flag, adds the account to the TMI Automation built-in group, and creates a client credential. The client secret is returned only once and cannot be retrieved later. Requires administrator privileges.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**CreateAutomationAccountRequest**](CreateAutomationAccountRequest.md)|  | 

### Return type

[**CreateAutomationAccountResponse**](CreateAutomationAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **DeleteAdminUserClientCredential**
> DeleteAdminUserClientCredential(ctx, internalUuid, credentialId)
Delete a client credential for an automation user

Deletes and revokes a client credential for the specified automation user. Only accessible for users with automation=true.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 
  **credentialId** | [**string**](.md)| Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ListAdminUserClientCredentials**
> ListClientCredentialsResponse ListAdminUserClientCredentials(ctx, internalUuid, optional)
List client credentials for an automation user

Lists all client credentials for the specified automation user. Only accessible for users with automation=true. Secrets are never returned.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **internalUuid** | [**string**](.md)| Internal system UUID of the user | 
 **optional** | ***AdminUsersApiListAdminUserClientCredentialsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a AdminUsersApiListAdminUserClientCredentialsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **optional.Int32**| Maximum number of results to return | [default to 50]
 **offset** | **optional.Int32**| Number of results to skip | [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

