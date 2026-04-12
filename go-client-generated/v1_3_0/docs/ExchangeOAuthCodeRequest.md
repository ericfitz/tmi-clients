# ExchangeOAuthCodeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**GrantType** | **string** | OAuth 2.0 grant type (RFC 6749) | 
**Code** | Pointer to **NullableString** | Authorization code received from OAuth provider. Per RFC 6749, can contain any visible ASCII characters (VSCHAR: 0x20-0x7E). | [optional] 
**State** | Pointer to **NullableString** | State parameter for CSRF protection (optional but recommended) | [optional] 
**RedirectUri** | Pointer to **NullableString** | Redirect URI used in the authorization request (must match exactly) | [optional] 
**CodeVerifier** | Pointer to **NullableString** | PKCE code verifier (RFC 7636) - High-entropy cryptographic random string used to mitigate authorization code interception attacks. Must be 43-128 characters using [A-Za-z0-9-._~] characters. | [optional] 
**ClientId** | Pointer to **NullableString** | Client identifier (required for client_credentials grant) | [optional] 
**ClientSecret** | Pointer to **NullableString** | Client secret (required for client_credentials grant) | [optional] 
**RefreshToken** | Pointer to **NullableString** | Refresh token (required for refresh_token grant) | [optional] 

## Methods

### NewExchangeOAuthCodeRequest

`func NewExchangeOAuthCodeRequest(grantType string, ) *ExchangeOAuthCodeRequest`

NewExchangeOAuthCodeRequest instantiates a new ExchangeOAuthCodeRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExchangeOAuthCodeRequestWithDefaults

`func NewExchangeOAuthCodeRequestWithDefaults() *ExchangeOAuthCodeRequest`

NewExchangeOAuthCodeRequestWithDefaults instantiates a new ExchangeOAuthCodeRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetGrantType

`func (o *ExchangeOAuthCodeRequest) GetGrantType() string`

GetGrantType returns the GrantType field if non-nil, zero value otherwise.

### GetGrantTypeOk

`func (o *ExchangeOAuthCodeRequest) GetGrantTypeOk() (*string, bool)`

GetGrantTypeOk returns a tuple with the GrantType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantType

`func (o *ExchangeOAuthCodeRequest) SetGrantType(v string)`

SetGrantType sets GrantType field to given value.


### GetCode

`func (o *ExchangeOAuthCodeRequest) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ExchangeOAuthCodeRequest) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ExchangeOAuthCodeRequest) SetCode(v string)`

SetCode sets Code field to given value.

### HasCode

`func (o *ExchangeOAuthCodeRequest) HasCode() bool`

HasCode returns a boolean if a field has been set.

### SetCodeNil

`func (o *ExchangeOAuthCodeRequest) SetCodeNil(b bool)`

 SetCodeNil sets the value for Code to be an explicit nil

### UnsetCode
`func (o *ExchangeOAuthCodeRequest) UnsetCode()`

UnsetCode ensures that no value is present for Code, not even an explicit nil
### GetState

`func (o *ExchangeOAuthCodeRequest) GetState() string`

GetState returns the State field if non-nil, zero value otherwise.

### GetStateOk

`func (o *ExchangeOAuthCodeRequest) GetStateOk() (*string, bool)`

GetStateOk returns a tuple with the State field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetState

`func (o *ExchangeOAuthCodeRequest) SetState(v string)`

SetState sets State field to given value.

### HasState

`func (o *ExchangeOAuthCodeRequest) HasState() bool`

HasState returns a boolean if a field has been set.

### SetStateNil

`func (o *ExchangeOAuthCodeRequest) SetStateNil(b bool)`

 SetStateNil sets the value for State to be an explicit nil

### UnsetState
`func (o *ExchangeOAuthCodeRequest) UnsetState()`

UnsetState ensures that no value is present for State, not even an explicit nil
### GetRedirectUri

`func (o *ExchangeOAuthCodeRequest) GetRedirectUri() string`

GetRedirectUri returns the RedirectUri field if non-nil, zero value otherwise.

### GetRedirectUriOk

`func (o *ExchangeOAuthCodeRequest) GetRedirectUriOk() (*string, bool)`

GetRedirectUriOk returns a tuple with the RedirectUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUri

`func (o *ExchangeOAuthCodeRequest) SetRedirectUri(v string)`

SetRedirectUri sets RedirectUri field to given value.

### HasRedirectUri

`func (o *ExchangeOAuthCodeRequest) HasRedirectUri() bool`

HasRedirectUri returns a boolean if a field has been set.

