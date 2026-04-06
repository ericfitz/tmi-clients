# @tmiclient/client@1.0.0

A TypeScript SDK client for the api.tmi.dev API.

## Usage

First, install the SDK from npm.

```bash
npm install @tmiclient/client --save
```

Next, try it out.


```ts
import {
  Configuration,
  AddonsApi,
} from '@tmiclient/client';
import type { CreateAddonOperationRequest } from '@tmiclient/client';

async function example() {
  console.log("🚀 Testing @tmiclient/client SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerAuth
    accessToken: "YOUR BEARER TOKEN",
  });
  const api = new AddonsApi(config);

  const body = {
    // CreateAddonRequest | Addon registration details
    createAddonRequest: ...,
  } satisfies CreateAddonOperationRequest;

  try {
    const data = await api.createAddon(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```


## Documentation

### API Endpoints

All URIs are relative to *https://api.tmi.dev*

| Class | Method | HTTP request | Description
| ----- | ------ | ------------ | -------------
*AddonsApi* | [**createAddon**](docs/AddonsApi.md#createaddonoperation) | **POST** /addons | Create add-on
*AddonsApi* | [**deleteAddon**](docs/AddonsApi.md#deleteaddon) | **DELETE** /addons/{id} | Delete add-on
*AddonsApi* | [**getAddon**](docs/AddonsApi.md#getaddon) | **GET** /addons/{id} | Get add-on
*AddonsApi* | [**getInvocation**](docs/AddonsApi.md#getinvocation) | **GET** /invocations/{id} | Get invocation
*AddonsApi* | [**invokeAddon**](docs/AddonsApi.md#invokeaddonoperation) | **POST** /addons/{id}/invoke | Invoke add-on
*AddonsApi* | [**listAddons**](docs/AddonsApi.md#listaddons) | **GET** /addons | List add-ons
*AddonsApi* | [**listInvocations**](docs/AddonsApi.md#listinvocations) | **GET** /invocations | List invocations
*AddonsApi* | [**updateInvocationStatus**](docs/AddonsApi.md#updateinvocationstatusoperation) | **POST** /invocations/{id}/status | Update invocation status
*AdminUsersApi* | [**createAdminUserClientCredential**](docs/AdminUsersApi.md#createadminuserclientcredential) | **POST** /admin/users/{internal_uuid}/client_credentials | Create a client credential for an automation user
*AdminUsersApi* | [**createAutomationAccount**](docs/AdminUsersApi.md#createautomationaccountoperation) | **POST** /admin/users/automation | Create an automation (service) account
*AdminUsersApi* | [**deleteAdminUserClientCredential**](docs/AdminUsersApi.md#deleteadminuserclientcredential) | **DELETE** /admin/users/{internal_uuid}/client_credentials/{credential_id} | Delete a client credential for an automation user
*AdminUsersApi* | [**listAdminUserClientCredentials**](docs/AdminUsersApi.md#listadminuserclientcredentials) | **GET** /admin/users/{internal_uuid}/client_credentials | List client credentials for an automation user
*AdministrationApi* | [**addGroupMember**](docs/AdministrationApi.md#addgroupmemberoperation) | **POST** /admin/groups/{internal_uuid}/members | Add member to group
*AdministrationApi* | [**createAdminGroup**](docs/AdministrationApi.md#createadmingroupoperation) | **POST** /admin/groups | Create provider-independent group
*AdministrationApi* | [**deleteAddonInvocationQuota**](docs/AdministrationApi.md#deleteaddoninvocationquota) | **DELETE** /admin/quotas/addons/{user_id} | Delete addon invocation quota
*AdministrationApi* | [**deleteAdminGroup**](docs/AdministrationApi.md#deleteadmingroup) | **DELETE** /admin/groups/{internal_uuid} | Delete group
*AdministrationApi* | [**deleteAdminUser**](docs/AdministrationApi.md#deleteadminuser) | **DELETE** /admin/users/{internal_uuid} | Delete user
*AdministrationApi* | [**deleteSystemSetting**](docs/AdministrationApi.md#deletesystemsetting) | **DELETE** /admin/settings/{key} | Delete system setting
*AdministrationApi* | [**deleteUserAPIQuota**](docs/AdministrationApi.md#deleteuserapiquota) | **DELETE** /admin/quotas/users/{user_id} | Delete user API quota
*AdministrationApi* | [**deleteWebhookQuota**](docs/AdministrationApi.md#deletewebhookquota) | **DELETE** /admin/quotas/webhooks/{user_id} | Delete webhook quota
*AdministrationApi* | [**getAddonInvocationQuota**](docs/AdministrationApi.md#getaddoninvocationquota) | **GET** /admin/quotas/addons/{user_id} | Get addon invocation quota
*AdministrationApi* | [**getAdminGroup**](docs/AdministrationApi.md#getadmingroup) | **GET** /admin/groups/{internal_uuid} | Get group details
*AdministrationApi* | [**getAdminUser**](docs/AdministrationApi.md#getadminuser) | **GET** /admin/users/{internal_uuid} | Get user details
*AdministrationApi* | [**getSystemSetting**](docs/AdministrationApi.md#getsystemsetting) | **GET** /admin/settings/{key} | Get system setting
*AdministrationApi* | [**getUserAPIQuota**](docs/AdministrationApi.md#getuserapiquota) | **GET** /admin/quotas/users/{user_id} | Get user API quota
*AdministrationApi* | [**getWebhookQuota**](docs/AdministrationApi.md#getwebhookquota) | **GET** /admin/quotas/webhooks/{user_id} | Get webhook quota
*AdministrationApi* | [**listAddonInvocationQuotas**](docs/AdministrationApi.md#listaddoninvocationquotas) | **GET** /admin/quotas/addons | List all addon invocation quotas
*AdministrationApi* | [**listAdminGroups**](docs/AdministrationApi.md#listadmingroups) | **GET** /admin/groups | List groups
*AdministrationApi* | [**listAdminUsers**](docs/AdministrationApi.md#listadminusers) | **GET** /admin/users | List users
*AdministrationApi* | [**listGroupMembers**](docs/AdministrationApi.md#listgroupmembers) | **GET** /admin/groups/{internal_uuid}/members | List group members
*AdministrationApi* | [**listSystemSettings**](docs/AdministrationApi.md#listsystemsettings) | **GET** /admin/settings | List system settings
*AdministrationApi* | [**listUserAPIQuotas**](docs/AdministrationApi.md#listuserapiquotas) | **GET** /admin/quotas/users | List all user API quotas
*AdministrationApi* | [**listWebhookQuotas**](docs/AdministrationApi.md#listwebhookquotas) | **GET** /admin/quotas/webhooks | List all webhook quotas
*AdministrationApi* | [**migrateSystemSettings**](docs/AdministrationApi.md#migratesystemsettings) | **POST** /admin/settings/migrate | Migrate settings from configuration
*AdministrationApi* | [**reencryptSystemSettings**](docs/AdministrationApi.md#reencryptsystemsettings) | **POST** /admin/settings/reencrypt | Re-encrypt all system settings
*AdministrationApi* | [**removeGroupMember**](docs/AdministrationApi.md#removegroupmember) | **DELETE** /admin/groups/{internal_uuid}/members/{member_uuid} | Remove member from group
*AdministrationApi* | [**transferAdminUserOwnership**](docs/AdministrationApi.md#transferadminuserownership) | **POST** /admin/users/{internal_uuid}/transfer | Transfer user ownership to another user
*AdministrationApi* | [**updateAddonInvocationQuota**](docs/AdministrationApi.md#updateaddoninvocationquota) | **PUT** /admin/quotas/addons/{user_id} | Update addon invocation quota
*AdministrationApi* | [**updateAdminGroup**](docs/AdministrationApi.md#updateadmingroupoperation) | **PATCH** /admin/groups/{internal_uuid} | Update group metadata
*AdministrationApi* | [**updateAdminUser**](docs/AdministrationApi.md#updateadminuseroperation) | **PATCH** /admin/users/{internal_uuid} | Update user metadata
*AdministrationApi* | [**updateSystemSetting**](docs/AdministrationApi.md#updatesystemsetting) | **PUT** /admin/settings/{key} | Update system setting
*AdministrationApi* | [**updateUserAPIQuota**](docs/AdministrationApi.md#updateuserapiquota) | **PUT** /admin/quotas/users/{user_id} | Update user API quota
*AdministrationApi* | [**updateWebhookQuota**](docs/AdministrationApi.md#updatewebhookquota) | **PUT** /admin/quotas/webhooks/{user_id} | Update webhook quota
*AssetsApi* | [**patchThreatModelAsset**](docs/AssetsApi.md#patchthreatmodelasset) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id} | Partially update asset
*AuditTrailApi* | [**getAssetAuditTrail**](docs/AuditTrailApi.md#getassetaudittrail) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/audit_trail | List audit trail for an asset
*AuditTrailApi* | [**getAuditEntry**](docs/AuditTrailApi.md#getauditentry) | **GET** /threat_models/{threat_model_id}/audit_trail/{entry_id} | Get a single audit trail entry
*AuditTrailApi* | [**getDiagramAuditTrail**](docs/AuditTrailApi.md#getdiagramaudittrail) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/audit_trail | List audit trail for a diagram
*AuditTrailApi* | [**getDocumentAuditTrail**](docs/AuditTrailApi.md#getdocumentaudittrail) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/audit_trail | List audit trail for a document
*AuditTrailApi* | [**getNoteAuditTrail**](docs/AuditTrailApi.md#getnoteaudittrail) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/audit_trail | List audit trail for a note
*AuditTrailApi* | [**getRepositoryAuditTrail**](docs/AuditTrailApi.md#getrepositoryaudittrail) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/audit_trail | List audit trail for a repository
*AuditTrailApi* | [**getThreatAuditTrail**](docs/AuditTrailApi.md#getthreataudittrail) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/audit_trail | List audit trail for a threat
*AuditTrailApi* | [**getThreatModelAuditTrail**](docs/AuditTrailApi.md#getthreatmodelaudittrail) | **GET** /threat_models/{threat_model_id}/audit_trail | List audit trail for a threat model and all sub-objects
*AuditTrailApi* | [**rollbackToVersion**](docs/AuditTrailApi.md#rollbacktoversion) | **POST** /threat_models/{threat_model_id}/audit_trail/{entry_id}/rollback | Rollback an entity to a previous version
*AuthenticationApi* | [**authorizeOAuthProvider**](docs/AuthenticationApi.md#authorizeoauthprovider) | **GET** /oauth2/authorize | Initiate OAuth authorization flow
*AuthenticationApi* | [**createCurrentUserClientCredential**](docs/AuthenticationApi.md#createcurrentuserclientcredentialoperation) | **POST** /me/client_credentials | Create client credential
*AuthenticationApi* | [**deleteCurrentUserClientCredential**](docs/AuthenticationApi.md#deletecurrentuserclientcredential) | **DELETE** /me/client_credentials/{credential_id} | Delete client credential
*AuthenticationApi* | [**exchangeOAuthCode**](docs/AuthenticationApi.md#exchangeoauthcodeoperation) | **POST** /oauth2/token | Exchange OAuth credentials for JWT tokens
*AuthenticationApi* | [**getAuthProviders**](docs/AuthenticationApi.md#getauthproviders) | **GET** /oauth2/providers | List available OAuth providers
*AuthenticationApi* | [**getCurrentUser**](docs/AuthenticationApi.md#getcurrentuser) | **GET** /oauth2/userinfo | Get current user information
*AuthenticationApi* | [**getCurrentUserProfile**](docs/AuthenticationApi.md#getcurrentuserprofile) | **GET** /me | Get current user profile
*AuthenticationApi* | [**getProviderGroups**](docs/AuthenticationApi.md#getprovidergroups) | **GET** /oauth2/providers/{idp}/groups | Get groups for identity provider
*AuthenticationApi* | [**getSAMLMetadata**](docs/AuthenticationApi.md#getsamlmetadata) | **GET** /saml/{provider}/metadata | Get SAML service provider metadata
*AuthenticationApi* | [**getSAMLProviders**](docs/AuthenticationApi.md#getsamlproviders) | **GET** /saml/providers | List available SAML providers
*AuthenticationApi* | [**handleOAuthCallback**](docs/AuthenticationApi.md#handleoauthcallback) | **GET** /oauth2/callback | Handle OAuth callback
*AuthenticationApi* | [**initiateSAMLLogin**](docs/AuthenticationApi.md#initiatesamllogin) | **GET** /saml/{provider}/login | Initiate SAML authentication
*AuthenticationApi* | [**introspectToken**](docs/AuthenticationApi.md#introspecttoken) | **POST** /oauth2/introspect | Token Introspection
*AuthenticationApi* | [**listCurrentUserClientCredentials**](docs/AuthenticationApi.md#listcurrentuserclientcredentials) | **GET** /me/client_credentials | List client credentials
*AuthenticationApi* | [**listMyGroupMembers**](docs/AuthenticationApi.md#listmygroupmembers) | **GET** /me/groups/{internal_uuid}/members | List members of my group
*AuthenticationApi* | [**listMyGroups**](docs/AuthenticationApi.md#listmygroups) | **GET** /me/groups | List my groups
*AuthenticationApi* | [**processSAMLLogout**](docs/AuthenticationApi.md#processsamllogout) | **GET** /saml/slo | SAML Single Logout
*AuthenticationApi* | [**processSAMLLogoutPost**](docs/AuthenticationApi.md#processsamllogoutpost) | **POST** /saml/slo | SAML Single Logout (POST)
*AuthenticationApi* | [**processSAMLResponse**](docs/AuthenticationApi.md#processsamlresponse) | **POST** /saml/acs | SAML Assertion Consumer Service
*AuthenticationApi* | [**refreshToken**](docs/AuthenticationApi.md#refreshtoken) | **POST** /oauth2/refresh | Refresh JWT token
*AuthenticationApi* | [**revokeToken**](docs/AuthenticationApi.md#revoketoken) | **POST** /oauth2/revoke | Revoke token
*CollaborationApi* | [**createDiagramCollaborationSession**](docs/CollaborationApi.md#creatediagramcollaborationsession) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Create diagram collaboration session
*CollaborationApi* | [**endDiagramCollaborationSession**](docs/CollaborationApi.md#enddiagramcollaborationsession) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | End diagram collaboration session
*CollaborationApi* | [**getCurrentUserSessions**](docs/CollaborationApi.md#getcurrentusersessions) | **GET** /me/sessions | List active collaboration sessions
*CollaborationApi* | [**getDiagramCollaborationSession**](docs/CollaborationApi.md#getdiagramcollaborationsession) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/collaborate | Get diagram collaboration session
*ConfigurationApi* | [**getClientConfig**](docs/ConfigurationApi.md#getclientconfig) | **GET** /config | Get client configuration
*DocumentsApi* | [**patchThreatModelDocument**](docs/DocumentsApi.md#patchthreatmodeldocument) | **PATCH** /threat_models/{threat_model_id}/documents/{document_id} | Partially update document
*GeneralApi* | [**getApiInfo**](docs/GeneralApi.md#getapiinfo) | **GET** / | Get API information
*NotesApi* | [**patchThreatModelNote**](docs/NotesApi.md#patchthreatmodelnote) | **PATCH** /threat_models/{threat_model_id}/notes/{note_id} | Partially update note
*OAuthDiscoveryApi* | [**getOAuthProtectedResourceMetadata**](docs/OAuthDiscoveryApi.md#getoauthprotectedresourcemetadata) | **GET** /.well-known/oauth-protected-resource | OAuth 2.0 Protected Resource Metadata
*OIDCDiscoveryApi* | [**getJWKS**](docs/OIDCDiscoveryApi.md#getjwks) | **GET** /.well-known/jwks.json | JSON Web Key Set
*OIDCDiscoveryApi* | [**getOAuthAuthorizationServerMetadata**](docs/OIDCDiscoveryApi.md#getoauthauthorizationservermetadata) | **GET** /.well-known/oauth-authorization-server | OAuth 2.0 Authorization Server Metadata
*OIDCDiscoveryApi* | [**getOpenIDConfiguration**](docs/OIDCDiscoveryApi.md#getopenidconfiguration) | **GET** /.well-known/openid-configuration | OpenID Connect Discovery Configuration
*ProjectsApi* | [**bulkCreateProjectMetadata**](docs/ProjectsApi.md#bulkcreateprojectmetadata) | **POST** /projects/{project_id}/metadata/bulk | Bulk create project metadata
*ProjectsApi* | [**bulkReplaceProjectMetadata**](docs/ProjectsApi.md#bulkreplaceprojectmetadata) | **PUT** /projects/{project_id}/metadata/bulk | Bulk replace project metadata
*ProjectsApi* | [**bulkUpsertProjectMetadata**](docs/ProjectsApi.md#bulkupsertprojectmetadata) | **PATCH** /projects/{project_id}/metadata/bulk | Bulk upsert project metadata
*ProjectsApi* | [**createProject**](docs/ProjectsApi.md#createproject) | **POST** /projects | Create a project
*ProjectsApi* | [**createProjectMetadata**](docs/ProjectsApi.md#createprojectmetadata) | **POST** /projects/{project_id}/metadata | Create project metadata
*ProjectsApi* | [**deleteProject**](docs/ProjectsApi.md#deleteproject) | **DELETE** /projects/{project_id} | Delete a project
*ProjectsApi* | [**deleteProjectMetadata**](docs/ProjectsApi.md#deleteprojectmetadata) | **DELETE** /projects/{project_id}/metadata/{key} | Delete project metadata
*ProjectsApi* | [**getProject**](docs/ProjectsApi.md#getproject) | **GET** /projects/{project_id} | Get a project
*ProjectsApi* | [**getProjectMetadata**](docs/ProjectsApi.md#getprojectmetadata) | **GET** /projects/{project_id}/metadata | Get project metadata
*ProjectsApi* | [**listProjects**](docs/ProjectsApi.md#listprojects) | **GET** /projects | List projects
*ProjectsApi* | [**patchProject**](docs/ProjectsApi.md#patchproject) | **PATCH** /projects/{project_id} | Patch a project
*ProjectsApi* | [**updateProject**](docs/ProjectsApi.md#updateproject) | **PUT** /projects/{project_id} | Update a project
*ProjectsApi* | [**updateProjectMetadata**](docs/ProjectsApi.md#updateprojectmetadata) | **PUT** /projects/{project_id}/metadata/{key} | Update project metadata
*RepositoriesApi* | [**patchThreatModelRepository**](docs/RepositoriesApi.md#patchthreatmodelrepository) | **PATCH** /threat_models/{threat_model_id}/repositories/{repository_id} | Partially update repository
*SAMLApi* | [**listSAMLUsers**](docs/SAMLApi.md#listsamlusers) | **GET** /saml/providers/{idp}/users | List SAML users for UI autocomplete
*SurveyAdministrationApi* | [**bulkCreateAdminSurveyMetadata**](docs/SurveyAdministrationApi.md#bulkcreateadminsurveymetadata) | **POST** /admin/surveys/{survey_id}/metadata/bulk | Bulk create metadata for a survey
*SurveyAdministrationApi* | [**bulkReplaceAdminSurveyMetadata**](docs/SurveyAdministrationApi.md#bulkreplaceadminsurveymetadata) | **PUT** /admin/surveys/{survey_id}/metadata/bulk | Bulk replace metadata for a survey
*SurveyAdministrationApi* | [**bulkUpsertAdminSurveyMetadata**](docs/SurveyAdministrationApi.md#bulkupsertadminsurveymetadata) | **PATCH** /admin/surveys/{survey_id}/metadata/bulk | Bulk upsert metadata for a survey
*SurveyAdministrationApi* | [**createAdminSurvey**](docs/SurveyAdministrationApi.md#createadminsurvey) | **POST** /admin/surveys | Create a survey
*SurveyAdministrationApi* | [**createAdminSurveyMetadata**](docs/SurveyAdministrationApi.md#createadminsurveymetadata) | **POST** /admin/surveys/{survey_id}/metadata | Add metadata to a survey
*SurveyAdministrationApi* | [**deleteAdminSurvey**](docs/SurveyAdministrationApi.md#deleteadminsurvey) | **DELETE** /admin/surveys/{survey_id} | Delete a survey
*SurveyAdministrationApi* | [**deleteAdminSurveyMetadataByKey**](docs/SurveyAdministrationApi.md#deleteadminsurveymetadatabykey) | **DELETE** /admin/surveys/{survey_id}/metadata/{key} | Delete metadata by key for a survey
*SurveyAdministrationApi* | [**getAdminSurvey**](docs/SurveyAdministrationApi.md#getadminsurvey) | **GET** /admin/surveys/{survey_id} | Get a survey
*SurveyAdministrationApi* | [**getAdminSurveyMetadata**](docs/SurveyAdministrationApi.md#getadminsurveymetadata) | **GET** /admin/surveys/{survey_id}/metadata | Get all metadata for a survey
*SurveyAdministrationApi* | [**getAdminSurveyMetadataByKey**](docs/SurveyAdministrationApi.md#getadminsurveymetadatabykey) | **GET** /admin/surveys/{survey_id}/metadata/{key} | Get metadata by key for a survey
*SurveyAdministrationApi* | [**listAdminSurveys**](docs/SurveyAdministrationApi.md#listadminsurveys) | **GET** /admin/surveys | List surveys
*SurveyAdministrationApi* | [**patchAdminSurvey**](docs/SurveyAdministrationApi.md#patchadminsurvey) | **PATCH** /admin/surveys/{survey_id} | Partially update a survey
*SurveyAdministrationApi* | [**updateAdminSurvey**](docs/SurveyAdministrationApi.md#updateadminsurvey) | **PUT** /admin/surveys/{survey_id} | Update a survey
*SurveyAdministrationApi* | [**updateAdminSurveyMetadataByKey**](docs/SurveyAdministrationApi.md#updateadminsurveymetadatabykey) | **PUT** /admin/surveys/{survey_id}/metadata/{key} | Update metadata by key for a survey
*SurveyIntakeApi* | [**bulkCreateIntakeSurveyResponseMetadata**](docs/SurveyIntakeApi.md#bulkcreateintakesurveyresponsemetadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk create metadata for a survey response
*SurveyIntakeApi* | [**bulkReplaceIntakeSurveyResponseMetadata**](docs/SurveyIntakeApi.md#bulkreplaceintakesurveyresponsemetadata) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk replace metadata for a survey response
*SurveyIntakeApi* | [**bulkUpsertIntakeSurveyResponseMetadata**](docs/SurveyIntakeApi.md#bulkupsertintakesurveyresponsemetadata) | **PATCH** /intake/survey_responses/{survey_response_id}/metadata/bulk | Bulk upsert metadata for a survey response
*SurveyIntakeApi* | [**createIntakeSurveyResponse**](docs/SurveyIntakeApi.md#createintakesurveyresponse) | **POST** /intake/survey_responses | Create survey response
*SurveyIntakeApi* | [**createIntakeSurveyResponseMetadata**](docs/SurveyIntakeApi.md#createintakesurveyresponsemetadata) | **POST** /intake/survey_responses/{survey_response_id}/metadata | Add metadata to a survey response
*SurveyIntakeApi* | [**deleteIntakeSurveyResponse**](docs/SurveyIntakeApi.md#deleteintakesurveyresponse) | **DELETE** /intake/survey_responses/{survey_response_id} | Delete survey response
*SurveyIntakeApi* | [**deleteIntakeSurveyResponseMetadataByKey**](docs/SurveyIntakeApi.md#deleteintakesurveyresponsemetadatabykey) | **DELETE** /intake/survey_responses/{survey_response_id}/metadata/{key} | Delete metadata by key for a survey response
*SurveyIntakeApi* | [**getIntakeSurvey**](docs/SurveyIntakeApi.md#getintakesurvey) | **GET** /intake/surveys/{survey_id} | Get an available survey
*SurveyIntakeApi* | [**getIntakeSurveyResponse**](docs/SurveyIntakeApi.md#getintakesurveyresponse) | **GET** /intake/survey_responses/{survey_response_id} | Get survey response
*SurveyIntakeApi* | [**getIntakeSurveyResponseMetadata**](docs/SurveyIntakeApi.md#getintakesurveyresponsemetadata) | **GET** /intake/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
*SurveyIntakeApi* | [**getIntakeSurveyResponseMetadataByKey**](docs/SurveyIntakeApi.md#getintakesurveyresponsemetadatabykey) | **GET** /intake/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
*SurveyIntakeApi* | [**getIntakeSurveyResponseTriageNote**](docs/SurveyIntakeApi.md#getintakesurveyresponsetriagenote) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
*SurveyIntakeApi* | [**listIntakeSurveyResponseTriageNotes**](docs/SurveyIntakeApi.md#listintakesurveyresponsetriagenotes) | **GET** /intake/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
*SurveyIntakeApi* | [**listIntakeSurveyResponses**](docs/SurveyIntakeApi.md#listintakesurveyresponses) | **GET** /intake/survey_responses | List user\&#39;s survey responses
*SurveyIntakeApi* | [**listIntakeSurveys**](docs/SurveyIntakeApi.md#listintakesurveys) | **GET** /intake/surveys | List available surveys
*SurveyIntakeApi* | [**patchIntakeSurveyResponse**](docs/SurveyIntakeApi.md#patchintakesurveyresponse) | **PATCH** /intake/survey_responses/{survey_response_id} | Partial update survey response
*SurveyIntakeApi* | [**updateIntakeSurveyResponse**](docs/SurveyIntakeApi.md#updateintakesurveyresponse) | **PUT** /intake/survey_responses/{survey_response_id} | Update survey response
*SurveyIntakeApi* | [**updateIntakeSurveyResponseMetadataByKey**](docs/SurveyIntakeApi.md#updateintakesurveyresponsemetadatabykey) | **PUT** /intake/survey_responses/{survey_response_id}/metadata/{key} | Update metadata by key for a survey response
*SurveyTriageApi* | [**createThreatModelFromSurveyResponse**](docs/SurveyTriageApi.md#createthreatmodelfromsurveyresponse) | **POST** /triage/survey_responses/{survey_response_id}/create_threat_model | Create threat model from survey response
*SurveyTriageApi* | [**createTriageSurveyResponseTriageNote**](docs/SurveyTriageApi.md#createtriagesurveyresponsetriagenote) | **POST** /triage/survey_responses/{survey_response_id}/triage_notes | Create a triage note
*SurveyTriageApi* | [**getTriageSurveyResponse**](docs/SurveyTriageApi.md#gettriagesurveyresponse) | **GET** /triage/survey_responses/{survey_response_id} | Get survey response for triage
*SurveyTriageApi* | [**getTriageSurveyResponseMetadata**](docs/SurveyTriageApi.md#gettriagesurveyresponsemetadata) | **GET** /triage/survey_responses/{survey_response_id}/metadata | Get all metadata for a survey response
*SurveyTriageApi* | [**getTriageSurveyResponseMetadataByKey**](docs/SurveyTriageApi.md#gettriagesurveyresponsemetadatabykey) | **GET** /triage/survey_responses/{survey_response_id}/metadata/{key} | Get metadata by key for a survey response
*SurveyTriageApi* | [**getTriageSurveyResponseTriageNote**](docs/SurveyTriageApi.md#gettriagesurveyresponsetriagenote) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes/{triage_note_id} | Get a specific triage note
*SurveyTriageApi* | [**listTriageSurveyResponseTriageNotes**](docs/SurveyTriageApi.md#listtriagesurveyresponsetriagenotes) | **GET** /triage/survey_responses/{survey_response_id}/triage_notes | List triage notes for a survey response
*SurveyTriageApi* | [**listTriageSurveyResponses**](docs/SurveyTriageApi.md#listtriagesurveyresponses) | **GET** /triage/survey_responses | List survey responses for triage
*SurveyTriageApi* | [**patchTriageSurveyResponse**](docs/SurveyTriageApi.md#patchtriagesurveyresponse) | **PATCH** /triage/survey_responses/{survey_response_id} | Partial update survey response for triage
*TeamsApi* | [**bulkCreateTeamMetadata**](docs/TeamsApi.md#bulkcreateteammetadata) | **POST** /teams/{team_id}/metadata/bulk | Bulk create team metadata
*TeamsApi* | [**bulkReplaceTeamMetadata**](docs/TeamsApi.md#bulkreplaceteammetadata) | **PUT** /teams/{team_id}/metadata/bulk | Bulk replace team metadata
*TeamsApi* | [**bulkUpsertTeamMetadata**](docs/TeamsApi.md#bulkupsertteammetadata) | **PATCH** /teams/{team_id}/metadata/bulk | Bulk upsert team metadata
*TeamsApi* | [**createTeam**](docs/TeamsApi.md#createteam) | **POST** /teams | Create a team
*TeamsApi* | [**createTeamMetadata**](docs/TeamsApi.md#createteammetadata) | **POST** /teams/{team_id}/metadata | Create team metadata
*TeamsApi* | [**deleteTeam**](docs/TeamsApi.md#deleteteam) | **DELETE** /teams/{team_id} | Delete a team
*TeamsApi* | [**deleteTeamMetadata**](docs/TeamsApi.md#deleteteammetadata) | **DELETE** /teams/{team_id}/metadata/{key} | Delete team metadata
*TeamsApi* | [**getTeam**](docs/TeamsApi.md#getteam) | **GET** /teams/{team_id} | Get a team
*TeamsApi* | [**getTeamMetadata**](docs/TeamsApi.md#getteammetadata) | **GET** /teams/{team_id}/metadata | Get team metadata
*TeamsApi* | [**listTeams**](docs/TeamsApi.md#listteams) | **GET** /teams | List teams
*TeamsApi* | [**patchTeam**](docs/TeamsApi.md#patchteam) | **PATCH** /teams/{team_id} | Patch a team
*TeamsApi* | [**updateTeam**](docs/TeamsApi.md#updateteam) | **PUT** /teams/{team_id} | Update a team
*TeamsApi* | [**updateTeamMetadata**](docs/TeamsApi.md#updateteammetadata) | **PUT** /teams/{team_id}/metadata/{key} | Update team metadata
*ThreatModelSubResourcesApi* | [**bulkCreateDiagramMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatediagrammetadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk create diagram metadata
*ThreatModelSubResourcesApi* | [**bulkCreateDocumentMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatedocumentmetadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk create document metadata
*ThreatModelSubResourcesApi* | [**bulkCreateNoteMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatenotemetadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk create note metadata
*ThreatModelSubResourcesApi* | [**bulkCreateRepositoryMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreaterepositorymetadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk create source metadata
*ThreatModelSubResourcesApi* | [**bulkCreateThreatMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmetadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk create threat metadata
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodelassetmetadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk create asset metadata
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelAssets**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodelassets) | **POST** /threat_models/{threat_model_id}/assets/bulk | Bulk create assets
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelDocuments**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodeldocuments) | **POST** /threat_models/{threat_model_id}/documents/bulk | Bulk create documents
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelMetadata**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodelmetadata) | **POST** /threat_models/{threat_model_id}/metadata/bulk | Bulk create threat model metadata
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelRepositories**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodelrepositories) | **POST** /threat_models/{threat_model_id}/repositories/bulk | Bulk create sources
*ThreatModelSubResourcesApi* | [**bulkCreateThreatModelThreats**](docs/ThreatModelSubResourcesApi.md#bulkcreatethreatmodelthreats) | **POST** /threat_models/{threat_model_id}/threats/bulk | Bulk create threats
*ThreatModelSubResourcesApi* | [**bulkReplaceDiagramMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacediagrammetadata) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk replace diagram metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceDocumentMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacedocumentmetadata) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk replace document metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceNoteMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacenotemetadata) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk replace note metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceRepositoryMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacerepositorymetadata) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk replace repository metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceThreatMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacethreatmetadata) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk replace threat metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacethreatmodelassetmetadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk replace asset metadata
*ThreatModelSubResourcesApi* | [**bulkReplaceThreatModelMetadata**](docs/ThreatModelSubResourcesApi.md#bulkreplacethreatmodelmetadata) | **PUT** /threat_models/{threat_model_id}/metadata/bulk | Bulk replace threat model metadata
*ThreatModelSubResourcesApi* | [**bulkUpdateThreatModelThreats**](docs/ThreatModelSubResourcesApi.md#bulkupdatethreatmodelthreats) | **PUT** /threat_models/{threat_model_id}/threats/bulk | Bulk update threats
*ThreatModelSubResourcesApi* | [**bulkUpsertDiagramMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertdiagrammetadata) | **PATCH** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/bulk | Bulk upsert diagram metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertDocumentMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertdocumentmetadata) | **PATCH** /threat_models/{threat_model_id}/documents/{document_id}/metadata/bulk | Bulk upsert document metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertNoteMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertnotemetadata) | **PATCH** /threat_models/{threat_model_id}/notes/{note_id}/metadata/bulk | Bulk upsert note metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertRepositoryMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertrepositorymetadata) | **PATCH** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/bulk | Bulk upsert repository metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmetadata) | **PATCH** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/bulk | Bulk upsert threat metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmodelassetmetadata) | **PATCH** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/bulk | Bulk upsert asset metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatModelAssets**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmodelassets) | **PUT** /threat_models/{threat_model_id}/assets/bulk | Bulk upsert assets
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatModelDocuments**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmodeldocuments) | **PUT** /threat_models/{threat_model_id}/documents/bulk | Bulk upsert documents
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatModelMetadata**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmodelmetadata) | **PATCH** /threat_models/{threat_model_id}/metadata/bulk | Bulk upsert threat model metadata
*ThreatModelSubResourcesApi* | [**bulkUpsertThreatModelRepositories**](docs/ThreatModelSubResourcesApi.md#bulkupsertthreatmodelrepositories) | **PUT** /threat_models/{threat_model_id}/repositories/bulk | Bulk upsert repositories
*ThreatModelSubResourcesApi* | [**createDiagramMetadata**](docs/ThreatModelSubResourcesApi.md#creatediagrammetadata) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Create diagram metadata
*ThreatModelSubResourcesApi* | [**createDocumentMetadata**](docs/ThreatModelSubResourcesApi.md#createdocumentmetadata) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Create document metadata
*ThreatModelSubResourcesApi* | [**createNoteMetadata**](docs/ThreatModelSubResourcesApi.md#createnotemetadata) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Create note metadata
*ThreatModelSubResourcesApi* | [**createRepositoryMetadata**](docs/ThreatModelSubResourcesApi.md#createrepositorymetadata) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Create source metadata
*ThreatModelSubResourcesApi* | [**createThreatMetadata**](docs/ThreatModelSubResourcesApi.md#createthreatmetadata) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Create threat metadata
*ThreatModelSubResourcesApi* | [**createThreatModelAsset**](docs/ThreatModelSubResourcesApi.md#createthreatmodelasset) | **POST** /threat_models/{threat_model_id}/assets | Create a new asset
*ThreatModelSubResourcesApi* | [**createThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#createthreatmodelassetmetadata) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Add metadata to an asset
*ThreatModelSubResourcesApi* | [**createThreatModelDiagram**](docs/ThreatModelSubResourcesApi.md#createthreatmodeldiagram) | **POST** /threat_models/{threat_model_id}/diagrams | Create a new diagram
*ThreatModelSubResourcesApi* | [**createThreatModelDocument**](docs/ThreatModelSubResourcesApi.md#createthreatmodeldocument) | **POST** /threat_models/{threat_model_id}/documents | Create a new document
*ThreatModelSubResourcesApi* | [**createThreatModelMetadata**](docs/ThreatModelSubResourcesApi.md#createthreatmodelmetadata) | **POST** /threat_models/{threat_model_id}/metadata | Create threat model metadata
*ThreatModelSubResourcesApi* | [**createThreatModelNote**](docs/ThreatModelSubResourcesApi.md#createthreatmodelnote) | **POST** /threat_models/{threat_model_id}/notes | Create a new note
*ThreatModelSubResourcesApi* | [**createThreatModelRepository**](docs/ThreatModelSubResourcesApi.md#createthreatmodelrepository) | **POST** /threat_models/{threat_model_id}/repositories | Create a new source reference
*ThreatModelSubResourcesApi* | [**createThreatModelThreat**](docs/ThreatModelSubResourcesApi.md#createthreatmodelthreat) | **POST** /threat_models/{threat_model_id}/threats | Create a new threat
*ThreatModelSubResourcesApi* | [**deleteDiagramMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deletediagrammetadatabykey) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Delete diagram metadata by key
*ThreatModelSubResourcesApi* | [**deleteDocumentMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deletedocumentmetadatabykey) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Delete document metadata by key
*ThreatModelSubResourcesApi* | [**deleteNoteMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deletenotemetadatabykey) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Delete note metadata by key
*ThreatModelSubResourcesApi* | [**deleteRepositoryMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deleterepositorymetadatabykey) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Delete source metadata by key
*ThreatModelSubResourcesApi* | [**deleteThreatMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deletethreatmetadatabykey) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Delete threat metadata by key
*ThreatModelSubResourcesApi* | [**deleteThreatModelAsset**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelasset) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id} | Delete an asset
*ThreatModelSubResourcesApi* | [**deleteThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelassetmetadata) | **DELETE** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Delete asset metadata
*ThreatModelSubResourcesApi* | [**deleteThreatModelDiagram**](docs/ThreatModelSubResourcesApi.md#deletethreatmodeldiagram) | **DELETE** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Delete a diagram
*ThreatModelSubResourcesApi* | [**deleteThreatModelDocument**](docs/ThreatModelSubResourcesApi.md#deletethreatmodeldocument) | **DELETE** /threat_models/{threat_model_id}/documents/{document_id} | Delete a document
*ThreatModelSubResourcesApi* | [**deleteThreatModelMetadataByKey**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelmetadatabykey) | **DELETE** /threat_models/{threat_model_id}/metadata/{key} | Delete threat model metadata by key
*ThreatModelSubResourcesApi* | [**deleteThreatModelNote**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelnote) | **DELETE** /threat_models/{threat_model_id}/notes/{note_id} | Delete a note
*ThreatModelSubResourcesApi* | [**deleteThreatModelRepository**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelrepository) | **DELETE** /threat_models/{threat_model_id}/repositories/{repository_id} | Delete a source reference
*ThreatModelSubResourcesApi* | [**deleteThreatModelThreat**](docs/ThreatModelSubResourcesApi.md#deletethreatmodelthreat) | **DELETE** /threat_models/{threat_model_id}/threats/{threat_id} | Delete a threat
*ThreatModelSubResourcesApi* | [**getDiagramMetadata**](docs/ThreatModelSubResourcesApi.md#getdiagrammetadata) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata | Get diagram metadata
*ThreatModelSubResourcesApi* | [**getDiagramMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getdiagrammetadatabykey) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Get diagram metadata by key
*ThreatModelSubResourcesApi* | [**getDiagramModel**](docs/ThreatModelSubResourcesApi.md#getdiagrammodel) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id}/model | Get minimal diagram model for automated analysis
*ThreatModelSubResourcesApi* | [**getDocumentMetadata**](docs/ThreatModelSubResourcesApi.md#getdocumentmetadata) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata | Get document metadata
*ThreatModelSubResourcesApi* | [**getDocumentMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getdocumentmetadatabykey) | **GET** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Get document metadata by key
*ThreatModelSubResourcesApi* | [**getNoteMetadata**](docs/ThreatModelSubResourcesApi.md#getnotemetadata) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata | Get note metadata
*ThreatModelSubResourcesApi* | [**getNoteMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getnotemetadatabykey) | **GET** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Get note metadata by key
*ThreatModelSubResourcesApi* | [**getRepositoryMetadata**](docs/ThreatModelSubResourcesApi.md#getrepositorymetadata) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata | Get source metadata
*ThreatModelSubResourcesApi* | [**getRepositoryMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getrepositorymetadatabykey) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Get source metadata by key
*ThreatModelSubResourcesApi* | [**getThreatMetadata**](docs/ThreatModelSubResourcesApi.md#getthreatmetadata) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata | Get threat metadata
*ThreatModelSubResourcesApi* | [**getThreatMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getthreatmetadatabykey) | **GET** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Get threat metadata by key
*ThreatModelSubResourcesApi* | [**getThreatModelAsset**](docs/ThreatModelSubResourcesApi.md#getthreatmodelasset) | **GET** /threat_models/{threat_model_id}/assets/{asset_id} | Get a specific asset
*ThreatModelSubResourcesApi* | [**getThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#getthreatmodelassetmetadata) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata | Get all metadata for an asset
*ThreatModelSubResourcesApi* | [**getThreatModelAssetMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getthreatmodelassetmetadatabykey) | **GET** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Get specific metadata for an asset
*ThreatModelSubResourcesApi* | [**getThreatModelAssets**](docs/ThreatModelSubResourcesApi.md#getthreatmodelassets) | **GET** /threat_models/{threat_model_id}/assets | List assets in a threat model
*ThreatModelSubResourcesApi* | [**getThreatModelDiagram**](docs/ThreatModelSubResourcesApi.md#getthreatmodeldiagram) | **GET** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Get a specific diagram
*ThreatModelSubResourcesApi* | [**getThreatModelDiagrams**](docs/ThreatModelSubResourcesApi.md#getthreatmodeldiagrams) | **GET** /threat_models/{threat_model_id}/diagrams | List threat model diagrams
*ThreatModelSubResourcesApi* | [**getThreatModelDocument**](docs/ThreatModelSubResourcesApi.md#getthreatmodeldocument) | **GET** /threat_models/{threat_model_id}/documents/{document_id} | Get a specific document
*ThreatModelSubResourcesApi* | [**getThreatModelDocuments**](docs/ThreatModelSubResourcesApi.md#getthreatmodeldocuments) | **GET** /threat_models/{threat_model_id}/documents | List documents in a threat model
*ThreatModelSubResourcesApi* | [**getThreatModelMetadata**](docs/ThreatModelSubResourcesApi.md#getthreatmodelmetadata) | **GET** /threat_models/{threat_model_id}/metadata | Get threat model metadata
*ThreatModelSubResourcesApi* | [**getThreatModelMetadataByKey**](docs/ThreatModelSubResourcesApi.md#getthreatmodelmetadatabykey) | **GET** /threat_models/{threat_model_id}/metadata/{key} | Get threat model metadata by key
*ThreatModelSubResourcesApi* | [**getThreatModelNote**](docs/ThreatModelSubResourcesApi.md#getthreatmodelnote) | **GET** /threat_models/{threat_model_id}/notes/{note_id} | Get a specific note
*ThreatModelSubResourcesApi* | [**getThreatModelNotes**](docs/ThreatModelSubResourcesApi.md#getthreatmodelnotes) | **GET** /threat_models/{threat_model_id}/notes | List notes in a threat model
*ThreatModelSubResourcesApi* | [**getThreatModelRepositories**](docs/ThreatModelSubResourcesApi.md#getthreatmodelrepositories) | **GET** /threat_models/{threat_model_id}/repositories | List sources in a threat model
*ThreatModelSubResourcesApi* | [**getThreatModelRepository**](docs/ThreatModelSubResourcesApi.md#getthreatmodelrepository) | **GET** /threat_models/{threat_model_id}/repositories/{repository_id} | Get a specific source reference
*ThreatModelSubResourcesApi* | [**getThreatModelThreat**](docs/ThreatModelSubResourcesApi.md#getthreatmodelthreat) | **GET** /threat_models/{threat_model_id}/threats/{threat_id} | Get a specific threat
*ThreatModelSubResourcesApi* | [**getThreatModelThreats**](docs/ThreatModelSubResourcesApi.md#getthreatmodelthreats) | **GET** /threat_models/{threat_model_id}/threats | List threats in a threat model
*ThreatModelSubResourcesApi* | [**patchThreatModelDiagram**](docs/ThreatModelSubResourcesApi.md#patchthreatmodeldiagram) | **PATCH** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Partially update a diagram
*ThreatModelSubResourcesApi* | [**patchThreatModelThreat**](docs/ThreatModelSubResourcesApi.md#patchthreatmodelthreat) | **PATCH** /threat_models/{threat_model_id}/threats/{threat_id} | Partially update a threat
*ThreatModelSubResourcesApi* | [**restoreAsset**](docs/ThreatModelSubResourcesApi.md#restoreasset) | **POST** /threat_models/{threat_model_id}/assets/{asset_id}/restore | Restore a soft-deleted asset
*ThreatModelSubResourcesApi* | [**restoreDiagram**](docs/ThreatModelSubResourcesApi.md#restorediagram) | **POST** /threat_models/{threat_model_id}/diagrams/{diagram_id}/restore | Restore a soft-deleted diagram
*ThreatModelSubResourcesApi* | [**restoreDocument**](docs/ThreatModelSubResourcesApi.md#restoredocument) | **POST** /threat_models/{threat_model_id}/documents/{document_id}/restore | Restore a soft-deleted document
*ThreatModelSubResourcesApi* | [**restoreNote**](docs/ThreatModelSubResourcesApi.md#restorenote) | **POST** /threat_models/{threat_model_id}/notes/{note_id}/restore | Restore a soft-deleted note
*ThreatModelSubResourcesApi* | [**restoreRepository**](docs/ThreatModelSubResourcesApi.md#restorerepository) | **POST** /threat_models/{threat_model_id}/repositories/{repository_id}/restore | Restore a soft-deleted repository
*ThreatModelSubResourcesApi* | [**restoreThreat**](docs/ThreatModelSubResourcesApi.md#restorethreat) | **POST** /threat_models/{threat_model_id}/threats/{threat_id}/restore | Restore a soft-deleted threat
*ThreatModelSubResourcesApi* | [**updateDiagramMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updatediagrammetadatabykeyoperation) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id}/metadata/{key} | Update diagram metadata by key
*ThreatModelSubResourcesApi* | [**updateDocumentMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updatedocumentmetadatabykey) | **PUT** /threat_models/{threat_model_id}/documents/{document_id}/metadata/{key} | Update document metadata by key
*ThreatModelSubResourcesApi* | [**updateNoteMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updatenotemetadatabykey) | **PUT** /threat_models/{threat_model_id}/notes/{note_id}/metadata/{key} | Update note metadata by key
*ThreatModelSubResourcesApi* | [**updateRepositoryMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updaterepositorymetadatabykey) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id}/metadata/{key} | Update source metadata by key
*ThreatModelSubResourcesApi* | [**updateThreatMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updatethreatmetadatabykeyoperation) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id}/metadata/{key} | Update threat metadata by key
*ThreatModelSubResourcesApi* | [**updateThreatModelAsset**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelasset) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id} | Update an asset
*ThreatModelSubResourcesApi* | [**updateThreatModelAssetMetadata**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelassetmetadata) | **PUT** /threat_models/{threat_model_id}/assets/{asset_id}/metadata/{key} | Update asset metadata
*ThreatModelSubResourcesApi* | [**updateThreatModelDiagram**](docs/ThreatModelSubResourcesApi.md#updatethreatmodeldiagram) | **PUT** /threat_models/{threat_model_id}/diagrams/{diagram_id} | Update a diagram
*ThreatModelSubResourcesApi* | [**updateThreatModelDocument**](docs/ThreatModelSubResourcesApi.md#updatethreatmodeldocument) | **PUT** /threat_models/{threat_model_id}/documents/{document_id} | Update a document
*ThreatModelSubResourcesApi* | [**updateThreatModelMetadataByKey**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelmetadatabykey) | **PUT** /threat_models/{threat_model_id}/metadata/{key} | Update threat model metadata by key
*ThreatModelSubResourcesApi* | [**updateThreatModelNote**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelnote) | **PUT** /threat_models/{threat_model_id}/notes/{note_id} | Update a note
*ThreatModelSubResourcesApi* | [**updateThreatModelRepository**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelrepository) | **PUT** /threat_models/{threat_model_id}/repositories/{repository_id} | Update a source reference
*ThreatModelSubResourcesApi* | [**updateThreatModelThreat**](docs/ThreatModelSubResourcesApi.md#updatethreatmodelthreat) | **PUT** /threat_models/{threat_model_id}/threats/{threat_id} | Update a threat
*ThreatModelsApi* | [**createThreatModel**](docs/ThreatModelsApi.md#createthreatmodel) | **POST** /threat_models | Create a threat model
*ThreatModelsApi* | [**deleteThreatModel**](docs/ThreatModelsApi.md#deletethreatmodel) | **DELETE** /threat_models/{threat_model_id} | Delete a threat model
*ThreatModelsApi* | [**getThreatModel**](docs/ThreatModelsApi.md#getthreatmodel) | **GET** /threat_models/{threat_model_id} | Retrieve a threat model
*ThreatModelsApi* | [**listThreatModels**](docs/ThreatModelsApi.md#listthreatmodels) | **GET** /threat_models | List threat models
*ThreatModelsApi* | [**patchThreatModel**](docs/ThreatModelsApi.md#patchthreatmodel) | **PATCH** /threat_models/{threat_model_id} | Partially update a threat model
*ThreatModelsApi* | [**restoreThreatModel**](docs/ThreatModelsApi.md#restorethreatmodel) | **POST** /threat_models/{threat_model_id}/restore | Restore a soft-deleted threat model
*ThreatModelsApi* | [**updateThreatModel**](docs/ThreatModelsApi.md#updatethreatmodel) | **PUT** /threat_models/{threat_model_id} | Update a threat model
*ThreatsApi* | [**bulkDeleteThreatModelThreats**](docs/ThreatsApi.md#bulkdeletethreatmodelthreats) | **DELETE** /threat_models/{threat_model_id}/threats/bulk | Bulk DELETE threats
*ThreatsApi* | [**bulkPatchThreatModelThreats**](docs/ThreatsApi.md#bulkpatchthreatmodelthreats) | **PATCH** /threat_models/{threat_model_id}/threats/bulk | Bulk PATCH threats
*UserAccountApi* | [**createCurrentUserPreferences**](docs/UserAccountApi.md#createcurrentuserpreferences) | **POST** /me/preferences | Create user preferences
*UserAccountApi* | [**getCurrentUserPreferences**](docs/UserAccountApi.md#getcurrentuserpreferences) | **GET** /me/preferences | Get user preferences
*UserAccountApi* | [**updateCurrentUserPreferences**](docs/UserAccountApi.md#updatecurrentuserpreferences) | **PUT** /me/preferences | Update user preferences
*UsersApi* | [**deleteUserAccount**](docs/UsersApi.md#deleteuseraccount) | **DELETE** /me | Delete authenticated user account and all data
*UsersApi* | [**logoutCurrentUser**](docs/UsersApi.md#logoutcurrentuser) | **POST** /me/logout | Logout current user
*UsersApi* | [**transferCurrentUserOwnership**](docs/UsersApi.md#transfercurrentuserownership) | **POST** /me/transfer | Transfer ownership of all owned resources
*WebSocketApi* | [**getWsTicket**](docs/WebSocketApi.md#getwsticket) | **GET** /ws/ticket | Get a WebSocket authentication ticket
*WebhooksApi* | [**createWebhookSubscription**](docs/WebhooksApi.md#createwebhooksubscription) | **POST** /webhooks/subscriptions | Create webhook subscription
*WebhooksApi* | [**deleteWebhookSubscription**](docs/WebhooksApi.md#deletewebhooksubscription) | **DELETE** /webhooks/subscriptions/{webhook_id} | Delete webhook subscription
*WebhooksApi* | [**getWebhookDelivery**](docs/WebhooksApi.md#getwebhookdelivery) | **GET** /webhooks/deliveries/{delivery_id} | Get webhook delivery
*WebhooksApi* | [**getWebhookSubscription**](docs/WebhooksApi.md#getwebhooksubscription) | **GET** /webhooks/subscriptions/{webhook_id} | Get webhook subscription
*WebhooksApi* | [**listWebhookDeliveries**](docs/WebhooksApi.md#listwebhookdeliveries) | **GET** /webhooks/deliveries | List webhook deliveries
*WebhooksApi* | [**listWebhookSubscriptions**](docs/WebhooksApi.md#listwebhooksubscriptions) | **GET** /webhooks/subscriptions | List webhook subscriptions
*WebhooksApi* | [**testWebhookSubscription**](docs/WebhooksApi.md#testwebhooksubscription) | **POST** /webhooks/subscriptions/{webhook_id}/test | Test webhook subscription


### Models

- [AddGroupMemberRequest](docs/AddGroupMemberRequest.md)
- [AddonInvocationQuota](docs/AddonInvocationQuota.md)
- [AddonParameter](docs/AddonParameter.md)
- [AddonQuotaUpdate](docs/AddonQuotaUpdate.md)
- [AddonResponse](docs/AddonResponse.md)
- [AdminGroup](docs/AdminGroup.md)
- [AdminGroupListResponse](docs/AdminGroupListResponse.md)
- [AdminUser](docs/AdminUser.md)
- [AdminUserListResponse](docs/AdminUserListResponse.md)
- [ApiInfo](docs/ApiInfo.md)
- [ApiInfoApi](docs/ApiInfoApi.md)
- [ApiInfoHealth](docs/ApiInfoHealth.md)
- [ApiInfoOperator](docs/ApiInfoOperator.md)
- [ApiInfoService](docs/ApiInfoService.md)
- [ApiInfoStatus](docs/ApiInfoStatus.md)
- [Asset](docs/Asset.md)
- [AssetBase](docs/AssetBase.md)
- [AssetInput](docs/AssetInput.md)
- [AuditActor](docs/AuditActor.md)
- [AuditEntry](docs/AuditEntry.md)
- [AuthTokenResponse](docs/AuthTokenResponse.md)
- [Authorization](docs/Authorization.md)
- [BaseDiagram](docs/BaseDiagram.md)
- [BaseDiagramImage](docs/BaseDiagramImage.md)
- [BaseDiagramInput](docs/BaseDiagramInput.md)
- [BulkDeleteThreatModelThreats200Response](docs/BulkDeleteThreatModelThreats200Response.md)
- [BulkPatchRequest](docs/BulkPatchRequest.md)
- [BulkPatchRequestPatchesInner](docs/BulkPatchRequestPatchesInner.md)
- [CVSSScore](docs/CVSSScore.md)
- [Cell](docs/Cell.md)
- [CellData](docs/CellData.md)
- [ClientConfig](docs/ClientConfig.md)
- [ClientConfigFeatures](docs/ClientConfigFeatures.md)
- [ClientConfigLimits](docs/ClientConfigLimits.md)
- [ClientConfigOperator](docs/ClientConfigOperator.md)
- [ClientConfigUi](docs/ClientConfigUi.md)
- [ClientCredentialInfo](docs/ClientCredentialInfo.md)
- [ClientCredentialResponse](docs/ClientCredentialResponse.md)
- [CollaborationSession](docs/CollaborationSession.md)
- [ColorPaletteEntry](docs/ColorPaletteEntry.md)
- [ComponentHealth](docs/ComponentHealth.md)
- [CreateAddonRequest](docs/CreateAddonRequest.md)
- [CreateAdminGroupRequest](docs/CreateAdminGroupRequest.md)
- [CreateAutomationAccountRequest](docs/CreateAutomationAccountRequest.md)
- [CreateAutomationAccountResponse](docs/CreateAutomationAccountResponse.md)
- [CreateCurrentUserClientCredentialRequest](docs/CreateCurrentUserClientCredentialRequest.md)
- [CreateDiagramCollaborationSession409Response](docs/CreateDiagramCollaborationSession409Response.md)
- [CreateDiagramRequest](docs/CreateDiagramRequest.md)
- [CreateThreatModelFromSurveyResponse](docs/CreateThreatModelFromSurveyResponse.md)
- [DeletionChallenge](docs/DeletionChallenge.md)
- [DfdDiagram](docs/DfdDiagram.md)
- [DfdDiagramAllOfCells](docs/DfdDiagramAllOfCells.md)
- [DfdDiagramInput](docs/DfdDiagramInput.md)
- [DfdDiagramInputAllOfCells](docs/DfdDiagramInputAllOfCells.md)
- [DiagramListItem](docs/DiagramListItem.md)
- [DiagramListItemImage](docs/DiagramListItemImage.md)
- [Document](docs/Document.md)
- [DocumentBase](docs/DocumentBase.md)
- [DocumentInput](docs/DocumentInput.md)
- [Edge](docs/Edge.md)
- [EdgeAttrs](docs/EdgeAttrs.md)
- [EdgeAttrsLine](docs/EdgeAttrsLine.md)
- [EdgeAttrsLineSourceMarker](docs/EdgeAttrsLineSourceMarker.md)
- [EdgeAttrsLineTargetMarker](docs/EdgeAttrsLineTargetMarker.md)
- [EdgeConnector](docs/EdgeConnector.md)
- [EdgeConnectorOneOf](docs/EdgeConnectorOneOf.md)
- [EdgeConnectorOneOfArgs](docs/EdgeConnectorOneOfArgs.md)
- [EdgeLabel](docs/EdgeLabel.md)
- [EdgeLabelAttrs](docs/EdgeLabelAttrs.md)
- [EdgeLabelAttrsText](docs/EdgeLabelAttrsText.md)
- [EdgeLabelPosition](docs/EdgeLabelPosition.md)
- [EdgeLabelPositionOneOf](docs/EdgeLabelPositionOneOf.md)
- [EdgeLabelPositionOneOfOffset](docs/EdgeLabelPositionOneOfOffset.md)
- [EdgeLabelPositionOneOfOffsetOneOf](docs/EdgeLabelPositionOneOfOffsetOneOf.md)
- [EdgeLabelPositionOneOfOptions](docs/EdgeLabelPositionOneOfOptions.md)
- [EdgeRouter](docs/EdgeRouter.md)
- [EdgeRouterOneOf](docs/EdgeRouterOneOf.md)
- [EdgeRouterOneOfArgs](docs/EdgeRouterOneOfArgs.md)
- [EdgeTerminal](docs/EdgeTerminal.md)
- [ErrorDetails](docs/ErrorDetails.md)
- [ExchangeOAuthCodeRequest](docs/ExchangeOAuthCodeRequest.md)
- [ExtendedAsset](docs/ExtendedAsset.md)
- [GetAuthProviders200Response](docs/GetAuthProviders200Response.md)
- [GetAuthProviders200ResponseProvidersInner](docs/GetAuthProviders200ResponseProvidersInner.md)
- [GetCurrentUser200Response](docs/GetCurrentUser200Response.md)
- [GetJWKS200Response](docs/GetJWKS200Response.md)
- [GetJWKS200ResponseKeysInner](docs/GetJWKS200ResponseKeysInner.md)
- [GetOAuthAuthorizationServerMetadata200Response](docs/GetOAuthAuthorizationServerMetadata200Response.md)
- [GetOpenIDConfiguration200Response](docs/GetOpenIDConfiguration200Response.md)
- [GetProviderGroups200Response](docs/GetProviderGroups200Response.md)
- [GetProviderGroups200ResponseGroupsInner](docs/GetProviderGroups200ResponseGroupsInner.md)
- [GetSAMLProviders200Response](docs/GetSAMLProviders200Response.md)
- [GetUserAPIQuota429Response](docs/GetUserAPIQuota429Response.md)
- [GroupMember](docs/GroupMember.md)
- [GroupMemberListResponse](docs/GroupMemberListResponse.md)
- [IntrospectToken200Response](docs/IntrospectToken200Response.md)
- [IntrospectToken500Response](docs/IntrospectToken500Response.md)
- [InvocationResponse](docs/InvocationResponse.md)
- [InvokeAddonRequest](docs/InvokeAddonRequest.md)
- [InvokeAddonResponse](docs/InvokeAddonResponse.md)
- [JsonPatchDocumentInner](docs/JsonPatchDocumentInner.md)
- [ListAddonQuotasResponse](docs/ListAddonQuotasResponse.md)
- [ListAddonsResponse](docs/ListAddonsResponse.md)
- [ListAssetsResponse](docs/ListAssetsResponse.md)
- [ListAuditTrailResponse](docs/ListAuditTrailResponse.md)
- [ListClientCredentialsResponse](docs/ListClientCredentialsResponse.md)
- [ListDiagramsResponse](docs/ListDiagramsResponse.md)
- [ListDocumentsResponse](docs/ListDocumentsResponse.md)
- [ListInvocationsResponse](docs/ListInvocationsResponse.md)
- [ListNotesResponse](docs/ListNotesResponse.md)
- [ListProjectsResponse](docs/ListProjectsResponse.md)
- [ListRepositoriesResponse](docs/ListRepositoriesResponse.md)
- [ListSurveyResponsesResponse](docs/ListSurveyResponsesResponse.md)
- [ListSurveysResponse](docs/ListSurveysResponse.md)
- [ListTeamsResponse](docs/ListTeamsResponse.md)
- [ListThreatModelsResponse](docs/ListThreatModelsResponse.md)
- [ListThreatsResponse](docs/ListThreatsResponse.md)
- [ListTriageNotesResponse](docs/ListTriageNotesResponse.md)
- [ListUserQuotasResponse](docs/ListUserQuotasResponse.md)
- [ListWebhookDeliveriesResponse](docs/ListWebhookDeliveriesResponse.md)
- [ListWebhookQuotasResponse](docs/ListWebhookQuotasResponse.md)
- [ListWebhookSubscriptionsResponse](docs/ListWebhookSubscriptionsResponse.md)
- [Metadata](docs/Metadata.md)
- [MigrateSystemSettings200Response](docs/MigrateSystemSettings200Response.md)
- [MinimalCell](docs/MinimalCell.md)
- [MinimalDiagramModel](docs/MinimalDiagramModel.md)
- [MinimalEdge](docs/MinimalEdge.md)
- [MinimalNode](docs/MinimalNode.md)
- [ModelError](docs/ModelError.md)
- [MyGroupListResponse](docs/MyGroupListResponse.md)
- [Node](docs/Node.md)
- [NodeAllOfPosition](docs/NodeAllOfPosition.md)
- [NodeAllOfSize](docs/NodeAllOfSize.md)
- [NodeAttrs](docs/NodeAttrs.md)
- [NodeAttrsBody](docs/NodeAttrsBody.md)
- [NodeAttrsText](docs/NodeAttrsText.md)
- [Note](docs/Note.md)
- [NoteBase](docs/NoteBase.md)
- [NoteInput](docs/NoteInput.md)
- [NoteListItem](docs/NoteListItem.md)
- [OAuthProtectedResourceMetadata](docs/OAuthProtectedResourceMetadata.md)
- [Participant](docs/Participant.md)
- [Point](docs/Point.md)
- [PortConfiguration](docs/PortConfiguration.md)
- [PortConfigurationGroupsValue](docs/PortConfigurationGroupsValue.md)
- [PortConfigurationItemsInner](docs/PortConfigurationItemsInner.md)
- [Principal](docs/Principal.md)
- [ProcessSAMLLogout200Response](docs/ProcessSAMLLogout200Response.md)
- [Project](docs/Project.md)
- [ProjectBase](docs/ProjectBase.md)
- [ProjectListItem](docs/ProjectListItem.md)
- [ProjectStatus](docs/ProjectStatus.md)
- [ReencryptSystemSettings200Response](docs/ReencryptSystemSettings200Response.md)
- [ReencryptSystemSettings200ResponseErrorsInner](docs/ReencryptSystemSettings200ResponseErrorsInner.md)
- [RelatedProject](docs/RelatedProject.md)
- [RelatedTeam](docs/RelatedTeam.md)
- [RelationshipType](docs/RelationshipType.md)
- [Repository](docs/Repository.md)
- [RepositoryBase](docs/RepositoryBase.md)
- [RepositoryBaseParameters](docs/RepositoryBaseParameters.md)
- [RepositoryInput](docs/RepositoryInput.md)
- [ResponsibleParty](docs/ResponsibleParty.md)
- [RollbackResponse](docs/RollbackResponse.md)
- [SAMLProviderInfo](docs/SAMLProviderInfo.md)
- [Survey](docs/Survey.md)
- [SurveyBase](docs/SurveyBase.md)
- [SurveyInput](docs/SurveyInput.md)
- [SurveyListItem](docs/SurveyListItem.md)
- [SurveyResponse](docs/SurveyResponse.md)
- [SurveyResponseBase](docs/SurveyResponseBase.md)
- [SurveyResponseCreateRequest](docs/SurveyResponseCreateRequest.md)
- [SurveyResponseInput](docs/SurveyResponseInput.md)
- [SurveyResponseListItem](docs/SurveyResponseListItem.md)
- [SurveySettings](docs/SurveySettings.md)
- [SystemSetting](docs/SystemSetting.md)
- [SystemSettingUpdate](docs/SystemSettingUpdate.md)
- [TMListItem](docs/TMListItem.md)
- [Team](docs/Team.md)
- [TeamBase](docs/TeamBase.md)
- [TeamListItem](docs/TeamListItem.md)
- [TeamMember](docs/TeamMember.md)
- [TeamMemberRole](docs/TeamMemberRole.md)
- [TeamStatus](docs/TeamStatus.md)
- [Threat](docs/Threat.md)
- [ThreatBase](docs/ThreatBase.md)
- [ThreatBulkUpdateItem](docs/ThreatBulkUpdateItem.md)
- [ThreatInput](docs/ThreatInput.md)
- [ThreatModel](docs/ThreatModel.md)
- [ThreatModelBase](docs/ThreatModelBase.md)
- [ThreatModelInput](docs/ThreatModelInput.md)
- [TokenRefreshRequest](docs/TokenRefreshRequest.md)
- [TokenRevocationRequest](docs/TokenRevocationRequest.md)
- [TransferOwnershipRequest](docs/TransferOwnershipRequest.md)
- [TransferOwnershipResult](docs/TransferOwnershipResult.md)
- [TransferOwnershipResultSurveyResponsesTransferred](docs/TransferOwnershipResultSurveyResponsesTransferred.md)
- [TransferOwnershipResultThreatModelsTransferred](docs/TransferOwnershipResultThreatModelsTransferred.md)
- [TriageNote](docs/TriageNote.md)
- [TriageNoteBase](docs/TriageNoteBase.md)
- [TriageNoteInput](docs/TriageNoteInput.md)
- [TriageNoteListItem](docs/TriageNoteListItem.md)
- [UpdateAdminGroupRequest](docs/UpdateAdminGroupRequest.md)
- [UpdateAdminUserRequest](docs/UpdateAdminUserRequest.md)
- [UpdateDiagramMetadataByKeyRequest](docs/UpdateDiagramMetadataByKeyRequest.md)
- [UpdateInvocationStatusRequest](docs/UpdateInvocationStatusRequest.md)
- [UpdateInvocationStatusResponse](docs/UpdateInvocationStatusResponse.md)
- [UpdateThreatMetadataByKeyRequest](docs/UpdateThreatMetadataByKeyRequest.md)
- [User](docs/User.md)
- [UserAPIQuota](docs/UserAPIQuota.md)
- [UserGroupMembership](docs/UserGroupMembership.md)
- [UserQuotaUpdate](docs/UserQuotaUpdate.md)
- [UserWithAdminStatus](docs/UserWithAdminStatus.md)
- [WebhookDelivery](docs/WebhookDelivery.md)
- [WebhookEventType](docs/WebhookEventType.md)
- [WebhookQuota](docs/WebhookQuota.md)
- [WebhookQuotaUpdate](docs/WebhookQuotaUpdate.md)
- [WebhookSubscription](docs/WebhookSubscription.md)
- [WebhookSubscriptionInput](docs/WebhookSubscriptionInput.md)
- [WebhookTestRequest](docs/WebhookTestRequest.md)
- [WebhookTestResponse](docs/WebhookTestResponse.md)
- [WsTicketResponse](docs/WsTicketResponse.md)

### Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
#### bearerAuth


- **Type**: HTTP Bearer Token authentication (JWT)

## About

This TypeScript SDK client supports the [Fetch API](https://fetch.spec.whatwg.org/)
and is automatically generated by the
[OpenAPI Generator](https://openapi-generator.tech) project:

- API version: `1.3.0`
- Package version: `1.0.0`
- Generator version: `7.21.0`
- Build package: `org.openapitools.codegen.languages.TypeScriptFetchClientCodegen`

The generated npm module supports the following:

- Environments
  * Node.js
  * Webpack
  * Browserify
- Language levels
  * ES5 - you must have a Promises/A+ library installed
  * ES6
- Module systems
  * CommonJS
  * ES6 module system

For more information, please visit [https://github.com/ericfitz/tmi](https://github.com/ericfitz/tmi)

## Development

### Building

To build the TypeScript source code, you need to have Node.js and npm installed.
After cloning the repository, navigate to the project directory and run:

```bash
npm install
npm run build
```

### Publishing

Once you've built the package, you can publish it to npm:

```bash
npm publish
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
