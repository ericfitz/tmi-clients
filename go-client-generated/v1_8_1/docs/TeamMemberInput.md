# TeamMemberInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **string** | UUID of the team member user | 
**Role** | Pointer to [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**CustomRole** | Pointer to **string** | Custom role description when role is &#39;other&#39; | [optional] 

## Methods

### NewTeamMemberInput

`func NewTeamMemberInput(userId string, ) *TeamMemberInput`

NewTeamMemberInput instantiates a new TeamMemberInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamMemberInputWithDefaults

`func NewTeamMemberInputWithDefaults() *TeamMemberInput`

NewTeamMemberInputWithDefaults instantiates a new TeamMemberInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *TeamMemberInput) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *TeamMemberInput) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *TeamMemberInput) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetRole

`func (o *TeamMemberInput) GetRole() TeamMemberRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *TeamMemberInput) GetRoleOk() (*TeamMemberRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *TeamMemberInput) SetRole(v TeamMemberRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *TeamMemberInput) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetCustomRole

`func (o *TeamMemberInput) GetCustomRole() string`

GetCustomRole returns the CustomRole field if non-nil, zero value otherwise.

### GetCustomRoleOk

`func (o *TeamMemberInput) GetCustomRoleOk() (*string, bool)`

GetCustomRoleOk returns a tuple with the CustomRole field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomRole

`func (o *TeamMemberInput) SetCustomRole(v string)`

SetCustomRole sets CustomRole field to given value.

### HasCustomRole

`func (o *TeamMemberInput) HasCustomRole() bool`

HasCustomRole returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


