# EmbeddingProviderConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Embedding provider name | 
**model** | **str** | Embedding model name | 
**api_key** | **str** | Embedding provider API key | [optional] 
**base_url** | **str** | Custom base URL for self-hosted endpoints | [optional] 

## Example

```python
from tmi_client.models.embedding_provider_config import EmbeddingProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingProviderConfig from a JSON string
embedding_provider_config_instance = EmbeddingProviderConfig.from_json(json)
# print the JSON string representation of the object
print(EmbeddingProviderConfig.to_json())

# convert the object into a dict
embedding_provider_config_dict = embedding_provider_config_instance.to_dict()
# create an instance of EmbeddingProviderConfig from a dict
embedding_provider_config_from_dict = EmbeddingProviderConfig.from_dict(embedding_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


