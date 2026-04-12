# RepositoryBase

Base fields for Repository (user-writable only)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the source code reference | [optional] 
**description** | **str** | Description of the referenced source code | [optional] 
**type** | **str** | Source code repository type | [optional] 
**parameters** | [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**uri** | **str** | URL to retrieve the referenced source code | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]

## Example

```python
from tmi_client.models.repository_base import RepositoryBase

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryBase from a JSON string
repository_base_instance = RepositoryBase.from_json(json)
# print the JSON string representation of the object
print(RepositoryBase.to_json())

# convert the object into a dict
repository_base_dict = repository_base_instance.to_dict()
# create an instance of RepositoryBase from a dict
repository_base_from_dict = RepositoryBase.from_dict(repository_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


