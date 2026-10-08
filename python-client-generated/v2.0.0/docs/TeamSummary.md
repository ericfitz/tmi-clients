# TeamSummary

Minimal team reference embedded in other resources. Only the identifying fields are resolved; fetch /teams/{team_id} for the complete team.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the team (UUID) | [readonly] 
**name** | **str** | Team name | 
**description** | **str** | Team description | [optional] 

## Example

```python
from tmi_client.models.team_summary import TeamSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TeamSummary from a JSON string
team_summary_instance = TeamSummary.from_json(json)
# print the JSON string representation of the object
print(TeamSummary.to_json())

# convert the object into a dict
team_summary_dict = team_summary_instance.to_dict()
# create an instance of TeamSummary from a dict
team_summary_from_dict = TeamSummary.from_dict(team_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


