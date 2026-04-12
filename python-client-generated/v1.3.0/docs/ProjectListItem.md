# ProjectListItem

Summary of a project for list views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) | Project lifecycle status. | [optional] 
**team_id** | **UUID** |  | 
**team_name** | **str** | Name of the associated team | [optional] 
**created_at** | **datetime** |  | 
**modified_at** | **datetime** |  | [optional] 

## Example

```python
from tmi_client.models.project_list_item import ProjectListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListItem from a JSON string
project_list_item_instance = ProjectListItem.from_json(json)
# print the JSON string representation of the object
print(ProjectListItem.to_json())

# convert the object into a dict
project_list_item_dict = project_list_item_instance.to_dict()
# create an instance of ProjectListItem from a dict
project_list_item_from_dict = ProjectListItem.from_dict(project_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


