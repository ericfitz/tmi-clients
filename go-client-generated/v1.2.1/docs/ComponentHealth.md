# ComponentHealth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | Component health status | 
**LatencyMs** | Pointer to **int64** | Response latency in milliseconds | [optional] 
**Message** | Pointer to **string** | Human-readable status message or error description | [optional] 

## Methods

### NewComponentHealth

`func NewComponentHealth(status string, ) *ComponentHealth`

NewComponentHealth instantiates a new ComponentHealth object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewComponentHealthWithDefaults

`func NewComponentHealthWithDefaults() *ComponentHealth`

NewComponentHealthWithDefaults instantiates a new ComponentHealth object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *ComponentHealth) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ComponentHealth) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ComponentHealth) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetLatencyMs

`func (o *ComponentHealth) GetLatencyMs() int64`

GetLatencyMs returns the LatencyMs field if non-nil, zero value otherwise.

### GetLatencyMsOk

`func (o *ComponentHealth) GetLatencyMsOk() (*int64, bool)`

GetLatencyMsOk returns a tuple with the LatencyMs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLatencyMs

`func (o *ComponentHealth) SetLatencyMs(v int64)`

SetLatencyMs sets LatencyMs field to given value.

### HasLatencyMs

`func (o *ComponentHealth) HasLatencyMs() bool`

HasLatencyMs returns a boolean if a field has been set.

### GetMessage

`func (o *ComponentHealth) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *ComponentHealth) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *ComponentHealth) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *ComponentHealth) HasMessage() bool`

HasMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


