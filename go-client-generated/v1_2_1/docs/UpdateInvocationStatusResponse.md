# UpdateInvocationStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Invocation identifier | 
**Status** | **string** | Current status | 
**StatusPercent** | **int32** | Progress percentage | 
**StatusUpdatedAt** | **time.Time** | Status update timestamp | 

## Methods

### NewUpdateInvocationStatusResponse

`func NewUpdateInvocationStatusResponse(id string, status string, statusPercent int32, statusUpdatedAt time.Time, ) *UpdateInvocationStatusResponse`

NewUpdateInvocationStatusResponse instantiates a new UpdateInvocationStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateInvocationStatusResponseWithDefaults

`func NewUpdateInvocationStatusResponseWithDefaults() *UpdateInvocationStatusResponse`

NewUpdateInvocationStatusResponseWithDefaults instantiates a new UpdateInvocationStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateInvocationStatusResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateInvocationStatusResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateInvocationStatusResponse) SetId(v string)`

SetId sets Id field to given value.


### GetStatus

`func (o *UpdateInvocationStatusResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateInvocationStatusResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateInvocationStatusResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetStatusPercent

`func (o *UpdateInvocationStatusResponse) GetStatusPercent() int32`

GetStatusPercent returns the StatusPercent field if non-nil, zero value otherwise.

### GetStatusPercentOk

`func (o *UpdateInvocationStatusResponse) GetStatusPercentOk() (*int32, bool)`

GetStatusPercentOk returns a tuple with the StatusPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusPercent

`func (o *UpdateInvocationStatusResponse) SetStatusPercent(v int32)`

SetStatusPercent sets StatusPercent field to given value.


### GetStatusUpdatedAt

`func (o *UpdateInvocationStatusResponse) GetStatusUpdatedAt() time.Time`

GetStatusUpdatedAt returns the StatusUpdatedAt field if non-nil, zero value otherwise.

### GetStatusUpdatedAtOk

`func (o *UpdateInvocationStatusResponse) GetStatusUpdatedAtOk() (*time.Time, bool)`

GetStatusUpdatedAtOk returns a tuple with the StatusUpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUpdatedAt

`func (o *UpdateInvocationStatusResponse) SetStatusUpdatedAt(v time.Time)`

SetStatusUpdatedAt sets StatusUpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


