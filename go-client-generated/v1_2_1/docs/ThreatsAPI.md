# \ThreatsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkDeleteThreatModelThreats**](ThreatsAPI.md#BulkDeleteThreatModelThreats) | **Delete** /threat_models/{threat_model_id}/threats/bulk | Bulk DELETE threats
[**BulkPatchThreatModelThreats**](ThreatsAPI.md#BulkPatchThreatModelThreats) | **Patch** /threat_models/{threat_model_id}/threats/bulk | Bulk PATCH threats



## BulkDeleteThreatModelThreats

> BulkDeleteThreatModelThreats200Response BulkDeleteThreatModelThreats(ctx, threatModelId).ThreatIds(threatIds).Execute()

Bulk DELETE threats



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	threatIds := []string{"Inner_example"} // []string | Comma-separated list of threat IDs to delete (UUID format)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatsAPI.BulkDeleteThreatModelThreats(context.Background(), threatModelId).ThreatIds(threatIds).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatsAPI.BulkDeleteThreatModelThreats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkDeleteThreatModelThreats`: BulkDeleteThreatModelThreats200Response
	fmt.Fprintf(os.Stdout, "Response from `ThreatsAPI.BulkDeleteThreatModelThreats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkDeleteThreatModelThreatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **threatIds** | **[]string** | Comma-separated list of threat IDs to delete (UUID format) | 

### Return type

[**BulkDeleteThreatModelThreats200Response**](BulkDeleteThreatModelThreats200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkPatchThreatModelThreats

> []Threat BulkPatchThreatModelThreats(ctx, threatModelId).BulkPatchRequest(bulkPatchRequest).Execute()

Bulk PATCH threats



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	bulkPatchRequest := *openapiclient.NewBulkPatchRequest([]openapiclient.BulkPatchRequestPatchesInner{*openapiclient.NewBulkPatchRequestPatchesInner("Id_example", []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")})}) // BulkPatchRequest | JSON Patch operations to apply to multiple threats

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatsAPI.BulkPatchThreatModelThreats(context.Background(), threatModelId).BulkPatchRequest(bulkPatchRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatsAPI.BulkPatchThreatModelThreats``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkPatchThreatModelThreats`: []Threat
	fmt.Fprintf(os.Stdout, "Response from `ThreatsAPI.BulkPatchThreatModelThreats`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkPatchThreatModelThreatsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **bulkPatchRequest** | [**BulkPatchRequest**](BulkPatchRequest.md) | JSON Patch operations to apply to multiple threats | 

### Return type

[**[]Threat**](Threat.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

