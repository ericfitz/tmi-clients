# DfdDiagramInputAllOfCells

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

### NewDfdDiagramInputAllOfCells

`func NewDfdDiagramInputAllOfCells(id string, shape string, source EdgeTerminal, target EdgeTerminal, ) *DfdDiagramInputAllOfCells`

NewDfdDiagramInputAllOfCells instantiates a new DfdDiagramInputAllOfCells object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramInputAllOfCellsWithDefaults

`func NewDfdDiagramInputAllOfCellsWithDefaults() *DfdDiagramInputAllOfCells`

NewDfdDiagramInputAllOfCellsWithDefaults instantiates a new DfdDiagramInputAllOfCells object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DfdDiagramInputAllOfCells) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DfdDiagramInputAllOfCells) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DfdDiagramInputAllOfCells) SetId(v string)`

SetId sets Id field to given value.


### GetShape

`func (o *DfdDiagramInputAllOfCells) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *DfdDiagramInputAllOfCells) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *DfdDiagramInputAllOfCells) SetShape(v string)`

SetShape sets Shape field to given value.


### GetData

`func (o *DfdDiagramInputAllOfCells) GetData() CellData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DfdDiagramInputAllOfCells) GetDataOk() (*CellData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *DfdDiagramInputAllOfCells) SetData(v CellData)`

SetData sets Data field to given value.

### HasData

`func (o *DfdDiagramInputAllOfCells) HasData() bool`

HasData returns a boolean if a field has been set.

### GetPosition

`func (o *DfdDiagramInputAllOfCells) GetPosition() NodeAllOfPosition`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *DfdDiagramInputAllOfCells) GetPositionOk() (*NodeAllOfPosition, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *DfdDiagramInputAllOfCells) SetPosition(v NodeAllOfPosition)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *DfdDiagramInputAllOfCells) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetSize

`func (o *DfdDiagramInputAllOfCells) GetSize() NodeAllOfSize`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *DfdDiagramInputAllOfCells) GetSizeOk() (*NodeAllOfSize, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *DfdDiagramInputAllOfCells) SetSize(v NodeAllOfSize)`

SetSize sets Size field to given value.

### HasSize

`func (o *DfdDiagramInputAllOfCells) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetAngle

`func (o *DfdDiagramInputAllOfCells) GetAngle() float32`

GetAngle returns the Angle field if non-nil, zero value otherwise.

### GetAngleOk

`func (o *DfdDiagramInputAllOfCells) GetAngleOk() (*float32, bool)`

GetAngleOk returns a tuple with the Angle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAngle

`func (o *DfdDiagramInputAllOfCells) SetAngle(v float32)`

SetAngle sets Angle field to given value.

### HasAngle

`func (o *DfdDiagramInputAllOfCells) HasAngle() bool`

HasAngle returns a boolean if a field has been set.

### GetAttrs

`func (o *DfdDiagramInputAllOfCells) GetAttrs() EdgeAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *DfdDiagramInputAllOfCells) GetAttrsOk() (*EdgeAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *DfdDiagramInputAllOfCells) SetAttrs(v EdgeAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *DfdDiagramInputAllOfCells) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetPorts

`func (o *DfdDiagramInputAllOfCells) GetPorts() PortConfiguration`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *DfdDiagramInputAllOfCells) GetPortsOk() (*PortConfiguration, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *DfdDiagramInputAllOfCells) SetPorts(v PortConfiguration)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *DfdDiagramInputAllOfCells) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetParent

