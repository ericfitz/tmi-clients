# ListRepositoriesResponse

Paginated list of repositories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repositories** | [**List[Repository]**](Repository.md) |  | 
**total** | **int** | Total number of repositories matching criteria | 
**limit** | **int** | Pagination limit | 
**offset** | **int** | Pagination offset | 

## Example

```python
from tmi_client.models.list_repositories_response import ListRepositoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListRepositoriesResponse from a JSON string
list_repositories_response_instance = ListRepositoriesResponse.from_json(json)
# print the JSON string representation of the object
print(ListRepositoriesResponse.to_json())

# convert the object into a dict
list_repositories_response_dict = list_repositories_response_instance.to_dict()
# create an instance of ListRepositoriesResponse from a dict
list_repositories_response_from_dict = ListRepositoriesResponse.from_dict(list_repositories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


