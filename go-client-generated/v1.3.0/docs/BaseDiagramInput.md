# BaseDiagramInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the diagram | 
**Type** | **string** | Type of diagram with version | 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**Image** | Pointer to [**NullableBaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**Description** | Pointer to **NullableString** | Optional description of the diagram | [optional] 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**ColorPalette** | Pointer to [**[]ColorPaletteEntry**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 

## Methods

### NewBaseDiagramInput

`func NewBaseDiagramInput(name string, type_ string, ) *BaseDiagramInput`

NewBaseDiagramInput instantiates a new BaseDiagramInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBaseDiagramInputWithDefaults

`func NewBaseDiagramInputWithDefaults() *BaseDiagramInput`

NewBaseDiagramInputWithDefaults instantiates a new BaseDiagramInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *BaseDiagramInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BaseDiagramInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BaseDiagramInput) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *BaseDiagramInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BaseDiagramInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BaseDiagramInput) SetType(v string)`

SetType sets Type field to given value.


### GetMetadata

`func (o *BaseDiagramInput) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *BaseDiagramInput) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *BaseDiagramInput) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *BaseDiagramInput) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *BaseDiagramInput) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *BaseDiagramInput) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetImage

`func (o *BaseDiagramInput) GetImage() BaseDiagramImage`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *BaseDiagramInput) GetImageOk() (*BaseDiagramImage, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *BaseDiagramInput) SetImage(v BaseDiagramImage)`

SetImage sets Image field to given value.

### HasImage

`func (o *BaseDiagramInput) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *BaseDiagramInput) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *BaseDiagramInput) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetDescription

`func (o *BaseDiagramInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BaseDiagramInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BaseDiagramInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BaseDiagramInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *BaseDiagramInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *BaseDiagramInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIncludeInReport

`func (o *BaseDiagramInput) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *BaseDiagramInput) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *BaseDiagramInput) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *BaseDiagramInput) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *BaseDiagramInput) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *BaseDiagramInput) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *BaseDiagramInput) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *BaseDiagramInput) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetColorPalette

`func (o *BaseDiagramInput) GetColorPalette() []ColorPaletteEntry`

GetColorPalette returns the ColorPalette field if non-nil, zero value otherwise.

### GetColorPaletteOk

`func (o *BaseDiagramInput) GetColorPaletteOk() (*[]ColorPaletteEntry, bool)`

GetColorPaletteOk returns a tuple with the ColorPalette field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorPalette

`func (o *BaseDiagramInput) SetColorPalette(v []ColorPaletteEntry)`

SetColorPalette sets ColorPalette field to given value.

### HasColorPalette

`func (o *BaseDiagramInput) HasColorPalette() bool`

HasColorPalette returns a boolean if a field has been set.

### SetColorPaletteNil

`func (o *BaseDiagramInput) SetColorPaletteNil(b bool)`

 SetColorPaletteNil sets the value for ColorPalette to be an explicit nil

### UnsetColorPalette
`func (o *BaseDiagramInput) UnsetColorPalette()`

UnsetColorPalette ensures that no value is present for ColorPalette, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


