# RequestDocumentAccess200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from tmi_client.models.request_document_access200_response import RequestDocumentAccess200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDocumentAccess200Response from a JSON string
request_document_access200_response_instance = RequestDocumentAccess200Response.from_json(json)
# print the JSON string representation of the object
print(RequestDocumentAccess200Response.to_json())

# convert the object into a dict
request_document_access200_response_dict = request_document_access200_response_instance.to_dict()
# create an instance of RequestDocumentAccess200Response from a dict
request_document_access200_response_from_dict = RequestDocumentAccess200Response.from_dict(request_document_access200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


