# Diagram

DEPRECATED: Empty wrapper schema for polymorphic diagram types. Use DfdDiagram directly instead. This schema is kept for backward compatibility but generates empty classes in client libraries.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from tmi_client.models.diagram import Diagram

# TODO update the JSON string below
json = "{}"
# create an instance of Diagram from a JSON string
diagram_instance = Diagram.from_json(json)
# print the JSON string representation of the object
print(Diagram.to_json())

# convert the object into a dict
diagram_dict = diagram_instance.to_dict()
# create an instance of Diagram from a dict
diagram_from_dict = Diagram.from_dict(diagram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


