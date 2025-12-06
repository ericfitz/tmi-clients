# TmiJsClient.AdministrationApi

All URIs are relative to *http://localhost:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGroupMember**](AdministrationApi.md#addGroupMember) | **POST** /admin/groups/{internal_uuid}/members | Add member to group
[**createAdminGroup**](AdministrationApi.md#createAdminGroup) | **POST** /admin/groups | Create provider-independent group
[**createAdministrator**](AdministrationApi.md#createAdministrator) | **POST** /admin/administrators | Create administrator grant
[**deleteAddonInvocationQuota**](AdministrationApi.md#deleteAddonInvocationQuota) | **DELETE** /admin/quotas/addons/{user_id} | Delete addon invocation quota
[**deleteAdminGroup**](AdministrationApi.md#deleteAdminGroup) | **DELETE** /admin/groups | Delete group (Not Implemented)
[**deleteAdminUser**](AdministrationApi.md#deleteAdminUser) | **DELETE** /admin/users | Delete user
[**deleteAdministrator**](AdministrationApi.md#deleteAdministrator) | **DELETE** /admin/administrators/{id} | Delete administrator grant
[**deleteUserAPIQuota**](AdministrationApi.md#deleteUserAPIQuota) | **DELETE** /admin/quotas/users/{user_id} | Delete user API quota
[**deleteWebhookQuota**](AdministrationApi.md#deleteWebhookQuota) | **DELETE** /admin/quotas/webhooks/{user_id} | Delete webhook quota
[**getAddonInvocationQuota**](AdministrationApi.md#getAddonInvocationQuota) | **GET** /admin/quotas/addons/{user_id} | Get addon invocation quota
[**getAdminGroup**](AdministrationApi.md#getAdminGroup) | **GET** /admin/groups/{internal_uuid} | Get group details
[**getAdminUser**](AdministrationApi.md#getAdminUser) | **GET** /admin/users/{internal_uuid} | Get user details
[**getUserAPIQuota**](AdministrationApi.md#getUserAPIQuota) | **GET** /admin/quotas/users/{user_id} | Get user API quota
[**getWebhookQuota**](AdministrationApi.md#getWebhookQuota) | **GET** /admin/quotas/webhooks/{user_id} | Get webhook quota
[**listAddonInvocationQuotas**](AdministrationApi.md#listAddonInvocationQuotas) | **GET** /admin/quotas/addons | List all addon invocation quotas
[**listAdminGroups**](AdministrationApi.md#listAdminGroups) | **GET** /admin/groups | List groups
[**listAdminUsers**](AdministrationApi.md#listAdminUsers) | **GET** /admin/users | List users
[**listAdministrators**](AdministrationApi.md#listAdministrators) | **GET** /admin/administrators | List administrators
[**listGroupMembers**](AdministrationApi.md#listGroupMembers) | **GET** /admin/groups/{internal_uuid}/members | List group members
[**listUserAPIQuotas**](AdministrationApi.md#listUserAPIQuotas) | **GET** /admin/quotas/users | List all user API quotas
[**listWebhookQuotas**](AdministrationApi.md#listWebhookQuotas) | **GET** /admin/quotas/webhooks | List all webhook quotas
[**removeGroupMember**](AdministrationApi.md#removeGroupMember) | **DELETE** /admin/groups/{internal_uuid}/members/{user_uuid} | Remove member from group
[**updateAddonInvocationQuota**](AdministrationApi.md#updateAddonInvocationQuota) | **PUT** /admin/quotas/addons/{user_id} | Update addon invocation quota
[**updateAdminGroup**](AdministrationApi.md#updateAdminGroup) | **PATCH** /admin/groups/{internal_uuid} | Update group metadata
[**updateAdminUser**](AdministrationApi.md#updateAdminUser) | **PATCH** /admin/users/{internal_uuid} | Update user metadata
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
let body = new TmiJsClient.AddGroupMemberRequest(); // AddGroupMemberRequest | 
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the group

apiInstance.addGroupMember(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md)|  | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the group | 

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
let body = new TmiJsClient.CreateAdminGroupRequest(); // CreateAdminGroupRequest | 

apiInstance.createAdminGroup(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAdminGroupRequest**](CreateAdminGroupRequest.md)|  | 

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

Grants administrator privileges to a user or group for a specific provider. Exactly one of user_id or group_id must be specified.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let body = new TmiJsClient.CreateAdministratorRequest(); // CreateAdministratorRequest | 

apiInstance.createAdministrator(body).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAdministratorRequest**](CreateAdministratorRequest.md)|  | 

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
> deleteAdminGroup(provider, groupName)

Delete group (Not Implemented)

Group deletion is not currently supported. This endpoint returns 501 Not Implemented. Groups remain in the system for audit and historical purposes.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let provider = "provider_example"; // String | OAuth/SAML provider identifier or \"*\" for provider-independent groups
let groupName = "groupName_example"; // String | Group name identifier

apiInstance.deleteAdminGroup(provider, groupName).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| OAuth/SAML provider identifier or \&quot;*\&quot; for provider-independent groups | 
 **groupName** | **String**| Group name identifier | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="deleteAdminUser"></a>
# **deleteAdminUser**
> deleteAdminUser(provider, providerUserId)

Delete user

Deletes a user and all associated data. Transfers sole-owned threat models or deletes them if no other owners exist. Requires both provider and provider_user_id query parameters.

### Example
```javascript
import {TmiJsClient} from 'tmi-js-client';
let defaultClient = TmiJsClient.ApiClient.instance;


let apiInstance = new TmiJsClient.AdministrationApi();
let provider = "provider_example"; // String | OAuth/SAML provider identifier
let providerUserId = "providerUserId_example"; // String | Provider-assigned user identifier

apiInstance.deleteAdminUser(provider, providerUserId).then(() => {
  console.log('API called successfully.');
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| OAuth/SAML provider identifier | 
 **providerUserId** | **String**| Provider-assigned user identifier | 

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
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the group

apiInstance.getAdminGroup(internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internalUuid** | [**String**](.md)| Internal system UUID of the group | 

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
> [AddonInvocationQuota] listAddonInvocationQuotas(opts)

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

[**[AddonInvocationQuota]**](AddonInvocationQuota.md)

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
  'provider': "provider_example", // String | Filter by OAuth/SAML provider (use \"*\" for provider-independent groups)
  'groupName': "groupName_example", // String | Filter by group name (case-insensitive substring match)
  'usedInAuthorizations': true, // Boolean | Filter groups used (true) or not used (false) in authorizations
  'limit': 50, // Number | Maximum number of results to return
  'offset': 0, // Number | Number of results to skip
  'sortBy': "group_name", // String | Field to sort by
  'sortOrder': "asc" // String | Sort direction
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
 **provider** | **String**| Filter by OAuth/SAML provider (use \&quot;*\&quot; for provider-independent groups) | [optional] 
 **groupName** | **String**| Filter by group name (case-insensitive substring match) | [optional] 
 **usedInAuthorizations** | **Boolean**| Filter groups used (true) or not used (false) in authorizations | [optional] 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]
 **sortBy** | **String**| Field to sort by | [optional] [default to group_name]
 **sortOrder** | **String**| Sort direction | [optional] [default to asc]

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
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the group
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
 **internalUuid** | [**String**](.md)| Internal system UUID of the group | 
 **limit** | **Number**| Maximum number of results to return | [optional] [default to 50]
 **offset** | **Number**| Number of results to skip | [optional] [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listUserAPIQuotas"></a>
# **listUserAPIQuotas**
> [UserAPIQuota] listUserAPIQuotas(opts)

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

[**[UserAPIQuota]**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="listWebhookQuotas"></a>
# **listWebhookQuotas**
> [WebhookQuota] listWebhookQuotas(opts)

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

[**[WebhookQuota]**](WebhookQuota.md)

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
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the group
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
 **internalUuid** | [**String**](.md)| Internal system UUID of the group | 
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
let body = new TmiJsClient.AddonsUserIdBody(); // AddonsUserIdBody | 
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
 **body** | [**AddonsUserIdBody**](AddonsUserIdBody.md)|  | 
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
let body = new TmiJsClient.UpdateAdminGroupRequest(); // UpdateAdminGroupRequest | 
let internalUuid = "38400000-8cf0-11bd-b23e-10b96e4ef00d"; // String | Internal system UUID of the group

apiInstance.updateAdminGroup(body, internalUuid).then((data) => {
  console.log('API called successfully. Returned data: ' + data);
}, (error) => {
  console.error(error);
});

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAdminGroupRequest**](UpdateAdminGroupRequest.md)|  | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the group | 

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
let body = new TmiJsClient.UpdateAdminUserRequest(); // UpdateAdminUserRequest | 
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
 **body** | [**UpdateAdminUserRequest**](UpdateAdminUserRequest.md)|  | 
 **internalUuid** | [**String**](.md)| Internal system UUID of the user | 

### Return type

[**AdminUser**](AdminUser.md)

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
let body = new TmiJsClient.UsersUserIdBody(); // UsersUserIdBody | 
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
 **body** | [**UsersUserIdBody**](UsersUserIdBody.md)|  | 
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
let body = new TmiJsClient.WebhooksUserIdBody(); // WebhooksUserIdBody | 
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
 **body** | [**WebhooksUserIdBody**](WebhooksUserIdBody.md)|  | 
 **userId** | [**String**](.md)| User ID | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

