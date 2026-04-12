# RelatedProject

A relationship entry linking to another project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related_project_id** | **UUID** | UUID of the related project | 
**relationship** | [**RelationshipType**](RelationshipType.md) |  | 
**custom_relationship** | **str** | Custom relationship description when relationship is &#39;other&#39; | [optional] 

## Example

```python
from tmi_client.models.related_project import RelatedProject

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedProject from a JSON string
related_project_instance = RelatedProject.from_json(json)
# print the JSON string representation of the object
print(RelatedProject.to_json())

# convert the object into a dict
related_project_dict = related_project_instance.to_dict()
# create an instance of RelatedProject from a dict
related_project_from_dict = RelatedProject.from_dict(related_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


