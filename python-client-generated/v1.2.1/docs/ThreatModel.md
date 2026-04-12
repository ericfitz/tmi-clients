# ThreatModel

A threat model containing diagrams, threats, documents, and other security analysis artifacts

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
**id** | **UUID** | Unique identifier for the threat model (UUID) | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**created_by** | [**User**](User.md) | User who created the threat model | [optional] [readonly] 
**documents** | [**List[Document]**](Document.md) | List of documents related to the threat model | [optional] [readonly] 
**repositories** | [**List[Repository]**](Repository.md) | List of source code repositories related to the threat model | [optional] [readonly] 
**diagrams** | [**List[DfdDiagram]**](DfdDiagram.md) | List of diagram objects associated with this threat model | [optional] [readonly] 
**threats** | [**List[Threat]**](Threat.md) | List of threats within the threat model | [optional] [readonly] 
**notes** | [**List[Note]**](Note.md) | List of notes associated with the threat model | [optional] [readonly] 
**assets** | [**List[ExtendedAsset]**](ExtendedAsset.md) | List of assets associated with the threat model | [optional] [readonly] 
**status_updated** | **datetime** | Timestamp when the status field was last modified (RFC3339). Automatically updated by the server when status changes. | [optional] [readonly] 
**is_confidential** | **bool** | Whether this threat model is confidential (set at creation, read-only after) | [optional] [readonly] 

## Example

```python
from tmi_client.models.threat_model import ThreatModel

# TODO update the JSON string below
json = "{}"
# create an instance of ThreatModel from a JSON string
threat_model_instance = ThreatModel.from_json(json)
# print the JSON string representation of the object
print(ThreatModel.to_json())

# convert the object into a dict
threat_model_dict = threat_model_instance.to_dict()
# create an instance of ThreatModel from a dict
threat_model_from_dict = ThreatModel.from_dict(threat_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


