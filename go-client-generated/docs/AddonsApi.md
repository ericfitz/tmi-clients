# \AddonsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateAddon**](AddonsAPI.md#CreateAddon) | **Post** /addons | Create add-on
[**DeleteAddon**](AddonsAPI.md#DeleteAddon) | **Delete** /addons/{id} | Delete add-on
[**GetAddon**](AddonsAPI.md#GetAddon) | **Get** /addons/{id} | Get add-on
[**InvokeAddon**](AddonsAPI.md#InvokeAddon) | **Post** /addons/{id}/invoke | Invoke add-on
[**ListAddons**](AddonsAPI.md#ListAddons) | **Get** /addons | List add-ons



## CreateAddon

> AddonResponse CreateAddon(ctx).CreateAddonRequest(createAddonRequest).Execute()

Create add-on



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
	createAddonRequest := *openapiclient.NewCreateAddonRequest("Name_example", "WebhookId_example") // CreateAddonRequest | Addon registration details

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AddonsAPI.CreateAddon(context.Background()).CreateAddonRequest(createAddonRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AddonsAPI.CreateAddon``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAddon`: AddonResponse
	fmt.Fprintf(os.Stdout, "Response from `AddonsAPI.CreateAddon`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAddonRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAddonRequest** | [**CreateAddonRequest**](CreateAddonRequest.md) | Addon registration details | 

### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteAddon

> DeleteAddon(ctx, id).Execute()

Delete add-on



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Resource identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.AddonsAPI.DeleteAddon(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AddonsAPI.DeleteAddon``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Resource identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAddonRequest struct via the builder pattern


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


## GetAddon

> AddonResponse GetAddon(ctx, id).Execute()

Get add-on



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Resource identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AddonsAPI.GetAddon(context.Background(), id).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AddonsAPI.GetAddon``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAddon`: AddonResponse
	fmt.Fprintf(os.Stdout, "Response from `AddonsAPI.GetAddon`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Resource identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAddonRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**AddonResponse**](AddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## InvokeAddon

> InvokeAddonResponse InvokeAddon(ctx, id).InvokeAddonRequest(invokeAddonRequest).Execute()

Invoke add-on



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
	id := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Resource identifier
	invokeAddonRequest := *openapiclient.NewInvokeAddonRequest("ThreatModelId_example") // InvokeAddonRequest | Addon invocation parameters

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AddonsAPI.InvokeAddon(context.Background(), id).InvokeAddonRequest(invokeAddonRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AddonsAPI.InvokeAddon``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `InvokeAddon`: InvokeAddonResponse
	fmt.Fprintf(os.Stdout, "Response from `AddonsAPI.InvokeAddon`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**id** | **string** | Resource identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiInvokeAddonRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **invokeAddonRequest** | [**InvokeAddonRequest**](InvokeAddonRequest.md) | Addon invocation parameters | 

### Return type

[**InvokeAddonResponse**](InvokeAddonResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListAddons

> ListAddonsResponse ListAddons(ctx).Limit(limit).Offset(offset).ThreatModelId(threatModelId).Execute()

List add-ons



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter subscriptions by threat model ID (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AddonsAPI.ListAddons(context.Background()).Limit(limit).Offset(offset).ThreatModelId(threatModelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AddonsAPI.ListAddons``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAddons`: ListAddonsResponse
	fmt.Fprintf(os.Stdout, "Response from `AddonsAPI.ListAddons`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAddonsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **threatModelId** | **string** | Filter subscriptions by threat model ID | 

### Return type

[**ListAddonsResponse**](ListAddonsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

