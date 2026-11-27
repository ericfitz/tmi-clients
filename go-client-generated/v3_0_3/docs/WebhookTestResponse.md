# WebhookTestResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DeliveryId** | **string** | Test delivery ID | 
**Status** | **string** | Test result status | 
**Message** | Pointer to **string** | Result message | [optional] 

## Methods

### NewWebhookTestResponse

`func NewWebhookTestResponse(deliveryId string, status string, ) *WebhookTestResponse`

NewWebhookTestResponse instantiates a new WebhookTestResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookTestResponseWithDefaults

`func NewWebhookTestResponseWithDefaults() *WebhookTestResponse`

NewWebhookTestResponseWithDefaults instantiates a new WebhookTestResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDeliveryId

`func (o *WebhookTestResponse) GetDeliveryId() string`

GetDeliveryId returns the DeliveryId field if non-nil, zero value otherwise.

### GetDeliveryIdOk

`func (o *WebhookTestResponse) GetDeliveryIdOk() (*string, bool)`

GetDeliveryIdOk returns a tuple with the DeliveryId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeliveryId

`func (o *WebhookTestResponse) SetDeliveryId(v string)`

SetDeliveryId sets DeliveryId field to given value.


### GetStatus

`func (o *WebhookTestResponse) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *WebhookTestResponse) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *WebhookTestResponse) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetMessage

`func (o *WebhookTestResponse) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *WebhookTestResponse) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *WebhookTestResponse) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *WebhookTestResponse) HasMessage() bool`

HasMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


