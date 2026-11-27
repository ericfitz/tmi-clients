# ContentAuthorizationURL

OAuth authorization URL plus expiry of the associated server-side state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_url** | **str** | Provider authorization URL to which the client must navigate the user. | 
**expires_at** | **datetime** | Timestamp after which the associated server-side state nonce is no longer valid (ISO 8601). | 

## Example

```python
from tmi_client.models.content_authorization_url import ContentAuthorizationURL

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAuthorizationURL from a JSON string
content_authorization_url_instance = ContentAuthorizationURL.from_json(json)
# print the JSON string representation of the object
print(ContentAuthorizationURL.to_json())

# convert the object into a dict
content_authorization_url_dict = content_authorization_url_instance.to_dict()
# create an instance of ContentAuthorizationURL from a dict
content_authorization_url_from_dict = ContentAuthorizationURL.from_dict(content_authorization_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


