# \DocumentsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PatchThreatModelDocument**](DocumentsAPI.md#PatchThreatModelDocument) | **Patch** /threat_models/{threat_model_id}/documents/{document_id} | Partially update document
[**RequestDocumentAccess**](DocumentsAPI.md#RequestDocumentAccess) | **Post** /threat_models/{threat_model_id}/documents/{document_id}/request_access | Request document access



## PatchThreatModelDocument

> Document PatchThreatModelDocument(ctx, threatModelId, documentId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update document



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
	documentId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Document identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the document

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentsAPI.PatchThreatModelDocument(context.Background(), threatModelId, documentId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentsAPI.PatchThreatModelDocument``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchThreatModelDocument`: Document
	fmt.Fprintf(os.Stdout, "Response from `DocumentsAPI.PatchThreatModelDocument`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**documentId** | **string** | Document identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchThreatModelDocumentRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the document | 

### Return type

[**Document**](Document.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RequestDocumentAccess

> RequestDocumentAccess200Response RequestDocumentAccess(ctx, threatModelId, documentId).Execute()

Request document access



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
	documentId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Document identifier

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.DocumentsAPI.RequestDocumentAccess(context.Background(), threatModelId, documentId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `DocumentsAPI.RequestDocumentAccess``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RequestDocumentAccess`: RequestDocumentAccess200Response
	fmt.Fprintf(os.Stdout, "Response from `DocumentsAPI.RequestDocumentAccess`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**documentId** | **string** | Document identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiRequestDocumentAccessRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**RequestDocumentAccess200Response**](RequestDocumentAccess200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

