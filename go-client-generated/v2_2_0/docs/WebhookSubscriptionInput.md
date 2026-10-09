# WebhookSubscriptionInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ThreatModelId** | Pointer to **NullableString** | Optional threat model filter | [optional] 
**Name** | **string** | Descriptive name for the subscription | 
**Url** | **string** | Webhook endpoint URL (must be HTTPS) | 
**Events** | **[]string** | List of event types to subscribe to | 
**Secret** | Pointer to **string** | Optional HMAC secret for signing payloads (auto-generated if not provided) | [optional] 

## Methods

### NewWebhookSubscriptionInput

`func NewWebhookSubscriptionInput(name string, url string, events []string, ) *WebhookSubscriptionInput`

NewWebhookSubscriptionInput instantiates a new WebhookSubscriptionInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWebhookSubscriptionInputWithDefaults

`func NewWebhookSubscriptionInputWithDefaults() *WebhookSubscriptionInput`

NewWebhookSubscriptionInputWithDefaults instantiates a new WebhookSubscriptionInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetThreatModelId

`func (o *WebhookSubscriptionInput) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *WebhookSubscriptionInput) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *WebhookSubscriptionInput) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *WebhookSubscriptionInput) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.

### SetThreatModelIdNil

`func (o *WebhookSubscriptionInput) SetThreatModelIdNil(b bool)`

 SetThreatModelIdNil sets the value for ThreatModelId to be an explicit nil

### UnsetThreatModelId
`func (o *WebhookSubscriptionInput) UnsetThreatModelId()`

UnsetThreatModelId ensures that no value is present for ThreatModelId, not even an explicit nil
### GetName

`func (o *WebhookSubscriptionInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *WebhookSubscriptionInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *WebhookSubscriptionInput) SetName(v string)`

SetName sets Name field to given value.


### GetUrl

`func (o *WebhookSubscriptionInput) GetUrl() string`

GetUrl returns the Url field if non-nil, zero value otherwise.

### GetUrlOk

`func (o *WebhookSubscriptionInput) GetUrlOk() (*string, bool)`

GetUrlOk returns a tuple with the Url field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUrl

`func (o *WebhookSubscriptionInput) SetUrl(v string)`

SetUrl sets Url field to given value.


### GetEvents

`func (o *WebhookSubscriptionInput) GetEvents() []string`

GetEvents returns the Events field if non-nil, zero value otherwise.

### GetEventsOk

`func (o *WebhookSubscriptionInput) GetEventsOk() (*[]string, bool)`

GetEventsOk returns a tuple with the Events field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEvents

`func (o *WebhookSubscriptionInput) SetEvents(v []string)`

SetEvents sets Events field to given value.


### GetSecret

`func (o *WebhookSubscriptionInput) GetSecret() string`

GetSecret returns the Secret field if non-nil, zero value otherwise.

### GetSecretOk

`func (o *WebhookSubscriptionInput) GetSecretOk() (*string, bool)`

GetSecretOk returns a tuple with the Secret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecret

`func (o *WebhookSubscriptionInput) SetSecret(v string)`

SetSecret sets Secret field to given value.

### HasSecret

`func (o *WebhookSubscriptionInput) HasSecret() bool`

HasSecret returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


