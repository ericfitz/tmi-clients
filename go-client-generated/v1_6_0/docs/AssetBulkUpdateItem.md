# AssetBulkUpdateItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Asset name | 
**Description** | Pointer to **NullableString** | Description of the asset | [optional] 
**Type** | **string** | Type of asset | 
**Criticality** | Pointer to **NullableString** | Criticality level of the asset | [optional] 
**Classification** | Pointer to **[]string** | Classification tags for the asset | [optional] 
**Sensitivity** | Pointer to **NullableString** | Sensitivity label for the asset | [optional] 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Id** | **string** | Unique identifier of the asset to update (required for bulk updates) | 

## Methods

### NewAssetBulkUpdateItem

`func NewAssetBulkUpdateItem(name string, type_ string, id string, ) *AssetBulkUpdateItem`

NewAssetBulkUpdateItem instantiates a new AssetBulkUpdateItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAssetBulkUpdateItemWithDefaults

`func NewAssetBulkUpdateItemWithDefaults() *AssetBulkUpdateItem`

NewAssetBulkUpdateItemWithDefaults instantiates a new AssetBulkUpdateItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *AssetBulkUpdateItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AssetBulkUpdateItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AssetBulkUpdateItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *AssetBulkUpdateItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AssetBulkUpdateItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AssetBulkUpdateItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AssetBulkUpdateItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *AssetBulkUpdateItem) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *AssetBulkUpdateItem) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *AssetBulkUpdateItem) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AssetBulkUpdateItem) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AssetBulkUpdateItem) SetType(v string)`

SetType sets Type field to given value.


### GetCriticality

`func (o *AssetBulkUpdateItem) GetCriticality() string`

GetCriticality returns the Criticality field if non-nil, zero value otherwise.

### GetCriticalityOk

`func (o *AssetBulkUpdateItem) GetCriticalityOk() (*string, bool)`

GetCriticalityOk returns a tuple with the Criticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticality

`func (o *AssetBulkUpdateItem) SetCriticality(v string)`

SetCriticality sets Criticality field to given value.

### HasCriticality

`func (o *AssetBulkUpdateItem) HasCriticality() bool`

HasCriticality returns a boolean if a field has been set.

### SetCriticalityNil

`func (o *AssetBulkUpdateItem) SetCriticalityNil(b bool)`

 SetCriticalityNil sets the value for Criticality to be an explicit nil

### UnsetCriticality
`func (o *AssetBulkUpdateItem) UnsetCriticality()`

UnsetCriticality ensures that no value is present for Criticality, not even an explicit nil
### GetClassification

`func (o *AssetBulkUpdateItem) GetClassification() []string`

GetClassification returns the Classification field if non-nil, zero value otherwise.

### GetClassificationOk

`func (o *AssetBulkUpdateItem) GetClassificationOk() (*[]string, bool)`

GetClassificationOk returns a tuple with the Classification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassification

`func (o *AssetBulkUpdateItem) SetClassification(v []string)`

SetClassification sets Classification field to given value.

### HasClassification

`func (o *AssetBulkUpdateItem) HasClassification() bool`

HasClassification returns a boolean if a field has been set.

### SetClassificationNil

`func (o *AssetBulkUpdateItem) SetClassificationNil(b bool)`

 SetClassificationNil sets the value for Classification to be an explicit nil

### UnsetClassification
`func (o *AssetBulkUpdateItem) UnsetClassification()`

UnsetClassification ensures that no value is present for Classification, not even an explicit nil
### GetSensitivity

`func (o *AssetBulkUpdateItem) GetSensitivity() string`

GetSensitivity returns the Sensitivity field if non-nil, zero value otherwise.

### GetSensitivityOk

`func (o *AssetBulkUpdateItem) GetSensitivityOk() (*string, bool)`

GetSensitivityOk returns a tuple with the Sensitivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSensitivity

`func (o *AssetBulkUpdateItem) SetSensitivity(v string)`

SetSensitivity sets Sensitivity field to given value.

### HasSensitivity

`func (o *AssetBulkUpdateItem) HasSensitivity() bool`

HasSensitivity returns a boolean if a field has been set.

### SetSensitivityNil

`func (o *AssetBulkUpdateItem) SetSensitivityNil(b bool)`

 SetSensitivityNil sets the value for Sensitivity to be an explicit nil

### UnsetSensitivity
`func (o *AssetBulkUpdateItem) UnsetSensitivity()`

UnsetSensitivity ensures that no value is present for Sensitivity, not even an explicit nil
### GetIncludeInReport

`func (o *AssetBulkUpdateItem) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *AssetBulkUpdateItem) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *AssetBulkUpdateItem) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *AssetBulkUpdateItem) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *AssetBulkUpdateItem) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *AssetBulkUpdateItem) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *AssetBulkUpdateItem) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *AssetBulkUpdateItem) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetId

`func (o *AssetBulkUpdateItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AssetBulkUpdateItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AssetBulkUpdateItem) SetId(v string)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


