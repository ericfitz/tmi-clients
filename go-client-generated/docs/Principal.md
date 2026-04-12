# Principal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PrincipalType** | **string** | Type of principal: user (individual) or group | 
**Provider** | **string** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;*\&quot; for provider-independent groups. | 
**ProviderId** | **string** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**DisplayName** | Pointer to **string** | Human-readable display name for UI presentation | [optional] 
**Email** | Pointer to **string** | Email address (required for users, optional for groups) | [optional] 

## Methods

### NewPrincipal

`func NewPrincipal(principalType string, provider string, providerId string, ) *Principal`

NewPrincipal instantiates a new Principal object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPrincipalWithDefaults

`func NewPrincipalWithDefaults() *Principal`

NewPrincipalWithDefaults instantiates a new Principal object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrincipalType

`func (o *Principal) GetPrincipalType() string`

GetPrincipalType returns the PrincipalType field if non-nil, zero value otherwise.

### GetPrincipalTypeOk

`func (o *Principal) GetPrincipalTypeOk() (*string, bool)`

GetPrincipalTypeOk returns a tuple with the PrincipalType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrincipalType

`func (o *Principal) SetPrincipalType(v string)`

SetPrincipalType sets PrincipalType field to given value.


### GetProvider

`func (o *Principal) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *Principal) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *Principal) SetProvider(v string)`

SetProvider sets Provider field to given value.


### GetProviderId

`func (o *Principal) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *Principal) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *Principal) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetDisplayName

`func (o *Principal) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *Principal) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *Principal) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.

### HasDisplayName

`func (o *Principal) HasDisplayName() bool`

HasDisplayName returns a boolean if a field has been set.

### GetEmail

`func (o *Principal) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *Principal) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *Principal) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *Principal) HasEmail() bool`

HasEmail returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


