# JsonPatchDocumentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** | Patch operation type | 
**path** | **str** | JSON path to target | 
**value** | **object** | The value to use for add/replace/test operations. Can be any JSON value per RFC 6902 (string, number, boolean, object, array, or null). | [optional] 

## Example

```python
from tmi_client.models.json_patch_document_inner import JsonPatchDocumentInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonPatchDocumentInner from a JSON string
json_patch_document_inner_instance = JsonPatchDocumentInner.from_json(json)
# print the JSON string representation of the object
print(JsonPatchDocumentInner.to_json())

# convert the object into a dict
json_patch_document_inner_dict = json_patch_document_inner_instance.to_dict()
# create an instance of JsonPatchDocumentInner from a dict
json_patch_document_inner_from_dict = JsonPatchDocumentInner.from_dict(json_patch_document_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


