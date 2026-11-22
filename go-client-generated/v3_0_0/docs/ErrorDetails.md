# ErrorDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Code** | Pointer to **string** | Machine-readable error code for programmatic handling | [optional] 
**Context** | Pointer to **map[string]interface{}** | Contextual information about the error | [optional] 
**Suggestion** | Pointer to **string** | Human-readable suggestion for resolving the error | [optional] 

## Methods

### NewErrorDetails

`func NewErrorDetails() *ErrorDetails`

NewErrorDetails instantiates a new ErrorDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewErrorDetailsWithDefaults

`func NewErrorDetailsWithDefaults() *ErrorDetails`

NewErrorDetailsWithDefaults instantiates a new ErrorDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCode

`func (o *ErrorDetails) GetCode() string`

GetCode returns the Code field if non-nil, zero value otherwise.

### GetCodeOk

`func (o *ErrorDetails) GetCodeOk() (*string, bool)`

GetCodeOk returns a tuple with the Code field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCode

`func (o *ErrorDetails) SetCode(v string)`

SetCode sets Code field to given value.

### HasCode

`func (o *ErrorDetails) HasCode() bool`

HasCode returns a boolean if a field has been set.

### GetContext

`func (o *ErrorDetails) GetContext() map[string]interface{}`

GetContext returns the Context field if non-nil, zero value otherwise.

### GetContextOk

`func (o *ErrorDetails) GetContextOk() (*map[string]interface{}, bool)`

GetContextOk returns a tuple with the Context field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContext

`func (o *ErrorDetails) SetContext(v map[string]interface{})`

SetContext sets Context field to given value.

### HasContext

`func (o *ErrorDetails) HasContext() bool`

HasContext returns a boolean if a field has been set.

### GetSuggestion

`func (o *ErrorDetails) GetSuggestion() string`

GetSuggestion returns the Suggestion field if non-nil, zero value otherwise.

### GetSuggestionOk

`func (o *ErrorDetails) GetSuggestionOk() (*string, bool)`

GetSuggestionOk returns a tuple with the Suggestion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSuggestion

`func (o *ErrorDetails) SetSuggestion(v string)`

SetSuggestion sets Suggestion field to given value.

### HasSuggestion

`func (o *ErrorDetails) HasSuggestion() bool`

HasSuggestion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


