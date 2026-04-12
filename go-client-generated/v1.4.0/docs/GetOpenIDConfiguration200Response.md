# GetOpenIDConfiguration200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Issuer** | **string** |  | 
**AuthorizationEndpoint** | **string** |  | 
**TokenEndpoint** | **string** |  | 
**UserinfoEndpoint** | Pointer to **string** |  | [optional] 
**JwksUri** | **string** |  | 
**ResponseTypesSupported** | **[]string** |  | 
**SubjectTypesSupported** | **[]string** |  | 
**IdTokenSigningAlgValuesSupported** | **[]string** |  | 
**ScopesSupported** | Pointer to **[]string** |  | [optional] 
**ClaimsSupported** | Pointer to **[]string** |  | [optional] 
**IntrospectionEndpoint** | Pointer to **string** |  | [optional] 

## Methods

### NewGetOpenIDConfiguration200Response

`func NewGetOpenIDConfiguration200Response(issuer string, authorizationEndpoint string, tokenEndpoint string, jwksUri string, responseTypesSupported []string, subjectTypesSupported []string, idTokenSigningAlgValuesSupported []string, ) *GetOpenIDConfiguration200Response`

NewGetOpenIDConfiguration200Response instantiates a new GetOpenIDConfiguration200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewGetOpenIDConfiguration200ResponseWithDefaults

`func NewGetOpenIDConfiguration200ResponseWithDefaults() *GetOpenIDConfiguration200Response`

NewGetOpenIDConfiguration200ResponseWithDefaults instantiates a new GetOpenIDConfiguration200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetIssuer

`func (o *GetOpenIDConfiguration200Response) GetIssuer() string`

GetIssuer returns the Issuer field if non-nil, zero value otherwise.

### GetIssuerOk

`func (o *GetOpenIDConfiguration200Response) GetIssuerOk() (*string, bool)`

GetIssuerOk returns a tuple with the Issuer field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssuer

`func (o *GetOpenIDConfiguration200Response) SetIssuer(v string)`

SetIssuer sets Issuer field to given value.


### GetAuthorizationEndpoint

`func (o *GetOpenIDConfiguration200Response) GetAuthorizationEndpoint() string`

GetAuthorizationEndpoint returns the AuthorizationEndpoint field if non-nil, zero value otherwise.

### GetAuthorizationEndpointOk

`func (o *GetOpenIDConfiguration200Response) GetAuthorizationEndpointOk() (*string, bool)`

GetAuthorizationEndpointOk returns a tuple with the AuthorizationEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationEndpoint

`func (o *GetOpenIDConfiguration200Response) SetAuthorizationEndpoint(v string)`

SetAuthorizationEndpoint sets AuthorizationEndpoint field to given value.


### GetTokenEndpoint

`func (o *GetOpenIDConfiguration200Response) GetTokenEndpoint() string`

GetTokenEndpoint returns the TokenEndpoint field if non-nil, zero value otherwise.

### GetTokenEndpointOk

`func (o *GetOpenIDConfiguration200Response) GetTokenEndpointOk() (*string, bool)`

GetTokenEndpointOk returns a tuple with the TokenEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTokenEndpoint

`func (o *GetOpenIDConfiguration200Response) SetTokenEndpoint(v string)`

SetTokenEndpoint sets TokenEndpoint field to given value.


### GetUserinfoEndpoint

`func (o *GetOpenIDConfiguration200Response) GetUserinfoEndpoint() string`

GetUserinfoEndpoint returns the UserinfoEndpoint field if non-nil, zero value otherwise.

### GetUserinfoEndpointOk

`func (o *GetOpenIDConfiguration200Response) GetUserinfoEndpointOk() (*string, bool)`

GetUserinfoEndpointOk returns a tuple with the UserinfoEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserinfoEndpoint

`func (o *GetOpenIDConfiguration200Response) SetUserinfoEndpoint(v string)`

SetUserinfoEndpoint sets UserinfoEndpoint field to given value.

### HasUserinfoEndpoint

`func (o *GetOpenIDConfiguration200Response) HasUserinfoEndpoint() bool`

HasUserinfoEndpoint returns a boolean if a field has been set.

### GetJwksUri

`func (o *GetOpenIDConfiguration200Response) GetJwksUri() string`

GetJwksUri returns the JwksUri field if non-nil, zero value otherwise.

### GetJwksUriOk

`func (o *GetOpenIDConfiguration200Response) GetJwksUriOk() (*string, bool)`

GetJwksUriOk returns a tuple with the JwksUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJwksUri

`func (o *GetOpenIDConfiguration200Response) SetJwksUri(v string)`

