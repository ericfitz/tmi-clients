# Threat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Name of the threat | 
**Description** | Pointer to **NullableString** | Description of the threat and risk to the organization | [optional] 
**Mitigation** | Pointer to **NullableString** | Recommended or planned mitigation(s) for the threat | [optional] 
**DiagramId** | Pointer to **NullableString** | Unique identifier of the associated diagram (if applicable) (UUID) | [optional] 
**CellId** | Pointer to **NullableString** | Unique identifier of the associated cell (if applicable) (UUID) | [optional] 
**Severity** | Pointer to **NullableString** | Severity level of the threat | [optional] 
**Score** | Pointer to **float32** | Numeric score representing the risk or impact of the threat | [optional] 
**Priority** | Pointer to **NullableString** | Priority level for addressing the threat | [optional] 
**Mitigated** | Pointer to **bool** | Whether the threat has been mitigated | [optional] 
**Status** | Pointer to **NullableString** | Current status of the threat | [optional] 
**ThreatType** | **[]string** | Types or categories of the threat. Supports multiple classifications within the same framework (e.g., [&#39;Spoofing&#39;, &#39;Tampering&#39;]). Empty array indicates no types assigned. | [default to {}]
**Metadata** | Pointer to [**[]Metadata**](Metadata.md) | Key-value pairs for additional threat metadata | [optional] 
**IssueUri** | Pointer to **NullableString** | URL to an issue in an issue tracking system for this threat | [optional] 
**AssetId** | Pointer to **NullableString** | Unique identifier of the associated asset (if applicable) (UUID) | [optional] 
**CweId** | Pointer to **[]string** | CWE (Common Weakness Enumeration) identifiers associated with this threat | [optional] 
**Cvss** | Pointer to [**[]CVSSScore**](CVSSScore.md) | CVSS scoring information for this threat | [optional] 
**IncludeInReport** | Pointer to **bool** | Whether this item should be included in generated reports | [optional] [default to true]
**TimmyEnabled** | Pointer to **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to true]
**Id** | Pointer to **string** | Unique identifier for the threat (UUID) | [optional] [readonly] 
**ThreatModelId** | Pointer to **string** | Unique identifier of the parent threat model (UUID) | [optional] [readonly] 
**CreatedAt** | Pointer to **time.Time** | Creation timestamp (RFC3339) | [optional] [readonly] 
**ModifiedAt** | Pointer to **time.Time** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**DeletedAt** | Pointer to **NullableTime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 

## Methods

### NewThreat

`func NewThreat(name string, threatType []string, ) *Threat`

NewThreat instantiates a new Threat object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatWithDefaults

`func NewThreatWithDefaults() *Threat`

NewThreatWithDefaults instantiates a new Threat object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *Threat) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *Threat) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *Threat) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *Threat) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *Threat) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *Threat) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *Threat) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *Threat) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *Threat) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetMitigation

`func (o *Threat) GetMitigation() string`

GetMitigation returns the Mitigation field if non-nil, zero value otherwise.

### GetMitigationOk

`func (o *Threat) GetMitigationOk() (*string, bool)`

GetMitigationOk returns a tuple with the Mitigation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigation

`func (o *Threat) SetMitigation(v string)`

SetMitigation sets Mitigation field to given value.

### HasMitigation

`func (o *Threat) HasMitigation() bool`

HasMitigation returns a boolean if a field has been set.

### SetMitigationNil

`func (o *Threat) SetMitigationNil(b bool)`

 SetMitigationNil sets the value for Mitigation to be an explicit nil

### UnsetMitigation
`func (o *Threat) UnsetMitigation()`

UnsetMitigation ensures that no value is present for Mitigation, not even an explicit nil
### GetDiagramId

`func (o *Threat) GetDiagramId() string`

GetDiagramId returns the DiagramId field if non-nil, zero value otherwise.

### GetDiagramIdOk

`func (o *Threat) GetDiagramIdOk() (*string, bool)`

GetDiagramIdOk returns a tuple with the DiagramId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramId

`func (o *Threat) SetDiagramId(v string)`

