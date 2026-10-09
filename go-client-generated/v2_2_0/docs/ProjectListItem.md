# ProjectListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Name** | **string** |  | 
**Description** | Pointer to **NullableString** |  | [optional] 
**Status** | Pointer to [**NullableProjectStatus**](ProjectStatus.md) | Project lifecycle status. | [optional] 
**TeamId** | **string** |  | 
**TeamName** | Pointer to **string** | Name of the associated team | [optional] 
**CreatedAt** | **time.Time** |  | 
**ModifiedAt** | Pointer to **time.Time** |  | [optional] 
**NoteCount** | Pointer to **int32** | Number of notes associated with this project | [optional] 

## Methods

### NewProjectListItem

`func NewProjectListItem(id string, name string, teamId string, createdAt time.Time, ) *ProjectListItem`

NewProjectListItem instantiates a new ProjectListItem object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectListItemWithDefaults

`func NewProjectListItemWithDefaults() *ProjectListItem`

NewProjectListItemWithDefaults instantiates a new ProjectListItem object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *ProjectListItem) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ProjectListItem) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ProjectListItem) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *ProjectListItem) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectListItem) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectListItem) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ProjectListItem) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ProjectListItem) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ProjectListItem) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ProjectListItem) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ProjectListItem) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ProjectListItem) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetStatus

`func (o *ProjectListItem) GetStatus() ProjectStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProjectListItem) GetStatusOk() (*ProjectStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProjectListItem) SetStatus(v ProjectStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ProjectListItem) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ProjectListItem) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ProjectListItem) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetTeamId

`func (o *ProjectListItem) GetTeamId() string`

GetTeamId returns the TeamId field if non-nil, zero value otherwise.

### GetTeamIdOk

`func (o *ProjectListItem) GetTeamIdOk() (*string, bool)`

GetTeamIdOk returns a tuple with the TeamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamId

`func (o *ProjectListItem) SetTeamId(v string)`

SetTeamId sets TeamId field to given value.


### GetTeamName

`func (o *ProjectListItem) GetTeamName() string`

GetTeamName returns the TeamName field if non-nil, zero value otherwise.

### GetTeamNameOk

`func (o *ProjectListItem) GetTeamNameOk() (*string, bool)`

GetTeamNameOk returns a tuple with the TeamName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamName

`func (o *ProjectListItem) SetTeamName(v string)`

SetTeamName sets TeamName field to given value.

### HasTeamName

`func (o *ProjectListItem) HasTeamName() bool`

HasTeamName returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ProjectListItem) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ProjectListItem) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ProjectListItem) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *ProjectListItem) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *ProjectListItem) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *ProjectListItem) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *ProjectListItem) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetNoteCount

`func (o *ProjectListItem) GetNoteCount() int32`

GetNoteCount returns the NoteCount field if non-nil, zero value otherwise.

### GetNoteCountOk

`func (o *ProjectListItem) GetNoteCountOk() (*int32, bool)`

GetNoteCountOk returns a tuple with the NoteCount field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNoteCount

`func (o *ProjectListItem) SetNoteCount(v int32)`

SetNoteCount sets NoteCount field to given value.

### HasNoteCount

`func (o *ProjectListItem) HasNoteCount() bool`

HasNoteCount returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


