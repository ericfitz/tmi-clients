# \UserAccountAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeContentToken**](UserAccountAPI.md#AuthorizeContentToken) | **Post** /me/content_tokens/{provider_id}/authorize | Start content provider authorization
[**CreateCurrentUserPreferences**](UserAccountAPI.md#CreateCurrentUserPreferences) | **Post** /me/preferences | Create user preferences
[**DeleteMyContentToken**](UserAccountAPI.md#DeleteMyContentToken) | **Delete** /me/content_tokens/{provider_id} | Revoke linked content provider token
[**GetCurrentUserPreferences**](UserAccountAPI.md#GetCurrentUserPreferences) | **Get** /me/preferences | Get user preferences
[**GrantMicrosoftFilePermission**](UserAccountAPI.md#GrantMicrosoftFilePermission) | **Post** /me/microsoft/picker_grants | Grant the TMI Entra app per-file read access to a picked OneDrive/SharePoint file.
[**ListMyContentTokens**](UserAccountAPI.md#ListMyContentTokens) | **Get** /me/content_tokens | List linked content provider tokens
[**MintPickerToken**](UserAccountAPI.md#MintPickerToken) | **Post** /me/picker_tokens/{provider_id} | Mint a short-lived access token for the Google Picker browser client
[**UpdateCurrentUserPreferences**](UserAccountAPI.md#UpdateCurrentUserPreferences) | **Put** /me/preferences | Update user preferences



## AuthorizeContentToken

> ContentAuthorizationURL AuthorizeContentToken(ctx, providerId).AuthorizeContentTokenRequest(authorizeContentTokenRequest).Execute()

Start content provider authorization



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
	providerId := "providerId_example" // string | Content OAuth provider id (e.g., 'confluence').
	authorizeContentTokenRequest := *openapiclient.NewAuthorizeContentTokenRequest("http://localhost:4200/oauth2/content-callback") // AuthorizeContentTokenRequest | Authorization parameters including the post-callback client URL.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.AuthorizeContentToken(context.Background(), providerId).AuthorizeContentTokenRequest(authorizeContentTokenRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.AuthorizeContentToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `AuthorizeContentToken`: ContentAuthorizationURL
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.AuthorizeContentToken`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**providerId** | **string** | Content OAuth provider id (e.g., &#39;confluence&#39;). | 

### Other Parameters

Other parameters are passed through a pointer to a apiAuthorizeContentTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **authorizeContentTokenRequest** | [**AuthorizeContentTokenRequest**](AuthorizeContentTokenRequest.md) | Authorization parameters including the post-callback client URL. | 

### Return type

[**ContentAuthorizationURL**](ContentAuthorizationURL.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateCurrentUserPreferences

> map[string]map[string]interface{} CreateCurrentUserPreferences(ctx).RequestBody(requestBody).Execute()

Create user preferences



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
	requestBody := map[string]map[string]interface{}{"key": map[string]interface{}{"key": interface{}(123)}} // map[string]map[string]interface{} | User preferences to create. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.CreateCurrentUserPreferences(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.CreateCurrentUserPreferences``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateCurrentUserPreferences`: map[string]map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.CreateCurrentUserPreferences`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateCurrentUserPreferencesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]map[string]interface{}** | User preferences to create. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name. | 

### Return type

[**map[string]map[string]interface{}**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteMyContentToken

> DeleteMyContentToken(ctx, providerId).Execute()

Revoke linked content provider token



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
	providerId := "providerId_example" // string | Content OAuth provider id to revoke.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.UserAccountAPI.DeleteMyContentToken(context.Background(), providerId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.DeleteMyContentToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**providerId** | **string** | Content OAuth provider id to revoke. | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteMyContentTokenRequest struct via the builder pattern


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


## GetCurrentUserPreferences

> map[string]map[string]interface{} GetCurrentUserPreferences(ctx).Execute()

Get user preferences



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
	resp, r, err := apiClient.UserAccountAPI.GetCurrentUserPreferences(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.GetCurrentUserPreferences``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetCurrentUserPreferences`: map[string]map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.GetCurrentUserPreferences`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetCurrentUserPreferencesRequest struct via the builder pattern


### Return type

[**map[string]map[string]interface{}**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GrantMicrosoftFilePermission

> MicrosoftPickerGrantResponse GrantMicrosoftFilePermission(ctx).MicrosoftPickerGrantRequest(microsoftPickerGrantRequest).Execute()

Grant the TMI Entra app per-file read access to a picked OneDrive/SharePoint file.



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
	microsoftPickerGrantRequest := *openapiclient.NewMicrosoftPickerGrantRequest("DriveId_example", "ItemId_example") // MicrosoftPickerGrantRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.GrantMicrosoftFilePermission(context.Background()).MicrosoftPickerGrantRequest(microsoftPickerGrantRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.GrantMicrosoftFilePermission``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GrantMicrosoftFilePermission`: MicrosoftPickerGrantResponse
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.GrantMicrosoftFilePermission`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGrantMicrosoftFilePermissionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoftPickerGrantRequest** | [**MicrosoftPickerGrantRequest**](MicrosoftPickerGrantRequest.md) |  | 

### Return type

[**MicrosoftPickerGrantResponse**](MicrosoftPickerGrantResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListMyContentTokens

> ContentTokenList ListMyContentTokens(ctx).Execute()

List linked content provider tokens



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
	resp, r, err := apiClient.UserAccountAPI.ListMyContentTokens(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.ListMyContentTokens``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMyContentTokens`: ContentTokenList
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.ListMyContentTokens`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListMyContentTokensRequest struct via the builder pattern


### Return type

[**ContentTokenList**](ContentTokenList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## MintPickerToken

> PickerTokenResponse MintPickerToken(ctx, providerId).Execute()

Mint a short-lived access token for the Google Picker browser client



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
	providerId := "providerId_example" // string | Content OAuth provider id (currently only 'google_workspace')

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.MintPickerToken(context.Background(), providerId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.MintPickerToken``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `MintPickerToken`: PickerTokenResponse
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.MintPickerToken`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**providerId** | **string** | Content OAuth provider id (currently only &#39;google_workspace&#39;) | 

### Other Parameters

Other parameters are passed through a pointer to a apiMintPickerTokenRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PickerTokenResponse**](PickerTokenResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateCurrentUserPreferences

> map[string]map[string]interface{} UpdateCurrentUserPreferences(ctx).RequestBody(requestBody).Execute()

Update user preferences



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
	requestBody := map[string]map[string]interface{}{"key": map[string]interface{}{"key": interface{}(123)}} // map[string]map[string]interface{} | User preferences to create or replace. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.UpdateCurrentUserPreferences(context.Background()).RequestBody(requestBody).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.UpdateCurrentUserPreferences``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateCurrentUserPreferences`: map[string]map[string]interface{}
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.UpdateCurrentUserPreferences`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiUpdateCurrentUserPreferencesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requestBody** | **map[string]map[string]interface{}** | User preferences to create or replace. Must be valid JSON not exceeding 1KB. Client keys must follow the pattern client-id:key-name. | 

### Return type

[**map[string]map[string]interface{}**](map.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

