# GroupMember

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the membership record | 
**GroupInternalUuid** | **string** | Internal UUID of the group | 
**UserInternalUuid** | Pointer to **NullableString** | Internal UUID of the user | [optional] 
**UserEmail** | Pointer to **NullableString** | Email address of the user | [optional] 
**UserName** | Pointer to **NullableString** | Display name of the user | [optional] 
**UserProvider** | Pointer to **NullableString** | OAuth/SAML provider for the user | [optional] 
**UserProviderUserId** | Pointer to **NullableString** | Provider-specific user identifier | [optional] 
**AddedByInternalUuid** | Pointer to **NullableString** | Internal UUID of the administrator who added this member | [optional] 
**AddedByEmail** | Pointer to **NullableString** | Email of the administrator who added this member | [optional] 
**AddedAt** | **time.Time** | Timestamp when the user was added to the group (RFC3339) | 
**Notes** | Pointer to **NullableString** | Optional notes about this membership | [optional] 
**SubjectType** | **string** | Type of member: user (direct user membership) or group (group-in-group membership) | [default to "user"]
**MemberGroupInternalUuid** | Pointer to **NullableString** | Internal UUID of the member group (when subject_type is group) | [optional] 
**MemberGroupName** | Pointer to **NullableString** | Display name of the member group (when subject_type is group) | [optional] 

## Methods

### NewGroupMember

`func NewGroupMember(id string, groupInternalUuid string, addedAt time.Time, subjectType string, ) *GroupMember`

NewGroupMember instantiates a new GroupMember object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGroupMemberWithDefaults

`func NewGroupMemberWithDefaults() *GroupMember`

