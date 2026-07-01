# TeamMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **string** | UUID of the team member user | 
**User** | Pointer to [**NullableUser**](User.md) | Resolved user details (read-only, populated by server) | [optional] [readonly] 
**Role** | Pointer to [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**CustomRole** | Pointer to **string** | Custom role description when role is &#39;other&#39; | [optional] 

## Methods

### NewTeamMember

`func NewTeamMember(userId string, ) *TeamMember`

NewTeamMember instantiates a new TeamMember object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTeamMemberWithDefaults

`func NewTeamMemberWithDefaults() *TeamMember`

NewTeamMemberWithDefaults instantiates a new TeamMember object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *TeamMember) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *TeamMember) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *TeamMember) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetUser

`func (o *TeamMember) GetUser() User`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *TeamMember) GetUserOk() (*User, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *TeamMember) SetUser(v User)`

SetUser sets User field to given value.

### HasUser

`func (o *TeamMember) HasUser() bool`

HasUser returns a boolean if a field has been set.

### SetUserNil

`func (o *TeamMember) SetUserNil(b bool)`

 SetUserNil sets the value for User to be an explicit nil

### UnsetUser
`func (o *TeamMember) UnsetUser()`

UnsetUser ensures that no value is present for User, not even an explicit nil
### GetRole

`func (o *TeamMember) GetRole() TeamMemberRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *TeamMember) GetRoleOk() (*TeamMemberRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *TeamMember) SetRole(v TeamMemberRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *TeamMember) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetCustomRole

`func (o *TeamMember) GetCustomRole() string`

GetCustomRole returns the CustomRole field if non-nil, zero value otherwise.

### GetCustomRoleOk

`func (o *TeamMember) GetCustomRoleOk() (*string, bool)`

GetCustomRoleOk returns a tuple with the CustomRole field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomRole

`func (o *TeamMember) SetCustomRole(v string)`

SetCustomRole sets CustomRole field to given value.

### HasCustomRole

`func (o *TeamMember) HasCustomRole() bool`

HasCustomRole returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