### SetRedirectUriNil

`func (o *ExchangeOAuthCodeRequest) SetRedirectUriNil(b bool)`

 SetRedirectUriNil sets the value for RedirectUri to be an explicit nil

### UnsetRedirectUri
`func (o *ExchangeOAuthCodeRequest) UnsetRedirectUri()`

UnsetRedirectUri ensures that no value is present for RedirectUri, not even an explicit nil
### GetCodeVerifier

`func (o *ExchangeOAuthCodeRequest) GetCodeVerifier() string`

GetCodeVerifier returns the CodeVerifier field if non-nil, zero value otherwise.

### GetCodeVerifierOk

`func (o *ExchangeOAuthCodeRequest) GetCodeVerifierOk() (*string, bool)`

GetCodeVerifierOk returns a tuple with the CodeVerifier field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeVerifier

`func (o *ExchangeOAuthCodeRequest) SetCodeVerifier(v string)`

SetCodeVerifier sets CodeVerifier field to given value.

### HasCodeVerifier

`func (o *ExchangeOAuthCodeRequest) HasCodeVerifier() bool`

HasCodeVerifier returns a boolean if a field has been set.

### SetCodeVerifierNil

`func (o *ExchangeOAuthCodeRequest) SetCodeVerifierNil(b bool)`

 SetCodeVerifierNil sets the value for CodeVerifier to be an explicit nil

### UnsetCodeVerifier
`func (o *ExchangeOAuthCodeRequest) UnsetCodeVerifier()`

UnsetCodeVerifier ensures that no value is present for CodeVerifier, not even an explicit nil
### GetClientId

`func (o *ExchangeOAuthCodeRequest) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *ExchangeOAuthCodeRequest) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *ExchangeOAuthCodeRequest) SetClientId(v string)`

SetClientId sets ClientId field to given value.

### HasClientId

`func (o *ExchangeOAuthCodeRequest) HasClientId() bool`

HasClientId returns a boolean if a field has been set.

### SetClientIdNil

`func (o *ExchangeOAuthCodeRequest) SetClientIdNil(b bool)`

 SetClientIdNil sets the value for ClientId to be an explicit nil

### UnsetClientId
`func (o *ExchangeOAuthCodeRequest) UnsetClientId()`

UnsetClientId ensures that no value is present for ClientId, not even an explicit nil
### GetClientSecret

`func (o *ExchangeOAuthCodeRequest) GetClientSecret() string`

GetClientSecret returns the ClientSecret field if non-nil, zero value otherwise.

### GetClientSecretOk

`func (o *ExchangeOAuthCodeRequest) GetClientSecretOk() (*string, bool)`

GetClientSecretOk returns a tuple with the ClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientSecret

`func (o *ExchangeOAuthCodeRequest) SetClientSecret(v string)`

SetClientSecret sets ClientSecret field to given value.

### HasClientSecret

`func (o *ExchangeOAuthCodeRequest) HasClientSecret() bool`

HasClientSecret returns a boolean if a field has been set.

### SetClientSecretNil

`func (o *ExchangeOAuthCodeRequest) SetClientSecretNil(b bool)`

 SetClientSecretNil sets the value for ClientSecret to be an explicit nil

### UnsetClientSecret
`func (o *ExchangeOAuthCodeRequest) UnsetClientSecret()`

UnsetClientSecret ensures that no value is present for ClientSecret, not even an explicit nil
### GetRefreshToken

`func (o *ExchangeOAuthCodeRequest) GetRefreshToken() string`

GetRefreshToken returns the RefreshToken field if non-nil, zero value otherwise.

### GetRefreshTokenOk

`func (o *ExchangeOAuthCodeRequest) GetRefreshTokenOk() (*string, bool)`

GetRefreshTokenOk returns a tuple with the RefreshToken field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefreshToken

`func (o *ExchangeOAuthCodeRequest) SetRefreshToken(v string)`

SetRefreshToken sets RefreshToken field to given value.

### HasRefreshToken

`func (o *ExchangeOAuthCodeRequest) HasRefreshToken() bool`

HasRefreshToken returns a boolean if a field has been set.

### SetRefreshTokenNil

`func (o *ExchangeOAuthCodeRequest) SetRefreshTokenNil(b bool)`

 SetRefreshTokenNil sets the value for RefreshToken to be an explicit nil

### UnsetRefreshToken
`func (o *ExchangeOAuthCodeRequest) UnsetRefreshToken()`

UnsetRefreshToken ensures that no value is present for RefreshToken, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


