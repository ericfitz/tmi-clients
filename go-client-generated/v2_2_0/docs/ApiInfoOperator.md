# ApiInfoOperator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | **string** | Operator name from environment variables | 
**Contact** | **string** | Operator contact information from environment variables | 

## Methods

### NewApiInfoOperator

`func NewApiInfoOperator(name string, contact string, ) *ApiInfoOperator`

NewApiInfoOperator instantiates a new ApiInfoOperator object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewApiInfoOperatorWithDefaults

`func NewApiInfoOperatorWithDefaults() *ApiInfoOperator`

NewApiInfoOperatorWithDefaults instantiates a new ApiInfoOperator object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *ApiInfoOperator) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *ApiInfoOperator) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *ApiInfoOperator) SetName(v string)`

SetName sets Name field to given value.


### GetContact

`func (o *ApiInfoOperator) GetContact() string`

GetContact returns the Contact field if non-nil, zero value otherwise.

### GetContactOk

`func (o *ApiInfoOperator) GetContactOk() (*string, bool)`

GetContactOk returns a tuple with the Contact field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContact

`func (o *ApiInfoOperator) SetContact(v string)`

SetContact sets Contact field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


