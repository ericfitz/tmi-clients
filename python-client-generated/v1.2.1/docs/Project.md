# Project

A project representing a product, service, or application

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project name | 
**description** | **str** | Project description | [optional] 
**team_id** | **UUID** | UUID of the team this project belongs to | 
**responsible_parties** | [**List[ResponsibleParty]**](ResponsibleParty.md) | Responsible parties for this project | [optional] 
**related_projects** | [**List[RelatedProject]**](RelatedProject.md) | Relationships to other projects | [optional] 
**uri** | **str** | URL or reference to internal project page | [optional] 
**status** | **str** | Project status (lifecycle, archival, deprecation, etc.) | [optional] 
**id** | **UUID** | Unique identifier for the project (UUID) | [optional] [readonly] 
**team** | **object** | The team this project belongs to (resolved) | [optional] [readonly] 
**created_by** | **object** | User who created the project | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_by** | **object** | User who last modified the project | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**reviewed_by** | **object** | User who last reviewed the project | [optional] 
**reviewed_at** | **datetime** | Last review timestamp (RFC3339) | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 

## Example

```python
from tmi_client.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


