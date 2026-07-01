# ContentTokenList

List response wrapper for delegated content provider tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_tokens** | [**List[ContentTokenInfo]**](ContentTokenInfo.md) | Array of linked content tokens for the user. | 

## Example

```python
from tmi_client.models.content_token_list import ContentTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTokenList from a JSON string
content_token_list_instance = ContentTokenList.from_json(json)
# print the JSON string representation of the object
print(ContentTokenList.to_json())

# convert the object into a dict
content_token_list_dict = content_token_list_instance.to_dict()
# create an instance of ContentTokenList from a dict
content_token_list_from_dict = ContentTokenList.from_dict(content_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