SetJwksUri sets JwksUri field to given value.


### GetResponseTypesSupported

`func (o *GetOpenIDConfiguration200Response) GetResponseTypesSupported() []string`

GetResponseTypesSupported returns the ResponseTypesSupported field if non-nil, zero value otherwise.

### GetResponseTypesSupportedOk

`func (o *GetOpenIDConfiguration200Response) GetResponseTypesSupportedOk() (*[]string, bool)`

GetResponseTypesSupportedOk returns a tuple with the ResponseTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseTypesSupported

`func (o *GetOpenIDConfiguration200Response) SetResponseTypesSupported(v []string)`

SetResponseTypesSupported sets ResponseTypesSupported field to given value.


### GetSubjectTypesSupported

`func (o *GetOpenIDConfiguration200Response) GetSubjectTypesSupported() []string`

GetSubjectTypesSupported returns the SubjectTypesSupported field if non-nil, zero value otherwise.

### GetSubjectTypesSupportedOk

`func (o *GetOpenIDConfiguration200Response) GetSubjectTypesSupportedOk() (*[]string, bool)`

GetSubjectTypesSupportedOk returns a tuple with the SubjectTypesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSubjectTypesSupported

`func (o *GetOpenIDConfiguration200Response) SetSubjectTypesSupported(v []string)`

SetSubjectTypesSupported sets SubjectTypesSupported field to given value.


### GetIdTokenSigningAlgValuesSupported

`func (o *GetOpenIDConfiguration200Response) GetIdTokenSigningAlgValuesSupported() []string`

GetIdTokenSigningAlgValuesSupported returns the IdTokenSigningAlgValuesSupported field if non-nil, zero value otherwise.

### GetIdTokenSigningAlgValuesSupportedOk

`func (o *GetOpenIDConfiguration200Response) GetIdTokenSigningAlgValuesSupportedOk() (*[]string, bool)`

GetIdTokenSigningAlgValuesSupportedOk returns a tuple with the IdTokenSigningAlgValuesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIdTokenSigningAlgValuesSupported

`func (o *GetOpenIDConfiguration200Response) SetIdTokenSigningAlgValuesSupported(v []string)`

SetIdTokenSigningAlgValuesSupported sets IdTokenSigningAlgValuesSupported field to given value.


### GetScopesSupported

`func (o *GetOpenIDConfiguration200Response) GetScopesSupported() []string`

GetScopesSupported returns the ScopesSupported field if non-nil, zero value otherwise.

### GetScopesSupportedOk

`func (o *GetOpenIDConfiguration200Response) GetScopesSupportedOk() (*[]string, bool)`

GetScopesSupportedOk returns a tuple with the ScopesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopesSupported

`func (o *GetOpenIDConfiguration200Response) SetScopesSupported(v []string)`

SetScopesSupported sets ScopesSupported field to given value.

### HasScopesSupported

`func (o *GetOpenIDConfiguration200Response) HasScopesSupported() bool`

HasScopesSupported returns a boolean if a field has been set.

### GetClaimsSupported

`func (o *GetOpenIDConfiguration200Response) GetClaimsSupported() []string`

GetClaimsSupported returns the ClaimsSupported field if non-nil, zero value otherwise.

### GetClaimsSupportedOk

`func (o *GetOpenIDConfiguration200Response) GetClaimsSupportedOk() (*[]string, bool)`

GetClaimsSupportedOk returns a tuple with the ClaimsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClaimsSupported

`func (o *GetOpenIDConfiguration200Response) SetClaimsSupported(v []string)`

SetClaimsSupported sets ClaimsSupported field to given value.

### HasClaimsSupported

`func (o *GetOpenIDConfiguration200Response) HasClaimsSupported() bool`

HasClaimsSupported returns a boolean if a field has been set.

### GetIntrospectionEndpoint

`func (o *GetOpenIDConfiguration200Response) GetIntrospectionEndpoint() string`

GetIntrospectionEndpoint returns the IntrospectionEndpoint field if non-nil, zero value otherwise.

### GetIntrospectionEndpointOk

`func (o *GetOpenIDConfiguration200Response) GetIntrospectionEndpointOk() (*string, bool)`

GetIntrospectionEndpointOk returns a tuple with the IntrospectionEndpoint field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIntrospectionEndpoint

`func (o *GetOpenIDConfiguration200Response) SetIntrospectionEndpoint(v string)`

SetIntrospectionEndpoint sets IntrospectionEndpoint field to given value.

### HasIntrospectionEndpoint

`func (o *GetOpenIDConfiguration200Response) HasIntrospectionEndpoint() bool`

HasIntrospectionEndpoint returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


