# RepositoryBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **string** | Name for the source code reference | [optional] 
**Description** | Pointer to **NullableString** | Description of the referenced source code | [optional] 
**Type** | Pointer to **string** | Source code repository type | [optional] 
**Parameters** | Pointer to [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**Uri** | **string** | URL to retrieve the referenced source code | 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]

## Methods

### NewRepositoryBase

`func NewRepositoryBase(uri string, ) *RepositoryBase`

NewRepositoryBase instantiates a new RepositoryBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepositoryBaseWithDefaults

`func NewRepositoryBaseWithDefaults() *RepositoryBase`

NewRepositoryBaseWithDefaults instantiates a new RepositoryBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RepositoryBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RepositoryBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RepositoryBase) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *RepositoryBase) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *RepositoryBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RepositoryBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RepositoryBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RepositoryBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RepositoryBase) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RepositoryBase) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *RepositoryBase) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RepositoryBase) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RepositoryBase) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *RepositoryBase) HasType() bool`

HasType returns a boolean if a field has been set.

### GetParameters

`func (o *RepositoryBase) GetParameters() RepositoryBaseParameters`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *RepositoryBase) GetParametersOk() (*RepositoryBaseParameters, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *RepositoryBase) SetParameters(v RepositoryBaseParameters)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *RepositoryBase) HasParameters() bool`

HasParameters returns a boolean if a field has been set.

### GetUri

`func (o *RepositoryBase) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *RepositoryBase) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *RepositoryBase) SetUri(v string)`

SetUri sets Uri field to given value.


### GetIncludeInReport

`func (o *RepositoryBase) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *RepositoryBase) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *RepositoryBase) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *RepositoryBase) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


