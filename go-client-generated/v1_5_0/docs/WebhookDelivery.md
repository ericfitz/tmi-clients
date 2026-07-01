# WebhookDelivery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier (UUIDv7) | 
**SubscriptionId** | **string** | Subscription that triggered this delivery | 
**EventType** | [**WebhookEventType**](WebhookEventType.md) |  | 
**Payload** | Pointer to **map[string]interface{}** | Event payload (JSON) | [optional] 
**Status** | **string** | Delivery status | 
**Attempts** | **int32** | Number of delivery attempts | 
**NextRetryAt** | Pointer to **NullableTime** | Next retry timestamp | [optional] 
**LastError** | Pointer to **string** | Last error message | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp | 
**DeliveredAt** | Pointer to **NullableTime** | Successful delivery timestamp | [optional] 
**StatusPercent** | Pointer to **int32** | Progress percentage | [optional] 
**StatusMessage** | Pointer to **string** | Human-readable status description | [optional] 
**LastActivityAt** | Pointer to **NullableTime** | Last status update or delivery attempt | [optional] 
**AddonId** | Pointer to **NullableString** | Add-on ID (for addon invocations only) | [optional] 
**InvokedBy** | Pointer to [**NullableUser**](User.md) | User who invoked the add-on (for addon invocations only) | [optional] 

## Methods

### NewWebhookDelivery

`func NewWebhookDelivery(id string, subscriptionId string, eventType WebhookEventType, status string, attempts int32, createdAt time.Time, ) *WebhookDelivery`

NewWebhookDelivery instantiates a new WebhookDelivery object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookDeliveryWithDefaults

`func NewWebhookDeliveryWithDefaults() *WebhookDelivery`

NewWebhookDeliveryWithDefaults instantiates a new WebhookDelivery object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WebhookDelivery) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WebhookDelivery) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WebhookDelivery) SetId(v string)`

SetId sets Id field to given value.


### GetSubscriptionId

`func (o *WebhookDelivery) GetSubscriptionId() string`

GetSubscriptionId returns the SubscriptionId field if non-nil, zero value otherwise.

### GetSubscriptionIdOk

`func (o *WebhookDelivery) GetSubscriptionIdOk() (*string, bool)`

GetSubscriptionIdOk returns a tuple with the SubscriptionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubscriptionId

`func (o *WebhookDelivery) SetSubscriptionId(v string)`

SetSubscriptionId sets SubscriptionId field to given value.


### GetEventType

`func (o *WebhookDelivery) GetEventType() WebhookEventType`

GetEventType returns the EventType field if non-nil, zero value otherwise.

### GetEventTypeOk

`func (o *WebhookDelivery) GetEventTypeOk() (*WebhookEventType, bool)`

GetEventTypeOk returns a tuple with the EventType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventType

`func (o *WebhookDelivery) SetEventType(v WebhookEventType)`

SetEventType sets EventType field to given value.


### GetPayload

`func (o *WebhookDelivery) GetPayload() map[string]interface{}`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *WebhookDelivery) GetPayloadOk() (*map[string]interface{}, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *WebhookDelivery) SetPayload(v map[string]interface{})`

SetPayload sets Payload field to given value.

### HasPayload

`func (o *WebhookDelivery) HasPayload() bool`

HasPayload returns a boolean if a field has been set.

### GetStatus

`func (o *WebhookDelivery) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *WebhookDelivery) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *WebhookDelivery) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetAttempts

`func (o *WebhookDelivery) GetAttempts() int32`

GetAttempts returns the Attempts field if non-nil, zero value otherwise.

### GetAttemptsOk

`func (o *WebhookDelivery) GetAttemptsOk() (*int32, bool)`

GetAttemptsOk returns a tuple with the Attempts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttempts

`func (o *WebhookDelivery) SetAttempts(v int32)`

SetAttempts sets Attempts field to given value.


### GetNextRetryAt

`func (o *WebhookDelivery) GetNextRetryAt() time.Time`

GetNextRetryAt returns the NextRetryAt field if non-nil, zero value otherwise.

### GetNextRetryAtOk

`func (o *WebhookDelivery) GetNextRetryAtOk() (*time.Time, bool)`

GetNextRetryAtOk returns a tuple with the NextRetryAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextRetryAt

`func (o *WebhookDelivery) SetNextRetryAt(v time.Time)`

SetNextRetryAt sets NextRetryAt field to given value.

### HasNextRetryAt

`func (o *WebhookDelivery) HasNextRetryAt() bool`

HasNextRetryAt returns a boolean if a field has been set.

### SetNextRetryAtNil

`func (o *WebhookDelivery) SetNextRetryAtNil(b bool)`

 SetNextRetryAtNil sets the value for NextRetryAt to be an explicit nil

### UnsetNextRetryAt
`func (o *WebhookDelivery) UnsetNextRetryAt()`

UnsetNextRetryAt ensures that no value is present for NextRetryAt, not even an explicit nil
### GetLastError

`func (o *WebhookDelivery) GetLastError() string`

GetLastError returns the LastError field if non-nil, zero value otherwise.

### GetLastErrorOk

`func (o *WebhookDelivery) GetLastErrorOk() (*string, bool)`

GetLastErrorOk returns a tuple with the LastError field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastError

`func (o *WebhookDelivery) SetLastError(v string)`

SetLastError sets LastError field to given value.

### HasLastError

`func (o *WebhookDelivery) HasLastError() bool`

HasLastError returns a boolean if a field has been set.

### GetCreatedAt

`func (o *WebhookDelivery) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WebhookDelivery) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WebhookDelivery) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetDeliveredAt

