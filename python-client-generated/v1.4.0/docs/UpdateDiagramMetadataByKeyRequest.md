# UpdateDiagramMetadataByKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Metadata value | 

## Example

```python
from tmi_client.models.update_diagram_metadata_by_key_request import UpdateDiagramMetadataByKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDiagramMetadataByKeyRequest from a JSON string
update_diagram_metadata_by_key_request_instance = UpdateDiagramMetadataByKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDiagramMetadataByKeyRequest.to_json())

# convert the object into a dict
update_diagram_metadata_by_key_request_dict = update_diagram_metadata_by_key_request_instance.to_dict()
# create an instance of UpdateDiagramMetadataByKeyRequest from a dict
update_diagram_metadata_by_key_request_from_dict = UpdateDiagramMetadataByKeyRequest.from_dict(update_diagram_metadata_by_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


