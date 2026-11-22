# ApiInfoApi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | API version | 
**specification** | **str** | URL to the API specification | 

## Example

```python
from tmi_client.models.api_info_api import ApiInfoApi

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoApi from a JSON string
api_info_api_instance = ApiInfoApi.from_json(json)
# print the JSON string representation of the object
print(ApiInfoApi.to_json())

# convert the object into a dict
api_info_api_dict = api_info_api_instance.to_dict()
# create an instance of ApiInfoApi from a dict
api_info_api_from_dict = ApiInfoApi.from_dict(api_info_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


