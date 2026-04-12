# Cell

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the cell (UUID) | 
**Shape** | **string** | Shape type identifier that determines cell structure and behavior | 
**Data** | Pointer to [**CellData**](CellData.md) |  | [optional] [default to {"_metadata":[]}]

## Methods

### NewCell

`func NewCell(id string, shape string, ) *Cell`

NewCell instantiates a new Cell object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCellWithDefaults

`func NewCellWithDefaults() *Cell`

NewCellWithDefaults instantiates a new Cell object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *Cell) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Cell) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Cell) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *Cell) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *Cell) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *Cell) SetShape(v string)`

SetShape sets Shape field to given value.


### GetData

`func (o *Cell) GetData() CellData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *Cell) GetDataOk() (*CellData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *Cell) SetData(v CellData)`

SetData sets Data field to given value.

### HasData

`func (o *Cell) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


