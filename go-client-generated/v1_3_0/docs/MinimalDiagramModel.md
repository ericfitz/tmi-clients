# MinimalDiagramModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Threat model unique identifier | 
**Name** | **string** | Threat model name | 
**Description** | **string** | Threat model description | 
**Metadata** | **map[string]string** | Flattened metadata from threat model (converted from array format to key-value pairs) | 
**Cells** | [**[]MinimalCell**](MinimalCell.md) | Minimal cell data (nodes and edges) without visual styling | 
**Assets** | [**[]Asset**](Asset.md) | Asset objects referenced by cells in this diagram via dataAssetIds | 

## Methods

### NewMinimalDiagramModel

`func NewMinimalDiagramModel(id string, name string, description string, metadata map[string]string, cells []MinimalCell, assets []Asset, ) *MinimalDiagramModel`

NewMinimalDiagramModel instantiates a new MinimalDiagramModel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMinimalDiagramModelWithDefaults

`func NewMinimalDiagramModelWithDefaults() *MinimalDiagramModel`

NewMinimalDiagramModelWithDefaults instantiates a new MinimalDiagramModel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *MinimalDiagramModel) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *MinimalDiagramModel) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *MinimalDiagramModel) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *MinimalDiagramModel) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *MinimalDiagramModel) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *MinimalDiagramModel) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *MinimalDiagramModel) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *MinimalDiagramModel) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *MinimalDiagramModel) SetDescription(v string)`

SetDescription sets Description field to given value.


### GetMetadata

`func (o *MinimalDiagramModel) GetMetadata() map[string]string`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *MinimalDiagramModel) GetMetadataOk() (*map[string]string, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *MinimalDiagramModel) SetMetadata(v map[string]string)`

SetMetadata sets Metadata field to given value.


### GetCells

`func (o *MinimalDiagramModel) GetCells() []MinimalCell`

GetCells returns the Cells field if non-nil, zero value otherwise.

### GetCellsOk

`func (o *MinimalDiagramModel) GetCellsOk() (*[]MinimalCell, bool)`

GetCellsOk returns a tuple with the Cells field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCells

`func (o *MinimalDiagramModel) SetCells(v []MinimalCell)`

SetCells sets Cells field to given value.


### GetAssets

`func (o *MinimalDiagramModel) GetAssets() []Asset`

GetAssets returns the Assets field if non-nil, zero value otherwise.

### GetAssetsOk

`func (o *MinimalDiagramModel) GetAssetsOk() (*[]Asset, bool)`

GetAssetsOk returns a tuple with the Assets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssets

`func (o *MinimalDiagramModel) SetAssets(v []Asset)`

SetAssets sets Assets field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


