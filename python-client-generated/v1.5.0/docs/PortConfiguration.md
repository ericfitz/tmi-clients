# PortConfiguration

Port configuration for node connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**Dict[str, PortConfigurationGroupsValue]**](PortConfigurationGroupsValue.md) | Port group definitions | [optional] 
**items** | [**List[PortConfigurationItemsInner]**](PortConfigurationItemsInner.md) | Individual port instances | [optional] 

## Example

```python
from tmi_client.models.port_configuration import PortConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortConfiguration from a JSON string
port_configuration_instance = PortConfiguration.from_json(json)
# print the JSON string representation of the object
print(PortConfiguration.to_json())

# convert the object into a dict
port_configuration_dict = port_configuration_instance.to_dict()
# create an instance of PortConfiguration from a dict
port_configuration_from_dict = PortConfiguration.from_dict(port_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


