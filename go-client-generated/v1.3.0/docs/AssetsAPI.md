# \AssetsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PatchThreatModelAsset**](AssetsAPI.md#PatchThreatModelAsset) | **Patch** /threat_models/{threat_model_id}/assets/{asset_id} | Partially update asset



## PatchThreatModelAsset

> Asset PatchThreatModelAsset(ctx, threatModelId, assetId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update asset



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
	assetId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Asset identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the asset

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AssetsAPI.PatchThreatModelAsset(context.Background(), threatModelId, assetId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AssetsAPI.PatchThreatModelAsset``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchThreatModelAsset`: Asset
	fmt.Fprintf(os.Stdout, "Response from `AssetsAPI.PatchThreatModelAsset`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**assetId** | **string** | Asset identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchThreatModelAssetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the asset | 

### Return type

[**Asset**](Asset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

