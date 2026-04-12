# AssetInput

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

## Methods

### NewAssetInput

`func NewAssetInput(name string, type_ string, ) *AssetInput`

NewAssetInput instantiates a new AssetInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAssetInputWithDefaults

`func NewAssetInputWithDefaults() *AssetInput`

NewAssetInputWithDefaults instantiates a new AssetInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *AssetInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AssetInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AssetInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *AssetInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AssetInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AssetInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AssetInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *AssetInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *AssetInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *AssetInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AssetInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AssetInput) SetType(v string)`

SetType sets Type field to given value.


### GetCriticality

`func (o *AssetInput) GetCriticality() string`

GetCriticality returns the Criticality field if non-nil, zero value otherwise.

### GetCriticalityOk

`func (o *AssetInput) GetCriticalityOk() (*string, bool)`

GetCriticalityOk returns a tuple with the Criticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticality

`func (o *AssetInput) SetCriticality(v string)`

SetCriticality sets Criticality field to given value.

### HasCriticality

`func (o *AssetInput) HasCriticality() bool`

HasCriticality returns a boolean if a field has been set.

### SetCriticalityNil

`func (o *AssetInput) SetCriticalityNil(b bool)`

 SetCriticalityNil sets the value for Criticality to be an explicit nil

### UnsetCriticality
`func (o *AssetInput) UnsetCriticality()`

UnsetCriticality ensures that no value is present for Criticality, not even an explicit nil
### GetClassification

`func (o *AssetInput) GetClassification() []string`

GetClassification returns the Classification field if non-nil, zero value otherwise.

### GetClassificationOk

`func (o *AssetInput) GetClassificationOk() (*[]string, bool)`

GetClassificationOk returns a tuple with the Classification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassification

`func (o *AssetInput) SetClassification(v []string)`

SetClassification sets Classification field to given value.

### HasClassification

`func (o *AssetInput) HasClassification() bool`

HasClassification returns a boolean if a field has been set.

### SetClassificationNil

`func (o *AssetInput) SetClassificationNil(b bool)`

 SetClassificationNil sets the value for Classification to be an explicit nil

### UnsetClassification
`func (o *AssetInput) UnsetClassification()`

UnsetClassification ensures that no value is present for Classification, not even an explicit nil
### GetSensitivity

`func (o *AssetInput) GetSensitivity() string`

GetSensitivity returns the Sensitivity field if non-nil, zero value otherwise.

### GetSensitivityOk

`func (o *AssetInput) GetSensitivityOk() (*string, bool)`

GetSensitivityOk returns a tuple with the Sensitivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSensitivity

`func (o *AssetInput) SetSensitivity(v string)`

SetSensitivity sets Sensitivity field to given value.

### HasSensitivity

`func (o *AssetInput) HasSensitivity() bool`

HasSensitivity returns a boolean if a field has been set.

### SetSensitivityNil

`func (o *AssetInput) SetSensitivityNil(b bool)`

 SetSensitivityNil sets the value for Sensitivity to be an explicit nil

### UnsetSensitivity
`func (o *AssetInput) UnsetSensitivity()`

UnsetSensitivity ensures that no value is present for Sensitivity, not even an explicit nil
### GetIncludeInReport

`func (o *AssetInput) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *AssetInput) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *AssetInput) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *AssetInput) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