`func (o *DfdDiagramInputAllOfCells) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *DfdDiagramInputAllOfCells) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *DfdDiagramInputAllOfCells) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *DfdDiagramInputAllOfCells) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *DfdDiagramInputAllOfCells) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *DfdDiagramInputAllOfCells) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *DfdDiagramInputAllOfCells) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *DfdDiagramInputAllOfCells) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *DfdDiagramInputAllOfCells) SetChildren(v []string)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *DfdDiagramInputAllOfCells) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetX

`func (o *DfdDiagramInputAllOfCells) GetX() float32`

GetX returns the X field if non-nil, zero value otherwise.

### GetXOk

`func (o *DfdDiagramInputAllOfCells) GetXOk() (*float32, bool)`

GetXOk returns a tuple with the X field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetX

`func (o *DfdDiagramInputAllOfCells) SetX(v float32)`

SetX sets X field to given value.

### HasX

`func (o *DfdDiagramInputAllOfCells) HasX() bool`

HasX returns a boolean if a field has been set.

### GetY

`func (o *DfdDiagramInputAllOfCells) GetY() float32`

GetY returns the Y field if non-nil, zero value otherwise.

### GetYOk

`func (o *DfdDiagramInputAllOfCells) GetYOk() (*float32, bool)`

GetYOk returns a tuple with the Y field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetY

`func (o *DfdDiagramInputAllOfCells) SetY(v float32)`

SetY sets Y field to given value.

### HasY

`func (o *DfdDiagramInputAllOfCells) HasY() bool`

HasY returns a boolean if a field has been set.

### GetWidth

`func (o *DfdDiagramInputAllOfCells) GetWidth() float32`

GetWidth returns the Width field if non-nil, zero value otherwise.

### GetWidthOk

`func (o *DfdDiagramInputAllOfCells) GetWidthOk() (*float32, bool)`

GetWidthOk returns a tuple with the Width field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWidth

`func (o *DfdDiagramInputAllOfCells) SetWidth(v float32)`

SetWidth sets Width field to given value.

### HasWidth

`func (o *DfdDiagramInputAllOfCells) HasWidth() bool`

HasWidth returns a boolean if a field has been set.

### GetHeight

`func (o *DfdDiagramInputAllOfCells) GetHeight() float32`

GetHeight returns the Height field if non-nil, zero value otherwise.

### GetHeightOk

`func (o *DfdDiagramInputAllOfCells) GetHeightOk() (*float32, bool)`

GetHeightOk returns a tuple with the Height field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeight

`func (o *DfdDiagramInputAllOfCells) SetHeight(v float32)`

SetHeight sets Height field to given value.

### HasHeight

`func (o *DfdDiagramInputAllOfCells) HasHeight() bool`

HasHeight returns a boolean if a field has been set.

### GetSource

`func (o *DfdDiagramInputAllOfCells) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *DfdDiagramInputAllOfCells) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *DfdDiagramInputAllOfCells) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *DfdDiagramInputAllOfCells) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *DfdDiagramInputAllOfCells) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *DfdDiagramInputAllOfCells) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.


### GetLabels

`func (o *DfdDiagramInputAllOfCells) GetLabels() []EdgeLabel`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *DfdDiagramInputAllOfCells) GetLabelsOk() (*[]EdgeLabel, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *DfdDiagramInputAllOfCells) SetLabels(v []EdgeLabel)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *DfdDiagramInputAllOfCells) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetVertices

`func (o *DfdDiagramInputAllOfCells) GetVertices() []Point`

GetVertices returns the Vertices field if non-nil, zero value otherwise.

### GetVerticesOk

`func (o *DfdDiagramInputAllOfCells) GetVerticesOk() (*[]Point, bool)`

GetVerticesOk returns a tuple with the Vertices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVertices

`func (o *DfdDiagramInputAllOfCells) SetVertices(v []Point)`

SetVertices sets Vertices field to given value.

### HasVertices

`func (o *DfdDiagramInputAllOfCells) HasVertices() bool`

HasVertices returns a boolean if a field has been set.

### GetRouter

`func (o *DfdDiagramInputAllOfCells) GetRouter() EdgeRouter`

GetRouter returns the Router field if non-nil, zero value otherwise.

### GetRouterOk

`func (o *DfdDiagramInputAllOfCells) GetRouterOk() (*EdgeRouter, bool)`

GetRouterOk returns a tuple with the Router field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRouter

`func (o *DfdDiagramInputAllOfCells) SetRouter(v EdgeRouter)`

SetRouter sets Router field to given value.

### HasRouter

`func (o *DfdDiagramInputAllOfCells) HasRouter() bool`

HasRouter returns a boolean if a field has been set.

### GetConnector

`func (o *DfdDiagramInputAllOfCells) GetConnector() EdgeConnector`

GetConnector returns the Connector field if non-nil, zero value otherwise.

### GetConnectorOk

`func (o *DfdDiagramInputAllOfCells) GetConnectorOk() (*EdgeConnector, bool)`

GetConnectorOk returns a tuple with the Connector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnector

`func (o *DfdDiagramInputAllOfCells) SetConnector(v EdgeConnector)`

SetConnector sets Connector field to given value.

### HasConnector

`func (o *DfdDiagramInputAllOfCells) HasConnector() bool`

HasConnector returns a boolean if a field has been set.

### GetDefaultLabel

`func (o *DfdDiagramInputAllOfCells) GetDefaultLabel() EdgeLabel`

GetDefaultLabel returns the DefaultLabel field if non-nil, zero value otherwise.

### GetDefaultLabelOk

`func (o *DfdDiagramInputAllOfCells) GetDefaultLabelOk() (*EdgeLabel, bool)`

GetDefaultLabelOk returns a tuple with the DefaultLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultLabel

`func (o *DfdDiagramInputAllOfCells) SetDefaultLabel(v EdgeLabel)`

SetDefaultLabel sets DefaultLabel field to given value.

### HasDefaultLabel

`func (o *DfdDiagramInputAllOfCells) HasDefaultLabel() bool`

HasDefaultLabel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


