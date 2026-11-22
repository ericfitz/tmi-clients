# MicrosoftPickerGrantResponse

Response body for the Microsoft picker-grant endpoint. Returns the Graph permission id created by the grant call (informational; not needed for subsequent fetches).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_id** | **str** | Microsoft Graph permission id created by the grant call. | 
**drive_id** | **str** | OneDrive or SharePoint drive identifier of the granted file. | 
**item_id** | **str** | Drive item identifier of the granted file. | 

## Example

```python
from tmi_client.models.microsoft_picker_grant_response import MicrosoftPickerGrantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftPickerGrantResponse from a JSON string
microsoft_picker_grant_response_instance = MicrosoftPickerGrantResponse.from_json(json)
# print the JSON string representation of the object
print(MicrosoftPickerGrantResponse.to_json())

# convert the object into a dict
microsoft_picker_grant_response_dict = microsoft_picker_grant_response_instance.to_dict()
# create an instance of MicrosoftPickerGrantResponse from a dict
microsoft_picker_grant_response_from_dict = MicrosoftPickerGrantResponse.from_dict(microsoft_picker_grant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


