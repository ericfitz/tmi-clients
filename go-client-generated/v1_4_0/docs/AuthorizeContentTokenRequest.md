# AuthorizeContentTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ClientCallback** | **string** | Client URL to redirect back to after the content-OAuth callback completes. Must match the server-side allow list. | 

## Methods

### NewAuthorizeContentTokenRequest

`func NewAuthorizeContentTokenRequest(clientCallback string, ) *AuthorizeContentTokenRequest`

NewAuthorizeContentTokenRequest instantiates a new AuthorizeContentTokenRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuthorizeContentTokenRequestWithDefaults

`func NewAuthorizeContentTokenRequestWithDefaults() *AuthorizeContentTokenRequest`

NewAuthorizeContentTokenRequestWithDefaults instantiates a new AuthorizeContentTokenRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetClientCallback

`func (o *AuthorizeContentTokenRequest) GetClientCallback() string`

GetClientCallback returns the ClientCallback field if non-nil, zero value otherwise.

### GetClientCallbackOk

`func (o *AuthorizeContentTokenRequest) GetClientCallbackOk() (*string, bool)`

GetClientCallbackOk returns a tuple with the ClientCallback field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientCallback

`func (o *AuthorizeContentTokenRequest) SetClientCallback(v string)`

SetClientCallback sets ClientCallback field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


