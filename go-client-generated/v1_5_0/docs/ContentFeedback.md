# ContentFeedback

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
**Id** | **string** |  | 
**ThreatModelId** | **string** |  | 
**CreatedBy** | **string** |  | 
**CreatedAt** | **time.Time** |  | 

## Methods

### NewContentFeedback

`func NewContentFeedback(sentiment string, targetType string, targetId string, clientId string, id string, threatModelId string, createdBy string, createdAt time.Time, ) *ContentFeedback`

NewContentFeedback instantiates a new ContentFeedback object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContentFeedbackWithDefaults

`func NewContentFeedbackWithDefaults() *ContentFeedback`

NewContentFeedbackWithDefaults instantiates a new ContentFeedback object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSentiment

`func (o *ContentFeedback) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *ContentFeedback) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *ContentFeedback) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetTargetType

`func (o *ContentFeedback) GetTargetType() string`

GetTargetType returns the TargetType field if non-nil, zero value otherwise.

### GetTargetTypeOk

`func (o *ContentFeedback) GetTargetTypeOk() (*string, bool)`

GetTargetTypeOk returns a tuple with the TargetType field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetType

`func (o *ContentFeedback) SetTargetType(v string)`

SetTargetType sets TargetType field to given value.


### GetTargetId

`func (o *ContentFeedback) GetTargetId() string`

GetTargetId returns the TargetId field if non-nil, zero value otherwise.

### GetTargetIdOk

`func (o *ContentFeedback) GetTargetIdOk() (*string, bool)`

GetTargetIdOk returns a tuple with the TargetId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetId

`func (o *ContentFeedback) SetTargetId(v string)`

SetTargetId sets TargetId field to given value.


### GetTargetField

`func (o *ContentFeedback) GetTargetField() string`

GetTargetField returns the TargetField field if non-nil, zero value otherwise.

### GetTargetFieldOk

`func (o *ContentFeedback) GetTargetFieldOk() (*string, bool)`

GetTargetFieldOk returns a tuple with the TargetField field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTargetField

`func (o *ContentFeedback) SetTargetField(v string)`

SetTargetField sets TargetField field to given value.

### HasTargetField

`func (o *ContentFeedback) HasTargetField() bool`

HasTargetField returns a boolean if a field has been set.

### GetVerbatim

`func (o *ContentFeedback) GetVerbatim() string`

GetVerbatim returns the Verbatim field if non-nil, zero value otherwise.

### GetVerbatimOk

`func (o *ContentFeedback) GetVerbatimOk() (*string, bool)`

GetVerbatimOk returns a tuple with the Verbatim field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerbatim

`func (o *ContentFeedback) SetVerbatim(v string)`

SetVerbatim sets Verbatim field to given value.

### HasVerbatim

`func (o *ContentFeedback) HasVerbatim() bool`

HasVerbatim returns a boolean if a field has been set.

### GetFalsePositiveReason

`func (o *ContentFeedback) GetFalsePositiveReason() string`

GetFalsePositiveReason returns the FalsePositiveReason field if non-nil, zero value otherwise.

### GetFalsePositiveReasonOk

`func (o *ContentFeedback) GetFalsePositiveReasonOk() (*string, bool)`

GetFalsePositiveReasonOk returns a tuple with the FalsePositiveReason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFalsePositiveReason

`func (o *ContentFeedback) SetFalsePositiveReason(v string)`

SetFalsePositiveReason sets FalsePositiveReason field to given value.

### HasFalsePositiveReason

`func (o *ContentFeedback) HasFalsePositiveReason() bool`

HasFalsePositiveReason returns a boolean if a field has been set.

### GetFalsePositiveSubreason

`func (o *ContentFeedback) GetFalsePositiveSubreason() string`

GetFalsePositiveSubreason returns the FalsePositiveSubreason field if non-nil, zero value otherwise.

### GetFalsePositiveSubreasonOk

`func (o *ContentFeedback) GetFalsePositiveSubreasonOk() (*string, bool)`

GetFalsePositiveSubreasonOk returns a tuple with the FalsePositiveSubreason field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFalsePositiveSubreason

`func (o *ContentFeedback) SetFalsePositiveSubreason(v string)`

SetFalsePositiveSubreason sets FalsePositiveSubreason field to given value.

### HasFalsePositiveSubreason

`func (o *ContentFeedback) HasFalsePositiveSubreason() bool`

HasFalsePositiveSubreason returns a boolean if a field has been set.

### GetClientId

`func (o *ContentFeedback) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *ContentFeedback) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *ContentFeedback) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetClientVersion

`func (o *ContentFeedback) GetClientVersion() string`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *ContentFeedback) GetClientVersionOk() (*string, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *ContentFeedback) SetClientVersion(v string)`

SetClientVersion sets ClientVersion field to given value.

### HasClientVersion

`func (o *ContentFeedback) HasClientVersion() bool`

HasClientVersion returns a boolean if a field has been set.

### GetScreenshot

`func (o *ContentFeedback) GetScreenshot() string`

GetScreenshot returns the Screenshot field if non-nil, zero value otherwise.

### GetScreenshotOk

`func (o *ContentFeedback) GetScreenshotOk() (*string, bool)`

GetScreenshotOk returns a tuple with the Screenshot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScreenshot

`func (o *ContentFeedback) SetScreenshot(v string)`

SetScreenshot sets Screenshot field to given value.

### HasScreenshot

`func (o *ContentFeedback) HasScreenshot() bool`

HasScreenshot returns a boolean if a field has been set.

### GetId

`func (o *ContentFeedback) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *ContentFeedback) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *ContentFeedback) SetId(v string)`

SetId sets Id field to given value.


### GetThreatModelId

`func (o *ContentFeedback) GetThreatModelId() string`

GetThreatModelId returns the ThreatModelId field if non-nil, zero value otherwise.

### GetThreatModelIdOk

`func (o *ContentFeedback) GetThreatModelIdOk() (*string, bool)`

GetThreatModelIdOk returns a tuple with the ThreatModelId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreatModelId

`func (o *ContentFeedback) SetThreatModelId(v string)`

SetThreatModelId sets ThreatModelId field to given value.


### GetCreatedBy

`func (o *ContentFeedback) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *ContentFeedback) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *ContentFeedback) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.


### GetCreatedAt

`func (o *ContentFeedback) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *ContentFeedback) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *ContentFeedback) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


