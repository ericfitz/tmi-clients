# TmiJsClient.AdministrationApi

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGroupMember**](AdministrationApi.md#addGroupMember) | **POST** /admin/groups/{internal_uuid}/members | Add member to group
[**createAdminGroup**](AdministrationApi.md#createAdminGroup) | **POST** /admin/groups | Create provider-independent group
[**createAdministrator**](AdministrationApi.md#createAdministrator) | **POST** /admin/administrators | Create administrator grant
[**deleteAddonInvocationQuota**](AdministrationApi.md#deleteAddonInvocationQuota) | **DELETE** /admin/quotas/addons/{user_id} | Delete addon invocation quota
[**deleteAdminGroup**](AdministrationApi.md#deleteAdminGroup) | **DELETE** /admin/groups/{internal_uuid} | Delete group
[**deleteAdminUser**](AdministrationApi.md#deleteAdminUser) | **DELETE** /admin/users/{internal_uuid} | Delete user
[**deleteAdministrator**](AdministrationApi.md#deleteAdministrator) | **DELETE** /admin/administrators/{id} | Delete administrator grant
[**deleteSystemSetting**](AdministrationApi.md#deleteSystemSetting) | **DELETE** /admin/settings/{key} | Delete system setting
[**deleteUserAPIQuota**](AdministrationApi.md#deleteUserAPIQuota) | **DELETE** /admin/quotas/users/{user_id} | Delete user API quota
[**deleteWebhookQuota**](AdministrationApi.md#deleteWebhookQuota) | **DELETE** /admin/quotas/webhooks/{user_id} | Delete webhook quota
[**getAddonInvocationQuota**](AdministrationApi.md#getAddonInvocationQuota) | **GET** /admin/quotas/addons/{user_id} | Get addon invocation quota
[**getAdminGroup**](AdministrationApi.md#getAdminGroup) | **GET** /admin/groups/{internal_uuid} | Get group details
[**getAdminUser**](AdministrationApi.md#getAdminUser) | **GET** /admin/users/{internal_uuid} | Get user details
[**getSystemSetting**](AdministrationApi.md#getSystemSetting) | **GET** /admin/settings/{key} | Get system setting
[**getUserAPIQuota**](AdministrationApi.md#getUserAPIQuota) | **GET** /admin/quotas/users/{user_id} | Get user API quota
[**getWebhookQuota**](AdministrationApi.md#getWebhookQuota) | **GET** /admin/quotas/webhooks/{user_id} | Get webhook quota
[**listAddonInvocationQuotas**](AdministrationApi.md#listAddonInvocationQuotas) | **GET** /admin/quotas/addons | List all addon invocation quotas
[**listAdminGroups**](AdministrationApi.md#listAdminGroups) | **GET** /admin/groups | List groups
[**listAdminUsers**](AdministrationApi.md#listAdminUsers) | **GET** /admin/users | List users
[**listAdministrators**](AdministrationApi.md#listAdministrators) | **GET** /admin/administrators | List administrators
[**listGroupMembers**](AdministrationApi.md#listGroupMembers) | **GET** /admin/groups/{internal_uuid}/members | List group members
[**listSystemSettings**](AdministrationApi.md#listSystemSettings) | **GET** /admin/settings | List system settings
[**listUserAPIQuotas**](AdministrationApi.md#listUserAPIQuotas) | **GET** /admin/quotas/users | List all user API quotas
[**listWebhookQuotas**](AdministrationApi.md#listWebhookQuotas) | **GET** /admin/quotas/webhooks | List all webhook quotas
[**migrateSystemSettings**](AdministrationApi.md#migrateSystemSettings) | **POST** /admin/settings/migrate | Migrate settings from configuration
[**removeGroupMember**](AdministrationApi.md#removeGroupMember) | **DELETE** /admin/groups/{internal_uuid}/members/{user_uuid} | Remove member from group
[**updateAddonInvocationQuota**](AdministrationApi.md#updateAddonInvocationQuota) | **PUT** /admin/quotas/addons/{user_id} | Update addon invocation quota
[**updateAdminGroup**](AdministrationApi.md#updateAdminGroup) | **PATCH** /admin/groups/{internal_uuid} | Update group metadata
[**updateAdminUser**](AdministrationApi.md#updateAdminUser) | **PATCH** /admin/users/{internal_uuid} | Update user metadata
[**updateSystemSetting**](AdministrationApi.md#updateSystemSetting) | **PUT** /admin/settings/{key} | Update system setting
[**updateUserAPIQuota**](AdministrationApi.md#updateUserAPIQuota) | **PUT** /admin/quotas/users/{user_id} | Update user API quota
[**updateWebhookQuota**](AdministrationApi.md#updateWebhookQuota) | **PUT** /admin/quotas/webhooks/{user_id} | Update webhook quota

<a name="addGroupMember"></a>
# **addGroupMember**
> GroupMember addGroupMember(body, internalUuid)

Add member to group

Adds a user to a group. The user must exist in the system. Cannot add members to the special &#x27;everyone&#x27; pseudo-group.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.AddGroupMemberRequest(); // AddGroupMemberRequest | Group membership update
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.addGroupMember(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md)| Group membership update | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createAdminGroup"></a>
# **createAdminGroup**
> AdminGroup createAdminGroup(body)

Create provider-independent group

Creates a new provider-independent group (provider&#x3D;\&quot;*\&quot;). These groups can be used across all providers for authorization and administration.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.CreateAdminGroupRequest(); // CreateAdminGroupRequest | Group creation request

apiInstance.createAdminGroup(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAdminGroupRequest**](CreateAdminGroupRequest.md)| Group creation request | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="createAdministrator"></a>
# **createAdministrator**
> Administrator createAdministrator(body)

Create administrator grant

Grants administrator privileges to a user or group for a specific provider. Exactly one of email, provider_user_id, or group_name must be specified.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.CreateAdministratorRequest(); // CreateAdministratorRequest | Administrator creation request

apiInstance.createAdministrator(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAdministratorRequest**](CreateAdministratorRequest.md)| Administrator creation request | 

### Return type

[**Administrator**](Administrator.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAddonInvocationQuota"></a>
# **deleteAddonInvocationQuota**
> deleteAddonInvocationQuota(userId)

Delete addon invocation quota

Deletes the custom addon invocation quota for a user, reverting to system defaults

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.deleteAddonInvocationQuota(userId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAdminGroup"></a>
# **deleteAdminGroup**
> deleteAdminGroup(internalUuid)

Delete group

Deletes a TMI-managed group and handles threat model cleanup. Protected groups like &#x27;everyone&#x27; cannot be deleted.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.deleteAdminGroup(internalUuid).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAdminUser"></a>
# **deleteAdminUser**
> deleteAdminUser(internalUuid)

Delete user

Deletes a user and all associated data. Transfers sole-owned threat models or deletes them if no other owners exist.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.deleteAdminUser(internalUuid).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAdministrator"></a>
# **deleteAdministrator**
> deleteAdministrator(id)

Delete administrator grant

Revokes administrator privileges. Users cannot revoke their own privileges or privileges for groups they belong to.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Administrator grant ID

apiInstance.deleteAdministrator(id).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**String**](.md)| Administrator grant ID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteSystemSetting"></a>
# **deleteSystemSetting**
> deleteSystemSetting(key)

Delete system setting

Deletes a system setting. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let key = "key_example"; // String | The setting key

apiInstance.deleteSystemSetting(key).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| The setting key | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteUserAPIQuota"></a>
# **deleteUserAPIQuota**
> deleteUserAPIQuota(userId)

Delete user API quota

Deletes the custom API quota for a user, reverting to system defaults

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.deleteUserAPIQuota(userId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteWebhookQuota"></a>
# **deleteWebhookQuota**
> deleteWebhookQuota(userId)

Delete webhook quota

Deletes the custom webhook quota for a user, reverting to system defaults

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.deleteWebhookQuota(userId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAddonInvocationQuota"></a>
# **getAddonInvocationQuota**
> AddonInvocationQuota getAddonInvocationQuota(userId)

Get addon invocation quota

Retrieves the addon invocation quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.getAddonInvocationQuota(userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAdminGroup"></a>
# **getAdminGroup**
> AdminGroup getAdminGroup(internalUuid)

Get group details

Returns detailed information about a specific group, including enriched data (usage in authorizations and admin grants).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.getAdminGroup(internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getAdminUser"></a>
# **getAdminUser**
> AdminUser getAdminUser(internalUuid)

Get user details

Returns detailed information about a specific user, including enriched data (admin status, groups, threat model counts).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.getAdminUser(internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getSystemSetting"></a>
# **getSystemSetting**
> SystemSetting getSystemSetting(key)

Get system setting

Returns a specific system setting by key. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let key = "key_example"; // String | The setting key

apiInstance.getSystemSetting(key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getUserAPIQuota"></a>
# **getUserAPIQuota**
> UserAPIQuota getUserAPIQuota(userId)

Get user API quota

Retrieves the API rate limit quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.getUserAPIQuota(userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getWebhookQuota"></a>
# **getWebhookQuota**
> WebhookQuota getWebhookQuota(userId)

Get webhook quota

Retrieves the webhook quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.getWebhookQuota(userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | [**String**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAddonInvocationQuotas"></a>
# **listAddonInvocationQuotas**
> ListAddonQuotasResponse listAddonInvocationQuotas(opts)

List all addon invocation quotas

Retrieves all custom addon invocation quotas (users with non-default quotas)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listAddonInvocationQuotas(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAddonQuotasResponse**](ListAddonQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAdminGroups"></a>
# **listAdminGroups**
> AdminGroupListResponse listAdminGroups(opts)

List groups

Returns a paginated list of groups with optional filtering by provider, name, and usage. Includes enriched data (usage in authorizations and admin grants).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'provider': "provider_example", // String | Filter by OAuth/SAML provider
  'groupName': "groupName_example", // String | Filter by group name (case-insensitive substring match)
  'usedInAuthorizations': true, // Boolean | Filter groups used (true) or not used (false) in authorizations
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sortBy': "created_at", // String | Field to sort by
  'sortOrder': "desc" // String | Sort direction
};
apiInstance.listAdminGroups(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| Filter by OAuth/SAML provider | [optional] 
 **groupName** | **String**| Filter by group name (case-insensitive substring match) | [optional] 
 **usedInAuthorizations** | **Boolean**| Filter groups used (true) or not used (false) in authorizations | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **sortBy** | **String**| Field to sort by | [optional] [default to created_at]
 **sortOrder** | **String**| Sort direction | [optional] [default to desc]

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAdminUsers"></a>
# **listAdminUsers**
> AdminUserListResponse listAdminUsers(opts)

List users

Returns a paginated list of users with optional filtering by provider, email, and date ranges. Includes enriched data (admin status, groups, threat model counts).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'provider': "provider_example", // String | Filter by OAuth/SAML provider
  'email': "email_example", // String | Filter by email (case-insensitive substring match)
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter users created after this timestamp (RFC3339)
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter users created before this timestamp (RFC3339)
  'lastLoginAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter users who logged in after this timestamp (RFC3339)
  'lastLoginBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter users who logged in before this timestamp (RFC3339)
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sortBy': "created_at", // String | Field to sort by
  'sortOrder': "desc" // String | Sort direction
};
apiInstance.listAdminUsers(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| Filter by OAuth/SAML provider | [optional] 
 **email** | **String**| Filter by email (case-insensitive substring match) | [optional] 
 **createdAfter** | **Date**| Filter users created after this timestamp (RFC3339) | [optional] 
 **createdBefore** | **Date**| Filter users created before this timestamp (RFC3339) | [optional] 
 **lastLoginAfter** | **Date**| Filter users who logged in after this timestamp (RFC3339) | [optional] 
 **lastLoginBefore** | **Date**| Filter users who logged in before this timestamp (RFC3339) | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **sortBy** | **String**| Field to sort by | [optional] [default to created_at]
 **sortOrder** | **String**| Sort direction | [optional] [default to desc]

### Return type

[**AdminUserListResponse**](AdminUserListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listAdministrators"></a>
# **listAdministrators**
> ListAdministratorsResponse listAdministrators(opts)

List administrators

Returns a list of administrator grants with optional filtering by provider, user, or group

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'provider': "provider_example", // String | Filter by OAuth/SAML provider
  'userId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by user ID
  'groupId': "38400000-8cf0-11bd-b23e-10b96e4ef00d", // String | Filter by group ID
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listAdministrators(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| Filter by OAuth/SAML provider | [optional] 
 **userId** | [**String**](.md)| Filter by user ID | [optional] 
 **groupId** | [**String**](.md)| Filter by group ID | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListAdministratorsResponse**](ListAdministratorsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listGroupMembers"></a>
# **listGroupMembers**
> GroupMemberListResponse listGroupMembers(internalUuid, opts)

List group members

Returns a paginated list of users who are members of the specified group. Includes user details (email, name, provider information).

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user
let opts = { 
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listGroupMembers(internalUuid, opts).then((data) => {
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

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listSystemSettings"></a>
# **listSystemSettings**
> [SystemSetting] listSystemSettings()

List system settings

Returns all system settings. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
apiInstance.listSystemSettings().then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[SystemSetting]**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listUserAPIQuotas"></a>
# **listUserAPIQuotas**
> ListUserQuotasResponse listUserAPIQuotas(opts)

List all user API quotas

Retrieves all custom API rate limit quotas (users with non-default quotas)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listUserAPIQuotas(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListUserQuotasResponse**](ListUserQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listWebhookQuotas"></a>
# **listWebhookQuotas**
> ListWebhookQuotasResponse listWebhookQuotas(opts)

List all webhook quotas

Retrieves all custom webhook quotas (users with non-default quotas)

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0 // Number | Number of results to skip
};
apiInstance.listWebhookQuotas(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**ListWebhookQuotasResponse**](ListWebhookQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="migrateSystemSettings"></a>
# **migrateSystemSettings**
> InlineResponse20010 migrateSystemSettings(opts)

Migrate settings from configuration

Migrates settings from the server configuration (config file or environment variables) to the database. When overwrite is false (default), only settings that don&#x27;t already exist in the database are added. When overwrite is true, all settings are imported, overwriting existing values. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let opts = { 
  'overwrite': false // Boolean | If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don't already exist.
};
apiInstance.migrateSystemSettings(opts).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overwrite** | **Boolean**| If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don&#x27;t already exist. | [optional] [default to false]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="removeGroupMember"></a>
# **removeGroupMember**
> removeGroupMember(internalUuid, userUuid)

Remove member from group

Removes a user from a group. Cannot remove members from the special &#x27;everyone&#x27; pseudo-group.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user
let userUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user to remove

apiInstance.removeGroupMember(internalUuid, userUuid).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 
 **userUuid** | [**String**](.md)| Internal system UUID of the user to remove | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="updateAddonInvocationQuota"></a>
# **updateAddonInvocationQuota**
> AddonInvocationQuota updateAddonInvocationQuota(body, userId)

Update addon invocation quota

Creates or updates the addon invocation quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.AddonQuotaUpdate(); // AddonQuotaUpdate | Addon quota update configuration
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.updateAddonInvocationQuota(body, userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddonQuotaUpdate**](AddonQuotaUpdate.md)| Addon quota update configuration | 
 **userId** | [**String**](.md)| User ID | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateAdminGroup"></a>
# **updateAdminGroup**
> AdminGroup updateAdminGroup(body, internalUuid)

Update group metadata

Updates group metadata fields (name, description). Only provided fields are updated.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.UpdateAdminGroupRequest(); // UpdateAdminGroupRequest | Group update details
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.updateAdminGroup(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminGroupRequest**](UpdateAdminGroupRequest.md)| Group update details | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateAdminUser"></a>
# **updateAdminUser**
> AdminUser updateAdminUser(body, internalUuid)

Update user metadata

Updates user metadata fields (email, name, email_verified). Only provided fields are updated.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.UpdateAdminUserRequest(); // UpdateAdminUserRequest | User profile update
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the user

apiInstance.updateAdminUser(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminUserRequest**](UpdateAdminUserRequest.md)| User profile update | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateSystemSetting"></a>
# **updateSystemSetting**
> SystemSetting updateSystemSetting(body, key)

Update system setting

Creates or updates a system setting. Requires administrator privileges.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.SystemSettingUpdate(); // SystemSettingUpdate | The system setting value to create or update
let key = "key_example"; // String | The setting key

apiInstance.updateSystemSetting(body, key).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemSettingUpdate**](SystemSettingUpdate.md)| The system setting value to create or update | 
 **key** | **String**| The setting key | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateUserAPIQuota"></a>
# **updateUserAPIQuota**
> UserAPIQuota updateUserAPIQuota(body, userId)

Update user API quota

Creates or updates the API rate limit quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.UserQuotaUpdate(); // UserQuotaUpdate | User quota update configuration
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.updateUserAPIQuota(body, userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserQuotaUpdate**](UserQuotaUpdate.md)| User quota update configuration | 
 **userId** | [**String**](.md)| User ID | 

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="updateWebhookQuota"></a>
# **updateWebhookQuota**
> WebhookQuota updateWebhookQuota(body, userId)

Update webhook quota

Creates or updates the webhook quota for a specific user

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.WebhookQuotaUpdate(); // WebhookQuotaUpdate | Webhook quota update configuration
let userId = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | User ID

apiInstance.updateWebhookQuota(body, userId).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WebhookQuotaUpdate**](WebhookQuotaUpdate.md)| Webhook quota update configuration | 
 **userId** | [**String**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

