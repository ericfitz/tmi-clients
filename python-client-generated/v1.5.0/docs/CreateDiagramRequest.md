# CreateDiagramRequest

Request body for creating a new diagram - only includes client-provided fields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the diagram | 
**type** | **str** | Type of diagram with version | 

## Example

```python
from tmi_client.models.create_diagram_request import CreateDiagramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiagramRequest from a JSON string
create_diagram_request_instance = CreateDiagramRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDiagramRequest.to_json())

# convert the object into a dict
create_diagram_request_dict = create_diagram_request_instance.to_dict()
# create an instance of CreateDiagramRequest from a dict
create_diagram_request_from_dict = CreateDiagramRequest.from_dict(create_diagram_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


