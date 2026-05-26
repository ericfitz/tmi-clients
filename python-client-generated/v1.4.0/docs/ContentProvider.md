# ContentProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Source identifier (matches ContentSource.Name()) | 
**name** | **str** | Display label for the provider | 
**kind** | **str** | delegated: per-user OAuth (client must call /me/content_tokens/{id}/authorize); service: operator-credentialed (no per-user link); direct: no auth (e.g., HTTP fetch) | 
**icon** | **str** | Font Awesome class string (matches OAuth IdP convention). Empty if no default and no override. | 
**picker_config** | **Dict[str, str]** | Browser-safe OAuth/picker bootstrap values for in-browser file pickers. Present only when the operator has configured a public Web OAuth client for this provider. All values are intended for browser use; never include client_secret or service-account material here. Per-provider keys are documented in the provider&#39;s section. | [optional] 

## Example

```python
from tmi_client.models.content_provider import ContentProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ContentProvider from a JSON string
content_provider_instance = ContentProvider.from_json(json)
# print the JSON string representation of the object
print(ContentProvider.to_json())

# convert the object into a dict
content_provider_dict = content_provider_instance.to_dict()
# create an instance of ContentProvider from a dict
content_provider_from_dict = ContentProvider.from_dict(content_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


