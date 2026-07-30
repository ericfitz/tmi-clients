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
**AccessDiagnostics** | Pointer to **map[string]interface{}** | Per-viewer access diagnostics; present when access_status is not &#39;accessible&#39; | [optional] [readonly] 
**AccessStatusUpdatedAt** | Pointer to **NullableTime** | Timestamp of the last access_status transition (RFC3339) | [optional] [readonly] 
**Alias** | Pointer to **int32** | Server-assigned monotonically-increasing integer alias, unique within the parent threat model. Immutable after creation. | [optional] [readonly] 
**Version** | Pointer to **int32** | Server-managed monotonically-increasing optimistic-locking version. Returned on reads and bumped by every successful PUT/PATCH. Clients echo this back via the If-Match request header (preferred) or the body &#39;version&#39; field on the next mutation. A mismatch returns 409 Conflict. See issue #385. | [optional] [readonly] 

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
### GetAccessDiagnostics

`func (o *Document) GetAccessDiagnostics() map[string]interface{}`

GetAccessDiagnostics returns the AccessDiagnostics field if non-nil, zero value otherwise.

### GetAccessDiagnosticsOk

`func (o *Document) GetAccessDiagnosticsOk() (*map[string]interface{}, bool)`

GetAccessDiagnosticsOk returns a tuple with the AccessDiagnostics field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessDiagnostics

`func (o *Document) SetAccessDiagnostics(v map[string]interface{})`

SetAccessDiagnostics sets AccessDiagnostics field to given value.

### HasAccessDiagnostics

`func (o *Document) HasAccessDiagnostics() bool`

HasAccessDiagnostics returns a boolean if a field has been set.

### SetAccessDiagnosticsNil

`func (o *Document) SetAccessDiagnosticsNil(b bool)`

 SetAccessDiagnosticsNil sets the value for AccessDiagnostics to be an explicit nil

### UnsetAccessDiagnostics
`func (o *Document) UnsetAccessDiagnostics()`

UnsetAccessDiagnostics ensures that no value is present for AccessDiagnostics, not even an explicit nil
### GetAccessStatusUpdatedAt

`func (o *Document) GetAccessStatusUpdatedAt() time.Time`

GetAccessStatusUpdatedAt returns the AccessStatusUpdatedAt field if non-nil, zero value otherwise.

### GetAccessStatusUpdatedAtOk

`func (o *Document) GetAccessStatusUpdatedAtOk() (*time.Time, bool)`

GetAccessStatusUpdatedAtOk returns a tuple with the AccessStatusUpdatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAccessStatusUpdatedAt

`func (o *Document) SetAccessStatusUpdatedAt(v time.Time)`

SetAccessStatusUpdatedAt sets AccessStatusUpdatedAt field to given value.

### HasAccessStatusUpdatedAt

`func (o *Document) HasAccessStatusUpdatedAt() bool`

HasAccessStatusUpdatedAt returns a boolean if a field has been set.

### SetAccessStatusUpdatedAtNil

`func (o *Document) SetAccessStatusUpdatedAtNil(b bool)`

 SetAccessStatusUpdatedAtNil sets the value for AccessStatusUpdatedAt to be an explicit nil

### UnsetAccessStatusUpdatedAt
`func (o *Document) UnsetAccessStatusUpdatedAt()`

UnsetAccessStatusUpdatedAt ensures that no value is present for AccessStatusUpdatedAt, not even an explicit nil
### GetAlias

`func (o *Document) GetAlias() int32`

GetAlias returns the Alias field if non-nil, zero value otherwise.

### GetAliasOk

`func (o *Document) GetAliasOk() (*int32, bool)`

GetAliasOk returns a tuple with the Alias field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAlias

`func (o *Document) SetAlias(v int32)`

SetAlias sets Alias field to given value.

### HasAlias

`func (o *Document) HasAlias() bool`

HasAlias returns a boolean if a field has been set.

### GetVersion

`func (o *Document) GetVersion() int32`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *Document) GetVersionOk() (*int32, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *Document) SetVersion(v int32)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *Document) HasVersion() bool`

HasVersion returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


