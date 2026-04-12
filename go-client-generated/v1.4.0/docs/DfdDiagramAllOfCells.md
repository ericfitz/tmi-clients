# DfdDiagramAllOfCells

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the cell (UUID) | 
**Shape** | **string** | Edge type identifier | 
**Data** | Pointer to [**CellData**](CellData.md) |  | [optional] [default to {"_metadata":[]}]
**Position** | Pointer to [**NodeAllOfPosition**](NodeAllOfPosition.md) |  | [optional] 
**Size** | Pointer to [**NodeAllOfSize**](NodeAllOfSize.md) |  | [optional] 
**Angle** | Pointer to **float32** | Rotation angle in degrees | [optional] [default to 0]
**Attrs** | Pointer to [**EdgeAttrs**](EdgeAttrs.md) | Visual styling attributes for the edge | [optional] 
**Ports** | Pointer to [**PortConfiguration**](PortConfiguration.md) | Port configuration for connections | [optional] 
**Parent** | Pointer to **NullableString** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**Children** | Pointer to **[]string** | IDs of child cells contained within this node (UUIDs) | [optional] 
**X** | Pointer to **float32** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**Y** | Pointer to **float32** | Y coordinate (flat format) | [optional] 
**Width** | Pointer to **float32** | Width in pixels (flat format) | [optional] 
**Height** | Pointer to **float32** | Height in pixels (flat format) | [optional] 
**Source** | [**EdgeTerminal**](EdgeTerminal.md) | Source connection point | 
**Target** | [**EdgeTerminal**](EdgeTerminal.md) | Target connection point | 
**Labels** | Pointer to [**[]EdgeLabel**](EdgeLabel.md) | Text labels positioned along the edge | [optional] 
**Vertices** | Pointer to [**[]Point**](Point.md) | Intermediate waypoints for edge routing | [optional] 
**Router** | Pointer to [**EdgeRouter**](EdgeRouter.md) | Edge routing algorithm configuration for path calculation | [optional] 
**Connector** | Pointer to [**EdgeConnector**](EdgeConnector.md) | Edge connector style configuration for visual appearance | [optional] 
**DefaultLabel** | Pointer to [**EdgeLabel**](EdgeLabel.md) | Default label configuration applied to edges without explicit labels | [optional] 

## Methods

### NewDfdDiagramAllOfCells

`func NewDfdDiagramAllOfCells(id string, shape string, source EdgeTerminal, target EdgeTerminal, ) *DfdDiagramAllOfCells`

NewDfdDiagramAllOfCells instantiates a new DfdDiagramAllOfCells object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramAllOfCellsWithDefaults

`func NewDfdDiagramAllOfCellsWithDefaults() *DfdDiagramAllOfCells`

NewDfdDiagramAllOfCellsWithDefaults instantiates a new DfdDiagramAllOfCells object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DfdDiagramAllOfCells) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DfdDiagramAllOfCells) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DfdDiagramAllOfCells) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *DfdDiagramAllOfCells) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *DfdDiagramAllOfCells) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *DfdDiagramAllOfCells) SetShape(v string)`

SetShape sets Shape field to given value.


### GetData

`func (o *DfdDiagramAllOfCells) GetData() CellData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DfdDiagramAllOfCells) GetDataOk() (*CellData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *DfdDiagramAllOfCells) SetData(v CellData)`

SetData sets Data field to given value.

### HasData

`func (o *DfdDiagramAllOfCells) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPosition

`func (o *DfdDiagramAllOfCells) GetPosition() NodeAllOfPosition`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *DfdDiagramAllOfCells) GetPositionOk() (*NodeAllOfPosition, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *DfdDiagramAllOfCells) SetPosition(v NodeAllOfPosition)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *DfdDiagramAllOfCells) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetSize

`func (o *DfdDiagramAllOfCells) GetSize() NodeAllOfSize`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *DfdDiagramAllOfCells) GetSizeOk() (*NodeAllOfSize, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *DfdDiagramAllOfCells) SetSize(v NodeAllOfSize)`

SetSize sets Size field to given value.

### HasSize

`func (o *DfdDiagramAllOfCells) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetAngle

`func (o *DfdDiagramAllOfCells) GetAngle() float32`

GetAngle returns the Angle field if non-nil, zero value otherwise.

### GetAngleOk

`func (o *DfdDiagramAllOfCells) GetAngleOk() (*float32, bool)`

GetAngleOk returns a tuple with the Angle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAngle

`func (o *DfdDiagramAllOfCells) SetAngle(v float32)`

SetAngle sets Angle field to given value.

### HasAngle

`func (o *DfdDiagramAllOfCells) HasAngle() bool`

HasAngle returns a boolean if a field has been set.

### GetAttrs

`func (o *DfdDiagramAllOfCells) GetAttrs() EdgeAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *DfdDiagramAllOfCells) GetAttrsOk() (*EdgeAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *DfdDiagramAllOfCells) SetAttrs(v EdgeAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *DfdDiagramAllOfCells) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetPorts

`func (o *DfdDiagramAllOfCells) GetPorts() PortConfiguration`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *DfdDiagramAllOfCells) GetPortsOk() (*PortConfiguration, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *DfdDiagramAllOfCells) SetPorts(v PortConfiguration)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *DfdDiagramAllOfCells) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetParent

`func (o *DfdDiagramAllOfCells) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *DfdDiagramAllOfCells) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *DfdDiagramAllOfCells) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *DfdDiagramAllOfCells) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *DfdDiagramAllOfCells) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *DfdDiagramAllOfCells) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *DfdDiagramAllOfCells) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *DfdDiagramAllOfCells) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *DfdDiagramAllOfCells) SetChildren(v []string)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *DfdDiagramAllOfCells) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetX

