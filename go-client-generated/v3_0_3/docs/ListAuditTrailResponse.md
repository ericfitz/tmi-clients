# ListAuditTrailResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AuditEntries** | [**[]AuditEntry**](AuditEntry.md) |  | 
**Total** | **int32** | Total number of matching audit entries | 
**Limit** | **int32** | Maximum number of entries returned | 
**Offset** | **int32** | Offset from the beginning of the result set | 

## Methods

### NewListAuditTrailResponse

`func NewListAuditTrailResponse(auditEntries []AuditEntry, total int32, limit int32, offset int32, ) *ListAuditTrailResponse`

NewListAuditTrailResponse instantiates a new ListAuditTrailResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListAuditTrailResponseWithDefaults

`func NewListAuditTrailResponseWithDefaults() *ListAuditTrailResponse`

NewListAuditTrailResponseWithDefaults instantiates a new ListAuditTrailResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAuditEntries

`func (o *ListAuditTrailResponse) GetAuditEntries() []AuditEntry`

GetAuditEntries returns the AuditEntries field if non-nil, zero value otherwise.

### GetAuditEntriesOk

`func (o *ListAuditTrailResponse) GetAuditEntriesOk() (*[]AuditEntry, bool)`

GetAuditEntriesOk returns a tuple with the AuditEntries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuditEntries

`func (o *ListAuditTrailResponse) SetAuditEntries(v []AuditEntry)`

SetAuditEntries sets AuditEntries field to given value.


### GetTotal

`func (o *ListAuditTrailResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListAuditTrailResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListAuditTrailResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListAuditTrailResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListAuditTrailResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListAuditTrailResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListAuditTrailResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListAuditTrailResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListAuditTrailResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


