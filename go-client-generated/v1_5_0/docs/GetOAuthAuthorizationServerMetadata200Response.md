# GetOAuthAuthorizationServerMetadata200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Issuer** | **string** |  | 
**AuthorizationEndpoint** | **string** |  | 
**TokenEndpoint** | **string** |  | 
**IntrospectionEndpoint** | Pointer to **string** |  | [optional] 
**ResponseTypesSupported** | **[]string** |  | 
**GrantTypesSupported** | Pointer to **[]string** |  | [optional] 
**TokenEndpointAuthMethodsSupported** | Pointer to **[]string** |  | [optional] 
**CodeChallengeMethodsSupported** | Pointer to **[]string** |  | [optional] 
**JwksUri** | Pointer to **string** |  | [optional] 
**RevocationEndpoint** | Pointer to **string** |  | [optional] 
**ScopesSupported** | Pointer to **[]string** |  | [optional] 

## Methods

### NewGetOAuthAuthorizationServerMetadata200Response

`func NewGetOAuthAuthorizationServerMetadata200Response(issuer string, authorizationEndpoint string, tokenEndpoint string, responseTypesSupported []string, ) *GetOAuthAuthorizationServerMetadata200Response`

NewGetOAuthAuthorizationServerMetadata200Response instantiates a new GetOAuthAuthorizationServerMetadata200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOAuthAuthorizationServerMetadata200ResponseWithDefaults

`func NewGetOAuthAuthorizationServerMetadata200ResponseWithDefaults() *GetOAuthAuthorizationServerMetadata200Response`

NewGetOAuthAuthorizationServerMetadata200ResponseWithDefaults instantiates a new GetOAuthAuthorizationServerMetadata200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIssuer

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetIssuer() string`

GetIssuer returns the Issuer field if non-nil, zero value otherwise.

### GetIssuerOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetIssuerOk() (*string, bool)`

GetIssuerOk returns a tuple with the Issuer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssuer

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetIssuer(v string)`

SetIssuer sets Issuer field to given value.


### GetAuthorizationEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetAuthorizationEndpoint() string`

GetAuthorizationEndpoint returns the AuthorizationEndpoint field if non-nil, zero value otherwise.

### GetAuthorizationEndpointOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetAuthorizationEndpointOk() (*string, bool)`

GetAuthorizationEndpointOk returns a tuple with the AuthorizationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetAuthorizationEndpoint(v string)`

SetAuthorizationEndpoint sets AuthorizationEndpoint field to given value.


### GetTokenEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetTokenEndpoint() string`

GetTokenEndpoint returns the TokenEndpoint field if non-nil, zero value otherwise.

### GetTokenEndpointOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetTokenEndpointOk() (*string, bool)`

GetTokenEndpointOk returns a tuple with the TokenEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetTokenEndpoint(v string)`

SetTokenEndpoint sets TokenEndpoint field to given value.


### GetIntrospectionEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetIntrospectionEndpoint() string`

GetIntrospectionEndpoint returns the IntrospectionEndpoint field if non-nil, zero value otherwise.

### GetIntrospectionEndpointOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetIntrospectionEndpointOk() (*string, bool)`

GetIntrospectionEndpointOk returns a tuple with the IntrospectionEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntrospectionEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetIntrospectionEndpoint(v string)`

SetIntrospectionEndpoint sets IntrospectionEndpoint field to given value.

### HasIntrospectionEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasIntrospectionEndpoint() bool`

HasIntrospectionEndpoint returns a boolean if a field has been set.

### GetResponseTypesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetResponseTypesSupported() []string`

GetResponseTypesSupported returns the ResponseTypesSupported field if non-nil, zero value otherwise.

### GetResponseTypesSupportedOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetResponseTypesSupportedOk() (*[]string, bool)`

GetResponseTypesSupportedOk returns a tuple with the ResponseTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseTypesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetResponseTypesSupported(v []string)`

SetResponseTypesSupported sets ResponseTypesSupported field to given value.


### GetGrantTypesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetGrantTypesSupported() []string`

