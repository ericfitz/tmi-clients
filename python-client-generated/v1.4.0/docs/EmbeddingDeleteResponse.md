# EmbeddingDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **int** | Number of embeddings deleted | 

## Example

```python
from tmi_client.models.embedding_delete_response import EmbeddingDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingDeleteResponse from a JSON string
embedding_delete_response_instance = EmbeddingDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddingDeleteResponse.to_json())

# convert the object into a dict
embedding_delete_response_dict = embedding_delete_response_instance.to_dict()
# create an instance of EmbeddingDeleteResponse from a dict
embedding_delete_response_from_dict = EmbeddingDeleteResponse.from_dict(embedding_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


