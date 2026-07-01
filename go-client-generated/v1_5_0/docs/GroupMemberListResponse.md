# GroupMemberListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Members** | [**[]GroupMember**](GroupMember.md) |  | 
**Total** | **int32** | Total number of members in the group | 
**Limit** | **int32** | Maximum number of results per page | 
**Offset** | **int32** | Number of results skipped | 

## Methods

### NewGroupMemberListResponse

`func NewGroupMemberListResponse(members []GroupMember, total int32, limit int32, offset int32, ) *GroupMemberListResponse`

NewGroupMemberListResponse instantiates a new GroupMemberListResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGroupMemberListResponseWithDefaults

`func NewGroupMemberListResponseWithDefaults() *GroupMemberListResponse`

NewGroupMemberListResponseWithDefaults instantiates a new GroupMemberListResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMembers

`func (o *GroupMemberListResponse) GetMembers() []GroupMember`

GetMembers returns the Members field if non-nil, zero value otherwise.

### GetMembersOk

`func (o *GroupMemberListResponse) GetMembersOk() (*[]GroupMember, bool)`

GetMembersOk returns a tuple with the Members field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMembers

`func (o *GroupMemberListResponse) SetMembers(v []GroupMember)`

SetMembers sets Members field to given value.


### GetTotal

`func (o *GroupMemberListResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *GroupMemberListResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *GroupMemberListResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *GroupMemberListResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *GroupMemberListResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *GroupMemberListResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *GroupMemberListResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *GroupMemberListResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *GroupMemberListResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


