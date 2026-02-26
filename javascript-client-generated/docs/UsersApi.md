# TmiJsClient.UsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserAccount**](UsersApi.md#deleteUserAccount) | **DELETE** /me | Delete authenticated user account and all data
[**logoutCurrentUser**](UsersApi.md#logoutCurrentUser) | **POST** /me/logout | Logout current user
[**transferCurrentUserOwnership**](UsersApi.md#transferCurrentUserOwnership) | **POST** /me/transfer | Transfer ownership of all owned resources

<a name="deleteUserAccount"></a>
# **deleteUserAccount**
> DeletionChallenge deleteUserAccount(opts)

Delete authenticated user account and all data

Two-step deletion process: 1. First call (no challenge parameter) - Returns challenge string 2. Second call (with challenge parameter) - Confirms deletion  Ownership behavior: - Shared threat models: Transfers ownership to another owner from authorization list - Unshared threat models: Deletes completely along with all child resources

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UsersApi();
let opts = { 
  'challenge': "challenge_example" // String | Challenge string from first request (step 2 only). Must match exactly.
};
apiInstance.deleteUserAccount(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge** | **String**| Challenge string from first request (step 2 only). Must match exactly. | [optional] 

### Return type

[**DeletionChallenge**](DeletionChallenge.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="logoutCurrentUser"></a>
# **logoutCurrentUser**
> logoutCurrentUser()

Logout current user

Revokes the authenticated user&#x27;s current JWT token. This is a convenience endpoint that automatically revokes the token used to authenticate the request, without requiring the token to be passed in the request body. The token is immediately added to the blacklist and cannot be used for further requests.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UsersApi();
apiInstance.logoutCurrentUser().then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="transferCurrentUserOwnership"></a>
# **transferCurrentUserOwnership**
> TransferOwnershipResult transferCurrentUserOwnership(body)

Transfer ownership of all owned resources

Transfers ownership of all threat models and survey responses owned by the current user to the specified target user. The current user is downgraded to writer role on all transferred items.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UsersApi();
let body = new TmiJsClient.TransferOwnershipRequest(); // TransferOwnershipRequest | Ownership transfer request specifying the target user

apiInstance.transferCurrentUserOwnership(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)| Ownership transfer request specifying the target user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

