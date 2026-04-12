# UpdateThreatMetadataByKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | New value for the metadata entry | 

## Example

```python
from tmi_client.models.update_threat_metadata_by_key_request import UpdateThreatMetadataByKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThreatMetadataByKeyRequest from a JSON string
update_threat_metadata_by_key_request_instance = UpdateThreatMetadataByKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateThreatMetadataByKeyRequest.to_json())

# convert the object into a dict
update_threat_metadata_by_key_request_dict = update_threat_metadata_by_key_request_instance.to_dict()
# create an instance of UpdateThreatMetadataByKeyRequest from a dict
update_threat_metadata_by_key_request_from_dict = UpdateThreatMetadataByKeyRequest.from_dict(update_threat_metadata_by_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


