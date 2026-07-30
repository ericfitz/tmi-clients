# ListAddonsResponse

Paginated list of registered addons

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addons** | [**List[AddonResponse]**](AddonResponse.md) |  | 
**total** | **int** | Total number of add-ons matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_addons_response import ListAddonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddonsResponse from a JSON string
list_addons_response_instance = ListAddonsResponse.from_json(json)
# print the JSON string representation of the object
print(ListAddonsResponse.to_json())

# convert the object into a dict
list_addons_response_dict = list_addons_response_instance.to_dict()
# create an instance of ListAddonsResponse from a dict
list_addons_response_from_dict = ListAddonsResponse.from_dict(list_addons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


