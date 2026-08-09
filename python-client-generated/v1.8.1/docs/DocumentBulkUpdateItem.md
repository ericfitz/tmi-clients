# DocumentBulkUpdateItem

Document data for bulk update operations, including required ID field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Document name | 
**description** | **str** | Description of document purpose or content | [optional] 
**uri** | **str** | URL location of the document | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**id** | **UUID** | Unique identifier of the document to update (required for bulk updates) | 

## Example

```python
from tmi_client.models.document_bulk_update_item import DocumentBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentBulkUpdateItem from a JSON string
document_bulk_update_item_instance = DocumentBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(DocumentBulkUpdateItem.to_json())

# convert the object into a dict
document_bulk_update_item_dict = document_bulk_update_item_instance.to_dict()
# create an instance of DocumentBulkUpdateItem from a dict
document_bulk_update_item_from_dict = DocumentBulkUpdateItem.from_dict(document_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


