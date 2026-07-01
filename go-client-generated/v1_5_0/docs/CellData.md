# CellData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Reserved namespace for structured business metadata | [optional] 
**SecurityBoundary** | Pointer to **bool** | Indicates whether this cell represents a security boundary in the threat model | [optional] [default to false]
**DataAssets** | Pointer to **[]string** | References to Asset IDs associated with this cell. Each UUID must reference an existing Asset in the same threat model. | [optional] 

## Methods

### NewCellData

`func NewCellData() *CellData`

NewCellData instantiates a new CellData object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCellDataWithDefaults

`func NewCellDataWithDefaults() *CellData`

NewCellDataWithDefaults instantiates a new CellData object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetadata

`func (o *CellData) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *CellData) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *CellData) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *CellData) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetSecurityBoundary

`func (o *CellData) GetSecurityBoundary() bool`

GetSecurityBoundary returns the SecurityBoundary field if non-nil, zero value otherwise.

### GetSecurityBoundaryOk

`func (o *CellData) GetSecurityBoundaryOk() (*bool, bool)`

GetSecurityBoundaryOk returns a tuple with the SecurityBoundary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSecurityBoundary

`func (o *CellData) SetSecurityBoundary(v bool)`

SetSecurityBoundary sets SecurityBoundary field to given value.

### HasSecurityBoundary

`func (o *CellData) HasSecurityBoundary() bool`

HasSecurityBoundary returns a boolean if a field has been set.

### GetDataAssets

`func (o *CellData) GetDataAssets() []string`

GetDataAssets returns the DataAssets field if non-nil, zero value otherwise.

### GetDataAssetsOk

`func (o *CellData) GetDataAssetsOk() (*[]string, bool)`

GetDataAssetsOk returns a tuple with the DataAssets field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDataAssets

`func (o *CellData) SetDataAssets(v []string)`

SetDataAssets sets DataAssets field to given value.

### HasDataAssets

`func (o *CellData) HasDataAssets() bool`

HasDataAssets returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


