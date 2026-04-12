# OAuthProtectedResourceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Resource** | **string** | The protected resource&#39;s resource identifier URL | 
**ScopesSupported** | Pointer to **[]string** | JSON array of OAuth scope values supported by this protected resource | [optional] 
**AuthorizationServers** | Pointer to **[]string** | List of authorization server issuer identifiers that can issue tokens for this resource | [optional] 
**JwksUri** | Pointer to **string** | URL of the protected resource&#39;s JSON Web Key Set (RFC 9728) | [optional] 
**BearerMethodsSupported** | Pointer to **[]string** | Supported token presentation methods for bearer tokens | [optional] 
**ResourceName** | Pointer to **string** | Human-readable name of the protected resource | [optional] 
**ResourceDocumentation** | Pointer to **string** | URL with information for developers on how to use this protected resource | [optional] 
**TlsClientCertificateBoundAccessTokens** | Pointer to **bool** | Whether the protected resource supports TLS client certificate bound access tokens | [optional] 

## Methods

### NewOAuthProtectedResourceMetadata

`func NewOAuthProtectedResourceMetadata(resource string, ) *OAuthProtectedResourceMetadata`

NewOAuthProtectedResourceMetadata instantiates a new OAuthProtectedResourceMetadata object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOAuthProtectedResourceMetadataWithDefaults

`func NewOAuthProtectedResourceMetadataWithDefaults() *OAuthProtectedResourceMetadata`

NewOAuthProtectedResourceMetadataWithDefaults instantiates a new OAuthProtectedResourceMetadata object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResource

`func (o *OAuthProtectedResourceMetadata) GetResource() string`

GetResource returns the Resource field if non-nil, zero value otherwise.

### GetResourceOk

`func (o *OAuthProtectedResourceMetadata) GetResourceOk() (*string, bool)`

GetResourceOk returns a tuple with the Resource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResource

`func (o *OAuthProtectedResourceMetadata) SetResource(v string)`

SetResource sets Resource field to given value.


### GetScopesSupported

`func (o *OAuthProtectedResourceMetadata) GetScopesSupported() []string`

GetScopesSupported returns the ScopesSupported field if non-nil, zero value otherwise.

### GetScopesSupportedOk

`func (o *OAuthProtectedResourceMetadata) GetScopesSupportedOk() (*[]string, bool)`

GetScopesSupportedOk returns a tuple with the ScopesSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScopesSupported

`func (o *OAuthProtectedResourceMetadata) SetScopesSupported(v []string)`

SetScopesSupported sets ScopesSupported field to given value.

### HasScopesSupported

`func (o *OAuthProtectedResourceMetadata) HasScopesSupported() bool`

HasScopesSupported returns a boolean if a field has been set.

### GetAuthorizationServers

`func (o *OAuthProtectedResourceMetadata) GetAuthorizationServers() []string`

GetAuthorizationServers returns the AuthorizationServers field if non-nil, zero value otherwise.

### GetAuthorizationServersOk

`func (o *OAuthProtectedResourceMetadata) GetAuthorizationServersOk() (*[]string, bool)`

GetAuthorizationServersOk returns a tuple with the AuthorizationServers field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthorizationServers

`func (o *OAuthProtectedResourceMetadata) SetAuthorizationServers(v []string)`

SetAuthorizationServers sets AuthorizationServers field to given value.

### HasAuthorizationServers

`func (o *OAuthProtectedResourceMetadata) HasAuthorizationServers() bool`

HasAuthorizationServers returns a boolean if a field has been set.

### GetJwksUri

`func (o *OAuthProtectedResourceMetadata) GetJwksUri() string`

GetJwksUri returns the JwksUri field if non-nil, zero value otherwise.

### GetJwksUriOk

`func (o *OAuthProtectedResourceMetadata) GetJwksUriOk() (*string, bool)`

GetJwksUriOk returns a tuple with the JwksUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJwksUri

`func (o *OAuthProtectedResourceMetadata) SetJwksUri(v string)`

SetJwksUri sets JwksUri field to given value.

### HasJwksUri

`func (o *OAuthProtectedResourceMetadata) HasJwksUri() bool`

HasJwksUri returns a boolean if a field has been set.

### GetBearerMethodsSupported

`func (o *OAuthProtectedResourceMetadata) GetBearerMethodsSupported() []string`

GetBearerMethodsSupported returns the BearerMethodsSupported field if non-nil, zero value otherwise.

### GetBearerMethodsSupportedOk

`func (o *OAuthProtectedResourceMetadata) GetBearerMethodsSupportedOk() (*[]string, bool)`

GetBearerMethodsSupportedOk returns a tuple with the BearerMethodsSupported field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetBearerMethodsSupported

`func (o *OAuthProtectedResourceMetadata) SetBearerMethodsSupported(v []string)`

SetBearerMethodsSupported sets BearerMethodsSupported field to given value.

### HasBearerMethodsSupported

`func (o *OAuthProtectedResourceMetadata) HasBearerMethodsSupported() bool`

HasBearerMethodsSupported returns a boolean if a field has been set.

### GetResourceName

`func (o *OAuthProtectedResourceMetadata) GetResourceName() string`

GetResourceName returns the ResourceName field if non-nil, zero value otherwise.

### GetResourceNameOk

`func (o *OAuthProtectedResourceMetadata) GetResourceNameOk() (*string, bool)`

GetResourceNameOk returns a tuple with the ResourceName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceName

`func (o *OAuthProtectedResourceMetadata) SetResourceName(v string)`

SetResourceName sets ResourceName field to given value.

### HasResourceName

`func (o *OAuthProtectedResourceMetadata) HasResourceName() bool`

HasResourceName returns a boolean if a field has been set.

### GetResourceDocumentation

`func (o *OAuthProtectedResourceMetadata) GetResourceDocumentation() string`

GetResourceDocumentation returns the ResourceDocumentation field if non-nil, zero value otherwise.

### GetResourceDocumentationOk

`func (o *OAuthProtectedResourceMetadata) GetResourceDocumentationOk() (*string, bool)`

GetResourceDocumentationOk returns a tuple with the ResourceDocumentation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResourceDocumentation

`func (o *OAuthProtectedResourceMetadata) SetResourceDocumentation(v string)`

SetResourceDocumentation sets ResourceDocumentation field to given value.

### HasResourceDocumentation

`func (o *OAuthProtectedResourceMetadata) HasResourceDocumentation() bool`

HasResourceDocumentation returns a boolean if a field has been set.

### GetTlsClientCertificateBoundAccessTokens

`func (o *OAuthProtectedResourceMetadata) GetTlsClientCertificateBoundAccessTokens() bool`

GetTlsClientCertificateBoundAccessTokens returns the TlsClientCertificateBoundAccessTokens field if non-nil, zero value otherwise.

### GetTlsClientCertificateBoundAccessTokensOk

`func (o *OAuthProtectedResourceMetadata) GetTlsClientCertificateBoundAccessTokensOk() (*bool, bool)`

GetTlsClientCertificateBoundAccessTokensOk returns a tuple with the TlsClientCertificateBoundAccessTokens field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTlsClientCertificateBoundAccessTokens

`func (o *OAuthProtectedResourceMetadata) SetTlsClientCertificateBoundAccessTokens(v bool)`

SetTlsClientCertificateBoundAccessTokens sets TlsClientCertificateBoundAccessTokens field to given value.

### HasTlsClientCertificateBoundAccessTokens

`func (o *OAuthProtectedResourceMetadata) HasTlsClientCertificateBoundAccessTokens() bool`

HasTlsClientCertificateBoundAccessTokens returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


