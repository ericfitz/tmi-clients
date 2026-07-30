# RepositoryBulkUpdateItem

Repository data for bulk update operations, including required ID field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the source code reference | [optional] 
**description** | **str** | Description of the referenced source code | [optional] 
**type** | **str** | Source code repository type | [optional] 
**parameters** | [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**uri** | **str** | URL to retrieve the referenced source code | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**id** | **UUID** | Unique identifier of the repository to update (required for bulk updates) | 

## Example

```python
from tmi_client.models.repository_bulk_update_item import RepositoryBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryBulkUpdateItem from a JSON string
repository_bulk_update_item_instance = RepositoryBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(RepositoryBulkUpdateItem.to_json())

# convert the object into a dict
repository_bulk_update_item_dict = repository_bulk_update_item_instance.to_dict()
# create an instance of RepositoryBulkUpdateItem from a dict
repository_bulk_update_item_from_dict = RepositoryBulkUpdateItem.from_dict(repository_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


