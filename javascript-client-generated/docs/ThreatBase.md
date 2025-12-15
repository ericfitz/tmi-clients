# TmiThreatModelingImprovedApi.ThreatBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Name of the threat | 
**description** | **String** | Description of the threat and risk to the organization | [optional] 
**mitigation** | **String** | Recommended or planned mitigation(s) for the threat | [optional] 
**diagramId** | **String** | Unique identifier of the associated diagram (if applicable) (UUID) | [optional] 
**cellId** | **String** | Unique identifier of the associated cell (if applicable) (UUID) | [optional] 
**severity** | **String** | Severity level of the threat | [optional] 
**score** | **Number** | Numeric score representing the risk or impact of the threat | [optional] 
**priority** | **String** | Priority level for addressing the threat | [optional] 
**mitigated** | **Boolean** | Whether the threat has been mitigated | [optional] 
**status** | **String** | Current status of the threat | [optional] 
**threatType** | **[String]** | Types or categories of the threat. Supports multiple classifications within the same framework (e.g., [&#x27;Spoofing&#x27;, &#x27;Tampering&#x27;]). Empty array indicates no types assigned. | 
**metadata** | [**[Metadata]**](Metadata.md) | Key-value pairs for additional threat metadata | [optional] 
**issueUri** | **String** | URL to an issue in an issue tracking system for this threat | [optional] 
**assetId** | **String** | Unique identifier of the associated asset (if applicable) (UUID) | [optional] 
