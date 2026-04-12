# MinimalEdge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Cell unique identifier | 
**Shape** | **string** | Edge shape type | 
**Source** | [**EdgeTerminal**](EdgeTerminal.md) | Source node connection details | 
**Target** | [**EdgeTerminal**](EdgeTerminal.md) | Target node connection details | 
**Labels** | **[]string** | Text labels extracted from edge labels array | 
**DataAssetIds** | Pointer to **[]string** | References to Asset IDs associated with this edge | [optional] 
**Metadata** | **map[string]string** | Flattened edge metadata (converted from _metadata array in edge.data) | 

## Methods

### NewMinimalEdge

`func NewMinimalEdge(id string, shape string, source EdgeTerminal, target EdgeTerminal, labels []string, metadata map[string]string, ) *MinimalEdge`

NewMinimalEdge instantiates a new MinimalEdge object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMinimalEdgeWithDefaults

`func NewMinimalEdgeWithDefaults() *MinimalEdge`

NewMinimalEdgeWithDefaults instantiates a new MinimalEdge object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MinimalEdge) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MinimalEdge) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MinimalEdge) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *MinimalEdge) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *MinimalEdge) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *MinimalEdge) SetShape(v string)`

SetShape sets Shape field to given value.


### GetSource

`func (o *MinimalEdge) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *MinimalEdge) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *MinimalEdge) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *MinimalEdge) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *MinimalEdge) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *MinimalEdge) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.


### GetLabels

`func (o *MinimalEdge) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *MinimalEdge) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *MinimalEdge) SetLabels(v []string)`

SetLabels sets Labels field to given value.


### GetDataAssetIds

`func (o *MinimalEdge) GetDataAssetIds() []string`

GetDataAssetIds returns the DataAssetIds field if non-nil, zero value otherwise.

### GetDataAssetIdsOk

`func (o *MinimalEdge) GetDataAssetIdsOk() (*[]string, bool)`

GetDataAssetIdsOk returns a tuple with the DataAssetIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataAssetIds

`func (o *MinimalEdge) SetDataAssetIds(v []string)`

SetDataAssetIds sets DataAssetIds field to given value.

### HasDataAssetIds

`func (o *MinimalEdge) HasDataAssetIds() bool`

HasDataAssetIds returns a boolean if a field has been set.

### GetMetadata

`func (o *MinimalEdge) GetMetadata() map[string]string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *MinimalEdge) GetMetadataOk() (*map[string]string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *MinimalEdge) SetMetadata(v map[string]string)`

SetMetadata sets Metadata field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


