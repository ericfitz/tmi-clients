# Team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Team name | 
**Description** | Pointer to **NullableString** | Team description | [optional] 
**Members** | Pointer to [**[]TeamMember**](TeamMember.md) | List of team members with their roles | [optional] 
**ResponsibleParties** | Pointer to [**[]ResponsibleParty**](ResponsibleParty.md) | Responsible parties for this team (in lieu of owner) | [optional] 
**RelatedTeams** | Pointer to [**[]RelatedTeam**](RelatedTeam.md) | Relationships to other teams | [optional] 
**Uri** | Pointer to **NullableString** | URL or reference to internal team page | [optional] 
**EmailAddress** | Pointer to **NullableString** | Team email address | [optional] 
**Status** | Pointer to [**NullableTeamStatus**](TeamStatus.md) | Team lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**Id** | Pointer to **string** | Unique identifier for the team (UUID) | [optional] [readonly] 
**CreatedBy** | Pointer to **map[string]interface{}** | User who created the team | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedBy** | Pointer to **map[string]interface{}** | User who last modified the team | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**ReviewedBy** | Pointer to **map[string]interface{}** | User who last reviewed the team | [optional] 
**ReviewedAt** | Pointer to **NullableTime** | Last review timestamp (RFC3339) | [optional] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] 

## Methods

### NewTeam

`func NewTeam(name string, ) *Team`

NewTeam instantiates a new Team object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamWithDefaults

`func NewTeamWithDefaults() *Team`

NewTeamWithDefaults instantiates a new Team object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Team) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Team) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Team) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Team) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Team) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Team) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Team) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Team) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Team) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetMembers

`func (o *Team) GetMembers() []TeamMember`

GetMembers returns the Members field if non-nil, zero value otherwise.

### GetMembersOk

`func (o *Team) GetMembersOk() (*[]TeamMember, bool)`

GetMembersOk returns a tuple with the Members field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembers

`func (o *Team) SetMembers(v []TeamMember)`

SetMembers sets Members field to given value.

### HasMembers

`func (o *Team) HasMembers() bool`

HasMembers returns a boolean if a field has been set.

### GetResponsibleParties

`func (o *Team) GetResponsibleParties() []ResponsibleParty`

GetResponsibleParties returns the ResponsibleParties field if non-nil, zero value otherwise.

### GetResponsiblePartiesOk

`func (o *Team) GetResponsiblePartiesOk() (*[]ResponsibleParty, bool)`

GetResponsiblePartiesOk returns a tuple with the ResponsibleParties field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponsibleParties

`func (o *Team) SetResponsibleParties(v []ResponsibleParty)`

SetResponsibleParties sets ResponsibleParties field to given value.

### HasResponsibleParties

`func (o *Team) HasResponsibleParties() bool`

HasResponsibleParties returns a boolean if a field has been set.

### GetRelatedTeams

`func (o *Team) GetRelatedTeams() []RelatedTeam`

GetRelatedTeams returns the RelatedTeams field if non-nil, zero value otherwise.

### GetRelatedTeamsOk

`func (o *Team) GetRelatedTeamsOk() (*[]RelatedTeam, bool)`

GetRelatedTeamsOk returns a tuple with the RelatedTeams field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRelatedTeams

`func (o *Team) SetRelatedTeams(v []RelatedTeam)`

SetRelatedTeams sets RelatedTeams field to given value.

### HasRelatedTeams

`func (o *Team) HasRelatedTeams() bool`

HasRelatedTeams returns a boolean if a field has been set.

### GetUri

`func (o *Team) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *Team) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *Team) SetUri(v string)`

SetUri sets Uri field to given value.

### HasUri

`func (o *Team) HasUri() bool`

HasUri returns a boolean if a field has been set.

### SetUriNil

`func (o *Team) SetUriNil(b bool)`

 SetUriNil sets the value for Uri to be an explicit nil

### UnsetUri
`func (o *Team) UnsetUri()`

UnsetUri ensures that no value is present for Uri, not even an explicit nil
### GetEmailAddress

`func (o *Team) GetEmailAddress() string`

GetEmailAddress returns the EmailAddress field if non-nil, zero value otherwise.

### GetEmailAddressOk

`func (o *Team) GetEmailAddressOk() (*string, bool)`

GetEmailAddressOk returns a tuple with the EmailAddress field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmailAddress

`func (o *Team) SetEmailAddress(v string)`

SetEmailAddress sets EmailAddress field to given value.

### HasEmailAddress

`func (o *Team) HasEmailAddress() bool`

