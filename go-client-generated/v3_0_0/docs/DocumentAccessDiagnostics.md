# DocumentAccessDiagnostics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ReasonCode** | **string** |  | 
**ReasonDetail** | Pointer to **NullableString** | Raw error text; populated only when reason_code is &#39;other&#39; | [optional] 
**Remediations** | [**[]AccessRemediation**](AccessRemediation.md) |  | 

## Methods

### NewDocumentAccessDiagnostics

`func NewDocumentAccessDiagnostics(reasonCode string, remediations []AccessRemediation, ) *DocumentAccessDiagnostics`

NewDocumentAccessDiagnostics instantiates a new DocumentAccessDiagnostics object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDocumentAccessDiagnosticsWithDefaults

`func NewDocumentAccessDiagnosticsWithDefaults() *DocumentAccessDiagnostics`

NewDocumentAccessDiagnosticsWithDefaults instantiates a new DocumentAccessDiagnostics object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetReasonCode

`func (o *DocumentAccessDiagnostics) GetReasonCode() string`

GetReasonCode returns the ReasonCode field if non-nil, zero value otherwise.

### GetReasonCodeOk

`func (o *DocumentAccessDiagnostics) GetReasonCodeOk() (*string, bool)`

GetReasonCodeOk returns a tuple with the ReasonCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReasonCode

`func (o *DocumentAccessDiagnostics) SetReasonCode(v string)`

SetReasonCode sets ReasonCode field to given value.


### GetReasonDetail

`func (o *DocumentAccessDiagnostics) GetReasonDetail() string`

GetReasonDetail returns the ReasonDetail field if non-nil, zero value otherwise.

### GetReasonDetailOk

`func (o *DocumentAccessDiagnostics) GetReasonDetailOk() (*string, bool)`

GetReasonDetailOk returns a tuple with the ReasonDetail field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetReasonDetail

`func (o *DocumentAccessDiagnostics) SetReasonDetail(v string)`

SetReasonDetail sets ReasonDetail field to given value.

### HasReasonDetail

`func (o *DocumentAccessDiagnostics) HasReasonDetail() bool`

HasReasonDetail returns a boolean if a field has been set.

### SetReasonDetailNil

`func (o *DocumentAccessDiagnostics) SetReasonDetailNil(b bool)`

 SetReasonDetailNil sets the value for ReasonDetail to be an explicit nil

### UnsetReasonDetail
`func (o *DocumentAccessDiagnostics) UnsetReasonDetail()`

UnsetReasonDetail ensures that no value is present for ReasonDetail, not even an explicit nil
### GetRemediations

`func (o *DocumentAccessDiagnostics) GetRemediations() []AccessRemediation`

GetRemediations returns the Remediations field if non-nil, zero value otherwise.

### GetRemediationsOk

`func (o *DocumentAccessDiagnostics) GetRemediationsOk() (*[]AccessRemediation, bool)`

GetRemediationsOk returns a tuple with the Remediations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRemediations

`func (o *DocumentAccessDiagnostics) SetRemediations(v []AccessRemediation)`

SetRemediations sets Remediations field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


