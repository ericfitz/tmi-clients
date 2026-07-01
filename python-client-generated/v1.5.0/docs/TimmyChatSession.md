# TimmyChatSession

A Timmy AI assistant chat session within a threat model

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the chat session | [readonly] 
**threat_model_id** | **UUID** | Identifier of the parent threat model | [readonly] 
**user_id** | **UUID** | Identifier of the user who created the session | [readonly] 
**title** | **str** | Optional session title | [optional] 
**source_snapshot** | [**List[TimmyChatSessionSourceSnapshotInner]**](TimmyChatSessionSourceSnapshotInner.md) | Snapshot of source entities used for context | [optional] 
**system_prompt_hash** | **str** | Hash of the system prompt used for this session | [optional] [readonly] 
**status** | **str** | Current status of the chat session | 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [readonly] 

## Example

```python
from tmi_client.models.timmy_chat_session import TimmyChatSession

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyChatSession from a JSON string
timmy_chat_session_instance = TimmyChatSession.from_json(json)
# print the JSON string representation of the object
print(TimmyChatSession.to_json())

# convert the object into a dict
timmy_chat_session_dict = timmy_chat_session_instance.to_dict()
# create an instance of TimmyChatSession from a dict
timmy_chat_session_from_dict = TimmyChatSession.from_dict(timmy_chat_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


