# BaseDiagram

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the diagram (UUID) | [readonly] 
**Name** | **string** | Name of the diagram | 
**Type** | **string** | Type of diagram with version | 
**CreatedAt** | **time.Time** | Creation timestamp (ISO3339) | [readonly] 
**ModifiedAt** | **time.Time** | Last modification timestamp (ISO3339) | [readonly] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional diagram metadata | [optional] 
**UpdateVector** | Pointer to **int64** | Server-managed monotonic version counter, incremented on each diagram update | [optional] [readonly] 
**Image** | Pointer to [**NullableBaseDiagramImage**](BaseDiagramImage.md) |  | [optional] 
**Description** | Pointer to **NullableString** | Optional description of the diagram | [optional] 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]

## Methods

### NewBaseDiagram

`func NewBaseDiagram(id string, name string, type_ string, createdAt time.Time, modifiedAt time.Time, ) *BaseDiagram`

NewBaseDiagram instantiates a new BaseDiagram object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewBaseDiagramWithDefaults

`func NewBaseDiagramWithDefaults() *BaseDiagram`

NewBaseDiagramWithDefaults instantiates a new BaseDiagram object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *BaseDiagram) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *BaseDiagram) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *BaseDiagram) SetId(v string)`

SetId sets Id field to given value.


### GetName

`func (o *BaseDiagram) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *BaseDiagram) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *BaseDiagram) SetName(v string)`

SetName sets Name field to given value.


### GetType

`func (o *BaseDiagram) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *BaseDiagram) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *BaseDiagram) SetType(v string)`

SetType sets Type field to given value.


### GetCreatedAt

`func (o *BaseDiagram) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *BaseDiagram) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *BaseDiagram) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetModifiedAt

`func (o *BaseDiagram) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *BaseDiagram) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *BaseDiagram) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.


### GetMetadata

`func (o *BaseDiagram) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *BaseDiagram) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *BaseDiagram) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *BaseDiagram) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *BaseDiagram) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *BaseDiagram) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetUpdateVector

`func (o *BaseDiagram) GetUpdateVector() int64`

GetUpdateVector returns the UpdateVector field if non-nil, zero value otherwise.

### GetUpdateVectorOk

`func (o *BaseDiagram) GetUpdateVectorOk() (*int64, bool)`

GetUpdateVectorOk returns a tuple with the UpdateVector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUpdateVector

`func (o *BaseDiagram) SetUpdateVector(v int64)`

SetUpdateVector sets UpdateVector field to given value.

### HasUpdateVector

`func (o *BaseDiagram) HasUpdateVector() bool`

HasUpdateVector returns a boolean if a field has been set.

### GetImage

`func (o *BaseDiagram) GetImage() BaseDiagramImage`

GetImage returns the Image field if non-nil, zero value otherwise.

### GetImageOk

`func (o *BaseDiagram) GetImageOk() (*BaseDiagramImage, bool)`

GetImageOk returns a tuple with the Image field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetImage

`func (o *BaseDiagram) SetImage(v BaseDiagramImage)`

SetImage sets Image field to given value.

### HasImage

`func (o *BaseDiagram) HasImage() bool`

HasImage returns a boolean if a field has been set.

### SetImageNil

`func (o *BaseDiagram) SetImageNil(b bool)`

 SetImageNil sets the value for Image to be an explicit nil

### UnsetImage
`func (o *BaseDiagram) UnsetImage()`

UnsetImage ensures that no value is present for Image, not even an explicit nil
### GetDescription

`func (o *BaseDiagram) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *BaseDiagram) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *BaseDiagram) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *BaseDiagram) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *BaseDiagram) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *BaseDiagram) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetIncludeInReport

`func (o *BaseDiagram) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *BaseDiagram) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *BaseDiagram) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *BaseDiagram) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


