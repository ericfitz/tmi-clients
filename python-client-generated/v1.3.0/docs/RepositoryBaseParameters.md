# RepositoryBaseParameters

repo-specific parameters for retrieving the source

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_type** | **str** | Reference type (branch, tag, or commit) | 
**ref_value** | **str** | Reference value (branch name, tag value, or commit id) | 
**sub_path** | **str** | Sub-path within the repository | [optional] 

## Example

```python
from tmi_client.models.repository_base_parameters import RepositoryBaseParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryBaseParameters from a JSON string
repository_base_parameters_instance = RepositoryBaseParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryBaseParameters.to_json())

# convert the object into a dict
repository_base_parameters_dict = repository_base_parameters_instance.to_dict()
# create an instance of RepositoryBaseParameters from a dict
repository_base_parameters_from_dict = RepositoryBaseParameters.from_dict(repository_base_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


