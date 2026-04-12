# SSVCScore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Vector** | **string** | SSVC vector string following CERT/CC convention (e.g., SSVCv2/E:A/U:S/T:T/P:S/2026-04-08/) | 
**Decision** | **string** | SSVC decision outcome | 
**Methodology** | **string** | The SSVC stakeholder perspective used for assessment | 

## Methods

### NewSSVCScore

`func NewSSVCScore(vector string, decision string, methodology string, ) *SSVCScore`

NewSSVCScore instantiates a new SSVCScore object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSSVCScoreWithDefaults

`func NewSSVCScoreWithDefaults() *SSVCScore`

NewSSVCScoreWithDefaults instantiates a new SSVCScore object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetVector

`func (o *SSVCScore) GetVector() string`

GetVector returns the Vector field if non-nil, zero value otherwise.

### GetVectorOk

`func (o *SSVCScore) GetVectorOk() (*string, bool)`

GetVectorOk returns a tuple with the Vector field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVector

`func (o *SSVCScore) SetVector(v string)`

SetVector sets Vector field to given value.


### GetDecision

`func (o *SSVCScore) GetDecision() string`

GetDecision returns the Decision field if non-nil, zero value otherwise.

### GetDecisionOk

`func (o *SSVCScore) GetDecisionOk() (*string, bool)`

GetDecisionOk returns a tuple with the Decision field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDecision

`func (o *SSVCScore) SetDecision(v string)`

SetDecision sets Decision field to given value.


### GetMethodology

`func (o *SSVCScore) GetMethodology() string`

GetMethodology returns the Methodology field if non-nil, zero value otherwise.

### GetMethodologyOk

`func (o *SSVCScore) GetMethodologyOk() (*string, bool)`

GetMethodologyOk returns a tuple with the Methodology field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethodology

`func (o *SSVCScore) SetMethodology(v string)`

SetMethodology sets Methodology field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


