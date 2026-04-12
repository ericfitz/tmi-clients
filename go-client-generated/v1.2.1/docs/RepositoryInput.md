# RepositoryInput

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

### NewRepositoryInput

`func NewRepositoryInput(uri string, ) *RepositoryInput`

NewRepositoryInput instantiates a new RepositoryInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepositoryInputWithDefaults

`func NewRepositoryInputWithDefaults() *RepositoryInput`

NewRepositoryInputWithDefaults instantiates a new RepositoryInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RepositoryInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RepositoryInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RepositoryInput) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *RepositoryInput) HasName() bool`

HasName returns a boolean if a field has been set.

### GetDescription

`func (o *RepositoryInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RepositoryInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RepositoryInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RepositoryInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RepositoryInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RepositoryInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *RepositoryInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RepositoryInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RepositoryInput) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *RepositoryInput) HasType() bool`

HasType returns a boolean if a field has been set.

### GetParameters

`func (o *RepositoryInput) GetParameters() RepositoryBaseParameters`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *RepositoryInput) GetParametersOk() (*RepositoryBaseParameters, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *RepositoryInput) SetParameters(v RepositoryBaseParameters)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *RepositoryInput) HasParameters() bool`

HasParameters returns a boolean if a field has been set.

### GetUri

`func (o *RepositoryInput) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *RepositoryInput) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *RepositoryInput) SetUri(v string)`

SetUri sets Uri field to given value.


### GetIncludeInReport

`func (o *RepositoryInput) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *RepositoryInput) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *RepositoryInput) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *RepositoryInput) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


