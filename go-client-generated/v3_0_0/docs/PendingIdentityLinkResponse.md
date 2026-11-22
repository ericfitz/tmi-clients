# PendingIdentityLinkResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Pending** | [**PendingIdentityLinkResponsePending**](PendingIdentityLinkResponsePending.md) |  | 
**Account** | [**PendingIdentityLinkResponseAccount**](PendingIdentityLinkResponseAccount.md) |  | 

## Methods

### NewPendingIdentityLinkResponse

`func NewPendingIdentityLinkResponse(pending PendingIdentityLinkResponsePending, account PendingIdentityLinkResponseAccount, ) *PendingIdentityLinkResponse`

NewPendingIdentityLinkResponse instantiates a new PendingIdentityLinkResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPendingIdentityLinkResponseWithDefaults

`func NewPendingIdentityLinkResponseWithDefaults() *PendingIdentityLinkResponse`

NewPendingIdentityLinkResponseWithDefaults instantiates a new PendingIdentityLinkResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPending

`func (o *PendingIdentityLinkResponse) GetPending() PendingIdentityLinkResponsePending`

GetPending returns the Pending field if non-nil, zero value otherwise.

### GetPendingOk

`func (o *PendingIdentityLinkResponse) GetPendingOk() (*PendingIdentityLinkResponsePending, bool)`

GetPendingOk returns a tuple with the Pending field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPending

`func (o *PendingIdentityLinkResponse) SetPending(v PendingIdentityLinkResponsePending)`

SetPending sets Pending field to given value.


### GetAccount

`func (o *PendingIdentityLinkResponse) GetAccount() PendingIdentityLinkResponseAccount`

GetAccount returns the Account field if non-nil, zero value otherwise.

### GetAccountOk

`func (o *PendingIdentityLinkResponse) GetAccountOk() (*PendingIdentityLinkResponseAccount, bool)`

GetAccountOk returns a tuple with the Account field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccount

`func (o *PendingIdentityLinkResponse) SetAccount(v PendingIdentityLinkResponseAccount)`

SetAccount sets Account field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


