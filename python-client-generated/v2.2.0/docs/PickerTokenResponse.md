# PickerTokenResponse

Response body for `POST /me/picker_tokens/{provider_id}`. Carries a short-lived access token and the public picker configuration values that the browser client needs to initialize the provider's picker widget.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Short-lived OAuth access token, scoped to the picker session. | 
**expires_at** | **datetime** | Token expiration timestamp (RFC3339). | 
**developer_key** | **str** | Google Picker developer key. Deprecated — prefer provider_config.developer_key. Populated only for provider_id&#x3D;google_workspace. | [optional] 
**app_id** | **str** | Google Cloud app id. Deprecated — prefer provider_config.app_id. Populated only for provider_id&#x3D;google_workspace. | [optional] 
**provider_config** | **Dict[str, str]** | Provider-specific public configuration values for picker initialization. Keys vary by provider — see provider documentation. For google_workspace: developer_key, app_id. For microsoft: client_id, tenant_id, picker_origin. | [optional] 

## Example

```python
from tmi_client.models.picker_token_response import PickerTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PickerTokenResponse from a JSON string
picker_token_response_instance = PickerTokenResponse.from_json(json)
# print the JSON string representation of the object
print(PickerTokenResponse.to_json())

# convert the object into a dict
picker_token_response_dict = picker_token_response_instance.to_dict()
# create an instance of PickerTokenResponse from a dict
picker_token_response_from_dict = PickerTokenResponse.from_dict(picker_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


