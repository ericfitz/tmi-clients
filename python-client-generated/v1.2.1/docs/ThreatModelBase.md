# ThreatModelBase

Base schema for ThreatModel with client-writable fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the threat model | 
**description** | **str** | Description of the threat model | [optional] 
**owner** | [**User**](User.md) | User who owns the threat model (can be null for orphaned models) | 
**threat_model_framework** | **str** | The framework used for this threat model | 
**authorization** | [**List[Authorization]**](Authorization.md) | List of users and their roles for this threat model | 
**metadata** | [**List[Metadata]**](Metadata.md) | Key-value pairs for additional threat model metadata | [optional] 
**issue_uri** | **str** | URL to an issue in an issue tracking system for this threat model | [optional] 
**status** | **str** | Status of the threat model in the organization&#39;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**alias** | **List[str]** | Alternative names or identifiers for the threat model | [optional] 
**security_reviewer** | [**User**](User.md) | Security reviewer assigned to this threat model. When set, the security reviewer is automatically added to the authorization list with the owner role. The security reviewer&#39;s owner role cannot be removed via authorization changes while they remain assigned as security reviewer. To change the security reviewer&#39;s authorization, first unassign them as security reviewer. | [optional] 
**project_id** | **UUID** | Optional reference to the project this threat model belongs to | [optional] 

## Example

```python
from tmi_client.models.threat_model_base import ThreatModelBase

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatModelBase from a JSON string
threat_model_base_instance = ThreatModelBase.from_json(json)
# print the JSON string representation of the object
print(ThreatModelBase.to_json())

# convert the object into a dict
threat_model_base_dict = threat_model_base_instance.to_dict()
# create an instance of ThreatModelBase from a dict
threat_model_base_from_dict = ThreatModelBase.from_dict(threat_model_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


