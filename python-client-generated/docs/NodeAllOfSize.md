# NodeAllOfSize

Node size in X6 nested format. Use either this with position object OR use flat x/y/width/height properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Width in pixels | 
**height** | **float** | Height in pixels | 

## Example

```python
from tmi_client.models.node_all_of_size import NodeAllOfSize

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAllOfSize from a JSON string
node_all_of_size_instance = NodeAllOfSize.from_json(json)
# print the JSON string representation of the object
print(NodeAllOfSize.to_json())

# convert the object into a dict
node_all_of_size_dict = node_all_of_size_instance.to_dict()
# create an instance of NodeAllOfSize from a dict
node_all_of_size_from_dict = NodeAllOfSize.from_dict(node_all_of_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


