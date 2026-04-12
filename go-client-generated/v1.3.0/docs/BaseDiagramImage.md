# BaseDiagramImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Svg** | Pointer to **string** | BASE64 encoded SVG representation of the diagram, used for thumbnails and reports | [optional] 
**UpdateVector** | Pointer to **int64** | Version of the diagram when this SVG was generated. If not provided when svg is updated, will be auto-set to BaseDiagram.update_vector | [optional] 

## Methods

### NewBaseDiagramImage

`func NewBaseDiagramImage() *BaseDiagramImage`

NewBaseDiagramImage instantiates a new BaseDiagramImage object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBaseDiagramImageWithDefaults

`func NewBaseDiagramImageWithDefaults() *BaseDiagramImage`

NewBaseDiagramImageWithDefaults instantiates a new BaseDiagramImage object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSvg

`func (o *BaseDiagramImage) GetSvg() string`

GetSvg returns the Svg field if non-nil, zero value otherwise.

### GetSvgOk

`func (o *BaseDiagramImage) GetSvgOk() (*string, bool)`

GetSvgOk returns a tuple with the Svg field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSvg

`func (o *BaseDiagramImage) SetSvg(v string)`

SetSvg sets Svg field to given value.

### HasSvg

`func (o *BaseDiagramImage) HasSvg() bool`

HasSvg returns a boolean if a field has been set.

### GetUpdateVector

`func (o *BaseDiagramImage) GetUpdateVector() int64`

GetUpdateVector returns the UpdateVector field if non-nil, zero value otherwise.

### GetUpdateVectorOk

`func (o *BaseDiagramImage) GetUpdateVectorOk() (*int64, bool)`

GetUpdateVectorOk returns a tuple with the UpdateVector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateVector

`func (o *BaseDiagramImage) SetUpdateVector(v int64)`

SetUpdateVector sets UpdateVector field to given value.

### HasUpdateVector

`func (o *BaseDiagramImage) HasUpdateVector() bool`

HasUpdateVector returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


