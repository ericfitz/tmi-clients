# SkippedSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **UUID** | ID of the skipped entity | 
**name** | **str** | Name of the skipped entity | 
**reason** | **str** | Why this entity was skipped | 

## Example

```python
from tmi_client.models.skipped_source import SkippedSource

# TODO update the JSON string below
json = "{}"
# create an instance of SkippedSource from a JSON string
skipped_source_instance = SkippedSource.from_json(json)
# print the JSON string representation of the object
print(SkippedSource.to_json())

# convert the object into a dict
skipped_source_dict = skipped_source_instance.to_dict()
# create an instance of SkippedSource from a dict
skipped_source_from_dict = SkippedSource.from_dict(skipped_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


