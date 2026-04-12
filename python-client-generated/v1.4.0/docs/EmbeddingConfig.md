# EmbeddingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text_embedding** | [**EmbeddingProviderConfig**](EmbeddingProviderConfig.md) |  | 
**code_embedding** | [**EmbeddingProviderConfig**](EmbeddingProviderConfig.md) | Code embedding config. Null if not configured. | [optional] 

## Example

```python
from tmi_client.models.embedding_config import EmbeddingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingConfig from a JSON string
embedding_config_instance = EmbeddingConfig.from_json(json)
# print the JSON string representation of the object
print(EmbeddingConfig.to_json())

# convert the object into a dict
embedding_config_dict = embedding_config_instance.to_dict()
# create an instance of EmbeddingConfig from a dict
embedding_config_from_dict = EmbeddingConfig.from_dict(embedding_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


