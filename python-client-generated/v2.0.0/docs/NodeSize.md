# NodeSize

Node size in X6 nested format. Use either this with position object OR use flat x/y/width/height properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Width in pixels | 
**height** | **float** | Height in pixels | 

## Example

```python
from tmi_client.models.node_size import NodeSize

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSize from a JSON string
node_size_instance = NodeSize.from_json(json)
# print the JSON string representation of the object
print(NodeSize.to_json())

# convert the object into a dict
node_size_dict = node_size_instance.to_dict()
# create an instance of NodeSize from a dict
node_size_from_dict = NodeSize.from_dict(node_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


