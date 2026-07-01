# BulkPatchRequestPatchesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | ID of the threat to patch | 
**Operations** | [**[]JsonPatchDocumentInner**](JsonPatchDocumentInner.md) | JSON Patch document as defined in RFC 6902 | 

## Methods

### NewBulkPatchRequestPatchesInner

`func NewBulkPatchRequestPatchesInner(id string, operations []JsonPatchDocumentInner, ) *BulkPatchRequestPatchesInner`

NewBulkPatchRequestPatchesInner instantiates a new BulkPatchRequestPatchesInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkPatchRequestPatchesInnerWithDefaults

`func NewBulkPatchRequestPatchesInnerWithDefaults() *BulkPatchRequestPatchesInner`

NewBulkPatchRequestPatchesInnerWithDefaults instantiates a new BulkPatchRequestPatchesInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BulkPatchRequestPatchesInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BulkPatchRequestPatchesInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BulkPatchRequestPatchesInner) SetId(v string)`

SetId sets Id field to given value.


### GetOperations

`func (o *BulkPatchRequestPatchesInner) GetOperations() []JsonPatchDocumentInner`

GetOperations returns the Operations field if non-nil, zero value otherwise.

### GetOperationsOk

`func (o *BulkPatchRequestPatchesInner) GetOperationsOk() (*[]JsonPatchDocumentInner, bool)`

GetOperationsOk returns a tuple with the Operations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperations

`func (o *BulkPatchRequestPatchesInner) SetOperations(v []JsonPatchDocumentInner)`

SetOperations sets Operations field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


