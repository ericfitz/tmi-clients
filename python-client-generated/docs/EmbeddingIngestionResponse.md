# EmbeddingIngestionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingested** | **int** | Number of embeddings ingested | 

## Example

```python
from tmi_client.models.embedding_ingestion_response import EmbeddingIngestionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingIngestionResponse from a JSON string
embedding_ingestion_response_instance = EmbeddingIngestionResponse.from_json(json)
# print the JSON string representation of the object
print(EmbeddingIngestionResponse.to_json())

# convert the object into a dict
embedding_ingestion_response_dict = embedding_ingestion_response_instance.to_dict()
# create an instance of EmbeddingIngestionResponse from a dict
embedding_ingestion_response_from_dict = EmbeddingIngestionResponse.from_dict(embedding_ingestion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


