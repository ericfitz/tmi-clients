# UsabilityFeedbackInput

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

## Methods

### NewUsabilityFeedbackInput

`func NewUsabilityFeedbackInput(sentiment string, surface string, clientId string, ) *UsabilityFeedbackInput`

NewUsabilityFeedbackInput instantiates a new UsabilityFeedbackInput object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewUsabilityFeedbackInputWithDefaults

`func NewUsabilityFeedbackInputWithDefaults() *UsabilityFeedbackInput`

NewUsabilityFeedbackInputWithDefaults instantiates a new UsabilityFeedbackInput object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetSentiment

`func (o *UsabilityFeedbackInput) GetSentiment() string`

GetSentiment returns the Sentiment field if non-nil, zero value otherwise.

### GetSentimentOk

`func (o *UsabilityFeedbackInput) GetSentimentOk() (*string, bool)`

GetSentimentOk returns a tuple with the Sentiment field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSentiment

`func (o *UsabilityFeedbackInput) SetSentiment(v string)`

SetSentiment sets Sentiment field to given value.


### GetVerbatim

`func (o *UsabilityFeedbackInput) GetVerbatim() string`

GetVerbatim returns the Verbatim field if non-nil, zero value otherwise.

### GetVerbatimOk

`func (o *UsabilityFeedbackInput) GetVerbatimOk() (*string, bool)`

GetVerbatimOk returns a tuple with the Verbatim field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVerbatim

`func (o *UsabilityFeedbackInput) SetVerbatim(v string)`

SetVerbatim sets Verbatim field to given value.

### HasVerbatim

`func (o *UsabilityFeedbackInput) HasVerbatim() bool`

HasVerbatim returns a boolean if a field has been set.

### GetSurface

`func (o *UsabilityFeedbackInput) GetSurface() string`

GetSurface returns the Surface field if non-nil, zero value otherwise.

### GetSurfaceOk

`func (o *UsabilityFeedbackInput) GetSurfaceOk() (*string, bool)`

GetSurfaceOk returns a tuple with the Surface field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSurface

`func (o *UsabilityFeedbackInput) SetSurface(v string)`

SetSurface sets Surface field to given value.


### GetClientId

`func (o *UsabilityFeedbackInput) GetClientId() string`

GetClientId returns the ClientId field if non-nil, zero value otherwise.

### GetClientIdOk

`func (o *UsabilityFeedbackInput) GetClientIdOk() (*string, bool)`

GetClientIdOk returns a tuple with the ClientId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientId

`func (o *UsabilityFeedbackInput) SetClientId(v string)`

SetClientId sets ClientId field to given value.


### GetClientVersion

`func (o *UsabilityFeedbackInput) GetClientVersion() string`

GetClientVersion returns the ClientVersion field if non-nil, zero value otherwise.

### GetClientVersionOk

`func (o *UsabilityFeedbackInput) GetClientVersionOk() (*string, bool)`

GetClientVersionOk returns a tuple with the ClientVersion field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientVersion

`func (o *UsabilityFeedbackInput) SetClientVersion(v string)`

SetClientVersion sets ClientVersion field to given value.

### HasClientVersion

`func (o *UsabilityFeedbackInput) HasClientVersion() bool`

HasClientVersion returns a boolean if a field has been set.

### GetClientBuild

`func (o *UsabilityFeedbackInput) GetClientBuild() string`

GetClientBuild returns the ClientBuild field if non-nil, zero value otherwise.

### GetClientBuildOk

`func (o *UsabilityFeedbackInput) GetClientBuildOk() (*string, bool)`

GetClientBuildOk returns a tuple with the ClientBuild field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetClientBuild

`func (o *UsabilityFeedbackInput) SetClientBuild(v string)`

SetClientBuild sets ClientBuild field to given value.

### HasClientBuild

`func (o *UsabilityFeedbackInput) HasClientBuild() bool`

HasClientBuild returns a boolean if a field has been set.

### GetUserAgent

`func (o *UsabilityFeedbackInput) GetUserAgent() string`

GetUserAgent returns the UserAgent field if non-nil, zero value otherwise.

### GetUserAgentOk

`func (o *UsabilityFeedbackInput) GetUserAgentOk() (*string, bool)`

GetUserAgentOk returns a tuple with the UserAgent field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserAgent

`func (o *UsabilityFeedbackInput) SetUserAgent(v string)`

SetUserAgent sets UserAgent field to given value.

### HasUserAgent

`func (o *UsabilityFeedbackInput) HasUserAgent() bool`

HasUserAgent returns a boolean if a field has been set.

### GetUserAgentData

`func (o *UsabilityFeedbackInput) GetUserAgentData() map[string]interface{}`

GetUserAgentData returns the UserAgentData field if non-nil, zero value otherwise.

### GetUserAgentDataOk

`func (o *UsabilityFeedbackInput) GetUserAgentDataOk() (*map[string]interface{}, bool)`

GetUserAgentDataOk returns a tuple with the UserAgentData field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetUserAgentData

`func (o *UsabilityFeedbackInput) SetUserAgentData(v map[string]interface{})`

SetUserAgentData sets UserAgentData field to given value.

### HasUserAgentData

`func (o *UsabilityFeedbackInput) HasUserAgentData() bool`

HasUserAgentData returns a boolean if a field has been set.

### GetViewport

`func (o *UsabilityFeedbackInput) GetViewport() string`

GetViewport returns the Viewport field if non-nil, zero value otherwise.

### GetViewportOk

`func (o *UsabilityFeedbackInput) GetViewportOk() (*string, bool)`

GetViewportOk returns a tuple with the Viewport field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetViewport

`func (o *UsabilityFeedbackInput) SetViewport(v string)`

SetViewport sets Viewport field to given value.

### HasViewport

`func (o *UsabilityFeedbackInput) HasViewport() bool`

HasViewport returns a boolean if a field has been set.

### GetScreenshot

`func (o *UsabilityFeedbackInput) GetScreenshot() string`

GetScreenshot returns the Screenshot field if non-nil, zero value otherwise.

### GetScreenshotOk

`func (o *UsabilityFeedbackInput) GetScreenshotOk() (*string, bool)`

GetScreenshotOk returns a tuple with the Screenshot field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetScreenshot

`func (o *UsabilityFeedbackInput) SetScreenshot(v string)`

SetScreenshot sets Screenshot field to given value.

### HasScreenshot

`func (o *UsabilityFeedbackInput) HasScreenshot() bool`

HasScreenshot returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


