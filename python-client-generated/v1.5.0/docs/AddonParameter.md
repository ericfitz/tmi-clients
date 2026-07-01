# AddonParameter

Typed parameter declaration for an add-on, used to drive client UI generation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name (used as key in invocation data payload) | 
**type** | **str** | Parameter type determining client UI control | 
**description** | **str** | Human-readable description for UI display | [optional] 
**required** | **bool** | Whether the parameter must be provided on invocation | [optional] [default to False]
**enum_values** | **List[str]** | Allowed values (applicable when type is &#39;enum&#39;) | [optional] 
**default_value** | **str** | Default value if not provided by user | [optional] 
**metadata_key** | **str** | Metadata key name to auto-populate from TMI object (applicable when type is &#39;metadata_key&#39;) | [optional] 
**number_min** | **float** | Minimum allowed value (applicable when type is &#39;number&#39;) | [optional] 
**number_max** | **float** | Maximum allowed value (applicable when type is &#39;number&#39;) | [optional] 
**string_max_length** | **int** | Maximum string length (applicable when type is &#39;string&#39;) | [optional] 
**string_validation_regex** | **str** | Regular expression for string validation (applicable when type is &#39;string&#39;) | [optional] 

## Example

```python
from tmi_client.models.addon_parameter import AddonParameter

# TODO update the JSON string below
json = "{}"
# create an instance of AddonParameter from a JSON string
addon_parameter_instance = AddonParameter.from_json(json)
# print the JSON string representation of the object
print(AddonParameter.to_json())

# convert the object into a dict
addon_parameter_dict = addon_parameter_instance.to_dict()
# create an instance of AddonParameter from a dict
addon_parameter_from_dict = AddonParameter.from_dict(addon_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


