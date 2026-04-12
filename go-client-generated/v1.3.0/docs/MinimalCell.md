# MinimalCell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Cell unique identifier | 
**Shape** | **string** | Edge shape type | 
**Parent** | Pointer to **NullableString** | Parent cell ID for nested nodes (null for top-level nodes) | [optional] 
**Children** | **[]string** | Child cell IDs (computed bidirectional relationship including reverse parent references) | 
**Labels** | **[]string** | Text labels extracted from edge labels array | 
**DataAssetIds** | Pointer to **[]string** | References to Asset IDs associated with this edge | [optional] 
**Metadata** | **map[string]string** | Flattened edge metadata (converted from _metadata array in edge.data) | 
**SecurityBoundary** | **bool** | Indicates whether this node represents a security boundary. Always true for shape&#x3D;&#39;security-boundary&#39;, otherwise derived from cell data. | [default to false]
**Source** | [**EdgeTerminal**](EdgeTerminal.md) | Source node connection details | 
**Target** | [**EdgeTerminal**](EdgeTerminal.md) | Target node connection details | 

## Methods

### NewMinimalCell

`func NewMinimalCell(id string, shape string, children []string, labels []string, metadata map[string]string, securityBoundary bool, source EdgeTerminal, target EdgeTerminal, ) *MinimalCell`

NewMinimalCell instantiates a new MinimalCell object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMinimalCellWithDefaults

`func NewMinimalCellWithDefaults() *MinimalCell`

NewMinimalCellWithDefaults instantiates a new MinimalCell object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MinimalCell) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MinimalCell) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MinimalCell) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *MinimalCell) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *MinimalCell) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *MinimalCell) SetShape(v string)`

SetShape sets Shape field to given value.


### GetParent

`func (o *MinimalCell) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *MinimalCell) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *MinimalCell) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *MinimalCell) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *MinimalCell) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *MinimalCell) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *MinimalCell) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *MinimalCell) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *MinimalCell) SetChildren(v []string)`

SetChildren sets Children field to given value.


### GetLabels

`func (o *MinimalCell) GetLabels() []string`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *MinimalCell) GetLabelsOk() (*[]string, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *MinimalCell) SetLabels(v []string)`

SetLabels sets Labels field to given value.


### GetDataAssetIds

`func (o *MinimalCell) GetDataAssetIds() []string`

GetDataAssetIds returns the DataAssetIds field if non-nil, zero value otherwise.

### GetDataAssetIdsOk

`func (o *MinimalCell) GetDataAssetIdsOk() (*[]string, bool)`

GetDataAssetIdsOk returns a tuple with the DataAssetIds field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataAssetIds

`func (o *MinimalCell) SetDataAssetIds(v []string)`

SetDataAssetIds sets DataAssetIds field to given value.

### HasDataAssetIds

`func (o *MinimalCell) HasDataAssetIds() bool`

HasDataAssetIds returns a boolean if a field has been set.

### GetMetadata

`func (o *MinimalCell) GetMetadata() map[string]string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *MinimalCell) GetMetadataOk() (*map[string]string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *MinimalCell) SetMetadata(v map[string]string)`

SetMetadata sets Metadata field to given value.


### GetSecurityBoundary

`func (o *MinimalCell) GetSecurityBoundary() bool`

GetSecurityBoundary returns the SecurityBoundary field if non-nil, zero value otherwise.

### GetSecurityBoundaryOk

`func (o *MinimalCell) GetSecurityBoundaryOk() (*bool, bool)`

GetSecurityBoundaryOk returns a tuple with the SecurityBoundary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityBoundary

`func (o *MinimalCell) SetSecurityBoundary(v bool)`

SetSecurityBoundary sets SecurityBoundary field to given value.


### GetSource

`func (o *MinimalCell) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *MinimalCell) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *MinimalCell) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *MinimalCell) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *MinimalCell) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *MinimalCell) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


