# TriageNote

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Triage note name | 
**Content** | **string** | Triage note content in markdown format. Safe inline HTML (tables, SVG, formatting) is allowed and sanitized server-side; dangerous elements (script, iframe, event handlers) are stripped. | 
**Id** | **int32** | Sequential identifier for the triage note within its survey response | [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**CreatedBy** | Pointer to **map[string]interface{}** | User who created this triage note | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**ModifiedBy** | Pointer to **map[string]interface{}** | User who last modified this triage note | [optional] [readonly] 

## Methods

### NewTriageNote

`func NewTriageNote(name string, content string, id int32, ) *TriageNote`

NewTriageNote instantiates a new TriageNote object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTriageNoteWithDefaults

`func NewTriageNoteWithDefaults() *TriageNote`

NewTriageNoteWithDefaults instantiates a new TriageNote object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *TriageNote) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TriageNote) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TriageNote) SetName(v string)`

SetName sets Name field to given value.


### GetContent

`func (o *TriageNote) GetContent() string`

GetContent returns the Content field if non-nil, zero value otherwise.

### GetContentOk

`func (o *TriageNote) GetContentOk() (*string, bool)`

GetContentOk returns a tuple with the Content field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContent

`func (o *TriageNote) SetContent(v string)`

SetContent sets Content field to given value.


### GetId

`func (o *TriageNote) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *TriageNote) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *TriageNote) SetId(v int32)`

SetId sets Id field to given value.


### GetCreatedAt

`func (o *TriageNote) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *TriageNote) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *TriageNote) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *TriageNote) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetCreatedBy

`func (o *TriageNote) GetCreatedBy() map[string]interface{}`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *TriageNote) GetCreatedByOk() (*map[string]interface{}, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *TriageNote) SetCreatedBy(v map[string]interface{})`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *TriageNote) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *TriageNote) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *TriageNote) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetModifiedAt

`func (o *TriageNote) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *TriageNote) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *TriageNote) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *TriageNote) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetModifiedBy

`func (o *TriageNote) GetModifiedBy() map[string]interface{}`

GetModifiedBy returns the ModifiedBy field if non-nil, zero value otherwise.

### GetModifiedByOk

`func (o *TriageNote) GetModifiedByOk() (*map[string]interface{}, bool)`

GetModifiedByOk returns a tuple with the ModifiedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedBy

`func (o *TriageNote) SetModifiedBy(v map[string]interface{})`

SetModifiedBy sets ModifiedBy field to given value.

### HasModifiedBy

`func (o *TriageNote) HasModifiedBy() bool`

HasModifiedBy returns a boolean if a field has been set.

### SetModifiedByNil

`func (o *TriageNote) SetModifiedByNil(b bool)`

 SetModifiedByNil sets the value for ModifiedBy to be an explicit nil

### UnsetModifiedBy
`func (o *TriageNote) UnsetModifiedBy()`

UnsetModifiedBy ensures that no value is present for ModifiedBy, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


