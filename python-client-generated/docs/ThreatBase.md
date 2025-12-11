# ThreatBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the threat | 
**description** | **str** | Description of the threat and risk to the organization | [optional] 
**mitigation** | **str** | Recommended or planned mitigation(s) for the threat | [optional] 
**diagram_id** | **str** | Unique identifier of the associated diagram (if applicable) (UUID) | [optional] 
**cell_id** | **str** | Unique identifier of the associated cell (if applicable) (UUID) | [optional] 
**severity** | **str** | Severity level of the threat | [optional] 
**score** | **float** | Numeric score representing the risk or impact of the threat | [optional] 
**priority** | **str** | Priority level for addressing the threat | [optional] 
**mitigated** | **bool** | Whether the threat has been mitigated | [optional] 
**status** | **str** | Current status of the threat | [optional] 
**threat_type** | **list[str]** | Types or categories of the threat. Supports multiple classifications within the same framework (e.g., [&#x27;Spoofing&#x27;, &#x27;Tampering&#x27;]). Empty array indicates no types assigned. | 
**metadata** | [**list[Metadata]**](Metadata.md) | Key-value pairs for additional threat metadata | [optional] 
**issue_uri** | **str** | URL to an issue in an issue tracking system for this threat | [optional] 
**asset_id** | **str** | Unique identifier of the associated asset (if applicable) (UUID) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

