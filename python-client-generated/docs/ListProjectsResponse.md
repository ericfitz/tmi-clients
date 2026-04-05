# ListProjectsResponse

Paginated list of projects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectListItem]**](ProjectListItem.md) |  | 
**total** | **int** | Total number of projects matching the filter | 
**limit** | **int** | Maximum number of results per page | 
**offset** | **int** | Number of results skipped | 

## Example

```python
from tmi_client.models.list_projects_response import ListProjectsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListProjectsResponse from a JSON string
list_projects_response_instance = ListProjectsResponse.from_json(json)
# print the JSON string representation of the object
print(ListProjectsResponse.to_json())

# convert the object into a dict
list_projects_response_dict = list_projects_response_instance.to_dict()
# create an instance of ListProjectsResponse from a dict
list_projects_response_from_dict = ListProjectsResponse.from_dict(list_projects_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


