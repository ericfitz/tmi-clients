# \NotesAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**PatchThreatModelNote**](NotesAPI.md#PatchThreatModelNote) | **Patch** /threat_models/{threat_model_id}/notes/{note_id} | Partially update note



## PatchThreatModelNote

> Note PatchThreatModelNote(ctx, threatModelId, noteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update note



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
	noteId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Note identifier
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the note

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.NotesAPI.PatchThreatModelNote(context.Background(), threatModelId, noteId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `NotesAPI.PatchThreatModelNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchThreatModelNote`: Note
	fmt.Fprintf(os.Stdout, "Response from `NotesAPI.PatchThreatModelNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**noteId** | **string** | Note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchThreatModelNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the note | 

### Return type

[**Note**](Note.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

