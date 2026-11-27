# ApiInfoApi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Version** | **string** | API version | 
**Specification** | **string** | URL to the API specification | 

## Methods

### NewApiInfoApi

`func NewApiInfoApi(version string, specification string, ) *ApiInfoApi`

NewApiInfoApi instantiates a new ApiInfoApi object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoApiWithDefaults

`func NewApiInfoApiWithDefaults() *ApiInfoApi`

NewApiInfoApiWithDefaults instantiates a new ApiInfoApi object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVersion

`func (o *ApiInfoApi) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *ApiInfoApi) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *ApiInfoApi) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetSpecification

`func (o *ApiInfoApi) GetSpecification() string`

GetSpecification returns the Specification field if non-nil, zero value otherwise.

### GetSpecificationOk

`func (o *ApiInfoApi) GetSpecificationOk() (*string, bool)`

GetSpecificationOk returns a tuple with the Specification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSpecification

`func (o *ApiInfoApi) SetSpecification(v string)`

SetSpecification sets Specification field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


