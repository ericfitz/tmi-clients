# TeamNoteListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the team note | [readonly] 
**Name** | **string** | Note name | 
**Description** | Pointer to **NullableString** | Description of note purpose or context | [optional] 
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Sharable** | Pointer to **bool** | Controls note visibility | [optional] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Methods

### NewTeamNoteListItem

`func NewTeamNoteListItem(id string, name string, ) *TeamNoteListItem`

NewTeamNoteListItem instantiates a new TeamNoteListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamNoteListItemWithDefaults

`func NewTeamNoteListItemWithDefaults() *TeamNoteListItem`

NewTeamNoteListItemWithDefaults instantiates a new TeamNoteListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *TeamNoteListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TeamNoteListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TeamNoteListItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *TeamNoteListItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TeamNoteListItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TeamNoteListItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *TeamNoteListItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TeamNoteListItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TeamNoteListItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TeamNoteListItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *TeamNoteListItem) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *TeamNoteListItem) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTimmyEnabled

`func (o *TeamNoteListItem) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *TeamNoteListItem) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *TeamNoteListItem) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *TeamNoteListItem) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSharable

`func (o *TeamNoteListItem) GetSharable() bool`

GetSharable returns the Sharable field if non-nil, zero value otherwise.

### GetSharableOk

`func (o *TeamNoteListItem) GetSharableOk() (*bool, bool)`

GetSharableOk returns a tuple with the Sharable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSharable

`func (o *TeamNoteListItem) SetSharable(v bool)`

SetSharable sets Sharable field to given value.

### HasSharable

`func (o *TeamNoteListItem) HasSharable() bool`

HasSharable returns a boolean if a field has been set.

### GetCreatedAt

`func (o *TeamNoteListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TeamNoteListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TeamNoteListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TeamNoteListItem) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *TeamNoteListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *TeamNoteListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *TeamNoteListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *TeamNoteListItem) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


