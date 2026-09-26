# UsabilityFeedback

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Sentiment** | **string** | User sentiment | 
**Verbatim** | Pointer to **string** | Optional free-text comment from the user | [optional] 
**Surface** | **string** | Logical UI-surface identifier (developer-supplied tag for analytics) | 
**ClientId** | **string** | Identifier of the client emitting the feedback (e.g., &#39;tmi-ux&#39;) | 
**ClientVersion** | Pointer to **string** | Semver version string of the client | [optional] 
**ClientBuild** | Pointer to **string** | Short commit hash of the client build | [optional] 
**UserAgent** | Pointer to **string** | Browser User-Agent header value (when applicable) | [optional] 
**UserAgentData** | Pointer to **map[string]interface{}** | Optional NavigatorUAData payload (≤ 4 KB serialized) | [optional] 
**Viewport** | Pointer to **string** | Viewport dimensions, e.g. &#39;1280x1024&#39; | [optional] 
**Screenshot** | Pointer to **string** | Optional viewport screenshot captured by the client at submission time. Data URL form (e.g. &#x60;data:image/jpeg;base64,...&#x60;). Used as support context. | [optional] 
**Id** | **string** | Server-assigned identifier | 
**CreatedBy** | **string** | Internal UUID of the submitting user | 
**CreatedAt** | **time.Time** | Server-assigned timestamp | 

## Methods

### NewUsabilityFeedback

`func NewUsabilityFeedback(sentiment string, surface string, clientId string, id string, createdBy string, createdAt time.Time, ) *UsabilityFeedback`

NewUsabilityFeedback instantiates a new UsabilityFeedback object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUsabilityFeedbackWithDefaults

`func NewUsabilityFeedbackWithDefaults() *UsabilityFeedback`

NewUsabilityFeedbackWithDefaults instantiates a new UsabilityFeedback object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSentiment

`func (o *UsabilityFeedback) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *UsabilityFeedback) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *UsabilityFeedback) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetVerbatim

`func (o *UsabilityFeedback) GetVerbatim() string`

GetVerbatim returns the Verbatim field if non-nil, zero value otherwise.

### GetVerbatimOk

`func (o *UsabilityFeedback) GetVerbatimOk() (*string, bool)`

GetVerbatimOk returns a tuple with the Verbatim field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerbatim

`func (o *UsabilityFeedback) SetVerbatim(v string)`

SetVerbatim sets Verbatim field to given value.

### HasVerbatim

`func (o *UsabilityFeedback) HasVerbatim() bool`

HasVerbatim returns a boolean if a field has been set.

### GetSurface

`func (o *UsabilityFeedback) GetSurface() string`

GetSurface returns the Surface field if non-nil, zero value otherwise.

### GetSurfaceOk

`func (o *UsabilityFeedback) GetSurfaceOk() (*string, bool)`

GetSurfaceOk returns a tuple with the Surface field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurface

`func (o *UsabilityFeedback) SetSurface(v string)`

SetSurface sets Surface field to given value.


### GetClientId

`func (o *UsabilityFeedback) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *UsabilityFeedback) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *UsabilityFeedback) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetClientVersion

