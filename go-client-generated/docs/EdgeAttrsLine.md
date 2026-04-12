# EdgeAttrsLine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Stroke** | Pointer to **string** | Line color | [optional] 
**StrokeWidth** | Pointer to **float32** | Line width in pixels | [optional] 
**StrokeDasharray** | Pointer to **NullableString** | Dash pattern for the line | [optional] 
**TargetMarker** | Pointer to [**EdgeAttrsLineTargetMarker**](EdgeAttrsLineTargetMarker.md) |  | [optional] 
**SourceMarker** | Pointer to [**EdgeAttrsLineSourceMarker**](EdgeAttrsLineSourceMarker.md) |  | [optional] 

## Methods

### NewEdgeAttrsLine

`func NewEdgeAttrsLine() *EdgeAttrsLine`

NewEdgeAttrsLine instantiates a new EdgeAttrsLine object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEdgeAttrsLineWithDefaults

`func NewEdgeAttrsLineWithDefaults() *EdgeAttrsLine`

NewEdgeAttrsLineWithDefaults instantiates a new EdgeAttrsLine object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStroke

`func (o *EdgeAttrsLine) GetStroke() string`

GetStroke returns the Stroke field if non-nil, zero value otherwise.

### GetStrokeOk

`func (o *EdgeAttrsLine) GetStrokeOk() (*string, bool)`

GetStrokeOk returns a tuple with the Stroke field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStroke

`func (o *EdgeAttrsLine) SetStroke(v string)`

SetStroke sets Stroke field to given value.

### HasStroke

`func (o *EdgeAttrsLine) HasStroke() bool`

HasStroke returns a boolean if a field has been set.

### GetStrokeWidth

`func (o *EdgeAttrsLine) GetStrokeWidth() float32`

GetStrokeWidth returns the StrokeWidth field if non-nil, zero value otherwise.

### GetStrokeWidthOk

`func (o *EdgeAttrsLine) GetStrokeWidthOk() (*float32, bool)`

GetStrokeWidthOk returns a tuple with the StrokeWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrokeWidth

`func (o *EdgeAttrsLine) SetStrokeWidth(v float32)`

SetStrokeWidth sets StrokeWidth field to given value.

### HasStrokeWidth

`func (o *EdgeAttrsLine) HasStrokeWidth() bool`

HasStrokeWidth returns a boolean if a field has been set.

### GetStrokeDasharray

`func (o *EdgeAttrsLine) GetStrokeDasharray() string`

GetStrokeDasharray returns the StrokeDasharray field if non-nil, zero value otherwise.

### GetStrokeDasharrayOk

`func (o *EdgeAttrsLine) GetStrokeDasharrayOk() (*string, bool)`

GetStrokeDasharrayOk returns a tuple with the StrokeDasharray field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrokeDasharray

`func (o *EdgeAttrsLine) SetStrokeDasharray(v string)`

SetStrokeDasharray sets StrokeDasharray field to given value.

### HasStrokeDasharray

`func (o *EdgeAttrsLine) HasStrokeDasharray() bool`

HasStrokeDasharray returns a boolean if a field has been set.

### SetStrokeDasharrayNil

`func (o *EdgeAttrsLine) SetStrokeDasharrayNil(b bool)`

 SetStrokeDasharrayNil sets the value for StrokeDasharray to be an explicit nil

### UnsetStrokeDasharray
`func (o *EdgeAttrsLine) UnsetStrokeDasharray()`

UnsetStrokeDasharray ensures that no value is present for StrokeDasharray, not even an explicit nil
### GetTargetMarker

`func (o *EdgeAttrsLine) GetTargetMarker() EdgeAttrsLineTargetMarker`

GetTargetMarker returns the TargetMarker field if non-nil, zero value otherwise.

### GetTargetMarkerOk

`func (o *EdgeAttrsLine) GetTargetMarkerOk() (*EdgeAttrsLineTargetMarker, bool)`

GetTargetMarkerOk returns a tuple with the TargetMarker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetMarker

`func (o *EdgeAttrsLine) SetTargetMarker(v EdgeAttrsLineTargetMarker)`

SetTargetMarker sets TargetMarker field to given value.

### HasTargetMarker

`func (o *EdgeAttrsLine) HasTargetMarker() bool`

HasTargetMarker returns a boolean if a field has been set.

### GetSourceMarker

`func (o *EdgeAttrsLine) GetSourceMarker() EdgeAttrsLineSourceMarker`

GetSourceMarker returns the SourceMarker field if non-nil, zero value otherwise.

### GetSourceMarkerOk

`func (o *EdgeAttrsLine) GetSourceMarkerOk() (*EdgeAttrsLineSourceMarker, bool)`

GetSourceMarkerOk returns a tuple with the SourceMarker field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSourceMarker

`func (o *EdgeAttrsLine) SetSourceMarker(v EdgeAttrsLineSourceMarker)`

SetSourceMarker sets SourceMarker field to given value.

### HasSourceMarker

`func (o *EdgeAttrsLine) HasSourceMarker() bool`

HasSourceMarker returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


