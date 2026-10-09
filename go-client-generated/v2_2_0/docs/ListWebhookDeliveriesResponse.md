# ListWebhookDeliveriesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Deliveries** | [**[]WebhookDelivery**](WebhookDelivery.md) |  | 
**Total** | **int32** | Total number of deliveries matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListWebhookDeliveriesResponse

`func NewListWebhookDeliveriesResponse(deliveries []WebhookDelivery, total int32, limit int32, offset int32, ) *ListWebhookDeliveriesResponse`

NewListWebhookDeliveriesResponse instantiates a new ListWebhookDeliveriesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookDeliveriesResponseWithDefaults

`func NewListWebhookDeliveriesResponseWithDefaults() *ListWebhookDeliveriesResponse`

NewListWebhookDeliveriesResponseWithDefaults instantiates a new ListWebhookDeliveriesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDeliveries

`func (o *ListWebhookDeliveriesResponse) GetDeliveries() []WebhookDelivery`

GetDeliveries returns the Deliveries field if non-nil, zero value otherwise.

### GetDeliveriesOk

`func (o *ListWebhookDeliveriesResponse) GetDeliveriesOk() (*[]WebhookDelivery, bool)`

GetDeliveriesOk returns a tuple with the Deliveries field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeliveries

`func (o *ListWebhookDeliveriesResponse) SetDeliveries(v []WebhookDelivery)`

SetDeliveries sets Deliveries field to given value.


### GetTotal

`func (o *ListWebhookDeliveriesResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListWebhookDeliveriesResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListWebhookDeliveriesResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListWebhookDeliveriesResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListWebhookDeliveriesResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListWebhookDeliveriesResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListWebhookDeliveriesResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListWebhookDeliveriesResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListWebhookDeliveriesResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


