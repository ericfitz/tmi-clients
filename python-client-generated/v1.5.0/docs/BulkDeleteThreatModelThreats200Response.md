# BulkDeleteThreatModelThreats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_count** | **int** | Number of threats deleted | [optional] 
**deleted_ids** | **List[UUID]** | IDs of deleted threats | [optional] 

## Example

```python
from tmi_client.models.bulk_delete_threat_model_threats200_response import BulkDeleteThreatModelThreats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteThreatModelThreats200Response from a JSON string
bulk_delete_threat_model_threats200_response_instance = BulkDeleteThreatModelThreats200Response.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteThreatModelThreats200Response.to_json())

# convert the object into a dict
bulk_delete_threat_model_threats200_response_dict = bulk_delete_threat_model_threats200_response_instance.to_dict()
# create an instance of BulkDeleteThreatModelThreats200Response from a dict
bulk_delete_threat_model_threats200_response_from_dict = BulkDeleteThreatModelThreats200Response.from_dict(bulk_delete_threat_model_threats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


