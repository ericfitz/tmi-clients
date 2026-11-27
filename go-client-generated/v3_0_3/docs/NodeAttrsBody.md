# NodeAttrsBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Fill** | Pointer to **string** | Fill color | [optional] 
**Stroke** | Pointer to **string** | Stroke color | [optional] 
**StrokeWidth** | Pointer to **float32** | Stroke width in pixels | [optional] 
**StrokeDasharray** | Pointer to **NullableString** | Dash pattern for strokes | [optional] 
**Rx** | Pointer to **float32** | Corner radius along the x-axis (set as default by X6 shape registrations, e.g., actor/process/security-boundary) | [optional] 
**Ry** | Pointer to **float32** | Corner radius along the y-axis (set as default by X6 shape registrations) | [optional] 
**Lateral** | Pointer to **float32** | Cylinder lateral parameter for the X6 &#39;store&#39; shape (drives the body &#39;d&#39; path computation) | [optional] 
**RefWidth** | Pointer to [**NodeAttrsBodyRefWidth**](NodeAttrsBodyRefWidth.md) |  | [optional] 
**RefHeight** | Pointer to [**NodeAttrsBodyRefHeight**](NodeAttrsBodyRefHeight.md) |  | [optional] 
**FillOpacity** | Pointer to **float32** | Body fill opacity (0-1); typically transient drag-to-embed visual feedback | [optional] 

## Methods

### NewNodeAttrsBody

`func NewNodeAttrsBody() *NodeAttrsBody`

NewNodeAttrsBody instantiates a new NodeAttrsBody object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNodeAttrsBodyWithDefaults

`func NewNodeAttrsBodyWithDefaults() *NodeAttrsBody`

NewNodeAttrsBodyWithDefaults instantiates a new NodeAttrsBody object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetFill

`func (o *NodeAttrsBody) GetFill() string`

GetFill returns the Fill field if non-nil, zero value otherwise.

### GetFillOk

`func (o *NodeAttrsBody) GetFillOk() (*string, bool)`

GetFillOk returns a tuple with the Fill field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFill

`func (o *NodeAttrsBody) SetFill(v string)`

SetFill sets Fill field to given value.

### HasFill

`func (o *NodeAttrsBody) HasFill() bool`

HasFill returns a boolean if a field has been set.

### GetStroke

`func (o *NodeAttrsBody) GetStroke() string`

GetStroke returns the Stroke field if non-nil, zero value otherwise.

### GetStrokeOk

`func (o *NodeAttrsBody) GetStrokeOk() (*string, bool)`

GetStrokeOk returns a tuple with the Stroke field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStroke

`func (o *NodeAttrsBody) SetStroke(v string)`

SetStroke sets Stroke field to given value.

### HasStroke

`func (o *NodeAttrsBody) HasStroke() bool`

HasStroke returns a boolean if a field has been set.

### GetStrokeWidth

`func (o *NodeAttrsBody) GetStrokeWidth() float32`

GetStrokeWidth returns the StrokeWidth field if non-nil, zero value otherwise.

### GetStrokeWidthOk

`func (o *NodeAttrsBody) GetStrokeWidthOk() (*float32, bool)`

GetStrokeWidthOk returns a tuple with the StrokeWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrokeWidth

`func (o *NodeAttrsBody) SetStrokeWidth(v float32)`

SetStrokeWidth sets StrokeWidth field to given value.

### HasStrokeWidth

`func (o *NodeAttrsBody) HasStrokeWidth() bool`

HasStrokeWidth returns a boolean if a field has been set.

### GetStrokeDasharray

`func (o *NodeAttrsBody) GetStrokeDasharray() string`

GetStrokeDasharray returns the StrokeDasharray field if non-nil, zero value otherwise.

### GetStrokeDasharrayOk

`func (o *NodeAttrsBody) GetStrokeDasharrayOk() (*string, bool)`

GetStrokeDasharrayOk returns a tuple with the StrokeDasharray field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStrokeDasharray

`func (o *NodeAttrsBody) SetStrokeDasharray(v string)`

SetStrokeDasharray sets StrokeDasharray field to given value.

### HasStrokeDasharray

`func (o *NodeAttrsBody) HasStrokeDasharray() bool`

