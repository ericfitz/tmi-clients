# CreateTimmySessionRequest

Optional request body for creating a Timmy chat session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Optional session title | [optional] 

## Example

```python
from tmi_client.models.create_timmy_session_request import CreateTimmySessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimmySessionRequest from a JSON string
create_timmy_session_request_instance = CreateTimmySessionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTimmySessionRequest.to_json())

# convert the object into a dict
create_timmy_session_request_dict = create_timmy_session_request_instance.to_dict()
# create an instance of CreateTimmySessionRequest from a dict
create_timmy_session_request_from_dict = CreateTimmySessionRequest.from_dict(create_timmy_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


