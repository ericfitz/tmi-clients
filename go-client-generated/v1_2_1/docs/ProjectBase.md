# ProjectBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Project name | 
**Description** | Pointer to **string** | Project description | [optional] 
**TeamId** | **string** | UUID of the team this project belongs to | 
**ResponsibleParties** | Pointer to [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this project | [optional] 
**RelatedProjects** | Pointer to [**[]RelatedProject**](RelatedProject.md) | Relationships to other projects | [optional] 
**Uri** | Pointer to **string** | URL or reference to internal project page | [optional] 
**Status** | Pointer to **string** | Project status (lifecycle, archival, deprecation, etc.) | [optional] 

## Methods

### NewProjectBase

`func NewProjectBase(name string, teamId string, ) *ProjectBase`

NewProjectBase instantiates a new ProjectBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectBaseWithDefaults

`func NewProjectBaseWithDefaults() *ProjectBase`

NewProjectBaseWithDefaults instantiates a new ProjectBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ProjectBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectBase) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ProjectBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ProjectBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ProjectBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ProjectBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetTeamId

`func (o *ProjectBase) GetTeamId() string`

GetTeamId returns the TeamId field if non-nil, zero value otherwise.

### GetTeamIdOk

`func (o *ProjectBase) GetTeamIdOk() (*string, bool)`

GetTeamIdOk returns a tuple with the TeamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamId

`func (o *ProjectBase) SetTeamId(v string)`

SetTeamId sets TeamId field to given value.


### GetResponsibleParties

`func (o *ProjectBase) GetResponsibleParties() []ResponsibleParty`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *ProjectBase) GetResponsiblePartiesOk() (*[]ResponsibleParty, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *ProjectBase) SetResponsibleParties(v []ResponsibleParty)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *ProjectBase) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.

### GetRelatedProjects

`func (o *ProjectBase) GetRelatedProjects() []RelatedProject`

GetRelatedProjects returns the RelatedProjects field if non-nil, zero value otherwise.

### GetRelatedProjectsOk

`func (o *ProjectBase) GetRelatedProjectsOk() (*[]RelatedProject, bool)`

GetRelatedProjectsOk returns a tuple with the RelatedProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedProjects

`func (o *ProjectBase) SetRelatedProjects(v []RelatedProject)`

SetRelatedProjects sets RelatedProjects field to given value.

### HasRelatedProjects

`func (o *ProjectBase) HasRelatedProjects() bool`

HasRelatedProjects returns a boolean if a field has been set.

### GetUri

`func (o *ProjectBase) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *ProjectBase) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *ProjectBase) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *ProjectBase) HasUri() bool`

HasUri returns a boolean if a field has been set.

### GetStatus

`func (o *ProjectBase) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProjectBase) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProjectBase) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ProjectBase) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


