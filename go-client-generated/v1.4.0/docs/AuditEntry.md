# AuditEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Unique identifier for the audit entry | 
**ThreatModelId** | **string** | ID of the threat model this audit entry belongs to | 
**ObjectType** | **string** | Type of the entity that was mutated | 
**ObjectId** | **string** | ID of the entity that was mutated | 
**Version** | Pointer to **NullableInt32** | Version number. Null if the version snapshot has been pruned and rollback is no longer available. | [optional] 
**ChangeType** | **string** | Type of mutation | 
**Actor** | [**AuditActor**](AuditActor.md) |  | 
**ChangeSummary** | Pointer to **NullableString** | Human-readable summary of what changed | [optional] 
**CreatedAt** | **time.Time** | When the mutation occurred | 

## Methods

### NewAuditEntry

`func NewAuditEntry(id string, threatModelId string, objectType string, objectId string, changeType string, actor AuditActor, createdAt time.Time, ) *AuditEntry`

NewAuditEntry instantiates a new AuditEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAuditEntryWithDefaults

`func NewAuditEntryWithDefaults() *AuditEntry`

NewAuditEntryWithDefaults instantiates a new AuditEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AuditEntry) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AuditEntry) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AuditEntry) SetId(v string)`

SetId sets Id field to given value.


### GetThreatModelId

`func (o *AuditEntry) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *AuditEntry) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *AuditEntry) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetObjectType

`func (o *AuditEntry) GetObjectType() string`

GetObjectType returns the ObjectType field if non-nil, zero value otherwise.

### GetObjectTypeOk

`func (o *AuditEntry) GetObjectTypeOk() (*string, bool)`

GetObjectTypeOk returns a tuple with the ObjectType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectType

`func (o *AuditEntry) SetObjectType(v string)`

SetObjectType sets ObjectType field to given value.


### GetObjectId

`func (o *AuditEntry) GetObjectId() string`

GetObjectId returns the ObjectId field if non-nil, zero value otherwise.

### GetObjectIdOk

`func (o *AuditEntry) GetObjectIdOk() (*string, bool)`

GetObjectIdOk returns a tuple with the ObjectId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetObjectId

`func (o *AuditEntry) SetObjectId(v string)`

SetObjectId sets ObjectId field to given value.


### GetVersion

`func (o *AuditEntry) GetVersion() int32`

GetVersion returns the Version field if non-nil, zero value otherwise.

### GetVersionOk

`func (o *AuditEntry) GetVersionOk() (*int32, bool)`

GetVersionOk returns a tuple with the Version field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVersion

`func (o *AuditEntry) SetVersion(v int32)`

SetVersion sets Version field to given value.

### HasVersion

`func (o *AuditEntry) HasVersion() bool`

HasVersion returns a boolean if a field has been set.

### SetVersionNil

`func (o *AuditEntry) SetVersionNil(b bool)`

 SetVersionNil sets the value for Version to be an explicit nil

### UnsetVersion
`func (o *AuditEntry) UnsetVersion()`

UnsetVersion ensures that no value is present for Version, not even an explicit nil
### GetChangeType

`func (o *AuditEntry) GetChangeType() string`

GetChangeType returns the ChangeType field if non-nil, zero value otherwise.

### GetChangeTypeOk

`func (o *AuditEntry) GetChangeTypeOk() (*string, bool)`

GetChangeTypeOk returns a tuple with the ChangeType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeType

`func (o *AuditEntry) SetChangeType(v string)`

SetChangeType sets ChangeType field to given value.


### GetActor

`func (o *AuditEntry) GetActor() AuditActor`

GetActor returns the Actor field if non-nil, zero value otherwise.

### GetActorOk

`func (o *AuditEntry) GetActorOk() (*AuditActor, bool)`

GetActorOk returns a tuple with the Actor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActor

`func (o *AuditEntry) SetActor(v AuditActor)`

SetActor sets Actor field to given value.


### GetChangeSummary

`func (o *AuditEntry) GetChangeSummary() string`

GetChangeSummary returns the ChangeSummary field if non-nil, zero value otherwise.

### GetChangeSummaryOk

`func (o *AuditEntry) GetChangeSummaryOk() (*string, bool)`

GetChangeSummaryOk returns a tuple with the ChangeSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeSummary

`func (o *AuditEntry) SetChangeSummary(v string)`

SetChangeSummary sets ChangeSummary field to given value.

### HasChangeSummary

`func (o *AuditEntry) HasChangeSummary() bool`

HasChangeSummary returns a boolean if a field has been set.

### SetChangeSummaryNil

`func (o *AuditEntry) SetChangeSummaryNil(b bool)`

 SetChangeSummaryNil sets the value for ChangeSummary to be an explicit nil

### UnsetChangeSummary
`func (o *AuditEntry) UnsetChangeSummary()`

UnsetChangeSummary ensures that no value is present for ChangeSummary, not even an explicit nil
### GetCreatedAt

`func (o *AuditEntry) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *AuditEntry) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *AuditEntry) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


