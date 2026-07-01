# StepUpAuthenticate200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Result** | **string** |  | 
**RedirectUrl** | Pointer to **string** | Upstream IdP authorization URL (with fresh-prompt parameters appended) the client must top-level navigate to. Present only when result&#x3D;&#39;step_up_redirect&#39;. | [optional] 
**Provider** | Pointer to **string** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 
**AuthTime** | Pointer to **int64** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 
**Message** | Pointer to **string** | Present only when result&#x3D;&#39;step_up_weak_complete&#39;. | [optional] 

## Methods

### NewStepUpAuthenticate200Response

`func NewStepUpAuthenticate200Response(result string, ) *StepUpAuthenticate200Response`

NewStepUpAuthenticate200Response instantiates a new StepUpAuthenticate200Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewStepUpAuthenticate200ResponseWithDefaults

`func NewStepUpAuthenticate200ResponseWithDefaults() *StepUpAuthenticate200Response`

NewStepUpAuthenticate200ResponseWithDefaults instantiates a new StepUpAuthenticate200Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResult

`func (o *StepUpAuthenticate200Response) GetResult() string`

GetResult returns the Result field if non-nil, zero value otherwise.

### GetResultOk

`func (o *StepUpAuthenticate200Response) GetResultOk() (*string, bool)`

GetResultOk returns a tuple with the Result field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResult

`func (o *StepUpAuthenticate200Response) SetResult(v string)`

SetResult sets Result field to given value.


### GetRedirectUrl

`func (o *StepUpAuthenticate200Response) GetRedirectUrl() string`

GetRedirectUrl returns the RedirectUrl field if non-nil, zero value otherwise.

### GetRedirectUrlOk

`func (o *StepUpAuthenticate200Response) GetRedirectUrlOk() (*string, bool)`

GetRedirectUrlOk returns a tuple with the RedirectUrl field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRedirectUrl

`func (o *StepUpAuthenticate200Response) SetRedirectUrl(v string)`

SetRedirectUrl sets RedirectUrl field to given value.

### HasRedirectUrl

`func (o *StepUpAuthenticate200Response) HasRedirectUrl() bool`

HasRedirectUrl returns a boolean if a field has been set.

### GetProvider

`func (o *StepUpAuthenticate200Response) GetProvider() string`

GetProvider returns the Provider field if non-nil, zero value otherwise.

### GetProviderOk

`func (o *StepUpAuthenticate200Response) GetProviderOk() (*string, bool)`

GetProviderOk returns a tuple with the Provider field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetProvider

`func (o *StepUpAuthenticate200Response) SetProvider(v string)`

SetProvider sets Provider field to given value.

### HasProvider

`func (o *StepUpAuthenticate200Response) HasProvider() bool`

HasProvider returns a boolean if a field has been set.

### GetAuthTime

`func (o *StepUpAuthenticate200Response) GetAuthTime() int64`

GetAuthTime returns the AuthTime field if non-nil, zero value otherwise.

### GetAuthTimeOk

`func (o *StepUpAuthenticate200Response) GetAuthTimeOk() (*int64, bool)`

GetAuthTimeOk returns a tuple with the AuthTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAuthTime

`func (o *StepUpAuthenticate200Response) SetAuthTime(v int64)`

SetAuthTime sets AuthTime field to given value.

### HasAuthTime

`func (o *StepUpAuthenticate200Response) HasAuthTime() bool`

HasAuthTime returns a boolean if a field has been set.

### GetMessage

`func (o *StepUpAuthenticate200Response) GetMessage() string`

GetMessage returns the Message field if non-nil, zero value otherwise.

### GetMessageOk

`func (o *StepUpAuthenticate200Response) GetMessageOk() (*string, bool)`

GetMessageOk returns a tuple with the Message field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMessage

`func (o *StepUpAuthenticate200Response) SetMessage(v string)`

SetMessage sets Message field to given value.

### HasMessage

`func (o *StepUpAuthenticate200Response) HasMessage() bool`

HasMessage returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


