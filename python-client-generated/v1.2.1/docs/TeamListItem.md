# TeamListItem

Summary of a team for list views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**member_count** | **int** | Number of team members | [optional] 
**project_count** | **int** | Number of projects associated with this team | [optional] 
**created_at** | **datetime** |  | 
**modified_at** | **datetime** |  | [optional] 

## Example

```python
from tmi_client.models.team_list_item import TeamListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TeamListItem from a JSON string
team_list_item_instance = TeamListItem.from_json(json)
# print the JSON string representation of the object
print(TeamListItem.to_json())

# convert the object into a dict
team_list_item_dict = team_list_item_instance.to_dict()
# create an instance of TeamListItem from a dict
team_list_item_from_dict = TeamListItem.from_dict(team_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