NewGroupMemberWithDefaults instantiates a new GroupMember object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *GroupMember) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *GroupMember) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *GroupMember) SetId(v string)`

SetId sets Id field to given value.


### GetGroupInternalUuid

`func (o *GroupMember) GetGroupInternalUuid() string`

GetGroupInternalUuid returns the GroupInternalUuid field if non-nil, zero value otherwise.

### GetGroupInternalUuidOk

`func (o *GroupMember) GetGroupInternalUuidOk() (*string, bool)`

GetGroupInternalUuidOk returns a tuple with the GroupInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupInternalUuid

`func (o *GroupMember) SetGroupInternalUuid(v string)`

SetGroupInternalUuid sets GroupInternalUuid field to given value.


### GetUserInternalUuid

`func (o *GroupMember) GetUserInternalUuid() string`

GetUserInternalUuid returns the UserInternalUuid field if non-nil, zero value otherwise.

### GetUserInternalUuidOk

`func (o *GroupMember) GetUserInternalUuidOk() (*string, bool)`

GetUserInternalUuidOk returns a tuple with the UserInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserInternalUuid

`func (o *GroupMember) SetUserInternalUuid(v string)`

SetUserInternalUuid sets UserInternalUuid field to given value.

### HasUserInternalUuid

`func (o *GroupMember) HasUserInternalUuid() bool`

HasUserInternalUuid returns a boolean if a field has been set.

### SetUserInternalUuidNil

`func (o *GroupMember) SetUserInternalUuidNil(b bool)`

 SetUserInternalUuidNil sets the value for UserInternalUuid to be an explicit nil

### UnsetUserInternalUuid
`func (o *GroupMember) UnsetUserInternalUuid()`

UnsetUserInternalUuid ensures that no value is present for UserInternalUuid, not even an explicit nil
### GetUserEmail

`func (o *GroupMember) GetUserEmail() string`

GetUserEmail returns the UserEmail field if non-nil, zero value otherwise.

### GetUserEmailOk

`func (o *GroupMember) GetUserEmailOk() (*string, bool)`

GetUserEmailOk returns a tuple with the UserEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserEmail

`func (o *GroupMember) SetUserEmail(v string)`

SetUserEmail sets UserEmail field to given value.

### HasUserEmail

`func (o *GroupMember) HasUserEmail() bool`

HasUserEmail returns a boolean if a field has been set.

### SetUserEmailNil

`func (o *GroupMember) SetUserEmailNil(b bool)`

 SetUserEmailNil sets the value for UserEmail to be an explicit nil

### UnsetUserEmail
`func (o *GroupMember) UnsetUserEmail()`

UnsetUserEmail ensures that no value is present for UserEmail, not even an explicit nil
### GetUserName

`func (o *GroupMember) GetUserName() string`

GetUserName returns the UserName field if non-nil, zero value otherwise.

### GetUserNameOk

`func (o *GroupMember) GetUserNameOk() (*string, bool)`

GetUserNameOk returns a tuple with the UserName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserName

`func (o *GroupMember) SetUserName(v string)`

SetUserName sets UserName field to given value.

### HasUserName

`func (o *GroupMember) HasUserName() bool`

HasUserName returns a boolean if a field has been set.

### SetUserNameNil

`func (o *GroupMember) SetUserNameNil(b bool)`

 SetUserNameNil sets the value for UserName to be an explicit nil

### UnsetUserName
`func (o *GroupMember) UnsetUserName()`

UnsetUserName ensures that no value is present for UserName, not even an explicit nil
### GetUserProvider

`func (o *GroupMember) GetUserProvider() string`

GetUserProvider returns the UserProvider field if non-nil, zero value otherwise.

### GetUserProviderOk

`func (o *GroupMember) GetUserProviderOk() (*string, bool)`

GetUserProviderOk returns a tuple with the UserProvider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserProvider

`func (o *GroupMember) SetUserProvider(v string)`

SetUserProvider sets UserProvider field to given value.

### HasUserProvider

`func (o *GroupMember) HasUserProvider() bool`

HasUserProvider returns a boolean if a field has been set.

### SetUserProviderNil

`func (o *GroupMember) SetUserProviderNil(b bool)`

 SetUserProviderNil sets the value for UserProvider to be an explicit nil

### UnsetUserProvider
`func (o *GroupMember) UnsetUserProvider()`

UnsetUserProvider ensures that no value is present for UserProvider, not even an explicit nil
### GetUserProviderUserId

`func (o *GroupMember) GetUserProviderUserId() string`

GetUserProviderUserId returns the UserProviderUserId field if non-nil, zero value otherwise.

### GetUserProviderUserIdOk

`func (o *GroupMember) GetUserProviderUserIdOk() (*string, bool)`

GetUserProviderUserIdOk returns a tuple with the UserProviderUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserProviderUserId

`func (o *GroupMember) SetUserProviderUserId(v string)`

SetUserProviderUserId sets UserProviderUserId field to given value.

### HasUserProviderUserId

`func (o *GroupMember) HasUserProviderUserId() bool`

HasUserProviderUserId returns a boolean if a field has been set.

### SetUserProviderUserIdNil

`func (o *GroupMember) SetUserProviderUserIdNil(b bool)`

 SetUserProviderUserIdNil sets the value for UserProviderUserId to be an explicit nil

### UnsetUserProviderUserId
`func (o *GroupMember) UnsetUserProviderUserId()`

UnsetUserProviderUserId ensures that no value is present for UserProviderUserId, not even an explicit nil
### GetAddedByInternalUuid

`func (o *GroupMember) GetAddedByInternalUuid() string`

GetAddedByInternalUuid returns the AddedByInternalUuid field if non-nil, zero value otherwise.

### GetAddedByInternalUuidOk

`func (o *GroupMember) GetAddedByInternalUuidOk() (*string, bool)`

GetAddedByInternalUuidOk returns a tuple with the AddedByInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddedByInternalUuid

`func (o *GroupMember) SetAddedByInternalUuid(v string)`

SetAddedByInternalUuid sets AddedByInternalUuid field to given value.

### HasAddedByInternalUuid

`func (o *GroupMember) HasAddedByInternalUuid() bool`

HasAddedByInternalUuid returns a boolean if a field has been set.

### SetAddedByInternalUuidNil

`func (o *GroupMember) SetAddedByInternalUuidNil(b bool)`

 SetAddedByInternalUuidNil sets the value for AddedByInternalUuid to be an explicit nil

### UnsetAddedByInternalUuid
`func (o *GroupMember) UnsetAddedByInternalUuid()`

UnsetAddedByInternalUuid ensures that no value is present for AddedByInternalUuid, not even an explicit nil
### GetAddedByEmail

`func (o *GroupMember) GetAddedByEmail() string`

GetAddedByEmail returns the AddedByEmail field if non-nil, zero value otherwise.

### GetAddedByEmailOk

`func (o *GroupMember) GetAddedByEmailOk() (*string, bool)`

GetAddedByEmailOk returns a tuple with the AddedByEmail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddedByEmail

`func (o *GroupMember) SetAddedByEmail(v string)`

SetAddedByEmail sets AddedByEmail field to given value.

### HasAddedByEmail

`func (o *GroupMember) HasAddedByEmail() bool`

HasAddedByEmail returns a boolean if a field has been set.

### SetAddedByEmailNil

`func (o *GroupMember) SetAddedByEmailNil(b bool)`

 SetAddedByEmailNil sets the value for AddedByEmail to be an explicit nil

### UnsetAddedByEmail
`func (o *GroupMember) UnsetAddedByEmail()`

UnsetAddedByEmail ensures that no value is present for AddedByEmail, not even an explicit nil
### GetAddedAt

`func (o *GroupMember) GetAddedAt() time.Time`

GetAddedAt returns the AddedAt field if non-nil, zero value otherwise.

### GetAddedAtOk

`func (o *GroupMember) GetAddedAtOk() (*time.Time, bool)`

GetAddedAtOk returns a tuple with the AddedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddedAt

`func (o *GroupMember) SetAddedAt(v time.Time)`

SetAddedAt sets AddedAt field to given value.


### GetNotes

`func (o *GroupMember) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *GroupMember) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *GroupMember) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *GroupMember) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### SetNotesNil

