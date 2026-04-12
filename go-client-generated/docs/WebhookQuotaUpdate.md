# WebhookQuotaUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**MaxSubscriptions** | **int32** | Maximum webhook subscriptions | 
**MaxEventsPerMinute** | **int32** | Maximum webhook events per minute | 
**MaxSubscriptionRequestsPerMinute** | **int32** | Maximum subscription requests per minute | 
**MaxSubscriptionRequestsPerDay** | **int32** | Maximum subscription requests per day | 

## Methods

### NewWebhookQuotaUpdate

`func NewWebhookQuotaUpdate(maxSubscriptions int32, maxEventsPerMinute int32, maxSubscriptionRequestsPerMinute int32, maxSubscriptionRequestsPerDay int32, ) *WebhookQuotaUpdate`

NewWebhookQuotaUpdate instantiates a new WebhookQuotaUpdate object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookQuotaUpdateWithDefaults

`func NewWebhookQuotaUpdateWithDefaults() *WebhookQuotaUpdate`

NewWebhookQuotaUpdateWithDefaults instantiates a new WebhookQuotaUpdate object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMaxSubscriptions

`func (o *WebhookQuotaUpdate) GetMaxSubscriptions() int32`

GetMaxSubscriptions returns the MaxSubscriptions field if non-nil, zero value otherwise.

### GetMaxSubscriptionsOk

`func (o *WebhookQuotaUpdate) GetMaxSubscriptionsOk() (*int32, bool)`

GetMaxSubscriptionsOk returns a tuple with the MaxSubscriptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptions

`func (o *WebhookQuotaUpdate) SetMaxSubscriptions(v int32)`

SetMaxSubscriptions sets MaxSubscriptions field to given value.


### GetMaxEventsPerMinute

`func (o *WebhookQuotaUpdate) GetMaxEventsPerMinute() int32`

GetMaxEventsPerMinute returns the MaxEventsPerMinute field if non-nil, zero value otherwise.

### GetMaxEventsPerMinuteOk

`func (o *WebhookQuotaUpdate) GetMaxEventsPerMinuteOk() (*int32, bool)`

GetMaxEventsPerMinuteOk returns a tuple with the MaxEventsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxEventsPerMinute

`func (o *WebhookQuotaUpdate) SetMaxEventsPerMinute(v int32)`

SetMaxEventsPerMinute sets MaxEventsPerMinute field to given value.


### GetMaxSubscriptionRequestsPerMinute

`func (o *WebhookQuotaUpdate) GetMaxSubscriptionRequestsPerMinute() int32`

GetMaxSubscriptionRequestsPerMinute returns the MaxSubscriptionRequestsPerMinute field if non-nil, zero value otherwise.

### GetMaxSubscriptionRequestsPerMinuteOk

`func (o *WebhookQuotaUpdate) GetMaxSubscriptionRequestsPerMinuteOk() (*int32, bool)`

GetMaxSubscriptionRequestsPerMinuteOk returns a tuple with the MaxSubscriptionRequestsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptionRequestsPerMinute

`func (o *WebhookQuotaUpdate) SetMaxSubscriptionRequestsPerMinute(v int32)`

SetMaxSubscriptionRequestsPerMinute sets MaxSubscriptionRequestsPerMinute field to given value.


### GetMaxSubscriptionRequestsPerDay

`func (o *WebhookQuotaUpdate) GetMaxSubscriptionRequestsPerDay() int32`

GetMaxSubscriptionRequestsPerDay returns the MaxSubscriptionRequestsPerDay field if non-nil, zero value otherwise.

### GetMaxSubscriptionRequestsPerDayOk

`func (o *WebhookQuotaUpdate) GetMaxSubscriptionRequestsPerDayOk() (*int32, bool)`

GetMaxSubscriptionRequestsPerDayOk returns a tuple with the MaxSubscriptionRequestsPerDay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptionRequestsPerDay

`func (o *WebhookQuotaUpdate) SetMaxSubscriptionRequestsPerDay(v int32)`

SetMaxSubscriptionRequestsPerDay sets MaxSubscriptionRequestsPerDay field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


