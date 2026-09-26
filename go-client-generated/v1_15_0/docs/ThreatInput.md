# ThreatInput

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

### NewThreatInput

`func NewThreatInput(name string, threatType []string, ) *ThreatInput`

NewThreatInput instantiates a new ThreatInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewThreatInputWithDefaults

`func NewThreatInputWithDefaults() *ThreatInput`

NewThreatInputWithDefaults instantiates a new ThreatInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ThreatInput) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ThreatInput) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ThreatInput) SetName(v string)`

SetName sets Name field to given value.


### GetDescription

`func (o *ThreatInput) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *ThreatInput) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *ThreatInput) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *ThreatInput) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### SetDescriptionNil

`func (o *ThreatInput) SetDescriptionNil(b bool)`

 SetDescriptionNil sets the value for Description to be an explicit nil

### UnsetDescription
`func (o *ThreatInput) UnsetDescription()`

UnsetDescription ensures that no value is present for Description, not even an explicit nil
### GetMitigation

`func (o *ThreatInput) GetMitigation() string`

GetMitigation returns the Mitigation field if non-nil, zero value otherwise.

### GetMitigationOk

`func (o *ThreatInput) GetMitigationOk() (*string, bool)`

GetMitigationOk returns a tuple with the Mitigation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigation

`func (o *ThreatInput) SetMitigation(v string)`

SetMitigation sets Mitigation field to given value.

### HasMitigation

`func (o *ThreatInput) HasMitigation() bool`

HasMitigation returns a boolean if a field has been set.

### SetMitigationNil

`func (o *ThreatInput) SetMitigationNil(b bool)`

 SetMitigationNil sets the value for Mitigation to be an explicit nil

### UnsetMitigation
`func (o *ThreatInput) UnsetMitigation()`

UnsetMitigation ensures that no value is present for Mitigation, not even an explicit nil
### GetDiagramId

`func (o *ThreatInput) GetDiagramId() string`

GetDiagramId returns the DiagramId field if non-nil, zero value otherwise.

### GetDiagramIdOk

`func (o *ThreatInput) GetDiagramIdOk() (*string, bool)`

GetDiagramIdOk returns a tuple with the DiagramId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDiagramId

`func (o *ThreatInput) SetDiagramId(v string)`

SetDiagramId sets DiagramId field to given value.

### HasDiagramId

`func (o *ThreatInput) HasDiagramId() bool`

HasDiagramId returns a boolean if a field has been set.

### SetDiagramIdNil

`func (o *ThreatInput) SetDiagramIdNil(b bool)`

 SetDiagramIdNil sets the value for DiagramId to be an explicit nil

### UnsetDiagramId
`func (o *ThreatInput) UnsetDiagramId()`

UnsetDiagramId ensures that no value is present for DiagramId, not even an explicit nil
### GetCellId

`func (o *ThreatInput) GetCellId() string`

GetCellId returns the CellId field if non-nil, zero value otherwise.

### GetCellIdOk

`func (o *ThreatInput) GetCellIdOk() (*string, bool)`

GetCellIdOk returns a tuple with the CellId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCellId

`func (o *ThreatInput) SetCellId(v string)`

SetCellId sets CellId field to given value.

### HasCellId

`func (o *ThreatInput) HasCellId() bool`

HasCellId returns a boolean if a field has been set.

### SetCellIdNil

`func (o *ThreatInput) SetCellIdNil(b bool)`

 SetCellIdNil sets the value for CellId to be an explicit nil

### UnsetCellId
`func (o *ThreatInput) UnsetCellId()`

UnsetCellId ensures that no value is present for CellId, not even an explicit nil
### GetSeverity

`func (o *ThreatInput) GetSeverity() string`

GetSeverity returns the Severity field if non-nil, zero value otherwise.

### GetSeverityOk

`func (o *ThreatInput) GetSeverityOk() (*string, bool)`

GetSeverityOk returns a tuple with the Severity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSeverity

`func (o *ThreatInput) SetSeverity(v string)`

SetSeverity sets Severity field to given value.

### HasSeverity

`func (o *ThreatInput) HasSeverity() bool`

HasSeverity returns a boolean if a field has been set.

### SetSeverityNil

`func (o *ThreatInput) SetSeverityNil(b bool)`

 SetSeverityNil sets the value for Severity to be an explicit nil

