# AddonResponse

Addon details including configuration and status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Add-on identifier | 
**created_at** | **datetime** | Creation timestamp | 
**name** | **str** | Display name | 
**webhook_id** | **UUID** | Associated webhook subscription ID | 
**description** | **str** | Add-on description | [optional] 
**icon** | **str** | Icon identifier | [optional] 
**objects** | **List[str]** | Supported TMI object types | [optional] 
**threat_model_id** | **UUID** | Threat model scope (if scoped) | [optional] 
**parameters** | [**List[AddonParameter]**](AddonParameter.md) | Typed parameter declarations for client UI generation. Each parameter defines a name, type, and type-specific configuration that clients use to render appropriate input controls. | [optional] 

## Example

```python
from tmi_client.models.addon_response import AddonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponse from a JSON string
addon_response_instance = AddonResponse.from_json(json)
# print the JSON string representation of the object
print(AddonResponse.to_json())

# convert the object into a dict
addon_response_dict = addon_response_instance.to_dict()
# create an instance of AddonResponse from a dict
addon_response_from_dict = AddonResponse.from_dict(addon_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


