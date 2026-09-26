# TimmyStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MemoryUsedBytes** | **int32** | Current memory usage in bytes | 
**MemoryBudgetBytes** | **int32** | Total memory budget in bytes | 
**MemoryUtilizationPct** | **float32** | Memory utilization percentage | 
**LoadedIndexes** | **int32** | Number of currently loaded indexes | 
**ActiveSessions** | **int32** | Number of active chat sessions | 
**EvictionsTotal** | **int32** | Total number of index evictions | 
**EvictionsPressure** | **int32** | Number of evictions due to memory pressure | 
**SessionsRejectedTotal** | **int32** | Total number of sessions rejected due to resource constraints | 

## Methods

### NewTimmyStatusResponse

`func NewTimmyStatusResponse(memoryUsedBytes int32, memoryBudgetBytes int32, memoryUtilizationPct float32, loadedIndexes int32, activeSessions int32, evictionsTotal int32, evictionsPressure int32, sessionsRejectedTotal int32, ) *TimmyStatusResponse`

NewTimmyStatusResponse instantiates a new TimmyStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTimmyStatusResponseWithDefaults

`func NewTimmyStatusResponseWithDefaults() *TimmyStatusResponse`

NewTimmyStatusResponseWithDefaults instantiates a new TimmyStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMemoryUsedBytes

`func (o *TimmyStatusResponse) GetMemoryUsedBytes() int32`

GetMemoryUsedBytes returns the MemoryUsedBytes field if non-nil, zero value otherwise.

### GetMemoryUsedBytesOk

`func (o *TimmyStatusResponse) GetMemoryUsedBytesOk() (*int32, bool)`

GetMemoryUsedBytesOk returns a tuple with the MemoryUsedBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemoryUsedBytes

`func (o *TimmyStatusResponse) SetMemoryUsedBytes(v int32)`

SetMemoryUsedBytes sets MemoryUsedBytes field to given value.


### GetMemoryBudgetBytes

`func (o *TimmyStatusResponse) GetMemoryBudgetBytes() int32`

GetMemoryBudgetBytes returns the MemoryBudgetBytes field if non-nil, zero value otherwise.

### GetMemoryBudgetBytesOk

`func (o *TimmyStatusResponse) GetMemoryBudgetBytesOk() (*int32, bool)`

GetMemoryBudgetBytesOk returns a tuple with the MemoryBudgetBytes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemoryBudgetBytes

`func (o *TimmyStatusResponse) SetMemoryBudgetBytes(v int32)`

SetMemoryBudgetBytes sets MemoryBudgetBytes field to given value.


### GetMemoryUtilizationPct

`func (o *TimmyStatusResponse) GetMemoryUtilizationPct() float32`

GetMemoryUtilizationPct returns the MemoryUtilizationPct field if non-nil, zero value otherwise.

### GetMemoryUtilizationPctOk

`func (o *TimmyStatusResponse) GetMemoryUtilizationPctOk() (*float32, bool)`

GetMemoryUtilizationPctOk returns a tuple with the MemoryUtilizationPct field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMemoryUtilizationPct

`func (o *TimmyStatusResponse) SetMemoryUtilizationPct(v float32)`

SetMemoryUtilizationPct sets MemoryUtilizationPct field to given value.


### GetLoadedIndexes

`func (o *TimmyStatusResponse) GetLoadedIndexes() int32`

GetLoadedIndexes returns the LoadedIndexes field if non-nil, zero value otherwise.

### GetLoadedIndexesOk

`func (o *TimmyStatusResponse) GetLoadedIndexesOk() (*int32, bool)`

GetLoadedIndexesOk returns a tuple with the LoadedIndexes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLoadedIndexes

`func (o *TimmyStatusResponse) SetLoadedIndexes(v int32)`

SetLoadedIndexes sets LoadedIndexes field to given value.


### GetActiveSessions

`func (o *TimmyStatusResponse) GetActiveSessions() int32`

GetActiveSessions returns the ActiveSessions field if non-nil, zero value otherwise.

### GetActiveSessionsOk

`func (o *TimmyStatusResponse) GetActiveSessionsOk() (*int32, bool)`

GetActiveSessionsOk returns a tuple with the ActiveSessions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActiveSessions

`func (o *TimmyStatusResponse) SetActiveSessions(v int32)`

SetActiveSessions sets ActiveSessions field to given value.


### GetEvictionsTotal

`func (o *TimmyStatusResponse) GetEvictionsTotal() int32`

GetEvictionsTotal returns the EvictionsTotal field if non-nil, zero value otherwise.

### GetEvictionsTotalOk

`func (o *TimmyStatusResponse) GetEvictionsTotalOk() (*int32, bool)`

GetEvictionsTotalOk returns a tuple with the EvictionsTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvictionsTotal

`func (o *TimmyStatusResponse) SetEvictionsTotal(v int32)`

SetEvictionsTotal sets EvictionsTotal field to given value.


### GetEvictionsPressure

`func (o *TimmyStatusResponse) GetEvictionsPressure() int32`

GetEvictionsPressure returns the EvictionsPressure field if non-nil, zero value otherwise.

### GetEvictionsPressureOk

`func (o *TimmyStatusResponse) GetEvictionsPressureOk() (*int32, bool)`

GetEvictionsPressureOk returns a tuple with the EvictionsPressure field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvictionsPressure

`func (o *TimmyStatusResponse) SetEvictionsPressure(v int32)`

SetEvictionsPressure sets EvictionsPressure field to given value.


### GetSessionsRejectedTotal

`func (o *TimmyStatusResponse) GetSessionsRejectedTotal() int32`

GetSessionsRejectedTotal returns the SessionsRejectedTotal field if non-nil, zero value otherwise.

### GetSessionsRejectedTotalOk

`func (o *TimmyStatusResponse) GetSessionsRejectedTotalOk() (*int32, bool)`

GetSessionsRejectedTotalOk returns a tuple with the SessionsRejectedTotal field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSessionsRejectedTotal

`func (o *TimmyStatusResponse) SetSessionsRejectedTotal(v int32)`

SetSessionsRejectedTotal sets SessionsRejectedTotal field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


