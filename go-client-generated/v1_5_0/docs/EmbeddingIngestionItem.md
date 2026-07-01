# EmbeddingIngestionItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EntityType** | **string** | Entity type (e.g., repository, asset) | 
**EntityId** | **string** | Entity UUID | 
**ChunkIndex** | **int32** | Sequential chunk number | 
**ChunkText** | **string** | Original text of the chunk | 
**ContentHash** | **string** | SHA256 hash of the original content | 
**EmbeddingModel** | **string** | Model used to generate the embedding | 
**EmbeddingDim** | **int32** | Embedding vector dimension | 
**Vector** | **[]float32** | Embedding vector | 

## Methods

### NewEmbeddingIngestionItem

`func NewEmbeddingIngestionItem(entityType string, entityId string, chunkIndex int32, chunkText string, contentHash string, embeddingModel string, embeddingDim int32, vector []float32, ) *EmbeddingIngestionItem`

NewEmbeddingIngestionItem instantiates a new EmbeddingIngestionItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingIngestionItemWithDefaults

`func NewEmbeddingIngestionItemWithDefaults() *EmbeddingIngestionItem`

NewEmbeddingIngestionItemWithDefaults instantiates a new EmbeddingIngestionItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntityType

`func (o *EmbeddingIngestionItem) GetEntityType() string`

GetEntityType returns the EntityType field if non-nil, zero value otherwise.

### GetEntityTypeOk

`func (o *EmbeddingIngestionItem) GetEntityTypeOk() (*string, bool)`

GetEntityTypeOk returns a tuple with the EntityType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntityType

`func (o *EmbeddingIngestionItem) SetEntityType(v string)`

SetEntityType sets EntityType field to given value.


### GetEntityId

`func (o *EmbeddingIngestionItem) GetEntityId() string`

GetEntityId returns the EntityId field if non-nil, zero value otherwise.

### GetEntityIdOk

`func (o *EmbeddingIngestionItem) GetEntityIdOk() (*string, bool)`

GetEntityIdOk returns a tuple with the EntityId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntityId

`func (o *EmbeddingIngestionItem) SetEntityId(v string)`

SetEntityId sets EntityId field to given value.


### GetChunkIndex

`func (o *EmbeddingIngestionItem) GetChunkIndex() int32`

GetChunkIndex returns the ChunkIndex field if non-nil, zero value otherwise.

### GetChunkIndexOk

`func (o *EmbeddingIngestionItem) GetChunkIndexOk() (*int32, bool)`

GetChunkIndexOk returns a tuple with the ChunkIndex field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunkIndex

`func (o *EmbeddingIngestionItem) SetChunkIndex(v int32)`

SetChunkIndex sets ChunkIndex field to given value.


### GetChunkText

`func (o *EmbeddingIngestionItem) GetChunkText() string`

GetChunkText returns the ChunkText field if non-nil, zero value otherwise.

### GetChunkTextOk

`func (o *EmbeddingIngestionItem) GetChunkTextOk() (*string, bool)`

GetChunkTextOk returns a tuple with the ChunkText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChunkText

`func (o *EmbeddingIngestionItem) SetChunkText(v string)`

SetChunkText sets ChunkText field to given value.


### GetContentHash

`func (o *EmbeddingIngestionItem) GetContentHash() string`

GetContentHash returns the ContentHash field if non-nil, zero value otherwise.

### GetContentHashOk

`func (o *EmbeddingIngestionItem) GetContentHashOk() (*string, bool)`

GetContentHashOk returns a tuple with the ContentHash field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentHash

`func (o *EmbeddingIngestionItem) SetContentHash(v string)`

SetContentHash sets ContentHash field to given value.


### GetEmbeddingModel

`func (o *EmbeddingIngestionItem) GetEmbeddingModel() string`

GetEmbeddingModel returns the EmbeddingModel field if non-nil, zero value otherwise.

### GetEmbeddingModelOk

`func (o *EmbeddingIngestionItem) GetEmbeddingModelOk() (*string, bool)`

GetEmbeddingModelOk returns a tuple with the EmbeddingModel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingModel

`func (o *EmbeddingIngestionItem) SetEmbeddingModel(v string)`

SetEmbeddingModel sets EmbeddingModel field to given value.


### GetEmbeddingDim

`func (o *EmbeddingIngestionItem) GetEmbeddingDim() int32`

GetEmbeddingDim returns the EmbeddingDim field if non-nil, zero value otherwise.

### GetEmbeddingDimOk

`func (o *EmbeddingIngestionItem) GetEmbeddingDimOk() (*int32, bool)`

GetEmbeddingDimOk returns a tuple with the EmbeddingDim field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmbeddingDim

`func (o *EmbeddingIngestionItem) SetEmbeddingDim(v int32)`

SetEmbeddingDim sets EmbeddingDim field to given value.


### GetVector

`func (o *EmbeddingIngestionItem) GetVector() []float32`

GetVector returns the Vector field if non-nil, zero value otherwise.

### GetVectorOk

`func (o *EmbeddingIngestionItem) GetVectorOk() (*[]float32, bool)`

GetVectorOk returns a tuple with the Vector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVector

`func (o *EmbeddingIngestionItem) SetVector(v []float32)`

SetVector sets Vector field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


