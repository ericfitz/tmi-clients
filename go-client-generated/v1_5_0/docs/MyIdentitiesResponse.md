# MyIdentitiesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Primary** | [**MyIdentitiesResponsePrimary**](MyIdentitiesResponsePrimary.md) |  | 
**Linked** | Pointer to [**[]LinkedIdentity**](LinkedIdentity.md) | Additional linked identities | [optional] 

## Methods

### NewMyIdentitiesResponse

`func NewMyIdentitiesResponse(primary MyIdentitiesResponsePrimary, ) *MyIdentitiesResponse`

NewMyIdentitiesResponse instantiates a new MyIdentitiesResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewMyIdentitiesResponseWithDefaults

`func NewMyIdentitiesResponseWithDefaults() *MyIdentitiesResponse`

NewMyIdentitiesResponseWithDefaults instantiates a new MyIdentitiesResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPrimary

`func (o *MyIdentitiesResponse) GetPrimary() MyIdentitiesResponsePrimary`

GetPrimary returns the Primary field if non-nil, zero value otherwise.

### GetPrimaryOk

`func (o *MyIdentitiesResponse) GetPrimaryOk() (*MyIdentitiesResponsePrimary, bool)`

GetPrimaryOk returns a tuple with the Primary field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPrimary

`func (o *MyIdentitiesResponse) SetPrimary(v MyIdentitiesResponsePrimary)`

SetPrimary sets Primary field to given value.


### GetLinked

`func (o *MyIdentitiesResponse) GetLinked() []LinkedIdentity`

GetLinked returns the Linked field if non-nil, zero value otherwise.

### GetLinkedOk

`func (o *MyIdentitiesResponse) GetLinkedOk() (*[]LinkedIdentity, bool)`

GetLinkedOk returns a tuple with the Linked field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLinked

`func (o *MyIdentitiesResponse) SetLinked(v []LinkedIdentity)`

SetLinked sets Linked field to given value.

### HasLinked

`func (o *MyIdentitiesResponse) HasLinked() bool`

HasLinked returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


