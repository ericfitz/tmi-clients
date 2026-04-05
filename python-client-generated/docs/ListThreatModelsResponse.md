# ListThreatModelsResponse

Paginated list of threat models

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_models** | [**List[TMListItem]**](TMListItem.md) |  | 
**total** | **int** | Total number of threat models matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_threat_models_response import ListThreatModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListThreatModelsResponse from a JSON string
list_threat_models_response_instance = ListThreatModelsResponse.from_json(json)
# print the JSON string representation of the object
print(ListThreatModelsResponse.to_json())

# convert the object into a dict
list_threat_models_response_dict = list_threat_models_response_instance.to_dict()
# create an instance of ListThreatModelsResponse from a dict
list_threat_models_response_from_dict = ListThreatModelsResponse.from_dict(list_threat_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


