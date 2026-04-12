# Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Document name | 
**Description** | Pointer to **NullableString** | Description of document purpose or content | [optional] 
**Uri** | **string** | URL location of the document | 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Id** | **string** | Unique identifier for the document | [readonly] 
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Optional metadata key-value pairs | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**DeletedAt** | Pointer to **NullableTime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 
**AccessStatus** | Pointer to **string** | Access validation status for external content providers | [optional] [readonly] [default to "unknown"]
**ContentSource** | Pointer to **NullableString** | Content provider that handles this documents URI (e.g., google_drive, http) | [optional] [readonly] 

## Methods

### NewDocument

`func NewDocument(name string, uri string, id string, ) *Document`

NewDocument instantiates a new Document object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentWithDefaults

`func NewDocumentWithDefaults() *Document`

NewDocumentWithDefaults instantiates a new Document object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Document) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Document) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Document) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Document) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Document) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Document) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Document) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Document) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Document) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetUri

`func (o *Document) GetUri() string`

GetUri returns the Uri field if non-nil, zero value otherwise.

### GetUriOk

`func (o *Document) GetUriOk() (*string, bool)`

GetUriOk returns a tuple with the Uri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUri

`func (o *Document) SetUri(v string)`

SetUri sets Uri field to given value.


### GetIncludeInReport

`func (o *Document) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *Document) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *Document) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *Document) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *Document) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *Document) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *Document) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *Document) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetId

`func (o *Document) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Document) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Document) SetId(v string)`

SetId sets Id field to given value.


### GetMetadata

`func (o *Document) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Document) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Document) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Document) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Document) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Document) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Document) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Document) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *Document) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *Document) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *Document) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *Document) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetDeletedAt

`func (o *Document) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *Document) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *Document) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *Document) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *Document) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *Document) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil
### GetAccessStatus

`func (o *Document) GetAccessStatus() string`

GetAccessStatus returns the AccessStatus field if non-nil, zero value otherwise.

### GetAccessStatusOk

`func (o *Document) GetAccessStatusOk() (*string, bool)`

GetAccessStatusOk returns a tuple with the AccessStatus field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessStatus

`func (o *Document) SetAccessStatus(v string)`

SetAccessStatus sets AccessStatus field to given value.

### HasAccessStatus

`func (o *Document) HasAccessStatus() bool`

HasAccessStatus returns a boolean if a field has been set.

### GetContentSource

`func (o *Document) GetContentSource() string`

GetContentSource returns the ContentSource field if non-nil, zero value otherwise.

### GetContentSourceOk

`func (o *Document) GetContentSourceOk() (*string, bool)`

GetContentSourceOk returns a tuple with the ContentSource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContentSource

`func (o *Document) SetContentSource(v string)`

SetContentSource sets ContentSource field to given value.

### HasContentSource

`func (o *Document) HasContentSource() bool`

HasContentSource returns a boolean if a field has been set.

### SetContentSourceNil

`func (o *Document) SetContentSourceNil(b bool)`

 SetContentSourceNil sets the value for ContentSource to be an explicit nil

### UnsetContentSource
`func (o *Document) UnsetContentSource()`

UnsetContentSource ensures that no value is present for ContentSource, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


