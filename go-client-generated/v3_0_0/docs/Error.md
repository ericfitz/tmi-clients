# Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** | Machine-readable REST error code. One of: invalid_input (400, a body, field, header or query value fails validation); invalid_id (400, a path or query identifier is malformed); invalid_patch (400, a JSON Patch document is malformed or cannot be applied); unauthorized (401, missing, expired or invalid credentials); insufficient_user_authentication (401, step-up authentication required, RFC 9470); forbidden (403, authenticated but not permitted); not_found (404, resource does not exist or is hidden by authorization); method_not_allowed (405); not_acceptable (406); conflict (409, duplicate, in use, or wrong lifecycle state); gone (410, permanently removed); version_mismatch (409, If-Match does not match the current version); payload_too_large (413); unsupported_media_type (415); unprocessable_entity (422, well-formed request that cannot be processed in the current state); if_match_required (428, If-Match header missing); rate_limit_exceeded (429, transient limit, honor Retry-After); quota_exceeded (403 or 429, hard cap reached, retrying does not help); server_error (500); not_implemented (501); service_unavailable (503, a dependency is unavailable, retry later); feature_not_available (404) and content_token_provider_not_configured (422) are legacy domain codes kept at top level because clients branch on them; they are also present in details.code and will move to details.code only in a future breaking change. A domain-specific reason a client can act on is in details.code. | 
**ErrorDescription** | **string** | Human-readable error description | 
**ErrorUri** | Pointer to **string** | URI to documentation about the error | [optional] 
**Details** | Pointer to [**NullableErrorDetails**](ErrorDetails.md) |  | [optional] 

## Methods

### NewError

`func NewError(error_ string, errorDescription string, ) *Error`

NewError instantiates a new Error object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewErrorWithDefaults

`func NewErrorWithDefaults() *Error`

NewErrorWithDefaults instantiates a new Error object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *Error) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *Error) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *Error) SetError(v string)`

SetError sets Error field to given value.


### GetErrorDescription

`func (o *Error) GetErrorDescription() string`

GetErrorDescription returns the ErrorDescription field if non-nil, zero value otherwise.

### GetErrorDescriptionOk

`func (o *Error) GetErrorDescriptionOk() (*string, bool)`

GetErrorDescriptionOk returns a tuple with the ErrorDescription field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorDescription

`func (o *Error) SetErrorDescription(v string)`

SetErrorDescription sets ErrorDescription field to given value.


### GetErrorUri

`func (o *Error) GetErrorUri() string`

GetErrorUri returns the ErrorUri field if non-nil, zero value otherwise.

### GetErrorUriOk

`func (o *Error) GetErrorUriOk() (*string, bool)`

GetErrorUriOk returns a tuple with the ErrorUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrorUri

`func (o *Error) SetErrorUri(v string)`

SetErrorUri sets ErrorUri field to given value.

### HasErrorUri

`func (o *Error) HasErrorUri() bool`

HasErrorUri returns a boolean if a field has been set.

### GetDetails

`func (o *Error) GetDetails() ErrorDetails`

GetDetails returns the Details field if non-nil, zero value otherwise.

### GetDetailsOk

`func (o *Error) GetDetailsOk() (*ErrorDetails, bool)`

GetDetailsOk returns a tuple with the Details field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDetails

`func (o *Error) SetDetails(v ErrorDetails)`

SetDetails sets Details field to given value.

### HasDetails

`func (o *Error) HasDetails() bool`

HasDetails returns a boolean if a field has been set.

### SetDetailsNil

`func (o *Error) SetDetailsNil(b bool)`

 SetDetailsNil sets the value for Details to be an explicit nil

### UnsetDetails
`func (o *Error) UnsetDetails()`

UnsetDetails ensures that no value is present for Details, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


