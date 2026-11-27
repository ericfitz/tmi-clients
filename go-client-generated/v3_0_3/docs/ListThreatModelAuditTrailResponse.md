# ListThreatModelAuditTrailResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuditEntries** | [**[]AuditEntry**](AuditEntry.md) |  | 
**Total** | **int32** | Total number of matching audit entries | 
**Limit** | **int32** | Maximum number of entries returned | 
**NextCursor** | Pointer to **NullableString** | Cursor for the next (older) page; absent or null when exhausted. | [optional] 
**PrevCursor** | Pointer to **NullableString** | Cursor for the previous (newer) page; absent or null when at the newest end. | [optional] 

## Methods

### NewListThreatModelAuditTrailResponse

`func NewListThreatModelAuditTrailResponse(auditEntries []AuditEntry, total int32, limit int32, ) *ListThreatModelAuditTrailResponse`

NewListThreatModelAuditTrailResponse instantiates a new ListThreatModelAuditTrailResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListThreatModelAuditTrailResponseWithDefaults

`func NewListThreatModelAuditTrailResponseWithDefaults() *ListThreatModelAuditTrailResponse`

NewListThreatModelAuditTrailResponseWithDefaults instantiates a new ListThreatModelAuditTrailResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuditEntries

`func (o *ListThreatModelAuditTrailResponse) GetAuditEntries() []AuditEntry`

GetAuditEntries returns the AuditEntries field if non-nil, zero value otherwise.

### GetAuditEntriesOk

`func (o *ListThreatModelAuditTrailResponse) GetAuditEntriesOk() (*[]AuditEntry, bool)`

GetAuditEntriesOk returns a tuple with the AuditEntries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuditEntries

`func (o *ListThreatModelAuditTrailResponse) SetAuditEntries(v []AuditEntry)`

SetAuditEntries sets AuditEntries field to given value.


### GetTotal

`func (o *ListThreatModelAuditTrailResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListThreatModelAuditTrailResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListThreatModelAuditTrailResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListThreatModelAuditTrailResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListThreatModelAuditTrailResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListThreatModelAuditTrailResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetNextCursor

`func (o *ListThreatModelAuditTrailResponse) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ListThreatModelAuditTrailResponse) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ListThreatModelAuditTrailResponse) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *ListThreatModelAuditTrailResponse) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *ListThreatModelAuditTrailResponse) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ListThreatModelAuditTrailResponse) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil
### GetPrevCursor

`func (o *ListThreatModelAuditTrailResponse) GetPrevCursor() string`

GetPrevCursor returns the PrevCursor field if non-nil, zero value otherwise.

### GetPrevCursorOk

`func (o *ListThreatModelAuditTrailResponse) GetPrevCursorOk() (*string, bool)`

GetPrevCursorOk returns a tuple with the PrevCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrevCursor

`func (o *ListThreatModelAuditTrailResponse) SetPrevCursor(v string)`

SetPrevCursor sets PrevCursor field to given value.

### HasPrevCursor

`func (o *ListThreatModelAuditTrailResponse) HasPrevCursor() bool`

HasPrevCursor returns a boolean if a field has been set.

### SetPrevCursorNil

`func (o *ListThreatModelAuditTrailResponse) SetPrevCursorNil(b bool)`

 SetPrevCursorNil sets the value for PrevCursor to be an explicit nil

### UnsetPrevCursor
`func (o *ListThreatModelAuditTrailResponse) UnsetPrevCursor()`

UnsetPrevCursor ensures that no value is present for PrevCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


