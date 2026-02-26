# Threat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the threat (UUID) | [optional] [default to null]
**ThreatModelId** | **string** | Unique identifier of the parent threat model (UUID) | [optional] [default to null]
**CreatedAt** | [**time.Time**](time.Time.md) | Creation timestamp (RFC3339) | [optional] [default to null]
**ModifiedAt** | [**time.Time**](time.Time.md) | Last modification timestamp (RFC3339) | [optional] [default to null]
**Name** | **string** | Name of the threat | [default to null]
**Description** | **string** | Description of the threat and risk to the organization | [optional] [default to null]
**Mitigation** | **string** | Recommended or planned mitigation(s) for the threat | [optional] [default to null]
**DiagramId** | **string** | Unique identifier of the associated diagram (if applicable) (UUID) | [optional] [default to null]
**CellId** | **string** | Unique identifier of the associated cell (if applicable) (UUID) | [optional] [default to null]
**Severity** | **string** | Severity level of the threat | [optional] [default to null]
**Score** | **float64** | Numeric score representing the risk or impact of the threat | [optional] [default to null]
**Priority** | **string** | Priority level for addressing the threat | [optional] [default to null]
**Mitigated** | **bool** | Whether the threat has been mitigated | [optional] [default to null]
**Status** | **string** | Current status of the threat | [optional] [default to null]
**ThreatType** | **[]string** | Types or categories of the threat. Supports multiple classifications within the same framework (e.g., [&#x27;Spoofing&#x27;, &#x27;Tampering&#x27;]). Empty array indicates no types assigned. | [default to []]
**Metadata** | [**[]Metadata**](Metadata.md) | Key-value pairs for additional threat metadata | [optional] [default to null]
**IssueUri** | **string** | URL to an issue in an issue tracking system for this threat | [optional] [default to null]
**AssetId** | **string** | Unique identifier of the associated asset (if applicable) (UUID) | [optional] [default to null]
**CweId** | **[]string** | CWE (Common Weakness Enumeration) identifiers associated with this threat | [optional] [default to null]
**Cvss** | [**[]CvssScore**](CVSSScore.md) | CVSS scoring information for this threat | [optional] [default to null]
**IncludeInReport** | **bool** | Whether this item should be included in generated reports | [optional] [default to true]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