HasEmailAddress returns a boolean if a field has been set.

### SetEmailAddressNil

`func (o *Team) SetEmailAddressNil(b bool)`

 SetEmailAddressNil sets the value for EmailAddress to be an explicit nil

### UnsetEmailAddress
`func (o *Team) UnsetEmailAddress()`

UnsetEmailAddress ensures that no value is present for EmailAddress, not even an explicit nil
### GetStatus

`func (o *Team) GetStatus() TeamStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *Team) GetStatusOk() (*TeamStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *Team) SetStatus(v TeamStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *Team) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *Team) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *Team) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetId

`func (o *Team) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Team) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Team) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Team) HasId() bool`

HasId returns a boolean if a field has been set.

### GetCreatedBy

`func (o *Team) GetCreatedBy() map[string]interface{}`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *Team) GetCreatedByOk() (*map[string]interface{}, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *Team) SetCreatedBy(v map[string]interface{})`

SetCreatedBy sets CreatedBy field to given value.

### HasCreatedBy

`func (o *Team) HasCreatedBy() bool`

HasCreatedBy returns a boolean if a field has been set.

### SetCreatedByNil

`func (o *Team) SetCreatedByNil(b bool)`

 SetCreatedByNil sets the value for CreatedBy to be an explicit nil

### UnsetCreatedBy
`func (o *Team) UnsetCreatedBy()`

UnsetCreatedBy ensures that no value is present for CreatedBy, not even an explicit nil
### GetCreatedAt

`func (o *Team) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Team) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Team) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Team) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedBy

`func (o *Team) GetModifiedBy() map[string]interface{}`

GetModifiedBy returns the ModifiedBy field if non-nil, zero value otherwise.

### GetModifiedByOk

`func (o *Team) GetModifiedByOk() (*map[string]interface{}, bool)`

GetModifiedByOk returns a tuple with the ModifiedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedBy

`func (o *Team) SetModifiedBy(v map[string]interface{})`

SetModifiedBy sets ModifiedBy field to given value.

### HasModifiedBy

`func (o *Team) HasModifiedBy() bool`

HasModifiedBy returns a boolean if a field has been set.

### SetModifiedByNil

`func (o *Team) SetModifiedByNil(b bool)`

 SetModifiedByNil sets the value for ModifiedBy to be an explicit nil

### UnsetModifiedBy
`func (o *Team) UnsetModifiedBy()`

UnsetModifiedBy ensures that no value is present for ModifiedBy, not even an explicit nil
### GetModifiedAt

`func (o *Team) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *Team) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *Team) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *Team) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetReviewedBy

`func (o *Team) GetReviewedBy() map[string]interface{}`

GetReviewedBy returns the ReviewedBy field if non-nil, zero value otherwise.

### GetReviewedByOk

`func (o *Team) GetReviewedByOk() (*map[string]interface{}, bool)`

GetReviewedByOk returns a tuple with the ReviewedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedBy

`func (o *Team) SetReviewedBy(v map[string]interface{})`

SetReviewedBy sets ReviewedBy field to given value.

### HasReviewedBy

`func (o *Team) HasReviewedBy() bool`

HasReviewedBy returns a boolean if a field has been set.

### SetReviewedByNil

`func (o *Team) SetReviewedByNil(b bool)`

 SetReviewedByNil sets the value for ReviewedBy to be an explicit nil

### UnsetReviewedBy
`func (o *Team) UnsetReviewedBy()`

UnsetReviewedBy ensures that no value is present for ReviewedBy, not even an explicit nil
### GetReviewedAt

`func (o *Team) GetReviewedAt() time.Time`

GetReviewedAt returns the ReviewedAt field if non-nil, zero value otherwise.

### GetReviewedAtOk

`func (o *Team) GetReviewedAtOk() (*time.Time, bool)`

GetReviewedAtOk returns a tuple with the ReviewedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReviewedAt

`func (o *Team) SetReviewedAt(v time.Time)`

SetReviewedAt sets ReviewedAt field to given value.

### HasReviewedAt

`func (o *Team) HasReviewedAt() bool`

HasReviewedAt returns a boolean if a field has been set.

### SetReviewedAtNil

`func (o *Team) SetReviewedAtNil(b bool)`

 SetReviewedAtNil sets the value for ReviewedAt to be an explicit nil

### UnsetReviewedAt
`func (o *Team) UnsetReviewedAt()`

UnsetReviewedAt ensures that no value is present for ReviewedAt, not even an explicit nil
### GetMetadata

`func (o *Team) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Team) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Team) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Team) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *Team) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *Team) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


