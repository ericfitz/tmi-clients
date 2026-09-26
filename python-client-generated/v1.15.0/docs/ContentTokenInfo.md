# ContentTokenInfo

Information about a linked delegated content provider token. Does not expose secret token material.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Content OAuth provider id (e.g., &#39;confluence&#39;). | 
**provider_account_id** | **str** | External account identifier reported by the provider. May be empty if the provider has no stable id. | [optional] 
**provider_account_label** | **str** | Human-readable account label (email or username) for display. | [optional] 
**scopes** | **List[str]** | OAuth scopes granted to the stored token. | 
**status** | **str** | Current health of the stored token. &#39;failed_refresh&#39; indicates the most recent refresh attempt failed and the user must re-link. | 
**expires_at** | **datetime** | Access-token expiry reported by the provider (ISO 8601). | [optional] 
**last_refresh_at** | **datetime** | Timestamp of the most recent successful refresh (ISO 8601). | [optional] 
**created_at** | **datetime** | Creation timestamp for this linked token (ISO 8601). | 

## Example

```python
from tmi_client.models.content_token_info import ContentTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentTokenInfo from a JSON string
content_token_info_instance = ContentTokenInfo.from_json(json)
# print the JSON string representation of the object
print(ContentTokenInfo.to_json())

# convert the object into a dict
content_token_info_dict = content_token_info_instance.to_dict()
# create an instance of ContentTokenInfo from a dict
content_token_info_from_dict = ContentTokenInfo.from_dict(content_token_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


