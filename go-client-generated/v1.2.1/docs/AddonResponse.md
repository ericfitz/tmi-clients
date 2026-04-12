# AddonResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Add-on identifier | 
**CreatedAt** | **time.Time** | Creation timestamp | 
**Name** | **string** | Display name | 
**WebhookId** | **string** | Associated webhook subscription ID | 
**Description** | Pointer to **string** | Add-on description | [optional] 
**Icon** | Pointer to **string** | Icon identifier | [optional] 
**Objects** | Pointer to **[]string** | Supported TMI object types | [optional] 
**ThreatModelId** | Pointer to **string** | Threat model scope (if scoped) | [optional] 

## Methods

### NewAddonResponse

`func NewAddonResponse(id string, createdAt time.Time, name string, webhookId string, ) *AddonResponse`

NewAddonResponse instantiates a new AddonResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddonResponseWithDefaults

`func NewAddonResponseWithDefaults() *AddonResponse`

NewAddonResponseWithDefaults instantiates a new AddonResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AddonResponse) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AddonResponse) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AddonResponse) SetId(v string)`

SetId sets Id field to given value.


### GetCreatedAt

`func (o *AddonResponse) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AddonResponse) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AddonResponse) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.


### GetName

`func (o *AddonResponse) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *AddonResponse) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *AddonResponse) SetName(v string)`

SetName sets Name field to given value.


### GetWebhookId

`func (o *AddonResponse) GetWebhookId() string`

GetWebhookId returns the WebhookId field if non-nil, zero value otherwise.

### GetWebhookIdOk

`func (o *AddonResponse) GetWebhookIdOk() (*string, bool)`

GetWebhookIdOk returns a tuple with the WebhookId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWebhookId

`func (o *AddonResponse) SetWebhookId(v string)`

SetWebhookId sets WebhookId field to given value.


### GetDescription

`func (o *AddonResponse) GetDescription() string`

GetDescription returns the Description field if non-nil, zero value otherwise.

### GetDescriptionOk

`func (o *AddonResponse) GetDescriptionOk() (*string, bool)`

GetDescriptionOk returns a tuple with the Description field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDescription

`func (o *AddonResponse) SetDescription(v string)`

SetDescription sets Description field to given value.

### HasDescription

`func (o *AddonResponse) HasDescription() bool`

HasDescription returns a boolean if a field has been set.

### GetIcon

`func (o *AddonResponse) GetIcon() string`

GetIcon returns the Icon field if non-nil, zero value otherwise.

### GetIconOk

`func (o *AddonResponse) GetIconOk() (*string, bool)`

GetIconOk returns a tuple with the Icon field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIcon

`func (o *AddonResponse) SetIcon(v string)`

SetIcon sets Icon field to given value.

### HasIcon

`func (o *AddonResponse) HasIcon() bool`

HasIcon returns a boolean if a field has been set.

### GetObjects

`func (o *AddonResponse) GetObjects() []string`

GetObjects returns the Objects field if non-nil, zero value otherwise.

### GetObjectsOk

`func (o *AddonResponse) GetObjectsOk() (*[]string, bool)`

GetObjectsOk returns a tuple with the Objects field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjects

`func (o *AddonResponse) SetObjects(v []string)`

SetObjects sets Objects field to given value.

### HasObjects

`func (o *AddonResponse) HasObjects() bool`

HasObjects returns a boolean if a field has been set.

### GetThreatModelId

`func (o *AddonResponse) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *AddonResponse) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *AddonResponse) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.

### HasThreatModelId

`func (o *AddonResponse) HasThreatModelId() bool`

HasThreatModelId returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


