# CreateAddonRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Display name for the add-on | 
**WebhookId** | **string** | UUID of the associated webhook subscription | 
**Description** | Pointer to **string** | Description of what the add-on does | [optional] 
**Icon** | Pointer to **string** | Icon identifier (Material Symbols or FontAwesome format) | [optional] 
**Objects** | Pointer to **[]string** | TMI object types this add-on can operate on | [optional] 
**ThreatModelId** | Pointer to **string** | Optional: Scope add-on to specific threat model | [optional] 
**Parameters** | Pointer to [**[]AddonParameter**](AddonParameter.md) | Typed parameter declarations for client UI generation. Each parameter defines a name, type, and type-specific configuration that clients use to render appropriate input controls. | [optional] 

## Methods

### NewCreateAddonRequest

`func NewCreateAddonRequest(name string, webhookId string, ) *CreateAddonRequest`

NewCreateAddonRequest instantiates a new CreateAddonRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateAddonRequestWithDefaults

`func NewCreateAddonRequestWithDefaults() *CreateAddonRequest`

NewCreateAddonRequestWithDefaults instantiates a new CreateAddonRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *CreateAddonRequest) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *CreateAddonRequest) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *CreateAddonRequest) SetName(v string)`

SetName sets Name field to given value.


### GetWebhookId

`func (o *CreateAddonRequest) GetWebhookId() string`

GetWebhookId returns the WebhookId field if non-nil, zero value otherwise.

### GetWebhookIdOk

`func (o *CreateAddonRequest) GetWebhookIdOk() (*string, bool)`

GetWebhookIdOk returns a tuple with the WebhookId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhookId

`func (o *CreateAddonRequest) SetWebhookId(v string)`

SetWebhookId sets WebhookId field to given value.


### GetDescription

`func (o *CreateAddonRequest) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *CreateAddonRequest) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *CreateAddonRequest) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *CreateAddonRequest) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIcon

`func (o *CreateAddonRequest) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *CreateAddonRequest) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *CreateAddonRequest) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *CreateAddonRequest) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### GetObjects

`func (o *CreateAddonRequest) GetObjects() []string`

GetObjects returns the Objects field if non-nil, zero value otherwise.

### GetObjectsOk

`func (o *CreateAddonRequest) GetObjectsOk() (*[]string, bool)`

GetObjectsOk returns a tuple with the Objects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjects

`func (o *CreateAddonRequest) SetObjects(v []string)`

SetObjects sets Objects field to given value.

### HasObjects

`func (o *CreateAddonRequest) HasObjects() bool`

HasObjects returns a boolean if a field has been set.

### GetThreatModelId

`func (o *CreateAddonRequest) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *CreateAddonRequest) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *CreateAddonRequest) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *CreateAddonRequest) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.

### GetParameters

`func (o *CreateAddonRequest) GetParameters() []AddonParameter`

GetParameters returns the Parameters field if non-nil, zero value otherwise.

### GetParametersOk

`func (o *CreateAddonRequest) GetParametersOk() (*[]AddonParameter, bool)`

GetParametersOk returns a tuple with the Parameters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetParameters

`func (o *CreateAddonRequest) SetParameters(v []AddonParameter)`

SetParameters sets Parameters field to given value.

### HasParameters

`func (o *CreateAddonRequest) HasParameters() bool`

HasParameters returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


