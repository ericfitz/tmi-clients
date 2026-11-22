# IdentityLinkStartResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**LinkState** | **string** | Opaque state identifier for the link flow | 
**AuthorizationUrl** | **string** | URL to redirect the user to for identity provider authorization (prompt&#x3D;select_account) | 
**ExpiresAt** | **time.Time** | When the link state expires (10 minutes from creation) | 

## Methods

### NewIdentityLinkStartResponse

`func NewIdentityLinkStartResponse(linkState string, authorizationUrl string, expiresAt time.Time, ) *IdentityLinkStartResponse`

NewIdentityLinkStartResponse instantiates a new IdentityLinkStartResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIdentityLinkStartResponseWithDefaults

`func NewIdentityLinkStartResponseWithDefaults() *IdentityLinkStartResponse`

NewIdentityLinkStartResponseWithDefaults instantiates a new IdentityLinkStartResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetLinkState

`func (o *IdentityLinkStartResponse) GetLinkState() string`

GetLinkState returns the LinkState field if non-nil, zero value otherwise.

### GetLinkStateOk

`func (o *IdentityLinkStartResponse) GetLinkStateOk() (*string, bool)`

GetLinkStateOk returns a tuple with the LinkState field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkState

`func (o *IdentityLinkStartResponse) SetLinkState(v string)`

SetLinkState sets LinkState field to given value.


### GetAuthorizationUrl

`func (o *IdentityLinkStartResponse) GetAuthorizationUrl() string`

GetAuthorizationUrl returns the AuthorizationUrl field if non-nil, zero value otherwise.

### GetAuthorizationUrlOk

`func (o *IdentityLinkStartResponse) GetAuthorizationUrlOk() (*string, bool)`

GetAuthorizationUrlOk returns a tuple with the AuthorizationUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationUrl

`func (o *IdentityLinkStartResponse) SetAuthorizationUrl(v string)`

SetAuthorizationUrl sets AuthorizationUrl field to given value.


### GetExpiresAt

`func (o *IdentityLinkStartResponse) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *IdentityLinkStartResponse) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *IdentityLinkStartResponse) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


