# TimmyChatMessage

A message within a Timmy chat session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier for the message | [readonly] 
**session_id** | **UUID** | Identifier of the parent chat session | [readonly] 
**role** | **str** | Role of the message sender | 
**content** | **str** | Message content | 
**token_count** | **int** | Number of tokens in the message | [optional] [readonly] 
**sequence** | **int** | Message sequence number within the session | [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [readonly] 

## Example

```python
from tmi_client.models.timmy_chat_message import TimmyChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TimmyChatMessage from a JSON string
timmy_chat_message_instance = TimmyChatMessage.from_json(json)
# print the JSON string representation of the object
print(TimmyChatMessage.to_json())

# convert the object into a dict
timmy_chat_message_dict = timmy_chat_message_instance.to_dict()
# create an instance of TimmyChatMessage from a dict
timmy_chat_message_from_dict = TimmyChatMessage.from_dict(timmy_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


