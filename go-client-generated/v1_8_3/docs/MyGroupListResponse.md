# MyGroupListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Groups** | [**[]UserGroupMembership**](UserGroupMembership.md) | List of groups the user is a direct member of | 
**Total** | **int32** | Total number of groups | 

## Methods

### NewMyGroupListResponse

`func NewMyGroupListResponse(groups []UserGroupMembership, total int32, ) *MyGroupListResponse`

NewMyGroupListResponse instantiates a new MyGroupListResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMyGroupListResponseWithDefaults

`func NewMyGroupListResponseWithDefaults() *MyGroupListResponse`

NewMyGroupListResponseWithDefaults instantiates a new MyGroupListResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGroups

`func (o *MyGroupListResponse) GetGroups() []UserGroupMembership`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *MyGroupListResponse) GetGroupsOk() (*[]UserGroupMembership, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *MyGroupListResponse) SetGroups(v []UserGroupMembership)`

SetGroups sets Groups field to given value.


### GetTotal

`func (o *MyGroupListResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *MyGroupListResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *MyGroupListResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


