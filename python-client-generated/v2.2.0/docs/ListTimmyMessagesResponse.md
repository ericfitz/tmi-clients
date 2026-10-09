# ListTimmyMessagesResponse

Paginated list of Timmy chat messages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[TimmyChatMessage]**](TimmyChatMessage.md) |  | 
**total** | **int** | Total number of messages matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_timmy_messages_response import ListTimmyMessagesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTimmyMessagesResponse from a JSON string
list_timmy_messages_response_instance = ListTimmyMessagesResponse.from_json(json)
# print the JSON string representation of the object
print(ListTimmyMessagesResponse.to_json())

# convert the object into a dict
list_timmy_messages_response_dict = list_timmy_messages_response_instance.to_dict()
# create an instance of ListTimmyMessagesResponse from a dict
list_timmy_messages_response_from_dict = ListTimmyMessagesResponse.from_dict(list_timmy_messages_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


