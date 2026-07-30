# DiagramListItemImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Svg** | Pointer to **string** | BASE64 encoded SVG representation of the diagram, used for thumbnails and reports | [optional] 
**UpdateVector** | Pointer to **int64** | Version of the diagram when this SVG was generated | [optional] 

## Methods

### NewDiagramListItemImage

`func NewDiagramListItemImage() *DiagramListItemImage`

NewDiagramListItemImage instantiates a new DiagramListItemImage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDiagramListItemImageWithDefaults

`func NewDiagramListItemImageWithDefaults() *DiagramListItemImage`

NewDiagramListItemImageWithDefaults instantiates a new DiagramListItemImage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSvg

`func (o *DiagramListItemImage) GetSvg() string`

GetSvg returns the Svg field if non-nil, zero value otherwise.

### GetSvgOk

`func (o *DiagramListItemImage) GetSvgOk() (*string, bool)`

GetSvgOk returns a tuple with the Svg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSvg

`func (o *DiagramListItemImage) SetSvg(v string)`

SetSvg sets Svg field to given value.

### HasSvg

`func (o *DiagramListItemImage) HasSvg() bool`

HasSvg returns a boolean if a field has been set.

### GetUpdateVector

`func (o *DiagramListItemImage) GetUpdateVector() int64`

GetUpdateVector returns the UpdateVector field if non-nil, zero value otherwise.

### GetUpdateVectorOk

`func (o *DiagramListItemImage) GetUpdateVectorOk() (*int64, bool)`

GetUpdateVectorOk returns a tuple with the UpdateVector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateVector

`func (o *DiagramListItemImage) SetUpdateVector(v int64)`

SetUpdateVector sets UpdateVector field to given value.

### HasUpdateVector

`func (o *DiagramListItemImage) HasUpdateVector() bool`

HasUpdateVector returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


