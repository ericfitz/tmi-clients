# Document

Complete Document schema with server-generated fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name | 
**description** | **str** | Description of document purpose or content | [optional] 
**uri** | **str** | URL location of the document | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**id** | **UUID** | Unique identifier for the document | [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Example

```python
from tmi_client.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


