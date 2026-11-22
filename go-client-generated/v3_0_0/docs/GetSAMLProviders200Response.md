# GetSAMLProviders200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Providers** | [**[]SAMLProviderInfo**](SAMLProviderInfo.md) |  | 

## Methods

### NewGetSAMLProviders200Response

`func NewGetSAMLProviders200Response(providers []SAMLProviderInfo, ) *GetSAMLProviders200Response`

NewGetSAMLProviders200Response instantiates a new GetSAMLProviders200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetSAMLProviders200ResponseWithDefaults

`func NewGetSAMLProviders200ResponseWithDefaults() *GetSAMLProviders200Response`

NewGetSAMLProviders200ResponseWithDefaults instantiates a new GetSAMLProviders200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProviders

`func (o *GetSAMLProviders200Response) GetProviders() []SAMLProviderInfo`

GetProviders returns the Providers field if non-nil, zero value otherwise.

### GetProvidersOk

`func (o *GetSAMLProviders200Response) GetProvidersOk() (*[]SAMLProviderInfo, bool)`

GetProvidersOk returns a tuple with the Providers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviders

`func (o *GetSAMLProviders200Response) SetProviders(v []SAMLProviderInfo)`

SetProviders sets Providers field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