`func (o *GroupMember) SetNotesNil(b bool)`

 SetNotesNil sets the value for Notes to be an explicit nil

### UnsetNotes
`func (o *GroupMember) UnsetNotes()`

UnsetNotes ensures that no value is present for Notes, not even an explicit nil
### GetSubjectType

`func (o *GroupMember) GetSubjectType() string`

GetSubjectType returns the SubjectType field if non-nil, zero value otherwise.

### GetSubjectTypeOk

`func (o *GroupMember) GetSubjectTypeOk() (*string, bool)`

GetSubjectTypeOk returns a tuple with the SubjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectType

`func (o *GroupMember) SetSubjectType(v string)`

SetSubjectType sets SubjectType field to given value.


### GetMemberGroupInternalUuid

`func (o *GroupMember) GetMemberGroupInternalUuid() string`

GetMemberGroupInternalUuid returns the MemberGroupInternalUuid field if non-nil, zero value otherwise.

### GetMemberGroupInternalUuidOk

`func (o *GroupMember) GetMemberGroupInternalUuidOk() (*string, bool)`

GetMemberGroupInternalUuidOk returns a tuple with the MemberGroupInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemberGroupInternalUuid

`func (o *GroupMember) SetMemberGroupInternalUuid(v string)`

SetMemberGroupInternalUuid sets MemberGroupInternalUuid field to given value.

### HasMemberGroupInternalUuid

`func (o *GroupMember) HasMemberGroupInternalUuid() bool`

HasMemberGroupInternalUuid returns a boolean if a field has been set.

### SetMemberGroupInternalUuidNil

`func (o *GroupMember) SetMemberGroupInternalUuidNil(b bool)`

 SetMemberGroupInternalUuidNil sets the value for MemberGroupInternalUuid to be an explicit nil

### UnsetMemberGroupInternalUuid
`func (o *GroupMember) UnsetMemberGroupInternalUuid()`

UnsetMemberGroupInternalUuid ensures that no value is present for MemberGroupInternalUuid, not even an explicit nil
### GetMemberGroupName

`func (o *GroupMember) GetMemberGroupName() string`

GetMemberGroupName returns the MemberGroupName field if non-nil, zero value otherwise.

### GetMemberGroupNameOk

`func (o *GroupMember) GetMemberGroupNameOk() (*string, bool)`

GetMemberGroupNameOk returns a tuple with the MemberGroupName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemberGroupName

`func (o *GroupMember) SetMemberGroupName(v string)`

SetMemberGroupName sets MemberGroupName field to given value.

### HasMemberGroupName

`func (o *GroupMember) HasMemberGroupName() bool`

HasMemberGroupName returns a boolean if a field has been set.

### SetMemberGroupNameNil

`func (o *GroupMember) SetMemberGroupNameNil(b bool)`

 SetMemberGroupNameNil sets the value for MemberGroupName to be an explicit nil

### UnsetMemberGroupName
`func (o *GroupMember) UnsetMemberGroupName()`

UnsetMemberGroupName ensures that no value is present for MemberGroupName, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


