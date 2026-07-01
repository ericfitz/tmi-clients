# ApiInfoService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the service | 
**build** | **str** | Current build number | 

## Example

```python
from tmi_client.models.api_info_service import ApiInfoService

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInfoService from a JSON string
api_info_service_instance = ApiInfoService.from_json(json)
# print the JSON string representation of the object
print(ApiInfoService.to_json())

# convert the object into a dict
api_info_service_dict = api_info_service_instance.to_dict()
# create an instance of ApiInfoService from a dict
api_info_service_from_dict = ApiInfoService.from_dict(api_info_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


