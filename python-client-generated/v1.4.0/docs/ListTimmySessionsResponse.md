# ListTimmySessionsResponse

Paginated list of Timmy chat sessions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**List[TimmyChatSession]**](TimmyChatSession.md) |  | 
**total** | **int** | Total number of sessions matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_timmy_sessions_response import ListTimmySessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListTimmySessionsResponse from a JSON string
list_timmy_sessions_response_instance = ListTimmySessionsResponse.from_json(json)
# print the JSON string representation of the object
print(ListTimmySessionsResponse.to_json())

# convert the object into a dict
list_timmy_sessions_response_dict = list_timmy_sessions_response_instance.to_dict()
# create an instance of ListTimmySessionsResponse from a dict
list_timmy_sessions_response_from_dict = ListTimmySessionsResponse.from_dict(list_timmy_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


