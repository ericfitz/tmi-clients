# EmbeddingConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**TextEmbedding** | [**EmbeddingProviderConfig**](EmbeddingProviderConfig.md) |  | 
**CodeEmbedding** | Pointer to [**NullableEmbeddingProviderConfig**](EmbeddingProviderConfig.md) | Code embedding config. Null if not configured. | [optional] 

## Methods

### NewEmbeddingConfig

`func NewEmbeddingConfig(textEmbedding EmbeddingProviderConfig, ) *EmbeddingConfig`

NewEmbeddingConfig instantiates a new EmbeddingConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingConfigWithDefaults

`func NewEmbeddingConfigWithDefaults() *EmbeddingConfig`

NewEmbeddingConfigWithDefaults instantiates a new EmbeddingConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetTextEmbedding

`func (o *EmbeddingConfig) GetTextEmbedding() EmbeddingProviderConfig`

GetTextEmbedding returns the TextEmbedding field if non-nil, zero value otherwise.

### GetTextEmbeddingOk

`func (o *EmbeddingConfig) GetTextEmbeddingOk() (*EmbeddingProviderConfig, bool)`

GetTextEmbeddingOk returns a tuple with the TextEmbedding field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextEmbedding

`func (o *EmbeddingConfig) SetTextEmbedding(v EmbeddingProviderConfig)`

SetTextEmbedding sets TextEmbedding field to given value.


### GetCodeEmbedding

`func (o *EmbeddingConfig) GetCodeEmbedding() EmbeddingProviderConfig`

GetCodeEmbedding returns the CodeEmbedding field if non-nil, zero value otherwise.

### GetCodeEmbeddingOk

`func (o *EmbeddingConfig) GetCodeEmbeddingOk() (*EmbeddingProviderConfig, bool)`

GetCodeEmbeddingOk returns a tuple with the CodeEmbedding field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeEmbedding

`func (o *EmbeddingConfig) SetCodeEmbedding(v EmbeddingProviderConfig)`

SetCodeEmbedding sets CodeEmbedding field to given value.

### HasCodeEmbedding

`func (o *EmbeddingConfig) HasCodeEmbedding() bool`

HasCodeEmbedding returns a boolean if a field has been set.

### SetCodeEmbeddingNil

`func (o *EmbeddingConfig) SetCodeEmbeddingNil(b bool)`

 SetCodeEmbeddingNil sets the value for CodeEmbedding to be an explicit nil

### UnsetCodeEmbedding
`func (o *EmbeddingConfig) UnsetCodeEmbedding()`

UnsetCodeEmbedding ensures that no value is present for CodeEmbedding, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


