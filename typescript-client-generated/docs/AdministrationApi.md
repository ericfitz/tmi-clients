# AdministrationApi

All URIs are relative to *https://api.tmi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addGroupMember**](AdministrationApi.md#addgroupmemberoperation) | **POST** /admin/groups/{internal_uuid}/members | Add member to group |
| [**createAdminGroup**](AdministrationApi.md#createadmingroupoperation) | **POST** /admin/groups | Create provider-independent group |
| [**deleteAddonInvocationQuota**](AdministrationApi.md#deleteaddoninvocationquota) | **DELETE** /admin/quotas/addons/{user_id} | Delete addon invocation quota |
| [**deleteAdminGroup**](AdministrationApi.md#deleteadmingroup) | **DELETE** /admin/groups/{internal_uuid} | Delete group |
| [**deleteAdminUser**](AdministrationApi.md#deleteadminuser) | **DELETE** /admin/users/{internal_uuid} | Delete user |
| [**deleteSystemSetting**](AdministrationApi.md#deletesystemsetting) | **DELETE** /admin/settings/{key} | Delete system setting |
| [**deleteUserAPIQuota**](AdministrationApi.md#deleteuserapiquota) | **DELETE** /admin/quotas/users/{user_id} | Delete user API quota |
| [**deleteWebhookQuota**](AdministrationApi.md#deletewebhookquota) | **DELETE** /admin/quotas/webhooks/{user_id} | Delete webhook quota |
| [**getAddonInvocationQuota**](AdministrationApi.md#getaddoninvocationquota) | **GET** /admin/quotas/addons/{user_id} | Get addon invocation quota |
| [**getAdminGroup**](AdministrationApi.md#getadmingroup) | **GET** /admin/groups/{internal_uuid} | Get group details |
| [**getAdminUser**](AdministrationApi.md#getadminuser) | **GET** /admin/users/{internal_uuid} | Get user details |
| [**getSystemSetting**](AdministrationApi.md#getsystemsetting) | **GET** /admin/settings/{key} | Get system setting |
| [**getUserAPIQuota**](AdministrationApi.md#getuserapiquota) | **GET** /admin/quotas/users/{user_id} | Get user API quota |
| [**getWebhookQuota**](AdministrationApi.md#getwebhookquota) | **GET** /admin/quotas/webhooks/{user_id} | Get webhook quota |
| [**listAddonInvocationQuotas**](AdministrationApi.md#listaddoninvocationquotas) | **GET** /admin/quotas/addons | List all addon invocation quotas |
| [**listAdminGroups**](AdministrationApi.md#listadmingroups) | **GET** /admin/groups | List groups |
| [**listAdminUsers**](AdministrationApi.md#listadminusers) | **GET** /admin/users | List users |
| [**listGroupMembers**](AdministrationApi.md#listgroupmembers) | **GET** /admin/groups/{internal_uuid}/members | List group members |
| [**listSystemSettings**](AdministrationApi.md#listsystemsettings) | **GET** /admin/settings | List system settings |
| [**listUserAPIQuotas**](AdministrationApi.md#listuserapiquotas) | **GET** /admin/quotas/users | List all user API quotas |
| [**listWebhookQuotas**](AdministrationApi.md#listwebhookquotas) | **GET** /admin/quotas/webhooks | List all webhook quotas |
| [**reencryptSystemSettings**](AdministrationApi.md#reencryptsystemsettings) | **POST** /admin/settings/reencrypt | Re-encrypt all system settings |
| [**removeGroupMember**](AdministrationApi.md#removegroupmember) | **DELETE** /admin/groups/{internal_uuid}/members/{member_uuid} | Remove member from group |
| [**transferAdminUserOwnership**](AdministrationApi.md#transferadminuserownership) | **POST** /admin/users/{internal_uuid}/transfer | Transfer user ownership to another user |
| [**updateAddonInvocationQuota**](AdministrationApi.md#updateaddoninvocationquota) | **PUT** /admin/quotas/addons/{user_id} | Update addon invocation quota |
| [**updateAdminGroup**](AdministrationApi.md#updateadmingroupoperation) | **PATCH** /admin/groups/{internal_uuid} | Update group metadata |
| [**updateAdminUser**](AdministrationApi.md#updateadminuseroperation) | **PATCH** /admin/users/{internal_uuid} | Update user metadata |
| [**updateSystemSetting**](AdministrationApi.md#updatesystemsetting) | **PUT** /admin/settings/{key} | Update system setting |
| [**updateUserAPIQuota**](AdministrationApi.md#updateuserapiquota) | **PUT** /admin/quotas/users/{user_id} | Update user API quota |
| [**updateWebhookQuota**](AdministrationApi.md#updatewebhookquota) | **PUT** /admin/quotas/webhooks/{user_id} | Update webhook quota |



## addGroupMember

> GroupMember addGroupMember(internalUuid, addGroupMemberRequest)

Add member to group

Adds a user to a group. The user must exist in the system. Cannot add members to the special \&#39;everyone\&#39; pseudo-group.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { AddGroupMemberOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // AddGroupMemberRequest | Group membership update
    addGroupMemberRequest: ...,
  } satisfies AddGroupMemberOperationRequest;

  try {
    const data = await api.addGroupMember(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **addGroupMemberRequest** | [AddGroupMemberRequest](AddGroupMemberRequest.md) | Group membership update | |

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Member added successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group or user not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - User is already a member of this group |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createAdminGroup

> AdminGroup createAdminGroup(createAdminGroupRequest)

Create provider-independent group

Creates a new provider-independent group (provider&#x3D;\&quot;*\&quot;). These groups can be used across all providers for authorization and administration.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { CreateAdminGroupOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // CreateAdminGroupRequest | Group creation request
    createAdminGroupRequest: ...,
  } satisfies CreateAdminGroupOperationRequest;

  try {
    const data = await api.createAdminGroup(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdminGroupRequest** | [CreateAdminGroupRequest](CreateAdminGroupRequest.md) | Group creation request | |

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Group created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - Group already exists |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteAddonInvocationQuota

> deleteAddonInvocationQuota(userId)

Delete addon invocation quota

Deletes the custom addon invocation quota for a user, reverting to system defaults

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteAddonInvocationQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteAddonInvocationQuotaRequest;

  try {
    const data = await api.deleteAddonInvocationQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Quota deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Quota not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteAdminGroup

> deleteAdminGroup(internalUuid)

Delete group

Deletes a TMI-managed group and handles threat model cleanup. Protected groups like \&#39;everyone\&#39; cannot be deleted.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteAdminGroupRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteAdminGroupRequest;

  try {
    const data = await api.deleteAdminGroup(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Group deleted successfully (no content) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid UUID format |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Cannot delete protected group or insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteAdminUser

> deleteAdminUser(internalUuid)

Delete user

Deletes a user and all associated data. Transfers sole-owned threat models or deletes them if no other owners exist.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteAdminUserRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteAdminUserRequest;

  try {
    const data = await api.deleteAdminUser(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User deleted successfully (no content) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | User not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteSystemSetting

> deleteSystemSetting(key)

Delete system setting

Deletes a system setting. Requires administrator privileges.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteSystemSettingRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | The setting key
    key: key_example,
  } satisfies DeleteSystemSettingRequest;

  try {
    const data = await api.deleteSystemSetting(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | `string` | The setting key | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Setting deleted |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid key format (must match pattern ^[a-z][a-z0-9_.]*$) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteUserAPIQuota

> deleteUserAPIQuota(userId)

Delete user API quota

Deletes the custom API quota for a user, reverting to system defaults

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteUserAPIQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteUserAPIQuotaRequest;

  try {
    const data = await api.deleteUserAPIQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Quota deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Quota not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteWebhookQuota

> deleteWebhookQuota(userId)

Delete webhook quota

Deletes the custom webhook quota for a user, reverting to system defaults

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { DeleteWebhookQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies DeleteWebhookQuotaRequest;

  try {
    const data = await api.deleteWebhookQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Quota deleted successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Quota not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAddonInvocationQuota

> AddonInvocationQuota getAddonInvocationQuota(userId)

Get addon invocation quota

Retrieves the addon invocation quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetAddonInvocationQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetAddonInvocationQuotaRequest;

  try {
    const data = await api.getAddonInvocationQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Addon invocation quota |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAdminGroup

> AdminGroup getAdminGroup(internalUuid)

Get group details

Returns detailed information about a specific group, including enriched data (usage in authorizations and admin grants).

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetAdminGroupRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetAdminGroupRequest;

  try {
    const data = await api.getAdminGroup(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid UUID format |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAdminUser

> AdminUser getAdminUser(internalUuid)

Get user details

Returns detailed information about a specific user, including enriched data (admin status, groups, threat model counts).

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetAdminUserRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetAdminUserRequest;

  try {
    const data = await api.getAdminUser(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User details |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid UUID format |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | User not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSystemSetting

> SystemSetting getSystemSetting(key)

Get system setting

Returns a specific system setting by key. Requires administrator privileges.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetSystemSettingRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | The setting key
    key: key_example,
  } satisfies GetSystemSettingRequest;

  try {
    const data = await api.getSystemSetting(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | `string` | The setting key | [Defaults to `undefined`] |

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | System setting |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid key format (must match pattern ^[a-z][a-z0-9_.]*$) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getUserAPIQuota

> UserAPIQuota getUserAPIQuota(userId)

Get user API quota

Retrieves the API rate limit quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetUserAPIQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetUserAPIQuotaRequest;

  try {
    const data = await api.getUserAPIQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User API quota |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getWebhookQuota

> WebhookQuota getWebhookQuota(userId)

Get webhook quota

Retrieves the webhook quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { GetWebhookQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
  } satisfies GetWebhookQuotaRequest;

  try {
    const data = await api.getWebhookQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook quota |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid user ID |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listAddonInvocationQuotas

> ListAddonQuotasResponse listAddonInvocationQuotas(limit, offset)

List all addon invocation quotas

Retrieves all custom addon invocation quotas (users with non-default quotas)

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListAddonInvocationQuotasRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListAddonInvocationQuotasRequest;

  try {
    const data = await api.listAddonInvocationQuotas(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**ListAddonQuotasResponse**](ListAddonQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of addon invocation quotas |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listAdminGroups

> AdminGroupListResponse listAdminGroups(provider, groupName, usedInAuthorizations, limit, offset, sortBy, sortOrder)

List groups

Returns a paginated list of groups with optional filtering by provider, name, and usage. Includes enriched data (usage in authorizations and admin grants).

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListAdminGroupsRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Filter by OAuth/SAML provider (optional)
    provider: provider_example,
    // string | Filter by group name (case-insensitive substring match) (optional)
    groupName: groupName_example,
    // boolean | Filter groups used (true) or not used (false) in authorizations (optional)
    usedInAuthorizations: true,
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
    // 'created_at' | 'last_login' | 'email' | 'name' | Field to sort by (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' | Sort direction (optional)
    sortOrder: sortOrder_example,
  } satisfies ListAdminGroupsRequest;

  try {
    const data = await api.listAdminGroups(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **provider** | `string` | Filter by OAuth/SAML provider | [Optional] [Defaults to `undefined`] |
| **groupName** | `string` | Filter by group name (case-insensitive substring match) | [Optional] [Defaults to `undefined`] |
| **usedInAuthorizations** | `boolean` | Filter groups used (true) or not used (false) in authorizations | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |
| **sortBy** | `created_at`, `last_login`, `email`, `name` | Field to sort by | [Optional] [Defaults to `&#39;created_at&#39;`] [Enum: created_at, last_login, email, name] |
| **sortOrder** | `asc`, `desc` | Sort direction | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/plain`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of groups |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listAdminUsers

> AdminUserListResponse listAdminUsers(provider, email, name, createdAfter, createdBefore, lastLoginAfter, lastLoginBefore, limit, offset, sortBy, sortOrder, automation)

List users

Returns a paginated list of users with optional filtering by provider, email, and date ranges. Includes enriched data (admin status, groups, threat model counts).

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListAdminUsersRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Filter by OAuth/SAML provider (optional)
    provider: provider_example,
    // string | Filter by email (case-insensitive substring match) (optional)
    email: email_example,
    // string | Filter by name (case-insensitive substring match) (optional)
    name: name_example,
    // Date | Filter users created after this timestamp (RFC3339) (optional)
    createdAfter: 2013-10-20T19:20:30+01:00,
    // Date | Filter users created before this timestamp (RFC3339) (optional)
    createdBefore: 2013-10-20T19:20:30+01:00,
    // Date | Filter users who logged in after this timestamp (RFC3339) (optional)
    lastLoginAfter: 2013-10-20T19:20:30+01:00,
    // Date | Filter users who logged in before this timestamp (RFC3339) (optional)
    lastLoginBefore: 2013-10-20T19:20:30+01:00,
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
    // 'created_at' | 'last_login' | 'email' | 'name' | Field to sort by (optional)
    sortBy: sortBy_example,
    // 'asc' | 'desc' | Sort direction (optional)
    sortOrder: sortOrder_example,
    // boolean | Filter by automation account status. True returns only automation accounts, false returns only non-automation accounts. (optional)
    automation: true,
  } satisfies ListAdminUsersRequest;

  try {
    const data = await api.listAdminUsers(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **provider** | `string` | Filter by OAuth/SAML provider | [Optional] [Defaults to `undefined`] |
| **email** | `string` | Filter by email (case-insensitive substring match) | [Optional] [Defaults to `undefined`] |
| **name** | `string` | Filter by name (case-insensitive substring match) | [Optional] [Defaults to `undefined`] |
| **createdAfter** | `Date` | Filter users created after this timestamp (RFC3339) | [Optional] [Defaults to `undefined`] |
| **createdBefore** | `Date` | Filter users created before this timestamp (RFC3339) | [Optional] [Defaults to `undefined`] |
| **lastLoginAfter** | `Date` | Filter users who logged in after this timestamp (RFC3339) | [Optional] [Defaults to `undefined`] |
| **lastLoginBefore** | `Date` | Filter users who logged in before this timestamp (RFC3339) | [Optional] [Defaults to `undefined`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |
| **sortBy** | `created_at`, `last_login`, `email`, `name` | Field to sort by | [Optional] [Defaults to `&#39;created_at&#39;`] [Enum: created_at, last_login, email, name] |
| **sortOrder** | `asc`, `desc` | Sort direction | [Optional] [Defaults to `&#39;desc&#39;`] [Enum: asc, desc] |
| **automation** | `boolean` | Filter by automation account status. True returns only automation accounts, false returns only non-automation accounts. | [Optional] [Defaults to `undefined`] |

### Return type

[**AdminUserListResponse**](AdminUserListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of users |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listGroupMembers

> GroupMemberListResponse listGroupMembers(internalUuid, limit, offset)

List group members

Returns a paginated list of users who are members of the specified group. Includes user details (email, name, provider information).

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListGroupMembersRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListGroupMembersRequest;

  try {
    const data = await api.listGroupMembers(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of group members |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listSystemSettings

> Array&lt;SystemSetting&gt; listSystemSettings()

List system settings

Returns all system settings. Requires administrator privileges.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListSystemSettingsRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  try {
    const data = await api.listSystemSettings();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Array&lt;SystemSetting&gt;**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of system settings |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **400** | Bad Request - Invalid request parameters |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listUserAPIQuotas

> ListUserQuotasResponse listUserAPIQuotas(limit, offset)

List all user API quotas

Retrieves all custom API rate limit quotas (users with non-default quotas)

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListUserAPIQuotasRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListUserAPIQuotasRequest;

  try {
    const data = await api.listUserAPIQuotas(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**ListUserQuotasResponse**](ListUserQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of user API quotas |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listWebhookQuotas

> ListWebhookQuotasResponse listWebhookQuotas(limit, offset)

List all webhook quotas

Retrieves all custom webhook quotas (users with non-default quotas)

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ListWebhookQuotasRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // number | Maximum number of results to return (optional)
    limit: 56,
    // number | Number of results to skip (optional)
    offset: 56,
  } satisfies ListWebhookQuotasRequest;

  try {
    const data = await api.listWebhookQuotas(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **limit** | `number` | Maximum number of results to return | [Optional] [Defaults to `50`] |
| **offset** | `number` | Number of results to skip | [Optional] [Defaults to `0`] |

### Return type

[**ListWebhookQuotasResponse**](ListWebhookQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of webhook quotas |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## reencryptSystemSettings

> ReencryptSystemSettings200Response reencryptSystemSettings()

Re-encrypt all system settings

Re-encrypts all system settings with the current encryption key. Use this after rotating the encryption key or when first enabling encryption on existing settings. Requires administrator privileges. Settings that cannot be decrypted are reported as errors but do not prevent other settings from being processed.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { ReencryptSystemSettingsRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  try {
    const data = await api.reencryptSystemSettings();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ReencryptSystemSettings200Response**](ReencryptSystemSettings200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Re-encryption completed |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **409** | Conflict - Encryption is not enabled on this server |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |
| **400** | Bad request - Invalid or malformed request body |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## removeGroupMember

> removeGroupMember(internalUuid, memberUuid, subjectType)

Remove member from group

Removes a user or nested group from a group. Use the subject_type query parameter to specify whether the member is a user (default) or a group. Cannot remove members from the special \&#39;everyone\&#39; pseudo-group.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { RemoveGroupMemberRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // string | Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group)
    memberUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // 'user' | 'group' | Type of member to remove: \'user\' (default) for a user member, \'group\' for a nested group member (optional)
    subjectType: subjectType_example,
  } satisfies RemoveGroupMemberRequest;

  try {
    const data = await api.removeGroupMember(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **memberUuid** | `string` | Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group) | [Defaults to `undefined`] |
| **subjectType** | `user`, `group` | Type of member to remove: \&#39;user\&#39; (default) for a user member, \&#39;group\&#39; for a nested group member | [Optional] [Defaults to `&#39;user&#39;`] [Enum: user, group] |

### Return type

`void` (Empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Member removed successfully (no content) |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad request - Invalid UUID format |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group, member, or membership not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## transferAdminUserOwnership

> TransferOwnershipResult transferAdminUserOwnership(internalUuid, transferOwnershipRequest)

Transfer user ownership to another user

Transfers ownership of all threat models and survey responses owned by the specified user to the target user. The source user is downgraded to writer role on all transferred items. Requires administrator privileges.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { TransferAdminUserOwnershipRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // TransferOwnershipRequest | Ownership transfer request specifying the target user
    transferOwnershipRequest: ...,
  } satisfies TransferAdminUserOwnershipRequest;

  try {
    const data = await api.transferAdminUserOwnership(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **transferOwnershipRequest** | [TransferOwnershipRequest](TransferOwnershipRequest.md) | Ownership transfer request specifying the target user | |

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ownership transferred successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters or attempting to transfer to same user |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Source or target user not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateAddonInvocationQuota

> AddonInvocationQuota updateAddonInvocationQuota(userId, addonQuotaUpdate)

Update addon invocation quota

Creates or updates the addon invocation quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateAddonInvocationQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // AddonQuotaUpdate | Addon quota update configuration
    addonQuotaUpdate: {"max_active_invocations":5,"max_invocations_per_hour":100},
  } satisfies UpdateAddonInvocationQuotaRequest;

  try {
    const data = await api.updateAddonInvocationQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |
| **addonQuotaUpdate** | [AddonQuotaUpdate](AddonQuotaUpdate.md) | Addon quota update configuration | |

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quota updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **201** | Quota created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateAdminGroup

> AdminGroup updateAdminGroup(internalUuid, updateAdminGroupRequest)

Update group metadata

Updates group metadata fields (name, description). Only provided fields are updated.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateAdminGroupOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // UpdateAdminGroupRequest | Group update details
    updateAdminGroupRequest: ...,
  } satisfies UpdateAdminGroupOperationRequest;

  try {
    const data = await api.updateAdminGroup(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **updateAdminGroupRequest** | [UpdateAdminGroupRequest](UpdateAdminGroupRequest.md) | Group update details | |

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | Group not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateAdminUser

> AdminUser updateAdminUser(internalUuid, updateAdminUserRequest)

Update user metadata

Updates user metadata fields (email, name, email_verified). Only provided fields are updated.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateAdminUserOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | Internal system UUID of the user
    internalUuid: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // UpdateAdminUserRequest | User profile update
    updateAdminUserRequest: ...,
  } satisfies UpdateAdminUserOperationRequest;

  try {
    const data = await api.updateAdminUser(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **internalUuid** | `string` | Internal system UUID of the user | [Defaults to `undefined`] |
| **updateAdminUserRequest** | [UpdateAdminUserRequest](UpdateAdminUserRequest.md) | User profile update | |

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **404** | User not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateSystemSetting

> SystemSetting updateSystemSetting(key, systemSettingUpdate)

Update system setting

Creates or updates a system setting. Requires administrator privileges.

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateSystemSettingRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | The setting key
    key: key_example,
    // SystemSettingUpdate | The system setting value to create or update
    systemSettingUpdate: ...,
  } satisfies UpdateSystemSettingRequest;

  try {
    const data = await api.updateSystemSetting(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | `string` | The setting key | [Defaults to `undefined`] |
| **systemSettingUpdate** | [SystemSettingUpdate](SystemSettingUpdate.md) | The system setting value to create or update | |

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Setting updated |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized - Invalid or missing authentication token |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Error response |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **429** | Too Many Requests - Rate limit exceeded. The client has sent too many requests in a given amount of time. See rate limit headers for details. |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix timestamp (seconds since epoch) when the rate limit window resets <br>  * Retry-After - Number of seconds to wait before retrying the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateUserAPIQuota

> UserAPIQuota updateUserAPIQuota(userId, userQuotaUpdate)

Update user API quota

Creates or updates the API rate limit quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateUserAPIQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // UserQuotaUpdate | User quota update configuration
    userQuotaUpdate: {"max_requests_per_minute":60,"max_requests_per_hour":1000},
  } satisfies UpdateUserAPIQuotaRequest;

  try {
    const data = await api.updateUserAPIQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |
| **userQuotaUpdate** | [UserQuotaUpdate](UserQuotaUpdate.md) | User quota update configuration | |

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quota updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **201** | Quota created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateWebhookQuota

> WebhookQuota updateWebhookQuota(userId, webhookQuotaUpdate)

Update webhook quota

Creates or updates the webhook quota for a specific user

### Example

```ts
import {
  Configuration,
  AdministrationApi,
} from '@tmiclient/client';
import type { UpdateWebhookQuotaRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AdministrationApi(config);

  const body = {
    // string | User ID
    userId: 38400000-8cf0-11bd-b23e-10b96e4ef00d,
    // WebhookQuotaUpdate | Webhook quota update configuration
    webhookQuotaUpdate: {"max_subscriptions":10,"max_events_per_minute":100,"max_subscription_requests_per_minute":10,"max_subscription_requests_per_day":100},
  } satisfies UpdateWebhookQuotaRequest;

  try {
    const data = await api.updateWebhookQuota(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userId** | `string` | User ID | [Defaults to `undefined`] |
| **webhookQuotaUpdate** | [WebhookQuotaUpdate](WebhookQuotaUpdate.md) | Webhook quota update configuration | |

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quota updated successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **201** | Quota created successfully |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **400** | Bad Request - Invalid parameters, malformed UUIDs, or validation failures |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **401** | Unauthorized |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **403** | Forbidden - Insufficient permissions to access this resource |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |
| **500** | Internal server error |  -  |
| **429** | Too many requests - rate limit exceeded |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  * Retry-After - Seconds until rate limit resets <br>  |
| **404** | Resource not found |  * X-RateLimit-Limit - Maximum number of requests allowed in the current time window <br>  * X-RateLimit-Remaining - Number of requests remaining in the current time window <br>  * X-RateLimit-Reset - Unix epoch seconds when the rate limit window resets <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

