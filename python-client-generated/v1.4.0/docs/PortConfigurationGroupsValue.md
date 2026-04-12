# PortConfigurationGroupsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | Port position on the node | [optional] 
**attrs** | **object** | Visual attributes for port group rendering (e.g., circle styling) | [optional] 

## Example

```python
from tmi_client.models.port_configuration_groups_value import PortConfigurationGroupsValue

# TODO update the JSON string below
json = "{}"
# create an instance of PortConfigurationGroupsValue from a JSON string
port_configuration_groups_value_instance = PortConfigurationGroupsValue.from_json(json)
# print the JSON string representation of the object
print(PortConfigurationGroupsValue.to_json())

# convert the object into a dict
port_configuration_groups_value_dict = port_configuration_groups_value_instance.to_dict()
# create an instance of PortConfigurationGroupsValue from a dict
port_configuration_groups_value_from_dict = PortConfigurationGroupsValue.from_dict(port_configuration_groups_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


