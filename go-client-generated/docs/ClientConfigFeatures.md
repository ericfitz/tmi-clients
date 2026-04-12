# ClientConfigFeatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WebsocketEnabled** | Pointer to **bool** | Whether WebSocket collaboration is enabled | [optional] 
**SamlEnabled** | Pointer to **bool** | Whether SAML authentication is enabled | [optional] 
**WebhooksEnabled** | Pointer to **bool** | Whether webhook subscriptions are enabled | [optional] 

## Methods

### NewClientConfigFeatures

`func NewClientConfigFeatures() *ClientConfigFeatures`

NewClientConfigFeatures instantiates a new ClientConfigFeatures object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewClientConfigFeaturesWithDefaults

`func NewClientConfigFeaturesWithDefaults() *ClientConfigFeatures`

NewClientConfigFeaturesWithDefaults instantiates a new ClientConfigFeatures object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWebsocketEnabled

`func (o *ClientConfigFeatures) GetWebsocketEnabled() bool`

GetWebsocketEnabled returns the WebsocketEnabled field if non-nil, zero value otherwise.

### GetWebsocketEnabledOk

`func (o *ClientConfigFeatures) GetWebsocketEnabledOk() (*bool, bool)`

GetWebsocketEnabledOk returns a tuple with the WebsocketEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebsocketEnabled

`func (o *ClientConfigFeatures) SetWebsocketEnabled(v bool)`

SetWebsocketEnabled sets WebsocketEnabled field to given value.

### HasWebsocketEnabled

`func (o *ClientConfigFeatures) HasWebsocketEnabled() bool`

HasWebsocketEnabled returns a boolean if a field has been set.

### GetSamlEnabled

`func (o *ClientConfigFeatures) GetSamlEnabled() bool`

GetSamlEnabled returns the SamlEnabled field if non-nil, zero value otherwise.

### GetSamlEnabledOk

`func (o *ClientConfigFeatures) GetSamlEnabledOk() (*bool, bool)`

GetSamlEnabledOk returns a tuple with the SamlEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSamlEnabled

`func (o *ClientConfigFeatures) SetSamlEnabled(v bool)`

SetSamlEnabled sets SamlEnabled field to given value.

### HasSamlEnabled

`func (o *ClientConfigFeatures) HasSamlEnabled() bool`

HasSamlEnabled returns a boolean if a field has been set.

### GetWebhooksEnabled

`func (o *ClientConfigFeatures) GetWebhooksEnabled() bool`

GetWebhooksEnabled returns the WebhooksEnabled field if non-nil, zero value otherwise.

### GetWebhooksEnabledOk

`func (o *ClientConfigFeatures) GetWebhooksEnabledOk() (*bool, bool)`

GetWebhooksEnabledOk returns a tuple with the WebhooksEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhooksEnabled

`func (o *ClientConfigFeatures) SetWebhooksEnabled(v bool)`

SetWebhooksEnabled sets WebhooksEnabled field to given value.

### HasWebhooksEnabled

`func (o *ClientConfigFeatures) HasWebhooksEnabled() bool`

HasWebhooksEnabled returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


