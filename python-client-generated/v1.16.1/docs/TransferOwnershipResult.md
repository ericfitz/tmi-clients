# TransferOwnershipResult

Result of an ownership transfer operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_models_transferred** | [**TransferOwnershipResultThreatModelsTransferred**](TransferOwnershipResultThreatModelsTransferred.md) |  | 
**survey_responses_transferred** | [**TransferOwnershipResultSurveyResponsesTransferred**](TransferOwnershipResultSurveyResponsesTransferred.md) |  | 

## Example

```python
from tmi_client.models.transfer_ownership_result import TransferOwnershipResult

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOwnershipResult from a JSON string
transfer_ownership_result_instance = TransferOwnershipResult.from_json(json)
# print the JSON string representation of the object
print(TransferOwnershipResult.to_json())

# convert the object into a dict
transfer_ownership_result_dict = transfer_ownership_result_instance.to_dict()
# create an instance of TransferOwnershipResult from a dict
transfer_ownership_result_from_dict = TransferOwnershipResult.from_dict(transfer_ownership_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


