# TeamNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Note name | 
**Content** | **string** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**Description** | Pointer to **NullableString** | Description of note purpose or context | [optional] 
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Sharable** | Pointer to **bool** | Controls note visibility. When true, visible to all team/project members. When false, only visible to admins and security reviewers. Only admins and security reviewers can set this field; regular users who include this field in requests will receive a 403 error. Default: true for regular users, false for admins/security reviewers. | [optional] 
**Id** | **string** | Unique identifier for the team note | [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Methods

### NewTeamNote

`func NewTeamNote(name string, content string, id string, ) *TeamNote`

NewTeamNote instantiates a new TeamNote object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamNoteWithDefaults

`func NewTeamNoteWithDefaults() *TeamNote`

NewTeamNoteWithDefaults instantiates a new TeamNote object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *TeamNote) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TeamNote) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TeamNote) SetName(v string)`

SetName sets Name field to given value.


### GetContent

`func (o *TeamNote) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *TeamNote) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *TeamNote) SetContent(v string)`

SetContent sets Content field to given value.


### GetDescription

`func (o *TeamNote) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TeamNote) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TeamNote) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TeamNote) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *TeamNote) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *TeamNote) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTimmyEnabled

`func (o *TeamNote) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *TeamNote) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *TeamNote) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *TeamNote) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSharable

`func (o *TeamNote) GetSharable() bool`

GetSharable returns the Sharable field if non-nil, zero value otherwise.

### GetSharableOk

`func (o *TeamNote) GetSharableOk() (*bool, bool)`

GetSharableOk returns a tuple with the Sharable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSharable

`func (o *TeamNote) SetSharable(v bool)`

SetSharable sets Sharable field to given value.

### HasSharable

`func (o *TeamNote) HasSharable() bool`

HasSharable returns a boolean if a field has been set.

### GetId

`func (o *TeamNote) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TeamNote) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TeamNote) SetId(v string)`

SetId sets Id field to given value.


### GetCreatedAt

`func (o *TeamNote) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TeamNote) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TeamNote) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TeamNote) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *TeamNote) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *TeamNote) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *TeamNote) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *TeamNote) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


