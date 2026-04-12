# ExtendedAsset

Asset with extended metadata for detailed security analysis

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
**id** | **UUID** | Unique identifier for the asset | [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (ISO3339) | 
**modified_at** | **datetime** | Last modification timestamp (ISO3339) | 
**deleted_at** | **datetime** | Deletion timestamp (RFC3339). Present only on soft-deleted entities within the tombstone retention period. | [optional] [readonly] 
**threat_model_id** | **UUID** | ID of the threat model this asset belongs to | 

## Example

```python
from tmi_client.models.extended_asset import ExtendedAsset

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedAsset from a JSON string
extended_asset_instance = ExtendedAsset.from_json(json)
# print the JSON string representation of the object
print(ExtendedAsset.to_json())

# convert the object into a dict
extended_asset_dict = extended_asset_instance.to_dict()
# create an instance of ExtendedAsset from a dict
extended_asset_from_dict = ExtendedAsset.from_dict(extended_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


