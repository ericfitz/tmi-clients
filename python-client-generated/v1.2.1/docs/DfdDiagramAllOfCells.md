# DfdDiagramAllOfCells


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the cell (UUID) | 
**shape** | **str** | Edge type identifier | 
**data** | [**CellData**](CellData.md) |  | [optional] 
**position** | [**NodeAllOfPosition**](NodeAllOfPosition.md) |  | [optional] 
**size** | [**NodeAllOfSize**](NodeAllOfSize.md) |  | [optional] 
**angle** | **float** | Rotation angle in degrees | [optional] [default to 0]
**attrs** | [**EdgeAttrs**](EdgeAttrs.md) | Visual styling attributes for the edge | [optional] 
**ports** | [**PortConfiguration**](PortConfiguration.md) | Port configuration for connections | [optional] 
**parent** | **UUID** | ID of the parent cell for nested/grouped nodes (UUID) | [optional] 
**children** | **List[UUID]** | IDs of child cells contained within this node (UUIDs) | [optional] 
**x** | **float** | X coordinate (flat format). Use either this with y, width, height OR use position/size objects. | [optional] 
**y** | **float** | Y coordinate (flat format) | [optional] 
**width** | **float** | Width in pixels (flat format) | [optional] 
**height** | **float** | Height in pixels (flat format) | [optional] 
**source** | [**EdgeTerminal**](EdgeTerminal.md) | Source connection point | 
**target** | [**EdgeTerminal**](EdgeTerminal.md) | Target connection point | 
**labels** | [**List[EdgeLabel]**](EdgeLabel.md) | Text labels positioned along the edge | [optional] 
**vertices** | [**List[Point]**](Point.md) | Intermediate waypoints for edge routing | [optional] 
**router** | [**EdgeRouter**](EdgeRouter.md) | Edge routing algorithm configuration for path calculation | [optional] 
**connector** | [**EdgeConnector**](EdgeConnector.md) | Edge connector style configuration for visual appearance | [optional] 
**default_label** | [**EdgeLabel**](EdgeLabel.md) | Default label configuration applied to edges without explicit labels | [optional] 

## Example

```python
from tmi_client.models.dfd_diagram_all_of_cells import DfdDiagramAllOfCells

# TODO update the JSON string below
json = "{}"
# create an instance of DfdDiagramAllOfCells from a JSON string
dfd_diagram_all_of_cells_instance = DfdDiagramAllOfCells.from_json(json)
# print the JSON string representation of the object
print(DfdDiagramAllOfCells.to_json())

# convert the object into a dict
dfd_diagram_all_of_cells_dict = dfd_diagram_all_of_cells_instance.to_dict()
# create an instance of DfdDiagramAllOfCells from a dict
dfd_diagram_all_of_cells_from_dict = DfdDiagramAllOfCells.from_dict(dfd_diagram_all_of_cells_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


