# AssetBulkUpdateItem

Asset data for bulk update operations, including required ID field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Asset name | 
**description** | **str** | Description of the asset | [optional] 
**type** | **str** | Type of asset | 
**criticality** | **str** | Criticality level of the asset | [optional] 
**classification** | **List[str]** | Classification tags for the asset | [optional] 
**sensitivity** | **str** | Sensitivity label for the asset | [optional] 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]
**id** | **UUID** | Unique identifier of the asset to update (required for bulk updates) | 

## Example

```python
from tmi_client.models.asset_bulk_update_item import AssetBulkUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of AssetBulkUpdateItem from a JSON string
asset_bulk_update_item_instance = AssetBulkUpdateItem.from_json(json)
# print the JSON string representation of the object
print(AssetBulkUpdateItem.to_json())

# convert the object into a dict
asset_bulk_update_item_dict = asset_bulk_update_item_instance.to_dict()
# create an instance of AssetBulkUpdateItem from a dict
asset_bulk_update_item_from_dict = AssetBulkUpdateItem.from_dict(asset_bulk_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


