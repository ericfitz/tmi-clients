# UpdateWebhookDeliveryStatusRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | **string** | New delivery status | 
**StatusPercent** | Pointer to **int32** | Progress percentage (0-100) | [optional] 
**StatusMessage** | Pointer to **string** | Human-readable status description | [optional] 

## Methods

### NewUpdateWebhookDeliveryStatusRequest

`func NewUpdateWebhookDeliveryStatusRequest(status string, ) *UpdateWebhookDeliveryStatusRequest`

NewUpdateWebhookDeliveryStatusRequest instantiates a new UpdateWebhookDeliveryStatusRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateWebhookDeliveryStatusRequestWithDefaults

`func NewUpdateWebhookDeliveryStatusRequestWithDefaults() *UpdateWebhookDeliveryStatusRequest`

NewUpdateWebhookDeliveryStatusRequestWithDefaults instantiates a new UpdateWebhookDeliveryStatusRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateWebhookDeliveryStatusRequest) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetStatusPercent

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatusPercent() int32`

GetStatusPercent returns the StatusPercent field if non-nil, zero value otherwise.

### GetStatusPercentOk

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatusPercentOk() (*int32, bool)`

GetStatusPercentOk returns a tuple with the StatusPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusPercent

`func (o *UpdateWebhookDeliveryStatusRequest) SetStatusPercent(v int32)`

SetStatusPercent sets StatusPercent field to given value.

### HasStatusPercent

`func (o *UpdateWebhookDeliveryStatusRequest) HasStatusPercent() bool`

HasStatusPercent returns a boolean if a field has been set.

### GetStatusMessage

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatusMessage() string`

GetStatusMessage returns the StatusMessage field if non-nil, zero value otherwise.

### GetStatusMessageOk

`func (o *UpdateWebhookDeliveryStatusRequest) GetStatusMessageOk() (*string, bool)`

GetStatusMessageOk returns a tuple with the StatusMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusMessage

`func (o *UpdateWebhookDeliveryStatusRequest) SetStatusMessage(v string)`

SetStatusMessage sets StatusMessage field to given value.

### HasStatusMessage

`func (o *UpdateWebhookDeliveryStatusRequest) HasStatusMessage() bool`

HasStatusMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


