# ColorPaletteEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Position** | **int32** | Display order position (1-8) | 
**Color** | **string** | Hex color value (#RGB or #RRGGBB), stored as lowercase #RRGGBB | 

## Methods

### NewColorPaletteEntry

`func NewColorPaletteEntry(position int32, color string, ) *ColorPaletteEntry`

NewColorPaletteEntry instantiates a new ColorPaletteEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewColorPaletteEntryWithDefaults

`func NewColorPaletteEntryWithDefaults() *ColorPaletteEntry`

NewColorPaletteEntryWithDefaults instantiates a new ColorPaletteEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPosition

`func (o *ColorPaletteEntry) GetPosition() int32`

GetPosition returns the Position field if non-nil, zero value otherwise.

### GetPositionOk

`func (o *ColorPaletteEntry) GetPositionOk() (*int32, bool)`

GetPositionOk returns a tuple with the Position field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPosition

`func (o *ColorPaletteEntry) SetPosition(v int32)`

SetPosition sets Position field to given value.


### GetColor

`func (o *ColorPaletteEntry) GetColor() string`

GetColor returns the Color field if non-nil, zero value otherwise.

### GetColorOk

`func (o *ColorPaletteEntry) GetColorOk() (*string, bool)`

GetColorOk returns a tuple with the Color field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColor

`func (o *ColorPaletteEntry) SetColor(v string)`

SetColor sets Color field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


