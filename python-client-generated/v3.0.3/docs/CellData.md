# CellData

Flexible data storage compatible with X6, with reserved metadata namespace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[Metadata]**](Metadata.md) | Reserved namespace for structured business metadata | [optional] 
**security_boundary** | **bool** | Indicates whether this cell represents a security boundary in the threat model | [optional] [default to False]
**data_assets** | **List[UUID]** | References to Asset IDs associated with this cell. Each UUID must reference an existing Asset in the same threat model. | [optional] 

## Example

```python
from tmi_client.models.cell_data import CellData

# TODO update the JSON string below
json = "{}"
# create an instance of CellData from a JSON string
cell_data_instance = CellData.from_json(json)
# print the JSON string representation of the object
print(CellData.to_json())

# convert the object into a dict
cell_data_dict = cell_data_instance.to_dict()
# create an instance of CellData from a dict
cell_data_from_dict = CellData.from_dict(cell_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