HasStrokeDasharray returns a boolean if a field has been set.

### SetStrokeDasharrayNil

`func (o *NodeAttrsBody) SetStrokeDasharrayNil(b bool)`

 SetStrokeDasharrayNil sets the value for StrokeDasharray to be an explicit nil

### UnsetStrokeDasharray
`func (o *NodeAttrsBody) UnsetStrokeDasharray()`

UnsetStrokeDasharray ensures that no value is present for StrokeDasharray, not even an explicit nil
### GetRx

`func (o *NodeAttrsBody) GetRx() float32`

GetRx returns the Rx field if non-nil, zero value otherwise.

### GetRxOk

`func (o *NodeAttrsBody) GetRxOk() (*float32, bool)`

GetRxOk returns a tuple with the Rx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRx

`func (o *NodeAttrsBody) SetRx(v float32)`

SetRx sets Rx field to given value.

### HasRx

`func (o *NodeAttrsBody) HasRx() bool`

HasRx returns a boolean if a field has been set.

### GetRy

`func (o *NodeAttrsBody) GetRy() float32`

GetRy returns the Ry field if non-nil, zero value otherwise.

### GetRyOk

`func (o *NodeAttrsBody) GetRyOk() (*float32, bool)`

GetRyOk returns a tuple with the Ry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRy

`func (o *NodeAttrsBody) SetRy(v float32)`

SetRy sets Ry field to given value.

### HasRy

`func (o *NodeAttrsBody) HasRy() bool`

HasRy returns a boolean if a field has been set.

### GetLateral

`func (o *NodeAttrsBody) GetLateral() float32`

GetLateral returns the Lateral field if non-nil, zero value otherwise.

### GetLateralOk

`func (o *NodeAttrsBody) GetLateralOk() (*float32, bool)`

GetLateralOk returns a tuple with the Lateral field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLateral

`func (o *NodeAttrsBody) SetLateral(v float32)`

SetLateral sets Lateral field to given value.

### HasLateral

`func (o *NodeAttrsBody) HasLateral() bool`

HasLateral returns a boolean if a field has been set.

### GetRefWidth

`func (o *NodeAttrsBody) GetRefWidth() NodeAttrsBodyRefWidth`

GetRefWidth returns the RefWidth field if non-nil, zero value otherwise.

### GetRefWidthOk

`func (o *NodeAttrsBody) GetRefWidthOk() (*NodeAttrsBodyRefWidth, bool)`

GetRefWidthOk returns a tuple with the RefWidth field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefWidth

`func (o *NodeAttrsBody) SetRefWidth(v NodeAttrsBodyRefWidth)`

SetRefWidth sets RefWidth field to given value.

### HasRefWidth

`func (o *NodeAttrsBody) HasRefWidth() bool`

HasRefWidth returns a boolean if a field has been set.

### GetRefHeight

`func (o *NodeAttrsBody) GetRefHeight() NodeAttrsBodyRefHeight`

GetRefHeight returns the RefHeight field if non-nil, zero value otherwise.

### GetRefHeightOk

`func (o *NodeAttrsBody) GetRefHeightOk() (*NodeAttrsBodyRefHeight, bool)`

GetRefHeightOk returns a tuple with the RefHeight field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefHeight

`func (o *NodeAttrsBody) SetRefHeight(v NodeAttrsBodyRefHeight)`

SetRefHeight sets RefHeight field to given value.

### HasRefHeight

`func (o *NodeAttrsBody) HasRefHeight() bool`

HasRefHeight returns a boolean if a field has been set.

### GetFillOpacity

`func (o *NodeAttrsBody) GetFillOpacity() float32`

GetFillOpacity returns the FillOpacity field if non-nil, zero value otherwise.

### GetFillOpacityOk

`func (o *NodeAttrsBody) GetFillOpacityOk() (*float32, bool)`

GetFillOpacityOk returns a tuple with the FillOpacity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFillOpacity

`func (o *NodeAttrsBody) SetFillOpacity(v float32)`

SetFillOpacity sets FillOpacity field to given value.

### HasFillOpacity

`func (o *NodeAttrsBody) HasFillOpacity() bool`

HasFillOpacity returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


