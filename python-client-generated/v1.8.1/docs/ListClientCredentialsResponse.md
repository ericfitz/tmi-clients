# ListClientCredentialsResponse

Paginated list of client credentials

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[ClientCredentialInfo]**](ClientCredentialInfo.md) |  | 
**total** | **int** | Total number of credentials matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_client_credentials_response import ListClientCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientCredentialsResponse from a JSON string
list_client_credentials_response_instance = ListClientCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(ListClientCredentialsResponse.to_json())

# convert the object into a dict
list_client_credentials_response_dict = list_client_credentials_response_instance.to_dict()
# create an instance of ListClientCredentialsResponse from a dict
list_client_credentials_response_from_dict = ListClientCredentialsResponse.from_dict(list_client_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


