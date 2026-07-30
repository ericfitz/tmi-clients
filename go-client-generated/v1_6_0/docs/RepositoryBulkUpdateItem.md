# RepositoryBulkUpdateItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | Name for the source code reference | [optional] 
**Description** | Pointer to **NullableString** | Description of the referenced source code | [optional] 
**Type** | Pointer to **NullableString** | Source code repository type | [optional] 
**Parameters** | Pointer to [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**Uri** | **string** | URL to retrieve the referenced source code | 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Id** | **string** | Unique identifier of the repository to update (required for bulk updates) | 

## Methods

### NewRepositoryBulkUpdateItem

`func NewRepositoryBulkUpdateItem(uri string, id string, ) *RepositoryBulkUpdateItem`

NewRepositoryBulkUpdateItem instantiates a new RepositoryBulkUpdateItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRepositoryBulkUpdateItemWithDefaults

`func NewRepositoryBulkUpdateItemWithDefaults() *RepositoryBulkUpdateItem`

NewRepositoryBulkUpdateItemWithDefaults instantiates a new RepositoryBulkUpdateItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *RepositoryBulkUpdateItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *RepositoryBulkUpdateItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *RepositoryBulkUpdateItem) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *RepositoryBulkUpdateItem) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *RepositoryBulkUpdateItem) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *RepositoryBulkUpdateItem) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetDescription

`func (o *RepositoryBulkUpdateItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *RepositoryBulkUpdateItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *RepositoryBulkUpdateItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *RepositoryBulkUpdateItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *RepositoryBulkUpdateItem) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *RepositoryBulkUpdateItem) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *RepositoryBulkUpdateItem) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *RepositoryBulkUpdateItem) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *RepositoryBulkUpdateItem) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *RepositoryBulkUpdateItem) HasType() bool`

HasType returns a boolean if a field has been set.

### SetTypeNil

`func (o *RepositoryBulkUpdateItem) SetTypeNil(b bool)`

 SetTypeNil sets the value for Type to be an explicit nil

### UnsetType
`func (o *RepositoryBulkUpdateItem) UnsetType()`

UnsetType ensures that no value is present for Type, not even an explicit nil
### GetParameters

`func (o *RepositoryBulkUpdateItem) GetParameters() RepositoryBaseParameters`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *RepositoryBulkUpdateItem) GetParametersOk() (*RepositoryBaseParameters, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *RepositoryBulkUpdateItem) SetParameters(v RepositoryBaseParameters)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *RepositoryBulkUpdateItem) HasParameters() bool`

HasParameters returns a boolean if a field has been set.

### GetUri

`func (o *RepositoryBulkUpdateItem) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *RepositoryBulkUpdateItem) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *RepositoryBulkUpdateItem) SetUri(v string)`

SetUri sets Uri field to given value.


### GetIncludeInReport

`func (o *RepositoryBulkUpdateItem) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *RepositoryBulkUpdateItem) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *RepositoryBulkUpdateItem) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *RepositoryBulkUpdateItem) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *RepositoryBulkUpdateItem) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *RepositoryBulkUpdateItem) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *RepositoryBulkUpdateItem) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *RepositoryBulkUpdateItem) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetId

`func (o *RepositoryBulkUpdateItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *RepositoryBulkUpdateItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *RepositoryBulkUpdateItem) SetId(v string)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


