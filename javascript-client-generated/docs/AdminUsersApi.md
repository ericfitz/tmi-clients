# TmiJsClient.AdminUsersApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAdminUserClientCredential**](AdminUsersApi.md#createAdminUserClientCredential) | **POST** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
[**createAutomationAccount**](AdminUsersApi.md#createAutomationAccount) | **POST** /admin/users/automation | Create an automation (service) account
[**deleteAdminUserClientCredential**](AdminUsersApi.md#deleteAdminUserClientCredential) | **DELETE** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
[**listAdminUserClientCredentials**](AdminUsersApi.md#listAdminUserClientCredentials) | **GET** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user

<a name="createAdminUserClientCredential"></a>
# **createAdminUserClientCredential**
> ClientCredentialResponse createAdminUserClientCredential(body, internalUuid)

Create a client credential for an automation user

Creates a new client credential for the specified automation user. Only accessible for users with automation&#x3D;true. The client_secret is returned only once. Admin operations bypass quota limits.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdminUsersApi();
let body = new TmiJsClient.InternalUuidClientCredentialsBody(); // InternalUuidClientCredentialsBody | 
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.createAdminUserClientCredential(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InternalUuidClientCredentialsBody**](InternalUuidClientCredentialsBody.md)|  | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**ClientCredentialResponse**](ClientCredentialResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createAutomationAccount"></a>
# **createAutomationAccount**
> CreateAutomationAccountResponse createAutomationAccount(body)

Create an automation (service) account

Creates a new automation account with the TMI provider, sets the automation flag, adds the account to the TMI Automation built-in group, and creates a client credential. The client secret is returned only once and cannot be retrieved later. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdminUsersApi();
let body = new TmiJsClient.CreateAutomationAccountRequest(); // CreateAutomationAccountRequest | 

apiInstance.createAutomationAccount(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAutomationAccountRequest**](CreateAutomationAccountRequest.md)|  | 

### Return type

[**CreateAutomationAccountResponse**](CreateAutomationAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAdminUserClientCredential"></a>
# **deleteAdminUserClientCredential**
> deleteAdminUserClientCredential(internalUuid, credentialId)

Delete a client credential for an automation user

Deletes and revokes a client credential for the specified automation user. Only accessible for users with automation&#x3D;true.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdminUsersApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user
let credentialId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal UUID of the client credential (the \"id\" field from the list response, not the \"client_id\")

apiInstance.deleteAdminUserClientCredential(internalUuid, credentialId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 
 **credentialId** | [**String**](.md)| Internal UUID of the client credential (the \&quot;id\&quot; field from the list response, not the \&quot;client_id\&quot;) | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAdminUserClientCredentials"></a>
# **listAdminUserClientCredentials**
> ListClientCredentialsResponse listAdminUserClientCredentials(internalUuid, opts)

List client credentials for an automation user

Lists all client credentials for the specified automation user. Only accessible for users with automation&#x3D;true. Secrets are never returned.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdminUsersApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user
let opts = { 
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listAdminUserClientCredentials(internalUuid, opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListClientCredentialsResponse**](ListClientCredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

