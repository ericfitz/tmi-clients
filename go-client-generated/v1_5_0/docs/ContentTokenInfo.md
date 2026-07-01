# ContentTokenInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ProviderId** | **string** | Content OAuth provider id (e.g., &#39;confluence&#39;). | 
**ProviderAccountId** | Pointer to **string** | External account identifier reported by the provider. May be empty if the provider has no stable id. | [optional] 
**ProviderAccountLabel** | Pointer to **string** | Human-readable account label (email or username) for display. | [optional] 
**Scopes** | **[]string** | OAuth scopes granted to the stored token. | 
**Status** | **string** | Current health of the stored token. &#39;failed_refresh&#39; indicates the most recent refresh attempt failed and the user must re-link. | 
**ExpiresAt** | Pointer to **time.Time** | Access-token expiry reported by the provider (ISO 8601). | [optional] 
**LastRefreshAt** | Pointer to **time.Time** | Timestamp of the most recent successful refresh (ISO 8601). | [optional] 
**CreatedAt** | **time.Time** | Creation timestamp for this linked token (ISO 8601). | 

## Methods

### NewContentTokenInfo

`func NewContentTokenInfo(providerId string, scopes []string, status string, createdAt time.Time, ) *ContentTokenInfo`

NewContentTokenInfo instantiates a new ContentTokenInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentTokenInfoWithDefaults

`func NewContentTokenInfoWithDefaults() *ContentTokenInfo`

NewContentTokenInfoWithDefaults instantiates a new ContentTokenInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetProviderId

`func (o *ContentTokenInfo) GetProviderId() string`

GetProviderId returns the ProviderId field if non-nil, zero value otherwise.

### GetProviderIdOk

`func (o *ContentTokenInfo) GetProviderIdOk() (*string, bool)`

GetProviderIdOk returns a tuple with the ProviderId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderId

`func (o *ContentTokenInfo) SetProviderId(v string)`

SetProviderId sets ProviderId field to given value.


### GetProviderAccountId

`func (o *ContentTokenInfo) GetProviderAccountId() string`

GetProviderAccountId returns the ProviderAccountId field if non-nil, zero value otherwise.

### GetProviderAccountIdOk

`func (o *ContentTokenInfo) GetProviderAccountIdOk() (*string, bool)`

GetProviderAccountIdOk returns a tuple with the ProviderAccountId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderAccountId

`func (o *ContentTokenInfo) SetProviderAccountId(v string)`

SetProviderAccountId sets ProviderAccountId field to given value.

### HasProviderAccountId

`func (o *ContentTokenInfo) HasProviderAccountId() bool`

HasProviderAccountId returns a boolean if a field has been set.

### GetProviderAccountLabel

`func (o *ContentTokenInfo) GetProviderAccountLabel() string`

GetProviderAccountLabel returns the ProviderAccountLabel field if non-nil, zero value otherwise.

### GetProviderAccountLabelOk

`func (o *ContentTokenInfo) GetProviderAccountLabelOk() (*string, bool)`

GetProviderAccountLabelOk returns a tuple with the ProviderAccountLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderAccountLabel

`func (o *ContentTokenInfo) SetProviderAccountLabel(v string)`

SetProviderAccountLabel sets ProviderAccountLabel field to given value.

### HasProviderAccountLabel

`func (o *ContentTokenInfo) HasProviderAccountLabel() bool`

HasProviderAccountLabel returns a boolean if a field has been set.

### GetScopes

`func (o *ContentTokenInfo) GetScopes() []string`

GetScopes returns the Scopes field if non-nil, zero value otherwise.

### GetScopesOk

`func (o *ContentTokenInfo) GetScopesOk() (*[]string, bool)`

GetScopesOk returns a tuple with the Scopes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopes

`func (o *ContentTokenInfo) SetScopes(v []string)`

SetScopes sets Scopes field to given value.


### GetStatus

`func (o *ContentTokenInfo) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ContentTokenInfo) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ContentTokenInfo) SetStatus(v string)`

SetStatus sets Status field to given value.


### GetExpiresAt

`func (o *ContentTokenInfo) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *ContentTokenInfo) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *ContentTokenInfo) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.

### HasExpiresAt

`func (o *ContentTokenInfo) HasExpiresAt() bool`

HasExpiresAt returns a boolean if a field has been set.

### GetLastRefreshAt

`func (o *ContentTokenInfo) GetLastRefreshAt() time.Time`

GetLastRefreshAt returns the LastRefreshAt field if non-nil, zero value otherwise.

### GetLastRefreshAtOk

`func (o *ContentTokenInfo) GetLastRefreshAtOk() (*time.Time, bool)`

GetLastRefreshAtOk returns a tuple with the LastRefreshAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastRefreshAt

`func (o *ContentTokenInfo) SetLastRefreshAt(v time.Time)`

SetLastRefreshAt sets LastRefreshAt field to given value.

### HasLastRefreshAt

`func (o *ContentTokenInfo) HasLastRefreshAt() bool`

HasLastRefreshAt returns a boolean if a field has been set.

### GetCreatedAt

`func (o *ContentTokenInfo) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ContentTokenInfo) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ContentTokenInfo) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


