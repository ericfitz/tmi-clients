# ExtendedAsset

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
**Id** | **string** | Unique identifier for the asset | [readonly] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] [readonly] 
**CreatedAt** | **time.Time** | Creation timestamp (ISO3339) | 
**ModifiedAt** | **time.Time** | Last modification timestamp (ISO3339) | 
**DeletedAt** | Pointer to **NullableTime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 
**ThreatModelId** | **string** | ID of the threat model this asset belongs to | 

## Methods

### NewExtendedAsset

`func NewExtendedAsset(name string, type_ string, id string, createdAt time.Time, modifiedAt time.Time, threatModelId string, ) *ExtendedAsset`

NewExtendedAsset instantiates a new ExtendedAsset object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExtendedAssetWithDefaults

`func NewExtendedAssetWithDefaults() *ExtendedAsset`

NewExtendedAssetWithDefaults instantiates a new ExtendedAsset object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ExtendedAsset) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ExtendedAsset) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ExtendedAsset) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ExtendedAsset) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ExtendedAsset) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ExtendedAsset) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ExtendedAsset) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ExtendedAsset) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ExtendedAsset) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetType

`func (o *ExtendedAsset) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *ExtendedAsset) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *ExtendedAsset) SetType(v string)`

SetType sets Type field to given value.


### GetCriticality

`func (o *ExtendedAsset) GetCriticality() string`

GetCriticality returns the Criticality field if non-nil, zero value otherwise.

### GetCriticalityOk

`func (o *ExtendedAsset) GetCriticalityOk() (*string, bool)`

GetCriticalityOk returns a tuple with the Criticality field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCriticality

`func (o *ExtendedAsset) SetCriticality(v string)`

SetCriticality sets Criticality field to given value.

### HasCriticality

`func (o *ExtendedAsset) HasCriticality() bool`

HasCriticality returns a boolean if a field has been set.

### SetCriticalityNil

`func (o *ExtendedAsset) SetCriticalityNil(b bool)`

 SetCriticalityNil sets the value for Criticality to be an explicit nil

### UnsetCriticality
`func (o *ExtendedAsset) UnsetCriticality()`

UnsetCriticality ensures that no value is present for Criticality, not even an explicit nil
### GetClassification

`func (o *ExtendedAsset) GetClassification() []string`

GetClassification returns the Classification field if non-nil, zero value otherwise.

### GetClassificationOk

`func (o *ExtendedAsset) GetClassificationOk() (*[]string, bool)`

GetClassificationOk returns a tuple with the Classification field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClassification

`func (o *ExtendedAsset) SetClassification(v []string)`

SetClassification sets Classification field to given value.

### HasClassification

`func (o *ExtendedAsset) HasClassification() bool`

HasClassification returns a boolean if a field has been set.

### SetClassificationNil

`func (o *ExtendedAsset) SetClassificationNil(b bool)`

 SetClassificationNil sets the value for Classification to be an explicit nil

### UnsetClassification
`func (o *ExtendedAsset) UnsetClassification()`

UnsetClassification ensures that no value is present for Classification, not even an explicit nil
### GetSensitivity

`func (o *ExtendedAsset) GetSensitivity() string`

GetSensitivity returns the Sensitivity field if non-nil, zero value otherwise.

### GetSensitivityOk

`func (o *ExtendedAsset) GetSensitivityOk() (*string, bool)`

GetSensitivityOk returns a tuple with the Sensitivity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSensitivity

`func (o *ExtendedAsset) SetSensitivity(v string)`

SetSensitivity sets Sensitivity field to given value.

### HasSensitivity

`func (o *ExtendedAsset) HasSensitivity() bool`

HasSensitivity returns a boolean if a field has been set.

### SetSensitivityNil

`func (o *ExtendedAsset) SetSensitivityNil(b bool)`

 SetSensitivityNil sets the value for Sensitivity to be an explicit nil

### UnsetSensitivity
`func (o *ExtendedAsset) UnsetSensitivity()`

UnsetSensitivity ensures that no value is present for Sensitivity, not even an explicit nil
### GetIncludeInReport

`func (o *ExtendedAsset) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *ExtendedAsset) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *ExtendedAsset) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *ExtendedAsset) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *ExtendedAsset) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *ExtendedAsset) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *ExtendedAsset) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *ExtendedAsset) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetId

`func (o *ExtendedAsset) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ExtendedAsset) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ExtendedAsset) SetId(v string)`

SetId sets Id field to given value.


### GetMetadata

`func (o *ExtendedAsset) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ExtendedAsset) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ExtendedAsset) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ExtendedAsset) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ExtendedAsset) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ExtendedAsset) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ExtendedAsset) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *ExtendedAsset) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ExtendedAsset) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ExtendedAsset) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetDeletedAt

`func (o *ExtendedAsset) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *ExtendedAsset) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *ExtendedAsset) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *ExtendedAsset) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *ExtendedAsset) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *ExtendedAsset) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetThreatModelId

`func (o *ExtendedAsset) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *ExtendedAsset) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *ExtendedAsset) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


