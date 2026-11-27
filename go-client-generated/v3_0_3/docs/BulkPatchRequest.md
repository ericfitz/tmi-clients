# BulkPatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Patches** | [**[]BulkPatchRequestPatchesInner**](BulkPatchRequestPatchesInner.md) | Array of patch operations, each targeting a specific threat by ID | 

## Methods

### NewBulkPatchRequest

`func NewBulkPatchRequest(patches []BulkPatchRequestPatchesInner, ) *BulkPatchRequest`

NewBulkPatchRequest instantiates a new BulkPatchRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBulkPatchRequestWithDefaults

`func NewBulkPatchRequestWithDefaults() *BulkPatchRequest`

NewBulkPatchRequestWithDefaults instantiates a new BulkPatchRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPatches

`func (o *BulkPatchRequest) GetPatches() []BulkPatchRequestPatchesInner`

GetPatches returns the Patches field if non-nil, zero value otherwise.

### GetPatchesOk

`func (o *BulkPatchRequest) GetPatchesOk() (*[]BulkPatchRequestPatchesInner, bool)`

GetPatchesOk returns a tuple with the Patches field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPatches

`func (o *BulkPatchRequest) SetPatches(v []BulkPatchRequestPatchesInner)`

SetPatches sets Patches field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


