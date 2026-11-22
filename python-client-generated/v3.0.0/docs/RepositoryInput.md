# RepositoryInput

Input schema for creating or updating Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name for the source code reference | [optional] 
**description** | **str** | Description of the referenced source code | [optional] 
**type** | **str** | Source code repository type | [optional] 
**parameters** | [**RepositoryBaseParameters**](RepositoryBaseParameters.md) |  | [optional] 
**uri** | **str** | URL to retrieve the referenced source code | 
**include_in_report** | **bool** | Whether this item should be included in generated reports | [optional] [default to True]
**timmy_enabled** | **bool** | Whether the Timmy AI assistant is enabled for this entity | [optional] [default to True]

## Example

```python
from tmi_client.models.repository_input import RepositoryInput

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryInput from a JSON string
repository_input_instance = RepositoryInput.from_json(json)
# print the JSON string representation of the object
print(RepositoryInput.to_json())

# convert the object into a dict
repository_input_dict = repository_input_instance.to_dict()
# create an instance of RepositoryInput from a dict
repository_input_from_dict = RepositoryInput.from_dict(repository_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


