# TMListItem

Enhanced item for threat model list endpoints with key metadata and counts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the threat model (UUID) | [readonly] 
**name** | **str** | Name of the threat model | 
**description** | **str** | Description of the threat model | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC3339) | 
**modified_at** | **datetime** | Last modification timestamp (RFC3339) | 
**owner** | [**User**](User.md) | User who owns the threat model | 
**created_by** | [**User**](User.md) | User who created the threat model | 
**threat_model_framework** | **str** | The framework used for this threat model | 
**document_count** | **int** | Number of documents associated with this threat model | 
**repo_count** | **int** | Number of source code repository entries associated with this threat model | 
**diagram_count** | **int** | Number of diagrams associated with this threat model | 
**threat_count** | **int** | Number of threats defined in this threat model | 
**issue_uri** | **str** | URL to an issue in an issue tracking system | [optional] 
**asset_count** | **int** | Number of assets associated with this threat model | 
**note_count** | **int** | Number of notes associated with this threat model | 
**status** | **str** | Status of the threat model in the organization&#39;s threat modeling or SDLC process. Examples: \&quot;Not started\&quot;, \&quot;In progress\&quot;, \&quot;Review\&quot;, \&quot;Approved\&quot;, \&quot;Closed\&quot; | [optional] 
**status_updated** | **datetime** | Timestamp when the status field was last modified (RFC3339). Automatically updated by the server when status changes. | [optional] [readonly] 
**security_reviewer** | [**User**](User.md) | Security reviewer assigned to this threat model. The assigned security reviewer automatically has the owner role on this threat model. | [optional] 

## Example

```python
from tmi_client.models.tm_list_item import TMListItem

# TODO update the JSON string below
json = "{}"
# create an instance of TMListItem from a JSON string
tm_list_item_instance = TMListItem.from_json(json)
# print the JSON string representation of the object
print(TMListItem.to_json())

# convert the object into a dict
tm_list_item_dict = tm_list_item_instance.to_dict()
# create an instance of TMListItem from a dict
tm_list_item_from_dict = TMListItem.from_dict(tm_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


