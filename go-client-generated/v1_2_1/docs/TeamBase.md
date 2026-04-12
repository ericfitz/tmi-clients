# TeamBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Team name | 
**Description** | Pointer to **string** | Team description | [optional] 
**Members** | Pointer to [**[]TeamMember**](TeamMember.md) | List of team members with their roles | [optional] 
**ResponsibleParties** | Pointer to [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] 
**RelatedTeams** | Pointer to [**[]RelatedTeam**](RelatedTeam.md) | Relationships to other teams | [optional] 
**Uri** | Pointer to **string** | URL or reference to internal team page | [optional] 
**EmailAddress** | Pointer to **string** | Team email address | [optional] 
**Status** | Pointer to **string** | Team status (lifecycle, archival, deprecation, etc.) | [optional] 

## Methods

### NewTeamBase

`func NewTeamBase(name string, ) *TeamBase`

NewTeamBase instantiates a new TeamBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamBaseWithDefaults

`func NewTeamBaseWithDefaults() *TeamBase`

NewTeamBaseWithDefaults instantiates a new TeamBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *TeamBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TeamBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TeamBase) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *TeamBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TeamBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TeamBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TeamBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetMembers

`func (o *TeamBase) GetMembers() []TeamMember`

GetMembers returns the Members field if non-nil, zero value otherwise.

### GetMembersOk

`func (o *TeamBase) GetMembersOk() (*[]TeamMember, bool)`

GetMembersOk returns a tuple with the Members field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembers

`func (o *TeamBase) SetMembers(v []TeamMember)`

SetMembers sets Members field to given value.

### HasMembers

`func (o *TeamBase) HasMembers() bool`

HasMembers returns a boolean if a field has been set.

### GetResponsibleParties

`func (o *TeamBase) GetResponsibleParties() []ResponsibleParty`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *TeamBase) GetResponsiblePartiesOk() (*[]ResponsibleParty, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *TeamBase) SetResponsibleParties(v []ResponsibleParty)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *TeamBase) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.

### GetRelatedTeams

`func (o *TeamBase) GetRelatedTeams() []RelatedTeam`

GetRelatedTeams returns the RelatedTeams field if non-nil, zero value otherwise.

### GetRelatedTeamsOk

`func (o *TeamBase) GetRelatedTeamsOk() (*[]RelatedTeam, bool)`

GetRelatedTeamsOk returns a tuple with the RelatedTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedTeams

`func (o *TeamBase) SetRelatedTeams(v []RelatedTeam)`

SetRelatedTeams sets RelatedTeams field to given value.

### HasRelatedTeams

`func (o *TeamBase) HasRelatedTeams() bool`

HasRelatedTeams returns a boolean if a field has been set.

### GetUri

`func (o *TeamBase) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *TeamBase) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *TeamBase) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *TeamBase) HasUri() bool`

HasUri returns a boolean if a field has been set.

### GetEmailAddress

`func (o *TeamBase) GetEmailAddress() string`

GetEmailAddress returns the EmailAddress field if non-nil, zero value otherwise.

### GetEmailAddressOk

`func (o *TeamBase) GetEmailAddressOk() (*string, bool)`

GetEmailAddressOk returns a tuple with the EmailAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailAddress

`func (o *TeamBase) SetEmailAddress(v string)`

SetEmailAddress sets EmailAddress field to given value.

### HasEmailAddress

`func (o *TeamBase) HasEmailAddress() bool`

HasEmailAddress returns a boolean if a field has been set.

### GetStatus

`func (o *TeamBase) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TeamBase) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TeamBase) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *TeamBase) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