### UnsetSeverity
`func (o *ThreatInput) UnsetSeverity()`

UnsetSeverity ensures that no value is present for Severity, not even an explicit nil
### GetScore

`func (o *ThreatInput) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *ThreatInput) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *ThreatInput) SetScore(v float32)`

SetScore sets Score field to given value.

### HasScore

`func (o *ThreatInput) HasScore() bool`

HasScore returns a boolean if a field has been set.

### GetPriority

`func (o *ThreatInput) GetPriority() string`

GetPriority returns the Priority field if non-nil, zero value otherwise.

### GetPriorityOk

`func (o *ThreatInput) GetPriorityOk() (*string, bool)`

GetPriorityOk returns a tuple with the Priority field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPriority

`func (o *ThreatInput) SetPriority(v string)`

SetPriority sets Priority field to given value.

### HasPriority

`func (o *ThreatInput) HasPriority() bool`

HasPriority returns a boolean if a field has been set.

### SetPriorityNil

`func (o *ThreatInput) SetPriorityNil(b bool)`

 SetPriorityNil sets the value for Priority to be an explicit nil

### UnsetPriority
`func (o *ThreatInput) UnsetPriority()`

UnsetPriority ensures that no value is present for Priority, not even an explicit nil
### GetMitigated

`func (o *ThreatInput) GetMitigated() bool`

GetMitigated returns the Mitigated field if non-nil, zero value otherwise.

### GetMitigatedOk

`func (o *ThreatInput) GetMitigatedOk() (*bool, bool)`

GetMitigatedOk returns a tuple with the Mitigated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMitigated

`func (o *ThreatInput) SetMitigated(v bool)`

SetMitigated sets Mitigated field to given value.

### HasMitigated

`func (o *ThreatInput) HasMitigated() bool`

HasMitigated returns a boolean if a field has been set.

### GetStatus

`func (o *ThreatInput) GetStatus() string`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ThreatInput) GetStatusOk() (*string, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ThreatInput) SetStatus(v string)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ThreatInput) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### SetStatusNil

`func (o *ThreatInput) SetStatusNil(b bool)`

 SetStatusNil sets the value for Status to be an explicit nil

### UnsetStatus
`func (o *ThreatInput) UnsetStatus()`

UnsetStatus ensures that no value is present for Status, not even an explicit nil
### GetThreatType

`func (o *ThreatInput) GetThreatType() []string`

GetThreatType returns the ThreatType field if non-nil, zero value otherwise.

### GetThreatTypeOk

`func (o *ThreatInput) GetThreatTypeOk() (*[]string, bool)`

GetThreatTypeOk returns a tuple with the ThreatType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatType

`func (o *ThreatInput) SetThreatType(v []string)`

SetThreatType sets ThreatType field to given value.


### GetMetadata

`func (o *ThreatInput) GetMetadata() []Metadata`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ThreatInput) GetMetadataOk() (*[]Metadata, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ThreatInput) SetMetadata(v []Metadata)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ThreatInput) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### SetMetadataNil

`func (o *ThreatInput) SetMetadataNil(b bool)`

 SetMetadataNil sets the value for Metadata to be an explicit nil

### UnsetMetadata
`func (o *ThreatInput) UnsetMetadata()`

UnsetMetadata ensures that no value is present for Metadata, not even an explicit nil
### GetIssueUri

`func (o *ThreatInput) GetIssueUri() string`

GetIssueUri returns the IssueUri field if non-nil, zero value otherwise.

### GetIssueUriOk

`func (o *ThreatInput) GetIssueUriOk() (*string, bool)`

GetIssueUriOk returns a tuple with the IssueUri field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIssueUri

`func (o *ThreatInput) SetIssueUri(v string)`

SetIssueUri sets IssueUri field to given value.

### HasIssueUri

`func (o *ThreatInput) HasIssueUri() bool`

HasIssueUri returns a boolean if a field has been set.

### SetIssueUriNil

`func (o *ThreatInput) SetIssueUriNil(b bool)`

 SetIssueUriNil sets the value for IssueUri to be an explicit nil

### UnsetIssueUri
`func (o *ThreatInput) UnsetIssueUri()`

UnsetIssueUri ensures that no value is present for IssueUri, not even an explicit nil
### GetAssetId

