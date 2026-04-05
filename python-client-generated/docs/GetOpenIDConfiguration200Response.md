# GetOpenIDConfiguration200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | 
**authorization_endpoint** | **str** |  | 
**token_endpoint** | **str** |  | 
**userinfo_endpoint** | **str** |  | [optional] 
**jwks_uri** | **str** |  | 
**response_types_supported** | **List[str]** |  | 
**subject_types_supported** | **List[str]** |  | 
**id_token_signing_alg_values_supported** | **List[str]** |  | 
**scopes_supported** | **List[str]** |  | [optional] 
**claims_supported** | **List[str]** |  | [optional] 
**introspection_endpoint** | **str** |  | [optional] 

## Example

```python
from tmi_client.models.get_open_id_configuration200_response import GetOpenIDConfiguration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOpenIDConfiguration200Response from a JSON string
get_open_id_configuration200_response_instance = GetOpenIDConfiguration200Response.from_json(json)
# print the JSON string representation of the object
print(GetOpenIDConfiguration200Response.to_json())

# convert the object into a dict
get_open_id_configuration200_response_dict = get_open_id_configuration200_response_instance.to_dict()
# create an instance of GetOpenIDConfiguration200Response from a dict
get_open_id_configuration200_response_from_dict = GetOpenIDConfiguration200Response.from_dict(get_open_id_configuration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