SetDiagramId sets DiagramId field to given value.

### HasDiagramId

`func (o *Threat) HasDiagramId() bool`

HasDiagramId returns a boolean if a field has been set.

### SetDiagramIdNil

`func (o *Threat) SetDiagramIdNil(b bool)`

 SetDiagramIdNil sets the value for DiagramId to be an explicit nil

### UnsetDiagramId
`func (o *Threat) UnsetDiagramId()`

UnsetDiagramId ensures that no value is present for DiagramId, not even an explicit nil
### GetCellId

`func (o *Threat) GetCellId() string`

GetCellId returns the CellId field if non-nil, zero value otherwise.

### GetCellIdOk

`func (o *Threat) GetCellIdOk() (*string, bool)`

GetCellIdOk returns a tuple with the CellId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCellId

`func (o *Threat) SetCellId(v string)`

SetCellId sets CellId field to given value.

### HasCellId

`func (o *Threat) HasCellId() bool`

HasCellId returns a boolean if a field has been set.

### SetCellIdNil

`func (o *Threat) SetCellIdNil(b bool)`

 SetCellIdNil sets the value for CellId to be an explicit nil

### UnsetCellId
`func (o *Threat) UnsetCellId()`

UnsetCellId ensures that no value is present for CellId, not even an explicit nil
### GetSeverity

`func (o *Threat) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *Threat) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *Threat) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *Threat) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### SetSeverityNil

`func (o *Threat) SetSeverityNil(b bool)`

 SetSeverityNil sets the value for Severity to be an explicit nil

### UnsetSeverity
`func (o *Threat) UnsetSeverity()`

UnsetSeverity ensures that no value is present for Severity, not even an explicit nil
### GetScore

`func (o *Threat) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *Threat) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *Threat) SetScore(v float32)`

SetScore sets Score field to given value.

### HasScore

`func (o *Threat) HasScore() bool`

HasScore returns a boolean if a field has been set.

### GetPriority

`func (o *Threat) GetPriority() string`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *Threat) GetPriorityOk() (*string, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *Threat) SetPriority(v string)`

SetPriority sets Priority field to given value.

### HasPriority

`func (o *Threat) HasPriority() bool`

HasPriority returns a boolean if a field has been set.

### SetPriorityNil

`func (o *Threat) SetPriorityNil(b bool)`

 SetPriorityNil sets the value for Priority to be an explicit nil

### UnsetPriority
`func (o *Threat) UnsetPriority()`

UnsetPriority ensures that no value is present for Priority, not even an explicit nil
### GetMitigated

`func (o *Threat) GetMitigated() bool`

GetMitigated returns the Mitigated field if non-nil, zero value otherwise.

### GetMitigatedOk

`func (o *Threat) GetMitigatedOk() (*bool, bool)`

GetMitigatedOk returns a tuple with the Mitigated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigated

`func (o *Threat) SetMitigated(v bool)`

SetMitigated sets Mitigated field to given value.

### HasMitigated

`func (o *Threat) HasMitigated() bool`

HasMitigated returns a boolean if a field has been set.

### GetStatus

`func (o *Threat) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *Threat) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *Threat) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *Threat) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *Threat) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *Threat) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetThreatType

`func (o *Threat) GetThreatType() []string`

GetThreatType returns the ThreatType field if non-nil, zero value otherwise.

### GetThreatTypeOk

`func (o *Threat) GetThreatTypeOk() (*[]string, bool)`

GetThreatTypeOk returns a tuple with the ThreatType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatType

`func (o *Threat) SetThreatType(v []string)`

SetThreatType sets ThreatType field to given value.


### GetMetadata

`func (o *Threat) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *Threat) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *Threat) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *Threat) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *Threat) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *Threat) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *Threat) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *Threat) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *Threat) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *Threat) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### SetIssueUriNil

`func (o *Threat) SetIssueUriNil(b bool)`

 SetIssueUriNil sets the value for IssueUri to be an explicit nil

### UnsetIssueUri
`func (o *Threat) UnsetIssueUri()`

UnsetIssueUri ensures that no value is present for IssueUri, not even an explicit nil
### GetAssetId

