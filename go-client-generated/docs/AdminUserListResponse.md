# AdminUserListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Users** | [**[]AdminUser**](AdminUser.md) | List of users | 
**Total** | **int32** | Total number of users matching the filter | 
**Limit** | **int32** | Maximum number of results returned | 
**Offset** | **int32** | Number of results skipped | 

## Methods

### NewAdminUserListResponse

`func NewAdminUserListResponse(users []AdminUser, total int32, limit int32, offset int32, ) *AdminUserListResponse`

NewAdminUserListResponse instantiates a new AdminUserListResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAdminUserListResponseWithDefaults

`func NewAdminUserListResponseWithDefaults() *AdminUserListResponse`

NewAdminUserListResponseWithDefaults instantiates a new AdminUserListResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUsers

`func (o *AdminUserListResponse) GetUsers() []AdminUser`

GetUsers returns the Users field if non-nil, zero value otherwise.

### GetUsersOk

`func (o *AdminUserListResponse) GetUsersOk() (*[]AdminUser, bool)`

GetUsersOk returns a tuple with the Users field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsers

`func (o *AdminUserListResponse) SetUsers(v []AdminUser)`

SetUsers sets Users field to given value.


### GetTotal

`func (o *AdminUserListResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *AdminUserListResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *AdminUserListResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *AdminUserListResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *AdminUserListResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *AdminUserListResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *AdminUserListResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *AdminUserListResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *AdminUserListResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


