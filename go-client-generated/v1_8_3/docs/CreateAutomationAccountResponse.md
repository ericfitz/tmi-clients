# CreateAutomationAccountResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**User** | [**AdminUser**](AdminUser.md) |  | 
**ClientCredential** | [**ClientCredentialResponse**](ClientCredentialResponse.md) |  | 

## Methods

### NewCreateAutomationAccountResponse

`func NewCreateAutomationAccountResponse(user AdminUser, clientCredential ClientCredentialResponse, ) *CreateAutomationAccountResponse`

NewCreateAutomationAccountResponse instantiates a new CreateAutomationAccountResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAutomationAccountResponseWithDefaults

`func NewCreateAutomationAccountResponseWithDefaults() *CreateAutomationAccountResponse`

NewCreateAutomationAccountResponseWithDefaults instantiates a new CreateAutomationAccountResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetUser

`func (o *CreateAutomationAccountResponse) GetUser() AdminUser`

GetUser returns the User field if non-nil, zero value otherwise.

### GetUserOk

`func (o *CreateAutomationAccountResponse) GetUserOk() (*AdminUser, bool)`

GetUserOk returns a tuple with the User field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUser

`func (o *CreateAutomationAccountResponse) SetUser(v AdminUser)`

SetUser sets User field to given value.


### GetClientCredential

`func (o *CreateAutomationAccountResponse) GetClientCredential() ClientCredentialResponse`

GetClientCredential returns the ClientCredential field if non-nil, zero value otherwise.

### GetClientCredentialOk

`func (o *CreateAutomationAccountResponse) GetClientCredentialOk() (*ClientCredentialResponse, bool)`

GetClientCredentialOk returns a tuple with the ClientCredential field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientCredential

`func (o *CreateAutomationAccountResponse) SetClientCredential(v ClientCredentialResponse)`

SetClientCredential sets ClientCredential field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


