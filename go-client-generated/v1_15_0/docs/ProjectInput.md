# ProjectInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Project name | 
**Description** | Pointer to **NullableString** | Project description | [optional] 
**TeamId** | **string** | UUID of the team this project belongs to | 
**RelatedProjects** | Pointer to [**[]RelatedProject**](RelatedProject.md) | Relationships to other projects | [optional] 
**Uri** | Pointer to **NullableString** | URL or reference to internal project page | [optional] 
**Status** | Pointer to [**NullableProjectStatus**](ProjectStatus.md) | Project lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**ResponsibleParties** | Pointer to [**[]ResponsiblePartyInput**](ResponsiblePartyInput.md) | Responsible parties for this project | [optional] 

## Methods

### NewProjectInput

`func NewProjectInput(name string, teamId string, ) *ProjectInput`

NewProjectInput instantiates a new ProjectInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewProjectInputWithDefaults

`func NewProjectInputWithDefaults() *ProjectInput`

NewProjectInputWithDefaults instantiates a new ProjectInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ProjectInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ProjectInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ProjectInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ProjectInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ProjectInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ProjectInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ProjectInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ProjectInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ProjectInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetTeamId

`func (o *ProjectInput) GetTeamId() string`

GetTeamId returns the TeamId field if non-nil, zero value otherwise.

### GetTeamIdOk

`func (o *ProjectInput) GetTeamIdOk() (*string, bool)`

GetTeamIdOk returns a tuple with the TeamId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTeamId

`func (o *ProjectInput) SetTeamId(v string)`

SetTeamId sets TeamId field to given value.


### GetRelatedProjects

`func (o *ProjectInput) GetRelatedProjects() []RelatedProject`

GetRelatedProjects returns the RelatedProjects field if non-nil, zero value otherwise.

### GetRelatedProjectsOk

`func (o *ProjectInput) GetRelatedProjectsOk() (*[]RelatedProject, bool)`

GetRelatedProjectsOk returns a tuple with the RelatedProjects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedProjects

`func (o *ProjectInput) SetRelatedProjects(v []RelatedProject)`

SetRelatedProjects sets RelatedProjects field to given value.

### HasRelatedProjects

`func (o *ProjectInput) HasRelatedProjects() bool`

HasRelatedProjects returns a boolean if a field has been set.

### GetUri

`func (o *ProjectInput) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *ProjectInput) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *ProjectInput) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *ProjectInput) HasUri() bool`

HasUri returns a boolean if a field has been set.

### SetUriNil

`func (o *ProjectInput) SetUriNil(b bool)`

 SetUriNil sets the value for Uri to be an explicit nil

### UnsetUri
`func (o *ProjectInput) UnsetUri()`

UnsetUri ensures that no value is present for Uri, not even an explicit nil
### GetStatus

`func (o *ProjectInput) GetStatus() ProjectStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ProjectInput) GetStatusOk() (*ProjectStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ProjectInput) SetStatus(v ProjectStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ProjectInput) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ProjectInput) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ProjectInput) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetResponsibleParties

`func (o *ProjectInput) GetResponsibleParties() []ResponsiblePartyInput`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *ProjectInput) GetResponsiblePartiesOk() (*[]ResponsiblePartyInput, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *ProjectInput) SetResponsibleParties(v []ResponsiblePartyInput)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *ProjectInput) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