`func (o *UsabilityFeedback) GetClientVersion() string`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *UsabilityFeedback) GetClientVersionOk() (*string, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *UsabilityFeedback) SetClientVersion(v string)`

SetClientVersion sets ClientVersion field to given value.

### HasClientVersion

`func (o *UsabilityFeedback) HasClientVersion() bool`

HasClientVersion returns a boolean if a field has been set.

### GetClientBuild

`func (o *UsabilityFeedback) GetClientBuild() string`

GetClientBuild returns the ClientBuild field if non-nil, zero value otherwise.

### GetClientBuildOk

`func (o *UsabilityFeedback) GetClientBuildOk() (*string, bool)`

GetClientBuildOk returns a tuple with the ClientBuild field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientBuild

`func (o *UsabilityFeedback) SetClientBuild(v string)`

SetClientBuild sets ClientBuild field to given value.

### HasClientBuild

`func (o *UsabilityFeedback) HasClientBuild() bool`

HasClientBuild returns a boolean if a field has been set.

### GetUserAgent

`func (o *UsabilityFeedback) GetUserAgent() string`

GetUserAgent returns the UserAgent field if non-nil, zero value otherwise.

### GetUserAgentOk

`func (o *UsabilityFeedback) GetUserAgentOk() (*string, bool)`

GetUserAgentOk returns a tuple with the UserAgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserAgent

`func (o *UsabilityFeedback) SetUserAgent(v string)`

SetUserAgent sets UserAgent field to given value.

### HasUserAgent

`func (o *UsabilityFeedback) HasUserAgent() bool`

HasUserAgent returns a boolean if a field has been set.

### GetUserAgentData

`func (o *UsabilityFeedback) GetUserAgentData() map[string]interface{}`

GetUserAgentData returns the UserAgentData field if non-nil, zero value otherwise.

### GetUserAgentDataOk

`func (o *UsabilityFeedback) GetUserAgentDataOk() (*map[string]interface{}, bool)`

GetUserAgentDataOk returns a tuple with the UserAgentData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserAgentData

`func (o *UsabilityFeedback) SetUserAgentData(v map[string]interface{})`

SetUserAgentData sets UserAgentData field to given value.

### HasUserAgentData

`func (o *UsabilityFeedback) HasUserAgentData() bool`

HasUserAgentData returns a boolean if a field has been set.

### GetViewport

`func (o *UsabilityFeedback) GetViewport() string`

GetViewport returns the Viewport field if non-nil, zero value otherwise.

### GetViewportOk

`func (o *UsabilityFeedback) GetViewportOk() (*string, bool)`

GetViewportOk returns a tuple with the Viewport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewport

`func (o *UsabilityFeedback) SetViewport(v string)`

SetViewport sets Viewport field to given value.

### HasViewport

`func (o *UsabilityFeedback) HasViewport() bool`

HasViewport returns a boolean if a field has been set.

### GetScreenshot

`func (o *UsabilityFeedback) GetScreenshot() string`

GetScreenshot returns the Screenshot field if non-nil, zero value otherwise.

### GetScreenshotOk

`func (o *UsabilityFeedback) GetScreenshotOk() (*string, bool)`

GetScreenshotOk returns a tuple with the Screenshot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScreenshot

`func (o *UsabilityFeedback) SetScreenshot(v string)`

SetScreenshot sets Screenshot field to given value.

### HasScreenshot

`func (o *UsabilityFeedback) HasScreenshot() bool`

HasScreenshot returns a boolean if a field has been set.

### GetId

`func (o *UsabilityFeedback) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *UsabilityFeedback) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *UsabilityFeedback) SetId(v string)`

SetId sets Id field to given value.


### GetCreatedBy

`func (o *UsabilityFeedback) GetCreatedBy() string`

GetCreatedBy returns the CreatedBy field if non-nil, zero value otherwise.

### GetCreatedByOk

`func (o *UsabilityFeedback) GetCreatedByOk() (*string, bool)`

GetCreatedByOk returns a tuple with the CreatedBy field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedBy

`func (o *UsabilityFeedback) SetCreatedBy(v string)`

SetCreatedBy sets CreatedBy field to given value.


### GetCreatedAt

`func (o *UsabilityFeedback) GetCreatedAt() time.Time`

GetCreatedAt returns the CreatedAt field if non-nil, zero value otherwise.

### GetCreatedAtOk

`func (o *UsabilityFeedback) GetCreatedAtOk() (*time.Time, bool)`

GetCreatedAtOk returns a tuple with the CreatedAt field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCreatedAt

`func (o *UsabilityFeedback) SetCreatedAt(v time.Time)`

SetCreatedAt sets CreatedAt field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


