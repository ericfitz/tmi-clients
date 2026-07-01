# NodeAllOfPosition

Node position in X6 nested format. Use either this with size object OR use flat x/y/width/height properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** | X coordinate | 
**y** | **float** | Y coordinate | 

## Example

```python
from tmi_client.models.node_all_of_position import NodeAllOfPosition

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAllOfPosition from a JSON string
node_all_of_position_instance = NodeAllOfPosition.from_json(json)
# print the JSON string representation of the object
print(NodeAllOfPosition.to_json())

# convert the object into a dict
node_all_of_position_dict = node_all_of_position_instance.to_dict()
# create an instance of NodeAllOfPosition from a dict
node_all_of_position_from_dict = NodeAllOfPosition.from_dict(node_all_of_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


