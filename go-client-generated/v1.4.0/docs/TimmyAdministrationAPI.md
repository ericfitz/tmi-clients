# \TimmyAdministrationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetTimmyStatus**](TimmyAdministrationAPI.md#GetTimmyStatus) | **Get** /admin/timmy/status | Get Timmy system status
[**GetTimmyUsage**](TimmyAdministrationAPI.md#GetTimmyUsage) | **Get** /admin/timmy/usage | Get Timmy usage statistics



## GetTimmyStatus

> TimmyStatusResponse GetTimmyStatus(ctx).Execute()

Get Timmy system status



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
	resp, r, err := apiClient.TimmyAdministrationAPI.GetTimmyStatus(context.Background()).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyAdministrationAPI.GetTimmyStatus``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTimmyStatus`: TimmyStatusResponse
	fmt.Fprintf(os.Stdout, "Response from `TimmyAdministrationAPI.GetTimmyStatus`: %v\n", resp)
}
```

### Path Parameters

This endpoint does not need any parameter.

### Other Parameters

Other parameters are passed through a pointer to a apiGetTimmyStatusRequest struct via the builder pattern


### Return type

[**TimmyStatusResponse**](TimmyStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTimmyUsage

> TimmyUsageResponse GetTimmyUsage(ctx).UserId(userId).ThreatModelId(threatModelId).StartDate(startDate).EndDate(endDate).Execute()

Get Timmy usage statistics



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
	userId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter usage by user identifier (optional)
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter usage by threat model identifier (optional)
	startDate := time.Now() // time.Time | Filter usage records starting from this date (RFC3339) (optional)
	endDate := time.Now() // time.Time | Filter usage records up to this date (RFC3339) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.TimmyAdministrationAPI.GetTimmyUsage(context.Background()).UserId(userId).ThreatModelId(threatModelId).StartDate(startDate).EndDate(endDate).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `TimmyAdministrationAPI.GetTimmyUsage``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTimmyUsage`: TimmyUsageResponse
	fmt.Fprintf(os.Stdout, "Response from `TimmyAdministrationAPI.GetTimmyUsage`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiGetTimmyUsageRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **string** | Filter usage by user identifier | 
 **threatModelId** | **string** | Filter usage by threat model identifier | 
 **startDate** | **time.Time** | Filter usage records starting from this date (RFC3339) | 
 **endDate** | **time.Time** | Filter usage records up to this date (RFC3339) | 

### Return type

[**TimmyUsageResponse**](TimmyUsageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

