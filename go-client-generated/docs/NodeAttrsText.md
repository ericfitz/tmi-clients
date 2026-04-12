# NodeAttrsText

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Text** | Pointer to **string** | Label text content | [optional] 
**FontSize** | Pointer to **float32** | Font size in pixels | [optional] 
**Fill** | Pointer to **string** | Text color | [optional] 
**FontFamily** | Pointer to **string** | Font family | [optional] 
**RefX** | Pointer to [**NodeAttrsTextRefX**](NodeAttrsTextRefX.md) |  | [optional] 
**RefY** | Pointer to [**NodeAttrsTextRefY**](NodeAttrsTextRefY.md) |  | [optional] 
**RefDx** | Pointer to **float32** | Horizontal offset from refX | [optional] 
**RefDy** | Pointer to **float32** | Vertical offset from refY | [optional] 
**TextAnchor** | Pointer to **string** | Horizontal text alignment anchor point | [optional] 
**TextVerticalAnchor** | Pointer to **string** | Vertical text alignment anchor point | [optional] 

## Methods

### NewNodeAttrsText

`func NewNodeAttrsText() *NodeAttrsText`

NewNodeAttrsText instantiates a new NodeAttrsText object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewNodeAttrsTextWithDefaults

`func NewNodeAttrsTextWithDefaults() *NodeAttrsText`

NewNodeAttrsTextWithDefaults instantiates a new NodeAttrsText object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetText

`func (o *NodeAttrsText) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *NodeAttrsText) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *NodeAttrsText) SetText(v string)`

SetText sets Text field to given value.

### HasText

`func (o *NodeAttrsText) HasText() bool`

HasText returns a boolean if a field has been set.

### GetFontSize

`func (o *NodeAttrsText) GetFontSize() float32`

GetFontSize returns the FontSize field if non-nil, zero value otherwise.

### GetFontSizeOk

`func (o *NodeAttrsText) GetFontSizeOk() (*float32, bool)`

GetFontSizeOk returns a tuple with the FontSize field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFontSize

`func (o *NodeAttrsText) SetFontSize(v float32)`

SetFontSize sets FontSize field to given value.

### HasFontSize

`func (o *NodeAttrsText) HasFontSize() bool`

HasFontSize returns a boolean if a field has been set.

### GetFill

`func (o *NodeAttrsText) GetFill() string`

GetFill returns the Fill field if non-nil, zero value otherwise.

### GetFillOk

`func (o *NodeAttrsText) GetFillOk() (*string, bool)`

GetFillOk returns a tuple with the Fill field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFill

`func (o *NodeAttrsText) SetFill(v string)`

SetFill sets Fill field to given value.

### HasFill

`func (o *NodeAttrsText) HasFill() bool`

HasFill returns a boolean if a field has been set.

### GetFontFamily

`func (o *NodeAttrsText) GetFontFamily() string`

GetFontFamily returns the FontFamily field if non-nil, zero value otherwise.

### GetFontFamilyOk

`func (o *NodeAttrsText) GetFontFamilyOk() (*string, bool)`

GetFontFamilyOk returns a tuple with the FontFamily field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFontFamily

`func (o *NodeAttrsText) SetFontFamily(v string)`

SetFontFamily sets FontFamily field to given value.

### HasFontFamily

`func (o *NodeAttrsText) HasFontFamily() bool`

HasFontFamily returns a boolean if a field has been set.

### GetRefX

`func (o *NodeAttrsText) GetRefX() NodeAttrsTextRefX`

GetRefX returns the RefX field if non-nil, zero value otherwise.

### GetRefXOk

`func (o *NodeAttrsText) GetRefXOk() (*NodeAttrsTextRefX, bool)`

GetRefXOk returns a tuple with the RefX field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefX

`func (o *NodeAttrsText) SetRefX(v NodeAttrsTextRefX)`

SetRefX sets RefX field to given value.

### HasRefX

`func (o *NodeAttrsText) HasRefX() bool`

HasRefX returns a boolean if a field has been set.

### GetRefY

`func (o *NodeAttrsText) GetRefY() NodeAttrsTextRefY`

GetRefY returns the RefY field if non-nil, zero value otherwise.

### GetRefYOk

`func (o *NodeAttrsText) GetRefYOk() (*NodeAttrsTextRefY, bool)`

GetRefYOk returns a tuple with the RefY field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefY

`func (o *NodeAttrsText) SetRefY(v NodeAttrsTextRefY)`

SetRefY sets RefY field to given value.

### HasRefY

`func (o *NodeAttrsText) HasRefY() bool`

HasRefY returns a boolean if a field has been set.

### GetRefDx

`func (o *NodeAttrsText) GetRefDx() float32`

GetRefDx returns the RefDx field if non-nil, zero value otherwise.

### GetRefDxOk

`func (o *NodeAttrsText) GetRefDxOk() (*float32, bool)`

GetRefDxOk returns a tuple with the RefDx field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefDx

`func (o *NodeAttrsText) SetRefDx(v float32)`

SetRefDx sets RefDx field to given value.

### HasRefDx

`func (o *NodeAttrsText) HasRefDx() bool`

HasRefDx returns a boolean if a field has been set.

### GetRefDy

`func (o *NodeAttrsText) GetRefDy() float32`

GetRefDy returns the RefDy field if non-nil, zero value otherwise.

### GetRefDyOk

`func (o *NodeAttrsText) GetRefDyOk() (*float32, bool)`

GetRefDyOk returns a tuple with the RefDy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRefDy

`func (o *NodeAttrsText) SetRefDy(v float32)`

SetRefDy sets RefDy field to given value.

### HasRefDy

`func (o *NodeAttrsText) HasRefDy() bool`

HasRefDy returns a boolean if a field has been set.

### GetTextAnchor

`func (o *NodeAttrsText) GetTextAnchor() string`

GetTextAnchor returns the TextAnchor field if non-nil, zero value otherwise.

### GetTextAnchorOk

`func (o *NodeAttrsText) GetTextAnchorOk() (*string, bool)`

GetTextAnchorOk returns a tuple with the TextAnchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextAnchor

`func (o *NodeAttrsText) SetTextAnchor(v string)`

SetTextAnchor sets TextAnchor field to given value.

### HasTextAnchor

`func (o *NodeAttrsText) HasTextAnchor() bool`

HasTextAnchor returns a boolean if a field has been set.

### GetTextVerticalAnchor

`func (o *NodeAttrsText) GetTextVerticalAnchor() string`

GetTextVerticalAnchor returns the TextVerticalAnchor field if non-nil, zero value otherwise.

### GetTextVerticalAnchorOk

`func (o *NodeAttrsText) GetTextVerticalAnchorOk() (*string, bool)`

GetTextVerticalAnchorOk returns a tuple with the TextVerticalAnchor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTextVerticalAnchor

`func (o *NodeAttrsText) SetTextVerticalAnchor(v string)`

SetTextVerticalAnchor sets TextVerticalAnchor field to given value.

### HasTextVerticalAnchor

`func (o *NodeAttrsText) HasTextVerticalAnchor() bool`

HasTextVerticalAnchor returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


