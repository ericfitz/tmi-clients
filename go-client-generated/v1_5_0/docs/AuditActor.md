# AuditActor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **string** | User email at the time of the action | 
**Provider** | **string** | Identity provider (e.g., google, github, tmi) | 
**ProviderId** | **string** | Provider-specific user identifier | 
**DisplayName** | **string** | User display name at the time of the action | 

## Methods

### NewAuditActor

`func NewAuditActor(email string, provider string, providerId string, displayName string, ) *AuditActor`

NewAuditActor instantiates a new AuditActor object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuditActorWithDefaults

`func NewAuditActorWithDefaults() *AuditActor`

NewAuditActorWithDefaults instantiates a new AuditActor object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *AuditActor) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *AuditActor) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *AuditActor) SetEmail(v string)`

SetEmail sets Email field to given value.


### GetProvider

`func (o *AuditActor) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *AuditActor) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *AuditActor) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderId

`func (o *AuditActor) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *AuditActor) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *AuditActor) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetDisplayName

`func (o *AuditActor) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *AuditActor) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *AuditActor) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


