# RelatedTeam

A relationship entry linking to another team

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_team_id** | **UUID** | UUID of the related team | 
**relationship** | [**RelationshipType**](RelationshipType.md) |  | 
**custom_relationship** | **str** | Custom relationship description when relationship is &#39;other&#39; | [optional] 

## Example

```python
from tmi_client.models.related_team import RelatedTeam

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedTeam from a JSON string
related_team_instance = RelatedTeam.from_json(json)
# print the JSON string representation of the object
print(RelatedTeam.to_json())

# convert the object into a dict
related_team_dict = related_team_instance.to_dict()
# create an instance of RelatedTeam from a dict
related_team_from_dict = RelatedTeam.from_dict(related_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


