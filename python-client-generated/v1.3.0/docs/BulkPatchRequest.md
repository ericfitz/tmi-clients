# BulkPatchRequest

Request body for bulk patching multiple threats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patches** | [**List[BulkPatchRequestPatchesInner]**](BulkPatchRequestPatchesInner.md) | Array of patch operations, each targeting a specific threat by ID | 

## Example

```python
from tmi_client.models.bulk_patch_request import BulkPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPatchRequest from a JSON string
bulk_patch_request_instance = BulkPatchRequest.from_json(json)
# print the JSON string representation of the object
print(BulkPatchRequest.to_json())

# convert the object into a dict
bulk_patch_request_dict = bulk_patch_request_instance.to_dict()
# create an instance of BulkPatchRequest from a dict
bulk_patch_request_from_dict = BulkPatchRequest.from_dict(bulk_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


