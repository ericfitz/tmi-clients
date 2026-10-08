# DfdDiagramCellsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier of the cell (UUID) | 
**Data** | Pointer to [**CellData**](CellData.md) |  | [optional] [default to {"_metadata":[]}]
**Shape** | **string** | Edge type identifier | 
**Position** | Pointer to [**NodePosition**](NodePosition.md) |  | [optional] 
**Size** | Pointer to [**NodeSize**](NodeSize.md) |  | [optional] 
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

### NewDfdDiagramCellsInner

`func NewDfdDiagramCellsInner(id string, shape string, source EdgeTerminal, target EdgeTerminal, ) *DfdDiagramCellsInner`

NewDfdDiagramCellsInner instantiates a new DfdDiagramCellsInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramCellsInnerWithDefaults

`func NewDfdDiagramCellsInnerWithDefaults() *DfdDiagramCellsInner`

NewDfdDiagramCellsInnerWithDefaults instantiates a new DfdDiagramCellsInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DfdDiagramCellsInner) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DfdDiagramCellsInner) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DfdDiagramCellsInner) SetId(v string)`

SetId sets Id field to given value.


### GetData

`func (o *DfdDiagramCellsInner) GetData() CellData`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *DfdDiagramCellsInner) GetDataOk() (*CellData, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *DfdDiagramCellsInner) SetData(v CellData)`

SetData sets Data field to given value.

### HasData

`func (o *DfdDiagramCellsInner) HasData() bool`

HasData returns a boolean if a field has been set.

### GetShape

`func (o *DfdDiagramCellsInner) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *DfdDiagramCellsInner) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *DfdDiagramCellsInner) SetShape(v string)`

SetShape sets Shape field to given value.


### GetPosition

`func (o *DfdDiagramCellsInner) GetPosition() NodePosition`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *DfdDiagramCellsInner) GetPositionOk() (*NodePosition, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *DfdDiagramCellsInner) SetPosition(v NodePosition)`

SetPosition sets Position field to given value.

### HasPosition

`func (o *DfdDiagramCellsInner) HasPosition() bool`

HasPosition returns a boolean if a field has been set.

### GetSize

`func (o *DfdDiagramCellsInner) GetSize() NodeSize`

GetSize returns the Size field if non-nil, zero value otherwise.

### GetSizeOk

`func (o *DfdDiagramCellsInner) GetSizeOk() (*NodeSize, bool)`

GetSizeOk returns a tuple with the Size field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSize

`func (o *DfdDiagramCellsInner) SetSize(v NodeSize)`

SetSize sets Size field to given value.

### HasSize

`func (o *DfdDiagramCellsInner) HasSize() bool`

HasSize returns a boolean if a field has been set.

### GetAngle

`func (o *DfdDiagramCellsInner) GetAngle() float32`

GetAngle returns the Angle field if non-nil, zero value otherwise.

### GetAngleOk

`func (o *DfdDiagramCellsInner) GetAngleOk() (*float32, bool)`

GetAngleOk returns a tuple with the Angle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAngle

`func (o *DfdDiagramCellsInner) SetAngle(v float32)`

SetAngle sets Angle field to given value.

### HasAngle

`func (o *DfdDiagramCellsInner) HasAngle() bool`

HasAngle returns a boolean if a field has been set.

### GetAttrs

`func (o *DfdDiagramCellsInner) GetAttrs() EdgeAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *DfdDiagramCellsInner) GetAttrsOk() (*EdgeAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *DfdDiagramCellsInner) SetAttrs(v EdgeAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *DfdDiagramCellsInner) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetPorts

`func (o *DfdDiagramCellsInner) GetPorts() PortConfiguration`

GetPorts returns the Ports field if non-nil, zero value otherwise.

### GetPortsOk

`func (o *DfdDiagramCellsInner) GetPortsOk() (*PortConfiguration, bool)`

GetPortsOk returns a tuple with the Ports field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPorts

`func (o *DfdDiagramCellsInner) SetPorts(v PortConfiguration)`

SetPorts sets Ports field to given value.

### HasPorts

`func (o *DfdDiagramCellsInner) HasPorts() bool`

HasPorts returns a boolean if a field has been set.

### GetParent

`func (o *DfdDiagramCellsInner) GetParent() string`

GetParent returns the Parent field if non-nil, zero value otherwise.

### GetParentOk

`func (o *DfdDiagramCellsInner) GetParentOk() (*string, bool)`

GetParentOk returns a tuple with the Parent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParent

`func (o *DfdDiagramCellsInner) SetParent(v string)`

SetParent sets Parent field to given value.

### HasParent

`func (o *DfdDiagramCellsInner) HasParent() bool`

HasParent returns a boolean if a field has been set.

### SetParentNil

`func (o *DfdDiagramCellsInner) SetParentNil(b bool)`

 SetParentNil sets the value for Parent to be an explicit nil

### UnsetParent
`func (o *DfdDiagramCellsInner) UnsetParent()`

UnsetParent ensures that no value is present for Parent, not even an explicit nil
### GetChildren

`func (o *DfdDiagramCellsInner) GetChildren() []string`

GetChildren returns the Children field if non-nil, zero value otherwise.

### GetChildrenOk

`func (o *DfdDiagramCellsInner) GetChildrenOk() (*[]string, bool)`

GetChildrenOk returns a tuple with the Children field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChildren

`func (o *DfdDiagramCellsInner) SetChildren(v []string)`