`func (o *ThreatInput) GetAssetId() string`

GetAssetId returns the AssetId field if non-nil, zero value otherwise.

### GetAssetIdOk

`func (o *ThreatInput) GetAssetIdOk() (*string, bool)`

GetAssetIdOk returns a tuple with the AssetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAssetId

`func (o *ThreatInput) SetAssetId(v string)`

SetAssetId sets AssetId field to given value.

### HasAssetId

`func (o *ThreatInput) HasAssetId() bool`

HasAssetId returns a boolean if a field has been set.

### SetAssetIdNil

`func (o *ThreatInput) SetAssetIdNil(b bool)`

 SetAssetIdNil sets the value for AssetId to be an explicit nil

### UnsetAssetId
`func (o *ThreatInput) UnsetAssetId()`

UnsetAssetId ensures that no value is present for AssetId, not even an explicit nil
### GetCweId

`func (o *ThreatInput) GetCweId() []string`

GetCweId returns the CweId field if non-nil, zero value otherwise.

### GetCweIdOk

`func (o *ThreatInput) GetCweIdOk() (*[]string, bool)`

GetCweIdOk returns a tuple with the CweId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCweId

`func (o *ThreatInput) SetCweId(v []string)`

SetCweId sets CweId field to given value.

### HasCweId

`func (o *ThreatInput) HasCweId() bool`

HasCweId returns a boolean if a field has been set.

### GetCvss

`func (o *ThreatInput) GetCvss() []CVSSScore`

GetCvss returns the Cvss field if non-nil, zero value otherwise.

### GetCvssOk

`func (o *ThreatInput) GetCvssOk() (*[]CVSSScore, bool)`

GetCvssOk returns a tuple with the Cvss field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCvss

`func (o *ThreatInput) SetCvss(v []CVSSScore)`

SetCvss sets Cvss field to given value.

### HasCvss

`func (o *ThreatInput) HasCvss() bool`

HasCvss returns a boolean if a field has been set.

### GetIncludeInReport

`func (o *ThreatInput) GetIncludeInReport() bool`

GetIncludeInReport returns the IncludeInReport field if non-nil, zero value otherwise.

### GetIncludeInReportOk

`func (o *ThreatInput) GetIncludeInReportOk() (*bool, bool)`

GetIncludeInReportOk returns a tuple with the IncludeInReport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIncludeInReport

`func (o *ThreatInput) SetIncludeInReport(v bool)`

SetIncludeInReport sets IncludeInReport field to given value.

### HasIncludeInReport

`func (o *ThreatInput) HasIncludeInReport() bool`

HasIncludeInReport returns a boolean if a field has been set.

### GetTimmyEnabled

`func (o *ThreatInput) GetTimmyEnabled() bool`

GetTimmyEnabled returns the TimmyEnabled field if non-nil, zero value otherwise.

### GetTimmyEnabledOk

`func (o *ThreatInput) GetTimmyEnabledOk() (*bool, bool)`

GetTimmyEnabledOk returns a tuple with the TimmyEnabled field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTimmyEnabled

`func (o *ThreatInput) SetTimmyEnabled(v bool)`

SetTimmyEnabled sets TimmyEnabled field to given value.

### HasTimmyEnabled

`func (o *ThreatInput) HasTimmyEnabled() bool`

HasTimmyEnabled returns a boolean if a field has been set.

### GetSsvc

`func (o *ThreatInput) GetSsvc() SSVCScore`

GetSsvc returns the Ssvc field if non-nil, zero value otherwise.

### GetSsvcOk

`func (o *ThreatInput) GetSsvcOk() (*SSVCScore, bool)`

GetSsvcOk returns a tuple with the Ssvc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSsvc

`func (o *ThreatInput) SetSsvc(v SSVCScore)`

SetSsvc sets Ssvc field to given value.

### HasSsvc

`func (o *ThreatInput) HasSsvc() bool`

HasSsvc returns a boolean if a field has been set.

### SetSsvcNil

`func (o *ThreatInput) SetSsvcNil(b bool)`

 SetSsvcNil sets the value for Ssvc to be an explicit nil

### UnsetSsvc
`func (o *ThreatInput) UnsetSsvc()`

UnsetSsvc ensures that no value is present for Ssvc, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


