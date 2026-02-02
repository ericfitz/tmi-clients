# TmiJsClient.UserAccountApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCurrentUserPreferences**](UserAccountApi.md#createCurrentUserPreferences) | **POST** /me/preferences | Create user preferences
[**getCurrentUserPreferences**](UserAccountApi.md#getCurrentUserPreferences) | **GET** /me/preferences | Get user preferences
[**updateCurrentUserPreferences**](UserAccountApi.md#updateCurrentUserPreferences) | **PUT** /me/preferences | Update user preferences

<a name="createCurrentUserPreferences"></a>
# **createCurrentUserPreferences**
> UserPreferences createCurrentUserPreferences(body)

Create user preferences

Creates preferences for the current user. Fails with 409 Conflict if preferences already exist (use PUT to update).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UserAccountApi();
let body = null; // {String: {String: Object}} | User preferences to create. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name.

apiInstance.createCurrentUserPreferences(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**{String: {String: Object}}**](Object.md)| User preferences to create. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name. | 

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getCurrentUserPreferences"></a>
# **getCurrentUserPreferences**
> UserPreferences getCurrentUserPreferences()

Get user preferences

Retrieves the current user&#x27;s preferences. Returns an empty object {} if no preferences have been set.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UserAccountApi();
apiInstance.getCurrentUserPreferences().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateCurrentUserPreferences"></a>
# **updateCurrentUserPreferences**
> UserPreferences updateCurrentUserPreferences(body)

Update user preferences

Creates or replaces the current user&#x27;s preferences. This is an upsert operation - creates if not exists, replaces entirely if exists.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.UserAccountApi();
let body = null; // {String: {String: Object}} | User preferences to create or replace. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name.

apiInstance.updateCurrentUserPreferences(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**{String: {String: Object}}**](Object.md)| User preferences to create or replace. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name. | 

### Return type

[**UserPreferences**](UserPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

