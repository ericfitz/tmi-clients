# TokenRefreshRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RefreshToken** | Pointer to **string** | Refresh token. Optional: browser SPA clients may omit it and send an empty body, in which case the server reads the refresh token from the HttpOnly refresh cookie. Non-browser clients should supply it in the body. | [optional] 

## Methods

### NewTokenRefreshRequest

`func NewTokenRefreshRequest() *TokenRefreshRequest`

NewTokenRefreshRequest instantiates a new TokenRefreshRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTokenRefreshRequestWithDefaults

`func NewTokenRefreshRequestWithDefaults() *TokenRefreshRequest`

NewTokenRefreshRequestWithDefaults instantiates a new TokenRefreshRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRefreshToken

`func (o *TokenRefreshRequest) GetRefreshToken() string`

GetRefreshToken returns the RefreshToken field if non-nil, zero value otherwise.

### GetRefreshTokenOk

`func (o *TokenRefreshRequest) GetRefreshTokenOk() (*string, bool)`

GetRefreshTokenOk returns a tuple with the RefreshToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefreshToken

`func (o *TokenRefreshRequest) SetRefreshToken(v string)`

SetRefreshToken sets RefreshToken field to given value.

### HasRefreshToken

`func (o *TokenRefreshRequest) HasRefreshToken() bool`

HasRefreshToken returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


