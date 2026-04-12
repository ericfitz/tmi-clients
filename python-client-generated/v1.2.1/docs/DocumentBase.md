# DocumentBase

Base fields for Document (user-writable only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name | 
**description** | **str** | Description of document purpose or content | [optional] 
**uri** | **str** | URL location of the document | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.document_base import DocumentBase

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBase from a JSON string
document_base_instance = DocumentBase.from_json(json)
# print the JSON string representation of the object
print(DocumentBase.to_json())

# convert the object into a dict
document_base_dict = document_base_instance.to_dict()
# create an instance of DocumentBase from a dict
document_base_from_dict = DocumentBase.from_dict(document_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


