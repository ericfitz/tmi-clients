# ListAdminAuditEntriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Entries** | [**[]AuditEntry**](AuditEntry.md) |  | 
**Total** | **int32** | Total entries matching the filter. | 
**Limit** | **int32** | Page size used. | 
**NextCursor** | Pointer to **NullableString** | Cursor for the next page; absent or null when exhausted. | [optional] 
**PrevCursor** | Pointer to **NullableString** | Cursor for the previous (newer) page; absent or null when at the newest end. | [optional] 

## Methods

### NewListAdminAuditEntriesResponse

`func NewListAdminAuditEntriesResponse(entries []AuditEntry, total int32, limit int32, ) *ListAdminAuditEntriesResponse`

NewListAdminAuditEntriesResponse instantiates a new ListAdminAuditEntriesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListAdminAuditEntriesResponseWithDefaults

`func NewListAdminAuditEntriesResponseWithDefaults() *ListAdminAuditEntriesResponse`

NewListAdminAuditEntriesResponseWithDefaults instantiates a new ListAdminAuditEntriesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEntries

`func (o *ListAdminAuditEntriesResponse) GetEntries() []AuditEntry`

GetEntries returns the Entries field if non-nil, zero value otherwise.

### GetEntriesOk

`func (o *ListAdminAuditEntriesResponse) GetEntriesOk() (*[]AuditEntry, bool)`

GetEntriesOk returns a tuple with the Entries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEntries

`func (o *ListAdminAuditEntriesResponse) SetEntries(v []AuditEntry)`

SetEntries sets Entries field to given value.


### GetTotal

`func (o *ListAdminAuditEntriesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListAdminAuditEntriesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListAdminAuditEntriesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListAdminAuditEntriesResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListAdminAuditEntriesResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListAdminAuditEntriesResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetNextCursor

`func (o *ListAdminAuditEntriesResponse) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ListAdminAuditEntriesResponse) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ListAdminAuditEntriesResponse) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *ListAdminAuditEntriesResponse) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *ListAdminAuditEntriesResponse) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ListAdminAuditEntriesResponse) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil
### GetPrevCursor

`func (o *ListAdminAuditEntriesResponse) GetPrevCursor() string`

GetPrevCursor returns the PrevCursor field if non-nil, zero value otherwise.

### GetPrevCursorOk

`func (o *ListAdminAuditEntriesResponse) GetPrevCursorOk() (*string, bool)`

GetPrevCursorOk returns a tuple with the PrevCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrevCursor

`func (o *ListAdminAuditEntriesResponse) SetPrevCursor(v string)`

SetPrevCursor sets PrevCursor field to given value.

### HasPrevCursor

`func (o *ListAdminAuditEntriesResponse) HasPrevCursor() bool`

HasPrevCursor returns a boolean if a field has been set.

### SetPrevCursorNil

`func (o *ListAdminAuditEntriesResponse) SetPrevCursorNil(b bool)`

 SetPrevCursorNil sets the value for PrevCursor to be an explicit nil

### UnsetPrevCursor
`func (o *ListAdminAuditEntriesResponse) UnsetPrevCursor()`

UnsetPrevCursor ensures that no value is present for PrevCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


