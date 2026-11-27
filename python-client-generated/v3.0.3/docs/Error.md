# Error

Standard error response format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Machine-readable REST error code. One of: invalid_input (400, a body, field, header or query value fails validation); invalid_id (400, a path or query identifier is malformed); invalid_patch (400, a JSON Patch document is malformed or cannot be applied); unauthorized (401, missing, expired or invalid credentials); insufficient_user_authentication (401, step-up authentication required, RFC 9470); forbidden (403, authenticated but not permitted); not_found (404, resource does not exist or is hidden by authorization); method_not_allowed (405); not_acceptable (406); conflict (409, duplicate, in use, or wrong lifecycle state); gone (410, permanently removed); version_mismatch (409, If-Match does not match the current version); payload_too_large (413); unsupported_media_type (415); unprocessable_entity (422, well-formed request that cannot be processed in the current state); if_match_required (428, If-Match header missing); rate_limit_exceeded (429, transient limit, honor Retry-After); quota_exceeded (403 or 429, hard cap reached, retrying does not help); server_error (500); not_implemented (501); service_unavailable (503, a dependency is unavailable, retry later); feature_not_available (404) and content_token_provider_not_configured (422) are legacy domain codes kept at top level because clients branch on them; they are also present in details.code and will move to details.code only in a future breaking change. A domain-specific reason a client can act on is in details.code. | 
**error_description** | **str** | Human-readable error description | 
**error_uri** | **str** | URI to documentation about the error | [optional] 
**details** | [**ErrorDetails**](ErrorDetails.md) |  | [optional] 

## Example

```python
from tmi_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


