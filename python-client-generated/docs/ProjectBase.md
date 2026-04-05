# ProjectBase

Client-writable fields for a project

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

## Example

```python
from tmi_client.models.project_base import ProjectBase

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBase from a JSON string
project_base_instance = ProjectBase.from_json(json)
# print the JSON string representation of the object
print(ProjectBase.to_json())

# convert the object into a dict
project_base_dict = project_base_instance.to_dict()
# create an instance of ProjectBase from a dict
project_base_from_dict = ProjectBase.from_dict(project_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