`func (o *Threat) GetAssetId() string`

GetAssetId returns the AssetId field if non-nil, zero value otherwise.

### GetAssetIdOk

`func (o *Threat) GetAssetIdOk() (*string, bool)`

GetAssetIdOk returns a tuple with the AssetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetId

`func (o *Threat) SetAssetId(v string)`

SetAssetId sets AssetId field to given value.

### HasAssetId

`func (o *Threat) HasAssetId() bool`

HasAssetId returns a boolean if a field has been set.

### SetAssetIdNil

`func (o *Threat) SetAssetIdNil(b bool)`

 SetAssetIdNil sets the value for AssetId to be an explicit nil

### UnsetAssetId
`func (o *Threat) UnsetAssetId()`

UnsetAssetId ensures that no value is present for AssetId, not even an explicit nil
### GetCweId

`func (o *Threat) GetCweId() []string`

GetCweId returns the CweId field if non-nil, zero value otherwise.

### GetCweIdOk

`func (o *Threat) GetCweIdOk() (*[]string, bool)`

GetCweIdOk returns a tuple with the CweId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCweId

`func (o *Threat) SetCweId(v []string)`

SetCweId sets CweId field to given value.

### HasCweId

`func (o *Threat) HasCweId() bool`

HasCweId returns a boolean if a field has been set.

### GetCvss

`func (o *Threat) GetCvss() []CVSSScore`

GetCvss returns the Cvss field if non-nil, zero value otherwise.

### GetCvssOk

`func (o *Threat) GetCvssOk() (*[]CVSSScore, bool)`

GetCvssOk returns a tuple with the Cvss field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCvss

`func (o *Threat) SetCvss(v []CVSSScore)`

SetCvss sets Cvss field to given value.

### HasCvss

`func (o *Threat) HasCvss() bool`

HasCvss returns a boolean if a field has been set.

### GetIncludeInReport

`func (o *Threat) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *Threat) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *Threat) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *Threat) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *Threat) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *Threat) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *Threat) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *Threat) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetId

`func (o *Threat) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *Threat) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *Threat) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *Threat) HasId() bool`

HasId returns a boolean if a field has been set.

### GetThreatModelId

`func (o *Threat) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *Threat) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *Threat) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *Threat) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.

### GetCreatedAt

`func (o *Threat) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *Threat) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *Threat) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.

### HasCreatedAt

`func (o *Threat) HasCreatedAt() bool`

HasCreatedAt returns a boolean if a field has been set.

### GetModifiedAt

`func (o *Threat) GetModifiedAt() time.Time`

GetModifiedAt returns the ModifiedAt field if non-nil, zero value otherwise.

### GetModifiedAtOk

`func (o *Threat) GetModifiedAtOk() (*time.Time, bool)`

GetModifiedAtOk returns a tuple with the ModifiedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetModifiedAt

`func (o *Threat) SetModifiedAt(v time.Time)`

SetModifiedAt sets ModifiedAt field to given value.

### HasModifiedAt

`func (o *Threat) HasModifiedAt() bool`

HasModifiedAt returns a boolean if a field has been set.

### GetDeletedAt

`func (o *Threat) GetDeletedAt() time.Time`

GetDeletedAt returns the DeletedAt field if non-nil, zero value otherwise.

### GetDeletedAtOk

`func (o *Threat) GetDeletedAtOk() (*time.Time, bool)`

GetDeletedAtOk returns a tuple with the DeletedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDeletedAt

`func (o *Threat) SetDeletedAt(v time.Time)`

SetDeletedAt sets DeletedAt field to given value.

### HasDeletedAt

`func (o *Threat) HasDeletedAt() bool`

HasDeletedAt returns a boolean if a field has been set.

### SetDeletedAtNil

`func (o *Threat) SetDeletedAtNil(b bool)`

 SetDeletedAtNil sets the value for DeletedAt to be an explicit nil

### UnsetDeletedAt
`func (o *Threat) UnsetDeletedAt()`

UnsetDeletedAt ensures that no value is present for DeletedAt, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


