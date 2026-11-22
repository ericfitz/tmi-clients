# SurveyListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the survey (UUID) | [readonly] 
**Name** | **string** | Name of the survey | 
**Description** | Pointer to **string** | Description of the survey | [optional] 
**Version** | **string** | Version string | 
**Status** | **string** | Survey status | 
**CreatedAt** | **time.Time** | Creation timestamp (RFC3339) | 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] 
**CreatedBy** | Pointer to [**User**](User.md) | Administrator who created the survey | [optional] 

## Methods

### NewSurveyListItem

`func NewSurveyListItem(id string, name string, version string, status string, createdAt time.Time, ) *SurveyListItem`

NewSurveyListItem instantiates a new SurveyListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyListItemWithDefaults

`func NewSurveyListItemWithDefaults() *SurveyListItem`

NewSurveyListItemWithDefaults instantiates a new SurveyListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SurveyListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SurveyListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SurveyListItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *SurveyListItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SurveyListItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SurveyListItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *SurveyListItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *SurveyListItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *SurveyListItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *SurveyListItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetVersion

`func (o *SurveyListItem) GetVersion() string`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *SurveyListItem) GetVersionOk() (*string, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *SurveyListItem) SetVersion(v string)`

SetVersion sets Version field to given value.


### GetStatus

`func (o *SurveyListItem) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SurveyListItem) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SurveyListItem) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *SurveyListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SurveyListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SurveyListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *SurveyListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *SurveyListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *SurveyListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *SurveyListItem) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetCreatedBy

`func (o *SurveyListItem) GetCreatedBy() User`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *SurveyListItem) GetCreatedByOk() (*User, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *SurveyListItem) SetCreatedBy(v User)`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *SurveyListItem) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


