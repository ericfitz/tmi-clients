# CVSSScore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Vector** | **string** | CVSS vector string (e.g., CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) | 
**Score** | **float32** | CVSS score (0.0-10.0) | 

## Methods

### NewCVSSScore

`func NewCVSSScore(vector string, score float32, ) *CVSSScore`

NewCVSSScore instantiates a new CVSSScore object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCVSSScoreWithDefaults

`func NewCVSSScoreWithDefaults() *CVSSScore`

NewCVSSScoreWithDefaults instantiates a new CVSSScore object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVector

`func (o *CVSSScore) GetVector() string`

GetVector returns the Vector field if non-nil, zero value otherwise.

### GetVectorOk

`func (o *CVSSScore) GetVectorOk() (*string, bool)`

GetVectorOk returns a tuple with the Vector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVector

`func (o *CVSSScore) SetVector(v string)`

SetVector sets Vector field to given value.


### GetScore

`func (o *CVSSScore) GetScore() float32`

GetScore returns the Score field if non-nil, zero value otherwise.

### GetScoreOk

`func (o *CVSSScore) GetScoreOk() (*float32, bool)`

GetScoreOk returns a tuple with the Score field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScore

`func (o *CVSSScore) SetScore(v float32)`

SetScore sets Score field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


