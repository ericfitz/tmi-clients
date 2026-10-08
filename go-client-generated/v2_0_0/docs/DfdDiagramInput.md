# DfdDiagramInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the diagram | 
**Type** | **string** | DFD diagram type with version | 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**Image** | Pointer to [**NullableDfdDiagramImage**](DfdDiagramImage.md) |  | [optional] 
**Description** | Pointer to **NullableString** | Optional description of the diagram | [optional] 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**ColorPalette** | Pointer to [**[]ColorPaletteEntry**](ColorPaletteEntry.md) | Custom color palette for diagram elements, ordered by position | [optional] 
**Cells** | [**[]DfdDiagramCellsInner**](DfdDiagramCellsInner.md) | List of diagram cells (nodes and edges) following X6 structure | 

## Methods

### NewDfdDiagramInput

`func NewDfdDiagramInput(name string, type_ string, cells []DfdDiagramCellsInner, ) *DfdDiagramInput`

NewDfdDiagramInput instantiates a new DfdDiagramInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDfdDiagramInputWithDefaults

`func NewDfdDiagramInputWithDefaults() *DfdDiagramInput`

NewDfdDiagramInputWithDefaults instantiates a new DfdDiagramInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *DfdDiagramInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *DfdDiagramInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *DfdDiagramInput) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *DfdDiagramInput) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DfdDiagramInput) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DfdDiagramInput) SetType(v string)`

SetType sets Type field to given value.


### GetMetadata

`func (o *DfdDiagramInput) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *DfdDiagramInput) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *DfdDiagramInput) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *DfdDiagramInput) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *DfdDiagramInput) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *DfdDiagramInput) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetImage

`func (o *DfdDiagramInput) GetImage() DfdDiagramImage`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *DfdDiagramInput) GetImageOk() (*DfdDiagramImage, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *DfdDiagramInput) SetImage(v DfdDiagramImage)`

SetImage sets Image field to given value.

### HasImage

`func (o *DfdDiagramInput) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *DfdDiagramInput) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *DfdDiagramInput) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetDescription

`func (o *DfdDiagramInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *DfdDiagramInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *DfdDiagramInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *DfdDiagramInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *DfdDiagramInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *DfdDiagramInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIncludeInReport

`func (o *DfdDiagramInput) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *DfdDiagramInput) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *DfdDiagramInput) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *DfdDiagramInput) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *DfdDiagramInput) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *DfdDiagramInput) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *DfdDiagramInput) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *DfdDiagramInput) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetColorPalette

`func (o *DfdDiagramInput) GetColorPalette() []ColorPaletteEntry`

GetColorPalette returns the ColorPalette field if non-nil, zero value otherwise.

### GetColorPaletteOk

`func (o *DfdDiagramInput) GetColorPaletteOk() (*[]ColorPaletteEntry, bool)`

GetColorPaletteOk returns a tuple with the ColorPalette field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetColorPalette

`func (o *DfdDiagramInput) SetColorPalette(v []ColorPaletteEntry)`

SetColorPalette sets ColorPalette field to given value.

### HasColorPalette

`func (o *DfdDiagramInput) HasColorPalette() bool`

HasColorPalette returns a boolean if a field has been set.

### SetColorPaletteNil

`func (o *DfdDiagramInput) SetColorPaletteNil(b bool)`

 SetColorPaletteNil sets the value for ColorPalette to be an explicit nil

### UnsetColorPalette
`func (o *DfdDiagramInput) UnsetColorPalette()`

UnsetColorPalette ensures that no value is present for ColorPalette, not even an explicit nil
### GetCells

`func (o *DfdDiagramInput) GetCells() []DfdDiagramCellsInner`

GetCells returns the Cells field if non-nil, zero value otherwise.

### GetCellsOk

`func (o *DfdDiagramInput) GetCellsOk() (*[]DfdDiagramCellsInner, bool)`

GetCellsOk returns a tuple with the Cells field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCells

`func (o *DfdDiagramInput) SetCells(v []DfdDiagramCellsInner)`

SetCells sets Cells field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


