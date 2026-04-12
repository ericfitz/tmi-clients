# IntrospectToken500Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Error** | **string** | Error message describing what went wrong | 
**RequestId** | Pointer to **string** | Unique request identifier for troubleshooting | [optional] 

## Methods

### NewIntrospectToken500Response

`func NewIntrospectToken500Response(error_ string, ) *IntrospectToken500Response`

NewIntrospectToken500Response instantiates a new IntrospectToken500Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewIntrospectToken500ResponseWithDefaults

`func NewIntrospectToken500ResponseWithDefaults() *IntrospectToken500Response`

NewIntrospectToken500ResponseWithDefaults instantiates a new IntrospectToken500Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetError

`func (o *IntrospectToken500Response) GetError() string`

GetError returns the Error field if non-nil, zero value otherwise.

### GetErrorOk

`func (o *IntrospectToken500Response) GetErrorOk() (*string, bool)`

GetErrorOk returns a tuple with the Error field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetError

`func (o *IntrospectToken500Response) SetError(v string)`

SetError sets Error field to given value.


### GetRequestId

`func (o *IntrospectToken500Response) GetRequestId() string`

GetRequestId returns the RequestId field if non-nil, zero value otherwise.

### GetRequestIdOk

`func (o *IntrospectToken500Response) GetRequestIdOk() (*string, bool)`

GetRequestIdOk returns a tuple with the RequestId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRequestId

`func (o *IntrospectToken500Response) SetRequestId(v string)`

SetRequestId sets RequestId field to given value.

### HasRequestId

`func (o *IntrospectToken500Response) HasRequestId() bool`

HasRequestId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


