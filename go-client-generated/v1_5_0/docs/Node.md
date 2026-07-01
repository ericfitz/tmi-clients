# Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shape** | Pointer to **string** | Node type determining its visual representation and behavior | [optional] 
**Position** | Pointer to [**NodeAllOfPosition**](NodeAllOfPosition.md) |  | [optional] 
**Size** | Pointer to [**NodeAllOfSize**](NodeAllOfSize.md) |  | [optional] 
**Angle** | Pointer to **float32** | Rotation angle in degrees | [optional] [default to 0]
**Attrs** | Pointer to [**NodeAttrs**](NodeAttrs.md) | Visual styling attributes for the node | [optional] 
**Ports** | Pointer to [**PortConfiguration**](PortConfiguration.md) | Port configuration for connections | [optional] 
**Parent** | Pointer to **NullableString** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**Children** | Pointer to **[]string** | IDs of child cells contained within this node (UUIDs) | [optional] 
**X** | Pointer to **float32** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**Y** | Pointer to **float32** | Y coordinate (flat format) | [optional] 
**Width** | Pointer to **float32** | Width in pixels (flat format) | [optional] 
**Height** | Pointer to **float32** | Height in pixels (flat format) | [optional] 

## Methods

### NewNode

`func NewNode() *Node`

NewNode instantiates a new Node object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNodeWithDefaults

`func NewNodeWithDefaults() *Node`

NewNodeWithDefaults instantiates a new Node object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShape

`func (o *Node) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *Node) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *Node) SetShape(v string)`

SetShape sets Shape field to given value.

### HasShape

`func (o *Node) HasShape() bool`

HasShape returns a boolean if a field has been set.

### GetPosition

`func (o *Node) GetPosition() NodeAllOfPosition`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *Node) GetPositionOk() (*NodeAllOfPosition, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *Node) SetPosition(v NodeAllOfPosition)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *Node) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetSize

`func (o *Node) GetSize() NodeAllOfSize`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *Node) GetSizeOk() (*NodeAllOfSize, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *Node) SetSize(v NodeAllOfSize)`

SetSize sets Size field to given value.

### HasSize

`func (o *Node) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetAngle

`func (o *Node) GetAngle() float32`

GetAngle returns the Angle field if non-nil, zero value otherwise.

### GetAngleOk

`func (o *Node) GetAngleOk() (*float32, bool)`

GetAngleOk returns a tuple with the Angle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAngle

`func (o *Node) SetAngle(v float32)`

SetAngle sets Angle field to given value.

### HasAngle

`func (o *Node) HasAngle() bool`

HasAngle returns a boolean if a field has been set.

### GetAttrs

`func (o *Node) GetAttrs() NodeAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *Node) GetAttrsOk() (*NodeAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *Node) SetAttrs(v NodeAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *Node) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetPorts

`func (o *Node) GetPorts() PortConfiguration`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *Node) GetPortsOk() (*PortConfiguration, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *Node) SetPorts(v PortConfiguration)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *Node) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetParent

`func (o *Node) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *Node) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *Node) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *Node) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *Node) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *Node) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *Node) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *Node) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *Node) SetChildren(v []string)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *Node) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetX

`func (o *Node) GetX() float32`

GetX returns the X field if non-nil, zero value otherwise.

### GetXOk

`func (o *Node) GetXOk() (*float32, bool)`

GetXOk returns a tuple with the X field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetX

`func (o *Node) SetX(v float32)`

SetX sets X field to given value.

### HasX

`func (o *Node) HasX() bool`

HasX returns a boolean if a field has been set.

### GetY

`func (o *Node) GetY() float32`

GetY returns the Y field if non-nil, zero value otherwise.

### GetYOk

`func (o *Node) GetYOk() (*float32, bool)`

GetYOk returns a tuple with the Y field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetY

`func (o *Node) SetY(v float32)`

SetY sets Y field to given value.

### HasY

`func (o *Node) HasY() bool`

HasY returns a boolean if a field has been set.

### GetWidth

`func (o *Node) GetWidth() float32`

GetWidth returns the Width field if non-nil, zero value otherwise.

### GetWidthOk

`func (o *Node) GetWidthOk() (*float32, bool)`

GetWidthOk returns a tuple with the Width field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWidth

`func (o *Node) SetWidth(v float32)`

SetWidth sets Width field to given value.

### HasWidth

`func (o *Node) HasWidth() bool`

HasWidth returns a boolean if a field has been set.

### GetHeight

`func (o *Node) GetHeight() float32`

GetHeight returns the Height field if non-nil, zero value otherwise.

### GetHeightOk

`func (o *Node) GetHeightOk() (*float32, bool)`

GetHeightOk returns a tuple with the Height field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeight

`func (o *Node) SetHeight(v float32)`

SetHeight sets Height field to given value.

### HasHeight

`func (o *Node) HasHeight() bool`

HasHeight returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


