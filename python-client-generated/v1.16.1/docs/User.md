# User

User profile information retrieved from identity provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**principal_type** | **str** | Always \&quot;user\&quot; for User objects | 
**provider** | **str** | Identity provider name (e.g., \&quot;google\&quot;, \&quot;github\&quot;, \&quot;microsoft\&quot;, \&quot;tmi\&quot;). Use \&quot;tmi\&quot; for TMI built-in groups. | 
**provider_id** | **str** | Provider-assigned identifier. For users: provider_user_id (e.g., email or OAuth sub). For groups: group_name. | 
**display_name** | **str** | User full name for display | 
**email** | **str** | User email address (required) | 

## Example

```python
from tmi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


