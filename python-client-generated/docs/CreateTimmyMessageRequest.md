# CreateTimmyMessageRequest

Request body for creating a message in a Timmy chat session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | Message content to send to Timmy | 

## Example

```python
from tmi_client.models.create_timmy_message_request import CreateTimmyMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTimmyMessageRequest from a JSON string
create_timmy_message_request_instance = CreateTimmyMessageRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTimmyMessageRequest.to_json())

# convert the object into a dict
create_timmy_message_request_dict = create_timmy_message_request_instance.to_dict()
# create an instance of CreateTimmyMessageRequest from a dict
create_timmy_message_request_from_dict = CreateTimmyMessageRequest.from_dict(create_timmy_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


