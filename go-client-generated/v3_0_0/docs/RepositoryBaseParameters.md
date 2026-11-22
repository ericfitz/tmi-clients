# RepositoryBaseParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RefType** | **string** | Reference type (branch, tag, or commit) | 
**RefValue** | **string** | Reference value (branch name, tag value, or commit id) | 
**SubPath** | Pointer to **string** | Sub-path within the repository | [optional] 

## Methods

### NewRepositoryBaseParameters

`func NewRepositoryBaseParameters(refType string, refValue string, ) *RepositoryBaseParameters`

NewRepositoryBaseParameters instantiates a new RepositoryBaseParameters object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepositoryBaseParametersWithDefaults

`func NewRepositoryBaseParametersWithDefaults() *RepositoryBaseParameters`

NewRepositoryBaseParametersWithDefaults instantiates a new RepositoryBaseParameters object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRefType

`func (o *RepositoryBaseParameters) GetRefType() string`

GetRefType returns the RefType field if non-nil, zero value otherwise.

### GetRefTypeOk

`func (o *RepositoryBaseParameters) GetRefTypeOk() (*string, bool)`

GetRefTypeOk returns a tuple with the RefType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefType

`func (o *RepositoryBaseParameters) SetRefType(v string)`

SetRefType sets RefType field to given value.


### GetRefValue

`func (o *RepositoryBaseParameters) GetRefValue() string`

GetRefValue returns the RefValue field if non-nil, zero value otherwise.

### GetRefValueOk

`func (o *RepositoryBaseParameters) GetRefValueOk() (*string, bool)`

GetRefValueOk returns a tuple with the RefValue field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefValue

`func (o *RepositoryBaseParameters) SetRefValue(v string)`

SetRefValue sets RefValue field to given value.


### GetSubPath

`func (o *RepositoryBaseParameters) GetSubPath() string`

GetSubPath returns the SubPath field if non-nil, zero value otherwise.

### GetSubPathOk

`func (o *RepositoryBaseParameters) GetSubPathOk() (*string, bool)`

GetSubPathOk returns a tuple with the SubPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubPath

`func (o *RepositoryBaseParameters) SetSubPath(v string)`

SetSubPath sets SubPath field to given value.

### HasSubPath

`func (o *RepositoryBaseParameters) HasSubPath() bool`

HasSubPath returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


