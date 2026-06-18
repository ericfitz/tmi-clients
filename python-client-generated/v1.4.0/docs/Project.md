# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Project name | 
**description** | **str** | Project description | [optional] 
**team_id** | **UUID** | UUID of the team this project belongs to | 
**responsible_parties** | [**List[ResponsibleParty]**](ResponsibleParty.md) | Responsible parties for this project | [optional] 
**related_projects** | [**List[RelatedProject]**](RelatedProject.md) | Relationships to other projects | [optional] 
**uri** | **str** | URL or reference to internal project page | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) | Project lifecycle status. Defaults to &#39;active&#39; if not provided or set to null. | [optional] 
**id** | **UUID** | Unique identifier for the project (UUID) | [optional] [readonly] 
**team** | **object** | Per-viewer access diagnostics; present when access_status is not &#39;accessible&#39; | [optional] [readonly] 
**created_by** | **object** | Per-viewer access diagnostics; present when access_status is not &#39;accessible&#39; | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_by** | **object** | Per-viewer access diagnostics; present when access_status is not &#39;accessible&#39; | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 
**reviewed_by** | **object** | Optional; when present, client has performed a Picker-based attachment | [optional] 
**reviewed_at** | **datetime** | Last review timestamp (RFC3339) | [optional] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] 
**notes** | [**List[ProjectNoteListItem]**](ProjectNoteListItem.md) | List of notes associated with the project | [optional] [readonly] 
**version** | **int** | Server-managed monotonically-increasing optimistic-locking version. Returned on reads and bumped by every successful PUT/PATCH. Clients echo this back via the If-Match request header (preferred) or the body &#39;version&#39; field on the next mutation. A mismatch returns 409 Conflict. See issue #385. | [optional] [readonly] 

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


