# EmbeddingProviderConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **string** | Embedding provider name | 
**Model** | **string** | Embedding model name | 
**ApiKey** | Pointer to **string** | Embedding provider API key | [optional] 
**BaseUrl** | Pointer to **string** | Custom base URL for self-hosted endpoints | [optional] 

## Methods

### NewEmbeddingProviderConfig

`func NewEmbeddingProviderConfig(provider string, model string, ) *EmbeddingProviderConfig`

NewEmbeddingProviderConfig instantiates a new EmbeddingProviderConfig object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEmbeddingProviderConfigWithDefaults

`func NewEmbeddingProviderConfigWithDefaults() *EmbeddingProviderConfig`

NewEmbeddingProviderConfigWithDefaults instantiates a new EmbeddingProviderConfig object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProvider

`func (o *EmbeddingProviderConfig) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *EmbeddingProviderConfig) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *EmbeddingProviderConfig) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetModel

`func (o *EmbeddingProviderConfig) GetModel() string`

GetModel returns the Model field if non-nil, zero value otherwise.

### GetModelOk

`func (o *EmbeddingProviderConfig) GetModelOk() (*string, bool)`

GetModelOk returns a tuple with the Model field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModel

`func (o *EmbeddingProviderConfig) SetModel(v string)`

SetModel sets Model field to given value.


### GetApiKey

`func (o *EmbeddingProviderConfig) GetApiKey() string`

GetApiKey returns the ApiKey field if non-nil, zero value otherwise.

### GetApiKeyOk

`func (o *EmbeddingProviderConfig) GetApiKeyOk() (*string, bool)`

GetApiKeyOk returns a tuple with the ApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetApiKey

`func (o *EmbeddingProviderConfig) SetApiKey(v string)`

SetApiKey sets ApiKey field to given value.

### HasApiKey

`func (o *EmbeddingProviderConfig) HasApiKey() bool`

HasApiKey returns a boolean if a field has been set.

### GetBaseUrl

`func (o *EmbeddingProviderConfig) GetBaseUrl() string`

GetBaseUrl returns the BaseUrl field if non-nil, zero value otherwise.

### GetBaseUrlOk

`func (o *EmbeddingProviderConfig) GetBaseUrlOk() (*string, bool)`

GetBaseUrlOk returns a tuple with the BaseUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBaseUrl

`func (o *EmbeddingProviderConfig) SetBaseUrl(v string)`

SetBaseUrl sets BaseUrl field to given value.

### HasBaseUrl

`func (o *EmbeddingProviderConfig) HasBaseUrl() bool`

HasBaseUrl returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


