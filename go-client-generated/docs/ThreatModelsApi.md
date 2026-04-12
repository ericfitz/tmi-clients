# \ThreatModelsAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**CreateThreatModel**](ThreatModelsAPI.md#CreateThreatModel) | **Post** /threat_models | Create a threat model
[**DeleteThreatModel**](ThreatModelsAPI.md#DeleteThreatModel) | **Delete** /threat_models/{threat_model_id} | Delete a threat model
[**GetThreatModel**](ThreatModelsAPI.md#GetThreatModel) | **Get** /threat_models/{threat_model_id} | Retrieve a threat model
[**ListThreatModels**](ThreatModelsAPI.md#ListThreatModels) | **Get** /threat_models | List threat models
[**PatchThreatModel**](ThreatModelsAPI.md#PatchThreatModel) | **Patch** /threat_models/{threat_model_id} | Partially update a threat model
[**RestoreThreatModel**](ThreatModelsAPI.md#RestoreThreatModel) | **Post** /threat_models/{threat_model_id}/restore | Restore a soft-deleted threat model
[**UpdateThreatModel**](ThreatModelsAPI.md#UpdateThreatModel) | **Put** /threat_models/{threat_model_id} | Update a threat model



## CreateThreatModel

> ThreatModel CreateThreatModel(ctx).ThreatModelInput(threatModelInput).Execute()

Create a threat model



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
	threatModelInput := *openapiclient.NewThreatModelInput("Name_example") // ThreatModelInput | Threat Model creation data

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.CreateThreatModel(context.Background()).ThreatModelInput(threatModelInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.CreateThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `CreateThreatModel`: ThreatModel
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.CreateThreatModel`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiCreateThreatModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **threatModelInput** | [**ThreatModelInput**](ThreatModelInput.md) | Threat Model creation data | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## DeleteThreatModel

> DeleteThreatModel(ctx, threatModelId).Execute()

Delete a threat model



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	r, err := apiClient.ThreatModelsAPI.DeleteThreatModel(context.Background(), threatModelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.DeleteThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteThreatModelRequest struct via the builder pattern


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


## GetThreatModel

> ThreatModel GetThreatModel(ctx, threatModelId).Execute()

Retrieve a threat model



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.GetThreatModel(context.Background(), threatModelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.GetThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetThreatModel`: ThreatModel
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.GetThreatModel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetThreatModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## ListThreatModels

> ListThreatModelsResponse ListThreatModels(ctx).Limit(limit).Offset(offset).Owner(owner).Name(name).Description(description).IssueUri(issueUri).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Status(status).StatusUpdatedAfter(statusUpdatedAfter).StatusUpdatedBefore(statusUpdatedBefore).IncludeDeleted(includeDeleted).SecurityReviewer(securityReviewer).Execute()

List threat models



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
	owner := "owner_example" // string | Filter by owner name or email (optional)
	name := "name_example" // string | Filter by name (case-insensitive substring match) (optional)
	description := "description_example" // string | Filter by threat model description (partial match) (optional)
	issueUri := "issueUri_example" // string | Filter by issue URI (partial match) (optional)
	createdAfter := time.Now() // time.Time | Filter results created after this timestamp (ISO 8601) (optional)
	createdBefore := time.Now() // time.Time | Filter results created before this timestamp (ISO 8601) (optional)
	modifiedAfter := time.Now() // time.Time | Filter results modified after this timestamp (ISO 8601) (optional)
	modifiedBefore := time.Now() // time.Time | Filter results modified before this timestamp (ISO 8601) (optional)
	status := []string{"Inner_example"} // []string | Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status=identified&status=mitigated (optional)
	statusUpdatedAfter := time.Now() // time.Time | Filter threat models where status was updated after this timestamp (RFC3339) (optional)
	statusUpdatedBefore := time.Now() // time.Time | Filter threat models where status was updated before this timestamp (RFC3339) (optional)
	includeDeleted := true // bool | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. (optional) (default to false)
	securityReviewer := "securityReviewer_example" // string | Filter by security reviewer. Plain value performs case-insensitive partial match on reviewer email or display name. Use 'is:null' to find unassigned threat models (no security reviewer), 'is:notnull' to find assigned ones. (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.ListThreatModels(context.Background()).Limit(limit).Offset(offset).Owner(owner).Name(name).Description(description).IssueUri(issueUri).CreatedAfter(createdAfter).CreatedBefore(createdBefore).ModifiedAfter(modifiedAfter).ModifiedBefore(modifiedBefore).Status(status).StatusUpdatedAfter(statusUpdatedAfter).StatusUpdatedBefore(statusUpdatedBefore).IncludeDeleted(includeDeleted).SecurityReviewer(securityReviewer).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.ListThreatModels``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `ListThreatModels`: ListThreatModelsResponse
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.ListThreatModels`: %v\n", resp)
}
```

### Path Parameters



### Other Parameters

Other parameters are passed through a pointer to a apiListThreatModelsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **owner** | **string** | Filter by owner name or email | 
 **name** | **string** | Filter by name (case-insensitive substring match) | 
 **description** | **string** | Filter by threat model description (partial match) | 
 **issueUri** | **string** | Filter by issue URI (partial match) | 
 **createdAfter** | **time.Time** | Filter results created after this timestamp (ISO 8601) | 
 **createdBefore** | **time.Time** | Filter results created before this timestamp (ISO 8601) | 
 **modifiedAfter** | **time.Time** | Filter results modified after this timestamp (ISO 8601) | 
 **modifiedBefore** | **time.Time** | Filter results modified before this timestamp (ISO 8601) | 
 **status** | **[]string** | Filter by status (OR logic). Returns threats matching ANY of the specified statuses. Example: ?status&#x3D;identified&amp;status&#x3D;mitigated | 
 **statusUpdatedAfter** | **time.Time** | Filter threat models where status was updated after this timestamp (RFC3339) | 
 **statusUpdatedBefore** | **time.Time** | Filter threat models where status was updated before this timestamp (RFC3339) | 
 **includeDeleted** | **bool** | Include soft-deleted (tombstoned) entities in the response. Requires owner or admin role. | [default to false]
 **securityReviewer** | **string** | Filter by security reviewer. Plain value performs case-insensitive partial match on reviewer email or display name. Use &#39;is:null&#39; to find unassigned threat models (no security reviewer), &#39;is:notnull&#39; to find assigned ones. | 

### Return type

[**ListThreatModelsResponse**](ListThreatModelsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## PatchThreatModel

> ThreatModel PatchThreatModel(ctx, threatModelId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()

Partially update a threat model



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
	jsonPatchDocumentInner := []openapiclient.JsonPatchDocumentInner{*openapiclient.NewJsonPatchDocumentInner("Op_example", "Path_example")} // []JsonPatchDocumentInner | JSON Patch operations to apply to the threat model (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.PatchThreatModel(context.Background(), threatModelId).JsonPatchDocumentInner(jsonPatchDocumentInner).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.PatchThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `PatchThreatModel`: ThreatModel
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.PatchThreatModel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiPatchThreatModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **jsonPatchDocumentInner** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch operations to apply to the threat model | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json-patch+json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RestoreThreatModel

> ThreatModel RestoreThreatModel(ctx, threatModelId).Execute()

Restore a soft-deleted threat model



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

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.RestoreThreatModel(context.Background(), threatModelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.RestoreThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RestoreThreatModel`: ThreatModel
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.RestoreThreatModel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiRestoreThreatModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## UpdateThreatModel

> ThreatModel UpdateThreatModel(ctx, threatModelId).ThreatModelInput(threatModelInput).Execute()

Update a threat model



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
	threatModelInput := *openapiclient.NewThreatModelInput("Name_example") // ThreatModelInput | Complete threat model data for replacement

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.ThreatModelsAPI.UpdateThreatModel(context.Background(), threatModelId).ThreatModelInput(threatModelInput).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `ThreatModelsAPI.UpdateThreatModel``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `UpdateThreatModel`: ThreatModel
	fmt.Fprintf(os.Stdout, "Response from `ThreatModelsAPI.UpdateThreatModel`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiUpdateThreatModelRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **threatModelInput** | [**ThreatModelInput**](ThreatModelInput.md) | Complete threat model data for replacement | 

### Return type

[**ThreatModel**](ThreatModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

