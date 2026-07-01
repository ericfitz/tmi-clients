# SystemAuditEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | Entry identifier. | 
**Actor** | [**AuditActor**](AuditActor.md) |  | 
**HttpMethod** | **string** | HTTP method of the audited request. | 
**HttpPath** | **string** | Request path of the audited request. | 
**FieldPath** | **string** | Dotted path of the changed field. | 
**OldValueRedacted** | Pointer to **NullableString** | Previous value, redacted at write time. | [optional] 
**NewValueRedacted** | Pointer to **NullableString** | New value, redacted at write time. | [optional] 
**ChangeSummary** | Pointer to **NullableString** | Human-readable change summary. | [optional] 
**CreatedAt** | **time.Time** | When the audited write completed. | 

## Methods

### NewSystemAuditEntry

`func NewSystemAuditEntry(id string, actor AuditActor, httpMethod string, httpPath string, fieldPath string, createdAt time.Time, ) *SystemAuditEntry`

NewSystemAuditEntry instantiates a new SystemAuditEntry object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSystemAuditEntryWithDefaults

`func NewSystemAuditEntryWithDefaults() *SystemAuditEntry`

NewSystemAuditEntryWithDefaults instantiates a new SystemAuditEntry object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SystemAuditEntry) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SystemAuditEntry) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SystemAuditEntry) SetId(v string)`

SetId sets Id field to given value.


### GetActor

`func (o *SystemAuditEntry) GetActor() AuditActor`

GetActor returns the Actor field if non-nil, zero value otherwise.

### GetActorOk

`func (o *SystemAuditEntry) GetActorOk() (*AuditActor, bool)`

GetActorOk returns a tuple with the Actor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActor

`func (o *SystemAuditEntry) SetActor(v AuditActor)`

SetActor sets Actor field to given value.


### GetHttpMethod

`func (o *SystemAuditEntry) GetHttpMethod() string`

GetHttpMethod returns the HttpMethod field if non-nil, zero value otherwise.

### GetHttpMethodOk

`func (o *SystemAuditEntry) GetHttpMethodOk() (*string, bool)`

GetHttpMethodOk returns a tuple with the HttpMethod field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHttpMethod

`func (o *SystemAuditEntry) SetHttpMethod(v string)`

SetHttpMethod sets HttpMethod field to given value.


### GetHttpPath

`func (o *SystemAuditEntry) GetHttpPath() string`

GetHttpPath returns the HttpPath field if non-nil, zero value otherwise.

### GetHttpPathOk

`func (o *SystemAuditEntry) GetHttpPathOk() (*string, bool)`

GetHttpPathOk returns a tuple with the HttpPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHttpPath

`func (o *SystemAuditEntry) SetHttpPath(v string)`

SetHttpPath sets HttpPath field to given value.


### GetFieldPath

`func (o *SystemAuditEntry) GetFieldPath() string`

GetFieldPath returns the FieldPath field if non-nil, zero value otherwise.

### GetFieldPathOk

`func (o *SystemAuditEntry) GetFieldPathOk() (*string, bool)`

GetFieldPathOk returns a tuple with the FieldPath field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFieldPath

`func (o *SystemAuditEntry) SetFieldPath(v string)`

SetFieldPath sets FieldPath field to given value.


### GetOldValueRedacted

`func (o *SystemAuditEntry) GetOldValueRedacted() string`

GetOldValueRedacted returns the OldValueRedacted field if non-nil, zero value otherwise.

### GetOldValueRedactedOk

`func (o *SystemAuditEntry) GetOldValueRedactedOk() (*string, bool)`

GetOldValueRedactedOk returns a tuple with the OldValueRedacted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOldValueRedacted

`func (o *SystemAuditEntry) SetOldValueRedacted(v string)`

SetOldValueRedacted sets OldValueRedacted field to given value.

### HasOldValueRedacted

`func (o *SystemAuditEntry) HasOldValueRedacted() bool`

HasOldValueRedacted returns a boolean if a field has been set.

### SetOldValueRedactedNil

`func (o *SystemAuditEntry) SetOldValueRedactedNil(b bool)`

 SetOldValueRedactedNil sets the value for OldValueRedacted to be an explicit nil

### UnsetOldValueRedacted
`func (o *SystemAuditEntry) UnsetOldValueRedacted()`

UnsetOldValueRedacted ensures that no value is present for OldValueRedacted, not even an explicit nil
### GetNewValueRedacted

`func (o *SystemAuditEntry) GetNewValueRedacted() string`

GetNewValueRedacted returns the NewValueRedacted field if non-nil, zero value otherwise.

### GetNewValueRedactedOk

`func (o *SystemAuditEntry) GetNewValueRedactedOk() (*string, bool)`

GetNewValueRedactedOk returns a tuple with the NewValueRedacted field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNewValueRedacted

`func (o *SystemAuditEntry) SetNewValueRedacted(v string)`

SetNewValueRedacted sets NewValueRedacted field to given value.

### HasNewValueRedacted

`func (o *SystemAuditEntry) HasNewValueRedacted() bool`

HasNewValueRedacted returns a boolean if a field has been set.

### SetNewValueRedactedNil

`func (o *SystemAuditEntry) SetNewValueRedactedNil(b bool)`

 SetNewValueRedactedNil sets the value for NewValueRedacted to be an explicit nil

### UnsetNewValueRedacted
`func (o *SystemAuditEntry) UnsetNewValueRedacted()`

UnsetNewValueRedacted ensures that no value is present for NewValueRedacted, not even an explicit nil
### GetChangeSummary

`func (o *SystemAuditEntry) GetChangeSummary() string`

GetChangeSummary returns the ChangeSummary field if non-nil, zero value otherwise.

### GetChangeSummaryOk

`func (o *SystemAuditEntry) GetChangeSummaryOk() (*string, bool)`

GetChangeSummaryOk returns a tuple with the ChangeSummary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChangeSummary

`func (o *SystemAuditEntry) SetChangeSummary(v string)`

SetChangeSummary sets ChangeSummary field to given value.

### HasChangeSummary

`func (o *SystemAuditEntry) HasChangeSummary() bool`

HasChangeSummary returns a boolean if a field has been set.

### SetChangeSummaryNil

`func (o *SystemAuditEntry) SetChangeSummaryNil(b bool)`

 SetChangeSummaryNil sets the value for ChangeSummary to be an explicit nil

### UnsetChangeSummary
`func (o *SystemAuditEntry) UnsetChangeSummary()`

UnsetChangeSummary ensures that no value is present for ChangeSummary, not even an explicit nil
### GetCreatedAt

`func (o *SystemAuditEntry) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *SystemAuditEntry) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *SystemAuditEntry) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


