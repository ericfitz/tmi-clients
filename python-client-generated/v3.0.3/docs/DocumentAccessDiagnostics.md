# DocumentAccessDiagnostics

Per-viewer diagnostics explaining why a document is currently not accessible and what the viewer (or the document owner) can do to restore access. Emitted on Document responses whenever `access_status` is not `accessible`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason_code** | **str** |  | 
**reason_detail** | **str** | Raw error text; populated only when reason_code is &#39;other&#39; | [optional] 
**remediations** | [**List[AccessRemediation]**](AccessRemediation.md) |  | 

## Example

```python
from tmi_client.models.document_access_diagnostics import DocumentAccessDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentAccessDiagnostics from a JSON string
document_access_diagnostics_instance = DocumentAccessDiagnostics.from_json(json)
# print the JSON string representation of the object
print(DocumentAccessDiagnostics.to_json())

# convert the object into a dict
document_access_diagnostics_dict = document_access_diagnostics_instance.to_dict()
# create an instance of DocumentAccessDiagnostics from a dict
document_access_diagnostics_from_dict = DocumentAccessDiagnostics.from_dict(document_access_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


