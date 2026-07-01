# DfdDiagramInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to **string** | DFD diagram type with version | [optional] 
**Cells** | [**[]DfdDiagramInputAllOfCells**](DfdDiagramInputAllOfCells.md) | List of diagram cells (nodes and edges) following X6 structure | 

## Methods

### NewDfdDiagramInput

`func NewDfdDiagramInput(cells []DfdDiagramInputAllOfCells, ) *DfdDiagramInput`

NewDfdDiagramInput instantiates a new DfdDiagramInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramInputWithDefaults

`func NewDfdDiagramInputWithDefaults() *DfdDiagramInput`

NewDfdDiagramInputWithDefaults instantiates a new DfdDiagramInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *DfdDiagramInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DfdDiagramInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DfdDiagramInput) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *DfdDiagramInput) HasType() bool`

HasType returns a boolean if a field has been set.

### GetCells

`func (o *DfdDiagramInput) GetCells() []DfdDiagramInputAllOfCells`

GetCells returns the Cells field if non-nil, zero value otherwise.

### GetCellsOk

`func (o *DfdDiagramInput) GetCellsOk() (*[]DfdDiagramInputAllOfCells, bool)`

GetCellsOk returns a tuple with the Cells field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCells

`func (o *DfdDiagramInput) SetCells(v []DfdDiagramInputAllOfCells)`

SetCells sets Cells field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


