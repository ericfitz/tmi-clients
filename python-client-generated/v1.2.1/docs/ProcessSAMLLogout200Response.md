# ProcessSAMLLogout200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from tmi_client.models.process_saml_logout200_response import ProcessSAMLLogout200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessSAMLLogout200Response from a JSON string
process_saml_logout200_response_instance = ProcessSAMLLogout200Response.from_json(json)
# print the JSON string representation of the object
print(ProcessSAMLLogout200Response.to_json())

# convert the object into a dict
process_saml_logout200_response_dict = process_saml_logout200_response_instance.to_dict()
# create an instance of ProcessSAMLLogout200Response from a dict
process_saml_logout200_response_from_dict = ProcessSAMLLogout200Response.from_dict(process_saml_logout200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