`func (o *DfdDiagramAllOfCells) GetX() float32`

GetX returns the X field if non-nil, zero value otherwise.

### GetXOk

`func (o *DfdDiagramAllOfCells) GetXOk() (*float32, bool)`

GetXOk returns a tuple with the X field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetX

`func (o *DfdDiagramAllOfCells) SetX(v float32)`

SetX sets X field to given value.

### HasX

`func (o *DfdDiagramAllOfCells) HasX() bool`

HasX returns a boolean if a field has been set.

### GetY

`func (o *DfdDiagramAllOfCells) GetY() float32`

GetY returns the Y field if non-nil, zero value otherwise.

### GetYOk

`func (o *DfdDiagramAllOfCells) GetYOk() (*float32, bool)`

GetYOk returns a tuple with the Y field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetY

`func (o *DfdDiagramAllOfCells) SetY(v float32)`

SetY sets Y field to given value.

### HasY

`func (o *DfdDiagramAllOfCells) HasY() bool`

HasY returns a boolean if a field has been set.

### GetWidth

`func (o *DfdDiagramAllOfCells) GetWidth() float32`

GetWidth returns the Width field if non-nil, zero value otherwise.

### GetWidthOk

`func (o *DfdDiagramAllOfCells) GetWidthOk() (*float32, bool)`

GetWidthOk returns a tuple with the Width field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWidth

`func (o *DfdDiagramAllOfCells) SetWidth(v float32)`

SetWidth sets Width field to given value.

### HasWidth

`func (o *DfdDiagramAllOfCells) HasWidth() bool`

HasWidth returns a boolean if a field has been set.

### GetHeight

`func (o *DfdDiagramAllOfCells) GetHeight() float32`

GetHeight returns the Height field if non-nil, zero value otherwise.

### GetHeightOk

`func (o *DfdDiagramAllOfCells) GetHeightOk() (*float32, bool)`

GetHeightOk returns a tuple with the Height field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeight

`func (o *DfdDiagramAllOfCells) SetHeight(v float32)`

SetHeight sets Height field to given value.

### HasHeight

`func (o *DfdDiagramAllOfCells) HasHeight() bool`

HasHeight returns a boolean if a field has been set.

### GetSource

`func (o *DfdDiagramAllOfCells) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *DfdDiagramAllOfCells) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *DfdDiagramAllOfCells) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *DfdDiagramAllOfCells) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *DfdDiagramAllOfCells) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *DfdDiagramAllOfCells) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.


### GetLabels

`func (o *DfdDiagramAllOfCells) GetLabels() []EdgeLabel`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *DfdDiagramAllOfCells) GetLabelsOk() (*[]EdgeLabel, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *DfdDiagramAllOfCells) SetLabels(v []EdgeLabel)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *DfdDiagramAllOfCells) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetVertices

`func (o *DfdDiagramAllOfCells) GetVertices() []Point`

GetVertices returns the Vertices field if non-nil, zero value otherwise.

### GetVerticesOk

`func (o *DfdDiagramAllOfCells) GetVerticesOk() (*[]Point, bool)`

GetVerticesOk returns a tuple with the Vertices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVertices

`func (o *DfdDiagramAllOfCells) SetVertices(v []Point)`

SetVertices sets Vertices field to given value.

### HasVertices

`func (o *DfdDiagramAllOfCells) HasVertices() bool`

HasVertices returns a boolean if a field has been set.

### GetRouter

`func (o *DfdDiagramAllOfCells) GetRouter() EdgeRouter`

GetRouter returns the Router field if non-nil, zero value otherwise.

### GetRouterOk

`func (o *DfdDiagramAllOfCells) GetRouterOk() (*EdgeRouter, bool)`

GetRouterOk returns a tuple with the Router field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRouter

`func (o *DfdDiagramAllOfCells) SetRouter(v EdgeRouter)`

SetRouter sets Router field to given value.

### HasRouter

`func (o *DfdDiagramAllOfCells) HasRouter() bool`

HasRouter returns a boolean if a field has been set.

### GetConnector

`func (o *DfdDiagramAllOfCells) GetConnector() EdgeConnector`

GetConnector returns the Connector field if non-nil, zero value otherwise.

### GetConnectorOk

`func (o *DfdDiagramAllOfCells) GetConnectorOk() (*EdgeConnector, bool)`

GetConnectorOk returns a tuple with the Connector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnector

`func (o *DfdDiagramAllOfCells) SetConnector(v EdgeConnector)`

SetConnector sets Connector field to given value.

### HasConnector

`func (o *DfdDiagramAllOfCells) HasConnector() bool`

HasConnector returns a boolean if a field has been set.

### GetDefaultLabel

`func (o *DfdDiagramAllOfCells) GetDefaultLabel() EdgeLabel`

GetDefaultLabel returns the DefaultLabel field if non-nil, zero value otherwise.

### GetDefaultLabelOk

`func (o *DfdDiagramAllOfCells) GetDefaultLabelOk() (*EdgeLabel, bool)`

GetDefaultLabelOk returns a tuple with the DefaultLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultLabel

`func (o *DfdDiagramAllOfCells) SetDefaultLabel(v EdgeLabel)`

SetDefaultLabel sets DefaultLabel field to given value.

### HasDefaultLabel

`func (o *DfdDiagramAllOfCells) HasDefaultLabel() bool`

HasDefaultLabel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


