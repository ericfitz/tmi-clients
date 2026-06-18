# PendingIdentityLinkResponsePending

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **string** | Identity provider of the second identity | 
**ProviderUserId** | **string** | User identifier at the provider (first 8 chars + ellipsis) | 
**Email** | Pointer to **string** | Cached email from the second identity (display only) | [optional] 
**Name** | Pointer to **string** | Cached display name from the second identity | [optional] 

## Methods

### NewPendingIdentityLinkResponsePending

`func NewPendingIdentityLinkResponsePending(provider string, providerUserId string, ) *PendingIdentityLinkResponsePending`

NewPendingIdentityLinkResponsePending instantiates a new PendingIdentityLinkResponsePending object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPendingIdentityLinkResponsePendingWithDefaults

`func NewPendingIdentityLinkResponsePendingWithDefaults() *PendingIdentityLinkResponsePending`

NewPendingIdentityLinkResponsePendingWithDefaults instantiates a new PendingIdentityLinkResponsePending object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProvider

`func (o *PendingIdentityLinkResponsePending) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *PendingIdentityLinkResponsePending) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *PendingIdentityLinkResponsePending) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderUserId

`func (o *PendingIdentityLinkResponsePending) GetProviderUserId() string`

GetProviderUserId returns the ProviderUserId field if non-nil, zero value otherwise.

### GetProviderUserIdOk

`func (o *PendingIdentityLinkResponsePending) GetProviderUserIdOk() (*string, bool)`

GetProviderUserIdOk returns a tuple with the ProviderUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderUserId

`func (o *PendingIdentityLinkResponsePending) SetProviderUserId(v string)`

SetProviderUserId sets ProviderUserId field to given value.


### GetEmail

`func (o *PendingIdentityLinkResponsePending) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *PendingIdentityLinkResponsePending) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *PendingIdentityLinkResponsePending) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *PendingIdentityLinkResponsePending) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *PendingIdentityLinkResponsePending) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *PendingIdentityLinkResponsePending) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *PendingIdentityLinkResponsePending) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *PendingIdentityLinkResponsePending) HasName() bool`

HasName returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


