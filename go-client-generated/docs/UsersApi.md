# {{classname}}

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteUserAccount**](UsersApi.md#DeleteUserAccount) | **Delete** /me | Delete authenticated user account and all data
[**LogoutCurrentUser**](UsersApi.md#LogoutCurrentUser) | **Post** /me/logout | Logout current user
[**TransferCurrentUserOwnership**](UsersApi.md#TransferCurrentUserOwnership) | **Post** /me/transfer | Transfer ownership of all owned resources

# **DeleteUserAccount**
> DeletionChallenge DeleteUserAccount(ctx, optional)
Delete authenticated user account and all data

Two-step deletion process: 1. First call (no challenge parameter) - Returns challenge string 2. Second call (with challenge parameter) - Confirms deletion  Ownership behavior: - Shared threat models: Transfers ownership to another owner from authorization list - Unshared threat models: Deletes completely along with all child resources

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***UsersApiDeleteUserAccountOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a UsersApiDeleteUserAccountOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge** | **optional.String**| Challenge string from first request (step 2 only). Must match exactly. | 

### Return type

[**DeletionChallenge**](DeletionChallenge.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **LogoutCurrentUser**
> LogoutCurrentUser(ctx, )
Logout current user

Revokes the authenticated user's current JWT token. This is a convenience endpoint that automatically revokes the token used to authenticate the request, without requiring the token to be passed in the request body. The token is immediately added to the blacklist and cannot be used for further requests.

### Required Parameters
This endpoint does not need any parameter.

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **TransferCurrentUserOwnership**
> TransferOwnershipResult TransferCurrentUserOwnership(ctx, body)
Transfer ownership of all owned resources

Transfers ownership of all threat models and survey responses owned by the current user to the specified target user. The current user is downgraded to writer role on all transferred items.

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
  **body** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)| Ownership transfer request specifying the target user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

