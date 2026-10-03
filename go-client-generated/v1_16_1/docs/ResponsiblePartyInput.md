# ResponsiblePartyInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserId** | **string** | UUID of the responsible party user | 
**Role** | Pointer to [**TeamMemberRole**](TeamMemberRole.md) |  | [optional] 
**CustomRole** | Pointer to **string** | Custom role description when role is &#39;other&#39; | [optional] 

## Methods

### NewResponsiblePartyInput

`func NewResponsiblePartyInput(userId string, ) *ResponsiblePartyInput`

NewResponsiblePartyInput instantiates a new ResponsiblePartyInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewResponsiblePartyInputWithDefaults

`func NewResponsiblePartyInputWithDefaults() *ResponsiblePartyInput`

NewResponsiblePartyInputWithDefaults instantiates a new ResponsiblePartyInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserId

`func (o *ResponsiblePartyInput) GetUserId() string`

GetUserId returns the UserId field if non-nil, zero value otherwise.

### GetUserIdOk

`func (o *ResponsiblePartyInput) GetUserIdOk() (*string, bool)`

GetUserIdOk returns a tuple with the UserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserId

`func (o *ResponsiblePartyInput) SetUserId(v string)`

SetUserId sets UserId field to given value.


### GetRole

`func (o *ResponsiblePartyInput) GetRole() TeamMemberRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *ResponsiblePartyInput) GetRoleOk() (*TeamMemberRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *ResponsiblePartyInput) SetRole(v TeamMemberRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *ResponsiblePartyInput) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetCustomRole

`func (o *ResponsiblePartyInput) GetCustomRole() string`

GetCustomRole returns the CustomRole field if non-nil, zero value otherwise.

### GetCustomRoleOk

`func (o *ResponsiblePartyInput) GetCustomRoleOk() (*string, bool)`

GetCustomRoleOk returns a tuple with the CustomRole field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCustomRole

`func (o *ResponsiblePartyInput) SetCustomRole(v string)`

SetCustomRole sets CustomRole field to given value.

### HasCustomRole

`func (o *ResponsiblePartyInput) HasCustomRole() bool`

HasCustomRole returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


