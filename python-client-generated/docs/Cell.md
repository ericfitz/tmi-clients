# Cell

Base schema for all diagram cells (nodes and edges). Contains common properties shared by Node and Edge types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the cell (UUID) | 
**shape** | **str** | Shape type identifier that determines cell structure and behavior | 
**data** | [**CellData**](CellData.md) |  | [optional] 

## Example

```python
from tmi_client.models.cell import Cell

# TODO update the JSON string below
json = "{}"
# create an instance of Cell from a JSON string
cell_instance = Cell.from_json(json)
# print the JSON string representation of the object
print(Cell.to_json())

# convert the object into a dict
cell_dict = cell_instance.to_dict()
# create an instance of Cell from a dict
cell_from_dict = Cell.from_dict(cell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


