# BulkDeleteThreatModelThreats500Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message describing what went wrong | 
**request_id** | **str** | Unique request identifier for troubleshooting | [optional] 

## Example

```python
from tmi_client.models.bulk_delete_threat_model_threats500_response import BulkDeleteThreatModelThreats500Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteThreatModelThreats500Response from a JSON string
bulk_delete_threat_model_threats500_response_instance = BulkDeleteThreatModelThreats500Response.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteThreatModelThreats500Response.to_json())

# convert the object into a dict
bulk_delete_threat_model_threats500_response_dict = bulk_delete_threat_model_threats500_response_instance.to_dict()
# create an instance of BulkDeleteThreatModelThreats500Response from a dict
bulk_delete_threat_model_threats500_response_from_dict = BulkDeleteThreatModelThreats500Response.from_dict(bulk_delete_threat_model_threats500_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


