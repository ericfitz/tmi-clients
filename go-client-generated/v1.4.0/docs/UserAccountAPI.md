# \UserAccountAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateCurrentUserPreferences**](UserAccountAPI.md#CreateCurrentUserPreferences) | **Post** /me/preferences | Create user preferences
[**GetCurrentUserPreferences**](UserAccountAPI.md#GetCurrentUserPreferences) | **Get** /me/preferences | Get user preferences
[**UpdateCurrentUserPreferences**](UserAccountAPI.md#UpdateCurrentUserPreferences) | **Put** /me/preferences | Update user preferences



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

