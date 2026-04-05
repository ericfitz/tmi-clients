# ApiInfo

API information response for the root endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ApiInfoStatus**](ApiInfoStatus.md) |  | 
**service** | [**ApiInfoService**](ApiInfoService.md) |  | 
**api** | [**ApiInfoApi**](ApiInfoApi.md) |  | 
**operator** | [**ApiInfoOperator**](ApiInfoOperator.md) |  | [optional] 
**health** | [**ApiInfoHealth**](ApiInfoHealth.md) |  | [optional] 

## Example

```python
from tmi_client.models.api_info import ApiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfo from a JSON string
api_info_instance = ApiInfo.from_json(json)
# print the JSON string representation of the object
print(ApiInfo.to_json())

# convert the object into a dict
api_info_dict = api_info_instance.to_dict()
# create an instance of ApiInfo from a dict
api_info_from_dict = ApiInfo.from_dict(api_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


