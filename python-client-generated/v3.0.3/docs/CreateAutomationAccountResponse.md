# CreateAutomationAccountResponse

Response from creating an automation account. Contains the created user and a client credential with the plaintext secret (shown only once).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**AdminUser**](AdminUser.md) |  | 
**client_credential** | [**ClientCredentialResponse**](ClientCredentialResponse.md) |  | 

## Example

```python
from tmi_client.models.create_automation_account_response import CreateAutomationAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAutomationAccountResponse from a JSON string
create_automation_account_response_instance = CreateAutomationAccountResponse.from_json(json)
# print the JSON string representation of the object
print(CreateAutomationAccountResponse.to_json())

# convert the object into a dict
create_automation_account_response_dict = create_automation_account_response_instance.to_dict()
# create an instance of CreateAutomationAccountResponse from a dict
create_automation_account_response_from_dict = CreateAutomationAccountResponse.from_dict(create_automation_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


