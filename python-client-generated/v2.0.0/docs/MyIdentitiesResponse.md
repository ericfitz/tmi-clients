# MyIdentitiesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | [**MyIdentitiesResponsePrimary**](MyIdentitiesResponsePrimary.md) |  | 
**linked** | [**List[LinkedIdentity]**](LinkedIdentity.md) | Additional linked identities | [optional] 

## Example

```python
from tmi_client.models.my_identities_response import MyIdentitiesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MyIdentitiesResponse from a JSON string
my_identities_response_instance = MyIdentitiesResponse.from_json(json)
# print the JSON string representation of the object
print(MyIdentitiesResponse.to_json())

# convert the object into a dict
my_identities_response_dict = my_identities_response_instance.to_dict()
# create an instance of MyIdentitiesResponse from a dict
my_identities_response_from_dict = MyIdentitiesResponse.from_dict(my_identities_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


