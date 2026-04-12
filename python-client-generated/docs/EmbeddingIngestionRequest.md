# EmbeddingIngestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_type** | **str** | Target index type | 
**embeddings** | [**List[EmbeddingIngestionItem]**](EmbeddingIngestionItem.md) | Batch of pre-computed embeddings | 

## Example

```python
from tmi_client.models.embedding_ingestion_request import EmbeddingIngestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingIngestionRequest from a JSON string
embedding_ingestion_request_instance = EmbeddingIngestionRequest.from_json(json)
# print the JSON string representation of the object
print(EmbeddingIngestionRequest.to_json())

# convert the object into a dict
embedding_ingestion_request_dict = embedding_ingestion_request_instance.to_dict()
# create an instance of EmbeddingIngestionRequest from a dict
embedding_ingestion_request_from_dict = EmbeddingIngestionRequest.from_dict(embedding_ingestion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


