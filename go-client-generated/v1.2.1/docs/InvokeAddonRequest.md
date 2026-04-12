# InvokeAddonRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ThreatModelId** | **string** | Threat model context for invocation | 
**ObjectType** | Pointer to **string** | Optional: Specific object type to operate on | [optional] 
**ObjectId** | Pointer to **string** | Optional: Specific object ID to operate on | [optional] 
**Payload** | Pointer to **map[string]interface{}** | User-provided data for the add-on (max 1KB JSON-serialized) | [optional] 

## Methods

### NewInvokeAddonRequest

`func NewInvokeAddonRequest(threatModelId string, ) *InvokeAddonRequest`

NewInvokeAddonRequest instantiates a new InvokeAddonRequest object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInvokeAddonRequestWithDefaults

`func NewInvokeAddonRequestWithDefaults() *InvokeAddonRequest`

NewInvokeAddonRequestWithDefaults instantiates a new InvokeAddonRequest object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetThreatModelId

`func (o *InvokeAddonRequest) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *InvokeAddonRequest) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *InvokeAddonRequest) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetObjectType

`func (o *InvokeAddonRequest) GetObjectType() string`

GetObjectType returns the ObjectType field if non-nil, zero value otherwise.

### GetObjectTypeOk

`func (o *InvokeAddonRequest) GetObjectTypeOk() (*string, bool)`

GetObjectTypeOk returns a tuple with the ObjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectType

`func (o *InvokeAddonRequest) SetObjectType(v string)`

SetObjectType sets ObjectType field to given value.

### HasObjectType

`func (o *InvokeAddonRequest) HasObjectType() bool`

HasObjectType returns a boolean if a field has been set.

### GetObjectId

`func (o *InvokeAddonRequest) GetObjectId() string`

GetObjectId returns the ObjectId field if non-nil, zero value otherwise.

### GetObjectIdOk

`func (o *InvokeAddonRequest) GetObjectIdOk() (*string, bool)`

GetObjectIdOk returns a tuple with the ObjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectId

`func (o *InvokeAddonRequest) SetObjectId(v string)`

SetObjectId sets ObjectId field to given value.

### HasObjectId

`func (o *InvokeAddonRequest) HasObjectId() bool`

HasObjectId returns a boolean if a field has been set.

### GetPayload

`func (o *InvokeAddonRequest) GetPayload() map[string]interface{}`

GetPayload returns the Payload field if non-nil, zero value otherwise.

### GetPayloadOk

`func (o *InvokeAddonRequest) GetPayloadOk() (*map[string]interface{}, bool)`

GetPayloadOk returns a tuple with the Payload field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPayload

`func (o *InvokeAddonRequest) SetPayload(v map[string]interface{})`

SetPayload sets Payload field to given value.

### HasPayload

`func (o *InvokeAddonRequest) HasPayload() bool`

HasPayload returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


