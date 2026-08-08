# CreateThreatModelDocument202Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Document** | [**Document**](Document.md) |  | 
**JobId** | **string** | Identifier of the queued extraction job, for client correlation. The extraction result is surfaced via the document access_status and the document.extraction_* webhook events; there is no dedicated job-status endpoint. | 

## Methods

### NewCreateThreatModelDocument202Response

`func NewCreateThreatModelDocument202Response(document Document, jobId string, ) *CreateThreatModelDocument202Response`

NewCreateThreatModelDocument202Response instantiates a new CreateThreatModelDocument202Response object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCreateThreatModelDocument202ResponseWithDefaults

`func NewCreateThreatModelDocument202ResponseWithDefaults() *CreateThreatModelDocument202Response`

NewCreateThreatModelDocument202ResponseWithDefaults instantiates a new CreateThreatModelDocument202Response object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDocument

`func (o *CreateThreatModelDocument202Response) GetDocument() Document`

GetDocument returns the Document field if non-nil, zero value otherwise.

### GetDocumentOk

`func (o *CreateThreatModelDocument202Response) GetDocumentOk() (*Document, bool)`

GetDocumentOk returns a tuple with the Document field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDocument

`func (o *CreateThreatModelDocument202Response) SetDocument(v Document)`

SetDocument sets Document field to given value.


### GetJobId

`func (o *CreateThreatModelDocument202Response) GetJobId() string`

GetJobId returns the JobId field if non-nil, zero value otherwise.

### GetJobIdOk

`func (o *CreateThreatModelDocument202Response) GetJobIdOk() (*string, bool)`

GetJobIdOk returns a tuple with the JobId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJobId

`func (o *CreateThreatModelDocument202Response) SetJobId(v string)`

SetJobId sets JobId field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


