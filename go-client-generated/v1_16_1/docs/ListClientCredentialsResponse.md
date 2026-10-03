# ListClientCredentialsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Credentials** | [**[]ClientCredentialInfo**](ClientCredentialInfo.md) |  | 
**Total** | **int32** | Total number of credentials matching criteria | 
**Limit** | **int32** | Pagination limit | 
**Offset** | **int32** | Pagination offset | 

## Methods

### NewListClientCredentialsResponse

`func NewListClientCredentialsResponse(credentials []ClientCredentialInfo, total int32, limit int32, offset int32, ) *ListClientCredentialsResponse`

NewListClientCredentialsResponse instantiates a new ListClientCredentialsResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewListClientCredentialsResponseWithDefaults

`func NewListClientCredentialsResponseWithDefaults() *ListClientCredentialsResponse`

NewListClientCredentialsResponseWithDefaults instantiates a new ListClientCredentialsResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCredentials

`func (o *ListClientCredentialsResponse) GetCredentials() []ClientCredentialInfo`

GetCredentials returns the Credentials field if non-nil, zero value otherwise.

### GetCredentialsOk

`func (o *ListClientCredentialsResponse) GetCredentialsOk() (*[]ClientCredentialInfo, bool)`

GetCredentialsOk returns a tuple with the Credentials field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCredentials

`func (o *ListClientCredentialsResponse) SetCredentials(v []ClientCredentialInfo)`

SetCredentials sets Credentials field to given value.


### GetTotal

`func (o *ListClientCredentialsResponse) GetTotal() int32`

GetTotal returns the Total field if non-nil, zero value otherwise.

### GetTotalOk

`func (o *ListClientCredentialsResponse) GetTotalOk() (*int32, bool)`

GetTotalOk returns a tuple with the Total field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotal

`func (o *ListClientCredentialsResponse) SetTotal(v int32)`

SetTotal sets Total field to given value.


### GetLimit

`func (o *ListClientCredentialsResponse) GetLimit() int32`

GetLimit returns the Limit field if non-nil, zero value otherwise.

### GetLimitOk

`func (o *ListClientCredentialsResponse) GetLimitOk() (*int32, bool)`

GetLimitOk returns a tuple with the Limit field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLimit

`func (o *ListClientCredentialsResponse) SetLimit(v int32)`

SetLimit sets Limit field to given value.


### GetOffset

`func (o *ListClientCredentialsResponse) GetOffset() int32`

GetOffset returns the Offset field if non-nil, zero value otherwise.

### GetOffsetOk

`func (o *ListClientCredentialsResponse) GetOffsetOk() (*int32, bool)`

GetOffsetOk returns a tuple with the Offset field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOffset

`func (o *ListClientCredentialsResponse) SetOffset(v int32)`

SetOffset sets Offset field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


