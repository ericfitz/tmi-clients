# TimmyChatSessionSourceSnapshotInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Type of the source entity | [optional] 
**entity_id** | **UUID** | Identifier of the source entity | [optional] 

## Example

```python
from tmi_client.models.timmy_chat_session_source_snapshot_inner import TimmyChatSessionSourceSnapshotInner

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyChatSessionSourceSnapshotInner from a JSON string
timmy_chat_session_source_snapshot_inner_instance = TimmyChatSessionSourceSnapshotInner.from_json(json)
# print the JSON string representation of the object
print(TimmyChatSessionSourceSnapshotInner.to_json())

# convert the object into a dict
timmy_chat_session_source_snapshot_inner_dict = timmy_chat_session_source_snapshot_inner_instance.to_dict()
# create an instance of TimmyChatSessionSourceSnapshotInner from a dict
timmy_chat_session_source_snapshot_inner_from_dict = TimmyChatSessionSourceSnapshotInner.from_dict(timmy_chat_session_source_snapshot_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


