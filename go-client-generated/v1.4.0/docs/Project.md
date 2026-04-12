# Project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Project name | 
**Description** | Pointer to **NullableString** | Project description | [optional] 
**TeamId** | **string** | UUID of the team this project belongs to | 
**ResponsibleParties** | Pointer to [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this project | [optional] 
**RelatedProjects** | Pointer to [**[]RelatedProject**](RelatedProject.md) | Relationships to other projects | [optional] 
**Uri** | Pointer to **NullableString** | URL or reference to internal project page | [optional] 
**Status** | Pointer to [**NullableProjectStatus**](ProjectStatus.md) | Project lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**Id** | Pointer to **string** | Unique identifier for the project (UUID) | [optional] [readonly] 
**Team** | Pointer to **map[string]interface{}** | The team this project belongs to (resolved) | [optional] [readonly] 
**CreatedBy** | Pointer to **map[string]interface{}** | User who created the project | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedBy** | Pointer to **map[string]interface{}** | User who last modified the project | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**ReviewedBy** | Pointer to **map[string]interface{}** | User who last reviewed the project | [optional] 
**ReviewedAt** | Pointer to **NullableTime** | Last review timestamp (RFC3339) | [optional] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**Notes** | Pointer to [**[]ProjectNoteListItem**](ProjectNoteListItem.md) | List of notes associated with the project | [optional] [readonly] 

## Methods

### NewProject

`func NewProject(name string, teamId string, ) *Project`

NewProject instantiates a new Project object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectWithDefaults

`func NewProjectWithDefaults() *Project`

NewProjectWithDefaults instantiates a new Project object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Project) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Project) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Project) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Project) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Project) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Project) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Project) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Project) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Project) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTeamId

`func (o *Project) GetTeamId() string`

GetTeamId returns the TeamId field if non-nil, zero value otherwise.

### GetTeamIdOk

`func (o *Project) GetTeamIdOk() (*string, bool)`

GetTeamIdOk returns a tuple with the TeamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamId

`func (o *Project) SetTeamId(v string)`

SetTeamId sets TeamId field to given value.


### GetResponsibleParties

`func (o *Project) GetResponsibleParties() []ResponsibleParty`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *Project) GetResponsiblePartiesOk() (*[]ResponsibleParty, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *Project) SetResponsibleParties(v []ResponsibleParty)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *Project) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.

### GetRelatedProjects

`func (o *Project) GetRelatedProjects() []RelatedProject`

GetRelatedProjects returns the RelatedProjects field if non-nil, zero value otherwise.

### GetRelatedProjectsOk

`func (o *Project) GetRelatedProjectsOk() (*[]RelatedProject, bool)`

GetRelatedProjectsOk returns a tuple with the RelatedProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedProjects

`func (o *Project) SetRelatedProjects(v []RelatedProject)`

SetRelatedProjects sets RelatedProjects field to given value.

### HasRelatedProjects

`func (o *Project) HasRelatedProjects() bool`

HasRelatedProjects returns a boolean if a field has been set.

### GetUri

`func (o *Project) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *Project) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *Project) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *Project) HasUri() bool`

HasUri returns a boolean if a field has been set.

### SetUriNil

`func (o *Project) SetUriNil(b bool)`

 SetUriNil sets the value for Uri to be an explicit nil

### UnsetUri
`func (o *Project) UnsetUri()`

UnsetUri ensures that no value is present for Uri, not even an explicit nil
### GetStatus

