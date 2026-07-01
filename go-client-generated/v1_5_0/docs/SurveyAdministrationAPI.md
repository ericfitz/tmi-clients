# \SurveyAdministrationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**BulkCreateAdminSurveyMetadata**](SurveyAdministrationAPI.md#BulkCreateAdminSurveyMetadata) | **Post** /admin/surveys/{survey_id}/metadata/bulk | Bulk create metadata for a survey
[**BulkReplaceAdminSurveyMetadata**](SurveyAdministrationAPI.md#BulkReplaceAdminSurveyMetadata) | **Put** /admin/surveys/{survey_id}/metadata/bulk | Bulk replace metadata for a survey
[**BulkUpsertAdminSurveyMetadata**](SurveyAdministrationAPI.md#BulkUpsertAdminSurveyMetadata) | **Patch** /admin/surveys/{survey_id}/metadata/bulk | Bulk upsert metadata for a survey
[**CreateAdminSurvey**](SurveyAdministrationAPI.md#CreateAdminSurvey) | **Post** /admin/surveys | Create a survey
[**CreateAdminSurveyMetadata**](SurveyAdministrationAPI.md#CreateAdminSurveyMetadata) | **Post** /admin/surveys/{survey_id}/metadata | Add metadata to a survey
[**DeleteAdminSurvey**](SurveyAdministrationAPI.md#DeleteAdminSurvey) | **Delete** /admin/surveys/{survey_id} | Delete a survey
[**DeleteAdminSurveyMetadataByKey**](SurveyAdministrationAPI.md#DeleteAdminSurveyMetadataByKey) | **Delete** /admin/surveys/{survey_id}/metadata/{key} | Delete metadata by key for a survey
[**GetAdminSurvey**](SurveyAdministrationAPI.md#GetAdminSurvey) | **Get** /admin/surveys/{survey_id} | Get a survey
[**GetAdminSurveyMetadata**](SurveyAdministrationAPI.md#GetAdminSurveyMetadata) | **Get** /admin/surveys/{survey_id}/metadata | Get all metadata for a survey
[**GetAdminSurveyMetadataByKey**](SurveyAdministrationAPI.md#GetAdminSurveyMetadataByKey) | **Get** /admin/surveys/{survey_id}/metadata/{key} | Get metadata by key for a survey
[**ListAdminSurveys**](SurveyAdministrationAPI.md#ListAdminSurveys) | **Get** /admin/surveys | List surveys
[**PatchAdminSurvey**](SurveyAdministrationAPI.md#PatchAdminSurvey) | **Patch** /admin/surveys/{survey_id} | Partially update a survey
[**UpdateAdminSurvey**](SurveyAdministrationAPI.md#UpdateAdminSurvey) | **Put** /admin/surveys/{survey_id} | Update a survey
[**UpdateAdminSurveyMetadataByKey**](SurveyAdministrationAPI.md#UpdateAdminSurveyMetadataByKey) | **Put** /admin/surveys/{survey_id}/metadata/{key} | Update metadata by key for a survey



## BulkCreateAdminSurveyMetadata

> []Metadata BulkCreateAdminSurveyMetadata(ctx, surveyId).Metadata(metadata).Execute()

Bulk create metadata for a survey



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Array of metadata key-value pairs to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.BulkCreateAdminSurveyMetadata(context.Background(), surveyId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.BulkCreateAdminSurveyMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkCreateAdminSurveyMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.BulkCreateAdminSurveyMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkCreateAdminSurveyMetadataRequest struct via the builder pattern


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


## BulkReplaceAdminSurveyMetadata

> []Metadata BulkReplaceAdminSurveyMetadata(ctx, surveyId).Metadata(metadata).Execute()

Bulk replace metadata for a survey



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Complete set of metadata key-value pairs to replace existing metadata

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.BulkReplaceAdminSurveyMetadata(context.Background(), surveyId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.BulkReplaceAdminSurveyMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkReplaceAdminSurveyMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.BulkReplaceAdminSurveyMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkReplaceAdminSurveyMetadataRequest struct via the builder pattern


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


## BulkUpsertAdminSurveyMetadata

> []Metadata BulkUpsertAdminSurveyMetadata(ctx, surveyId).Metadata(metadata).Execute()

Bulk upsert metadata for a survey



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
	metadata := []openapiclient.Metadata{*openapiclient.NewMetadata("Key_example", "Value_example")} // []Metadata | Metadata key-value pairs to create or update (merge)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.BulkUpsertAdminSurveyMetadata(context.Background(), surveyId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.BulkUpsertAdminSurveyMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `BulkUpsertAdminSurveyMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.BulkUpsertAdminSurveyMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiBulkUpsertAdminSurveyMetadataRequest struct via the builder pattern


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


## CreateAdminSurvey

> Survey CreateAdminSurvey(ctx).SurveyInput(surveyInput).Execute()

Create a survey



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
	surveyInput := *openapiclient.NewSurveyInput("Name_example", "Version_example", map[string]interface{}{"key": interface{}(123)}) // SurveyInput | Survey definition to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.CreateAdminSurvey(context.Background()).SurveyInput(surveyInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.CreateAdminSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAdminSurvey`: Survey
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.CreateAdminSurvey`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateAdminSurveyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyInput** | [**SurveyInput**](SurveyInput.md) | Survey definition to create | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## CreateAdminSurveyMetadata

> Metadata CreateAdminSurveyMetadata(ctx, surveyId).Metadata(metadata).Execute()

Add metadata to a survey



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
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata key-value pair to create

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.CreateAdminSurveyMetadata(context.Background(), surveyId).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.CreateAdminSurveyMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateAdminSurveyMetadata`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.CreateAdminSurveyMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiCreateAdminSurveyMetadataRequest struct via the builder pattern


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


## DeleteAdminSurvey

> DeleteAdminSurvey(ctx, surveyId).Execute()

Delete a survey



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
	r, err := apiClient.SurveyAdministrationAPI.DeleteAdminSurvey(context.Background(), surveyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.DeleteAdminSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAdminSurveyRequest struct via the builder pattern


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


## DeleteAdminSurveyMetadataByKey

> DeleteAdminSurveyMetadataByKey(ctx, surveyId, key).Execute()

Delete metadata by key for a survey



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
	key := "key_example" // string | Metadata key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.SurveyAdministrationAPI.DeleteAdminSurveyMetadataByKey(context.Background(), surveyId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.DeleteAdminSurveyMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteAdminSurveyMetadataByKeyRequest struct via the builder pattern


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


## GetAdminSurvey

> Survey GetAdminSurvey(ctx, surveyId).Execute()

Get a survey



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
	resp, r, err := apiClient.SurveyAdministrationAPI.GetAdminSurvey(context.Background(), surveyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.GetAdminSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAdminSurvey`: Survey
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.GetAdminSurvey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAdminSurveyRequest struct via the builder pattern


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


## GetAdminSurveyMetadata

> []Metadata GetAdminSurveyMetadata(ctx, surveyId).Execute()

Get all metadata for a survey



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
	resp, r, err := apiClient.SurveyAdministrationAPI.GetAdminSurveyMetadata(context.Background(), surveyId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.GetAdminSurveyMetadata``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAdminSurveyMetadata`: []Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.GetAdminSurveyMetadata`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAdminSurveyMetadataRequest struct via the builder pattern


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


## GetAdminSurveyMetadataByKey

> Metadata GetAdminSurveyMetadataByKey(ctx, surveyId, key).Execute()

Get metadata by key for a survey



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
	key := "key_example" // string | Metadata key

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.GetAdminSurveyMetadataByKey(context.Background(), surveyId, key).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.GetAdminSurveyMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAdminSurveyMetadataByKey`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.GetAdminSurveyMetadataByKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAdminSurveyMetadataByKeyRequest struct via the builder pattern


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


## ListAdminSurveys

> ListSurveysResponse ListAdminSurveys(ctx).Status(status).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()

List surveys



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
	status := "status_example" // string | Filter by survey status (optional)
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	sort := "sort_example" // string | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) (optional) (default to "created_at:desc")
	createdAfter := time.Now() // time.Time | Filter results created after this timestamp (ISO 8601) (optional)
	createdBefore := time.Now() // time.Time | Filter results created before this timestamp (ISO 8601) (optional)
	modifiedAfter := time.Now() // time.Time | Filter results modified after this timestamp (ISO 8601) (optional)
	modifiedBefore := time.Now() // time.Time | Filter results modified before this timestamp (ISO 8601) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.ListAdminSurveys(context.Background()).Status(status).Limit(limit).Offset(offset).Sort(sort).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.ListAdminSurveys``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListAdminSurveys`: ListSurveysResponse
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.ListAdminSurveys`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListAdminSurveysRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **string** | Filter by survey status | 
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **sort** | **string** | Sort order (e.g., created_at:desc, name:asc, severity:desc, score:desc) | [default to &quot;created_at:desc&quot;]
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


## PatchAdminSurvey

> Survey PatchAdminSurvey(ctx, surveyId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update a survey



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
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the survey

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.PatchAdminSurvey(context.Background(), surveyId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.PatchAdminSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchAdminSurvey`: Survey
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.PatchAdminSurvey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchAdminSurveyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the survey | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAdminSurvey

> Survey UpdateAdminSurvey(ctx, surveyId).SurveyInput(surveyInput).Execute()

Update a survey



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
	surveyInput := *openapiclient.NewSurveyInput("Name_example", "Version_example", map[string]interface{}{"key": interface{}(123)}) // SurveyInput | Complete survey definition to replace existing

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.UpdateAdminSurvey(context.Background(), surveyId).SurveyInput(surveyInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.UpdateAdminSurvey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAdminSurvey`: Survey
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.UpdateAdminSurvey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAdminSurveyRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **surveyInput** | [**SurveyInput**](SurveyInput.md) | Complete survey definition to replace existing | 

### Return type

[**Survey**](Survey.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateAdminSurveyMetadataByKey

> Metadata UpdateAdminSurveyMetadataByKey(ctx, surveyId, key).Metadata(metadata).Execute()

Update metadata by key for a survey



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
	key := "key_example" // string | Metadata key
	metadata := *openapiclient.NewMetadata("Key_example", "Value_example") // Metadata | Metadata key-value pair to update

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.SurveyAdministrationAPI.UpdateAdminSurveyMetadataByKey(context.Background(), surveyId, key).Metadata(metadata).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `SurveyAdministrationAPI.UpdateAdminSurveyMetadataByKey``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateAdminSurveyMetadataByKey`: Metadata
	fmt.Fprintf(os.Stdout, "Response from `SurveyAdministrationAPI.UpdateAdminSurveyMetadataByKey`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**surveyId** | **string** | Unique identifier of the survey | 
**key** | **string** | Metadata key | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateAdminSurveyMetadataByKeyRequest struct via the builder pattern


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

