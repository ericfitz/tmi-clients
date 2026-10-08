# MinimalNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Cell unique identifier | 
**Shape** | **string** | Node shape type determining its semantic role in the diagram | 
**Parent** | Pointer to **NullableString** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**Children** | **[]string** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**Labels** | **[]string** | Text labels extracted from node attrs and embedded text-box children | 
**Metadata** | **map[string]string** | Flattened cell metadata (converted from _metadata array in cell.data) | 
**SecurityBoundary** | **bool** | Indicates whether this node represents a security boundary. Always true for shape&#x3D;&#39;security-boundary&#39;, otherwise derived from cell data. | [default to false]
**DataAssetIds** | Pointer to **[]string** | References to Asset IDs associated with this node | [optional] 

## Methods

### NewMinimalNode

`func NewMinimalNode(id string, shape string, children []string, labels []string, metadata map[string]string, securityBoundary bool, ) *MinimalNode`

NewMinimalNode instantiates a new MinimalNode object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMinimalNodeWithDefaults

`func NewMinimalNodeWithDefaults() *MinimalNode`

NewMinimalNodeWithDefaults instantiates a new MinimalNode object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MinimalNode) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MinimalNode) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MinimalNode) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *MinimalNode) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *MinimalNode) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *MinimalNode) SetShape(v string)`

SetShape sets Shape field to given value.


### GetParent

`func (o *MinimalNode) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *MinimalNode) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *MinimalNode) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *MinimalNode) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *MinimalNode) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *MinimalNode) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *MinimalNode) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *MinimalNode) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *MinimalNode) SetChildren(v []string)`

SetChildren sets Children field to given value.


### GetLabels

`func (o *MinimalNode) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *MinimalNode) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *MinimalNode) SetLabels(v []string)`

SetLabels sets Labels field to given value.


### GetMetadata

`func (o *MinimalNode) GetMetadata() map[string]string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *MinimalNode) GetMetadataOk() (*map[string]string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *MinimalNode) SetMetadata(v map[string]string)`

SetMetadata sets Metadata field to given value.


### GetSecurityBoundary

`func (o *MinimalNode) GetSecurityBoundary() bool`

GetSecurityBoundary returns the SecurityBoundary field if non-nil, zero value otherwise.

### GetSecurityBoundaryOk

`func (o *MinimalNode) GetSecurityBoundaryOk() (*bool, bool)`

GetSecurityBoundaryOk returns a tuple with the SecurityBoundary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityBoundary

`func (o *MinimalNode) SetSecurityBoundary(v bool)`

SetSecurityBoundary sets SecurityBoundary field to given value.


### GetDataAssetIds

`func (o *MinimalNode) GetDataAssetIds() []string`

GetDataAssetIds returns the DataAssetIds field if non-nil, zero value otherwise.

### GetDataAssetIdsOk

`func (o *MinimalNode) GetDataAssetIdsOk() (*[]string, bool)`

GetDataAssetIdsOk returns a tuple with the DataAssetIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataAssetIds

`func (o *MinimalNode) SetDataAssetIds(v []string)`

SetDataAssetIds sets DataAssetIds field to given value.

### HasDataAssetIds

`func (o *MinimalNode) HasDataAssetIds() bool`

HasDataAssetIds returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


