# \RepositoriesAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PatchThreatModelRepository**](RepositoriesAPI.md#PatchThreatModelRepository) | **Patch** /threat_models/{threat_model_id}/repositories/{repository_id} | Partially update repository



## PatchThreatModelRepository

> Repository PatchThreatModelRepository(ctx, threatModelId, repositoryId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update repository



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
	repositoryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Repository identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the repository

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.RepositoriesAPI.PatchThreatModelRepository(context.Background(), threatModelId, repositoryId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `RepositoriesAPI.PatchThreatModelRepository``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchThreatModelRepository`: Repository
	fmt.Fprintf(os.Stdout, "Response from `RepositoriesAPI.PatchThreatModelRepository`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**repositoryId** | **string** | Repository identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchThreatModelRepositoryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the repository | 

### Return type

[**Repository**](Repository.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

