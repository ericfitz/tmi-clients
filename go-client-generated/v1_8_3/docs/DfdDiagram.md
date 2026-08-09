# DfdDiagram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to **string** | DFD diagram type with version | [optional] 
**Cells** | [**[]DfdDiagramAllOfCells**](DfdDiagramAllOfCells.md) | List of diagram cells (nodes and edges) following X6 structure | 
**Version** | Pointer to **int32** | Server-managed monotonically-increasing optimistic-locking version. Returned on reads and bumped by every successful PUT/PATCH. Clients echo this back via the If-Match request header (preferred) or the body &#39;version&#39; field on the next mutation. A mismatch returns 409 Conflict. See issue #385. | [optional] [readonly] 

## Methods

### NewDfdDiagram

`func NewDfdDiagram(cells []DfdDiagramAllOfCells, ) *DfdDiagram`

NewDfdDiagram instantiates a new DfdDiagram object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramWithDefaults

`func NewDfdDiagramWithDefaults() *DfdDiagram`

NewDfdDiagramWithDefaults instantiates a new DfdDiagram object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *DfdDiagram) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DfdDiagram) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DfdDiagram) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *DfdDiagram) HasType() bool`

HasType returns a boolean if a field has been set.

### GetCells

`func (o *DfdDiagram) GetCells() []DfdDiagramAllOfCells`

GetCells returns the Cells field if non-nil, zero value otherwise.

### GetCellsOk

`func (o *DfdDiagram) GetCellsOk() (*[]DfdDiagramAllOfCells, bool)`

GetCellsOk returns a tuple with the Cells field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCells

`func (o *DfdDiagram) SetCells(v []DfdDiagramAllOfCells)`

SetCells sets Cells field to given value.


### GetVersion

`func (o *DfdDiagram) GetVersion() int32`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *DfdDiagram) GetVersionOk() (*int32, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *DfdDiagram) SetVersion(v int32)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *DfdDiagram) HasVersion() bool`

HasVersion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


