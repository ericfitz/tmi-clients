# ListTimmySessionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sessions** | [**[]TimmyChatSession**](TimmyChatSession.md) |  | 
**Total** | **int32** | Total number of sessions matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListTimmySessionsResponse

`func NewListTimmySessionsResponse(sessions []TimmyChatSession, total int32, limit int32, offset int32, ) *ListTimmySessionsResponse`

NewListTimmySessionsResponse instantiates a new ListTimmySessionsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListTimmySessionsResponseWithDefaults

`func NewListTimmySessionsResponseWithDefaults() *ListTimmySessionsResponse`

NewListTimmySessionsResponseWithDefaults instantiates a new ListTimmySessionsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSessions

`func (o *ListTimmySessionsResponse) GetSessions() []TimmyChatSession`

GetSessions returns the Sessions field if non-nil, zero value otherwise.

### GetSessionsOk

`func (o *ListTimmySessionsResponse) GetSessionsOk() (*[]TimmyChatSession, bool)`

GetSessionsOk returns a tuple with the Sessions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessions

`func (o *ListTimmySessionsResponse) SetSessions(v []TimmyChatSession)`

SetSessions sets Sessions field to given value.


### GetTotal

`func (o *ListTimmySessionsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListTimmySessionsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListTimmySessionsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListTimmySessionsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListTimmySessionsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListTimmySessionsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListTimmySessionsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListTimmySessionsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListTimmySessionsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


