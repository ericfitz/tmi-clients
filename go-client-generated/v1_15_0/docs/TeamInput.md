# TeamInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Team name | 
**Description** | Pointer to **NullableString** | Team description | [optional] 
**RelatedTeams** | Pointer to [**[]RelatedTeam**](RelatedTeam.md) | Relationships to other teams | [optional] 
**Uri** | Pointer to **NullableString** | URL or reference to internal team page | [optional] 
**EmailAddress** | Pointer to **NullableString** | Team email address | [optional] 
**Status** | Pointer to [**NullableTeamStatus**](TeamStatus.md) | Team lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**Members** | Pointer to [**[]TeamMemberInput**](TeamMemberInput.md) | List of team members with their roles | [optional] 
**ResponsibleParties** | Pointer to [**[]ResponsiblePartyInput**](ResponsiblePartyInput.md) | Responsible parties for this team (in lieu of owner) | [optional] 

## Methods

### NewTeamInput

`func NewTeamInput(name string, ) *TeamInput`

NewTeamInput instantiates a new TeamInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamInputWithDefaults

`func NewTeamInputWithDefaults() *TeamInput`

NewTeamInputWithDefaults instantiates a new TeamInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *TeamInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *TeamInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *TeamInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *TeamInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *TeamInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *TeamInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *TeamInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *TeamInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *TeamInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetRelatedTeams

`func (o *TeamInput) GetRelatedTeams() []RelatedTeam`

GetRelatedTeams returns the RelatedTeams field if non-nil, zero value otherwise.

### GetRelatedTeamsOk

`func (o *TeamInput) GetRelatedTeamsOk() (*[]RelatedTeam, bool)`

GetRelatedTeamsOk returns a tuple with the RelatedTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedTeams

`func (o *TeamInput) SetRelatedTeams(v []RelatedTeam)`

SetRelatedTeams sets RelatedTeams field to given value.

### HasRelatedTeams

`func (o *TeamInput) HasRelatedTeams() bool`

HasRelatedTeams returns a boolean if a field has been set.

### GetUri

`func (o *TeamInput) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *TeamInput) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *TeamInput) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *TeamInput) HasUri() bool`

HasUri returns a boolean if a field has been set.

### SetUriNil

`func (o *TeamInput) SetUriNil(b bool)`

 SetUriNil sets the value for Uri to be an explicit nil

### UnsetUri
`func (o *TeamInput) UnsetUri()`

UnsetUri ensures that no value is present for Uri, not even an explicit nil
### GetEmailAddress

`func (o *TeamInput) GetEmailAddress() string`

GetEmailAddress returns the EmailAddress field if non-nil, zero value otherwise.

### GetEmailAddressOk

`func (o *TeamInput) GetEmailAddressOk() (*string, bool)`

GetEmailAddressOk returns a tuple with the EmailAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailAddress

`func (o *TeamInput) SetEmailAddress(v string)`

SetEmailAddress sets EmailAddress field to given value.

### HasEmailAddress

`func (o *TeamInput) HasEmailAddress() bool`

HasEmailAddress returns a boolean if a field has been set.

### SetEmailAddressNil

`func (o *TeamInput) SetEmailAddressNil(b bool)`

 SetEmailAddressNil sets the value for EmailAddress to be an explicit nil

### UnsetEmailAddress
`func (o *TeamInput) UnsetEmailAddress()`

UnsetEmailAddress ensures that no value is present for EmailAddress, not even an explicit nil
### GetStatus

`func (o *TeamInput) GetStatus() TeamStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *TeamInput) GetStatusOk() (*TeamStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *TeamInput) SetStatus(v TeamStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *TeamInput) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *TeamInput) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *TeamInput) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetMembers

`func (o *TeamInput) GetMembers() []TeamMemberInput`

GetMembers returns the Members field if non-nil, zero value otherwise.

### GetMembersOk

`func (o *TeamInput) GetMembersOk() (*[]TeamMemberInput, bool)`

GetMembersOk returns a tuple with the Members field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembers

`func (o *TeamInput) SetMembers(v []TeamMemberInput)`

SetMembers sets Members field to given value.

### HasMembers

`func (o *TeamInput) HasMembers() bool`

HasMembers returns a boolean if a field has been set.

### GetResponsibleParties

`func (o *TeamInput) GetResponsibleParties() []ResponsiblePartyInput`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *TeamInput) GetResponsiblePartiesOk() (*[]ResponsiblePartyInput, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *TeamInput) SetResponsibleParties(v []ResponsiblePartyInput)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *TeamInput) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


