# CreateAddonRequest

Request schema for registering a new addon

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the add-on | 
**webhook_id** | **UUID** | UUID of the associated webhook subscription | 
**description** | **str** | Description of what the add-on does | [optional] 
**icon** | **str** | Icon identifier (Material Symbols or FontAwesome format) | [optional] 
**objects** | **List[str]** | TMI object types this add-on can operate on | [optional] 
**threat_model_id** | **UUID** | Optional: Scope add-on to specific threat model | [optional] 
**parameters** | [**List[AddonParameter]**](AddonParameter.md) | Typed parameter declarations for client UI generation. Each parameter defines a name, type, and type-specific configuration that clients use to render appropriate input controls. | [optional] 

## Example

```python
from tmi_client.models.create_addon_request import CreateAddonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddonRequest from a JSON string
create_addon_request_instance = CreateAddonRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAddonRequest.to_json())

# convert the object into a dict
create_addon_request_dict = create_addon_request_instance.to_dict()
# create an instance of CreateAddonRequest from a dict
create_addon_request_from_dict = CreateAddonRequest.from_dict(create_addon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


