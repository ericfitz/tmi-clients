# ConfirmIdentityLink429Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** |  | 
**RetryAfter** | Pointer to **int32** |  | [optional] 

## Methods

### NewConfirmIdentityLink429Response

`func NewConfirmIdentityLink429Response(error_ string, ) *ConfirmIdentityLink429Response`

NewConfirmIdentityLink429Response instantiates a new ConfirmIdentityLink429Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewConfirmIdentityLink429ResponseWithDefaults

`func NewConfirmIdentityLink429ResponseWithDefaults() *ConfirmIdentityLink429Response`

NewConfirmIdentityLink429ResponseWithDefaults instantiates a new ConfirmIdentityLink429Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *ConfirmIdentityLink429Response) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *ConfirmIdentityLink429Response) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *ConfirmIdentityLink429Response) SetError(v string)`

SetError sets Error field to given value.


### GetRetryAfter

`func (o *ConfirmIdentityLink429Response) GetRetryAfter() int32`

GetRetryAfter returns the RetryAfter field if non-nil, zero value otherwise.

### GetRetryAfterOk

`func (o *ConfirmIdentityLink429Response) GetRetryAfterOk() (*int32, bool)`

GetRetryAfterOk returns a tuple with the RetryAfter field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRetryAfter

`func (o *ConfirmIdentityLink429Response) SetRetryAfter(v int32)`

SetRetryAfter sets RetryAfter field to given value.

### HasRetryAfter

`func (o *ConfirmIdentityLink429Response) HasRetryAfter() bool`

HasRetryAfter returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


