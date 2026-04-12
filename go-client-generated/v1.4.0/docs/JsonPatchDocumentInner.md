# JsonPatchDocumentInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Op** | **string** | Patch operation type | 
**Path** | **string** | JSON path to target | 
**Value** | Pointer to **interface{}** | The value to use for add/replace/test operations. Can be any JSON value per RFC 6902 (string, number, boolean, object, array, or null). | [optional] 

## Methods

### NewJsonPatchDocumentInner

`func NewJsonPatchDocumentInner(op string, path string, ) *JsonPatchDocumentInner`

NewJsonPatchDocumentInner instantiates a new JsonPatchDocumentInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewJsonPatchDocumentInnerWithDefaults

`func NewJsonPatchDocumentInnerWithDefaults() *JsonPatchDocumentInner`

NewJsonPatchDocumentInnerWithDefaults instantiates a new JsonPatchDocumentInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOp

`func (o *JsonPatchDocumentInner) GetOp() string`

GetOp returns the Op field if non-nil, zero value otherwise.

### GetOpOk

`func (o *JsonPatchDocumentInner) GetOpOk() (*string, bool)`

GetOpOk returns a tuple with the Op field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOp

`func (o *JsonPatchDocumentInner) SetOp(v string)`

SetOp sets Op field to given value.


### GetPath

`func (o *JsonPatchDocumentInner) GetPath() string`

GetPath returns the Path field if non-nil, zero value otherwise.

### GetPathOk

`func (o *JsonPatchDocumentInner) GetPathOk() (*string, bool)`

GetPathOk returns a tuple with the Path field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPath

`func (o *JsonPatchDocumentInner) SetPath(v string)`

SetPath sets Path field to given value.


### GetValue

`func (o *JsonPatchDocumentInner) GetValue() interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *JsonPatchDocumentInner) GetValueOk() (*interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *JsonPatchDocumentInner) SetValue(v interface{})`

SetValue sets Value field to given value.

### HasValue

`func (o *JsonPatchDocumentInner) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *JsonPatchDocumentInner) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *JsonPatchDocumentInner) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


