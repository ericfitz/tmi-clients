# TimmyUsageResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Usage** | [**[]TimmyUsageRecord**](TimmyUsageRecord.md) |  | 
**Total** | **int32** | Total number of usage records | 

## Methods

### NewTimmyUsageResponse

`func NewTimmyUsageResponse(usage []TimmyUsageRecord, total int32, ) *TimmyUsageResponse`

NewTimmyUsageResponse instantiates a new TimmyUsageResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimmyUsageResponseWithDefaults

`func NewTimmyUsageResponseWithDefaults() *TimmyUsageResponse`

NewTimmyUsageResponseWithDefaults instantiates a new TimmyUsageResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUsage

`func (o *TimmyUsageResponse) GetUsage() []TimmyUsageRecord`

GetUsage returns the Usage field if non-nil, zero value otherwise.

### GetUsageOk

`func (o *TimmyUsageResponse) GetUsageOk() (*[]TimmyUsageRecord, bool)`

GetUsageOk returns a tuple with the Usage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUsage

`func (o *TimmyUsageResponse) SetUsage(v []TimmyUsageRecord)`

SetUsage sets Usage field to given value.


### GetTotal

`func (o *TimmyUsageResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *TimmyUsageResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *TimmyUsageResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


