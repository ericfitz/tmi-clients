# PickerTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**AccessToken** | **string** | Short-lived OAuth access token, scoped to the picker session. | 
**ExpiresAt** | **time.Time** | Token expiration timestamp (RFC3339). | 
**DeveloperKey** | Pointer to **string** | Google Picker developer key. Deprecated — prefer provider_config.developer_key. Populated only for provider_id&#x3D;google_workspace. | [optional] 
**AppId** | Pointer to **string** | Google Cloud app id. Deprecated — prefer provider_config.app_id. Populated only for provider_id&#x3D;google_workspace. | [optional] 
**ProviderConfig** | Pointer to **map[string]string** | Provider-specific public configuration values for picker initialization. Keys vary by provider — see provider documentation. For google_workspace: developer_key, app_id. For microsoft: client_id, tenant_id, picker_origin. | [optional] 

## Methods

### NewPickerTokenResponse

`func NewPickerTokenResponse(accessToken string, expiresAt time.Time, ) *PickerTokenResponse`

NewPickerTokenResponse instantiates a new PickerTokenResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPickerTokenResponseWithDefaults

`func NewPickerTokenResponseWithDefaults() *PickerTokenResponse`

NewPickerTokenResponseWithDefaults instantiates a new PickerTokenResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAccessToken

`func (o *PickerTokenResponse) GetAccessToken() string`

GetAccessToken returns the AccessToken field if non-nil, zero value otherwise.

### GetAccessTokenOk

`func (o *PickerTokenResponse) GetAccessTokenOk() (*string, bool)`

GetAccessTokenOk returns a tuple with the AccessToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessToken

`func (o *PickerTokenResponse) SetAccessToken(v string)`

SetAccessToken sets AccessToken field to given value.


### GetExpiresAt

`func (o *PickerTokenResponse) GetExpiresAt() time.Time`

GetExpiresAt returns the ExpiresAt field if non-nil, zero value otherwise.

### GetExpiresAtOk

`func (o *PickerTokenResponse) GetExpiresAtOk() (*time.Time, bool)`

GetExpiresAtOk returns a tuple with the ExpiresAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpiresAt

`func (o *PickerTokenResponse) SetExpiresAt(v time.Time)`

SetExpiresAt sets ExpiresAt field to given value.


### GetDeveloperKey

`func (o *PickerTokenResponse) GetDeveloperKey() string`

GetDeveloperKey returns the DeveloperKey field if non-nil, zero value otherwise.

### GetDeveloperKeyOk

`func (o *PickerTokenResponse) GetDeveloperKeyOk() (*string, bool)`

GetDeveloperKeyOk returns a tuple with the DeveloperKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeveloperKey

`func (o *PickerTokenResponse) SetDeveloperKey(v string)`

SetDeveloperKey sets DeveloperKey field to given value.

### HasDeveloperKey

`func (o *PickerTokenResponse) HasDeveloperKey() bool`

HasDeveloperKey returns a boolean if a field has been set.

### GetAppId

`func (o *PickerTokenResponse) GetAppId() string`

GetAppId returns the AppId field if non-nil, zero value otherwise.

### GetAppIdOk

`func (o *PickerTokenResponse) GetAppIdOk() (*string, bool)`

GetAppIdOk returns a tuple with the AppId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAppId

`func (o *PickerTokenResponse) SetAppId(v string)`

SetAppId sets AppId field to given value.

### HasAppId

`func (o *PickerTokenResponse) HasAppId() bool`

HasAppId returns a boolean if a field has been set.

### GetProviderConfig

`func (o *PickerTokenResponse) GetProviderConfig() map[string]string`

GetProviderConfig returns the ProviderConfig field if non-nil, zero value otherwise.

### GetProviderConfigOk

`func (o *PickerTokenResponse) GetProviderConfigOk() (*map[string]string, bool)`

GetProviderConfigOk returns a tuple with the ProviderConfig field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProviderConfig

`func (o *PickerTokenResponse) SetProviderConfig(v map[string]string)`

SetProviderConfig sets ProviderConfig field to given value.

### HasProviderConfig

`func (o *PickerTokenResponse) HasProviderConfig() bool`

HasProviderConfig returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


