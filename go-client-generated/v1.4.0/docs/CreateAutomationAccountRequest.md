# CreateAutomationAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Short identifier for the automation account (2-64 characters). Used to construct the account name, email, and provider ID. Must start with a letter and end with a letter or digit. | 
**Email** | Pointer to **string** | Optional custom email address. If not provided, defaults to tmi-automation-{normalized_name}@tmi.local. | [optional] 

## Methods

### NewCreateAutomationAccountRequest

`func NewCreateAutomationAccountRequest(name string, ) *CreateAutomationAccountRequest`

NewCreateAutomationAccountRequest instantiates a new CreateAutomationAccountRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAutomationAccountRequestWithDefaults

`func NewCreateAutomationAccountRequestWithDefaults() *CreateAutomationAccountRequest`

NewCreateAutomationAccountRequestWithDefaults instantiates a new CreateAutomationAccountRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateAutomationAccountRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAutomationAccountRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateAutomationAccountRequest) SetName(v string)`

SetName sets Name field to given value.


### GetEmail

`func (o *CreateAutomationAccountRequest) GetEmail() string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *CreateAutomationAccountRequest) GetEmailOk() (*string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *CreateAutomationAccountRequest) SetEmail(v string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *CreateAutomationAccountRequest) HasEmail() bool`

HasEmail returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


