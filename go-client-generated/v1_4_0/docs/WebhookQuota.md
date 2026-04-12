# WebhookQuota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**OwnerId** | **string** | Owner ID | 
**MaxSubscriptions** | **int32** | Maximum number of webhook subscriptions | 
**MaxEventsPerMinute** | **int32** | Maximum webhook events per minute | 
**MaxSubscriptionRequestsPerMinute** | **int32** | Maximum subscription requests per minute | 
**MaxSubscriptionRequestsPerDay** | **int32** | Maximum subscription requests per day | 
**CreatedAt** | Pointer to **time.Time** | Timestamp when the quota was created | [optional] 
**ModifiedAt** | Pointer to **time.Time** | Timestamp when the quota was last modified | [optional] 

## Methods

### NewWebhookQuota

`func NewWebhookQuota(ownerId string, maxSubscriptions int32, maxEventsPerMinute int32, maxSubscriptionRequestsPerMinute int32, maxSubscriptionRequestsPerDay int32, ) *WebhookQuota`

NewWebhookQuota instantiates a new WebhookQuota object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookQuotaWithDefaults

`func NewWebhookQuotaWithDefaults() *WebhookQuota`

NewWebhookQuotaWithDefaults instantiates a new WebhookQuota object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOwnerId

`func (o *WebhookQuota) GetOwnerId() string`

GetOwnerId returns the OwnerId field if non-nil, zero value otherwise.

### GetOwnerIdOk

`func (o *WebhookQuota) GetOwnerIdOk() (*string, bool)`

GetOwnerIdOk returns a tuple with the OwnerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnerId

`func (o *WebhookQuota) SetOwnerId(v string)`

SetOwnerId sets OwnerId field to given value.


### GetMaxSubscriptions

`func (o *WebhookQuota) GetMaxSubscriptions() int32`

GetMaxSubscriptions returns the MaxSubscriptions field if non-nil, zero value otherwise.

### GetMaxSubscriptionsOk

`func (o *WebhookQuota) GetMaxSubscriptionsOk() (*int32, bool)`

GetMaxSubscriptionsOk returns a tuple with the MaxSubscriptions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptions

`func (o *WebhookQuota) SetMaxSubscriptions(v int32)`

SetMaxSubscriptions sets MaxSubscriptions field to given value.


### GetMaxEventsPerMinute

`func (o *WebhookQuota) GetMaxEventsPerMinute() int32`

GetMaxEventsPerMinute returns the MaxEventsPerMinute field if non-nil, zero value otherwise.

### GetMaxEventsPerMinuteOk

`func (o *WebhookQuota) GetMaxEventsPerMinuteOk() (*int32, bool)`

GetMaxEventsPerMinuteOk returns a tuple with the MaxEventsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxEventsPerMinute

`func (o *WebhookQuota) SetMaxEventsPerMinute(v int32)`

SetMaxEventsPerMinute sets MaxEventsPerMinute field to given value.


### GetMaxSubscriptionRequestsPerMinute

`func (o *WebhookQuota) GetMaxSubscriptionRequestsPerMinute() int32`

GetMaxSubscriptionRequestsPerMinute returns the MaxSubscriptionRequestsPerMinute field if non-nil, zero value otherwise.

### GetMaxSubscriptionRequestsPerMinuteOk

`func (o *WebhookQuota) GetMaxSubscriptionRequestsPerMinuteOk() (*int32, bool)`

GetMaxSubscriptionRequestsPerMinuteOk returns a tuple with the MaxSubscriptionRequestsPerMinute field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptionRequestsPerMinute

`func (o *WebhookQuota) SetMaxSubscriptionRequestsPerMinute(v int32)`

SetMaxSubscriptionRequestsPerMinute sets MaxSubscriptionRequestsPerMinute field to given value.


### GetMaxSubscriptionRequestsPerDay

`func (o *WebhookQuota) GetMaxSubscriptionRequestsPerDay() int32`

GetMaxSubscriptionRequestsPerDay returns the MaxSubscriptionRequestsPerDay field if non-nil, zero value otherwise.

### GetMaxSubscriptionRequestsPerDayOk

`func (o *WebhookQuota) GetMaxSubscriptionRequestsPerDayOk() (*int32, bool)`

GetMaxSubscriptionRequestsPerDayOk returns a tuple with the MaxSubscriptionRequestsPerDay field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMaxSubscriptionRequestsPerDay

`func (o *WebhookQuota) SetMaxSubscriptionRequestsPerDay(v int32)`

SetMaxSubscriptionRequestsPerDay sets MaxSubscriptionRequestsPerDay field to given value.


### GetCreatedAt

`func (o *WebhookQuota) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WebhookQuota) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WebhookQuota) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *WebhookQuota) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *WebhookQuota) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *WebhookQuota) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *WebhookQuota) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *WebhookQuota) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


