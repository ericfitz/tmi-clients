# SurveyResponseListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the response (UUID) | [readonly] 
**Status** | **string** | Current status of the survey response | 
**IsConfidential** | Pointer to **bool** | Whether this is a secret project (no auto Security Reviewers access) | [optional] 
**Owner** | Pointer to [**NullableUser**](User.md) | User who created the response | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp (RFC3339) | 
**SubmittedAt** | Pointer to **NullableTime** | When the response was submitted | [optional] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] 
**SurveyId** | **string** | ID of the survey | 
**SurveyName** | Pointer to **string** | Name of the survey | [optional] 
**SurveyVersion** | Pointer to **string** | Version of the survey | [optional] 

## Methods

### NewSurveyResponseListItem

`func NewSurveyResponseListItem(id string, status string, createdAt time.Time, surveyId string, ) *SurveyResponseListItem`

NewSurveyResponseListItem instantiates a new SurveyResponseListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseListItemWithDefaults

`func NewSurveyResponseListItemWithDefaults() *SurveyResponseListItem`

NewSurveyResponseListItemWithDefaults instantiates a new SurveyResponseListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SurveyResponseListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SurveyResponseListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SurveyResponseListItem) SetId(v string)`

SetId sets Id field to given value.


### GetStatus

`func (o *SurveyResponseListItem) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *SurveyResponseListItem) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *SurveyResponseListItem) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetIsConfidential

`func (o *SurveyResponseListItem) GetIsConfidential() bool`

GetIsConfidential returns the IsConfidential field if non-nil, zero value otherwise.

### GetIsConfidentialOk

`func (o *SurveyResponseListItem) GetIsConfidentialOk() (*bool, bool)`

GetIsConfidentialOk returns a tuple with the IsConfidential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsConfidential

`func (o *SurveyResponseListItem) SetIsConfidential(v bool)`

SetIsConfidential sets IsConfidential field to given value.

### HasIsConfidential

`func (o *SurveyResponseListItem) HasIsConfidential() bool`

HasIsConfidential returns a boolean if a field has been set.

### GetOwner

`func (o *SurveyResponseListItem) GetOwner() User`

GetOwner returns the Owner field if non-nil, zero value otherwise.

### GetOwnerOk

`func (o *SurveyResponseListItem) GetOwnerOk() (*User, bool)`

GetOwnerOk returns a tuple with the Owner field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwner

`func (o *SurveyResponseListItem) SetOwner(v User)`

SetOwner sets Owner field to given value.

### HasOwner

`func (o *SurveyResponseListItem) HasOwner() bool`

HasOwner returns a boolean if a field has been set.

### SetOwnerNil

`func (o *SurveyResponseListItem) SetOwnerNil(b bool)`

 SetOwnerNil sets the value for Owner to be an explicit nil

### UnsetOwner
`func (o *SurveyResponseListItem) UnsetOwner()`

UnsetOwner ensures that no value is present for Owner, not even an explicit nil
### GetCreatedAt

`func (o *SurveyResponseListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SurveyResponseListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SurveyResponseListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetSubmittedAt

`func (o *SurveyResponseListItem) GetSubmittedAt() time.Time`

GetSubmittedAt returns the SubmittedAt field if non-nil, zero value otherwise.

### GetSubmittedAtOk

`func (o *SurveyResponseListItem) GetSubmittedAtOk() (*time.Time, bool)`

GetSubmittedAtOk returns a tuple with the SubmittedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubmittedAt

`func (o *SurveyResponseListItem) SetSubmittedAt(v time.Time)`

SetSubmittedAt sets SubmittedAt field to given value.

### HasSubmittedAt

`func (o *SurveyResponseListItem) HasSubmittedAt() bool`

HasSubmittedAt returns a boolean if a field has been set.

### SetSubmittedAtNil

`func (o *SurveyResponseListItem) SetSubmittedAtNil(b bool)`

 SetSubmittedAtNil sets the value for SubmittedAt to be an explicit nil

### UnsetSubmittedAt
`func (o *SurveyResponseListItem) UnsetSubmittedAt()`

UnsetSubmittedAt ensures that no value is present for SubmittedAt, not even an explicit nil
### GetModifiedAt

`func (o *SurveyResponseListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *SurveyResponseListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *SurveyResponseListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *SurveyResponseListItem) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetSurveyId

`func (o *SurveyResponseListItem) GetSurveyId() string`

GetSurveyId returns the SurveyId field if non-nil, zero value otherwise.

### GetSurveyIdOk

`func (o *SurveyResponseListItem) GetSurveyIdOk() (*string, bool)`

GetSurveyIdOk returns a tuple with the SurveyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyId

`func (o *SurveyResponseListItem) SetSurveyId(v string)`

SetSurveyId sets SurveyId field to given value.


### GetSurveyName

`func (o *SurveyResponseListItem) GetSurveyName() string`

GetSurveyName returns the SurveyName field if non-nil, zero value otherwise.

### GetSurveyNameOk

`func (o *SurveyResponseListItem) GetSurveyNameOk() (*string, bool)`

GetSurveyNameOk returns a tuple with the SurveyName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyName

`func (o *SurveyResponseListItem) SetSurveyName(v string)`

SetSurveyName sets SurveyName field to given value.

### HasSurveyName

`func (o *SurveyResponseListItem) HasSurveyName() bool`

HasSurveyName returns a boolean if a field has been set.

### GetSurveyVersion

`func (o *SurveyResponseListItem) GetSurveyVersion() string`

GetSurveyVersion returns the SurveyVersion field if non-nil, zero value otherwise.

### GetSurveyVersionOk

`func (o *SurveyResponseListItem) GetSurveyVersionOk() (*string, bool)`

GetSurveyVersionOk returns a tuple with the SurveyVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurveyVersion

`func (o *SurveyResponseListItem) SetSurveyVersion(v string)`

SetSurveyVersion sets SurveyVersion field to given value.

### HasSurveyVersion

`func (o *SurveyResponseListItem) HasSurveyVersion() bool`

HasSurveyVersion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


