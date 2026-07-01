# EmbeddingIngestionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**IndexType** | **string** | Target index type | 
**Embeddings** | [**[]EmbeddingIngestionItem**](EmbeddingIngestionItem.md) | Batch of pre-computed embeddings | 

## Methods

### NewEmbeddingIngestionRequest

`func NewEmbeddingIngestionRequest(indexType string, embeddings []EmbeddingIngestionItem, ) *EmbeddingIngestionRequest`

NewEmbeddingIngestionRequest instantiates a new EmbeddingIngestionRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingIngestionRequestWithDefaults

`func NewEmbeddingIngestionRequestWithDefaults() *EmbeddingIngestionRequest`

NewEmbeddingIngestionRequestWithDefaults instantiates a new EmbeddingIngestionRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIndexType

`func (o *EmbeddingIngestionRequest) GetIndexType() string`

GetIndexType returns the IndexType field if non-nil, zero value otherwise.

### GetIndexTypeOk

`func (o *EmbeddingIngestionRequest) GetIndexTypeOk() (*string, bool)`

GetIndexTypeOk returns a tuple with the IndexType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndexType

`func (o *EmbeddingIngestionRequest) SetIndexType(v string)`

SetIndexType sets IndexType field to given value.


### GetEmbeddings

`func (o *EmbeddingIngestionRequest) GetEmbeddings() []EmbeddingIngestionItem`

GetEmbeddings returns the Embeddings field if non-nil, zero value otherwise.

### GetEmbeddingsOk

`func (o *EmbeddingIngestionRequest) GetEmbeddingsOk() (*[]EmbeddingIngestionItem, bool)`

GetEmbeddingsOk returns a tuple with the Embeddings field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddings

`func (o *EmbeddingIngestionRequest) SetEmbeddings(v []EmbeddingIngestionItem)`

SetEmbeddings sets Embeddings field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


