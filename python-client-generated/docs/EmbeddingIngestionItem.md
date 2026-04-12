# EmbeddingIngestionItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Entity type (e.g., repository, asset) | 
**entity_id** | **UUID** | Entity UUID | 
**chunk_index** | **int** | Sequential chunk number | 
**chunk_text** | **str** | Original text of the chunk | 
**content_hash** | **str** | SHA256 hash of the original content | 
**embedding_model** | **str** | Model used to generate the embedding | 
**embedding_dim** | **int** | Embedding vector dimension | 
**vector** | **List[float]** | Embedding vector | 

## Example

```python
from tmi_client.models.embedding_ingestion_item import EmbeddingIngestionItem

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingIngestionItem from a JSON string
embedding_ingestion_item_instance = EmbeddingIngestionItem.from_json(json)
# print the JSON string representation of the object
print(EmbeddingIngestionItem.to_json())

# convert the object into a dict
embedding_ingestion_item_dict = embedding_ingestion_item_instance.to_dict()
# create an instance of EmbeddingIngestionItem from a dict
embedding_ingestion_item_from_dict = EmbeddingIngestionItem.from_dict(embedding_ingestion_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


