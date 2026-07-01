# Principal

Base identity representation for users and groups with portable, globally-unique identifiers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** | Type of principal: user (individual) or group | 
**provider** | **str** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;tmi\&quot; for TMI built-in groups. | 
**provider_id** | **str** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**display_name** | **str** | Human-readable display name for UI presentation | [optional] 
**email** | **str** | Email address (required for users, optional for groups) | [optional] 

## Example

```python
from tmi_client.models.principal import Principal

# TODO update the JSON string below
json = "{}"
# create an instance of Principal from a JSON string
principal_instance = Principal.from_json(json)
# print the JSON string representation of the object
print(Principal.to_json())

# convert the object into a dict
principal_dict = principal_instance.to_dict()
# create an instance of Principal from a dict
principal_from_dict = Principal.from_dict(principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


