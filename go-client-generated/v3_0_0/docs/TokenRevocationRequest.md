# TokenRevocationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Token** | **string** | The token to be revoked (access token or refresh token) | 
**TokenTypeHint** | Pointer to **NullableString** | A hint about the type of the token. If omitted, the server will attempt to determine the token type. | [optional] 
**ClientId** | Pointer to **NullableString** | Client identifier for client credentials authentication (alternative to Bearer token) | [optional] 
**ClientSecret** | Pointer to **NullableString** | Client secret (required if client_id is provided) | [optional] 

## Methods

### NewTokenRevocationRequest

`func NewTokenRevocationRequest(token string, ) *TokenRevocationRequest`

NewTokenRevocationRequest instantiates a new TokenRevocationRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewTokenRevocationRequestWithDefaults

`func NewTokenRevocationRequestWithDefaults() *TokenRevocationRequest`

NewTokenRevocationRequestWithDefaults instantiates a new TokenRevocationRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetToken

`func (o *TokenRevocationRequest) GetToken() string`

GetToken returns the Token field if non-nil, zero value otherwise.

### GetTokenOk

`func (o *TokenRevocationRequest) GetTokenOk() (*string, bool)`

GetTokenOk returns a tuple with the Token field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetToken

`func (o *TokenRevocationRequest) SetToken(v string)`

SetToken sets Token field to given value.


### GetTokenTypeHint

`func (o *TokenRevocationRequest) GetTokenTypeHint() string`

GetTokenTypeHint returns the TokenTypeHint field if non-nil, zero value otherwise.

### GetTokenTypeHintOk

`func (o *TokenRevocationRequest) GetTokenTypeHintOk() (*string, bool)`

GetTokenTypeHintOk returns a tuple with the TokenTypeHint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenTypeHint

`func (o *TokenRevocationRequest) SetTokenTypeHint(v string)`

SetTokenTypeHint sets TokenTypeHint field to given value.

### HasTokenTypeHint

`func (o *TokenRevocationRequest) HasTokenTypeHint() bool`

HasTokenTypeHint returns a boolean if a field has been set.

### SetTokenTypeHintNil

`func (o *TokenRevocationRequest) SetTokenTypeHintNil(b bool)`

 SetTokenTypeHintNil sets the value for TokenTypeHint to be an explicit nil

### UnsetTokenTypeHint
`func (o *TokenRevocationRequest) UnsetTokenTypeHint()`

UnsetTokenTypeHint ensures that no value is present for TokenTypeHint, not even an explicit nil
### GetClientId

`func (o *TokenRevocationRequest) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *TokenRevocationRequest) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *TokenRevocationRequest) SetClientId(v string)`

SetClientId sets ClientId field to given value.

### HasClientId

`func (o *TokenRevocationRequest) HasClientId() bool`

HasClientId returns a boolean if a field has been set.

### SetClientIdNil

`func (o *TokenRevocationRequest) SetClientIdNil(b bool)`

 SetClientIdNil sets the value for ClientId to be an explicit nil

### UnsetClientId
`func (o *TokenRevocationRequest) UnsetClientId()`

UnsetClientId ensures that no value is present for ClientId, not even an explicit nil
### GetClientSecret

`func (o *TokenRevocationRequest) GetClientSecret() string`

GetClientSecret returns the ClientSecret field if non-nil, zero value otherwise.

### GetClientSecretOk

`func (o *TokenRevocationRequest) GetClientSecretOk() (*string, bool)`

GetClientSecretOk returns a tuple with the ClientSecret field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientSecret

`func (o *TokenRevocationRequest) SetClientSecret(v string)`

SetClientSecret sets ClientSecret field to given value.

### HasClientSecret

`func (o *TokenRevocationRequest) HasClientSecret() bool`

HasClientSecret returns a boolean if a field has been set.

### SetClientSecretNil

`func (o *TokenRevocationRequest) SetClientSecretNil(b bool)`

 SetClientSecretNil sets the value for ClientSecret to be an explicit nil

### UnsetClientSecret
`func (o *TokenRevocationRequest) UnsetClientSecret()`

UnsetClientSecret ensures that no value is present for ClientSecret, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


