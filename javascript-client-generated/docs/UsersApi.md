# TmiJsClient.UsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserAccount**](UsersApi.md#deleteUserAccount) | **DELETE** /users/me | Delete authenticated user account and all data

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

