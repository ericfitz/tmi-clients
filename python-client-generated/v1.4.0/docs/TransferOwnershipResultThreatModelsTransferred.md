# TransferOwnershipResultThreatModelsTransferred

Threat models that were transferred

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of threat models transferred | 
**threat_model_ids** | **List[UUID]** | IDs of the transferred threat models | 

## Example

```python
from tmi_client.models.transfer_ownership_result_threat_models_transferred import TransferOwnershipResultThreatModelsTransferred

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOwnershipResultThreatModelsTransferred from a JSON string
transfer_ownership_result_threat_models_transferred_instance = TransferOwnershipResultThreatModelsTransferred.from_json(json)
# print the JSON string representation of the object
print(TransferOwnershipResultThreatModelsTransferred.to_json())

# convert the object into a dict
transfer_ownership_result_threat_models_transferred_dict = transfer_ownership_result_threat_models_transferred_instance.to_dict()
# create an instance of TransferOwnershipResultThreatModelsTransferred from a dict
transfer_ownership_result_threat_models_transferred_from_dict = TransferOwnershipResultThreatModelsTransferred.from_dict(transfer_ownership_result_threat_models_transferred_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