`func (o *Project) GetStatus() ProjectStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *Project) GetStatusOk() (*ProjectStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *Project) SetStatus(v ProjectStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *Project) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *Project) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *Project) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetId

`func (o *Project) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Project) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Project) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Project) HasId() bool`

HasId returns a boolean if a field has been set.

### GetTeam

`func (o *Project) GetTeam() map[string]interface{}`

GetTeam returns the Team field if non-nil, zero value otherwise.

### GetTeamOk

`func (o *Project) GetTeamOk() (*map[string]interface{}, bool)`

GetTeamOk returns a tuple with the Team field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeam

`func (o *Project) SetTeam(v map[string]interface{})`

SetTeam sets Team field to given value.

### HasTeam

`func (o *Project) HasTeam() bool`

HasTeam returns a boolean if a field has been set.

### SetTeamNil

`func (o *Project) SetTeamNil(b bool)`

 SetTeamNil sets the value for Team to be an explicit nil

### UnsetTeam
`func (o *Project) UnsetTeam()`

UnsetTeam ensures that no value is present for Team, not even an explicit nil
### GetCreatedBy

`func (o *Project) GetCreatedBy() map[string]interface{}`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *Project) GetCreatedByOk() (*map[string]interface{}, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *Project) SetCreatedBy(v map[string]interface{})`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *Project) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *Project) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *Project) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetCreatedAt

`func (o *Project) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Project) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Project) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Project) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedBy

`func (o *Project) GetModifiedBy() map[string]interface{}`

GetModifiedBy returns the ModifiedBy field if non-nil, zero value otherwise.

### GetModifiedByOk

`func (o *Project) GetModifiedByOk() (*map[string]interface{}, bool)`

GetModifiedByOk returns a tuple with the ModifiedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedBy

`func (o *Project) SetModifiedBy(v map[string]interface{})`

SetModifiedBy sets ModifiedBy field to given value.

### HasModifiedBy

`func (o *Project) HasModifiedBy() bool`

HasModifiedBy returns a boolean if a field has been set.

### SetModifiedByNil

`func (o *Project) SetModifiedByNil(b bool)`

 SetModifiedByNil sets the value for ModifiedBy to be an explicit nil

### UnsetModifiedBy
`func (o *Project) UnsetModifiedBy()`

UnsetModifiedBy ensures that no value is present for ModifiedBy, not even an explicit nil
### GetModifiedAt

`func (o *Project) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *Project) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *Project) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *Project) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetReviewedBy

`func (o *Project) GetReviewedBy() map[string]interface{}`

GetReviewedBy returns the ReviewedBy field if non-nil, zero value otherwise.

### GetReviewedByOk

`func (o *Project) GetReviewedByOk() (*map[string]interface{}, bool)`

GetReviewedByOk returns a tuple with the ReviewedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedBy

`func (o *Project) SetReviewedBy(v map[string]interface{})`

SetReviewedBy sets ReviewedBy field to given value.

### HasReviewedBy

`func (o *Project) HasReviewedBy() bool`

HasReviewedBy returns a boolean if a field has been set.

### SetReviewedByNil

`func (o *Project) SetReviewedByNil(b bool)`

 SetReviewedByNil sets the value for ReviewedBy to be an explicit nil

### UnsetReviewedBy
`func (o *Project) UnsetReviewedBy()`

UnsetReviewedBy ensures that no value is present for ReviewedBy, not even an explicit nil
### GetReviewedAt

`func (o *Project) GetReviewedAt() time.Time`

GetReviewedAt returns the ReviewedAt field if non-nil, zero value otherwise.

### GetReviewedAtOk

`func (o *Project) GetReviewedAtOk() (*time.Time, bool)`

GetReviewedAtOk returns a tuple with the ReviewedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedAt

`func (o *Project) SetReviewedAt(v time.Time)`

SetReviewedAt sets ReviewedAt field to given value.

### HasReviewedAt

`func (o *Project) HasReviewedAt() bool`

HasReviewedAt returns a boolean if a field has been set.

### SetReviewedAtNil

`func (o *Project) SetReviewedAtNil(b bool)`

 SetReviewedAtNil sets the value for ReviewedAt to be an explicit nil

### UnsetReviewedAt
`func (o *Project) UnsetReviewedAt()`

UnsetReviewedAt ensures that no value is present for ReviewedAt, not even an explicit nil
### GetMetadata

`func (o *Project) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Project) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Project) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Project) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *Project) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *Project) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetNotes

`func (o *Project) GetNotes() []ProjectNoteListItem`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *Project) GetNotesOk() (*[]ProjectNoteListItem, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *Project) SetNotes(v []ProjectNoteListItem)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *Project) HasNotes() bool`

HasNotes returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