GetGrantTypesSupported returns the GrantTypesSupported field if non-nil, zero value otherwise.

### GetGrantTypesSupportedOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetGrantTypesSupportedOk() (*[]string, bool)`

GetGrantTypesSupportedOk returns a tuple with the GrantTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetGrantTypesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetGrantTypesSupported(v []string)`

SetGrantTypesSupported sets GrantTypesSupported field to given value.

### HasGrantTypesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasGrantTypesSupported() bool`

HasGrantTypesSupported returns a boolean if a field has been set.

### GetTokenEndpointAuthMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetTokenEndpointAuthMethodsSupported() []string`

GetTokenEndpointAuthMethodsSupported returns the TokenEndpointAuthMethodsSupported field if non-nil, zero value otherwise.

### GetTokenEndpointAuthMethodsSupportedOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetTokenEndpointAuthMethodsSupportedOk() (*[]string, bool)`

GetTokenEndpointAuthMethodsSupportedOk returns a tuple with the TokenEndpointAuthMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpointAuthMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetTokenEndpointAuthMethodsSupported(v []string)`

SetTokenEndpointAuthMethodsSupported sets TokenEndpointAuthMethodsSupported field to given value.

### HasTokenEndpointAuthMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasTokenEndpointAuthMethodsSupported() bool`

HasTokenEndpointAuthMethodsSupported returns a boolean if a field has been set.

### GetCodeChallengeMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetCodeChallengeMethodsSupported() []string`

GetCodeChallengeMethodsSupported returns the CodeChallengeMethodsSupported field if non-nil, zero value otherwise.

### GetCodeChallengeMethodsSupportedOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetCodeChallengeMethodsSupportedOk() (*[]string, bool)`

GetCodeChallengeMethodsSupportedOk returns a tuple with the CodeChallengeMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCodeChallengeMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetCodeChallengeMethodsSupported(v []string)`

SetCodeChallengeMethodsSupported sets CodeChallengeMethodsSupported field to given value.

### HasCodeChallengeMethodsSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasCodeChallengeMethodsSupported() bool`

HasCodeChallengeMethodsSupported returns a boolean if a field has been set.

### GetJwksUri

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetJwksUri() string`

GetJwksUri returns the JwksUri field if non-nil, zero value otherwise.

### GetJwksUriOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetJwksUriOk() (*string, bool)`

GetJwksUriOk returns a tuple with the JwksUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJwksUri

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetJwksUri(v string)`

SetJwksUri sets JwksUri field to given value.

### HasJwksUri

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasJwksUri() bool`

HasJwksUri returns a boolean if a field has been set.

### GetRevocationEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetRevocationEndpoint() string`

GetRevocationEndpoint returns the RevocationEndpoint field if non-nil, zero value otherwise.

### GetRevocationEndpointOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetRevocationEndpointOk() (*string, bool)`

GetRevocationEndpointOk returns a tuple with the RevocationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRevocationEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetRevocationEndpoint(v string)`

SetRevocationEndpoint sets RevocationEndpoint field to given value.

### HasRevocationEndpoint

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasRevocationEndpoint() bool`

HasRevocationEndpoint returns a boolean if a field has been set.

### GetScopesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetScopesSupported() []string`

GetScopesSupported returns the ScopesSupported field if non-nil, zero value otherwise.

### GetScopesSupportedOk

`func (o *GetOAuthAuthorizationServerMetadata200Response) GetScopesSupportedOk() (*[]string, bool)`

GetScopesSupportedOk returns a tuple with the ScopesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) SetScopesSupported(v []string)`

SetScopesSupported sets ScopesSupported field to given value.

### HasScopesSupported

`func (o *GetOAuthAuthorizationServerMetadata200Response) HasScopesSupported() bool`

HasScopesSupported returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