SetChildren sets Children field to given value.

### HasChildren

`func (o *DfdDiagramCellsInner) HasChildren() bool`

HasChildren returns a boolean if a field has been set.

### GetX

`func (o *DfdDiagramCellsInner) GetX() float32`

GetX returns the X field if non-nil, zero value otherwise.

### GetXOk

`func (o *DfdDiagramCellsInner) GetXOk() (*float32, bool)`

GetXOk returns a tuple with the X field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetX

`func (o *DfdDiagramCellsInner) SetX(v float32)`

SetX sets X field to given value.

### HasX

`func (o *DfdDiagramCellsInner) HasX() bool`

HasX returns a boolean if a field has been set.

### GetY

`func (o *DfdDiagramCellsInner) GetY() float32`

GetY returns the Y field if non-nil, zero value otherwise.

### GetYOk

`func (o *DfdDiagramCellsInner) GetYOk() (*float32, bool)`

GetYOk returns a tuple with the Y field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetY

`func (o *DfdDiagramCellsInner) SetY(v float32)`

SetY sets Y field to given value.

### HasY

`func (o *DfdDiagramCellsInner) HasY() bool`

HasY returns a boolean if a field has been set.

### GetWidth

`func (o *DfdDiagramCellsInner) GetWidth() float32`

GetWidth returns the Width field if non-nil, zero value otherwise.

### GetWidthOk

`func (o *DfdDiagramCellsInner) GetWidthOk() (*float32, bool)`

GetWidthOk returns a tuple with the Width field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWidth

`func (o *DfdDiagramCellsInner) SetWidth(v float32)`

SetWidth sets Width field to given value.

### HasWidth

`func (o *DfdDiagramCellsInner) HasWidth() bool`

HasWidth returns a boolean if a field has been set.

### GetHeight

`func (o *DfdDiagramCellsInner) GetHeight() float32`

GetHeight returns the Height field if non-nil, zero value otherwise.

### GetHeightOk

`func (o *DfdDiagramCellsInner) GetHeightOk() (*float32, bool)`

GetHeightOk returns a tuple with the Height field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHeight

`func (o *DfdDiagramCellsInner) SetHeight(v float32)`

SetHeight sets Height field to given value.

### HasHeight

`func (o *DfdDiagramCellsInner) HasHeight() bool`

HasHeight returns a boolean if a field has been set.

### GetSource

`func (o *DfdDiagramCellsInner) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *DfdDiagramCellsInner) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *DfdDiagramCellsInner) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *DfdDiagramCellsInner) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *DfdDiagramCellsInner) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *DfdDiagramCellsInner) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.


### GetLabels

`func (o *DfdDiagramCellsInner) GetLabels() []EdgeLabel`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *DfdDiagramCellsInner) GetLabelsOk() (*[]EdgeLabel, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *DfdDiagramCellsInner) SetLabels(v []EdgeLabel)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *DfdDiagramCellsInner) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetVertices

`func (o *DfdDiagramCellsInner) GetVertices() []Point`

GetVertices returns the Vertices field if non-nil, zero value otherwise.

### GetVerticesOk

`func (o *DfdDiagramCellsInner) GetVerticesOk() (*[]Point, bool)`

GetVerticesOk returns a tuple with the Vertices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVertices

`func (o *DfdDiagramCellsInner) SetVertices(v []Point)`

SetVertices sets Vertices field to given value.

### HasVertices

`func (o *DfdDiagramCellsInner) HasVertices() bool`

HasVertices returns a boolean if a field has been set.

### GetRouter

`func (o *DfdDiagramCellsInner) GetRouter() EdgeRouter`

GetRouter returns the Router field if non-nil, zero value otherwise.

### GetRouterOk

`func (o *DfdDiagramCellsInner) GetRouterOk() (*EdgeRouter, bool)`

GetRouterOk returns a tuple with the Router field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRouter

`func (o *DfdDiagramCellsInner) SetRouter(v EdgeRouter)`

SetRouter sets Router field to given value.

### HasRouter

`func (o *DfdDiagramCellsInner) HasRouter() bool`

HasRouter returns a boolean if a field has been set.

### GetConnector

`func (o *DfdDiagramCellsInner) GetConnector() EdgeConnector`

GetConnector returns the Connector field if non-nil, zero value otherwise.

### GetConnectorOk

`func (o *DfdDiagramCellsInner) GetConnectorOk() (*EdgeConnector, bool)`

GetConnectorOk returns a tuple with the Connector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnector

`func (o *DfdDiagramCellsInner) SetConnector(v EdgeConnector)`

SetConnector sets Connector field to given value.

### HasConnector

`func (o *DfdDiagramCellsInner) HasConnector() bool`

HasConnector returns a boolean if a field has been set.

### GetDefaultLabel

`func (o *DfdDiagramCellsInner) GetDefaultLabel() EdgeLabel`

GetDefaultLabel returns the DefaultLabel field if non-nil, zero value otherwise.

### GetDefaultLabelOk

`func (o *DfdDiagramCellsInner) GetDefaultLabelOk() (*EdgeLabel, bool)`

GetDefaultLabelOk returns a tuple with the DefaultLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultLabel

`func (o *DfdDiagramCellsInner) SetDefaultLabel(v EdgeLabel)`

SetDefaultLabel sets DefaultLabel field to given value.

### HasDefaultLabel

`func (o *DfdDiagramCellsInner) HasDefaultLabel() bool`

HasDefaultLabel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


