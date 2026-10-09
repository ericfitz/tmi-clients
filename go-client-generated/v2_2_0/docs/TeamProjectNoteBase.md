# TeamProjectNoteBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Note name | 
**Content** | **string** | Note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**Description** | Pointer to **NullableString** | Description of note purpose or context | [optional] 
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Sharable** | Pointer to **bool** | Controls note visibility. When true, visible to all team/project members. When false, only visible to admins and security reviewers. Only admins and security reviewers can set this field; regular users who include this field in requests will receive a 403 error. Default: true for regular users, false for admins/security reviewers. | [optional] 

## Methods

### NewTeamProjectNoteBase

`func NewTeamProjectNoteBase(name string, content string, ) *TeamProjectNoteBase`

NewTeamProjectNoteBase instantiates a new TeamProjectNoteBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamProjectNoteBaseWithDefaults

`func NewTeamProjectNoteBaseWithDefaults() *TeamProjectNoteBase`

NewTeamProjectNoteBaseWithDefaults instantiates a new TeamProjectNoteBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *TeamProjectNoteBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TeamProjectNoteBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TeamProjectNoteBase) SetName(v string)`

SetName sets Name field to given value.


### GetContent

`func (o *TeamProjectNoteBase) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *TeamProjectNoteBase) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *TeamProjectNoteBase) SetContent(v string)`

SetContent sets Content field to given value.


### GetDescription

`func (o *TeamProjectNoteBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TeamProjectNoteBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TeamProjectNoteBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TeamProjectNoteBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *TeamProjectNoteBase) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *TeamProjectNoteBase) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTimmyEnabled

`func (o *TeamProjectNoteBase) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *TeamProjectNoteBase) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *TeamProjectNoteBase) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *TeamProjectNoteBase) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSharable

`func (o *TeamProjectNoteBase) GetSharable() bool`

GetSharable returns the Sharable field if non-nil, zero value otherwise.

### GetSharableOk

`func (o *TeamProjectNoteBase) GetSharableOk() (*bool, bool)`

GetSharableOk returns a tuple with the Sharable field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSharable

`func (o *TeamProjectNoteBase) SetSharable(v bool)`

SetSharable sets Sharable field to given value.

### HasSharable

`func (o *TeamProjectNoteBase) HasSharable() bool`

HasSharable returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


