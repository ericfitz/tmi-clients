# \SurveyIntakeAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateIntakeSurveyResponseMetadata**](SurveyIntakeAPI.md#BulkCreateIntakeSurveyResponseMetadata) | **Post** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk create metadata for a survey response
[**BulkReplaceIntakeSurveyResponseMetadata**](SurveyIntakeAPI.md#BulkReplaceIntakeSurveyResponseMetadata) | **Put** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk replace metadata for a survey response
[**BulkUpsertIntakeSurveyResponseMetadata**](SurveyIntakeAPI.md#BulkUpsertIntakeSurveyResponseMetadata) | **Patch** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk upsert metadata for a survey response
[**CreateIntakeSurveyResponse**](SurveyIntakeAPI.md#CreateIntakeSurveyResponse) | **Post** /intake/survey_responses | Create survey response
[**CreateIntakeSurveyResponseMetadata**](SurveyIntakeAPI.md#CreateIntakeSurveyResponseMetadata) | **Post** /intake/survey_responses/{survey_response_id}/metadata | Add metadata to a survey response
[**DeleteIntakeSurveyResponse**](SurveyIntakeAPI.md#DeleteIntakeSurveyResponse) | **Delete** /intake/survey_responses/{survey_response_id} | Delete survey response
[**DeleteIntakeSurveyResponseMetadataByKey**](SurveyIntakeAPI.md#DeleteIntakeSurveyResponseMetadataByKey) | **Delete** /intake/survey_responses/{survey_response_id}/metadata/{key} | Delete metadata by key for a survey response
[**GetIntakeSurvey**](SurveyIntakeAPI.md#GetIntakeSurvey) | **Get** /intake/surveys/{survey_id} | Get an available survey
[**GetIntakeSurveyResponse**](SurveyIntakeAPI.md#GetIntakeSurveyResponse) | **Get** /intake/survey_responses/{survey_response_id} | Get survey response
[**GetIntakeSurveyResponseMetadata**](SurveyIntakeAPI.md#GetIntakeSurveyResponseMetadata) | **Get** /intake/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
[**GetIntakeSurveyResponseMetadataByKey**](SurveyIntakeAPI.md#GetIntakeSurveyResponseMetadataByKey) | **Get** /intake/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
[**GetIntakeSurveyResponseTriageNote**](SurveyIntakeAPI.md#GetIntakeSurveyResponseTriageNote) | **Get** /intake/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
[**ListIntakeSurveyResponseTriageNotes**](SurveyIntakeAPI.md#ListIntakeSurveyResponseTriageNotes) | **Get** /intake/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
[**ListIntakeSurveyResponses**](SurveyIntakeAPI.md#ListIntakeSurveyResponses) | **Get** /intake/survey_responses | List user&#39;s survey responses
[**ListIntakeSurveys**](SurveyIntakeAPI.md#ListIntakeSurveys) | **Get** /intake/surveys | List available surveys
[**PatchIntakeSurveyResponse**](SurveyIntakeAPI.md#PatchIntakeSurveyResponse) | **Patch** /intake/survey_responses/{survey_response_id} | Partial update survey response
[**UpdateIntakeSurveyResponse**](SurveyIntakeAPI.md#UpdateIntakeSurveyResponse) | **Put** /intake/survey_responses/{survey_response_id} | Update survey response
[**UpdateIntakeSurveyResponseMetadataByKey**](SurveyIntakeAPI.md#UpdateIntakeSurveyResponseMetadataByKey) | **Put** /intake/survey_responses/{survey_response_id}/metadata/{key} | Update metadata by key for a survey response



## BulkCreateIntakeSurveyResponseMetadata

> []Metadata BulkCreateIntakeSurveyResponseMetadata(ctx, surveyResponseId).Metadata(metadata).Execute()

Bulk create metadata for a survey response



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Array of metadata key-value pairs to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.BulkCreateIntakeSurveyResponseMetadata(context.Background(), surveyResponseId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.BulkCreateIntakeSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkCreateIntakeSurveyResponseMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.BulkCreateIntakeSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkCreateIntakeSurveyResponseMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**[]Metadata**](Metadata.md) | Array of metadata key-value pairs to create | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkReplaceIntakeSurveyResponseMetadata

> []Metadata BulkReplaceIntakeSurveyResponseMetadata(ctx, surveyResponseId).Metadata(metadata).Execute()

Bulk replace metadata for a survey response



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Complete set of metadata key-value pairs to replace existing metadata

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.BulkReplaceIntakeSurveyResponseMetadata(context.Background(), surveyResponseId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.BulkReplaceIntakeSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkReplaceIntakeSurveyResponseMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.BulkReplaceIntakeSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkReplaceIntakeSurveyResponseMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**[]Metadata**](Metadata.md) | Complete set of metadata key-value pairs to replace existing metadata | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## BulkUpsertIntakeSurveyResponseMetadata

> []Metadata BulkUpsertIntakeSurveyResponseMetadata(ctx, surveyResponseId).Metadata(metadata).Execute()

Bulk upsert metadata for a survey response



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Metadata key-value pairs to create or update (merge)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.BulkUpsertIntakeSurveyResponseMetadata(context.Background(), surveyResponseId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.BulkUpsertIntakeSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkUpsertIntakeSurveyResponseMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.BulkUpsertIntakeSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkUpsertIntakeSurveyResponseMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**[]Metadata**](Metadata.md) | Metadata key-value pairs to create or update (merge) | 

### Return type

[**[]Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateIntakeSurveyResponse

> SurveyResponse CreateIntakeSurveyResponse(ctx).SurveyResponseCreateRequest(surveyResponseCreateRequest).Execute()

Create survey response



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
	surveyResponseCreateRequest := *openapiclient.NewSurveyResponseCreateRequest("SurveyId_example") // SurveyResponseCreateRequest | Survey response to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.CreateIntakeSurveyResponse(context.Background()).SurveyResponseCreateRequest(surveyResponseCreateRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.CreateIntakeSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateIntakeSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.CreateIntakeSurveyResponse`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateIntakeSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyResponseCreateRequest** | [**SurveyResponseCreateRequest**](SurveyResponseCreateRequest.md) | Survey response to create | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateIntakeSurveyResponseMetadata

> Metadata CreateIntakeSurveyResponseMetadata(ctx, surveyResponseId).Metadata(metadata).Execute()

Add metadata to a survey response



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
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata key-value pair to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.CreateIntakeSurveyResponseMetadata(context.Background(), surveyResponseId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.CreateIntakeSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateIntakeSurveyResponseMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.CreateIntakeSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateIntakeSurveyResponseMetadataRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **metadata** | [**Metadata**](Metadata.md) | Metadata key-value pair to create | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteIntakeSurveyResponse

> DeleteIntakeSurveyResponse(ctx, surveyResponseId).Execute()

Delete survey response



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
	r, err := apiClient.SurveyIntakeAPI.DeleteIntakeSurveyResponse(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.DeleteIntakeSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteIntakeSurveyResponseRequest struct via the builder pattern


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


## DeleteIntakeSurveyResponseMetadataByKey

> DeleteIntakeSurveyResponseMetadataByKey(ctx, surveyResponseId, key).Execute()

Delete metadata by key for a survey response



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
	r, err := apiClient.SurveyIntakeAPI.DeleteIntakeSurveyResponseMetadataByKey(context.Background(), surveyResponseId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.DeleteIntakeSurveyResponseMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteIntakeSurveyResponseMetadataByKeyRequest struct via the builder pattern


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


## GetIntakeSurvey

> Survey GetIntakeSurvey(ctx, surveyId).Execute()

Get an available survey



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
	surveyId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the survey

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.GetIntakeSurvey(context.Background(), surveyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.GetIntakeSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIntakeSurvey`: Survey
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.GetIntakeSurvey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetIntakeSurveyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetIntakeSurveyResponse

> SurveyResponse GetIntakeSurveyResponse(ctx, surveyResponseId).Execute()

Get survey response



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
	resp, r, err := apiClient.SurveyIntakeAPI.GetIntakeSurveyResponse(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.GetIntakeSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIntakeSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.GetIntakeSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetIntakeSurveyResponseRequest struct via the builder pattern


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


## GetIntakeSurveyResponseMetadata

> []Metadata GetIntakeSurveyResponseMetadata(ctx, surveyResponseId).Execute()

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
	resp, r, err := apiClient.SurveyIntakeAPI.GetIntakeSurveyResponseMetadata(context.Background(), surveyResponseId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.GetIntakeSurveyResponseMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIntakeSurveyResponseMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.GetIntakeSurveyResponseMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetIntakeSurveyResponseMetadataRequest struct via the builder pattern


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


## GetIntakeSurveyResponseMetadataByKey

> Metadata GetIntakeSurveyResponseMetadataByKey(ctx, surveyResponseId, key).Execute()

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
	resp, r, err := apiClient.SurveyIntakeAPI.GetIntakeSurveyResponseMetadataByKey(context.Background(), surveyResponseId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.GetIntakeSurveyResponseMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIntakeSurveyResponseMetadataByKey`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.GetIntakeSurveyResponseMetadataByKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetIntakeSurveyResponseMetadataByKeyRequest struct via the builder pattern


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


## GetIntakeSurveyResponseTriageNote

> TriageNote GetIntakeSurveyResponseTriageNote(ctx, surveyResponseId, triageNoteId).Execute()

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
	resp, r, err := apiClient.SurveyIntakeAPI.GetIntakeSurveyResponseTriageNote(context.Background(), surveyResponseId, triageNoteId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.GetIntakeSurveyResponseTriageNote``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetIntakeSurveyResponseTriageNote`: TriageNote
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.GetIntakeSurveyResponseTriageNote`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**triageNoteId** | **int32** | Triage note identifier (sequential within survey response) | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetIntakeSurveyResponseTriageNoteRequest struct via the builder pattern


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


## ListIntakeSurveyResponseTriageNotes

> ListTriageNotesResponse ListIntakeSurveyResponseTriageNotes(ctx, surveyResponseId).Limit(limit).Offset(offset).Execute()

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
	resp, r, err := apiClient.SurveyIntakeAPI.ListIntakeSurveyResponseTriageNotes(context.Background(), surveyResponseId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.ListIntakeSurveyResponseTriageNotes``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListIntakeSurveyResponseTriageNotes`: ListTriageNotesResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.ListIntakeSurveyResponseTriageNotes`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiListIntakeSurveyResponseTriageNotesRequest struct via the builder pattern


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


## ListIntakeSurveyResponses

> ListSurveyResponsesResponse ListIntakeSurveyResponses(ctx).Status(status).SurveyId(surveyId).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()

List user's survey responses



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sort := "sort_example" // string | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to "created_at:desc")
	createdAfter := time.Now() // time.Time | Filter results created after this timestamp (ISO 8601) (optional)
	createdBefore := time.Now() // time.Time | Filter results created before this timestamp (ISO 8601) (optional)
	modifiedAfter := time.Now() // time.Time | Filter results modified after this timestamp (ISO 8601) (optional)
	modifiedBefore := time.Now() // time.Time | Filter results modified before this timestamp (ISO 8601) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.ListIntakeSurveyResponses(context.Background()).Status(status).SurveyId(surveyId).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.ListIntakeSurveyResponses``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListIntakeSurveyResponses`: ListSurveyResponsesResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.ListIntakeSurveyResponses`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListIntakeSurveyResponsesRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **string** | Filter by response status. Supports comma-separated values for multi-status filtering (e.g., status&#x3D;submitted,ready_for_review). | 
 **surveyId** | **string** | Filter by survey ID | 
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


## ListIntakeSurveys

> ListSurveysResponse ListIntakeSurveys(ctx).Limit(limit).Offset(offset).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()

List available surveys



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	createdAfter := time.Now() // time.Time | Filter results created after this timestamp (ISO 8601) (optional)
	createdBefore := time.Now() // time.Time | Filter results created before this timestamp (ISO 8601) (optional)
	modifiedAfter := time.Now() // time.Time | Filter results modified after this timestamp (ISO 8601) (optional)
	modifiedBefore := time.Now() // time.Time | Filter results modified before this timestamp (ISO 8601) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.ListIntakeSurveys(context.Background()).Limit(limit).Offset(offset).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.ListIntakeSurveys``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListIntakeSurveys`: ListSurveysResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.ListIntakeSurveys`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListIntakeSurveysRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **createdAfter** | **time.Time** | Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **time.Time** | Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **time.Time** | Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **time.Time** | Filter results modified before this timestamp (ISO 8601) | 

### Return type

[**ListSurveysResponse**](ListSurveysResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchIntakeSurveyResponse

> SurveyResponse PatchIntakeSurveyResponse(ctx, surveyResponseId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partial update survey response



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
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the survey response

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.PatchIntakeSurveyResponse(context.Background(), surveyResponseId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.PatchIntakeSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchIntakeSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.PatchIntakeSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchIntakeSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the survey response | 

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


## UpdateIntakeSurveyResponse

> SurveyResponse UpdateIntakeSurveyResponse(ctx, surveyResponseId).SurveyResponseInput(surveyResponseInput).Execute()

Update survey response



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
	surveyResponseInput := *openapiclient.NewSurveyResponseInput("SurveyId_example") // SurveyResponseInput | Complete survey response to replace existing

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.UpdateIntakeSurveyResponse(context.Background(), surveyResponseId).SurveyResponseInput(surveyResponseInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.UpdateIntakeSurveyResponse``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateIntakeSurveyResponse`: SurveyResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.UpdateIntakeSurveyResponse`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateIntakeSurveyResponseRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **surveyResponseInput** | [**SurveyResponseInput**](SurveyResponseInput.md) | Complete survey response to replace existing | 

### Return type

[**SurveyResponse**](SurveyResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateIntakeSurveyResponseMetadataByKey

> Metadata UpdateIntakeSurveyResponseMetadataByKey(ctx, surveyResponseId, key).Metadata(metadata).Execute()

Update metadata by key for a survey response



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
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata key-value pair to update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyIntakeAPI.UpdateIntakeSurveyResponseMetadataByKey(context.Background(), surveyResponseId, key).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyIntakeAPI.UpdateIntakeSurveyResponseMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateIntakeSurveyResponseMetadataByKey`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyIntakeAPI.UpdateIntakeSurveyResponseMetadataByKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyResponseId** | **string** | Unique identifier of the survey response | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateIntakeSurveyResponseMetadataByKeyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **metadata** | [**Metadata**](Metadata.md) | Metadata key-value pair to update | 

### Return type

[**Metadata**](Metadata.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

