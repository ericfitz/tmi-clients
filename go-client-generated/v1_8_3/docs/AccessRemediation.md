# AccessRemediation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Action** | **string** |  | 
**Params** | **map[string]interface{}** | Action-specific parameters. Examples: &#x60;service_account_email&#x60;, &#x60;provider_id&#x60;, &#x60;user_email&#x60; (for &#x60;share_with_service_account&#x60;); &#x60;drive_id&#x60;, &#x60;item_id&#x60;, &#x60;app_object_id&#x60;, &#x60;graph_call&#x60;, &#x60;graph_body&#x60; (for &#x60;share_with_application&#x60;). | 

## Methods

### NewAccessRemediation

`func NewAccessRemediation(action string, params map[string]interface{}, ) *AccessRemediation`

NewAccessRemediation instantiates a new AccessRemediation object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAccessRemediationWithDefaults

`func NewAccessRemediationWithDefaults() *AccessRemediation`

NewAccessRemediationWithDefaults instantiates a new AccessRemediation object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetAction

`func (o *AccessRemediation) GetAction() string`

GetAction returns the Action field if non-nil, zero value otherwise.

### GetActionOk

`func (o *AccessRemediation) GetActionOk() (*string, bool)`

GetActionOk returns a tuple with the Action field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAction

`func (o *AccessRemediation) SetAction(v string)`

SetAction sets Action field to given value.


### GetParams

`func (o *AccessRemediation) GetParams() map[string]interface{}`

GetParams returns the Params field if non-nil, zero value otherwise.

### GetParamsOk

`func (o *AccessRemediation) GetParamsOk() (*map[string]interface{}, bool)`

GetParamsOk returns a tuple with the Params field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParams

`func (o *AccessRemediation) SetParams(v map[string]interface{})`

SetParams sets Params field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


