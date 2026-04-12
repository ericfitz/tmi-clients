# ListWebhookSubscriptionsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Subscriptions** | [**[]WebhookSubscription**](WebhookSubscription.md) |  | 
**Total** | **int32** | Total number of subscriptions matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListWebhookSubscriptionsResponse

`func NewListWebhookSubscriptionsResponse(subscriptions []WebhookSubscription, total int32, limit int32, offset int32, ) *ListWebhookSubscriptionsResponse`

NewListWebhookSubscriptionsResponse instantiates a new ListWebhookSubscriptionsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListWebhookSubscriptionsResponseWithDefaults

`func NewListWebhookSubscriptionsResponseWithDefaults() *ListWebhookSubscriptionsResponse`

NewListWebhookSubscriptionsResponseWithDefaults instantiates a new ListWebhookSubscriptionsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSubscriptions

`func (o *ListWebhookSubscriptionsResponse) GetSubscriptions() []WebhookSubscription`

GetSubscriptions returns the Subscriptions field if non-nil, zero value otherwise.

### GetSubscriptionsOk

`func (o *ListWebhookSubscriptionsResponse) GetSubscriptionsOk() (*[]WebhookSubscription, bool)`

GetSubscriptionsOk returns a tuple with the Subscriptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubscriptions

`func (o *ListWebhookSubscriptionsResponse) SetSubscriptions(v []WebhookSubscription)`

SetSubscriptions sets Subscriptions field to given value.


### GetTotal

`func (o *ListWebhookSubscriptionsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListWebhookSubscriptionsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListWebhookSubscriptionsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListWebhookSubscriptionsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListWebhookSubscriptionsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListWebhookSubscriptionsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListWebhookSubscriptionsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListWebhookSubscriptionsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListWebhookSubscriptionsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


