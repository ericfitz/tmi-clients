# MicrosoftPickerGrantRequest

Request body for the Microsoft picker-grant endpoint. Carries the drive id and item id of the picked file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_id** | **str** | OneDrive or SharePoint drive identifier returned by the Microsoft File Picker. | 
**item_id** | **str** | Drive item identifier returned by the Microsoft File Picker. | 

## Example

```python
from tmi_client.models.microsoft_picker_grant_request import MicrosoftPickerGrantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPickerGrantRequest from a JSON string
microsoft_picker_grant_request_instance = MicrosoftPickerGrantRequest.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPickerGrantRequest.to_json())

# convert the object into a dict
microsoft_picker_grant_request_dict = microsoft_picker_grant_request_instance.to_dict()
# create an instance of MicrosoftPickerGrantRequest from a dict
microsoft_picker_grant_request_from_dict = MicrosoftPickerGrantRequest.from_dict(microsoft_picker_grant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


