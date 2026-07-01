# BulkPatchRequestPatchesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | ID of the threat to patch | 
**operations** | [**List[JsonPatchDocumentInner]**](JsonPatchDocumentInner.md) | JSON Patch document as defined in RFC 6902 | 

## Example

```python
from tmi_client.models.bulk_patch_request_patches_inner import BulkPatchRequestPatchesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkPatchRequestPatchesInner from a JSON string
bulk_patch_request_patches_inner_instance = BulkPatchRequestPatchesInner.from_json(json)
# print the JSON string representation of the object
print(BulkPatchRequestPatchesInner.to_json())

# convert the object into a dict
bulk_patch_request_patches_inner_dict = bulk_patch_request_patches_inner_instance.to_dict()
# create an instance of BulkPatchRequestPatchesInner from a dict
bulk_patch_request_patches_inner_from_dict = BulkPatchRequestPatchesInner.from_dict(bulk_patch_request_patches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


