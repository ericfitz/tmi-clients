# Edge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Shape** | Pointer to **string** | Edge type identifier | [optional] 
**Source** | [**EdgeTerminal**](EdgeTerminal.md) | Source connection point | 
**Target** | [**EdgeTerminal**](EdgeTerminal.md) | Target connection point | 
**Attrs** | Pointer to [**EdgeAttrs**](EdgeAttrs.md) | Visual styling attributes for the edge | [optional] 
**Labels** | Pointer to [**[]EdgeLabel**](EdgeLabel.md) | Text labels positioned along the edge | [optional] 
**Vertices** | Pointer to [**[]Point**](Point.md) | Intermediate waypoints for edge routing | [optional] 
**Router** | Pointer to [**EdgeRouter**](EdgeRouter.md) | Edge routing algorithm configuration for path calculation | [optional] 
**Connector** | Pointer to [**EdgeConnector**](EdgeConnector.md) | Edge connector style configuration for visual appearance | [optional] 
**DefaultLabel** | Pointer to [**EdgeLabel**](EdgeLabel.md) | Default label configuration applied to edges without explicit labels | [optional] 

## Methods

### NewEdge

`func NewEdge(source EdgeTerminal, target EdgeTerminal, ) *Edge`

NewEdge instantiates a new Edge object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeWithDefaults

`func NewEdgeWithDefaults() *Edge`

NewEdgeWithDefaults instantiates a new Edge object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetShape

`func (o *Edge) GetShape() string`

GetShape returns the Shape field if non-nil, zero value otherwise.

### GetShapeOk

`func (o *Edge) GetShapeOk() (*string, bool)`

GetShapeOk returns a tuple with the Shape field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShape

`func (o *Edge) SetShape(v string)`

SetShape sets Shape field to given value.

### HasShape

`func (o *Edge) HasShape() bool`

HasShape returns a boolean if a field has been set.

### GetSource

`func (o *Edge) GetSource() EdgeTerminal`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *Edge) GetSourceOk() (*EdgeTerminal, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *Edge) SetSource(v EdgeTerminal)`

SetSource sets Source field to given value.


### GetTarget

`func (o *Edge) GetTarget() EdgeTerminal`

GetTarget returns the Target field if non-nil, zero value otherwise.

### GetTargetOk

`func (o *Edge) GetTargetOk() (*EdgeTerminal, bool)`

GetTargetOk returns a tuple with the Target field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTarget

`func (o *Edge) SetTarget(v EdgeTerminal)`

SetTarget sets Target field to given value.


### GetAttrs

`func (o *Edge) GetAttrs() EdgeAttrs`

GetAttrs returns the Attrs field if non-nil, zero value otherwise.

### GetAttrsOk

`func (o *Edge) GetAttrsOk() (*EdgeAttrs, bool)`

GetAttrsOk returns a tuple with the Attrs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttrs

`func (o *Edge) SetAttrs(v EdgeAttrs)`

SetAttrs sets Attrs field to given value.

### HasAttrs

`func (o *Edge) HasAttrs() bool`

HasAttrs returns a boolean if a field has been set.

### GetLabels

`func (o *Edge) GetLabels() []EdgeLabel`

GetLabels returns the Labels field if non-nil, zero value otherwise.

### GetLabelsOk

`func (o *Edge) GetLabelsOk() (*[]EdgeLabel, bool)`

GetLabelsOk returns a tuple with the Labels field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLabels

`func (o *Edge) SetLabels(v []EdgeLabel)`

SetLabels sets Labels field to given value.

### HasLabels

`func (o *Edge) HasLabels() bool`

HasLabels returns a boolean if a field has been set.

### GetVertices

`func (o *Edge) GetVertices() []Point`

GetVertices returns the Vertices field if non-nil, zero value otherwise.

### GetVerticesOk

`func (o *Edge) GetVerticesOk() (*[]Point, bool)`

GetVerticesOk returns a tuple with the Vertices field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVertices

`func (o *Edge) SetVertices(v []Point)`

SetVertices sets Vertices field to given value.

### HasVertices

`func (o *Edge) HasVertices() bool`

HasVertices returns a boolean if a field has been set.

### GetRouter

`func (o *Edge) GetRouter() EdgeRouter`

GetRouter returns the Router field if non-nil, zero value otherwise.

### GetRouterOk

`func (o *Edge) GetRouterOk() (*EdgeRouter, bool)`

GetRouterOk returns a tuple with the Router field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRouter

`func (o *Edge) SetRouter(v EdgeRouter)`

SetRouter sets Router field to given value.

### HasRouter

`func (o *Edge) HasRouter() bool`

HasRouter returns a boolean if a field has been set.

### GetConnector

`func (o *Edge) GetConnector() EdgeConnector`

GetConnector returns the Connector field if non-nil, zero value otherwise.

### GetConnectorOk

`func (o *Edge) GetConnectorOk() (*EdgeConnector, bool)`

GetConnectorOk returns a tuple with the Connector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnector

`func (o *Edge) SetConnector(v EdgeConnector)`

SetConnector sets Connector field to given value.

### HasConnector

`func (o *Edge) HasConnector() bool`

HasConnector returns a boolean if a field has been set.

### GetDefaultLabel

`func (o *Edge) GetDefaultLabel() EdgeLabel`

GetDefaultLabel returns the DefaultLabel field if non-nil, zero value otherwise.

### GetDefaultLabelOk

`func (o *Edge) GetDefaultLabelOk() (*EdgeLabel, bool)`

GetDefaultLabelOk returns a tuple with the DefaultLabel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDefaultLabel

`func (o *Edge) SetDefaultLabel(v EdgeLabel)`

SetDefaultLabel sets DefaultLabel field to given value.

### HasDefaultLabel

`func (o *Edge) HasDefaultLabel() bool`

HasDefaultLabel returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


