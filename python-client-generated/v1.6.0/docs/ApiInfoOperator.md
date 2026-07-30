# ApiInfoOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Operator name from environment variables | 
**contact** | **str** | Operator contact information from environment variables | 

## Example

```python
from tmi_client.models.api_info_operator import ApiInfoOperator

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoOperator from a JSON string
api_info_operator_instance = ApiInfoOperator.from_json(json)
# print the JSON string representation of the object
print(ApiInfoOperator.to_json())

# convert the object into a dict
api_info_operator_dict = api_info_operator_instance.to_dict()
# create an instance of ApiInfoOperator from a dict
api_info_operator_from_dict = ApiInfoOperator.from_dict(api_info_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


