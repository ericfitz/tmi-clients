# \EmbeddingAutomationAPI

All URIs are relative to *https://api.tmi.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**DeleteEmbeddings**](EmbeddingAutomationAPI.md#DeleteEmbeddings) | **Delete** /automation/embeddings/{threat_model_id} | Delete embeddings
[**GetEmbeddingConfig**](EmbeddingAutomationAPI.md#GetEmbeddingConfig) | **Get** /automation/embeddings/{threat_model_id}/config | Get embedding provider configuration
[**IngestEmbeddings**](EmbeddingAutomationAPI.md#IngestEmbeddings) | **Post** /automation/embeddings/{threat_model_id} | Ingest pre-computed embeddings



## DeleteEmbeddings

> EmbeddingDeleteResponse DeleteEmbeddings(ctx, threatModelId).EntityType(entityType).EntityId(entityId).IndexType(indexType).Execute()

Delete embeddings



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
	entityType := "entityType_example" // string | Filter by entity type (optional)
	entityId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | Filter by entity UUID (optional)
	indexType := "indexType_example" // string | Filter by index type (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmbeddingAutomationAPI.DeleteEmbeddings(context.Background(), threatModelId).EntityType(entityType).EntityId(entityId).IndexType(indexType).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmbeddingAutomationAPI.DeleteEmbeddings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `DeleteEmbeddings`: EmbeddingDeleteResponse
	fmt.Fprintf(os.Stdout, "Response from `EmbeddingAutomationAPI.DeleteEmbeddings`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiDeleteEmbeddingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **entityType** | **string** | Filter by entity type | 
 **entityId** | **string** | Filter by entity UUID | 
 **indexType** | **string** | Filter by index type | 

### Return type

[**EmbeddingDeleteResponse**](EmbeddingDeleteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## GetEmbeddingConfig

> EmbeddingConfig GetEmbeddingConfig(ctx, threatModelId).Execute()

Get embedding provider configuration



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
	resp, r, err := apiClient.EmbeddingAutomationAPI.GetEmbeddingConfig(context.Background(), threatModelId).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmbeddingAutomationAPI.GetEmbeddingConfig``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `GetEmbeddingConfig`: EmbeddingConfig
	fmt.Fprintf(os.Stdout, "Response from `EmbeddingAutomationAPI.GetEmbeddingConfig`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiGetEmbeddingConfigRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**EmbeddingConfig**](EmbeddingConfig.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## IngestEmbeddings

> EmbeddingIngestionResponse IngestEmbeddings(ctx, threatModelId).EmbeddingIngestionRequest(embeddingIngestionRequest).Execute()

Ingest pre-computed embeddings



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
	embeddingIngestionRequest := *openapiclient.NewEmbeddingIngestionRequest("IndexType_example", []openapiclient.EmbeddingIngestionItem{*openapiclient.NewEmbeddingIngestionItem("EntityType_example", "EntityId_example", int32(123), "ChunkText_example", "ContentHash_example", "EmbeddingModel_example", int32(123), []float32{float32(123)})}) // EmbeddingIngestionRequest | Batch of pre-computed embeddings to ingest

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.EmbeddingAutomationAPI.IngestEmbeddings(context.Background(), threatModelId).EmbeddingIngestionRequest(embeddingIngestionRequest).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `EmbeddingAutomationAPI.IngestEmbeddings``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `IngestEmbeddings`: EmbeddingIngestionResponse
	fmt.Fprintf(os.Stdout, "Response from `EmbeddingAutomationAPI.IngestEmbeddings`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**threatModelId** | **string** | Threat model identifier | 

### Other Parameters

Other parameters are passed through a pointer to a apiIngestEmbeddingsRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **embeddingIngestionRequest** | [**EmbeddingIngestionRequest**](EmbeddingIngestionRequest.md) | Batch of pre-computed embeddings to ingest | 

### Return type

[**EmbeddingIngestionResponse**](EmbeddingIngestionResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

