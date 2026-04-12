# DocumentInput

Input schema for creating or updating Document

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name | 
**description** | **str** | Description of document purpose or content | [optional] 
**uri** | **str** | URL location of the document | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.document_input import DocumentInput

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentInput from a JSON string
document_input_instance = DocumentInput.from_json(json)
# print the JSON string representation of the object
print(DocumentInput.to_json())

# convert the object into a dict
document_input_dict = document_input_instance.to_dict()
# create an instance of DocumentInput from a dict
document_input_from_dict = DocumentInput.from_dict(document_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


