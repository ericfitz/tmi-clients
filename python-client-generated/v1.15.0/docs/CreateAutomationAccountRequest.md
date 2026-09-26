# CreateAutomationAccountRequest

Request body for creating an automation (service) account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short identifier for the automation account (2-64 characters). Used to construct the account name, email, and provider ID. Must start with a letter and end with a letter or digit. | 
**email** | **str** | Optional custom email address. If not provided, defaults to tmi-automation-{normalized_name}@tmi.local. | [optional] 
**direct_write** | **bool** | Opt in to direct writes for the initial client credential: tokens from it may modify threat-model sub-resources, authorized by the automation user&#39;s roles. Omitting the field is the same as false. | [optional] [default to False]
**addon_id** | **UUID** | Optional addon to link this credential to (only valid with direct_write&#x3D;true; 400 otherwise, or if the addon does not exist). Events caused by writes made with tokens from this credential are not delivered to the linked addon&#39;s own webhook subscription, matching the suppression applied to delegation-token write-backs. Not a foreign key: deleting the addon leaves the credential intact and simply stops the suppression. | [optional] 

## Example

```python
from tmi_client.models.create_automation_account_request import CreateAutomationAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomationAccountRequest from a JSON string
create_automation_account_request_instance = CreateAutomationAccountRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAutomationAccountRequest.to_json())

# convert the object into a dict
create_automation_account_request_dict = create_automation_account_request_instance.to_dict()
# create an instance of CreateAutomationAccountRequest from a dict
create_automation_account_request_from_dict = CreateAutomationAccountRequest.from_dict(create_automation_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


