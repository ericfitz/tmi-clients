# ApiInfoService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the service | 
**Build** | **string** | Current build number | 

## Methods

### NewApiInfoService

`func NewApiInfoService(name string, build string, ) *ApiInfoService`

NewApiInfoService instantiates a new ApiInfoService object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoServiceWithDefaults

`func NewApiInfoServiceWithDefaults() *ApiInfoService`

NewApiInfoServiceWithDefaults instantiates a new ApiInfoService object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ApiInfoService) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ApiInfoService) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ApiInfoService) SetName(v string)`

SetName sets Name field to given value.


### GetBuild

`func (o *ApiInfoService) GetBuild() string`

GetBuild returns the Build field if non-nil, zero value otherwise.

### GetBuildOk

`func (o *ApiInfoService) GetBuildOk() (*string, bool)`

GetBuildOk returns a tuple with the Build field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBuild

`func (o *ApiInfoService) SetBuild(v string)`

SetBuild sets Build field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


