# OAuthError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** | Error code for OAuth, SAML and discovery routes: the RFC 6749, 7009 and 9470 codes, the documented TMI extensions (identity_mismatch, account_conflict, email_not_verified, provider_unreachable, provider_response_invalid, invalid_provider), and the transport codes that route-agnostic middleware can emit (unauthorized, not_found, method_not_allowed, not_acceptable, payload_too_large, unsupported_media_type, rate_limit_exceeded, server_error). SAML routes also use the TMI extension codes saml_error, saml_not_enabled, saml_unavailable, saml_provider_not_found, saml_metadata_error, saml_init_error, saml_invalid_logout_request and saml_logout_error. | 
**ErrorDescription** | **string** | Human-readable error description | 
**ErrorUri** | Pointer to **string** | URI to documentation about the error | [optional] 
**Details** | Pointer to [**NullableErrorDetails**](ErrorDetails.md) |  | [optional] 

## Methods

### NewOAuthError

`func NewOAuthError(error_ string, errorDescription string, ) *OAuthError`

NewOAuthError instantiates a new OAuthError object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewOAuthErrorWithDefaults

`func NewOAuthErrorWithDefaults() *OAuthError`

NewOAuthErrorWithDefaults instantiates a new OAuthError object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *OAuthError) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *OAuthError) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *OAuthError) SetError(v string)`

SetError sets Error field to given value.


### GetErrorDescription

`func (o *OAuthError) GetErrorDescription() string`

GetErrorDescription returns the ErrorDescription field if non-nil, zero value otherwise.

### GetErrorDescriptionOk

`func (o *OAuthError) GetErrorDescriptionOk() (*string, bool)`

GetErrorDescriptionOk returns a tuple with the ErrorDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorDescription

`func (o *OAuthError) SetErrorDescription(v string)`

SetErrorDescription sets ErrorDescription field to given value.


### GetErrorUri

`func (o *OAuthError) GetErrorUri() string`

GetErrorUri returns the ErrorUri field if non-nil, zero value otherwise.

### GetErrorUriOk

`func (o *OAuthError) GetErrorUriOk() (*string, bool)`

GetErrorUriOk returns a tuple with the ErrorUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorUri

`func (o *OAuthError) SetErrorUri(v string)`

SetErrorUri sets ErrorUri field to given value.

### HasErrorUri

`func (o *OAuthError) HasErrorUri() bool`

HasErrorUri returns a boolean if a field has been set.

### GetDetails

`func (o *OAuthError) GetDetails() ErrorDetails`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *OAuthError) GetDetailsOk() (*ErrorDetails, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *OAuthError) SetDetails(v ErrorDetails)`

SetDetails sets Details field to given value.

### HasDetails

`func (o *OAuthError) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### SetDetailsNil

`func (o *OAuthError) SetDetailsNil(b bool)`

 SetDetailsNil sets the value for Details to be an explicit nil

### UnsetDetails
`func (o *OAuthError) UnsetDetails()`

UnsetDetails ensures that no value is present for Details, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


