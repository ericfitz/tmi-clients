# \AuditTrailAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetAssetAuditTrail**](AuditTrailAPI.md#GetAssetAuditTrail) | **Get** /threat_models/{threat_model_id}/assets/{asset_id}/audit_trail | List audit trail for an asset
[**GetAuditEntry**](AuditTrailAPI.md#GetAuditEntry) | **Get** /threat_models/{threat_model_id}/audit_trail/{entry_id} | Get a single audit trail entry
[**GetDiagramAuditTrail**](AuditTrailAPI.md#GetDiagramAuditTrail) | **Get** /threat_models/{threat_model_id}/diagrams/{diagram_id}/audit_trail | List audit trail for a diagram
[**GetDocumentAuditTrail**](AuditTrailAPI.md#GetDocumentAuditTrail) | **Get** /threat_models/{threat_model_id}/documents/{document_id}/audit_trail | List audit trail for a document
[**GetNoteAuditTrail**](AuditTrailAPI.md#GetNoteAuditTrail) | **Get** /threat_models/{threat_model_id}/notes/{note_id}/audit_trail | List audit trail for a note
[**GetRepositoryAuditTrail**](AuditTrailAPI.md#GetRepositoryAuditTrail) | **Get** /threat_models/{threat_model_id}/repositories/{repository_id}/audit_trail | List audit trail for a repository
[**GetThreatAuditTrail**](AuditTrailAPI.md#GetThreatAuditTrail) | **Get** /threat_models/{threat_model_id}/threats/{threat_id}/audit_trail | List audit trail for a threat
[**GetThreatModelAuditTrail**](AuditTrailAPI.md#GetThreatModelAuditTrail) | **Get** /threat_models/{threat_model_id}/audit_trail | List audit trail for a threat model and all sub-objects
[**RollbackToVersion**](AuditTrailAPI.md#RollbackToVersion) | **Post** /threat_models/{threat_model_id}/audit_trail/{entry_id}/rollback | Rollback an entity to a previous version



## GetAssetAuditTrail

> ListAuditTrailResponse GetAssetAuditTrail(ctx, threatModelId, assetId).Limit(limit).Offset(offset).Execute()

List audit trail for an asset



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetAssetAuditTrail(context.Background(), threatModelId, assetId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetAssetAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAssetAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetAssetAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**assetId** | **string** | Asset identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAssetAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetAuditEntry

> AuditEntry GetAuditEntry(ctx, threatModelId, entryId).Execute()

Get a single audit trail entry



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
	entryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the audit entry

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetAuditEntry(context.Background(), threatModelId, entryId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetAuditEntry``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetAuditEntry`: AuditEntry
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetAuditEntry`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**entryId** | **string** | Unique identifier of the audit entry | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetAuditEntryRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**AuditEntry**](AuditEntry.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDiagramAuditTrail

> ListAuditTrailResponse GetDiagramAuditTrail(ctx, threatModelId, diagramId).Limit(limit).Offset(offset).Execute()

List audit trail for a diagram



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
	diagramId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Diagram identifier
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetDiagramAuditTrail(context.Background(), threatModelId, diagramId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetDiagramAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDiagramAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetDiagramAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**diagramId** | **string** | Diagram identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDiagramAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetDocumentAuditTrail

> ListAuditTrailResponse GetDocumentAuditTrail(ctx, threatModelId, documentId).Limit(limit).Offset(offset).Execute()

List audit trail for a document



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetDocumentAuditTrail(context.Background(), threatModelId, documentId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetDocumentAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetDocumentAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetDocumentAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**documentId** | **string** | Document identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetDocumentAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetNoteAuditTrail

> ListAuditTrailResponse GetNoteAuditTrail(ctx, threatModelId, noteId).Limit(limit).Offset(offset).Execute()

List audit trail for a note



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetNoteAuditTrail(context.Background(), threatModelId, noteId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetNoteAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetNoteAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetNoteAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**noteId** | **string** | Note identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetNoteAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetRepositoryAuditTrail

> ListAuditTrailResponse GetRepositoryAuditTrail(ctx, threatModelId, repositoryId).Limit(limit).Offset(offset).Execute()

List audit trail for a repository



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
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetRepositoryAuditTrail(context.Background(), threatModelId, repositoryId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetRepositoryAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetRepositoryAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetRepositoryAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**repositoryId** | **string** | Repository identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetRepositoryAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetThreatAuditTrail

> ListAuditTrailResponse GetThreatAuditTrail(ctx, threatModelId, threatId).Limit(limit).Offset(offset).Execute()

List audit trail for a threat



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
	threatId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat identifier
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetThreatAuditTrail(context.Background(), threatModelId, threatId).Limit(limit).Offset(offset).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetThreatAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetThreatAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetThreatAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**threatId** | **string** | Threat identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetThreatAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetThreatModelAuditTrail

> ListAuditTrailResponse GetThreatModelAuditTrail(ctx, threatModelId).Limit(limit).Offset(offset).ObjectType(objectType).ChangeType(changeType).ActorEmail(actorEmail).After(after).Before(before).Execute()

List audit trail for a threat model and all sub-objects



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
	threatModelId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Threat model identifier
	limit := int32(56) // int32 | Maximum number of results to return (optional) (default to 20)
	offset := int32(56) // int32 | Number of results to skip (optional) (default to 0)
	objectType := "objectType_example" // string | Filter by object type (optional)
	changeType := "changeType_example" // string | Filter by change type (optional)
	actorEmail := "actorEmail_example" // string | Filter by actor email (optional)
	after := time.Now() // time.Time | Filter entries after this timestamp (ISO 8601) (optional)
	before := time.Now() // time.Time | Filter entries before this timestamp (ISO 8601) (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.GetThreatModelAuditTrail(context.Background(), threatModelId).Limit(limit).Offset(offset).ObjectType(objectType).ChangeType(changeType).ActorEmail(actorEmail).After(after).Before(before).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.GetThreatModelAuditTrail``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetThreatModelAuditTrail`: ListAuditTrailResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.GetThreatModelAuditTrail`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetThreatModelAuditTrailRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **limit** | **int32** | Maximum number of results to return | [default to 20]
 **offset** | **int32** | Number of results to skip | [default to 0]
 **objectType** | **string** | Filter by object type | 
 **changeType** | **string** | Filter by change type | 
 **actorEmail** | **string** | Filter by actor email | 
 **after** | **time.Time** | Filter entries after this timestamp (ISO 8601) | 
 **before** | **time.Time** | Filter entries before this timestamp (ISO 8601) | 

### Return type

[**ListAuditTrailResponse**](ListAuditTrailResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## RollbackToVersion

> RollbackResponse RollbackToVersion(ctx, threatModelId, entryId).Execute()

Rollback an entity to a previous version



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
	entryId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Unique identifier of the audit entry

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuditTrailAPI.RollbackToVersion(context.Background(), threatModelId, entryId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuditTrailAPI.RollbackToVersion``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `RollbackToVersion`: RollbackResponse
	fmt.Fprintf(os.Stdout, "Response from `AuditTrailAPI.RollbackToVersion`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 
**entryId** | **string** | Unique identifier of the audit entry | 

### Other Parameters

Other parameters are passed through a pointer to a apiRollbackToVersionRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------



### Return type

[**RollbackResponse**](RollbackResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

