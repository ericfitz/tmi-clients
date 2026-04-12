# ProjectNoteListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the project note | [readonly] 
**Name** | **string** | Note name | 
**Description** | Pointer to **NullableString** | Description of note purpose or context | [optional] 
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Sharable** | Pointer to **bool** | Controls note visibility | [optional] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Methods

### NewProjectNoteListItem

`func NewProjectNoteListItem(id string, name string, ) *ProjectNoteListItem`

NewProjectNoteListItem instantiates a new ProjectNoteListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectNoteListItemWithDefaults

`func NewProjectNoteListItemWithDefaults() *ProjectNoteListItem`

NewProjectNoteListItemWithDefaults instantiates a new ProjectNoteListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ProjectNoteListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ProjectNoteListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ProjectNoteListItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ProjectNoteListItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectNoteListItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectNoteListItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ProjectNoteListItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ProjectNoteListItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ProjectNoteListItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ProjectNoteListItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ProjectNoteListItem) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ProjectNoteListItem) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTimmyEnabled

`func (o *ProjectNoteListItem) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *ProjectNoteListItem) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *ProjectNoteListItem) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *ProjectNoteListItem) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSharable

`func (o *ProjectNoteListItem) GetSharable() bool`

GetSharable returns the Sharable field if non-nil, zero value otherwise.

### GetSharableOk

`func (o *ProjectNoteListItem) GetSharableOk() (*bool, bool)`

GetSharableOk returns a tuple with the Sharable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSharable

`func (o *ProjectNoteListItem) SetSharable(v bool)`

SetSharable sets Sharable field to given value.

### HasSharable

`func (o *ProjectNoteListItem) HasSharable() bool`

HasSharable returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ProjectNoteListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ProjectNoteListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ProjectNoteListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *ProjectNoteListItem) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *ProjectNoteListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ProjectNoteListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ProjectNoteListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *ProjectNoteListItem) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


