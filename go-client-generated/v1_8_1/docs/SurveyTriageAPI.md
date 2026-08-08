# \SurveyTriageAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateThreatModelFromSurveyResponse**](SurveyTriageAPI.md#CreateThreatModelFromSurveyResponse) | **Post** /triage/survey_responses/{survey_response_id}/create_threat_model | Create threat model from survey response
[**CreateTriageSurveyResponseTriageNote**](SurveyTriageAPI.md#CreateTriageSurveyResponseTriageNote) | **Post** /triage/survey_responses/{survey_response_id}/triage_notes | Create a triage note
[**GetTriageSurveyResponse**](SurveyTriageAPI.md#GetTriageSurveyResponse) | **Get** /triage/survey_responses/{survey_response_id} | Get survey response for triage
[**GetTriageSurveyResponseMetadata**](SurveyTriageAPI.md#GetTriageSurveyResponseMetadata) | **Get** /triage/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**GetTriageSurveyResponseMetadataByKey**](SurveyTriageAPI.md#GetTriageSurveyResponseMetadataByKey) | **Get** /triage/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**GetTriageSurveyResponseTriageNote**](SurveyTriageAPI.md#GetTriageSurveyResponseTriageNote) | **Get** /triage/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**ListTriageSurveyResponseTriageNotes**](SurveyTriageAPI.md#ListTriageSurveyResponseTriageNotes) | **Get** /triage/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**ListTriageSurveyResponses**](SurveyTriageAPI.md#ListTriageSurveyResponses) | **Get** /triage/survey_responses | List survey responses for triage
[**PatchTriageSurveyResponse**](SurveyTriageAPI.md#PatchTriageSurveyResponse) | **Patch** /triage/survey_responses/{survey_response_id} | Partial update survey response for triage



## CreateThreatModelFromSurveyResponse

> CreateThreatModelFromSurveyResponse CreateThreatModelFromSurveyResponse(ctx, surveyResponseId).Execute()

Create threat model from survey response



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.CreateThreatModelFromSurveyResponse(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.CreateThreatModelFromSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateThreatModelFromSurveyResponse`: CreateThreatModelFromSurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.CreateThreatModelFromSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateThreatModelFromSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**CreateThreatModelFromSurveyResponse**](CreateThreatModelFromSurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateTriageSurveyResponseTriageNote

> TriageNote CreateTriageSurveyResponseTriageNote(ctx, surveyResponseId).TriageNoteInput(triageNoteInput).Execute()

Create a triage note



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response
	triageNoteInput := *openapiclient.NewTriageNoteInput("Name_example", "Content_example") // TriageNoteInput | Triage note creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.CreateTriageSurveyResponseTriageNote(context.Background(), surveyResponseId).TriageNoteInput(triageNoteInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.CreateTriageSurveyResponseTriageNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateTriageSurveyResponseTriageNote`: TriageNote
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.CreateTriageSurveyResponseTriageNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateTriageSurveyResponseTriageNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **triageNoteInput** | [**TriageNoteInput**](TriageNoteInput.md) | Triage note creation data | 

### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTriageSurveyResponse

> SurveyResponse GetTriageSurveyResponse(ctx, surveyResponseId).Execute()

Get survey response for triage



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.GetTriageSurveyResponse(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.GetTriageSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTriageSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.GetTriageSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTriageSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTriageSurveyResponseMetadata

> []Metadata GetTriageSurveyResponseMetadata(ctx, surveyResponseId).Execute()

Get all metadata for a survey response



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.GetTriageSurveyResponseMetadata(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.GetTriageSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTriageSurveyResponseMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.GetTriageSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTriageSurveyResponseMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTriageSurveyResponseMetadataByKey

> Metadata GetTriageSurveyResponseMetadataByKey(ctx, surveyResponseId, key).Execute()

Get metadata by key for a survey response



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response
	key := "key_example" // string | Metadata key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.GetTriageSurveyResponseMetadataByKey(context.Background(), surveyResponseId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.GetTriageSurveyResponseMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTriageSurveyResponseMetadataByKey`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.GetTriageSurveyResponseMetadataByKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTriageSurveyResponseMetadataByKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetTriageSurveyResponseTriageNote

> TriageNote GetTriageSurveyResponseTriageNote(ctx, surveyResponseId, triageNoteId).Execute()

Get a specific triage note



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response
	triageNoteId := int32(56) // int32 | Triage note identifier (sequential within survey response)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.GetTriageSurveyResponseTriageNote(context.Background(), surveyResponseId, triageNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.GetTriageSurveyResponseTriageNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetTriageSurveyResponseTriageNote`: TriageNote
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.GetTriageSurveyResponseTriageNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**triageNoteId** | **int32** | Triage note identifier (sequential within survey response) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetTriageSurveyResponseTriageNoteRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**TriageNote**](TriageNote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTriageSurveyResponseTriageNotes

> ListTriageNotesResponse ListTriageSurveyResponseTriageNotes(ctx, surveyResponseId).Limit(limit).Offset(offset).Execute()

List triage notes for a survey response



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.ListTriageSurveyResponseTriageNotes(context.Background(), surveyResponseId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.ListTriageSurveyResponseTriageNotes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTriageSurveyResponseTriageNotes`: ListTriageNotesResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.ListTriageSurveyResponseTriageNotes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiListTriageSurveyResponseTriageNotesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListTriageNotesResponse**](ListTriageNotesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListTriageSurveyResponses

> ListSurveyResponsesResponse ListTriageSurveyResponses(ctx).Status(status).SurveyId(surveyId).IsConfidential(isConfidential).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()

List survey responses for triage



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
	status := "status_example" // string | Filter by response status. Supports comma-separated values for multi-status filtering (e.g., status=submitted,ready_for_review). (optional)
	surveyId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter by survey ID (optional)
	isConfidential := true // bool | Filter by secret_project flag (optional)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sort := "sort_example" // string | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to "created_at:desc")
	createdAfter := time.Now() // time.Time | Filter results created after this timestamp (ISO 8601) (optional)
	createdBefore := time.Now() // time.Time | Filter results created before this timestamp (ISO 8601) (optional)
	modifiedAfter := time.Now() // time.Time | Filter results modified after this timestamp (ISO 8601) (optional)
	modifiedBefore := time.Now() // time.Time | Filter results modified before this timestamp (ISO 8601) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.ListTriageSurveyResponses(context.Background()).Status(status).SurveyId(surveyId).IsConfidential(isConfidential).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.ListTriageSurveyResponses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListTriageSurveyResponses`: ListSurveyResponsesResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.ListTriageSurveyResponses`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListTriageSurveyResponsesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **string** | Filter by response status. Supports comma-separated values for multi-status filtering (e.g., status&#x3D;submitted,ready_for_review). | 
 **surveyId** | **string** | Filter by survey ID | 
 **isConfidential** | **bool** | Filter by secret_project flag | 
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **sort** | **string** | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [default to &quot;created_at:desc&quot;]
 **createdAfter** | **time.Time** | Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **time.Time** | Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **time.Time** | Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **time.Time** | Filter results modified before this timestamp (ISO 8601) | 

### Return type

[**ListSurveyResponsesResponse**](ListSurveyResponsesResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchTriageSurveyResponse

> SurveyResponse PatchTriageSurveyResponse(ctx, surveyResponseId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partial update survey response for triage



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
	surveyResponseId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey response
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the survey response during triage

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyTriageAPI.PatchTriageSurveyResponse(context.Background(), surveyResponseId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyTriageAPI.PatchTriageSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchTriageSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyTriageAPI.PatchTriageSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchTriageSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the survey response during triage | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