`func (o *WebhookDelivery) GetDeliveredAt() time.Time`

GetDeliveredAt returns the DeliveredAt field if non-nil, zero value otherwise.

### GetDeliveredAtOk

`func (o *WebhookDelivery) GetDeliveredAtOk() (*time.Time, bool)`

GetDeliveredAtOk returns a tuple with the DeliveredAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeliveredAt

`func (o *WebhookDelivery) SetDeliveredAt(v time.Time)`

SetDeliveredAt sets DeliveredAt field to given value.

### HasDeliveredAt

`func (o *WebhookDelivery) HasDeliveredAt() bool`

HasDeliveredAt returns a boolean if a field has been set.

### SetDeliveredAtNil

`func (o *WebhookDelivery) SetDeliveredAtNil(b bool)`

 SetDeliveredAtNil sets the value for DeliveredAt to be an explicit nil

### UnsetDeliveredAt
`func (o *WebhookDelivery) UnsetDeliveredAt()`

UnsetDeliveredAt ensures that no value is present for DeliveredAt, not even an explicit nil
### GetStatusPercent

`func (o *WebhookDelivery) GetStatusPercent() int32`

GetStatusPercent returns the StatusPercent field if non-nil, zero value otherwise.

### GetStatusPercentOk

`func (o *WebhookDelivery) GetStatusPercentOk() (*int32, bool)`

GetStatusPercentOk returns a tuple with the StatusPercent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusPercent

`func (o *WebhookDelivery) SetStatusPercent(v int32)`

SetStatusPercent sets StatusPercent field to given value.

### HasStatusPercent

`func (o *WebhookDelivery) HasStatusPercent() bool`

HasStatusPercent returns a boolean if a field has been set.

### GetStatusMessage

`func (o *WebhookDelivery) GetStatusMessage() string`

GetStatusMessage returns the StatusMessage field if non-nil, zero value otherwise.

### GetStatusMessageOk

`func (o *WebhookDelivery) GetStatusMessageOk() (*string, bool)`

GetStatusMessageOk returns a tuple with the StatusMessage field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatusMessage

`func (o *WebhookDelivery) SetStatusMessage(v string)`

SetStatusMessage sets StatusMessage field to given value.

### HasStatusMessage

`func (o *WebhookDelivery) HasStatusMessage() bool`

HasStatusMessage returns a boolean if a field has been set.

### GetLastActivityAt

`func (o *WebhookDelivery) GetLastActivityAt() time.Time`

GetLastActivityAt returns the LastActivityAt field if non-nil, zero value otherwise.

### GetLastActivityAtOk

`func (o *WebhookDelivery) GetLastActivityAtOk() (*time.Time, bool)`

GetLastActivityAtOk returns a tuple with the LastActivityAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastActivityAt

`func (o *WebhookDelivery) SetLastActivityAt(v time.Time)`

SetLastActivityAt sets LastActivityAt field to given value.

### HasLastActivityAt

`func (o *WebhookDelivery) HasLastActivityAt() bool`

HasLastActivityAt returns a boolean if a field has been set.

### SetLastActivityAtNil

`func (o *WebhookDelivery) SetLastActivityAtNil(b bool)`

 SetLastActivityAtNil sets the value for LastActivityAt to be an explicit nil

### UnsetLastActivityAt
`func (o *WebhookDelivery) UnsetLastActivityAt()`

UnsetLastActivityAt ensures that no value is present for LastActivityAt, not even an explicit nil
### GetAddonId

`func (o *WebhookDelivery) GetAddonId() string`

GetAddonId returns the AddonId field if non-nil, zero value otherwise.

### GetAddonIdOk

`func (o *WebhookDelivery) GetAddonIdOk() (*string, bool)`

GetAddonIdOk returns a tuple with the AddonId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddonId

`func (o *WebhookDelivery) SetAddonId(v string)`

SetAddonId sets AddonId field to given value.

### HasAddonId

`func (o *WebhookDelivery) HasAddonId() bool`

HasAddonId returns a boolean if a field has been set.

### SetAddonIdNil

`func (o *WebhookDelivery) SetAddonIdNil(b bool)`

 SetAddonIdNil sets the value for AddonId to be an explicit nil

### UnsetAddonId
`func (o *WebhookDelivery) UnsetAddonId()`

UnsetAddonId ensures that no value is present for AddonId, not even an explicit nil
### GetInvokedBy

`func (o *WebhookDelivery) GetInvokedBy() User`

GetInvokedBy returns the InvokedBy field if non-nil, zero value otherwise.

### GetInvokedByOk

`func (o *WebhookDelivery) GetInvokedByOk() (*User, bool)`

GetInvokedByOk returns a tuple with the InvokedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInvokedBy

`func (o *WebhookDelivery) SetInvokedBy(v User)`

SetInvokedBy sets InvokedBy field to given value.

### HasInvokedBy

`func (o *WebhookDelivery) HasInvokedBy() bool`

HasInvokedBy returns a boolean if a field has been set.

### SetInvokedByNil

`func (o *WebhookDelivery) SetInvokedByNil(b bool)`

 SetInvokedByNil sets the value for InvokedBy to be an explicit nil

### UnsetInvokedBy
`func (o *WebhookDelivery) UnsetInvokedBy()`

UnsetInvokedBy ensures that no value is present for InvokedBy, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


