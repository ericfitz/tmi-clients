# ContentFeedbackInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sentiment** | **string** |  | 
**TargetType** | **string** | Type of artifact the feedback targets | 
**TargetId** | **string** | ID of the targeted artifact (note/diagram/threat). For threat_classification, the threat ID. | 
**TargetField** | Pointer to **string** | Required iff target_type is &#39;threat_classification&#39;; identifies the field of the threat (e.g. &#39;cwe&#39;, &#39;severity&#39;) | [optional] 
**Verbatim** | Pointer to **string** |  | [optional] 
**FalsePositiveReason** | Pointer to **string** | Allowed only when sentiment&#x3D;&#39;down&#39; and target_type&#x3D;&#39;threat&#39; | [optional] 
**FalsePositiveSubreason** | Pointer to **string** | Allowed only when false_positive_reason has subreasons; must be a valid subreason for the chosen reason | [optional] 
**ClientId** | **string** |  | 
**ClientVersion** | Pointer to **string** |  | [optional] 
**Screenshot** | Pointer to **string** | Optional viewport screenshot captured by the client at submission time. Data URL form (e.g. &#x60;data:image/jpeg;base64,...&#x60;). Used as support context. | [optional] 

## Methods

### NewContentFeedbackInput

`func NewContentFeedbackInput(sentiment string, targetType string, targetId string, clientId string, ) *ContentFeedbackInput`

NewContentFeedbackInput instantiates a new ContentFeedbackInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentFeedbackInputWithDefaults

`func NewContentFeedbackInputWithDefaults() *ContentFeedbackInput`

NewContentFeedbackInputWithDefaults instantiates a new ContentFeedbackInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSentiment

`func (o *ContentFeedbackInput) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *ContentFeedbackInput) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *ContentFeedbackInput) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetTargetType

`func (o *ContentFeedbackInput) GetTargetType() string`

GetTargetType returns the TargetType field if non-nil, zero value otherwise.

### GetTargetTypeOk

`func (o *ContentFeedbackInput) GetTargetTypeOk() (*string, bool)`

GetTargetTypeOk returns a tuple with the TargetType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetType

`func (o *ContentFeedbackInput) SetTargetType(v string)`

SetTargetType sets TargetType field to given value.


### GetTargetId

`func (o *ContentFeedbackInput) GetTargetId() string`

GetTargetId returns the TargetId field if non-nil, zero value otherwise.

### GetTargetIdOk

`func (o *ContentFeedbackInput) GetTargetIdOk() (*string, bool)`

GetTargetIdOk returns a tuple with the TargetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetId

`func (o *ContentFeedbackInput) SetTargetId(v string)`

SetTargetId sets TargetId field to given value.


### GetTargetField

`func (o *ContentFeedbackInput) GetTargetField() string`

GetTargetField returns the TargetField field if non-nil, zero value otherwise.

### GetTargetFieldOk

`func (o *ContentFeedbackInput) GetTargetFieldOk() (*string, bool)`

GetTargetFieldOk returns a tuple with the TargetField field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetField

`func (o *ContentFeedbackInput) SetTargetField(v string)`

SetTargetField sets TargetField field to given value.

### HasTargetField

`func (o *ContentFeedbackInput) HasTargetField() bool`

HasTargetField returns a boolean if a field has been set.

### GetVerbatim

`func (o *ContentFeedbackInput) GetVerbatim() string`

GetVerbatim returns the Verbatim field if non-nil, zero value otherwise.

### GetVerbatimOk

`func (o *ContentFeedbackInput) GetVerbatimOk() (*string, bool)`

GetVerbatimOk returns a tuple with the Verbatim field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerbatim

`func (o *ContentFeedbackInput) SetVerbatim(v string)`

SetVerbatim sets Verbatim field to given value.

### HasVerbatim

`func (o *ContentFeedbackInput) HasVerbatim() bool`

HasVerbatim returns a boolean if a field has been set.

### GetFalsePositiveReason

`func (o *ContentFeedbackInput) GetFalsePositiveReason() string`

GetFalsePositiveReason returns the FalsePositiveReason field if non-nil, zero value otherwise.

### GetFalsePositiveReasonOk

`func (o *ContentFeedbackInput) GetFalsePositiveReasonOk() (*string, bool)`

GetFalsePositiveReasonOk returns a tuple with the FalsePositiveReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFalsePositiveReason

`func (o *ContentFeedbackInput) SetFalsePositiveReason(v string)`

SetFalsePositiveReason sets FalsePositiveReason field to given value.

### HasFalsePositiveReason

`func (o *ContentFeedbackInput) HasFalsePositiveReason() bool`

HasFalsePositiveReason returns a boolean if a field has been set.

### GetFalsePositiveSubreason

`func (o *ContentFeedbackInput) GetFalsePositiveSubreason() string`

GetFalsePositiveSubreason returns the FalsePositiveSubreason field if non-nil, zero value otherwise.

### GetFalsePositiveSubreasonOk

`func (o *ContentFeedbackInput) GetFalsePositiveSubreasonOk() (*string, bool)`

GetFalsePositiveSubreasonOk returns a tuple with the FalsePositiveSubreason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFalsePositiveSubreason

`func (o *ContentFeedbackInput) SetFalsePositiveSubreason(v string)`

SetFalsePositiveSubreason sets FalsePositiveSubreason field to given value.

### HasFalsePositiveSubreason

`func (o *ContentFeedbackInput) HasFalsePositiveSubreason() bool`

HasFalsePositiveSubreason returns a boolean if a field has been set.

### GetClientId

`func (o *ContentFeedbackInput) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *ContentFeedbackInput) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *ContentFeedbackInput) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetClientVersion

`func (o *ContentFeedbackInput) GetClientVersion() string`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *ContentFeedbackInput) GetClientVersionOk() (*string, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *ContentFeedbackInput) SetClientVersion(v string)`

SetClientVersion sets ClientVersion field to given value.

### HasClientVersion

`func (o *ContentFeedbackInput) HasClientVersion() bool`

HasClientVersion returns a boolean if a field has been set.

### GetScreenshot

`func (o *ContentFeedbackInput) GetScreenshot() string`

GetScreenshot returns the Screenshot field if non-nil, zero value otherwise.

### GetScreenshotOk

`func (o *ContentFeedbackInput) GetScreenshotOk() (*string, bool)`

GetScreenshotOk returns a tuple with the Screenshot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScreenshot

`func (o *ContentFeedbackInput) SetScreenshot(v string)`

SetScreenshot sets Screenshot field to given value.

### HasScreenshot

`func (o *ContentFeedbackInput) HasScreenshot() bool`

HasScreenshot returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


