# PendingIdentityLinkResponseAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Provider** | **string** | Primary identity provider of this TMI account | 
**Email** | **string** | Email address of this TMI account | 

## Methods

### NewPendingIdentityLinkResponseAccount

`func NewPendingIdentityLinkResponseAccount(provider string, email string, ) *PendingIdentityLinkResponseAccount`

NewPendingIdentityLinkResponseAccount instantiates a new PendingIdentityLinkResponseAccount object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPendingIdentityLinkResponseAccountWithDefaults

`func NewPendingIdentityLinkResponseAccountWithDefaults() *PendingIdentityLinkResponseAccount`

NewPendingIdentityLinkResponseAccountWithDefaults instantiates a new PendingIdentityLinkResponseAccount object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProvider

`func (o *PendingIdentityLinkResponseAccount) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *PendingIdentityLinkResponseAccount) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *PendingIdentityLinkResponseAccount) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetEmail

`func (o *PendingIdentityLinkResponseAccount) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *PendingIdentityLinkResponseAccount) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *PendingIdentityLinkResponseAccount) SetEmail(v string)`

SetEmail sets Email field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


