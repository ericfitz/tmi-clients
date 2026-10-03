# ColorPaletteEntry

A color entry in a diagram color palette with explicit position for ordering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **int** | Display order position (1-8) | 
**color** | **str** | Hex color value (#RGB or #RRGGBB), stored as lowercase #RRGGBB | 

## Example

```python
from tmi_client.models.color_palette_entry import ColorPaletteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ColorPaletteEntry from a JSON string
color_palette_entry_instance = ColorPaletteEntry.from_json(json)
# print the JSON string representation of the object
print(ColorPaletteEntry.to_json())

# convert the object into a dict
color_palette_entry_dict = color_palette_entry_instance.to_dict()
# create an instance of ColorPaletteEntry from a dict
color_palette_entry_from_dict = ColorPaletteEntry.from_dict(color_palette_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


