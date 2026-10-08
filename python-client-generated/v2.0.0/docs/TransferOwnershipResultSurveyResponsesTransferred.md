# TransferOwnershipResultSurveyResponsesTransferred

Survey responses that were transferred

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of survey responses transferred | 
**survey_response_ids** | **List[UUID]** | IDs of the transferred survey responses | 

## Example

```python
from tmi_client.models.transfer_ownership_result_survey_responses_transferred import TransferOwnershipResultSurveyResponsesTransferred

# TODO update the JSON string below
json = "{}"
# create an instance of TransferOwnershipResultSurveyResponsesTransferred from a JSON string
transfer_ownership_result_survey_responses_transferred_instance = TransferOwnershipResultSurveyResponsesTransferred.from_json(json)
# print the JSON string representation of the object
print(TransferOwnershipResultSurveyResponsesTransferred.to_json())

# convert the object into a dict
transfer_ownership_result_survey_responses_transferred_dict = transfer_ownership_result_survey_responses_transferred_instance.to_dict()
# create an instance of TransferOwnershipResultSurveyResponsesTransferred from a dict
transfer_ownership_result_survey_responses_transferred_from_dict = TransferOwnershipResultSurveyResponsesTransferred.from_dict(transfer_ownership_result_survey_responses_transferred_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


