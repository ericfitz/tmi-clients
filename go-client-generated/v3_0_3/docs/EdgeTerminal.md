# EdgeTerminal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Cell** | **string** | ID of the connected node (UUID) | 
**Port** | Pointer to **NullableString** | ID of the specific port on the node (optional) | [optional] 

## Methods

### NewEdgeTerminal

`func NewEdgeTerminal(cell string, ) *EdgeTerminal`

NewEdgeTerminal instantiates a new EdgeTerminal object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeTerminalWithDefaults

`func NewEdgeTerminalWithDefaults() *EdgeTerminal`

NewEdgeTerminalWithDefaults instantiates a new EdgeTerminal object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCell

`func (o *EdgeTerminal) GetCell() string`

GetCell returns the Cell field if non-nil, zero value otherwise.

### GetCellOk

`func (o *EdgeTerminal) GetCellOk() (*string, bool)`

GetCellOk returns a tuple with the Cell field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCell

`func (o *EdgeTerminal) SetCell(v string)`

SetCell sets Cell field to given value.


### GetPort

`func (o *EdgeTerminal) GetPort() string`

GetPort returns the Port field if non-nil, zero value otherwise.

### GetPortOk

`func (o *EdgeTerminal) GetPortOk() (*string, bool)`

GetPortOk returns a tuple with the Port field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPort

`func (o *EdgeTerminal) SetPort(v string)`

SetPort sets Port field to given value.

### HasPort

`func (o *EdgeTerminal) HasPort() bool`

HasPort returns a boolean if a field has been set.

### SetPortNil

`func (o *EdgeTerminal) SetPortNil(b bool)`

 SetPortNil sets the value for Port to be an explicit nil

### UnsetPort
`func (o *EdgeTerminal) UnsetPort()`

UnsetPort ensures that no value is present for Port, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


