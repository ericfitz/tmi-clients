# RollbackResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**RestoredEntity** | Pointer to **map[string]interface{}** | The entity restored to its previous state | [optional] 
**AuditEntry** | [**AuditEntry**](AuditEntry.md) | The new audit entry recording the rollback | 

## Methods

### NewRollbackResponse

`func NewRollbackResponse(auditEntry AuditEntry, ) *RollbackResponse`

NewRollbackResponse instantiates a new RollbackResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRollbackResponseWithDefaults

`func NewRollbackResponseWithDefaults() *RollbackResponse`

NewRollbackResponseWithDefaults instantiates a new RollbackResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetRestoredEntity

`func (o *RollbackResponse) GetRestoredEntity() map[string]interface{}`

GetRestoredEntity returns the RestoredEntity field if non-nil, zero value otherwise.

### GetRestoredEntityOk

`func (o *RollbackResponse) GetRestoredEntityOk() (*map[string]interface{}, bool)`

GetRestoredEntityOk returns a tuple with the RestoredEntity field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRestoredEntity

`func (o *RollbackResponse) SetRestoredEntity(v map[string]interface{})`

SetRestoredEntity sets RestoredEntity field to given value.

### HasRestoredEntity

`func (o *RollbackResponse) HasRestoredEntity() bool`

HasRestoredEntity returns a boolean if a field has been set.

### GetAuditEntry

`func (o *RollbackResponse) GetAuditEntry() AuditEntry`

GetAuditEntry returns the AuditEntry field if non-nil, zero value otherwise.

### GetAuditEntryOk

`func (o *RollbackResponse) GetAuditEntryOk() (*AuditEntry, bool)`

GetAuditEntryOk returns a tuple with the AuditEntry field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuditEntry

`func (o *RollbackResponse) SetAuditEntry(v AuditEntry)`

SetAuditEntry sets AuditEntry field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


