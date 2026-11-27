# ThreatBase

Base schema for Threat with client-writable fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the threat | 
**description** | **str** | Description of the threat and risk to the organization | [optional] 
**mitigation** | **str** | Recommended or planned mitigation(s) for the threat | [optional] 
**diagram_id** | **UUID** | Unique identifier of the associated diagram (if applicable) (UUID) | [optional] 
**cell_id** | **UUID** | Unique identifier of the associated cell (if applicable) (UUID) | [optional] 
**severity** | **str** | Severity level of the threat | [optional] 
**score** | **float** | Numeric score representing the risk or impact of the threat | [optional] 
**priority** | **str** | Priority level for addressing the threat | [optional] 
**mitigated** | **bool** | Whether the threat has been mitigated | [optional] 
**status** | **str** | Current status of the threat | [optional] 
**threat_type** | **List[str]** | Types or categories of the threat. Supports multiple classifications within the same framework (e.g., [&#39;Spoofing&#39;, &#39;Tampering&#39;]). Empty array indicates no types assigned. | [default to []]
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional threat metadata | [optional] 
**issue_uri** | **str** | URL to an issue in an issue tracking system for this threat | [optional] 
**asset_id** | **UUID** | Unique identifier of the associated asset (if applicable) (UUID) | [optional] 
**cwe_id** | **List[str]** | CWE (Common Weakness Enumeration) identifiers associated with this threat | [optional] 
**cvss** | [**List[CVSSScore]**](CVSSScore.md) | CVSS scoring information for this threat | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**ssvc** | [**SSVCScore**](SSVCScore.md) | SSVC (Stakeholder-Specific Vulnerability Categorization) assessment result. Optional structured decision from CISA/CERT-CC SSVC framework. | [optional] 

## Example

```python
from tmi_client.models.threat_base import ThreatBase

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatBase from a JSON string
threat_base_instance = ThreatBase.from_json(json)
# print the JSON string representation of the object
print(ThreatBase.to_json())

# convert the object into a dict
threat_base_dict = threat_base_instance.to_dict()
# create an instance of ThreatBase from a dict
threat_base_from_dict = ThreatBase.from_dict(threat_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


