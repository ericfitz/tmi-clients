# PortConfigurationItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique port identifier | 
**group** | **str** | Port group this port belongs to | 
**attrs** | **object** | Visual attributes for port rendering (e.g., text visibility, circle styling) | [optional] 

## Example

```python
from tmi_client.models.port_configuration_items_inner import PortConfigurationItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PortConfigurationItemsInner from a JSON string
port_configuration_items_inner_instance = PortConfigurationItemsInner.from_json(json)
# print the JSON string representation of the object
print(PortConfigurationItemsInner.to_json())

# convert the object into a dict
port_configuration_items_inner_dict = port_configuration_items_inner_instance.to_dict()
# create an instance of PortConfigurationItemsInner from a dict
port_configuration_items_inner_from_dict = PortConfigurationItemsInner.from_dict(port_configuration_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


