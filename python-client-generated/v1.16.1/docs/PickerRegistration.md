# PickerRegistration

Client-provided registration for a picker-mediated provider attachment. Supplied when a user attaches a file to a threat model via a picker flow (Google Picker, Microsoft File Picker); the server stores these fields on the document and uses them to dispatch fetch and access-validation operations through the matching delegated source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Content OAuth provider that issued the picker grant | 
**file_id** | **str** | Provider-native file identifier from the picker (e.g. Google Drive file ID, or Microsoft \&quot;{driveId}:{itemId}\&quot;) | 
**mime_type** | **str** | MIME type returned by the picker | 

## Example

```python
from tmi_client.models.picker_registration import PickerRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of PickerRegistration from a JSON string
picker_registration_instance = PickerRegistration.from_json(json)
# print the JSON string representation of the object
print(PickerRegistration.to_json())

# convert the object into a dict
picker_registration_dict = picker_registration_instance.to_dict()
# create an instance of PickerRegistration from a dict
picker_registration_from_dict = PickerRegistration.from_dict(picker_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


