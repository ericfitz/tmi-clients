# MyIdentitiesResponsePrimary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** | Primary identity provider ID | 
**email** | **str** | Primary account email address | 
**name** | **str** | Primary account display name | [optional] 

## Example

```python
from tmi_client.models.my_identities_response_primary import MyIdentitiesResponsePrimary

# TODO update the JSON string below
json = "{}"
# create an instance of MyIdentitiesResponsePrimary from a JSON string
my_identities_response_primary_instance = MyIdentitiesResponsePrimary.from_json(json)
# print the JSON string representation of the object
print(MyIdentitiesResponsePrimary.to_json())

# convert the object into a dict
my_identities_response_primary_dict = my_identities_response_primary_instance.to_dict()
# create an instance of MyIdentitiesResponsePrimary from a dict
my_identities_response_primary_from_dict = MyIdentitiesResponsePrimary.from_dict(my_identities_response_primary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


