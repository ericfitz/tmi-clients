# LinkedIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Linked identity unique identifier | 
**Provider** | **string** | Identity provider ID | 
**ProviderUserId** | **string** | User identifier at the provider (truncated for display) | 
**Email** | Pointer to **string** | Cached email address from provider (display only) | [optional] 
**Name** | Pointer to **string** | Cached display name from provider | [optional] 
**LinkedAt** | **time.Time** | When this identity was linked | 
**LastUsedAt** | Pointer to **NullableTime** | When this identity was last used to sign in | [optional] 

## Methods

### NewLinkedIdentity

`func NewLinkedIdentity(id string, provider string, providerUserId string, linkedAt time.Time, ) *LinkedIdentity`

NewLinkedIdentity instantiates a new LinkedIdentity object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewLinkedIdentityWithDefaults

`func NewLinkedIdentityWithDefaults() *LinkedIdentity`

NewLinkedIdentityWithDefaults instantiates a new LinkedIdentity object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *LinkedIdentity) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *LinkedIdentity) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *LinkedIdentity) SetId(v string)`

SetId sets Id field to given value.


### GetProvider

`func (o *LinkedIdentity) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *LinkedIdentity) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *LinkedIdentity) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderUserId

`func (o *LinkedIdentity) GetProviderUserId() string`

GetProviderUserId returns the ProviderUserId field if non-nil, zero value otherwise.

### GetProviderUserIdOk

`func (o *LinkedIdentity) GetProviderUserIdOk() (*string, bool)`

GetProviderUserIdOk returns a tuple with the ProviderUserId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderUserId

`func (o *LinkedIdentity) SetProviderUserId(v string)`

SetProviderUserId sets ProviderUserId field to given value.


### GetEmail

`func (o *LinkedIdentity) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *LinkedIdentity) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *LinkedIdentity) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *LinkedIdentity) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### GetName

`func (o *LinkedIdentity) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *LinkedIdentity) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *LinkedIdentity) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *LinkedIdentity) HasName() bool`

HasName returns a boolean if a field has been set.

### GetLinkedAt

`func (o *LinkedIdentity) GetLinkedAt() time.Time`

GetLinkedAt returns the LinkedAt field if non-nil, zero value otherwise.

### GetLinkedAtOk

`func (o *LinkedIdentity) GetLinkedAtOk() (*time.Time, bool)`

GetLinkedAtOk returns a tuple with the LinkedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinkedAt

`func (o *LinkedIdentity) SetLinkedAt(v time.Time)`

SetLinkedAt sets LinkedAt field to given value.


### GetLastUsedAt

`func (o *LinkedIdentity) GetLastUsedAt() time.Time`

GetLastUsedAt returns the LastUsedAt field if non-nil, zero value otherwise.

### GetLastUsedAtOk

`func (o *LinkedIdentity) GetLastUsedAtOk() (*time.Time, bool)`

GetLastUsedAtOk returns a tuple with the LastUsedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastUsedAt

`func (o *LinkedIdentity) SetLastUsedAt(v time.Time)`

SetLastUsedAt sets LastUsedAt field to given value.

### HasLastUsedAt

`func (o *LinkedIdentity) HasLastUsedAt() bool`

HasLastUsedAt returns a boolean if a field has been set.

### SetLastUsedAtNil

`func (o *LinkedIdentity) SetLastUsedAtNil(b bool)`

 SetLastUsedAtNil sets the value for LastUsedAt to be an explicit nil

### UnsetLastUsedAt
`func (o *LinkedIdentity) UnsetLastUsedAt()`

UnsetLastUsedAt ensures that no value is present for LastUsedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


