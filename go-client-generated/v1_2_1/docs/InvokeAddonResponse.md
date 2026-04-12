# InvokeAddonResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InvocationId** | **string** | Invocation identifier for tracking | 
**Status** | **string** | Current invocation status | 
**CreatedAt** | **time.Time** | Invocation creation timestamp | 

## Methods

### NewInvokeAddonResponse

`func NewInvokeAddonResponse(invocationId string, status string, createdAt time.Time, ) *InvokeAddonResponse`

NewInvokeAddonResponse instantiates a new InvokeAddonResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvokeAddonResponseWithDefaults

`func NewInvokeAddonResponseWithDefaults() *InvokeAddonResponse`

NewInvokeAddonResponseWithDefaults instantiates a new InvokeAddonResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInvocationId

`func (o *InvokeAddonResponse) GetInvocationId() string`

GetInvocationId returns the InvocationId field if non-nil, zero value otherwise.

### GetInvocationIdOk

`func (o *InvokeAddonResponse) GetInvocationIdOk() (*string, bool)`

GetInvocationIdOk returns a tuple with the InvocationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvocationId

`func (o *InvokeAddonResponse) SetInvocationId(v string)`

SetInvocationId sets InvocationId field to given value.


### GetStatus

`func (o *InvokeAddonResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *InvokeAddonResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *InvokeAddonResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetCreatedAt

`func (o *InvokeAddonResponse) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *InvokeAddonResponse) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *InvokeAddonResponse) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


