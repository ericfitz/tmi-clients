# ThreatBase

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
**Ssvc** | Pointer to [**NullableSSVCScore**](SSVCScore.md) | SSVC (Stakeholder-Specific Vulnerability Categorization) assessment result. Optional structured decision from CISA/CERT-CC SSVC framework. | [optional] 

## Methods

### NewThreatBase

`func NewThreatBase(name string, threatType []string, ) *ThreatBase`

NewThreatBase instantiates a new ThreatBase object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatBaseWithDefaults

`func NewThreatBaseWithDefaults() *ThreatBase`

NewThreatBaseWithDefaults instantiates a new ThreatBase object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ThreatBase) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ThreatBase) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ThreatBase) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ThreatBase) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ThreatBase) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ThreatBase) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ThreatBase) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ThreatBase) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ThreatBase) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetMitigation

`func (o *ThreatBase) GetMitigation() string`

GetMitigation returns the Mitigation field if non-nil, zero value otherwise.

### GetMitigationOk

`func (o *ThreatBase) GetMitigationOk() (*string, bool)`

GetMitigationOk returns a tuple with the Mitigation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigation

`func (o *ThreatBase) SetMitigation(v string)`

SetMitigation sets Mitigation field to given value.

### HasMitigation

`func (o *ThreatBase) HasMitigation() bool`

HasMitigation returns a boolean if a field has been set.

### SetMitigationNil

`func (o *ThreatBase) SetMitigationNil(b bool)`

 SetMitigationNil sets the value for Mitigation to be an explicit nil

### UnsetMitigation
`func (o *ThreatBase) UnsetMitigation()`

UnsetMitigation ensures that no value is present for Mitigation, not even an explicit nil
### GetDiagramId

`func (o *ThreatBase) GetDiagramId() string`

GetDiagramId returns the DiagramId field if non-nil, zero value otherwise.

### GetDiagramIdOk

`func (o *ThreatBase) GetDiagramIdOk() (*string, bool)`

GetDiagramIdOk returns a tuple with the DiagramId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramId

`func (o *ThreatBase) SetDiagramId(v string)`

SetDiagramId sets DiagramId field to given value.

### HasDiagramId

`func (o *ThreatBase) HasDiagramId() bool`

HasDiagramId returns a boolean if a field has been set.

### SetDiagramIdNil

`func (o *ThreatBase) SetDiagramIdNil(b bool)`

 SetDiagramIdNil sets the value for DiagramId to be an explicit nil

### UnsetDiagramId
`func (o *ThreatBase) UnsetDiagramId()`

UnsetDiagramId ensures that no value is present for DiagramId, not even an explicit nil
### GetCellId

`func (o *ThreatBase) GetCellId() string`

GetCellId returns the CellId field if non-nil, zero value otherwise.

### GetCellIdOk

`func (o *ThreatBase) GetCellIdOk() (*string, bool)`

GetCellIdOk returns a tuple with the CellId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCellId

`func (o *ThreatBase) SetCellId(v string)`

SetCellId sets CellId field to given value.

### HasCellId

`func (o *ThreatBase) HasCellId() bool`

HasCellId returns a boolean if a field has been set.

### SetCellIdNil

`func (o *ThreatBase) SetCellIdNil(b bool)`

 SetCellIdNil sets the value for CellId to be an explicit nil

### UnsetCellId
`func (o *ThreatBase) UnsetCellId()`

UnsetCellId ensures that no value is present for CellId, not even an explicit nil
### GetSeverity

`func (o *ThreatBase) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *ThreatBase) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *ThreatBase) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *ThreatBase) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### SetSeverityNil

`func (o *ThreatBase) SetSeverityNil(b bool)`

 SetSeverityNil sets the value for Severity to be an explicit nil

### UnsetSeverity
`func (o *ThreatBase) UnsetSeverity()`

UnsetSeverity ensures that no value is present for Severity, not even an explicit nil
### GetScore

`func (o *ThreatBase) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *ThreatBase) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *ThreatBase) SetScore(v float32)`

SetScore sets Score field to given value.

### HasScore

`func (o *ThreatBase) HasScore() bool`

HasScore returns a boolean if a field has been set.

### GetPriority

`func (o *ThreatBase) GetPriority() string`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *ThreatBase) GetPriorityOk() (*string, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *ThreatBase) SetPriority(v string)`

SetPriority sets Priority field to given value.

### HasPriority

`func (o *ThreatBase) HasPriority() bool`

HasPriority returns a boolean if a field has been set.

### SetPriorityNil

`func (o *ThreatBase) SetPriorityNil(b bool)`

 SetPriorityNil sets the value for Priority to be an explicit nil

### UnsetPriority
`func (o *ThreatBase) UnsetPriority()`

UnsetPriority ensures that no value is present for Priority, not even an explicit nil
### GetMitigated

