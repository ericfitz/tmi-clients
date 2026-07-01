# WebhookSubscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier | 
**OwnerId** | **string** | Owner user ID | 
**ThreatModelId** | Pointer to **NullableString** | Optional threat model filter (null means all threat models) | [optional] 
**Name** | **string** | Descriptive name | 
**Url** | **string** | Webhook endpoint URL (must be HTTPS) | 
**Events** | [**[]WebhookEventType**](WebhookEventType.md) | List of event types to subscribe to. See WebhookEventType for available events. | 
**Secret** | Pointer to **string** | HMAC secret for signing payloads (not returned in GET responses) | [optional] 
**Status** | **string** | Subscription status | 
**ChallengesSent** | Pointer to **int32** | Number of verification challenges sent | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp | 
**ModifiedAt** | **time.Time** | Last modification timestamp | 
**LastSuccessfulUse** | Pointer to **NullableTime** | Last successful delivery timestamp | [optional] 
**PublicationFailures** | Pointer to **int32** | Count of consecutive failed deliveries | [optional] 

## Methods

### NewWebhookSubscription

`func NewWebhookSubscription(id string, ownerId string, name string, url string, events []WebhookEventType, status string, createdAt time.Time, modifiedAt time.Time, ) *WebhookSubscription`

NewWebhookSubscription instantiates a new WebhookSubscription object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookSubscriptionWithDefaults

`func NewWebhookSubscriptionWithDefaults() *WebhookSubscription`

NewWebhookSubscriptionWithDefaults instantiates a new WebhookSubscription object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *WebhookSubscription) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *WebhookSubscription) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *WebhookSubscription) SetId(v string)`

SetId sets Id field to given value.


### GetOwnerId

`func (o *WebhookSubscription) GetOwnerId() string`

GetOwnerId returns the OwnerId field if non-nil, zero value otherwise.

### GetOwnerIdOk

`func (o *WebhookSubscription) GetOwnerIdOk() (*string, bool)`

GetOwnerIdOk returns a tuple with the OwnerId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOwnerId

`func (o *WebhookSubscription) SetOwnerId(v string)`

SetOwnerId sets OwnerId field to given value.


### GetThreatModelId

`func (o *WebhookSubscription) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *WebhookSubscription) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *WebhookSubscription) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *WebhookSubscription) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.

### SetThreatModelIdNil

`func (o *WebhookSubscription) SetThreatModelIdNil(b bool)`

 SetThreatModelIdNil sets the value for ThreatModelId to be an explicit nil

### UnsetThreatModelId
`func (o *WebhookSubscription) UnsetThreatModelId()`

UnsetThreatModelId ensures that no value is present for ThreatModelId, not even an explicit nil
### GetName

`func (o *WebhookSubscription) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *WebhookSubscription) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *WebhookSubscription) SetName(v string)`

SetName sets Name field to given value.


### GetUrl

`func (o *WebhookSubscription) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WebhookSubscription) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *WebhookSubscription) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetEvents

`func (o *WebhookSubscription) GetEvents() []WebhookEventType`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *WebhookSubscription) GetEventsOk() (*[]WebhookEventType, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *WebhookSubscription) SetEvents(v []WebhookEventType)`

SetEvents sets Events field to given value.


### GetSecret

`func (o *WebhookSubscription) GetSecret() string`

GetSecret returns the Secret field if non-nil, zero value otherwise.

### GetSecretOk

`func (o *WebhookSubscription) GetSecretOk() (*string, bool)`

GetSecretOk returns a tuple with the Secret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecret

`func (o *WebhookSubscription) SetSecret(v string)`

SetSecret sets Secret field to given value.

### HasSecret

`func (o *WebhookSubscription) HasSecret() bool`

HasSecret returns a boolean if a field has been set.

### GetStatus

`func (o *WebhookSubscription) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *WebhookSubscription) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *WebhookSubscription) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetChallengesSent

`func (o *WebhookSubscription) GetChallengesSent() int32`

GetChallengesSent returns the ChallengesSent field if non-nil, zero value otherwise.

### GetChallengesSentOk

`func (o *WebhookSubscription) GetChallengesSentOk() (*int32, bool)`

GetChallengesSentOk returns a tuple with the ChallengesSent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChallengesSent

`func (o *WebhookSubscription) SetChallengesSent(v int32)`

SetChallengesSent sets ChallengesSent field to given value.

### HasChallengesSent

`func (o *WebhookSubscription) HasChallengesSent() bool`

HasChallengesSent returns a boolean if a field has been set.

### GetCreatedAt

`func (o *WebhookSubscription) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *WebhookSubscription) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *WebhookSubscription) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *WebhookSubscription) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *WebhookSubscription) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *WebhookSubscription) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetLastSuccessfulUse

`func (o *WebhookSubscription) GetLastSuccessfulUse() time.Time`

GetLastSuccessfulUse returns the LastSuccessfulUse field if non-nil, zero value otherwise.

### GetLastSuccessfulUseOk

`func (o *WebhookSubscription) GetLastSuccessfulUseOk() (*time.Time, bool)`

GetLastSuccessfulUseOk returns a tuple with the LastSuccessfulUse field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastSuccessfulUse

`func (o *WebhookSubscription) SetLastSuccessfulUse(v time.Time)`

SetLastSuccessfulUse sets LastSuccessfulUse field to given value.

### HasLastSuccessfulUse

`func (o *WebhookSubscription) HasLastSuccessfulUse() bool`

HasLastSuccessfulUse returns a boolean if a field has been set.

### SetLastSuccessfulUseNil

`func (o *WebhookSubscription) SetLastSuccessfulUseNil(b bool)`

 SetLastSuccessfulUseNil sets the value for LastSuccessfulUse to be an explicit nil

### UnsetLastSuccessfulUse
`func (o *WebhookSubscription) UnsetLastSuccessfulUse()`

UnsetLastSuccessfulUse ensures that no value is present for LastSuccessfulUse, not even an explicit nil
### GetPublicationFailures

`func (o *WebhookSubscription) GetPublicationFailures() int32`

GetPublicationFailures returns the PublicationFailures field if non-nil, zero value otherwise.

### GetPublicationFailuresOk

`func (o *WebhookSubscription) GetPublicationFailuresOk() (*int32, bool)`

GetPublicationFailuresOk returns a tuple with the PublicationFailures field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicationFailures

`func (o *WebhookSubscription) SetPublicationFailures(v int32)`

SetPublicationFailures sets PublicationFailures field to given value.

### HasPublicationFailures

`func (o *WebhookSubscription) HasPublicationFailures() bool`

HasPublicationFailures returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


