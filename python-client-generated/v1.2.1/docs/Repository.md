# Repository

Complete Repository schema with server-generated fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the source code reference | [optional] 
**description** | **str** | Description of the referenced source code | [optional] 
**type** | **str** | Source code repository type | [optional] 
**parameters** | [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**uri** | **str** | URL to retrieve the referenced source code | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**id** | **UUID** | Unique identifier for the repository | [readonly] 
**metadata** | [**List[Metadata]**](Metadata.md) | Optional metadata key-value pairs | [optional] [readonly] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | [optional] [readonly] 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | [optional] [readonly] 

## Example

```python
from tmi_client.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print(Repository.to_json())

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_from_dict = Repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


