# \UserAccountAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**AuthorizeContentToken**](UserAccountAPI.md#AuthorizeContentToken) | **Post** /me/content_tokens/{provider_id}/authorize | Start content provider authorization
[**ConfirmIdentityLink**](UserAccountAPI.md#ConfirmIdentityLink) | **Post** /me/identities/link/confirm | Confirm and complete an identity link
[**CreateCurrentUserPreferences**](UserAccountAPI.md#CreateCurrentUserPreferences) | **Post** /me/preferences | Create user preferences
[**DeleteMyContentToken**](UserAccountAPI.md#DeleteMyContentToken) | **Delete** /me/content_tokens/{provider_id} | Revoke linked content provider token
[**DeleteMyIdentity**](UserAccountAPI.md#DeleteMyIdentity) | **Delete** /me/identities/{id} | Unlink a linked identity
[**GetCurrentUserPreferences**](UserAccountAPI.md#GetCurrentUserPreferences) | **Get** /me/preferences | Get user preferences
[**GetPendingIdentityLink**](UserAccountAPI.md#GetPendingIdentityLink) | **Get** /me/identities/link/pending/{link_id} | Get pending identity link details
[**GrantMicrosoftFilePermission**](UserAccountAPI.md#GrantMicrosoftFilePermission) | **Post** /me/microsoft/picker_grants | Grant the TMI Entra app per-file read access to a picked OneDrive/SharePoint file.
[**ListMyContentTokens**](UserAccountAPI.md#ListMyContentTokens) | **Get** /me/content_tokens | List linked content provider tokens
[**ListMyIdentities**](UserAccountAPI.md#ListMyIdentities) | **Get** /me/identities | List current user identities
[**MintPickerToken**](UserAccountAPI.md#MintPickerToken) | **Post** /me/picker_tokens/{provider_id} | Mint a short-lived access token for the Google Picker browser client
[**StartIdentityLink**](UserAccountAPI.md#StartIdentityLink) | **Post** /me/identities/link/start | Start an identity link flow
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


## ConfirmIdentityLink

> LinkedIdentity ConfirmIdentityLink(ctx).ConfirmIdentityLinkRequest(confirmIdentityLinkRequest).Execute()

Confirm and complete an identity link



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
	confirmIdentityLinkRequest := *openapiclient.NewConfirmIdentityLinkRequest("Token_example") // ConfirmIdentityLinkRequest | 

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.ConfirmIdentityLink(context.Background()).ConfirmIdentityLinkRequest(confirmIdentityLinkRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.ConfirmIdentityLink``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ConfirmIdentityLink`: LinkedIdentity
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.ConfirmIdentityLink`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiConfirmIdentityLinkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **confirmIdentityLinkRequest** | [**ConfirmIdentityLinkRequest**](ConfirmIdentityLinkRequest.md) |  | 

### Return type

[**LinkedIdentity**](LinkedIdentity.md)

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


## DeleteMyIdentity

> DeleteMyIdentity(ctx, id).Execute()

Unlink a linked identity



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Linked identity UUID

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.UserAccountAPI.DeleteMyIdentity(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.DeleteMyIdentity``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Linked identity UUID | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteMyIdentityRequest struct via the builder pattern


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


## GetPendingIdentityLink

> PendingIdentityLinkResponse GetPendingIdentityLink(ctx, linkId).Execute()

Get pending identity link details



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
	linkId := "linkId_example" // string | Pending identity link identifier returned by the OAuth callback

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.GetPendingIdentityLink(context.Background(), linkId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.GetPendingIdentityLink``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetPendingIdentityLink`: PendingIdentityLinkResponse
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.GetPendingIdentityLink`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**linkId** | **string** | Pending identity link identifier returned by the OAuth callback | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetPendingIdentityLinkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**PendingIdentityLinkResponse**](PendingIdentityLinkResponse.md)

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


## ListMyIdentities

> MyIdentitiesResponse ListMyIdentities(ctx).Execute()

List current user identities



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
	resp, r, err := apiClient.UserAccountAPI.ListMyIdentities(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.ListMyIdentities``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListMyIdentities`: MyIdentitiesResponse
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.ListMyIdentities`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiListMyIdentitiesRequest struct via the builder pattern


### Return type

[**MyIdentitiesResponse**](MyIdentitiesResponse.md)

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


## StartIdentityLink

> IdentityLinkStartResponse StartIdentityLink(ctx).Idp(idp).ClientCallback(clientCallback).Execute()

Start an identity link flow



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
	idp := "idp_example" // string | The identity provider ID to link
	clientCallback := "clientCallback_example" // string | The URL to redirect to after the provider returns. Must be in the allowlist.

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.UserAccountAPI.StartIdentityLink(context.Background()).Idp(idp).ClientCallback(clientCallback).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `UserAccountAPI.StartIdentityLink``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `StartIdentityLink`: IdentityLinkStartResponse
	fmt.Fprintf(os.Stdout, "Response from `UserAccountAPI.StartIdentityLink`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiStartIdentityLinkRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idp** | **string** | The identity provider ID to link | 
 **clientCallback** | **string** | The URL to redirect to after the provider returns. Must be in the allowlist. | 

### Return type

[**IdentityLinkStartResponse**](IdentityLinkStartResponse.md)

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

