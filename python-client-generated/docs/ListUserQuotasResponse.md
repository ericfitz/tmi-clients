# ListUserQuotasResponse

Paginated list of user API quotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**List[UserAPIQuota]**](UserAPIQuota.md) |  | 
**total** | **int** | Total number of quotas matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_user_quotas_response import ListUserQuotasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserQuotasResponse from a JSON string
list_user_quotas_response_instance = ListUserQuotasResponse.from_json(json)
# print the JSON string representation of the object
print(ListUserQuotasResponse.to_json())

# convert the object into a dict
list_user_quotas_response_dict = list_user_quotas_response_instance.to_dict()
# create an instance of ListUserQuotasResponse from a dict
list_user_quotas_response_from_dict = ListUserQuotasResponse.from_dict(list_user_quotas_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


