# AddGroupMemberRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**UserInternalUuid** | Pointer to **string** | Internal UUID of the user to add to the group | [optional] 
**Notes** | Pointer to **string** | Optional notes about this membership | [optional] 
**SubjectType** | Pointer to **string** | Type of member to add: user or group | [optional] [default to "user"]
**MemberGroupInternalUuid** | Pointer to **string** | Internal UUID of the group to add as a member (required when subject_type is group) | [optional] 

## Methods

### NewAddGroupMemberRequest

`func NewAddGroupMemberRequest() *AddGroupMemberRequest`

NewAddGroupMemberRequest instantiates a new AddGroupMemberRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddGroupMemberRequestWithDefaults

`func NewAddGroupMemberRequestWithDefaults() *AddGroupMemberRequest`

NewAddGroupMemberRequestWithDefaults instantiates a new AddGroupMemberRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUserInternalUuid

`func (o *AddGroupMemberRequest) GetUserInternalUuid() string`

GetUserInternalUuid returns the UserInternalUuid field if non-nil, zero value otherwise.

### GetUserInternalUuidOk

`func (o *AddGroupMemberRequest) GetUserInternalUuidOk() (*string, bool)`

GetUserInternalUuidOk returns a tuple with the UserInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserInternalUuid

`func (o *AddGroupMemberRequest) SetUserInternalUuid(v string)`

SetUserInternalUuid sets UserInternalUuid field to given value.

### HasUserInternalUuid

`func (o *AddGroupMemberRequest) HasUserInternalUuid() bool`

HasUserInternalUuid returns a boolean if a field has been set.

### GetNotes

`func (o *AddGroupMemberRequest) GetNotes() string`

GetNotes returns the Notes field if non-nil, zero value otherwise.

### GetNotesOk

`func (o *AddGroupMemberRequest) GetNotesOk() (*string, bool)`

GetNotesOk returns a tuple with the Notes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNotes

`func (o *AddGroupMemberRequest) SetNotes(v string)`

SetNotes sets Notes field to given value.

### HasNotes

`func (o *AddGroupMemberRequest) HasNotes() bool`

HasNotes returns a boolean if a field has been set.

### GetSubjectType

`func (o *AddGroupMemberRequest) GetSubjectType() string`

GetSubjectType returns the SubjectType field if non-nil, zero value otherwise.

### GetSubjectTypeOk

`func (o *AddGroupMemberRequest) GetSubjectTypeOk() (*string, bool)`

GetSubjectTypeOk returns a tuple with the SubjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectType

`func (o *AddGroupMemberRequest) SetSubjectType(v string)`

SetSubjectType sets SubjectType field to given value.

### HasSubjectType

`func (o *AddGroupMemberRequest) HasSubjectType() bool`

HasSubjectType returns a boolean if a field has been set.

### GetMemberGroupInternalUuid

`func (o *AddGroupMemberRequest) GetMemberGroupInternalUuid() string`

GetMemberGroupInternalUuid returns the MemberGroupInternalUuid field if non-nil, zero value otherwise.

### GetMemberGroupInternalUuidOk

`func (o *AddGroupMemberRequest) GetMemberGroupInternalUuidOk() (*string, bool)`

GetMemberGroupInternalUuidOk returns a tuple with the MemberGroupInternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemberGroupInternalUuid

`func (o *AddGroupMemberRequest) SetMemberGroupInternalUuid(v string)`

SetMemberGroupInternalUuid sets MemberGroupInternalUuid field to given value.

### HasMemberGroupInternalUuid

`func (o *AddGroupMemberRequest) HasMemberGroupInternalUuid() bool`

HasMemberGroupInternalUuid returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


