# ListContentFeedback200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ContentFeedback]**](ContentFeedback.md) |  | 
**total** | **int** |  | 

## Example

```python
from tmi_client.models.list_content_feedback200_response import ListContentFeedback200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListContentFeedback200Response from a JSON string
list_content_feedback200_response_instance = ListContentFeedback200Response.from_json(json)
# print the JSON string representation of the object
print(ListContentFeedback200Response.to_json())

# convert the object into a dict
list_content_feedback200_response_dict = list_content_feedback200_response_instance.to_dict()
# create an instance of ListContentFeedback200Response from a dict
list_content_feedback200_response_from_dict = ListContentFeedback200Response.from_dict(list_content_feedback200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


