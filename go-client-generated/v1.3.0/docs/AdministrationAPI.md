# \AdministrationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AddGroupMember**](AdministrationAPI.md#AddGroupMember) | **Post** /admin/groups/{internal_uuid}/members | Add member to group
[**CreateAdminGroup**](AdministrationAPI.md#CreateAdminGroup) | **Post** /admin/groups | Create provider-independent group
[**DeleteAddonInvocationQuota**](AdministrationAPI.md#DeleteAddonInvocationQuota) | **Delete** /admin/quotas/addons/{user_id} | Delete addon invocation quota
[**DeleteAdminGroup**](AdministrationAPI.md#DeleteAdminGroup) | **Delete** /admin/groups/{internal_uuid} | Delete group
[**DeleteAdminUser**](AdministrationAPI.md#DeleteAdminUser) | **Delete** /admin/users/{internal_uuid} | Delete user
[**DeleteSystemSetting**](AdministrationAPI.md#DeleteSystemSetting) | **Delete** /admin/settings/{key} | Delete system setting
[**DeleteUserAPIQuota**](AdministrationAPI.md#DeleteUserAPIQuota) | **Delete** /admin/quotas/users/{user_id} | Delete user API quota
[**DeleteWebhookQuota**](AdministrationAPI.md#DeleteWebhookQuota) | **Delete** /admin/quotas/webhooks/{user_id} | Delete webhook quota
[**GetAddonInvocationQuota**](AdministrationAPI.md#GetAddonInvocationQuota) | **Get** /admin/quotas/addons/{user_id} | Get addon invocation quota
[**GetAdminGroup**](AdministrationAPI.md#GetAdminGroup) | **Get** /admin/groups/{internal_uuid} | Get group details
[**GetAdminUser**](AdministrationAPI.md#GetAdminUser) | **Get** /admin/users/{internal_uuid} | Get user details
[**GetSystemSetting**](AdministrationAPI.md#GetSystemSetting) | **Get** /admin/settings/{key} | Get system setting
[**GetUserAPIQuota**](AdministrationAPI.md#GetUserAPIQuota) | **Get** /admin/quotas/users/{user_id} | Get user API quota
[**GetWebhookQuota**](AdministrationAPI.md#GetWebhookQuota) | **Get** /admin/quotas/webhooks/{user_id} | Get webhook quota
[**ListAddonInvocationQuotas**](AdministrationAPI.md#ListAddonInvocationQuotas) | **Get** /admin/quotas/addons | List all addon invocation quotas
[**ListAdminGroups**](AdministrationAPI.md#ListAdminGroups) | **Get** /admin/groups | List groups
[**ListAdminUsers**](AdministrationAPI.md#ListAdminUsers) | **Get** /admin/users | List users
[**ListGroupMembers**](AdministrationAPI.md#ListGroupMembers) | **Get** /admin/groups/{internal_uuid}/members | List group members
[**ListSystemSettings**](AdministrationAPI.md#ListSystemSettings) | **Get** /admin/settings | List system settings
[**ListUserAPIQuotas**](AdministrationAPI.md#ListUserAPIQuotas) | **Get** /admin/quotas/users | List all user API quotas
[**ListWebhookQuotas**](AdministrationAPI.md#ListWebhookQuotas) | **Get** /admin/quotas/webhooks | List all webhook quotas
[**MigrateSystemSettings**](AdministrationAPI.md#MigrateSystemSettings) | **Post** /admin/settings/migrate | Migrate settings from configuration
[**ReencryptSystemSettings**](AdministrationAPI.md#ReencryptSystemSettings) | **Post** /admin/settings/reencrypt | Re-encrypt all system settings
[**RemoveGroupMember**](AdministrationAPI.md#RemoveGroupMember) | **Delete** /admin/groups/{internal_uuid}/members/{member_uuid} | Remove member from group
[**TransferAdminUserOwnership**](AdministrationAPI.md#TransferAdminUserOwnership) | **Post** /admin/users/{internal_uuid}/transfer | Transfer user ownership to another user
[**UpdateAddonInvocationQuota**](AdministrationAPI.md#UpdateAddonInvocationQuota) | **Put** /admin/quotas/addons/{user_id} | Update addon invocation quota
[**UpdateAdminGroup**](AdministrationAPI.md#UpdateAdminGroup) | **Patch** /admin/groups/{internal_uuid} | Update group metadata
[**UpdateAdminUser**](AdministrationAPI.md#UpdateAdminUser) | **Patch** /admin/users/{internal_uuid} | Update user metadata
[**UpdateSystemSetting**](AdministrationAPI.md#UpdateSystemSetting) | **Put** /admin/settings/{key} | Update system setting
[**UpdateUserAPIQuota**](AdministrationAPI.md#UpdateUserAPIQuota) | **Put** /admin/quotas/users/{user_id} | Update user API quota
[**UpdateWebhookQuota**](AdministrationAPI.md#UpdateWebhookQuota) | **Put** /admin/quotas/webhooks/{user_id} | Update webhook quota



## AddGroupMember

> GroupMember AddGroupMember(ctx, internalUuid).AddGroupMemberRequest(addGroupMemberRequest).Execute()

Add member to group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	addGroupMemberRequest := *openapiclient.NewAddGroupMemberRequest() // AddGroupMemberRequest | Group membership update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.AddGroupMember(context.Background(), internalUuid).AddGroupMemberRequest(addGroupMemberRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.AddGroupMember``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AddGroupMember`: GroupMember
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.AddGroupMember`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiAddGroupMemberRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **addGroupMemberRequest** | [**AddGroupMemberRequest**](AddGroupMemberRequest.md) | Group membership update | 

### Return type

[**GroupMember**](GroupMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateAdminGroup

> AdminGroup CreateAdminGroup(ctx).CreateAdminGroupRequest(createAdminGroupRequest).Execute()

Create provider-independent group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	createAdminGroupRequest := *openapiclient.NewCreateAdminGroupRequest("GroupName_example", "Name_example") // CreateAdminGroupRequest | Group creation request

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.CreateAdminGroup(context.Background()).CreateAdminGroupRequest(createAdminGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.CreateAdminGroup``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAdminGroup`: AdminGroup
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.CreateAdminGroup`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAdminGroupRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAdminGroupRequest** | [**CreateAdminGroupRequest**](CreateAdminGroupRequest.md) | Group creation request | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAddonInvocationQuota

> DeleteAddonInvocationQuota(ctx, userId).Execute()

Delete addon invocation quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteAddonInvocationQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteAddonInvocationQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAddonInvocationQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAdminGroup

> DeleteAdminGroup(ctx, internalUuid).Execute()

Delete group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteAdminGroup(context.Background(), internalUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteAdminGroup``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAdminGroupRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAdminUser

> DeleteAdminUser(ctx, internalUuid).Execute()

Delete user



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteAdminUser(context.Background(), internalUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteAdminUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAdminUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteSystemSetting

> DeleteSystemSetting(ctx, key).Execute()

Delete system setting



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	key := "key_example" // string | The setting key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteSystemSetting(context.Background(), key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteSystemSetting``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** | The setting key | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteSystemSettingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteUserAPIQuota

> DeleteUserAPIQuota(ctx, userId).Execute()

Delete user API quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteUserAPIQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteUserAPIQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteUserAPIQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteWebhookQuota

> DeleteWebhookQuota(ctx, userId).Execute()

Delete webhook quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.DeleteWebhookQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.DeleteWebhookQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteWebhookQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAddonInvocationQuota

> AddonInvocationQuota GetAddonInvocationQuota(ctx, userId).Execute()

Get addon invocation quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetAddonInvocationQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetAddonInvocationQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAddonInvocationQuota`: AddonInvocationQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetAddonInvocationQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAddonInvocationQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAdminGroup

> AdminGroup GetAdminGroup(ctx, internalUuid).Execute()

Get group details



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetAdminGroup(context.Background(), internalUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetAdminGroup``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAdminGroup`: AdminGroup
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetAdminGroup`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAdminGroupRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAdminUser

> AdminUser GetAdminUser(ctx, internalUuid).Execute()

Get user details



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetAdminUser(context.Background(), internalUuid).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetAdminUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAdminUser`: AdminUser
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetAdminUser`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAdminUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetSystemSetting

> SystemSetting GetSystemSetting(ctx, key).Execute()

Get system setting



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	key := "key_example" // string | The setting key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetSystemSetting(context.Background(), key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetSystemSetting``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetSystemSetting`: SystemSetting
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetSystemSetting`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** | The setting key | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetSystemSettingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetUserAPIQuota

> UserAPIQuota GetUserAPIQuota(ctx, userId).Execute()

Get user API quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetUserAPIQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetUserAPIQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetUserAPIQuota`: UserAPIQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetUserAPIQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetUserAPIQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetWebhookQuota

> WebhookQuota GetWebhookQuota(ctx, userId).Execute()

Get webhook quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.GetWebhookQuota(context.Background(), userId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.GetWebhookQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetWebhookQuota`: WebhookQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.GetWebhookQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetWebhookQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAddonInvocationQuotas

> ListAddonQuotasResponse ListAddonInvocationQuotas(ctx).Limit(limit).Offset(offset).Execute()

List all addon invocation quotas



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListAddonInvocationQuotas(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListAddonInvocationQuotas``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAddonInvocationQuotas`: ListAddonQuotasResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListAddonInvocationQuotas`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAddonInvocationQuotasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAddonQuotasResponse**](ListAddonQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAdminGroups

> AdminGroupListResponse ListAdminGroups(ctx).Provider(provider).GroupName(groupName).UsedInAuthorizations(usedInAuthorizations).Limit(limit).Offset(offset).SortBy(sortBy).SortOrder(sortOrder).Execute()

List groups



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	provider := "provider_example" // string | Filter by OAuth/SAML provider (optional)
	groupName := "groupName_example" // string | Filter by group name (case-insensitive substring match) (optional)
	usedInAuthorizations := true // bool | Filter groups used (true) or not used (false) in authorizations (optional)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sortBy := "sortBy_example" // string | Field to sort by (optional) (default to "created_at")
	sortOrder := "sortOrder_example" // string | Sort direction (optional) (default to "desc")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListAdminGroups(context.Background()).Provider(provider).GroupName(groupName).UsedInAuthorizations(usedInAuthorizations).Limit(limit).Offset(offset).SortBy(sortBy).SortOrder(sortOrder).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListAdminGroups``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAdminGroups`: AdminGroupListResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListAdminGroups`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAdminGroupsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **string** | Filter by OAuth/SAML provider | 
 **groupName** | **string** | Filter by group name (case-insensitive substring match) | 
 **usedInAuthorizations** | **bool** | Filter groups used (true) or not used (false) in authorizations | 
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **sortBy** | **string** | Field to sort by | [default to &quot;created_at&quot;]
 **sortOrder** | **string** | Sort direction | [default to &quot;desc&quot;]

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAdminUsers

> AdminUserListResponse ListAdminUsers(ctx).Provider(provider).Email(email).Name(name).CreatedAfter(createdAfter).CreatedBefore(createdBefore).LastLoginAfter(lastLoginAfter).LastLoginBefore(lastLoginBefore).Limit(limit).Offset(offset).SortBy(sortBy).SortOrder(sortOrder).Automation(automation).Execute()

List users



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	provider := "provider_example" // string | Filter by OAuth/SAML provider (optional)
	email := "email_example" // string | Filter by email (case-insensitive substring match) (optional)
	name := "name_example" // string | Filter by name (case-insensitive substring match) (optional)
	createdAfter := time.Now() // time.Time | Filter users created after this timestamp (RFC3339) (optional)
	createdBefore := time.Now() // time.Time | Filter users created before this timestamp (RFC3339) (optional)
	lastLoginAfter := time.Now() // time.Time | Filter users who logged in after this timestamp (RFC3339) (optional)
	lastLoginBefore := time.Now() // time.Time | Filter users who logged in before this timestamp (RFC3339) (optional)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sortBy := "sortBy_example" // string | Field to sort by (optional) (default to "created_at")
	sortOrder := "sortOrder_example" // string | Sort direction (optional) (default to "desc")
	automation := true // bool | Filter by automation account status. True returns only automation accounts, false returns only non-automation accounts. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListAdminUsers(context.Background()).Provider(provider).Email(email).Name(name).CreatedAfter(createdAfter).CreatedBefore(createdBefore).LastLoginAfter(lastLoginAfter).LastLoginBefore(lastLoginBefore).Limit(limit).Offset(offset).SortBy(sortBy).SortOrder(sortOrder).Automation(automation).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListAdminUsers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAdminUsers`: AdminUserListResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListAdminUsers`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAdminUsersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **string** | Filter by OAuth/SAML provider | 
 **email** | **string** | Filter by email (case-insensitive substring match) | 
 **name** | **string** | Filter by name (case-insensitive substring match) | 
 **createdAfter** | **time.Time** | Filter users created after this timestamp (RFC3339) | 
 **createdBefore** | **time.Time** | Filter users created before this timestamp (RFC3339) | 
 **lastLoginAfter** | **time.Time** | Filter users who logged in after this timestamp (RFC3339) | 
 **lastLoginBefore** | **time.Time** | Filter users who logged in before this timestamp (RFC3339) | 
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **sortBy** | **string** | Field to sort by | [default to &quot;created_at&quot;]
 **sortOrder** | **string** | Sort direction | [default to &quot;desc&quot;]
 **automation** | **bool** | Filter by automation account status. True returns only automation accounts, false returns only non-automation accounts. | 

### Return type

[**AdminUserListResponse**](AdminUserListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListGroupMembers

> GroupMemberListResponse ListGroupMembers(ctx, internalUuid).Limit(limit).Offset(offset).Execute()

List group members



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListGroupMembers(context.Background(), internalUuid).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListGroupMembers``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListGroupMembers`: GroupMemberListResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListGroupMembers`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiListGroupMembersRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**GroupMemberListResponse**](GroupMemberListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListSystemSettings

> []SystemSetting ListSystemSettings(ctx).Execute()

List system settings



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListSystemSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListSystemSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListSystemSettings`: []SystemSetting
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListSystemSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListSystemSettingsRequest struct via the builder pattern


### Return type

[**[]SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListUserAPIQuotas

> ListUserQuotasResponse ListUserAPIQuotas(ctx).Limit(limit).Offset(offset).Execute()

List all user API quotas



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListUserAPIQuotas(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListUserAPIQuotas``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListUserAPIQuotas`: ListUserQuotasResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListUserAPIQuotas`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListUserAPIQuotasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListUserQuotasResponse**](ListUserQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListWebhookQuotas

> ListWebhookQuotasResponse ListWebhookQuotas(ctx).Limit(limit).Offset(offset).Execute()

List all webhook quotas



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 50)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ListWebhookQuotas(context.Background()).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ListWebhookQuotas``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListWebhookQuotas`: ListWebhookQuotasResponse
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ListWebhookQuotas`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListWebhookQuotasRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 50]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListWebhookQuotasResponse**](ListWebhookQuotasResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MigrateSystemSettings

> MigrateSystemSettings200Response MigrateSystemSettings(ctx).Overwrite(overwrite).Execute()

Migrate settings from configuration



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	overwrite := true // bool | If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don't already exist. (optional) (default to false)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.MigrateSystemSettings(context.Background()).Overwrite(overwrite).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.MigrateSystemSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MigrateSystemSettings`: MigrateSystemSettings200Response
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.MigrateSystemSettings`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiMigrateSystemSettingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **overwrite** | **bool** | If true, overwrite existing settings in the database with values from configuration. If false or omitted, only add settings that don&#39;t already exist. | [default to false]

### Return type

[**MigrateSystemSettings200Response**](MigrateSystemSettings200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ReencryptSystemSettings

> ReencryptSystemSettings200Response ReencryptSystemSettings(ctx).Execute()

Re-encrypt all system settings



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.ReencryptSystemSettings(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.ReencryptSystemSettings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ReencryptSystemSettings`: ReencryptSystemSettings200Response
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.ReencryptSystemSettings`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiReencryptSystemSettingsRequest struct via the builder pattern


### Return type

[**ReencryptSystemSettings200Response**](ReencryptSystemSettings200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RemoveGroupMember

> RemoveGroupMember(ctx, internalUuid, memberUuid).SubjectType(subjectType).Execute()

Remove member from group



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	memberUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group)
	subjectType := "subjectType_example" // string | Type of member to remove: 'user' (default) for a user member, 'group' for a nested group member (optional) (default to "user")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AdministrationAPI.RemoveGroupMember(context.Background(), internalUuid, memberUuid).SubjectType(subjectType).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.RemoveGroupMember``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 
**memberUuid** | **string** | Internal system UUID of the member to remove (user UUID when subject_type is user, group UUID when subject_type is group) | 

### Other Parameters

Other parameters are passed through a pointer to a apiRemoveGroupMemberRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **subjectType** | **string** | Type of member to remove: &#39;user&#39; (default) for a user member, &#39;group&#39; for a nested group member | [default to &quot;user&quot;]

### Return type

 (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## TransferAdminUserOwnership

> TransferOwnershipResult TransferAdminUserOwnership(ctx, internalUuid).TransferOwnershipRequest(transferOwnershipRequest).Execute()

Transfer user ownership to another user



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	transferOwnershipRequest := *openapiclient.NewTransferOwnershipRequest("550e8400-e29b-41d4-a716-446655440000") // TransferOwnershipRequest | Ownership transfer request specifying the target user

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.TransferAdminUserOwnership(context.Background(), internalUuid).TransferOwnershipRequest(transferOwnershipRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.TransferAdminUserOwnership``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `TransferAdminUserOwnership`: TransferOwnershipResult
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.TransferAdminUserOwnership`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiTransferAdminUserOwnershipRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **transferOwnershipRequest** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md) | Ownership transfer request specifying the target user | 

### Return type

[**TransferOwnershipResult**](TransferOwnershipResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAddonInvocationQuota

> AddonInvocationQuota UpdateAddonInvocationQuota(ctx, userId).AddonQuotaUpdate(addonQuotaUpdate).Execute()

Update addon invocation quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID
	addonQuotaUpdate := *openapiclient.NewAddonQuotaUpdate(int32(10), int32(1000)) // AddonQuotaUpdate | Addon quota update configuration

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateAddonInvocationQuota(context.Background(), userId).AddonQuotaUpdate(addonQuotaUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateAddonInvocationQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAddonInvocationQuota`: AddonInvocationQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateAddonInvocationQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAddonInvocationQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **addonQuotaUpdate** | [**AddonQuotaUpdate**](AddonQuotaUpdate.md) | Addon quota update configuration | 

### Return type

[**AddonInvocationQuota**](AddonInvocationQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAdminGroup

> AdminGroup UpdateAdminGroup(ctx, internalUuid).UpdateAdminGroupRequest(updateAdminGroupRequest).Execute()

Update group metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	updateAdminGroupRequest := *openapiclient.NewUpdateAdminGroupRequest() // UpdateAdminGroupRequest | Group update details

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateAdminGroup(context.Background(), internalUuid).UpdateAdminGroupRequest(updateAdminGroupRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateAdminGroup``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAdminGroup`: AdminGroup
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateAdminGroup`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAdminGroupRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateAdminGroupRequest** | [**UpdateAdminGroupRequest**](UpdateAdminGroupRequest.md) | Group update details | 

### Return type

[**AdminGroup**](AdminGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAdminUser

> AdminUser UpdateAdminUser(ctx, internalUuid).UpdateAdminUserRequest(updateAdminUserRequest).Execute()

Update user metadata



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	internalUuid := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Internal system UUID of the user
	updateAdminUserRequest := *openapiclient.NewUpdateAdminUserRequest() // UpdateAdminUserRequest | User profile update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateAdminUser(context.Background(), internalUuid).UpdateAdminUserRequest(updateAdminUserRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateAdminUser``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAdminUser`: AdminUser
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateAdminUser`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**internalUuid** | **string** | Internal system UUID of the user | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAdminUserRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **updateAdminUserRequest** | [**UpdateAdminUserRequest**](UpdateAdminUserRequest.md) | User profile update | 

### Return type

[**AdminUser**](AdminUser.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateSystemSetting

> SystemSetting UpdateSystemSetting(ctx, key).SystemSettingUpdate(systemSettingUpdate).Execute()

Update system setting



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	key := "key_example" // string | The setting key
	systemSettingUpdate := *openapiclient.NewSystemSettingUpdate("Value_example", "Type_example") // SystemSettingUpdate | The system setting value to create or update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateSystemSetting(context.Background(), key).SystemSettingUpdate(systemSettingUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateSystemSetting``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateSystemSetting`: SystemSetting
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateSystemSetting`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**key** | **string** | The setting key | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateSystemSettingRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **systemSettingUpdate** | [**SystemSettingUpdate**](SystemSettingUpdate.md) | The system setting value to create or update | 

### Return type

[**SystemSetting**](SystemSetting.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateUserAPIQuota

> UserAPIQuota UpdateUserAPIQuota(ctx, userId).UserQuotaUpdate(userQuotaUpdate).Execute()

Update user API quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID
	userQuotaUpdate := *openapiclient.NewUserQuotaUpdate(int32(60)) // UserQuotaUpdate | User quota update configuration

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateUserAPIQuota(context.Background(), userId).UserQuotaUpdate(userQuotaUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateUserAPIQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateUserAPIQuota`: UserAPIQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateUserAPIQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateUserAPIQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **userQuotaUpdate** | [**UserQuotaUpdate**](UserQuotaUpdate.md) | User quota update configuration | 

### Return type

[**UserAPIQuota**](UserAPIQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateWebhookQuota

> WebhookQuota UpdateWebhookQuota(ctx, userId).WebhookQuotaUpdate(webhookQuotaUpdate).Execute()

Update webhook quota



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/ericfitz/tmi-clients/go-client-generated"
)

func main() {
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | User ID
	webhookQuotaUpdate := *openapiclient.NewWebhookQuotaUpdate(int32(5), int32(100), int32(60), int32(1440)) // WebhookQuotaUpdate | Webhook quota update configuration

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AdministrationAPI.UpdateWebhookQuota(context.Background(), userId).WebhookQuotaUpdate(webhookQuotaUpdate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AdministrationAPI.UpdateWebhookQuota``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateWebhookQuota`: WebhookQuota
	fmt.Fprintf(os.Stdout, "Response from `AdministrationAPI.UpdateWebhookQuota`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**userId** | **string** | User ID | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateWebhookQuotaRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **webhookQuotaUpdate** | [**WebhookQuotaUpdate**](WebhookQuotaUpdate.md) | Webhook quota update configuration | 

### Return type

[**WebhookQuota**](WebhookQuota.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

