# AdminGroupListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Groups** | [**[]AdminGroup**](AdminGroup.md) | List of groups | 
**Total** | **int32** | Total number of groups matching the filter | 
**Limit** | **int32** | Maximum number of results returned | 
**Offset** | **int32** | Number of results skipped | 

## Methods

### NewAdminGroupListResponse

`func NewAdminGroupListResponse(groups []AdminGroup, total int32, limit int32, offset int32, ) *AdminGroupListResponse`

NewAdminGroupListResponse instantiates a new AdminGroupListResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAdminGroupListResponseWithDefaults

`func NewAdminGroupListResponseWithDefaults() *AdminGroupListResponse`

NewAdminGroupListResponseWithDefaults instantiates a new AdminGroupListResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGroups

`func (o *AdminGroupListResponse) GetGroups() []AdminGroup`

GetGroups returns the Groups field if non-nil, zero value otherwise.

### GetGroupsOk

`func (o *AdminGroupListResponse) GetGroupsOk() (*[]AdminGroup, bool)`

GetGroupsOk returns a tuple with the Groups field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGroups

`func (o *AdminGroupListResponse) SetGroups(v []AdminGroup)`

SetGroups sets Groups field to given value.


### GetTotal

`func (o *AdminGroupListResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *AdminGroupListResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *AdminGroupListResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *AdminGroupListResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *AdminGroupListResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *AdminGroupListResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *AdminGroupListResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *AdminGroupListResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *AdminGroupListResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