`func (o *ThreatBase) GetMitigated() bool`

GetMitigated returns the Mitigated field if non-nil, zero value otherwise.

### GetMitigatedOk

`func (o *ThreatBase) GetMitigatedOk() (*bool, bool)`

GetMitigatedOk returns a tuple with the Mitigated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigated

`func (o *ThreatBase) SetMitigated(v bool)`

SetMitigated sets Mitigated field to given value.

### HasMitigated

`func (o *ThreatBase) HasMitigated() bool`

HasMitigated returns a boolean if a field has been set.

### GetStatus

`func (o *ThreatBase) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ThreatBase) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ThreatBase) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ThreatBase) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ThreatBase) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ThreatBase) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetThreatType

`func (o *ThreatBase) GetThreatType() []string`

GetThreatType returns the ThreatType field if non-nil, zero value otherwise.

### GetThreatTypeOk

`func (o *ThreatBase) GetThreatTypeOk() (*[]string, bool)`

GetThreatTypeOk returns a tuple with the ThreatType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatType

`func (o *ThreatBase) SetThreatType(v []string)`

SetThreatType sets ThreatType field to given value.


### GetMetadata

`func (o *ThreatBase) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ThreatBase) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ThreatBase) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ThreatBase) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ThreatBase) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ThreatBase) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *ThreatBase) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *ThreatBase) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *ThreatBase) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *ThreatBase) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### SetIssueUriNil

`func (o *ThreatBase) SetIssueUriNil(b bool)`

 SetIssueUriNil sets the value for IssueUri to be an explicit nil

### UnsetIssueUri
`func (o *ThreatBase) UnsetIssueUri()`

UnsetIssueUri ensures that no value is present for IssueUri, not even an explicit nil
### GetAssetId

`func (o *ThreatBase) GetAssetId() string`

GetAssetId returns the AssetId field if non-nil, zero value otherwise.

### GetAssetIdOk

`func (o *ThreatBase) GetAssetIdOk() (*string, bool)`

GetAssetIdOk returns a tuple with the AssetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetId

`func (o *ThreatBase) SetAssetId(v string)`

SetAssetId sets AssetId field to given value.

### HasAssetId

`func (o *ThreatBase) HasAssetId() bool`

HasAssetId returns a boolean if a field has been set.

### SetAssetIdNil

`func (o *ThreatBase) SetAssetIdNil(b bool)`

 SetAssetIdNil sets the value for AssetId to be an explicit nil

### UnsetAssetId
`func (o *ThreatBase) UnsetAssetId()`

UnsetAssetId ensures that no value is present for AssetId, not even an explicit nil
### GetCweId

`func (o *ThreatBase) GetCweId() []string`

GetCweId returns the CweId field if non-nil, zero value otherwise.

### GetCweIdOk

`func (o *ThreatBase) GetCweIdOk() (*[]string, bool)`

GetCweIdOk returns a tuple with the CweId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCweId

`func (o *ThreatBase) SetCweId(v []string)`

SetCweId sets CweId field to given value.

### HasCweId

`func (o *ThreatBase) HasCweId() bool`

HasCweId returns a boolean if a field has been set.

### GetCvss

`func (o *ThreatBase) GetCvss() []CVSSScore`

GetCvss returns the Cvss field if non-nil, zero value otherwise.

### GetCvssOk

`func (o *ThreatBase) GetCvssOk() (*[]CVSSScore, bool)`

GetCvssOk returns a tuple with the Cvss field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCvss

`func (o *ThreatBase) SetCvss(v []CVSSScore)`

SetCvss sets Cvss field to given value.

### HasCvss

`func (o *ThreatBase) HasCvss() bool`

HasCvss returns a boolean if a field has been set.

### GetIncludeInReport

`func (o *ThreatBase) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *ThreatBase) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *ThreatBase) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *ThreatBase) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *ThreatBase) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *ThreatBase) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *ThreatBase) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *ThreatBase) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSsvc

`func (o *ThreatBase) GetSsvc() SSVCScore`

GetSsvc returns the Ssvc field if non-nil, zero value otherwise.

### GetSsvcOk

`func (o *ThreatBase) GetSsvcOk() (*SSVCScore, bool)`

GetSsvcOk returns a tuple with the Ssvc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsvc

`func (o *ThreatBase) SetSsvc(v SSVCScore)`

SetSsvc sets Ssvc field to given value.

### HasSsvc

`func (o *ThreatBase) HasSsvc() bool`

HasSsvc returns a boolean if a field has been set.

### SetSsvcNil

`func (o *ThreatBase) SetSsvcNil(b bool)`

 SetSsvcNil sets the value for Ssvc to be an explicit nil

### UnsetSsvc
`func (o *ThreatBase) UnsetSsvc()`

UnsetSsvc ensures that no value is present for Ssvc, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


