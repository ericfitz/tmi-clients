# AuditActor

Denormalized user information stored with audit entries. Persists after user deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email at the time of the action | 
**provider** | **str** | Identity provider (e.g., google, github, tmi) | 
**provider_id** | **str** | Provider-specific user identifier | 
**display_name** | **str** | User display name at the time of the action | 

## Example

```python
from tmi_client.models.audit_actor import AuditActor

# TODO update the JSON string below
json = "{}"
# create an instance of AuditActor from a JSON string
audit_actor_instance = AuditActor.from_json(json)
# print the JSON string representation of the object
print(AuditActor.to_json())

# convert the object into a dict
audit_actor_dict = audit_actor_instance.to_dict()
# create an instance of AuditActor from a dict
audit_actor_from_dict = AuditActor.from_dict(audit_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


