# ListAddonQuotasResponse

Paginated list of addon quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**List[AddonInvocationQuota]**](AddonInvocationQuota.md) |  | 
**total** | **int** | Total number of quotas matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_addon_quotas_response import ListAddonQuotasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListAddonQuotasResponse from a JSON string
list_addon_quotas_response_instance = ListAddonQuotasResponse.from_json(json)
# print the JSON string representation of the object
print(ListAddonQuotasResponse.to_json())

# convert the object into a dict
list_addon_quotas_response_dict = list_addon_quotas_response_instance.to_dict()
# create an instance of ListAddonQuotasResponse from a dict
list_addon_quotas_response_from_dict = ListAddonQuotasResponse.from_dict(list_addon_quotas_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


