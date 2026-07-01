# UserGroupMembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InternalUuid** | **string** | Group internal UUID | 
**GroupName** | **string** | Group name (e.g. administrators, security-reviewers) | 
**Name** | Pointer to **string** | Display name for the group | [optional] 

## Methods

### NewUserGroupMembership

`func NewUserGroupMembership(internalUuid string, groupName string, ) *UserGroupMembership`

NewUserGroupMembership instantiates a new UserGroupMembership object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUserGroupMembershipWithDefaults

`func NewUserGroupMembershipWithDefaults() *UserGroupMembership`

NewUserGroupMembershipWithDefaults instantiates a new UserGroupMembership object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInternalUuid

`func (o *UserGroupMembership) GetInternalUuid() string`

GetInternalUuid returns the InternalUuid field if non-nil, zero value otherwise.

### GetInternalUuidOk

`func (o *UserGroupMembership) GetInternalUuidOk() (*string, bool)`

GetInternalUuidOk returns a tuple with the InternalUuid field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInternalUuid

`func (o *UserGroupMembership) SetInternalUuid(v string)`

SetInternalUuid sets InternalUuid field to given value.


### GetGroupName

`func (o *UserGroupMembership) GetGroupName() string`

GetGroupName returns the GroupName field if non-nil, zero value otherwise.

### GetGroupNameOk

`func (o *UserGroupMembership) GetGroupNameOk() (*string, bool)`

GetGroupNameOk returns a tuple with the GroupName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroupName

`func (o *UserGroupMembership) SetGroupName(v string)`

SetGroupName sets GroupName field to given value.


### GetName

`func (o *UserGroupMembership) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *UserGroupMembership) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *UserGroupMembership) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *UserGroupMembership) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


