# UpdateWebhookDeliveryStatusResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** |  | 
**Status** | **string** |  | 
**StatusPercent** | **int32** |  | 
**StatusUpdatedAt** | **time.Time** |  | 

## Methods

### NewUpdateWebhookDeliveryStatusResponse

`func NewUpdateWebhookDeliveryStatusResponse(id string, status string, statusPercent int32, statusUpdatedAt time.Time, ) *UpdateWebhookDeliveryStatusResponse`

NewUpdateWebhookDeliveryStatusResponse instantiates a new UpdateWebhookDeliveryStatusResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUpdateWebhookDeliveryStatusResponseWithDefaults

`func NewUpdateWebhookDeliveryStatusResponseWithDefaults() *UpdateWebhookDeliveryStatusResponse`

NewUpdateWebhookDeliveryStatusResponseWithDefaults instantiates a new UpdateWebhookDeliveryStatusResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *UpdateWebhookDeliveryStatusResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UpdateWebhookDeliveryStatusResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UpdateWebhookDeliveryStatusResponse) SetId(v string)`

SetId sets Id field to given value.


### GetStatus

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *UpdateWebhookDeliveryStatusResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetStatusPercent

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatusPercent() int32`

GetStatusPercent returns the StatusPercent field if non-nil, zero value otherwise.

### GetStatusPercentOk

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatusPercentOk() (*int32, bool)`

GetStatusPercentOk returns a tuple with the StatusPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusPercent

`func (o *UpdateWebhookDeliveryStatusResponse) SetStatusPercent(v int32)`

SetStatusPercent sets StatusPercent field to given value.


### GetStatusUpdatedAt

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatusUpdatedAt() time.Time`

GetStatusUpdatedAt returns the StatusUpdatedAt field if non-nil, zero value otherwise.

### GetStatusUpdatedAtOk

`func (o *UpdateWebhookDeliveryStatusResponse) GetStatusUpdatedAtOk() (*time.Time, bool)`

GetStatusUpdatedAtOk returns a tuple with the StatusUpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusUpdatedAt

`func (o *UpdateWebhookDeliveryStatusResponse) SetStatusUpdatedAt(v time.Time)`

SetStatusUpdatedAt sets StatusUpdatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


