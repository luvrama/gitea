# routers

**475 endpoints**

## DELETE /api/v1/admin/actions/runners/{runner_id}

Delete a global action runner by ID

- **Auth:** bearer
- **ID:** `ep-116`

### Controller

- admin (serves)
- admin.DeleteRunner (serves)
- admin.DeleteRunner (data_flow)
- Action.DeleteRunner (calls)
- user.DeleteRunner (calls)
- admin.GetRunner (calls)

### Services

- shared.getRunnerByID (calls)
- convert.ToActionRunner (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

## DELETE /api/v1/admin/hooks/{id}

Delete a system or default webhook and its associated hook tasks

- **Auth:** bearer (admin required)
- **ID:** `ep-095`

### Controller

- admin (serves)
- admin.DeleteHook (serves)
- admin.DeleteHook (data_flow)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Delete count=0 (webhook not found) (handles_error)
- 500 Transaction fails (handles_error)

## DELETE /api/v1/admin/unadopted/{owner}/{repo}

Deletes unadopted repository files from the filesystem

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-109`

### Controller

- admin (serves)
- admin.DeleteUnadoptedRepository (serves)
- admin.DeleteUnadoptedRepository (data_flow)

### Services

- repo_service.DeleteUnadoptedRepository (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- repository.root_path (configured_by)

### Models

- Repository (uses_model)
- User (uses_model)

## DELETE /api/v1/admin/users/{username}

Delete a user account, optionally purging all owned data

- **Auth:** bearer
- **ID:** `ep-100`

### Controller

- admin (serves)
- admin.DeleteUser (serves)
- admin.DeleteUser (data_flow)

### Services

- user_service.DeleteUser (serves)
- deleteUser (internal) (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- USER_DELETE_WITH_COMMENTS_MAX_TIME (configured_by)

### Models

- user_model.User (uses_model)

### Error Handling

- 422 User owns repositories (handles_error)
- 422 User belongs to organizations (handles_error)
- 422 User owns packages (handles_error)

## DELETE /api/v1/admin/users/{username}/badges

Remove badges from a user by slug

- **Auth:** bearer
- **ID:** `ep-122`

### Controller

- admin (serves)
- admin.DeleteUserBadges (serves)
- admin.DeleteUserBadges (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.listUserOrgs (calls)

### Services

- user_model.RemoveUserBadges (serves)
- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- Badge (uses_model)
- UserBadge (uses_model)

## DELETE /api/v1/admin/users/{username}/keys/{id}

Delete a user's public SSH key

- **Auth:** bearer
- **ID:** `ep-102`

### Controller

- admin (serves)
- admin.DeleteUserPublicKey (serves)
- admin.DeleteUserPublicKey (data_flow)
- user.DeletePublicKey (calls)
- repo.DeleteDeploykey (calls)

### Services

- asymkey_service.DeletePublicKey (serves)
- asymkey_service.RewriteAllPublicKeys (data_flow)
- asymkey_service.DeleteDeployKey (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- asymkey_model.PublicKey (uses_model)

### Error Handling

- 404 Key ID not found (handles_error)
- 403 No permission to delete key (handles_error)

## DELETE /api/v1/orgs/{org}

Delete an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-034`

### Controller

- organization (serves)
- org.Delete (serves)
- org.Delete (data_flow)
- org.Rename (calls)
- org.Edit (calls)

### Services

- org.DeleteOrganization (serves)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.OrgUser (uses_model)
- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- organization.TeamUnit (uses_model)

### Error Handling

- 500 Org still has repositories (handles_error)
- 500 Org still has packages (handles_error)

## DELETE /api/v1/orgs/{org}/actions/runners/{runner_id}

Delete an org-level runner

- **Auth:** bearer
- **ID:** `ep-050`

### Controller

- organization (serves)
- Action.DeleteRunner (serves)
- Action.DeleteRunner (data_flow)
- admin.DeleteRunner (calls)
- user.DeleteRunner (calls)
- admin.GetRunner (calls)
- Action.UpdateRunner (calls)
- admin.UpdateRunner (calls)
- user.UpdateRunner (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)

### Services

- shared.getRunnerByID (data_flow)
- convert.ToActionRunner (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 404 runner ID not found in DB (handles_error)
- 404 runner not editable in org context (handles_error)

## DELETE /api/v1/orgs/{org}/actions/secrets/{secretname}

Delete a secret in an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-041`

### Controller

- organization (serves)
- org.Action.DeleteSecret (serves)
- org.Action.DeleteSecret (data_flow)
- org.DeleteOrgRepos (calls)
- org.UpdateAvatar (calls)
- org.DeleteAvatar (calls)
- org.Action.ListActionsSecrets (calls)
- org.Action.CreateOrUpdateSecret (calls)
- user.DeleteSecret (calls)
- Action.DeleteSecret (calls)

### Services

- secret_service.DeleteSecretByName (data_flow)
- secret_service (serves)
- org.deleteOrgReposBackground (calls)
- user_service.UploadAvatar (calls)
- user_service.DeleteAvatar (calls)
- secret_service.CreateOrUpdateSecret (calls)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)

### Models

- secret_model.Secret (uses_model)

## DELETE /api/v1/orgs/{org}/actions/variables/{variablename}

Delete an org-level variable by name

- **Auth:** bearer
- **ID:** `ep-045`

### Controller

- organization (serves)
- org.Action.DeleteVariable (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.DeleteVariableByName (serves)
- actions_service.GetVariable (serves)
- org_service.DeleteTeam (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionVariable (uses_model)

## DELETE /api/v1/orgs/{org}/avatar

Delete the avatar of an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-038`

### Controller

- organization (serves)
- org.DeleteAvatar (serves)
- org.DeleteAvatar (data_flow)
- org.DeleteOrgRepos (calls)
- org.UpdateAvatar (calls)
- org.Action.ListActionsSecrets (calls)
- org.Action.CreateOrUpdateSecret (calls)
- org.Action.DeleteSecret (calls)
- user.DeleteAvatar (calls)

### Services

- user_service.DeleteAvatar (data_flow)
- user_service (serves)
- org.deleteOrgReposBackground (calls)
- user_service.UploadAvatar (calls)
- secret_service.CreateOrUpdateSecret (calls)
- secret_service.DeleteSecretByName (calls)

### External APIs

- Avatar Storage Backend (integrates)

### Models

- user_model.User (uses_model)

## DELETE /api/v1/orgs/{org}/blocks/{username}

Unblock a user from the organization

- **Auth:** token
- **ID:** `ep-090`

### Controller

- organization (serves)
- org.UnblockUser (serves)
- org.UnblockUser (data_flow)
- user.UnblockUser (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)
- org.CheckUserBlock (calls)
- user.CheckUserBlock (calls)
- org.BlockUser (calls)
- user.BlockUser (calls)

### Services

- shared.UnblockUser (data_flow)
- user_service.UnblockUser (serves)
- shared.CheckUserBlock (calls)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 400 Unblock not permitted (not blocked or insufficient perms) (handles_error)
- 400 Target is an organization (handles_error)

## DELETE /api/v1/orgs/{org}/hooks/{id}

Delete an organization webhook

- **Auth:** token
- **ID:** `ep-081`

### Controller

- organization (serves)
- org.DeleteHook (serves)
- org.DeleteHook (data_flow)
- user.DeleteHook (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- webhook.Webhook (uses_model)

## DELETE /api/v1/orgs/{org}/labels/{id}

Delete a label from an organization

- **Auth:** token
- **ID:** `ep-086`

### Controller

- organization (serves)
- org.DeleteLabel (serves)
- org.DeleteLabel (data_flow)
- repo.DeleteLabel (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- issues_model.Label (uses_model)

## DELETE /api/v1/orgs/{org}/members/{username}

Remove a member from an organization. Removes from all teams, deletes repo access, unwatches repos.

- **Auth:** bearer
- **ID:** `ep-076`

### Controller

- organization (serves)
- org.DeleteMember (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- org_service.RemoveOrgUser (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)
- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- access_model.Access (uses_model)

### Error Handling

- 500 User is last owner of org (handles_error)
- 204 User not in org_user (handles_error)

## DELETE /api/v1/orgs/{org}/public_members/{username}

Conceal a user's membership in an organization. Sets is_public=false on the org_user record.

- **Auth:** bearer
- **ID:** `ep-075`

### Controller

- organization (serves)
- org.ConcealMember (serves)
- org.ListMembers (calls)
- listMembers (calls)
- orgAssignment(false, true) (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

## DELETE /api/v1/orgs/{org}/repos

Delete all repositories in an organization (async background deletion)

- **Auth:** bearer (reqToken + reqOrgOwnership + AccessTokenScopeCategoryRepository)
- **ID:** `ep-036`

### Controller

- organization (serves)
- org.DeleteOrgRepos (serves)
- org.DeleteOrgRepos (data_flow)
- org.UpdateAvatar (calls)
- org.DeleteAvatar (calls)
- org.Action.ListActionsSecrets (calls)
- org.Action.CreateOrUpdateSecret (calls)
- org.Action.DeleteSecret (calls)

### Services

- org.deleteOrgReposBackground (data_flow)
- repo_service (serves)
- user_service.UploadAvatar (calls)
- user_service.DeleteAvatar (calls)
- secret_service.CreateOrUpdateSecret (calls)
- secret_service.DeleteSecretByName (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- repo_model.Repository (uses_model)

## DELETE /api/v1/packages/{owner}/{type}/{name}

Delete a package and all its versions

- **Auth:** bearer
- **ID:** `ep-201`

### Controller

- package (serves)
- packages.DeletePackage (serves)
- packages.DeletePackage (data_flow)
- packages.GetPackage (calls)

### Services

- packages_service.RemovePackage (serves)
- convert.ToPackage (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- packages.limit_total_owner_count (configured_by)

### Models

- packages_model.Package (uses_model)
- packages_model.PackageVersion (uses_model)
- packages_model.PackageFile (uses_model)
- packages_model.PackageDescriptor (uses_model)

### Error Handling

- 404 Package not found (middleware) (handles_error)
- 500 Error during RemovePackage transaction (handles_error)

## DELETE /api/v1/packages/{owner}/{type}/{name}/{version}

Delete a specific version of a package

- **Auth:** bearer
- **ID:** `ep-202`

### Controller

- package (serves)
- packages.DeletePackageVersion (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.DeletePackageVersion (data_flow)
- packages.ListPackageFiles (calls)
- packages.ListPackageVersions (calls)
- packages.GetLatestPackageVersion (calls)
- packages.LinkPackage (calls)
- packages.UnlinkPackage (calls)

### Services

- packages_service.RemovePackageVersion (serves)
- packages_service.LinkToRepository (calls)
- packages_service.UnlinkFromRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.PackageVersion (uses_model)
- packages_model.PackageFile (uses_model)
- packages_model.PackageDescriptor (uses_model)

### Error Handling

- 404 Version not found in middleware (handles_error)
- 500 RemovePackageVersion fails (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}

Delete a repository

- **Auth:** bearer
- **ID:** `ep-370`

### Controller

- repository (serves)
- repo.Delete (serves)
- repo.Delete (data_flow)

### Services

- repo_service.DeleteRepository (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- repo_model.Repository (uses_model)

### Error Handling

- 403 User cannot delete (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}

Marks a specific artifact for deletion (v4 only)

- **Auth:** bearer
- **ID:** `ep-297`

### Controller

- repository (serves)
- repo.DeleteArtifact (serves)
- DeleteArtifact (v4 check + mark) (data_flow)
- GetArtifact (v4 check) (calls)
- DownloadArtifact (expiry check) (calls)

### Services

- actions_service.IsArtifactV4 (serves)
- convert.ToActionArtifact (calls)
- actions_service.DownloadArtifactV4ServeDirect (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- ActionArtifact (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

Delete a repo-level runner

- **Auth:** bearer
- **ID:** `ep-275`

### Controller

- repository (serves)
- Action.DeleteRunner (serves)
- Action.DeleteRunner (data_flow)
- admin.DeleteRunner (calls)
- user.DeleteRunner (calls)
- admin.GetRunner (calls)

### Services

- shared.runners (serves)
- shared.getRunnerByID (calls)
- convert.ToActionRunner (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- ActionRunner (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/actions/runs/{run}

Deletes a workflow run including all logs and artifacts

- **Auth:** bearer
- **ID:** `ep-294`

### Controller

- repository (serves)
- repo.DeleteActionRun (serves)
- DeleteActionRun (validation) (data_flow)

### Services

- actions_service.DeleteRun (serves)
- convert.ToActionWorkflowRun (calls)

### External APIs

- Object Storage (Minio/Azure/Local) (integrates)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- actions.artifact_storage.STORAGE_TYPE (configured_by)

### Models

- ActionArtifact (uses_model)
- ActionRun (uses_model)
- ActionRunJob (uses_model)
- ActionTask (uses_model)

### Error Handling

- 404 Run not found by repo+id (handles_error)
- 400 Run status is not done (handles_error)
- 500 DeleteRun fails (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}

Delete a secret in a repository

- **Auth:** bearer
- **ID:** `ep-266`

### Controller

- repository (serves)
- Action.DeleteSecret (serves)
- Action.DeleteSecret (data_flow)
- org.Action.DeleteSecret (calls)
- user.DeleteSecret (calls)

### Services

- secret_service.DeleteSecretByName (data_flow)
- secret_service (services/secrets) (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- secret_model.Secret (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

Delete a repo-level variable by name

- **Auth:** bearer
- **ID:** `ep-268`

### Controller

- repository (serves)
- Action.DeleteVariable (serves)
- Action.DeleteVariable (data_flow)
- user.DeleteVariable (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.DeleteVariableByName (data_flow)
- actions_service (services/actions) (serves)
- actions_service.GetVariable (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- actions_model.ActionVariable (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/avatar

Delete repository custom avatar

- **Auth:** bearer
- **ID:** `ep-263`

### Controller

- repository (serves)
- repo.DeleteAvatar (serves)
- repo.DeleteAvatar (data_flow)

### Services

- repo_service.DeleteAvatar (data_flow)
- repo_service (services/repository) (serves)

### External APIs

- File Storage (RepoAvatars) (integrates)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- repo_model.Repository (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/branch_protections/{name}

Delete a specific branch protection rule for the repository

- **Auth:** bearer
- **ID:** `ep-316`

### Controller

- repository (serves)
- repo.DeleteBranchProtection (serves)
- repo.DeleteBranchProtection (data_flow)

### Models

- git_model.ProtectedBranch (uses_model)

### Error Handling

- 404 bp == nil || bp.RepoID != repo.ID (handles_error)
- 500 DeleteProtectedBranch fails (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/branches/{branch}

Delete a specific branch from a repository

- **Auth:** bearer
- **ID:** `ep-307`

### Controller

- repository (serves)
- repo.DeleteBranch (serves)
- repo.DeleteBranch (data_flow)
- repo.ListBranches (calls)
- repo.ListBranchProtections (calls)

### Services

- repo_module.SyncRepoBranches (data_flow)
- repo_service.DeleteBranch (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- git_model.Branch (uses_model)
- git_model.ProtectedBranch (uses_model)

### Error Handling

- 404 Branch does not exist in git (handles_error)
- 403 Trying to delete default or PR target branch (handles_error)
- 403 Branch has protection rule (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

Remove a collaborator from a repository

- **Auth:** bearer
- **ID:** `ep-253`

### Controller

- repository (serves)
- repo.DeleteCollaborator (serves)
- repo.DeleteCollaborator (data_flow)

### Services

- repo_service.DeleteCollaboration (serves)

### Business Rules

- Org repo creation requires user to have create permission in org (enforces)

### Models

- repo_model.Collaboration (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/contents/{filepath}

- **Auth:** none
- **ID:** `ep-397`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/hooks/git/{id}

- **Auth:** none
- **ID:** `ep-389`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/hooks/{id}

Delete a webhook from a repository

- **Auth:** bearer
- **ID:** `ep-326`

### Controller

- repository (serves)
- repo.DeleteHook (serves)
- repo.DeleteHook (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Hook ID not found for repo (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}

- **Auth:** none
- **ID:** `ep-442`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

- **Auth:** none
- **ID:** `ep-428`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

Remove a reaction from a comment of an issue

- **Auth:** token
- **ID:** `ep-302`

### Controller

- issue (serves)
- repo.DeleteIssueCommentReaction (serves)
- repo.DeleteIssueCommentReaction (data_flow)
- repo.changeIssueCommentReaction (data_flow)
- repo.PostIssueCommentReaction (calls)

### Services

- issue_service.CreateCommentReaction (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Comment (uses_model)
- issues_model.Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}

- **Auth:** none
- **ID:** `ep-474`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

Delete an issue attachment

- **Auth:** token
- **ID:** `ep-261`

### Controller

- issue (serves)
- repo.DeleteIssueAttachment (serves)
- repo.DeleteIssueAttachment (data_flow)
- repo.EditIssueAttachment (calls)

### Services

- attachment_service.UpdateAttachment (calls)

### External APIs

- Object Storage (Attachments) (integrates)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- attachment.ENABLED (configured_by)

### Models

- repo_model.Attachment (uses_model)
- issues_model.Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

Unblock the issue given in the body by the issue in the URL path

- **Auth:** bearer
- **ID:** `ep-213`

### Controller

- issue (serves)
- repo.RemoveIssueBlocking (serves)
- repo.RemoveIssueBlocking (data_flow)
- repo.getParamsIssue (data_flow)
- repo.getFormIssue (data_flow)
- repo.removeIssueDependency (data_flow)
- repo.CreateIssueDependency (calls)
- repo.RemoveIssueDependency (calls)
- repo.GetIssueBlocks (calls)
- repo.CreateIssueBlocking (calls)
- repo.getPermissionForRepo (calls)
- repo.createIssueDependency (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)

### Services

- access_model.GetDoerRepoPermission (serves)
- convert.ToRepo (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- service.DEFAULT_ENABLE_DEPENDENCIES (configured_by)
- service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- IssueMeta (uses_model)

### Error Handling

- 500 Blocking relationship does not exist (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}

- **Auth:** none
- **ID:** `ep-443`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

Remove a dependency from the issue in the URL

- **Auth:** bearer
- **ID:** `ep-210`

### Controller

- issue (serves)
- repo.RemoveIssueDependency (serves)
- repo.RemoveIssueDependency (data_flow)
- repo.getParamsIssue (data_flow)
- repo.getFormIssue (data_flow)
- repo.removeIssueDependency (data_flow)
- repo.CreateIssueDependency (calls)
- repo.GetIssueBlocks (calls)
- repo.CreateIssueBlocking (calls)
- repo.RemoveIssueBlocking (calls)
- repo.getPermissionForRepo (calls)
- repo.createIssueDependency (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)

### Services

- access_model.GetDoerRepoPermission (serves)
- convert.ToRepo (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- service.DEFAULT_ENABLE_DEPENDENCIES (configured_by)
- service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- IssueMeta (uses_model)

### Error Handling

- 500 Dependency does not exist to remove (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels

Remove all labels from an issue

- **Auth:** bearer
- **ID:** `ep-339`

### Controller

- issue (serves)
- repo.ClearIssueLabels (serves)
- repo.ClearIssueLabels (data_flow)

### Services

- issue_service.ClearLabels (data_flow)
- issue_service (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- issues_model.Label (uses_model)
- issues_model.IssueLabel (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}

Remove a label from an issue

- **Auth:** bearer
- **ID:** `ep-337`

### Controller

- issue (serves)
- repo.DeleteIssueLabel (serves)
- repo.DeleteIssueLabel (data_flow)

### Services

- issue_service.RemoveLabel (data_flow)
- issue_service (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- issues_model.Label (uses_model)
- issues_model.IssueLabel (uses_model)

### Error Handling

- 404 Invalid issue index (handles_error)
- 422 Invalid label ID (handles_error)
- 403 No write access (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/lock

Unlock a previously locked issue

- **Auth:** bearer
- **ID:** `ep-320`

### Controller

- issue (serves)
- repo.UnlockIssue (serves)
- repo.UnlockIssue (data_flow)

### Services

- issues_model.UnlockIssue (serves)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/pin

Unpin an issue from the repository

- **Auth:** bearer
- **ID:** `ep-377`

### Controller

- issue (serves)
- repo.UnpinIssue (serves)
- repo.UnpinIssue (data_flow)

### Services

- issues_model.UnpinIssue (data_flow)
- issues_model (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- issues_model.IssuePin (uses_model)
- issues_model.Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

Remove a reaction from an issue

- **Auth:** token
- **ID:** `ep-305`

### Controller

- issue (serves)
- repo.DeleteIssueReaction (serves)
- repo.DeleteIssueReaction (data_flow)
- repo.changeIssueReaction (data_flow)
- repo.PostIssueReaction (calls)

### Services

- issue_service.CreateIssueReaction (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete

- **Auth:** none
- **ID:** `ep-384`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}

Unsubscribe a user from an issue

- **Auth:** token
- **ID:** `ep-219`

### Controller

- issue (serves)
- repo.DelIssueSubscription (serves)
- repo.DelIssueSubscription (data_flow)
- repo.AddIssueSubscription (calls)

### Services

- repo.setIssueSubscription (data_flow)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- issues.IssueWatch (uses_model)
- issues.Issue (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times

- **Auth:** none
- **ID:** `ep-409`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times/{id}

- **Auth:** none
- **ID:** `ep-410`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/keys/{id}

Delete a deploy key from a repository

- **Auth:** bearer
- **ID:** `ep-343`

### Controller

- repository (serves)
- repo.DeleteDeploykey (serves)
- repo.DeleteDeploykey (data_flow)
- admin.DeleteUserPublicKey (calls)

### Services

- asymkey_service.DeleteDeployKey (data_flow)
- asymkey_service.RewriteAllPublicKeys (data_flow)
- asymkey_service (serves)
- asymkey_service.DeletePublicKey (calls)

### Business Rules

- Org repo creation requires user to have create permission in org (enforces)

### Config

- SSH.StartBuiltinServer (configured_by)

### Models

- asymkey_model.DeployKey (uses_model)
- asymkey_model.PublicKey (uses_model)

### Error Handling

- 403 Key belongs to different repo (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/labels/{id}

Delete a label from a repository

- **Auth:** bearer
- **ID:** `ep-361`

### Controller

- issue (serves)
- repo.DeleteLabel (serves)
- repo.DeleteLabel (data_flow)
- org.DeleteLabel (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- issues_model.Label (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/milestones/{id}

- **Auth:** none
- **ID:** `ep-468`

### Controller

- issue (serves)

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

Cancel a scheduled auto-merge for a pull request

- **Auth:** bearer
- **ID:** `ep-231`

### Controller

- repository (serves)
- repo.CancelScheduledAutoMerge (serves)
- repo.CancelScheduledAutoMerge (data_flow)

### Services

- pull_service.IsUserAllowedToMerge (data_flow)
- automerge.RemoveScheduledAutoMerge (data_flow)
- pull_service (serves)
- automerge (serves)

### Business Rules

- Cancel auto-merge requires being the scheduler or having merge permission (enforces)

### Models

- issues_model.PullRequest (uses_model)
- pull_model.AutoMerge (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers

- **Auth:** none
- **ID:** `ep-461`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

- **Auth:** none
- **ID:** `ep-457`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/push_mirrors/{name}

Deletes a push mirror from a repository by its remote name

- **Auth:** bearer
- **ID:** `ep-239`

### Controller

- repository (serves)
- repo.DeletePushMirrorByRemoteName (serves)
- repo.DeletePushMirrorByRemoteName (data_flow)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- mirror.ENABLED (configured_by)

### Models

- repo_model.PushMirror (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/releases/tags/{tag}

Delete a release from a repository by tag name

- **Auth:** bearer (write access to releases required)
- **ID:** `ep-345`

### Controller

- repository (serves)
- repo.DeleteReleaseByTag (serves)
- DeleteReleaseByTag (data_flow)
- GetReleaseByTag (calls)
- repo.DeleteRelease (calls)
- repo.GetLatestRelease (calls)

### Services

- release_service.DeleteReleaseByID (data_flow)
- release_service (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- repo_model.Release (uses_model)

### Error Handling

- 404 Tag name not found (handles_error)
- 422 Tag is protected (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/releases/{id}

Delete a release (keeps the git tag, deletes attachments from storage)

- **Auth:** bearer (write:repository scope)
- **ID:** `ep-245`

### Controller

- repository (serves)
- repo.DeleteRelease (serves)
- repo.DeleteRelease (data_flow)
- GetReleaseByTag (calls)
- DeleteReleaseByTag (calls)

### Services

- release_service.DeleteReleaseByID (serves)

### External APIs

- Git Repository (local filesystem) (integrates)

### Business Rules

- Pin position must be >= 1 (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- repo_model.Release (uses_model)
- repo_model.Attachment (uses_model)
- git_model.ProtectedTag (uses_model)

### Error Handling

- 422 Tag is protected and user not allowed (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

Delete a release attachment and its file from storage

- **Auth:** token (write access required)
- **ID:** `ep-356`

### Controller

- repository (serves)
- repo.DeleteReleaseAttachment (serves)
- repo.DeleteReleaseAttachment (data_flow)
- repo.GetReleaseAttachment (calls)
- repo.CreateReleaseAttachment (calls)
- repo.EditReleaseAttachment (calls)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- repo.EditIssueAttachment (calls)
- repo.DeleteIssueAttachment (calls)

### Services

- attachment_service.UploadAttachmentForRelease (calls)
- attachment_service.UpdateAttachment (calls)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- issue_service.ChangeContent (calls)

### External APIs

- Object Storage (Attachments) (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- repo_model.Attachment (uses_model)
- repo_model.Release (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/subscription

Unwatch a repo (unsubscribe from notifications)

- **Auth:** bearer
- **ID:** `ep-198`

### Controller

- repository (serves)
- user.Unwatch (serves)
- user.Unwatch (data_flow)
- user.Watch (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- repo_model.Watch (uses_model)

### Error Handling

- 500 DB error in WatchRepo (handles_error)

## DELETE /api/v1/repos/{owner}/{repo}/tag_protections/{id}

- **Auth:** none
- **ID:** `ep-423`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/tags/{tag}

- **Auth:** none
- **ID:** `ep-418`

### Controller

- repository (serves)

## DELETE /api/v1/repos/{owner}/{repo}/teams/{team}

Delete a team from a repository

- **Auth:** bearer
- **ID:** `ep-332`

### Controller

- repository (serves)
- repo.DeleteTeam (serves)
- repo.DeleteTeam (data_flow)
- repo.changeRepoTeam (data_flow)
- repo.AddTeam (calls)
- repo.IsTeam (calls)
- reqTeamMembership (calls)

### Services

- repo_service.RemoveRepositoryFromTeam (serves)
- repo_service.HasRepository (serves)
- repo_service.TeamAddRepository (calls)
- convert.ToTeam (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/topics/{topic}

Delete a topic from a repository

- **Auth:** bearer (write access required)
- **ID:** `ep-350`

### Controller

- repository (serves)
- repo.DeleteTopic (serves)
- DeleteTopic (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- repo_model.Topic (uses_model)
- repo_model.RepoTopic (uses_model)

## DELETE /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

- **Auth:** none
- **ID:** `ep-447`

### Controller

- repository (serves)

## DELETE /api/v1/teams/{id}

Delete a team

- **Auth:** token
- **ID:** `ep-059`

### Controller

- organization (serves)
- org.DeleteTeam (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- org.ListMembers (calls)
- listMembers (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)

### Services

- org_service.DeleteTeam (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- convert.ToTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Pin position must be >= 1 (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUnit (uses_model)

## DELETE /api/v1/teams/{id}/members/{username}

Remove a team member

- **Auth:** token
- **ID:** `ep-063`

### Controller

- organization (serves)
- org.RemoveTeamMember (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- org.ListMembers (calls)
- listMembers (calls)

### Services

- org_service.RemoveTeamMember (serves)
- org_service.AddTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- user_model.User (uses_model)

### Error Handling

- 500 removing last owner team member (handles_error)

## DELETE /api/v1/teams/{id}/repos/{org}/{repo}

Remove a repository from a team (does not delete the repository)

- **Auth:** token
- **ID:** `ep-067`

### Controller

- organization (serves)
- org.RemoveTeamRepository (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership() (data_flow)
- org.RemoveTeamRepository (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- repo.changeRepoTeam (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- repo.AddTeam (calls)
- repo.DeleteTeam (calls)

### Services

- repo_service.RemoveRepositoryFromTeam (serves)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- repo_service.TeamAddRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)
- repo_model.Repository (uses_model)

## DELETE /api/v1/user/actions/runners/{runner_id}

Delete a user-level action runner

- **Auth:** bearer
- **ID:** `ep-178`

### Controller

- user (serves)
- user.DeleteRunner (serves)
- user.DeleteRunner (data_flow)
- Action.DeleteRunner (calls)
- admin.DeleteRunner (calls)
- admin.GetRunner (calls)

### Services

- shared.getRunnerByID (calls)
- convert.ToActionRunner (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

## DELETE /api/v1/user/actions/secrets/{secretname}

Deletes a secret in the user scope

- **Auth:** bearer
- **ID:** `ep-131`

### Controller

- user (serves)
- user.DeleteSecret (serves)
- user.DeleteSecret (data_flow)
- org.Action.DeleteSecret (calls)
- Action.DeleteSecret (calls)

### Services

- secret_service.DeleteSecretByName (data_flow)
- secret_service (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- Secret (uses_model)

### Error Handling

- 400 Invalid argument (handles_error)
- 404 Secret does not exist (handles_error)

## DELETE /api/v1/user/actions/variables/{variablename}

Deletes a user-level variable created by current doer

- **Auth:** bearer
- **ID:** `ep-134`

### Controller

- user (serves)
- user.DeleteVariable (serves)
- user.DeleteVariable (data_flow)
- Action.DeleteVariable (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.DeleteVariableByName (data_flow)
- actions_service (serves)
- actions_service.GetVariable (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- ActionVariable (uses_model)

## DELETE /api/v1/user/applications/oauth2/{id}

Delete an OAuth2 application by ID

- **Auth:** bearer
- **ID:** `ep-169`

### Controller

- user (serves)
- user.DeleteOauth2Application (serves)
- user.DeleteOauth2Application (data_flow)

### Services

- auth_model.DeleteOAuth2Application (data_flow)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- OAuth2.DefaultApplications (configured_by)

### Models

- auth.OAuth2Application (uses_model)

### Error Handling

- 404 App ID not found in DB (handles_error)
- 500 Attempting to delete a builtin app (handles_error)

## DELETE /api/v1/user/avatar

Deletes the current user's custom avatar

- **Auth:** bearer
- **ID:** `ep-129`

### Controller

- user (serves)
- user.DeleteAvatar (serves)
- user.DeleteAvatar (data_flow)
- org.DeleteAvatar (calls)

### Services

- user_service.DeleteAvatar (data_flow)
- user_service (serves)

### External APIs

- Avatar Storage Backend (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- avatar.STORAGE_TYPE (configured_by)

### Models

- User (uses_model)

### Error Handling

- 500 DB update or storage delete failure (handles_error)

## DELETE /api/v1/user/blocks/{username}

Unblock a user

- **Auth:** bearer
- **ID:** `ep-193`

### Controller

- user (serves)
- user.UnblockUser (serves)
- user.UnblockUser (data_flow)
- org.UnblockUser (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)

### Services

- shared.UnblockUser (serves)
- user_service.UnblockUser (serves)
- shared.CheckUserBlock (calls)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 404 GetUserByName returns error (handles_error)
- 400 CanUnblockUser returns false (handles_error)
- 400 blockee is organization (handles_error)

## DELETE /api/v1/user/emails

Delete email addresses from the authenticated user

- **Auth:** bearer
- **ID:** `ep-182`

### Controller

- user (serves)
- user.DeleteEmail (serves)
- user.DeleteEmail (data_flow)

### Services

- user_service.DeleteEmailAddresses (serves)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- EmailAddress (uses_model)

### Error Handling

- 404 Email not found for user (handles_error)

## DELETE /api/v1/user/following/{username}

Unfollow a user

- **Auth:** bearer
- **ID:** `ep-146`

### Controller

- user (serves)
- user.Unfollow (serves)
- user.Unfollow (data_flow)

### Services

- user_model (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- user_model.Follow (uses_model)
- user_model.User (uses_model)

## DELETE /api/v1/user/gpg_keys/{id}

Remove a GPG key belonging to the authenticated user

- **Auth:** bearer
- **ID:** `ep-189`

### Controller

- user (serves)
- user.DeleteGPGKey (serves)
- user.DeleteGPGKey (data_flow)

### Services

- asymkey_model.DeleteGPGKey (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- admin.USER_DISABLED_FEATURES / admin.EXTERNAL_USER_DISABLE_FEATURES (configured_by)
- setting.UserFeatureManageGPGKeys (configured_by)

### Models

- asymkey_model.GPGKey (uses_model)
- asymkey_model.GPGKeyImport (uses_model)

### Error Handling

- 404 manage_gpg_keys in disabled features (handles_error)
- 500 Delete operation fails (handles_error)

## DELETE /api/v1/user/hooks/{id}

Delete a webhook owned by the authenticated user

- **Auth:** bearer
- **ID:** `ep-151`

### Controller

- user (serves)
- user.DeleteHook (serves)
- user.DeleteHook (data_flow)
- org.DeleteHook (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- setting.DisableWebhooks (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Webhook not found by owner_id+id (handles_error)

## DELETE /api/v1/user/keys/{id}

Delete a public SSH key for the authenticated user

- **Auth:** bearer
- **ID:** `ep-161`

### Controller

- user (serves)
- user.DeletePublicKey (serves)
- user.DeletePublicKey (data_flow)
- admin.DeleteUserPublicKey (calls)
- repo.DeleteDeploykey (calls)

### Services

- asymkey_service.DeletePublicKey (serves)
- asymkey_service.RewriteAllPublicKeys (serves)
- asymkey_service.DeleteDeployKey (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- admin.USER_DISABLED_FEATURES (configured_by)
- admin.EXTERNAL_USER_DISABLE_FEATURES (configured_by)
- ssh.START_BUILTIN_SERVER (configured_by)

### Models

- asymkey_model.PublicKey (uses_model)
- auth.Source (uses_model)

### Error Handling

- 404 IsFeatureDisabledWithLoginType returns true (handles_error)
- 404 Key ID not found (handles_error)
- 403 Key is managed by external auth source (handles_error)
- 403 User is not admin and not key owner (handles_error)

## DELETE /api/v1/user/starred/{owner}/{repo}

Unstar the given repo for the authenticated user

- **Auth:** bearer
- **ID:** `ep-156`

### Controller

- user (serves)
- user.Unstar (serves)
- user.Unstar (data_flow)
- user.Star (calls)

### Services

- repo_model.StarRepo (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- repo_model.Star (uses_model)

### Error Handling

- 500 StarRepo fails (handles_error)

## DELETE /api/v1/users/{username}/tokens/{token}

Delete an access token by ID or name

- **Auth:** basic_or_reverse_proxy+token
- **ID:** `ep-166`

### Controller

- user (serves)
- user.DeleteAccessToken (serves)
- user.DeleteAccessToken (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.SuccessfulTokensCacheSize (configured_by)

### Models

- auth_model.AccessToken (uses_model)

### Error Handling

- 404 Token ID or name doesn't exist for user (handles_error)
- 422 Multiple tokens share the same name (handles_error)

## GET /api/v1/admin/actions/jobs

List all workflow jobs across all repositories (admin only)

- **Auth:** bearer
- **ID:** `ep-105`

### Controller

- admin (serves)
- admin.ListWorkflowJobs (serves)
- admin.ListWorkflowJobs (data_flow)
- Action.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (data_flow)
- actions_service.RerunWorkflowRunJobs (calls)

### Models

- actions_model.ActionRunJob (uses_model)

## GET /api/v1/admin/actions/runners

List all global action runners with optional disabled filter

- **Auth:** bearer
- **ID:** `ep-114`

### Controller

- admin (serves)
- admin.ListRunners (serves)
- admin.ListRunners (data_flow)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- admin.GetRunner (calls)

### Services

- convert.ToActionRunner (serves)
- shared.getRunnerByID (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 500 FindAndCount fails (handles_error)

## GET /api/v1/admin/actions/runners/{runner_id}

Get a specific global action runner by ID

- **Auth:** bearer
- **ID:** `ep-115`

### Controller

- admin (serves)
- admin.GetRunner (serves)
- admin.GetRunner (data_flow)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- Action.DeleteRunner (calls)
- admin.DeleteRunner (calls)
- user.DeleteRunner (calls)
- Action.UpdateRunner (calls)
- admin.UpdateRunner (calls)
- user.UpdateRunner (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- shared.getRunnerByID (data_flow)
- convert.ToActionRunner (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 404 Runner ID not found (handles_error)
- 500 GetRunnerByID fails (handles_error)

## GET /api/v1/admin/actions/runs

Lists all workflow runs across all repositories (admin-level)

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-106`

### Controller

- admin (serves)
- admin.ListWorkflowRuns (serves)
- admin.ListWorkflowRuns (data_flow)
- Action.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)
- GetWorkflowRun (calls)
- getCurrentRepoActionRunJobsByID (calls)
- RerunWorkflowJob (find job) (calls)

### Services

- shared.ListRuns (serves)
- convert.ToActionWorkflowRun (data_flow)
- actions_service.RerunWorkflowRunJobs (calls)
- actions_service.GetFailedJobsForRerun (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- ActionRun (uses_model)
- User (uses_model)

### Error Handling

- 400 Unknown status string in query (handles_error)
- 500 Actor username doesn't exist (handles_error)
- 500 Database query failure (handles_error)

## GET /api/v1/admin/cron

Lists all registered cron tasks with their schedule and execution info

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-110`

### Controller

- admin (serves)
- admin.ListCronTasks (serves)
- admin.ListCronTasks (data_flow)

### Services

- cron.ListTasks (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

## GET /api/v1/admin/emails

List all email addresses in the system with pagination

- **Auth:** bearer
- **ID:** `ep-118`

### Controller

- admin (serves)
- admin.GetAllEmails (serves)
- admin.GetAllEmails (data_flow)
- admin.SearchEmail (calls)

### Services

- convert.ToEmailSearch (serves)
- user_model.SearchEmails (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- EmailAddress (uses_model)

## GET /api/v1/admin/emails/search

Search all emails by keyword (searches name, full_name, email)

- **Auth:** bearer
- **ID:** `ep-119`

### Controller

- admin (serves)
- admin.SearchEmail (serves)
- admin.SearchEmail (data_flow)
- admin.GetAllEmails (data_flow)

### Services

- convert.ToEmailSearch (serves)
- user_model.SearchEmails (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- EmailAddress (uses_model)

## GET /api/v1/admin/hooks

List system and/or default webhooks with pagination

- **Auth:** bearer (admin required)
- **ID:** `ep-091`

### Controller

- admin (serves)
- admin.ListHooks (serves)
- admin.ListHooks (data_flow)
- org.GetAll (calls)
- user.Search (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)
- user_model.SearchUsers (calls)
- convert.ToOrganization (calls)
- convert.ToUser (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- AppURL (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 500 GetGlobalWebhooks fails (handles_error)
- 500 HeaderAuthorization() fails (handles_error)

## GET /api/v1/admin/hooks/{id}

Get a single system or default webhook by ID

- **Auth:** bearer (admin required)
- **ID:** `ep-092`

### Controller

- admin (serves)
- admin.GetHook (serves)
- admin.GetHook (data_flow)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Webhook ID not found with repo_id=0, owner_id=0 (handles_error)
- 500 Database query fails (handles_error)

## GET /api/v1/admin/orgs

List all organizations with pagination

- **Auth:** bearer (admin required)
- **ID:** `ep-097`

### Controller

- admin (serves)
- admin.GetAllOrgs (serves)
- admin.GetAllOrgs (data_flow)
- admin.SearchUsers (calls)
- org.GetAll (calls)
- admin.ListHooks (calls)
- user.Search (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- user_model.SearchUsers (data_flow)
- convert.ToOrganization (serves)
- convert.ToUser (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- mailer.SendRegisterNotifyMail (calls)
- shared.ListBlocks (calls)
- pull_service.GetReviewers (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)

## GET /api/v1/admin/unadopted

Lists unadopted repositories (git repos on disk not tracked in DB)

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-107`

### Controller

- admin (serves)
- admin.ListUnadoptedRepositories (serves)
- admin.ListUnadoptedRepositories (data_flow)

### Services

- repo_service.ListUnadoptedRepositories (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- repository.root_path (configured_by)
- database.iterate_buffer_size (configured_by)

### Models

- Repository (uses_model)
- User (uses_model)

## GET /api/v1/admin/users

Search users with various filter conditions (admin only)

- **Auth:** bearer
- **ID:** `ep-103`

### Controller

- admin (serves)
- admin.SearchUsers (serves)
- admin.SearchUsers (data_flow)
- admin.GetAllOrgs (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- org.GetAll (calls)
- admin.ListHooks (calls)
- user.Search (calls)
- user.UpdateUserSettings (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- user_model.SearchUsers (data_flow)
- convert.ToUser (data_flow)
- convert.ToOrganization (calls)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- shared.ListBlocks (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- pull_service.GetReviewers (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)

### Models

- user_model.User (uses_model)

## GET /api/v1/admin/users/{username}/badges

List all badges belonging to a user

- **Auth:** bearer
- **ID:** `ep-120`

### Controller

- admin (serves)
- admin.ListUserBadges (serves)
- admin.ListUserBadges (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.listUserOrgs (calls)

### Services

- user_model.GetUserBadges (serves)
- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- Badge (uses_model)
- UserBadge (uses_model)

## GET /api/v1/gitignore/templates

Returns a list of all gitignore template names

- **Auth:** none
- **ID:** `ep-011`

### Controller

- miscellaneous (serves)
- misc.ListGitignoresTemplates (serves)
- misc.ListGitignoresTemplates (data_flow)

## GET /api/v1/gitignore/templates/{name}

Returns information about a specific gitignore template

- **Auth:** none
- **ID:** `ep-012`

### Controller

- miscellaneous (serves)
- misc.GetGitignoreTemplateInfo (serves)
- misc.GetGitignoreTemplateInfo (data_flow)
- misc.GetLicenseTemplateInfo (calls)

### Services

- options.Gitignore (serves)
- options.License (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- setting.CustomPath (configured_by)

### Models

- GitignoreTemplateInfo (uses_model)

### Error Handling

- 404 Gitignore template name doesn't exist in any layer (handles_error)

## GET /api/v1/label/templates

Returns a list of all label template display names

- **Auth:** none
- **ID:** `ep-002`

### Controller

- miscellaneous (serves)
- misc.ListLabelTemplates (serves)
- misc.ListLabelTemplates (data_flow)

### Config

- repository.PREFERRED_LICENSES (configured_by)

## GET /api/v1/label/templates/{name}

Returns all labels in a specific label template

- **Auth:** none
- **ID:** `ep-003`

### Controller

- miscellaneous (serves)
- misc.GetLabelTemplate (serves)
- misc.GetLabelTemplate (data_flow)

### Services

- convert.ToLabelTemplateList (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- label.Label (uses_model)
- api.LabelTemplate (uses_model)

### Error Handling

- 404 Template display name not in map (handles_error)

## GET /api/v1/licenses

Returns a list of all license templates with metadata

- **Auth:** none
- **ID:** `ep-013`

### Controller

- miscellaneous (serves)
- misc.ListLicenseTemplates (serves)
- misc.ListLicenseTemplates (data_flow)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- setting.AppURL (configured_by)
- setting.Repository.PreferredLicenses (configured_by)

### Models

- LicensesTemplateListEntry (uses_model)

## GET /api/v1/licenses/{name}

Returns full information about a specific license template including body text

- **Auth:** none
- **ID:** `ep-014`

### Controller

- miscellaneous (serves)
- misc.GetLicenseTemplateInfo (serves)
- misc.GetLicenseTemplateInfo (data_flow)
- misc.GetGitignoreTemplateInfo (calls)

### Services

- options.License (serves)
- options.Gitignore (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- setting.AppURL (configured_by)
- setting.CustomPath (configured_by)

### Models

- LicenseTemplateInfo (uses_model)

### Error Handling

- 404 License template name doesn't exist in any layer (handles_error)

## GET /api/v1/notifications

List current user's notification threads with filtering by status, subject type, and time range

- **Auth:** bearer (notification scope)
- **ID:** `ep-019`

### Controller

- notification (serves)
- notify.ListNotifications (serves)
- notify.ListRepoNotifications (set RepoID) (calls)
- notify.ReadNotifications (calls)
- notify.getThread (calls)

### Services

- convert.ToNotifications (serves)
- convert.ToNotificationThread (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- api.MAX_RESPONSE_ITEMS (configured_by)
- api.DEFAULT_PAGING_NUM (configured_by)

### Models

- Notification (uses_model)
- NotificationThread (uses_model)

### Error Handling

- 422 Invalid RFC3339 before/since parameter (handles_error)
- 500 DB connection failure or query error (handles_error)

## GET /api/v1/notifications/new

Check if unread notifications exist and return the count

- **Auth:** bearer (notification scope)
- **ID:** `ep-021`

### Controller

- notification (serves)
- notify.NewAvailable (serves)
- notify.ListRepoNotifications (set RepoID) (calls)
- notify.ReadNotifications (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- Notification (uses_model)
- NotificationCount (uses_model)

### Error Handling

- 422 DB connection failure or query error (handles_error)

## GET /api/v1/notifications/threads/{id}

Get notification thread by ID

- **Auth:** token
- **ID:** `ep-024`

### Controller

- notification (serves)
- notify.GetThread (serves)
- notify.getThread (data_flow)

### Services

- convert.ToNotificationThread (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- activities_model.Notification (uses_model)
- structs.NotificationThread (uses_model)

### Error Handling

- 404 Notification ID not found (handles_error)
- 403 User is not owner and not admin (handles_error)
- 500 DB error loading repo/issue/user (handles_error)

## GET /api/v1/orgs

Get list of all organizations visible to the current user

- **Auth:** optional (token enhances visibility)
- **ID:** `ep-029`

### Controller

- organization (serves)
- org.GetAll (serves)
- org.GetAll (data_flow)
- admin.ListHooks (calls)
- user.Search (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- user_model.SearchUsers (serves)
- convert.ToOrganization (data_flow)
- convert.ToUser (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- webhook_service.ToHook (calls)
- mailer.SendRegisterNotifyMail (calls)
- shared.ListBlocks (calls)
- pull_service.GetReviewers (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)

### Error Handling

- 500 SearchUsers fails (handles_error)

## GET /api/v1/orgs/{org}

Get details of a specific organization

- **Auth:** optional (affects email visibility)
- **ID:** `ep-031`

### Controller

- organization (serves)
- org.Get (serves)
- orgAssignment(true) (data_flow)
- org.Get (data_flow)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.SearchTeam (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- user.UpdateUserSettings (calls)

### Services

- organization.HasOrgOrUserVisible (serves)
- convert.ToOrganization (data_flow)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- user_service.UpdateUser (calls)
- feed_service.GetFeeds (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- convert.ToUser (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.OrgUser (uses_model)

## GET /api/v1/orgs/{org}/actions/jobs

Get org-level workflow jobs

- **Auth:** bearer
- **ID:** `ep-052`

### Controller

- organization (serves)
- Action.ListWorkflowJobs (serves)
- Action.ListWorkflowJobs (data_flow)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (data_flow)
- actions_service.RerunWorkflowRunJobs (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)
- ActionRun (uses_model)
- ActionRunJob (uses_model)

### Error Handling

- 400 unrecognized status filter value (handles_error)

## GET /api/v1/orgs/{org}/actions/runners

Get org-level runners list

- **Auth:** bearer
- **ID:** `ep-048`

### Controller

- organization (serves)
- org.Action.ListRunners (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- convert.ToActionRunner (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- ActionRunner (uses_model)

## GET /api/v1/orgs/{org}/actions/runners/{runner_id}

Get a specific org-level runner by ID

- **Auth:** bearer
- **ID:** `ep-049`

### Controller

- organization (serves)
- org.Action.GetRunner (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- admin.GetRunner (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- shared.getRunnerByID (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- ActionRunner (uses_model)

## GET /api/v1/orgs/{org}/actions/runs

Get org-level workflow runs

- **Auth:** bearer
- **ID:** `ep-053`

### Controller

- organization (serves)
- Action.ListWorkflowRuns (serves)
- Action.ListWorkflowRuns (data_flow)
- admin.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)
- GetWorkflowRun (calls)
- getCurrentRepoActionRunJobsByID (calls)
- RerunWorkflowJob (find job) (calls)

### Services

- shared.ListRuns (serves)
- convert.ToActionWorkflowRun (data_flow)
- actions_service.RerunWorkflowRunJobs (calls)
- actions_service.GetFailedJobsForRerun (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRun (uses_model)

### Error Handling

- 400 unrecognized status filter value (handles_error)
- 500 actor username does not exist (handles_error)

## GET /api/v1/orgs/{org}/actions/secrets

List an organization's actions secrets

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-039`

### Controller

- organization (serves)
- org.Action.ListActionsSecrets (serves)
- org.Action.ListActionsSecrets (data_flow)
- org.DeleteOrgRepos (calls)
- org.UpdateAvatar (calls)
- org.DeleteAvatar (calls)
- org.Action.CreateOrUpdateSecret (calls)
- org.Action.DeleteSecret (calls)

### Services

- org.deleteOrgReposBackground (calls)
- user_service.UploadAvatar (calls)
- user_service.DeleteAvatar (calls)
- secret_service.CreateOrUpdateSecret (calls)
- secret_service.DeleteSecretByName (calls)

### Models

- secret_model.Secret (uses_model)

## GET /api/v1/orgs/{org}/actions/variables

Get an org-level variables list

- **Auth:** bearer
- **ID:** `ep-043`

### Controller

- organization (serves)
- org.Action.ListVariables (serves)
- Action.ListVariables (data_flow)
- org.ListMembers (calls)
- listMembers (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- ActionVariable (uses_model)

## GET /api/v1/orgs/{org}/actions/variables/{variablename}

Get an org-level variable by name

- **Auth:** bearer
- **ID:** `ep-044`

### Controller

- organization (serves)
- org.Action.GetVariable (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (serves)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionVariable (uses_model)

## GET /api/v1/orgs/{org}/activities/feeds

List an organization's activity feeds

- **Auth:** optional (public access allowed, private feeds require membership)
- **ID:** `ep-035`

### Controller

- organization (serves)
- org.ListOrgActivityFeeds (serves)
- orgAssignment(true) (data_flow)
- org.ListOrgActivityFeeds (data_flow)
- reqOrgMembership() (calls)
- user.ListUserActivityFeeds (calls)
- repo.ListRepoActivityFeeds (calls)
- org.Get (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.SearchTeam (calls)

### Services

- feed_service.GetFeeds (data_flow)
- convert.ToActivities (data_flow)
- feed_service (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- activities_model.Action (uses_model)

### Error Handling

- 500 DB error checking membership (handles_error)
- 500 DB query failure (handles_error)

## GET /api/v1/orgs/{org}/blocks

List users blocked by the organization

- **Auth:** token
- **ID:** `ep-087`

### Controller

- organization (serves)
- org.ListBlocks (serves)
- org.ListBlocks (data_flow)
- user.ListBlocks (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- shared.ListBlocks (data_flow)
- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

## GET /api/v1/orgs/{org}/blocks/{username}

Check if a user is blocked by the organization

- **Auth:** token
- **ID:** `ep-088`

### Controller

- organization (serves)
- org.CheckUserBlock (serves)
- org.CheckUserBlock (data_flow)
- user.CheckUserBlock (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)
- org.BlockUser (calls)
- user.BlockUser (calls)
- org.UnblockUser (calls)
- user.UnblockUser (calls)

### Services

- shared.CheckUserBlock (data_flow)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

## GET /api/v1/orgs/{org}/hooks

List an organization's webhooks

- **Auth:** token
- **ID:** `ep-077`

### Controller

- organization (serves)
- org.ListHooks (serves)
- org.ListHooks (data_flow)
- user.ListHooks (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)
- setting.SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 500 FindAndCount fails (handles_error)
- 500 HeaderAuthorization decrypt fails (handles_error)

## GET /api/v1/orgs/{org}/hooks/{id}

Get a single organization webhook by ID

- **Auth:** token
- **ID:** `ep-078`

### Controller

- organization (serves)
- org.GetHook (serves)
- org.GetHook (data_flow)
- user.GetHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Org repo creation requires user to have create permission in org (enforces)

### Config

- setting.SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

## GET /api/v1/orgs/{org}/labels

List an organization's labels

- **Auth:** token
- **ID:** `ep-082`

### Controller

- organization (serves)
- org.ListLabels (serves)
- org.ListLabels (data_flow)
- org.GetLabel (calls)
- repo.GetLabel (calls)
- org.CreateLabel (calls)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- issues_model.Label (uses_model)

## GET /api/v1/orgs/{org}/labels/{id}

Get a single label by ID or name in an organization

- **Auth:** token
- **ID:** `ep-084`

### Controller

- organization (serves)
- org.GetLabel (serves)
- org.GetLabel (data_flow)
- repo.GetLabel (calls)
- org.CreateLabel (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- issues_model.Label (uses_model)

### Error Handling

- 404 Label not found in org by ID or name (handles_error)

## GET /api/v1/orgs/{org}/members

List an organization's members. If the doer is a member or admin, shows all members; otherwise shows only public members.

- **Auth:** bearer
- **ID:** `ep-070`

### Controller

- organization (serves)
- org.ListMembers (serves)
- org.ListMembers (data_flow)
- listMembers (data_flow)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

### Error Handling

- 404 GetOrgByName returns ErrOrgNotExist (handles_error)
- 500 IsOrgMember/CountOrgMembers/FindOrgMembers fails (handles_error)

## GET /api/v1/orgs/{org}/members/{username}

Check if a user is a member of an organization. Returns 204 if member, 303 redirect to public_members check if doer is not a member/admin, 404 if not a member.

- **Auth:** bearer
- **ID:** `ep-072`

### Controller

- organization (serves)
- org.IsMember (serves)
- org.IsMember (data_flow)
- org.ListMembers (calls)
- listMembers (calls)
- orgAssignment(false, true) (calls)
- org.IsPublicMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

### Error Handling

- 404 GetUserByName returns ErrUserNotExist (handles_error)
- 404 Target user not in org_user (handles_error)

## GET /api/v1/orgs/{org}/public_members

List an organization's public members. Always shows only public members regardless of authentication.

- **Auth:** none
- **ID:** `ep-071`

### Controller

- organization (serves)
- org.ListPublicMembers (serves)
- listMembers (data_flow)
- org.ListMembers (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pin position must be >= 1 (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

## GET /api/v1/orgs/{org}/public_members/{username}

Check if a user is a public member of an organization. Returns 204 if public member, 404 otherwise.

- **Auth:** none
- **ID:** `ep-073`

### Controller

- organization (serves)
- org.IsPublicMember (serves)
- org.IsPublicMember (data_flow)
- org.ListMembers (calls)
- listMembers (calls)
- orgAssignment(false, true) (calls)
- org.IsMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

## GET /api/v1/orgs/{org}/repos

List an organization's repos

- **Auth:** bearer
- **ID:** `ep-174`

### Controller

- organization (serves)
- user.ListOrgRepos (serves)
- user.ListOrgRepos (data_flow)
- user.listUserRepos (data_flow)
- user.ListUserRepos (calls)
- repo.Get (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- convert.ToRepo (serves)
- access_model.GetDoerRepoPermission (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/orgs/{org}/teams

List an organization's teams

- **Auth:** bearer
- **ID:** `ep-054`

### Controller

- organization (serves)
- org.ListTeams (serves)
- org.ListTeams (data_flow)
- org.ListUserTeams (calls)
- repo.ListTeams (calls)

### Services

- organization.SearchTeam (serves)
- convert.ToTeams (serves)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- Team (uses_model)
- TeamUnit (uses_model)

## GET /api/v1/orgs/{org}/teams/search

Search for teams within an organization

- **Auth:** token
- **ID:** `ep-068`

### Controller

- organization (serves)
- org.SearchTeam (serves)
- orgAssignment(true) (data_flow)
- reqOrgMembership() (data_flow)
- org.SearchTeam (data_flow)
- org.ListOrgActivityFeeds (calls)
- org.Get (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- org.ListTeams (calls)
- org.ListUserTeams (calls)
- repo.ListTeams (calls)

### Services

- convert.ToTeams (serves)
- organization.SearchTeam (calls)
- feed_service.GetFeeds (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- organization.Team (uses_model)

### Error Handling

- 500 DB query error (handles_error)

## GET /api/v1/packages/{owner}

Gets all packages of an owner

- **Auth:** bearer
- **ID:** `ep-199`

### Controller

- package (serves)
- packages.ListPackages (serves)
- packages.ListPackages (data_flow)
- packages.GetPackage (calls)

### Services

- packages.searchPackages (data_flow)
- convert.ToPackage (serves)

### Cache

- Cache: EphemeralCache (uses_cache)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- service.require_signin_view_strict (configured_by)

### Models

- packages_model.Package (uses_model)
- packages_model.PackageVersion (uses_model)
- packages_model.PackageFile (uses_model)
- packages_model.PackageDescriptor (uses_model)
- api.Package (uses_model)

### Error Handling

- 500 DB error in SearchVersions or GetPackageDescriptors (handles_error)

## GET /api/v1/packages/{owner}/{type}/{name}

Gets all versions of a specific package

- **Auth:** bearer
- **ID:** `ep-204`

### Controller

- package (serves)
- packages.ListPackageVersions (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.ListPackageVersions (data_flow)
- packages.DeletePackageVersion (calls)
- packages.ListPackageFiles (calls)
- packages.GetLatestPackageVersion (calls)
- packages.LinkPackage (calls)
- packages.UnlinkPackage (calls)
- packages.GetPackage (calls)

### Services

- convert.ToPackage (serves)
- packages_service.RemovePackageVersion (calls)
- packages_service.LinkToRepository (calls)
- packages_service.UnlinkFromRepository (calls)

### Cache

- Cache: EphemeralCache (cache_get/set)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.Package (uses_model)
- packages_model.PackageVersion (uses_model)
- packages_model.PackageDescriptor (uses_model)

## GET /api/v1/packages/{owner}/{type}/{name}/-/latest

Gets the latest version of a package

- **Auth:** bearer
- **ID:** `ep-205`

### Controller

- package (serves)
- packages.GetLatestPackageVersion (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.GetLatestPackageVersion (data_flow)
- packages.DeletePackageVersion (calls)
- packages.ListPackageFiles (calls)
- packages.ListPackageVersions (calls)
- packages.LinkPackage (calls)
- packages.UnlinkPackage (calls)
- packages.GetPackage (calls)

### Services

- convert.ToPackage (serves)
- packages_service.RemovePackageVersion (calls)
- packages_service.LinkToRepository (calls)
- packages_service.UnlinkFromRepository (calls)

### Cache

- Cache: EphemeralCache (cache_get/set)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.Package (uses_model)
- packages_model.PackageVersion (uses_model)
- packages_model.PackageDescriptor (uses_model)

## GET /api/v1/packages/{owner}/{type}/{name}/{version}

Gets a specific package version

- **Auth:** bearer
- **ID:** `ep-200`

### Controller

- package (serves)
- packages.GetPackage (serves)
- packages.GetPackage (data_flow)
- packages.DeletePackage (calls)

### Services

- convert.ToPackage (serves)
- packages_service.RemovePackage (calls)

### Cache

- Cache: EphemeralCache (cache_get/set)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- service.require_signin_view_strict (configured_by)

### Models

- packages_model.Package (uses_model)
- packages_model.PackageVersion (uses_model)
- packages_model.PackageFile (uses_model)
- packages_model.PackageDescriptor (uses_model)
- api.Package (uses_model)

### Error Handling

- 404 Package or version not found (middleware) (handles_error)
- 500 Error in convert.ToPackage (handles_error)

## GET /api/v1/packages/{owner}/{type}/{name}/{version}/files

Gets all files of a specific package version

- **Auth:** bearer
- **ID:** `ep-203`

### Controller

- package (serves)
- packages.ListPackageFiles (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.ListPackageFiles (data_flow)
- packages.DeletePackageVersion (calls)
- packages.ListPackageVersions (calls)
- packages.GetLatestPackageVersion (calls)
- packages.LinkPackage (calls)
- packages.UnlinkPackage (calls)

### Services

- convert.ToPackageFile (serves)
- packages_service.RemovePackageVersion (calls)
- packages_service.LinkToRepository (calls)
- packages_service.UnlinkFromRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.PackageVersion (uses_model)
- packages_model.PackageFile (uses_model)
- packages_model.PackageBlob (uses_model)
- packages_model.PackageDescriptor (uses_model)

## GET /api/v1/repos/issues/search

- **Auth:** none
- **ID:** `ep-469`

### Controller

- issue (serves)

## GET /api/v1/repos/search

Search for repositories

- **Auth:** none (public, but results filtered by auth)
- **ID:** `ep-362`

### Controller

- repository (serves)
- repo.Search (serves)
- repo.Search (data_flow)

### Services

- repo_model.SearchRepository (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- repo_model.Repository (uses_model)
- user_model.User (uses_model)

### Error Handling

- 422 Mode not in allowed set (handles_error)
- 500 DB query fails (handles_error)

## GET /api/v1/repos/{owner}/{repo}

Get a repository by owner and name

- **Auth:** bearer
- **ID:** `ep-367`

### Controller

- repository (serves)
- repo.Get (serves)
- repo.Get (data_flow)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)

### Models

- repo_model.Repository (uses_model)
- repo_model.LanguageStat (uses_model)
- repo_model.Mirror (uses_model)

### Error Handling

- 500 DB error loading owner/language (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts

Lists all artifacts for a repository

- **Auth:** bearer
- **ID:** `ep-295`

### Controller

- repository (serves)
- repo.GetArtifacts (serves)
- GetArtifacts (data_flow)
- GetArtifactsOfRun (calls)
- GetArtifact (v4 check) (calls)

### Services

- convert.ToActionArtifact (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionArtifact (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}

Gets a specific artifact by ID for a workflow run (v4 only)

- **Auth:** bearer
- **ID:** `ep-296`

### Controller

- repository (serves)
- repo.GetArtifact (serves)
- GetArtifact (v4 check) (data_flow)
- DeleteArtifact (v4 check + mark) (calls)
- DownloadArtifact (expiry check) (calls)
- GetArtifactsOfRun (calls)
- GetArtifacts (calls)

### Services

- convert.ToActionArtifact (serves)
- actions_service.IsArtifactV4 (serves)
- actions_service.DownloadArtifactV4ServeDirect (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- ActionArtifact (uses_model)

### Error Handling

- 404 Artifact not found, wrong repo, or invalid status (handles_error)
- 404 Artifact is v3 format (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip

Downloads a specific artifact, redirecting to blob URL or serving directly

- **Auth:** bearer
- **ID:** `ep-298`

### Controller

- repository (serves)
- repo.DownloadArtifact (serves)
- DownloadArtifact (expiry check) (data_flow)
- GetArtifact (v4 check) (calls)
- DeleteArtifact (v4 check + mark) (calls)

### Services

- actions_service.DownloadArtifactV4ServeDirect (serves)
- actions_service.IsArtifactV4 (serves)
- convert.ToActionArtifact (calls)

### External APIs

- Object Storage (Minio/Azure/Local) (integrates)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- actions.artifact_storage.STORAGE_TYPE (configured_by)
- actions.artifact_storage.SERVE_DIRECT (configured_by)
- SECRET_KEY (general token signing) (configured_by)

### Models

- ActionArtifact (uses_model)

### Error Handling

- 404 Artifact not found or wrong repo (handles_error)
- 404 Artifact status is Expired (handles_error)
- 404 Artifact is v3 (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/jobs

Lists all jobs for a repository

- **Auth:** bearer
- **ID:** `ep-277`

### Controller

- repository (serves)
- Action.ListWorkflowJobs (serves)
- Action.ListWorkflowJobs (data_flow)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionRunJob (uses_model)
- ActionRun (uses_model)
- ActionTask (uses_model)

### Error Handling

- 400 status query param not in valid set (handles_error)
- 500 database query failure (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}

Gets a specific workflow job for a workflow run

- **Auth:** bearer
- **ID:** `ep-292`

### Controller

- repository (serves)
- repo.Action.GetWorkflowJob (serves)
- GetWorkflowJob (data_flow)
- Action.ListWorkflowJobs (calls)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)

### Services

- convert.ToActionWorkflowJob (serves)
- shared.ListJobs (calls)
- actions_service.RerunWorkflowRunJobs (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- ActionRunJob (uses_model)
- ActionTask (uses_model)
- ActionTaskStep (uses_model)

### Error Handling

- 404 Job doesn't exist or belongs to different repo (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs

- **Auth:** none
- **ID:** `ep-403`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/actions/runners

Get repo-level runners

- **Auth:** bearer
- **ID:** `ep-273`

### Controller

- repository (serves)
- Action.ListRunners (serves)
- Action.ListRunners (data_flow)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- shared.runners (serves)
- convert.ToActionRunner (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- shared.getRunnerByID (calls)

### Models

- ActionRunner (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

Get a repo-level runner

- **Auth:** bearer
- **ID:** `ep-274`

### Controller

- repository (serves)
- Action.GetRunner (serves)
- Action.GetRunner (data_flow)
- user.GetRunner (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- admin.GetRunner (calls)

### Services

- shared.runners (serves)
- shared.getRunnerByID (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- convert.ToActionRunner (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- ActionRunner (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/runs

Lists all runs for a repository

- **Auth:** bearer
- **ID:** `ep-278`

### Controller

- repository (serves)
- Action.ListWorkflowRuns (serves)
- Action.ListWorkflowRuns (data_flow)
- admin.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)
- GetWorkflowRun (calls)

### Services

- shared.ListRuns (serves)
- convert.ToActionWorkflowRun (calls)
- actions_service.RerunWorkflowRunJobs (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- ActionRun (uses_model)

### Error Handling

- 400 status query param not in valid set (handles_error)
- 500 actor username doesn't exist (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}

Gets a specific workflow run by ID

- **Auth:** bearer
- **ID:** `ep-285`

### Controller

- repository (serves)
- repo.Action.GetWorkflowRun (serves)
- GetWorkflowRun (data_flow)
- Action.ListWorkflowRuns (calls)
- admin.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)
- getCurrentRepoActionRunJobsByID (calls)
- RerunWorkflowJob (find job) (calls)

### Services

- convert.ToActionWorkflowRun (serves)
- shared.ListRuns (calls)
- actions_service.RerunWorkflowRunJobs (calls)
- actions_service.GetFailedJobsForRerun (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionRun (uses_model)

### Error Handling

- 404 Run not found in repo (handles_error)
- 500 Database failure (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts

Lists all artifacts for a specific workflow run in a repository

- **Auth:** bearer
- **ID:** `ep-293`

### Controller

- repository (serves)
- repo.GetArtifactsOfRun (serves)
- GetArtifactsOfRun (data_flow)
- GetArtifacts (calls)
- GetArtifact (v4 check) (calls)

### Services

- convert.ToActionArtifact (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionArtifact (uses_model)

### Error Handling

- 500 FindAndCount fails (handles_error)
- 500 ToActionArtifact fails (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}

Gets a specific workflow run attempt by run ID and attempt number

- **Auth:** bearer
- **ID:** `ep-286`

### Controller

- repository (serves)
- repo.Action.GetWorkflowRunAttempt (serves)
- DeleteActionRun (validation) (calls)
- GetWorkflowRun (calls)
- Action.ListWorkflowRuns (calls)
- admin.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)
- getCurrentRepoActionRunJobsByID (calls)
- RerunWorkflowJob (find job) (calls)

### Services

- convert.ToActionWorkflowRun (serves)
- shared.ListRuns (calls)
- actions_service.RerunWorkflowRunJobs (calls)
- actions_service.DeleteRun (calls)
- actions_service.GetFailedJobsForRerun (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionRun (uses_model)
- ActionRunAttempt (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs

Lists all jobs for a specific workflow run attempt

- **Auth:** bearer
- **ID:** `ep-291`

### Controller

- repository (serves)
- repo.Action.ListWorkflowRunAttemptJobs (serves)
- getCurrentRepoActionRunAttemptByNumber (data_flow)
- Action.ListWorkflowJobs (calls)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (serves)
- actions_service.RerunWorkflowRunJobs (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- ActionRun (uses_model)
- ActionRunAttempt (uses_model)
- ActionRunJob (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs

Lists all jobs for a workflow run (latest attempt)

- **Auth:** bearer
- **ID:** `ep-290`

### Controller

- repository (serves)
- repo.Action.ListWorkflowRunJobs (serves)
- ListWorkflowRunJobs (data_flow)
- Action.ListWorkflowJobs (calls)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (serves)
- actions_service.RerunWorkflowRunJobs (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- ActionRun (uses_model)
- ActionRunJob (uses_model)

### Error Handling

- 400 Invalid status query param (handles_error)
- 404 Run not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/secrets

List repository actions secrets (names only, not values)

- **Auth:** bearer
- **ID:** `ep-264`

### Controller

- repository (serves)
- Action.ListActionsSecrets (serves)
- Action.ListActionsSecrets (data_flow)

### Config

- api.DEFAULT_PAGING_NUM (configured_by)

### Models

- secret_model.Secret (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/tasks

List a repository's action tasks

- **Auth:** bearer
- **ID:** `ep-279`

### Controller

- repository (serves)
- repo.ListActionTasks (serves)
- ListActionTasks (data_flow)

### Models

- ActionTask (uses_model)

### Error Handling

- 500 database query failure (handles_error)

## GET /api/v1/repos/{owner}/{repo}/actions/variables

Get repo-level variables list

- **Auth:** bearer
- **ID:** `ep-271`

### Controller

- repository (serves)
- Action.ListVariables (serves)
- Action.ListVariables (data_flow)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Models

- ActionVariable (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

Get a repo-level variable by name

- **Auth:** bearer
- **ID:** `ep-267`

### Controller

- repository (serves)
- Action.GetVariable (serves)
- Action.GetVariable (data_flow)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service (services/actions) (serves)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- actions_model.ActionVariable (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/workflows

List repository workflows from default branch

- **Auth:** bearer
- **ID:** `ep-280`

### Controller

- repository (serves)
- repo.ActionsListRepositoryWorkflows (serves)
- ActionsListRepositoryWorkflows (data_flow)

### Services

- convert.ListActionWorkflows (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- actions.workflow_dirs (configured_by)

### Models

- ActionWorkflow (uses_model)

## GET /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}

Get a specific workflow by ID (filename)

- **Auth:** bearer
- **ID:** `ep-281`

### Controller

- repository (serves)
- repo.ActionsGetWorkflow (serves)
- ActionsGetWorkflow (data_flow)

### Services

- convert.GetActionWorkflow (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- actions.workflow_dirs (configured_by)

### Models

- ActionWorkflow (uses_model)

## GET /api/v1/repos/{owner}/{repo}/activities/feeds

List a repository's activity feeds

- **Auth:** bearer
- **ID:** `ep-374`

### Controller

- repository (serves)
- repo.ListRepoActivityFeeds (serves)
- repo.ListRepoActivityFeeds (data_flow)
- org.ListOrgActivityFeeds (calls)
- user.ListUserActivityFeeds (calls)
- orgAssignment(true) (calls)

### Services

- feed_service.GetFeeds (serves)
- convert.ToActivities (data_flow)

### Models

- repo_model.Repository (uses_model)
- activities_model.Action (uses_model)

## GET /api/v1/repos/{owner}/{repo}/archive/{archive}

- **Auth:** none
- **ID:** `ep-392`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/assignees

Return all users that have write access and can be assigned to issues

- **Auth:** token
- **ID:** `ep-256`

### Controller

- repository (serves)
- repo.GetAssignees (serves)
- repo.GetAssignees (data_flow)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)

### Services

- convert (serves)
- user_model.SearchUsers (calls)
- pull_service.GetReviewers (calls)
- convert.ToOrganization (calls)
- convert.ToUser (calls)
- issue_service.CanDoerChangeReviewRequests (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- user_model.User (uses_model)

## GET /api/v1/repos/{owner}/{repo}/branch_protections

List all branch protection rules for a repository

- **Auth:** bearer
- **ID:** `ep-313`

### Controller

- repository (serves)
- repo.ListBranchProtections (serves)
- repo.ListBranchProtections (data_flow)
- repo.DeleteBranch (calls)
- repo.ListBranches (calls)
- repo.GetBranchProtection (calls)

### Services

- convert.ToBranchProtection (serves)
- repo_module.SyncRepoBranches (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- git_model.ProtectedBranch (uses_model)

## GET /api/v1/repos/{owner}/{repo}/branch_protections/{name}

Get a specific branch protection rule for the repository

- **Auth:** bearer
- **ID:** `ep-312`

### Controller

- repository (serves)
- repo.GetBranchProtection (serves)
- repo.GetBranchProtection (data_flow)

### Services

- convert.ToBranchProtection (serves)

### Models

- git_model.ProtectedBranch (uses_model)

### Error Handling

- 500 GetProtectedBranchRuleByName fails (handles_error)
- 404 bp == nil || bp.RepoID != repo.ID (handles_error)

## GET /api/v1/repos/{owner}/{repo}/branches

List a repository's branches with pagination

- **Auth:** bearer
- **ID:** `ep-309`

### Controller

- repository (serves)
- repo.ListBranches (serves)
- repo.ListBranches (data_flow)
- repo.DeleteBranch (calls)
- repo.ListBranchProtections (calls)

### Services

- convert.ToBranch (loop) (data_flow)
- convert.ToBranch (serves)
- repo_module.SyncRepoBranches (calls)
- repo_service.DeleteBranch (calls)
- checkBranchName (calls)
- repository.GetUpstreamDivergingInfo (calls)
- pull.Update (calls)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- git_model.Branch (uses_model)
- git_model.ProtectedBranch (uses_model)
- api.Branch (uses_model)

## GET /api/v1/repos/{owner}/{repo}/branches/{branch}

Retrieve a specific branch from a repository, including its effective branch protection

- **Auth:** bearer
- **ID:** `ep-306`

### Controller

- repository (serves)
- repo.GetBranch (serves)
- repo.GetBranch (data_flow)

### Services

- convert.ToBranch (serves)
- checkBranchName (calls)
- repository.GetUpstreamDivergingInfo (calls)
- pull.Update (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- git_model.Branch (uses_model)
- git_model.ProtectedBranch (uses_model)
- api.Branch (uses_model)

## GET /api/v1/repos/{owner}/{repo}/collaborators

List all collaborators of a repository with pagination

- **Auth:** bearer
- **ID:** `ep-250`

### Controller

- repository (serves)
- repo.ListCollaborators (serves)
- repo.ListCollaborators (data_flow)

### Config

- api.DefaultPagingNum (configured_by)
- api.MaxResponseItems (configured_by)

### Models

- repo_model.Collaboration (uses_model)

## GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

Check if a user is a collaborator of a repository

- **Auth:** bearer
- **ID:** `ep-251`

### Controller

- repository (serves)
- repo.IsCollaborator (serves)
- repo.IsCollaborator (data_flow)

### Models

- repo_model.Collaboration (uses_model)

### Error Handling

- 422 Username not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission

Get repository permissions for a user

- **Auth:** token
- **ID:** `ep-254`

### Controller

- repository (serves)
- repo.GetRepoPermissions (serves)
- repo.GetRepoPermissions (data_flow)
- repo.ListPullRequests (calls)
- repo.Generate (calls)
- org.CheckUserBlock (calls)
- user.CheckUserBlock (calls)
- org.BlockUser (calls)
- user.BlockUser (calls)
- org.UnblockUser (calls)
- user.UnblockUser (calls)

### Services

- convert (serves)
- shared.CheckUserBlock (calls)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- user_model.User (uses_model)
- access_model.Permission (uses_model)

### Error Handling

- 403 Doer not admin/repo-admin/self (handles_error)
- 404 Collaborator username not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/commits

Get a list of all commits from a repository with pagination

- **Auth:** token
- **ID:** `ep-215`

### Controller

- repository (serves)
- repo.GetAllCommits (serves)
- repo.GetAllCommits (data_flow)
- repo.GetPullRequestCommits (calls)
- repo.GetPullRequestFiles (calls)

### Services

- convert.ToCommit (serves)
- git_service.GetCompareInfo (calls)
- repo.getCommit (calls)
- gitdiff.GetDiffForAPI (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- git.CommitsRangeSize (configured_by)
- api.SwaggerURL (configured_by)

### Models

- git.Commit (uses_model)
- api.Commit (uses_model)

### Error Handling

- 422 invalid since/until format (handles_error)
- 409 Repository.IsEmpty is true (handles_error)
- 404 sha/branch not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/commits/{ref}/status

- **Auth:** none
- **ID:** `ep-432`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/commits/{ref}/statuses

- **Auth:** none
- **ID:** `ep-431`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/commits/{sha}/pull

Get the merged pull request associated with a commit SHA

- **Auth:** token
- **ID:** `ep-217`

### Controller

- repository (serves)
- repo.GetCommitPullRequest (serves)
- repo.GetCommitPullRequest (data_flow)

### Services

- pull_service.StartPullRequestCheckOnView (calls)
- pull_service.NewPullRequest (calls)

### Models

- issues.PullRequest (uses_model)

### Error Handling

- 404 no merged PR for this commit (handles_error)

## GET /api/v1/repos/{owner}/{repo}/compare/{basehead}

- **Auth:** none
- **ID:** `ep-434`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/contents

- **Auth:** none
- **ID:** `ep-400`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/contents-ext/{filepath}

- **Auth:** none
- **ID:** `ep-398`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/contents/{filepath}

- **Auth:** none
- **ID:** `ep-399`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/editorconfig/{filepath}

- **Auth:** none
- **ID:** `ep-393`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/file-contents

- **Auth:** none
- **ID:** `ep-401`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/forks

List a repository's forks

- **Auth:** bearer
- **ID:** `ep-333`

### Controller

- repository (serves)
- repo.ListForks (serves)
- repo.ListForks (data_flow)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- repo.Get (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.getParamsIssue (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- repo_service.FindForks (serves)
- access_model.GetDoerRepoPermission (data_flow)
- convert.ToRepo (data_flow)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/repos/{owner}/{repo}/git/blobs/{sha}

- **Auth:** none
- **ID:** `ep-433`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}

Get a single commit from a repository by SHA or ref

- **Auth:** token
- **ID:** `ep-214`

### Controller

- repository (serves)
- repo.GetSingleCommit (serves)
- repo.GetSingleCommit (data_flow)
- repo.GetPullRequestCommits (calls)
- repo.GetPullRequestFiles (calls)

### Services

- repo.getCommit (data_flow)
- convert.ToCommit (serves)
- git_service.GetCompareInfo (calls)
- gitdiff.GetDiffForAPI (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- git.Commit (uses_model)
- api.Commit (uses_model)

### Error Handling

- 422 sha fails IsValidRefPattern (handles_error)
- 404 commit not found in repo (handles_error)

## GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}

Get a commit's diff or patch output as plain text

- **Auth:** token
- **ID:** `ep-216`

### Controller

- repository (serves)
- repo.DownloadCommitDiffOrPatch (serves)
- repo.DownloadCommitDiffOrPatch (data_flow)

### Services

- git.GetRawDiff (serves)

### Models

- git.Commit (uses_model)

## GET /api/v1/repos/{owner}/{repo}/git/notes/{sha}

Get a note corresponding to a single commit from a repository

- **Auth:** token
- **ID:** `ep-299`

### Controller

- repository (serves)
- repo.GetNote (serves)
- repo.GetNote (data_flow)
- repo.getNote (data_flow)
- repo.GetPullRequestCommits (calls)
- repo.GetPullRequestFiles (calls)

### Services

- convert.ToCommit (serves)
- git_service.GetCompareInfo (calls)
- repo.getCommit (calls)
- gitdiff.GetDiffForAPI (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- git.Note (uses_model)
- api.Note (uses_model)

### Error Handling

- 422 sha fails IsValidRefPattern (handles_error)
- 404 commit or note not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/git/refs

List all git references (branches, tags) of a repository

- **Auth:** bearer
- **ID:** `ep-247`

### Controller

- repository (serves)
- repo.GetGitAllRefs (serves)
- repo.GetGitAllRefs (data_flow)
- repo.getGitRefsInternal (data_flow)
- repo.GetGitRefs (calls)

### Models

- api.Reference (uses_model)

### Error Handling

- 404 Empty refs list (handles_error)

## GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}

Get specified ref or filtered list of refs by prefix

- **Auth:** bearer
- **ID:** `ep-248`

### Controller

- repository (serves)
- repo.GetGitRefs (serves)
- repo.GetGitRefs (data_flow)
- repo.getGitRefsInternal (data_flow)
- repo.GetGitAllRefs (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- api.Reference (uses_model)

## GET /api/v1/repos/{owner}/{repo}/git/tags/{sha}

- **Auth:** none
- **ID:** `ep-415`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/git/trees/{sha}

Gets the tree of a repository by SHA hash with pagination support

- **Auth:** bearer
- **ID:** `ep-246`

### Controller

- repository (serves)
- repo.GetTree (serves)
- repo.GetTree (data_flow)

### Services

- files.GetTreeBySHA (data_flow)
- files_service.GetTreeBySHA (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- api.DefaultGitTreesPerPage (configured_by)

### Models

- api.GitTreeResponse (uses_model)

### Error Handling

- 400 SHA not found in git repo (handles_error)

## GET /api/v1/repos/{owner}/{repo}/hooks

List all webhooks configured for a repository

- **Auth:** bearer
- **ID:** `ep-321`

### Controller

- repository (serves)
- repo.ListHooks (serves)
- repo.ListHooks (data_flow)
- repo.GetHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Models

- Webhook (uses_model)

## GET /api/v1/repos/{owner}/{repo}/hooks/git

- **Auth:** none
- **ID:** `ep-386`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/hooks/git/{id}

- **Auth:** none
- **ID:** `ep-387`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/hooks/{id}

Get a specific webhook by ID for a repository

- **Auth:** bearer
- **ID:** `ep-322`

### Controller

- repository (serves)
- repo.GetHook (serves)
- repo.GetHook (data_flow)
- repo.ListHooks (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Models

- Webhook (uses_model)

### Error Handling

- 404 Webhook ID not found for repo (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issue_config

Returns the issue config for a repo

- **Auth:** bearer
- **ID:** `ep-372`

### Controller

- repository (serves)
- repo.GetIssueConfig (serves)
- repo.GetIssueConfig (data_flow)

### Services

- issue.GetTemplateConfigFromDefaultBranch (serves)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issue_config/validate

Returns validation information for the issue config

- **Auth:** bearer
- **ID:** `ep-373`

### Controller

- repository (serves)
- repo.ValidateIssueConfig (serves)
- repo.ValidateIssueConfig (data_flow)
- repo.GetIssueConfig (calls)

### Services

- issue.GetTemplateConfigFromDefaultBranch (serves)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issue_templates

Get available issue templates for a repository

- **Auth:** bearer
- **ID:** `ep-371`

### Controller

- repository (serves)
- repo.GetIssueTemplates (serves)
- repo.GetIssueTemplates (data_flow)

### Services

- issue.ParseTemplatesFromDefaultBranch (serves)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- repository.issue.MaxPinned (configured_by)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues

- **Auth:** none
- **ID:** `ep-470`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/comments

- **Auth:** none
- **ID:** `ep-437`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}

- **Auth:** none
- **ID:** `ep-439`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets

- **Auth:** none
- **ID:** `ep-425`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

- **Auth:** none
- **ID:** `ep-424`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

Get a list of reactions from a comment of an issue

- **Auth:** token
- **ID:** `ep-300`

### Controller

- issue (serves)
- repo.GetIssueCommentReactions (serves)
- repo.GetIssueCommentReactions (data_flow)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- ui.REACTIONS (configured_by)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Comment (uses_model)
- issues_model.Issue (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues/pinned

List a repository's pinned issues (non-pull requests)

- **Auth:** bearer
- **ID:** `ep-379`

### Controller

- repository (serves)
- repo.ListPinnedIssues (serves)
- repo.ListPinnedIssues (data_flow)
- repo.ListPinnedPullRequests (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)

### Services

- issues_model (serves)
- convert (serves)
- access_model.GetDoerRepoPermission (calls)
- convert.ToRepo (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- issues_model.IssuePin (uses_model)
- issues_model.Issue (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}

- **Auth:** none
- **ID:** `ep-471`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets

List all attachments of an issue

- **Auth:** token
- **ID:** `ep-258`

### Controller

- issue (serves)
- repo.ListIssueAttachments (serves)
- repo.ListIssueAttachments (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- repo.GetIssueDependencies (calls)
- org.ListLabels (calls)
- repo.createIssueDependency (calls)
- repo.removeIssueDependency (calls)

### Services

- convert (serves)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UpdateAttachment (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- repo_model.Attachment (uses_model)
- issues_model.Issue (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

Get a single issue attachment

- **Auth:** token
- **ID:** `ep-257`

### Controller

- issue (serves)
- repo.GetIssueAttachment (serves)
- repo.GetIssueAttachment (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- repo.GetIssueDependencies (calls)
- repo.GetReleaseAttachment (calls)
- repo.CreateReleaseAttachment (calls)
- repo.EditReleaseAttachment (calls)
- repo.DeleteReleaseAttachment (calls)

### Services

- convert (serves)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- attachment_service.UpdateAttachment (calls)
- issue_service.ChangeContent (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UploadAttachmentForRelease (calls)
- issue_service.ChangeTitle (calls)
- attachment_service.UploadAttachmentForIssue (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- repo_model.Attachment (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 404 Issue index not found (handles_error)
- 404 Attachment ID not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

List issues that are blocked by this issue (issues this issue blocks)

- **Auth:** bearer
- **ID:** `ep-211`

### Controller

- issue (serves)
- repo.GetIssueBlocks (serves)
- repo.GetIssueBlocks (data_flow)
- repo.getParamsIssue (data_flow)
- repo.CreateIssueDependency (calls)
- repo.getFormIssue (calls)
- repo.RemoveIssueDependency (calls)
- repo.CreateIssueBlocking (calls)
- repo.RemoveIssueBlocking (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- repo.getPermissionForRepo (calls)
- repo.removeIssueDependency (calls)
- repo.createIssueDependency (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)
- repo.ListPinnedIssues (calls)
- repo.ListPinnedPullRequests (calls)

### Services

- access_model.GetDoerRepoPermission (serves)
- convert.ToRepo (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Pin position must be >= 1 (enforces)

### Config

- api.DEFAULT_PAGING_NUM (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- DependencyInfo (uses_model)

### Error Handling

- 404 Issue index not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/comments

- **Auth:** none
- **ID:** `ep-435`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

List issues that block the given issue (its dependencies)

- **Auth:** bearer
- **ID:** `ep-208`

### Controller

- issue (serves)
- repo.GetIssueDependencies (serves)
- repo.GetIssueDependencies (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)
- repo.getParamsIssue (calls)
- repo.ListPinnedIssues (calls)
- repo.ListPinnedPullRequests (calls)

### Services

- Repository.IsDependenciesEnabled (data_flow)
- access_model.GetDoerRepoPermission (serves)
- issues_model.PinIssue (calls)
- convert.ToRepo (calls)
- attachment_service.UpdateAttachment (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- service.DEFAULT_ENABLE_DEPENDENCIES (configured_by)
- api.DEFAULT_PAGING_NUM (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- DependencyInfo (uses_model)

### Error Handling

- 404 IsDependenciesEnabled returns false (handles_error)
- 404 Issue index not found (handles_error)
- 404 Cannot read issues/pulls (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/labels

Get an issue's labels

- **Auth:** bearer
- **ID:** `ep-335`

### Controller

- issue (serves)
- repo.ListIssueLabels (serves)
- repo.ListIssueLabels (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.PinIssue (calls)
- org.ListLabels (calls)
- repo.GetIssueDependencies (calls)

### Services

- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UpdateAttachment (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- issues_model.Issue (uses_model)
- issues_model.Label (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

Get a list of reactions of an issue

- **Auth:** token
- **ID:** `ep-303`

### Controller

- issue (serves)
- repo.GetIssueReactions (serves)
- repo.GetIssueReactions (data_flow)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Config

- ui.REACTIONS (configured_by)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Issue (uses_model)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions

Get users who subscribed to an issue

- **Auth:** bearer
- **ID:** `ep-221`

### Controller

- issue (serves)
- repo.GetIssueSubscribers (serves)
- repo.GetIssueSubscribers (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- repo.GetIssueDependencies (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (data_flow)
- convert (serves)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UpdateAttachment (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pin position must be >= 1 (enforces)

### Config

- API.DefaultPagingNum (configured_by)

### Models

- IssueWatch (uses_model)
- Issue (uses_model)
- User (uses_model)

### Error Handling

- 404 Issue not found (handles_error)
- 500 Failure in GetIssueWatchers/GetUsersByIDs/CountIssueWatchers (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check

Check if the authenticated user is subscribed to an issue

- **Auth:** bearer
- **ID:** `ep-220`

### Controller

- issue (serves)
- repo.CheckIssueSubscription (serves)
- repo.CheckIssueSubscription (data_flow)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- repo.GetIssueDependencies (calls)

### Services

- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UpdateAttachment (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- IssueWatch (uses_model)
- Issue (uses_model)
- User (uses_model)

### Error Handling

- 404 Issue index not found in repo (handles_error)
- 500 Database failure (handles_error)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/timeline

- **Auth:** none
- **ID:** `ep-436`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/issues/{index}/times

- **Auth:** none
- **ID:** `ep-407`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/keys

List a repository's deploy keys

- **Auth:** bearer
- **ID:** `ep-340`

### Controller

- repository (serves)
- repo.ListDeployKeys (serves)
- repo.ListDeployKeys (data_flow)

### Models

- asymkey_model.DeployKey (uses_model)
- asymkey_model.PublicKey (uses_model)

## GET /api/v1/repos/{owner}/{repo}/keys/{id}

Get a repository's deploy key by id

- **Auth:** bearer
- **ID:** `ep-341`

### Controller

- repository (serves)
- repo.GetDeployKey (serves)
- repo.GetDeployKey (data_flow)

### Models

- asymkey_model.DeployKey (uses_model)
- asymkey_model.PublicKey (uses_model)

## GET /api/v1/repos/{owner}/{repo}/labels

Get all labels of a repository with pagination

- **Auth:** token (optional for public repos)
- **ID:** `ep-357`

### Controller

- issue (serves)
- repo.ListLabels (serves)
- repo.ListLabels (data_flow)
- org.ListLabels (calls)

### Services

- convert (serves)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- issues_model.Label (uses_model)

## GET /api/v1/repos/{owner}/{repo}/labels/{id}

Get a single label by ID or name

- **Auth:** token (optional for public repos)
- **ID:** `ep-358`

### Controller

- issue (serves)
- repo.GetLabel (serves)
- repo.GetLabel (data_flow)
- org.GetLabel (calls)
- org.CreateLabel (calls)

### Services

- convert (serves)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- issues_model.Label (uses_model)

## GET /api/v1/repos/{owner}/{repo}/languages

Get languages and number of bytes of code written in the repository

- **Auth:** bearer
- **ID:** `ep-375`

### Controller

- repository (serves)
- repo.GetLanguages (serves)
- repo.GetLanguages (data_flow)

### Services

- repo_model (serves)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- repo_model.LanguageStat (uses_model)

## GET /api/v1/repos/{owner}/{repo}/licenses

Get the detected licenses for a repository

- **Auth:** optional (repo access required)
- **ID:** `ep-346`

### Controller

- repository (serves)
- repo.GetLicenses (serves)
- GetLicenses (data_flow)

### Models

- repo_model.RepoLicense (uses_model)

## GET /api/v1/repos/{owner}/{repo}/media/{filepath}

- **Auth:** none
- **ID:** `ep-391`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/milestones

- **Auth:** none
- **ID:** `ep-464`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/milestones/{id}

- **Auth:** none
- **ID:** `ep-465`

### Controller

- issue (serves)

## GET /api/v1/repos/{owner}/{repo}/new_pin_allowed

Returns whether new issue/PR pins are allowed (based on max pin limit)

- **Auth:** bearer
- **ID:** `ep-381`

### Controller

- repository (serves)
- repo.AreNewIssuePinsAllowed (serves)
- repo.AreNewIssuePinsAllowed (data_flow)

### Services

- issues_model (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- repository.issue.MAX_PINNED (configured_by)

### Models

- issues_model.IssuePin (uses_model)
- api.NewIssuePinsAllowed (uses_model)

## GET /api/v1/repos/{owner}/{repo}/notifications

List current user's notification threads for a specific repository

- **Auth:** bearer (notification scope)
- **ID:** `ep-022`

### Controller

- notification (serves)
- notify.ListRepoNotifications (serves)
- notify.ListRepoNotifications (set RepoID) (data_flow)
- notify.ReadNotifications (calls)
- notify.getThread (calls)

### Services

- convert.ToNotifications (serves)
- convert.ToNotificationThread (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- api.MAX_RESPONSE_ITEMS (configured_by)
- api.DEFAULT_PAGING_NUM (configured_by)

### Models

- Notification (uses_model)
- NotificationThread (uses_model)

### Error Handling

- 422 Invalid RFC3339 before/since parameter (handles_error)
- 500 DB connection failure or query error (handles_error)

## GET /api/v1/repos/{owner}/{repo}/pulls

List a repo's pull requests with filtering and pagination

- **Auth:** bearer
- **ID:** `ep-222`

### Controller

- repository (serves)
- repo.ListPullRequests (serves)
- repo.ListPullRequests (data_flow)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)
- org.CheckUserBlock (calls)
- user.CheckUserBlock (calls)
- org.BlockUser (calls)
- user.BlockUser (calls)
- org.UnblockUser (calls)
- user.UnblockUser (calls)

### Services

- convert (serves)
- shared.CheckUserBlock (calls)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- API.DefaultPagingNum (configured_by)

### Models

- PullRequest (uses_model)
- Issue (uses_model)
- User (uses_model)
- Branch (uses_model)

### Error Handling

- 400 Poster username filter doesn't exist (handles_error)
- 500 Database failure in PullRequests or ToAPIPullRequests (handles_error)

## GET /api/v1/repos/{owner}/{repo}/pulls/pinned

List a repository's pinned pull requests

- **Auth:** bearer
- **ID:** `ep-380`

### Controller

- repository (serves)
- repo.ListPinnedPullRequests (serves)
- repo.ListPinnedPullRequests (data_flow)
- repo.ListPinnedIssues (calls)
- repo.GetCommitPullRequest (calls)

### Services

- issues_model (serves)
- convert (serves)
- pull_service.StartPullRequestCheckOnView (calls)
- pull_service.NewPullRequest (calls)
- access_model.GetDoerRepoPermission (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- issues_model.IssuePin (uses_model)
- issues_model.Issue (uses_model)
- api.PullRequest (uses_model)

## GET /api/v1/repos/{owner}/{repo}/pulls/{base}/{head}

Get a pull request by base and head branch references

- **Auth:** bearer
- **ID:** `ep-224`

### Controller

- repository (serves)
- repo.GetPullRequestByBaseHead (serves)
- repo.GetPullRequestByBaseHead (data_flow)
- repo.GetCommitPullRequest (calls)

### Services

- pull_service.StartPullRequestCheckOnView (data_flow)
- pull_service (serves)
- convert (serves)
- pull_service.NewPullRequest (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- setting.IsInTesting (configured_by)

### Models

- PullRequest (uses_model)
- Issue (uses_model)
- Branch (uses_model)

### Error Handling

- 404 Head repo not found (cross-repo format) (handles_error)
- 404 No PR for given base/head combination (handles_error)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}

Get a single pull request by index

- **Auth:** bearer
- **ID:** `ep-223`

### Controller

- repository (serves)
- repo.GetPullRequest (serves)
- repo.GetPullRequest (data_flow)
- repo.DownloadPullDiffOrPatch (calls)
- repo.GetCommitPullRequest (calls)

### Services

- pull_service.StartPullRequestCheckOnView (data_flow)
- pull_service (serves)
- convert (serves)
- pull_service.DownloadDiffOrPatch (calls)
- pull_service.NewPullRequest (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- setting.IsInTesting (configured_by)

### Models

- PullRequest (uses_model)
- Issue (uses_model)
- Branch (uses_model)

### Error Handling

- 404 PR index not found (handles_error)
- 500 Failure loading repos (handles_error)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}

Get a pull request diff or patch file

- **Auth:** bearer
- **ID:** `ep-225`

### Controller

- repository (serves)
- repo.DownloadPullDiffOrPatch (serves)
- repo.DownloadPullDiffOrPatch (data_flow)
- repo.GetPullRequest (calls)

### Services

- pull_service.DownloadDiffOrPatch (data_flow)
- pull_service (serves)
- pull_service.StartPullRequestCheckOnView (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- PullRequest (uses_model)
- Issue (uses_model)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits

Get commits for a pull request

- **Auth:** bearer
- **ID:** `ep-232`

### Controller

- repository (serves)
- repo.GetPullRequestCommits (serves)
- repo.GetPullRequestCommits (data_flow)
- repo.GetPullRequestFiles (calls)

### Services

- git_service.GetCompareInfo (data_flow)
- convert.ToCommit (data_flow)
- convert (serves)
- git_service (serves)
- gitdiff.GetDiffForAPI (calls)
- gitdiff.GetDiffShortStat (calls)
- repo.getCommit (calls)

### Models

- issues_model.PullRequest (uses_model)
- git_service.CompareInfo (uses_model)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/files

Get changed files for a pull request

- **Auth:** bearer
- **ID:** `ep-233`

### Controller

- repository (serves)
- repo.GetPullRequestFiles (serves)
- repo.GetPullRequestFiles (data_flow)
- repo.GetPullRequestCommits (calls)

### Services

- git_service.GetCompareInfo (data_flow)
- gitdiff.GetDiffForAPI (data_flow)
- gitdiff.GetDiffShortStat (data_flow)
- convert (serves)
- gitdiff (serves)
- git_service (serves)
- convert.ToCommit (calls)

### Config

- git.MAX_GIT_DIFF_LINES (configured_by)
- git.MAX_GIT_DIFF_LINE_CHARACTERS (configured_by)

### Models

- issues_model.PullRequest (uses_model)
- git_service.CompareInfo (uses_model)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

Check if a pull request has been merged

- **Auth:** bearer
- **ID:** `ep-228`

### Controller

- repository (serves)
- repo.IsPullRequestMerged (serves)
- repo.IsPullRequestMerged (data_flow)

### Models

- issues_model.PullRequest (uses_model)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews

- **Auth:** none
- **ID:** `ep-451`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

- **Auth:** none
- **ID:** `ep-452`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments

- **Auth:** none
- **ID:** `ep-453`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/push_mirrors

Lists all push mirrors of a repository with pagination

- **Auth:** bearer
- **ID:** `ep-236`

### Controller

- repository (serves)
- repo.ListPushMirrors (serves)
- repo.ListPushMirrors (data_flow)
- repo.GetPushMirrorByName (calls)
- repo.CreatePushMirror (calls)

### Services

- convert.ToPushMirror (serves)
- mirror_service.AddPushMirrorRemote (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- mirror.ENABLED (configured_by)

### Models

- repo_model.PushMirror (uses_model)
- api.PushMirror (uses_model)

## GET /api/v1/repos/{owner}/{repo}/push_mirrors/{name}

Gets a specific push mirror by its remote name

- **Auth:** bearer
- **ID:** `ep-237`

### Controller

- repository (serves)
- repo.GetPushMirrorByName (serves)
- repo.GetPushMirrorByName (data_flow)
- repo.ListPushMirrors (calls)
- repo.CreatePushMirror (calls)

### Services

- convert.ToPushMirror (serves)
- mirror_service.AddPushMirrorRemote (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- mirror.ENABLED (configured_by)

### Models

- repo_model.PushMirror (uses_model)
- api.PushMirror (uses_model)

### Error Handling

- 404 Push mirror with given name doesn't exist (handles_error)
- 500 db.Get fails (handles_error)

## GET /api/v1/repos/{owner}/{repo}/raw/{filepath}

- **Auth:** none
- **ID:** `ep-390`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/releases

List a repository's releases with pagination and optional draft/pre-release filters

- **Auth:** optional (required for draft access)
- **ID:** `ep-242`

### Controller

- repository (serves)
- repo.ListReleases (serves)
- org.GetAll (calls)
- admin.ListHooks (calls)
- user.Search (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- repo.GetLatestRelease (calls)

### Services

- user_model.SearchUsers (calls)
- convert.ToOrganization (calls)
- convert.ToUser (calls)
- webhook_service.ToHook (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- api.DEFAULT_PAGING_NUM (configured_by)
- api.MAX_RESPONSE_ITEMS (configured_by)

### Models

- repo_model.Release (uses_model)
- repo_model.Attachment (uses_model)

## GET /api/v1/repos/{owner}/{repo}/releases/latest

Get the most recent non-prerelease, non-draft release sorted by created_at

- **Auth:** optional
- **ID:** `ep-241`

### Controller

- repository (serves)
- repo.GetLatestRelease (serves)
- repo.GetLatestRelease (data_flow)
- repo.GetRelease (calls)
- GetReleaseByTag (calls)
- DeleteReleaseByTag (calls)

### Services

- release_service.UpdateRelease (calls)
- release_service.DeleteReleaseByID (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- repo_model.Release (uses_model)
- repo_model.Attachment (uses_model)

## GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag}

Get a single release of a repository by tag name

- **Auth:** optional (required for draft access)
- **ID:** `ep-344`

### Controller

- repository (serves)
- repo.GetReleaseByTag (serves)
- GetReleaseByTag (data_flow)
- DeleteReleaseByTag (calls)
- repo.GetLatestRelease (calls)
- repo.DeleteRelease (calls)
- repo.GetRelease (calls)

### Services

- convert (serves)
- release_service.DeleteReleaseByID (calls)
- release_service.UpdateRelease (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- repo_model.Release (uses_model)

### Error Handling

- 404 Tag name not found in release table (handles_error)
- 404 Record is tag-only, not a release (handles_error)
- 404 User lacks write permission for draft (handles_error)

## GET /api/v1/repos/{owner}/{repo}/releases/{id}

Get a single release by ID for a repository

- **Auth:** optional (required for draft access)
- **ID:** `ep-240`

### Controller

- repository (serves)
- repo.GetRelease (serves)
- repo.GetRelease (data_flow)
- repo.GetLatestRelease (calls)
- GetReleaseByTag (calls)
- DeleteReleaseByTag (calls)

### Services

- release_service.UpdateRelease (calls)
- release_service.DeleteReleaseByID (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- repo_model.Release (uses_model)
- repo_model.Attachment (uses_model)

### Error Handling

- 404 Release ID not found for repo (handles_error)
- 404 Record is tag-only (handles_error)

## GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets

List all attachments of a release

- **Auth:** token (optional for public repos)
- **ID:** `ep-353`

### Controller

- repository (serves)
- repo.ListReleaseAttachments (serves)
- repo.ListReleaseAttachments (data_flow)
- repo.GetLatestRelease (calls)

### Services

- convert (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- server.APP_URL (configured_by)

### Models

- repo_model.Attachment (uses_model)
- repo_model.Release (uses_model)

## GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

Get a single attachment of a release by its ID

- **Auth:** token (optional for public repos)
- **ID:** `ep-352`

### Controller

- repository (serves)
- repo.GetReleaseAttachment (serves)
- repo.GetReleaseAttachment (data_flow)
- repo.CreateReleaseAttachment (calls)
- repo.EditReleaseAttachment (calls)
- repo.DeleteReleaseAttachment (calls)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)

### Services

- convert (serves)
- attachment_service.UploadAttachmentForRelease (calls)
- attachment_service.UpdateAttachment (calls)
- issue_service.ChangeContent (calls)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- issue_service.ChangeTitle (calls)
- attachment_service.UploadAttachmentForIssue (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- server.APP_URL (configured_by)

### Models

- repo_model.Attachment (uses_model)
- repo_model.Release (uses_model)

### Error Handling

- 404 Release ID not found (handles_error)
- 404 Attachment ID not found (handles_error)

## GET /api/v1/repos/{owner}/{repo}/reviewers

Return all users that can be requested to review in this repo

- **Auth:** token
- **ID:** `ep-255`

### Controller

- repository (serves)
- repo.GetReviewers (serves)
- repo.GetReviewers (data_flow)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- repo.GetAssignees (calls)

### Services

- issue_service.CanDoerChangeReviewRequests (data_flow)
- pull_service.GetReviewers (data_flow)
- issue_service (serves)
- pull_service (serves)
- convert (serves)
- user_model.SearchUsers (calls)
- convert.ToOrganization (calls)
- convert.ToUser (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- user_model.User (uses_model)

### Error Handling

- 403 Doer cannot change review requests (handles_error)

## GET /api/v1/repos/{owner}/{repo}/signing-key.gpg

Returns the GPG signing key for a given repository

- **Auth:** bearer
- **ID:** `ep-005`

### Controller

- repository (serves)
- misc.SigningKeyGPG (serves)
- misc.SigningKeyGPG (data_flow)
- misc.SigningKeySSH (calls)

### Services

- asymkey_service.PublicSigningKey (serves)

### External APIs

- GPG binary (gpg --export) (integrates)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- repository.SIGNING_KEY (configured_by)
- repository.SIGNING_FORMAT (configured_by)
- git.HOME_PATH (configured_by)

### Models

- git.SigningKey (uses_model)

## GET /api/v1/repos/{owner}/{repo}/signing-key.pub

Returns the SSH signing key for a given repository

- **Auth:** bearer
- **ID:** `ep-007`

### Controller

- repository (serves)
- misc.SigningKeySSH (serves)
- misc.SigningKeySSH (data_flow)
- misc.SigningKeyGPG (calls)

### Services

- asymkey_service.PublicSigningKey (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- repository.SIGNING_KEY (configured_by)
- repository.SIGNING_FORMAT (configured_by)

### Models

- git.SigningKey (uses_model)

## GET /api/v1/repos/{owner}/{repo}/stargazers

List users who starred the repository

- **Auth:** bearer
- **ID:** `ep-327`

### Controller

- repository (serves)
- repo.ListStargazers (serves)
- repo.ListStargazers (data_flow)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- user_model.User (uses_model)

## GET /api/v1/repos/{owner}/{repo}/statuses/{sha}

- **Auth:** none
- **ID:** `ep-430`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/subscribers

List users watching (subscribed to) the repository

- **Auth:** bearer
- **ID:** `ep-328`

### Controller

- repository (serves)
- repo.ListSubscribers (serves)
- repo.ListSubscribers (data_flow)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Models

- user_model.User (uses_model)

## GET /api/v1/repos/{owner}/{repo}/subscription

Check if the current user is watching a repo

- **Auth:** bearer
- **ID:** `ep-196`

### Controller

- repository (serves)
- user.IsWatching (serves)
- user.IsWatching (data_flow)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- repo_model.Watch (uses_model)
- api.WatchInfo (uses_model)

### Error Handling

- 404 IsWatching returns false (handles_error)

## GET /api/v1/repos/{owner}/{repo}/tag_protections

- **Auth:** none
- **ID:** `ep-419`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/tag_protections/{id}

- **Auth:** none
- **ID:** `ep-420`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/tags

- **Auth:** none
- **ID:** `ep-414`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/tags/{tag}

- **Auth:** none
- **ID:** `ep-416`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/teams

List teams that have access to the repository (org repos only)

- **Auth:** bearer
- **ID:** `ep-329`

### Controller

- repository (serves)
- repo.ListTeams (serves)
- repo.ListTeams (data_flow)
- org.ListTeams (calls)
- org.ListUserTeams (calls)

### Services

- convert.ToTeams (serves)
- organization.SearchTeam (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- organization.Team (uses_model)

## GET /api/v1/repos/{owner}/{repo}/teams/{team}

Check if a team is assigned to a repository

- **Auth:** bearer
- **ID:** `ep-330`

### Controller

- repository (serves)
- repo.IsTeam (serves)
- repo.IsTeam (data_flow)
- reqTeamMembership (calls)
- orgAssignment(false, true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)

### Services

- repo_service.HasRepository (serves)
- convert.ToTeam (serves)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)

### Error Handling

- 405 repo owner is not organization (handles_error)
- 404 team name not found (handles_error)
- 404 team not assigned to repo (handles_error)

## GET /api/v1/repos/{owner}/{repo}/times

- **Auth:** none
- **ID:** `ep-412`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/times/{user}

- **Auth:** none
- **ID:** `ep-411`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/topics

Get list of topics that a repository has

- **Auth:** optional (repo access required)
- **ID:** `ep-347`

### Controller

- repository (serves)
- repo.ListTopics (serves)
- ListTopics (data_flow)
- TopicSearch (calls)

### Models

- repo_model.Topic (uses_model)
- repo_model.RepoTopic (uses_model)

## GET /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

- **Auth:** none
- **ID:** `ep-449`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/wiki/pages

- **Auth:** none
- **ID:** `ep-448`

### Controller

- repository (serves)

## GET /api/v1/repos/{owner}/{repo}/wiki/revisions/{pageName}

- **Auth:** none
- **ID:** `ep-450`

### Controller

- repository (serves)

## GET /api/v1/repositories/{id}

Get a repository by its numeric ID

- **Auth:** bearer
- **ID:** `ep-368`

### Controller

- repository (serves)
- repo.GetByID (serves)
- repo.GetByID (data_flow)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.Get (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.getParamsIssue (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- access_model.GetDoerRepoPermission (data_flow)
- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- repo_model.Repository (uses_model)
- repo_model.LanguageStat (uses_model)
- repo_model.Mirror (uses_model)

### Error Handling

- 404 Repo ID not found (handles_error)
- 404 User has no permission (handles_error)

## GET /api/v1/settings/api

Returns instance's global API settings including pagination defaults and size limits

- **Auth:** none
- **ID:** `ep-016`

### Controller

- settings (serves)
- settings.GetGeneralAPISettings (serves)
- settings.GetGeneralAPISettings (data_flow)

### Config

- api.MAX_RESPONSE_ITEMS (configured_by)
- api.DEFAULT_PAGING_NUM (configured_by)
- api.DEFAULT_GIT_TREES_PER_PAGE (configured_by)
- api.DEFAULT_MAX_BLOB_SIZE (configured_by)
- api.DEFAULT_MAX_RESPONSE_SIZE (configured_by)

### Models

- GeneralAPISettings (uses_model)

## GET /api/v1/settings/attachment

Returns instance's global attachment settings including allowed types, max size, and max files

- **Auth:** none
- **ID:** `ep-018`

### Controller

- settings (serves)
- settings.GetGeneralAttachmentSettings (serves)
- settings.GetGeneralAttachmentSettings (data_flow)

### Config

- attachment.ENABLED (configured_by)
- attachment.MAX_SIZE (configured_by)

### Models

- GeneralAttachmentSettings (uses_model)

## GET /api/v1/settings/repository

Returns instance's global repository settings indicating which features are disabled

- **Auth:** none
- **ID:** `ep-017`

### Controller

- settings (serves)
- settings.GetGeneralRepoSettings (serves)
- settings.GetGeneralRepoSettings (data_flow)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Config

- mirror.ENABLED (configured_by)
- repository.DISABLE_HTTP_GIT (configured_by)

### Models

- GeneralRepoSettings (uses_model)

## GET /api/v1/settings/ui

Returns instance's global UI settings including default theme, allowed reactions, and custom emojis

- **Auth:** none
- **ID:** `ep-015`

### Controller

- settings (serves)
- settings.GetGeneralUISettings (serves)
- settings.GetGeneralUISettings (data_flow)

### Config

- ui.DEFAULT_THEME (configured_by)
- ui.REACTIONS (configured_by)
- ui.CUSTOM_EMOJIS (configured_by)

### Models

- GeneralUISettings (uses_model)

## GET /api/v1/signing-key.gpg

Returns the GPG public key of the default signing key

- **Auth:** none
- **ID:** `ep-004`

### Controller

- miscellaneous (serves)
- misc.SigningKeyGPG (serves)
- misc.SigningKeyGPG (data_flow)
- misc.SigningKeySSH (calls)

### Services

- asymkey_service.PublicSigningKey (serves)

### External APIs

- GPG binary (gpg --export) (integrates)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- repository.SIGNING_KEY (configured_by)
- repository.SIGNING_FORMAT (configured_by)
- git.HOME_PATH (configured_by)

### Models

- git.SigningKey (uses_model)

### Error Handling

- 404 No GPG key configured or key is SSH format (handles_error)
- 500 gpg binary fails or key not found (handles_error)

## GET /api/v1/signing-key.pub

Returns the SSH public key of the default signing key

- **Auth:** none
- **ID:** `ep-006`

### Controller

- miscellaneous (serves)
- misc.SigningKeySSH (serves)
- misc.SigningKeySSH (data_flow)
- misc.SigningKeyGPG (calls)

### Services

- asymkey_service.PublicSigningKey (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- repository.SIGNING_KEY (configured_by)
- repository.SIGNING_FORMAT (configured_by)

### Models

- git.SigningKey (uses_model)

## GET /api/v1/teams/{id}

Get a team by its ID

- **Auth:** token
- **ID:** `ep-056`

### Controller

- organization (serves)
- org.GetTeam (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership (data_flow)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)

### Services

- convert.ToTeam (serves)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)
- repo_service.HasRepository (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUnit (uses_model)

## GET /api/v1/teams/{id}/activities/feeds

List a team's activity feeds

- **Auth:** token
- **ID:** `ep-069`

### Controller

- organization (serves)
- org.ListTeamActivityFeeds (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership() (data_flow)
- org.ListTeamActivityFeeds (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListOrgActivityFeeds (calls)
- user.ListUserActivityFeeds (calls)
- repo.ListRepoActivityFeeds (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)

### Services

- feed_service.GetFeeds (serves)
- convert.ToActivities (serves)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- activities_model.Action (uses_model)

## GET /api/v1/teams/{id}/members

List a team's members

- **Auth:** token
- **ID:** `ep-060`

### Controller

- organization (serves)
- org.GetTeamMembers (serves)
- orgAssignment(false, true) (data_flow)
- org.GetTeamMembers (data_flow)
- reqTeamMembership (calls)
- reqTeamMembership() (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- user_model.User (uses_model)

## GET /api/v1/teams/{id}/members/{username}

Get a particular member of a team

- **Auth:** token
- **ID:** `ep-061`

### Controller

- organization (serves)
- org.GetTeamMember (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- org.ListMembers (calls)
- listMembers (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- user_model.User (uses_model)

## GET /api/v1/teams/{id}/repos

List all repositories belonging to a team

- **Auth:** token
- **ID:** `ep-064`

### Controller

- organization (serves)
- org.GetTeamRepos (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership() (data_flow)
- org.GetTeamRepos (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- repo.Get (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)
- repo_model.Repository (uses_model)

### Error Handling

- 500 GetTeamRepositories fails (handles_error)
- 500 GetDoerRepoPermission fails (handles_error)

## GET /api/v1/teams/{id}/repos/{org}/{repo}

Get a particular repository of a team

- **Auth:** token
- **ID:** `ep-065`

### Controller

- organization (serves)
- org.GetTeamRepo (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership() (data_flow)
- org.GetTeamRepo (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- org.GetTeamRepos (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- repo.Get (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)
- repo_model.Repository (uses_model)

## GET /api/v1/topics/search

Search topics via keyword

- **Auth:** optional
- **ID:** `ep-351`

### Controller

- repository (serves)
- repo.TopicSearch (serves)
- TopicSearch (data_flow)
- ListTopics (calls)

### Services

- convert (serves)

### Models

- repo_model.Topic (uses_model)

## GET /api/v1/user

Get the currently authenticated user's full profile

- **Auth:** bearer|basic (required)
- **ID:** `ep-125`

### Controller

- user (serves)
- user.GetAuthenticatedUser (serves)
- user.GetAuthenticatedUser (data_flow)
- user.GetInfo (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- user_model.User (uses_model)

## GET /api/v1/user/actions/jobs

Get workflow jobs for the authenticated user

- **Auth:** bearer
- **ID:** `ep-138`

### Controller

- user (serves)
- user.ListWorkflowJobs (serves)
- user.ListWorkflowJobs (data_flow)
- Action.ListWorkflowJobs (calls)
- admin.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)
- GetWorkflowJob (calls)

### Services

- shared.ListJobs (serves)
- convert.ToActionWorkflowJob (calls)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- ActionRunJob (uses_model)

### Error Handling

- 400 invalid status query param (handles_error)
- 500 job has nil run or repo after load (handles_error)
- 500 database failure (handles_error)

## GET /api/v1/user/actions/runners

Get user-level action runners

- **Auth:** bearer
- **ID:** `ep-176`

### Controller

- user (serves)
- user.ListRunners (serves)
- user.ListRunners (data_flow)
- admin.ListRunners (calls)
- Action.ListRunners (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- admin.GetRunner (calls)

### Services

- convert.ToActionRunner (serves)
- shared.getRunnerByID (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin position must be >= 1 (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

## GET /api/v1/user/actions/runners/{runner_id}

Get a specific user-level action runner by ID

- **Auth:** bearer
- **ID:** `ep-177`

### Controller

- user (serves)
- user.GetRunner (serves)
- user.GetRunner (data_flow)
- Action.GetRunner (calls)
- admin.GetRunner (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- Action.DeleteRunner (calls)
- admin.DeleteRunner (calls)
- user.DeleteRunner (calls)
- Action.UpdateRunner (calls)
- admin.UpdateRunner (calls)
- user.UpdateRunner (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)

### Services

- shared.getRunnerByID (data_flow)
- convert.ToActionRunner (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 404 Runner ID not found in DB (handles_error)
- 404 Runner belongs to different owner (handles_error)

## GET /api/v1/user/actions/runs

Get workflow runs for the authenticated user

- **Auth:** bearer
- **ID:** `ep-137`

### Controller

- user (serves)
- user.ListWorkflowRuns (serves)
- user.ListWorkflowRuns (data_flow)
- Action.ListWorkflowRuns (calls)
- admin.ListWorkflowRuns (calls)
- GetWorkflowRun (calls)

### Services

- shared.ListRuns (serves)
- convert.ToActionWorkflowRun (calls)
- actions_service.RerunWorkflowRunJobs (calls)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- ActionRun (uses_model)

### Error Handling

- 400 invalid status query param (handles_error)
- 500 actor username does not exist (handles_error)
- 500 database failure (handles_error)

## GET /api/v1/user/actions/variables

Get the user-level list of variables which is created by current doer

- **Auth:** bearer
- **ID:** `ep-136`

### Controller

- user (serves)
- user.ListVariables (serves)
- user.ListVariables (data_flow)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- ActionVariable (uses_model)

### Error Handling

- 500 database failure (handles_error)

## GET /api/v1/user/actions/variables/{variablename}

Get a user-level variable which is created by current doer

- **Auth:** bearer
- **ID:** `ep-135`

### Controller

- user (serves)
- user.GetVariable (serves)
- user.GetVariable (data_flow)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- Action.GetVariable (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service (serves)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- ActionVariable (uses_model)

### Error Handling

- 404 variable not found for user (handles_error)
- 500 database failure (handles_error)

## GET /api/v1/user/applications/oauth2

List the authenticated user's OAuth2 applications

- **Auth:** bearer
- **ID:** `ep-168`

### Controller

- user (serves)
- user.ListOauth2Applications (serves)
- user.ListOauth2Applications (data_flow)
- user.GetOauth2Application (calls)

### Services

- convert.ToOAuth2Application (serves)
- OAuth2Application.GenerateClientSecret (calls)
- auth_model.UpdateOAuth2Application (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- auth.OAuth2Application (uses_model)

## GET /api/v1/user/applications/oauth2/{id}

Get a specific OAuth2 application by ID

- **Auth:** bearer
- **ID:** `ep-170`

### Controller

- user (serves)
- user.GetOauth2Application (serves)
- user.GetOauth2Application (data_flow)
- user.ListOauth2Applications (calls)

### Services

- convert.ToOAuth2Application (serves)
- OAuth2Application.GenerateClientSecret (calls)
- auth_model.UpdateOAuth2Application (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- auth.OAuth2Application (uses_model)

### Error Handling

- 404 Invalid client ID (handles_error)
- 404 App not found (handles_error)
- 404 app.UID != ctx.Doer.ID (handles_error)

## GET /api/v1/user/blocks

List users blocked by the authenticated user

- **Auth:** bearer
- **ID:** `ep-190`

### Controller

- user (serves)
- user.ListBlocks (serves)
- user.ListBlocks (data_flow)
- org.ListBlocks (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- shared.ListBlocks (serves)
- convert.ToUser (data_flow)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 500 FindBlockings or LoadAttributes fails (handles_error)

## GET /api/v1/user/blocks/{username}

Check if a user is blocked by the authenticated user

- **Auth:** bearer
- **ID:** `ep-191`

### Controller

- user (serves)
- user.CheckUserBlock (serves)
- user.CheckUserBlock (data_flow)
- org.CheckUserBlock (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)

### Services

- shared.CheckUserBlock (serves)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 404 GetUserByName returns error (handles_error)
- 500 GetBlocking fails (handles_error)

## GET /api/v1/user/emails

List the authenticated user's email addresses

- **Auth:** bearer
- **ID:** `ep-180`

### Controller

- user (serves)
- user.ListEmails (serves)
- user.ListEmails (data_flow)

### Services

- convert.ToEmail (serves)

### Models

- EmailAddress (uses_model)

## GET /api/v1/user/followers

List the authenticated user's followers

- **Auth:** bearer
- **ID:** `ep-139`

### Controller

- user (serves)
- user.ListMyFollowers (serves)
- user.ListMyFollowers (data_flow)
- user.listUserFollowers (data_flow)
- user.ListFollowers (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- Follow (uses_model)
- User (uses_model)

### Error Handling

- 500 database failure (handles_error)

## GET /api/v1/user/following

List the users that the authenticated user is following

- **Auth:** bearer
- **ID:** `ep-141`

### Controller

- user (serves)
- user.ListMyFollowing (serves)
- user.ListMyFollowing (data_flow)
- user.listUserFollowing (data_flow)
- user.ListFollowing (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- Follow (uses_model)
- User (uses_model)

### Error Handling

- 500 database failure (handles_error)

## GET /api/v1/user/following/{username}

Check whether a user is followed by the authenticated user

- **Auth:** bearer
- **ID:** `ep-143`

### Controller

- user (serves)
- user.CheckMyFollowing (serves)
- user.CheckMyFollowing (data_flow)
- user.checkUserFollowing (data_flow)
- user.CheckFollowing (calls)

### Services

- user_model (serves)

### Models

- user_model.Follow (uses_model)
- user_model.User (uses_model)

## GET /api/v1/user/gpg_key_token

Get a token to verify GPG key ownership via signature

- **Auth:** bearer
- **ID:** `ep-186`

### Controller

- user (serves)
- user.GetVerificationToken (serves)
- user.GetVerificationToken (data_flow)

### Services

- asymkey_model.VerificationToken (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)

## GET /api/v1/user/gpg_keys

List the authenticated user's GPG keys

- **Auth:** bearer
- **ID:** `ep-184`

### Controller

- user (serves)
- user.ListMyGPGKeys (serves)
- user.ListMyGPGKeys (data_flow)
- user.listGPGKeys (data_flow)
- user.ListGPGKeys (calls)

### Services

- convert.ToGPGKey (serves)

### Models

- asymkey_model.GPGKey (uses_model)
- api.GPGKey (uses_model)

### Error Handling

- 500 FindAndCount or LoadSubKeys fails (handles_error)

## GET /api/v1/user/gpg_keys/{id}

Get a specific GPG key by ID for the authenticated user

- **Auth:** bearer
- **ID:** `ep-185`

### Controller

- user (serves)
- user.GetGPGKey (serves)
- user.GetGPGKey (data_flow)
- user.listGPGKeys (calls)
- user.ListGPGKeys (calls)
- user.ListMyGPGKeys (calls)

### Services

- convert.ToGPGKey (serves)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)

### Models

- asymkey_model.GPGKey (uses_model)
- api.GPGKey (uses_model)

### Error Handling

- 404 Key not found or not owned by user (handles_error)
- 500 Query failure (handles_error)

## GET /api/v1/user/hooks

List the authenticated user's webhooks

- **Auth:** bearer
- **ID:** `ep-147`

### Controller

- user (serves)
- user.ListHooks (serves)
- user.ListHooks (data_flow)
- org.ListHooks (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (data_flow)
- webhook_service (serves)
- utils (serves)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)
- SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

## GET /api/v1/user/hooks/{id}

Get a specific webhook of the authenticated user

- **Auth:** bearer
- **ID:** `ep-148`

### Controller

- user (serves)
- user.GetHook (serves)
- user.GetHook (data_flow)
- org.GetHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (data_flow)
- webhook_service (serves)
- utils (serves)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 webhook ID not found for owner (handles_error)
- 404 non-admin accessing other user's hook (handles_error)

## GET /api/v1/user/keys

List the authenticated user's public SSH keys

- **Auth:** bearer
- **ID:** `ep-157`

### Controller

- user (serves)
- user.ListMyPublicKeys (serves)
- user.ListMyPublicKeys (data_flow)
- user.listPublicKeys (data_flow)
- user.ListPublicKeys (calls)
- user.GetPublicKey (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- asymkey_model.PublicKey (uses_model)

## GET /api/v1/user/keys/{id}

Get a public key by ID

- **Auth:** bearer
- **ID:** `ep-159`

### Controller

- user (serves)
- user.GetPublicKey (serves)
- user.GetPublicKey (data_flow)
- user.listPublicKeys (calls)
- user.ListMyPublicKeys (calls)
- user.ListPublicKeys (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- asymkey_model.PublicKey (uses_model)

### Error Handling

- 404 Key ID not found in DB (handles_error)

## GET /api/v1/user/orgs

List the current user's organizations

- **Auth:** token
- **ID:** `ep-026`

### Controller

- organization (serves)
- org.ListMyOrgs (serves)
- org.ListMyOrgs (data_flow)
- org.listUserOrgs (data_flow)
- org.ListUserOrgs (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- convert.ToOrganization (serves)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- convert.ToUser (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- api.default_paging_num (configured_by)
- api.max_response_items (configured_by)
- service.default_org_member_visible (configured_by)

### Models

- organization.Organization (uses_model)
- organization.OrgUser (uses_model)

### Error Handling

- 500 FindAndCount fails (handles_error)

## GET /api/v1/user/repos

List the repos that the authenticated user owns

- **Auth:** bearer
- **ID:** `ep-173`

### Controller

- user (serves)
- user.ListMyRepos (serves)
- user.ListMyRepos (data_flow)
- user.listUserRepos (calls)
- repo.GetByID (calls)
- repo.Get (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.getParamsIssue (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- access_model.GetDoerRepoPermission (data_flow)
- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/user/settings

Get the authenticated user's settings (profile fields and privacy preferences)

- **Auth:** token
- **ID:** `ep-162`

### Controller

- user (serves)
- user.GetUserSettings (serves)
- user.GetUserSettings (data_flow)

### Services

- convert.User2UserSettings (serves)
- user_service.UpdateUser (calls)

### Models

- user_model.User (uses_model)

## GET /api/v1/user/starred

List repos that the authenticated user has starred

- **Auth:** bearer
- **ID:** `ep-153`

### Controller

- user (serves)
- user.GetMyStarredRepos (serves)
- user.GetMyStarredRepos (data_flow)
- user.GetStarredRepos (calls)
- repo.Get (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- user.getStarredRepos (data_flow)
- convert.ToRepo (serves)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- setting.Repository.DisableStars (configured_by)

### Models

- repo.Star (uses_model)

## GET /api/v1/user/starred/{owner}/{repo}

Check whether the authenticated user is starring a repo

- **Auth:** bearer
- **ID:** `ep-154`

### Controller

- user (serves)
- user.IsStarring (serves)
- user.IsStarring (data_flow)

### Services

- repo_model.IsStaring (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- setting.Repository.DisableStars (configured_by)

### Models

- repo.Star (uses_model)

## GET /api/v1/user/stopwatches

- **Auth:** none
- **ID:** `ep-385`

### Controller

- user (serves)

## GET /api/v1/user/subscriptions

List repositories watched by the authenticated user

- **Auth:** bearer
- **ID:** `ep-195`

### Controller

- user (serves)
- user.GetMyWatchedRepos (serves)
- user.GetMyWatchedRepos (data_flow)
- user.GetWatchedRepos (calls)
- repo.Get (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)

### Services

- user.getWatchedRepos (data_flow)
- convert.ToRepo (data_flow)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- user_model.User (uses_model)
- repo_model.Repository (uses_model)
- repo_model.Watch (uses_model)

## GET /api/v1/user/teams

List all the teams a user belongs to

- **Auth:** bearer
- **ID:** `ep-055`

### Controller

- user (serves)
- org.ListUserTeams (serves)
- org.ListUserTeams (data_flow)
- org.ListTeams (calls)
- repo.ListTeams (calls)

### Services

- organization.SearchTeam (serves)
- convert.ToTeams (serves)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- Team (uses_model)
- TeamUnit (uses_model)

## GET /api/v1/user/times

- **Auth:** none
- **ID:** `ep-413`

### Controller

- user (serves)

## GET /api/v1/users/search

Search for users by keyword, uid, with pagination

- **Auth:** none (public endpoint, but results vary by auth status)
- **ID:** `ep-123`

### Controller

- user (serves)
- user.Search (serves)
- user.Search (data_flow)
- org.GetAll (calls)
- admin.ListHooks (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- repo.GetAssignees (calls)
- user.UpdateUserSettings (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- user_model.SearchUsers (serves)
- convert.ToUser (serves)
- convert.ToOrganization (calls)
- pull_service.GetReviewers (calls)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- shared.ListBlocks (calls)
- webhook_service.ToHook (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- issue_service.CanDoerChangeReviewRequests (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- user_model.User (uses_model)

### Error Handling

- 500 SearchUsers fails (handles_error)

## GET /api/v1/users/{username}

Get a user's public profile information

- **Auth:** none (optional, affects visibility)
- **ID:** `ep-124`

### Controller

- user (serves)
- user.GetInfo (serves)
- user.GetInfo (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- user.GetAuthenticatedUser (calls)
- org.listUserOrgs (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- user_model.IsUserVisibleToViewer (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- user_model.User (uses_model)

### Error Handling

- 404 Username not found or user not visible (handles_error)

## GET /api/v1/users/{username}/activities/feeds

List a user's activity feeds with optional date and performer filters

- **Auth:** none (optional, affects private feed visibility)
- **ID:** `ep-127`

### Controller

- user (serves)
- user.ListUserActivityFeeds (serves)
- user.ListUserActivityFeeds (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListAccessTokens (calls)
- org.ListOrgActivityFeeds (calls)
- repo.ListRepoActivityFeeds (calls)
- org.listUserOrgs (calls)
- orgAssignment(true) (calls)

### Services

- feed_service.GetFeeds (serves)
- convert.ToActivities (serves)
- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- user_model.User (uses_model)
- activities_model.Action (uses_model)

## GET /api/v1/users/{username}/followers

List the given user's followers

- **Auth:** bearer
- **ID:** `ep-140`

### Controller

- user (serves)
- user.ListFollowers (serves)
- user.ListFollowers (data_flow)
- user.listUserFollowers (data_flow)
- user.ListMyFollowers (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- convert.ToUser (serves)
- mailer.SendRegisterNotifyMail (calls)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- Follow (uses_model)
- User (uses_model)

### Error Handling

- 404 username path param does not exist (handles_error)
- 500 database failure (handles_error)

## GET /api/v1/users/{username}/following

List the users that the given user is following

- **Auth:** optional (affects visibility filtering)
- **ID:** `ep-142`

### Controller

- user (serves)
- user.ListFollowing (serves)
- user.ListFollowing (data_flow)
- user.listUserFollowing (data_flow)
- user.ListMyFollowing (calls)

### Services

- user_model (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- API.DefaultPagingNum (configured_by)
- API.MaxResponseItems (configured_by)

### Models

- user_model.Follow (uses_model)
- user_model.User (uses_model)

## GET /api/v1/users/{username}/following/{target}

Check if one user is following another user

- **Auth:** optional
- **ID:** `ep-144`

### Controller

- user (serves)
- user.CheckFollowing (serves)
- user.CheckFollowing (data_flow)
- user.checkUserFollowing (data_flow)
- user.CheckMyFollowing (calls)

### Services

- user_model (serves)

### Models

- user_model.Follow (uses_model)
- user_model.User (uses_model)

## GET /api/v1/users/{username}/gpg_keys

List the given user's GPG keys

- **Auth:** none
- **ID:** `ep-183`

### Controller

- user (serves)
- user.ListGPGKeys (serves)
- user.ListGPGKeys (data_flow)
- user.listGPGKeys (data_flow)
- user.ListMyGPGKeys (calls)

### Services

- convert.ToGPGKey (serves)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- GPGKey (uses_model)

## GET /api/v1/users/{username}/heatmap

Get a user's contribution heatmap data for the past year

- **Auth:** none (optional, affects private activity visibility)
- **ID:** `ep-126`

### Controller

- user (serves)
- user.GetUserHeatmapData (serves)
- user.GetUserHeatmapData (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.listUserOrgs (calls)

### Services

- activities_model.GetUserHeatmapDataByUser (serves)
- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- feed_service.GetFeeds (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- user_model.User (uses_model)
- activities_model.Action (uses_model)
- activities_model.UserHeatmapData (uses_model)

### Error Handling

- 500 Heatmap query fails (handles_error)

## GET /api/v1/users/{username}/keys

List the given user's public SSH keys

- **Auth:** bearer
- **ID:** `ep-158`

### Controller

- user (serves)
- user.ListPublicKeys (serves)
- user.ListPublicKeys (data_flow)
- user.listPublicKeys (data_flow)
- user.ListMyPublicKeys (calls)
- user.GetPublicKey (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- asymkey_model.PublicKey (uses_model)

## GET /api/v1/users/{username}/orgs

List a user's organizations

- **Auth:** token
- **ID:** `ep-027`

### Controller

- organization (serves)
- org.ListUserOrgs (serves)
- org.ListUserOrgs (data_flow)
- org.listUserOrgs (data_flow)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.ListMyOrgs (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- convert.ToOrganization (serves)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- api.default_paging_num (configured_by)
- api.max_response_items (configured_by)
- service.default_org_member_visible (configured_by)

### Models

- organization.Organization (uses_model)
- organization.OrgUser (uses_model)

### Error Handling

- 404 Username does not exist (handles_error)
- 500 FindAndCount fails (handles_error)

## GET /api/v1/users/{username}/orgs/{org}/permissions

Get user permissions in organization

- **Auth:** token
- **ID:** `ep-028`

### Controller

- organization (serves)
- org.GetUserOrgsPermissions (serves)
- user.GetUserByPathParam(ctx, "org") (data_flow)
- org.ListUserOrgs (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.Get (calls)
- org.listUserOrgs (calls)

### Services

- organization.HasOrgOrUserVisible (data_flow)
- convert.ToOrganization (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- user_service.UpdateUser (calls)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- organization.Organization (uses_model)
- organization.OrgUser (uses_model)
- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- structs.OrganizationPermissions (uses_model)

### Error Handling

- 404 Username or org does not exist (handles_error)
- 404 HasOrgOrUserVisible returns false (handles_error)
- 500 GetOrgUserMaxAuthorizeLevel or CanCreateOrgRepo fails (handles_error)

## GET /api/v1/users/{username}/repos

List the repos owned by the given user

- **Auth:** bearer
- **ID:** `ep-172`

### Controller

- user (serves)
- user.ListUserRepos (serves)
- user.ListUserRepos (data_flow)
- user.listUserRepos (data_flow)
- user.ListOrgRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- repo.Get (calls)
- repo.getParamsIssue (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- access_model.GetDoerRepoPermission (data_flow)
- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- repo_model.Repository (uses_model)

## GET /api/v1/users/{username}/starred

List repos that the given user has starred

- **Auth:** bearer
- **ID:** `ep-152`

### Controller

- user (serves)
- user.GetStarredRepos (serves)
- user.GetStarredRepos (data_flow)
- user.GetMyStarredRepos (calls)
- repo.Get (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- user.getStarredRepos (data_flow)
- convert.ToRepo (serves)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- setting.Repository.DisableStars (configured_by)

### Models

- repo.Star (uses_model)

### Error Handling

- 500 Database query failure (handles_error)

## GET /api/v1/users/{username}/subscriptions

List the repositories watched by a user

- **Auth:** bearer
- **ID:** `ep-194`

### Controller

- user (serves)
- user.GetWatchedRepos (serves)
- user.GetWatchedRepos (data_flow)
- user.GetMyWatchedRepos (calls)
- repo.Get (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)

### Services

- user.getWatchedRepos (data_flow)
- convert.ToRepo (data_flow)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.API.DefaultPagingNum (configured_by)
- setting.API.MaxResponseItems (configured_by)

### Models

- user_model.User (uses_model)
- repo_model.Repository (uses_model)
- repo_model.Watch (uses_model)

## GET /api/v1/users/{username}/tokens

List the authenticated user's access tokens (requires basic auth or reverse proxy auth)

- **Auth:** basic_or_reverse_proxy
- **ID:** `ep-164`

### Controller

- user (serves)
- user.ListAccessTokens (serves)
- user.ListAccessTokens (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.AddUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- org.listUserOrgs (calls)

### Services

- organization.HasOrgOrUserVisible (calls)
- user_model.AddUserBadges (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.SuccessfulTokensCacheSize (configured_by)

### Models

- auth_model.AccessToken (uses_model)

## GET /api/v1/version

Returns the version of the Gitea application

- **Auth:** none
- **ID:** `ep-001`

### Controller

- miscellaneous (serves)
- misc.Version (serves)
- misc.Version (data_flow)

### Config

- APP_VER (configured_by)

### Models

- structs.ServerVersion (uses_model)

## PATCH /api/v1/admin/actions/runners/{runner_id}

Update a global action runner (currently only disable/enable)

- **Auth:** bearer
- **ID:** `ep-117`

### Controller

- admin (serves)
- admin.UpdateRunner (serves)
- admin.UpdateRunner (data_flow)
- Action.UpdateRunner (calls)
- user.UpdateRunner (calls)
- admin.GetRunner (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)

### Services

- convert.ToActionRunner (serves)
- shared.getRunnerByID (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 422 form.Disabled == nil (handles_error)
- 500 SetRunnerDisabled fails (handles_error)

## PATCH /api/v1/admin/hooks/{id}

Update an existing system or default webhook

- **Auth:** bearer (admin required)
- **ID:** `ep-094`

### Controller

- admin (serves)
- admin.EditHook (serves)
- admin.EditHook (data_flow)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.EditHook (calls)
- user.EditHook (calls)
- repo.EditHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- AppURL (configured_by)

### Models

- webhook.Webhook (uses_model)

## PATCH /api/v1/admin/users/{username}

Edit an existing user's profile, auth, and permission settings

- **Auth:** bearer
- **ID:** `ep-099`

### Controller

- admin (serves)
- admin.EditUser (serves)
- admin.EditUser (data_flow)
- user.UpdateUserSettings (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- org.Edit (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- user_service.UpdateAuth (serves)
- user_service.ReplacePrimaryEmailAddress (serves)
- user_service.UpdateUser (serves)
- convert.ToUser (data_flow)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- mailer.SendRegisterNotifyMail (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- convert.User2UserSettings (calls)

### External APIs

- HaveIBeenPwned API (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- MIN_PASSWORD_LENGTH (configured_by)
- PASSWORD_CHECK_PWN (configured_by)

### Models

- user_model.User (uses_model)
- user_model.EmailAddress (uses_model)

### Error Handling

- 400 Password shorter than MinPasswordLength (handles_error)
- 400 Password not complex enough (handles_error)
- 400 Password found in breach database (handles_error)
- 400 Email already in use (handles_error)
- 400 Removing admin from last admin (handles_error)

## PATCH /api/v1/notifications/threads/{id}

Mark notification thread as read by ID

- **Auth:** token
- **ID:** `ep-025`

### Controller

- notification (serves)
- notify.ReadThread (serves)
- notify.getThread (data_flow)

### Services

- convert.ToNotificationThread (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- activities_model.Notification (uses_model)
- structs.NotificationThread (uses_model)

### Error Handling

- 404 Notification ID not found (handles_error)
- 403 User is not owner and not admin (handles_error)
- 500 DB error or ownership mismatch in model (handles_error)

## PATCH /api/v1/orgs/{org}

Edit an organization's information

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-033`

### Controller

- organization (serves)
- org.Edit (serves)
- org.Edit (data_flow)
- org.Delete (calls)
- user.UpdateUserSettings (calls)
- org.Rename (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.Create (calls)
- admin.CreateOrg (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)

### Services

- org.UpdateOrgEmailAddress (serves)
- user_service.UpdateUser (serves)
- convert.ToOrganization (data_flow)
- user_service.ReplacePrimaryEmailAddress (calls)
- convert.ToUser (calls)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- org.DeleteOrganization (calls)
- user_service.UpdateAuth (calls)
- mailer.SendRegisterNotifyMail (calls)
- shared.ListBlocks (calls)
- convert.User2UserSettings (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.TeamUser (uses_model)

### Error Handling

- 422 Invalid email format/domain (handles_error)
- 500 UpdateUser fails (handles_error)

## PATCH /api/v1/orgs/{org}/actions/runners/{runner_id}

Update an org-level runner (enable/disable)

- **Auth:** bearer
- **ID:** `ep-051`

### Controller

- organization (serves)
- Action.UpdateRunner (serves)
- Action.UpdateRunner (data_flow)
- admin.UpdateRunner (calls)
- user.UpdateRunner (calls)
- admin.GetRunner (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- Action.DeleteRunner (calls)
- admin.DeleteRunner (calls)
- user.DeleteRunner (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- shared.getRunnerByID (data_flow)
- convert.ToActionRunner (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

### Error Handling

- 404 runner ID not found (handles_error)
- 422 form.Disabled == nil (handles_error)

## PATCH /api/v1/orgs/{org}/hooks/{id}

Update an organization webhook

- **Auth:** token
- **ID:** `ep-080`

### Controller

- organization (serves)
- org.EditHook (serves)
- org.EditHook (data_flow)
- user.EditHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- admin.EditHook (calls)
- repo.EditHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- setting.SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

## PATCH /api/v1/orgs/{org}/labels/{id}

Update a label in an organization

- **Auth:** token
- **ID:** `ep-085`

### Controller

- organization (serves)
- org.EditLabel (serves)
- org.EditLabel (data_flow)
- repo.CreateLabel (calls)
- org.CreateLabel (calls)
- repo.EditLabel (calls)
- org.GetLabel (calls)
- repo.GetLabel (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- issues_model.Label (uses_model)

### Error Handling

- 404 Label not found in org (handles_error)
- 422 Invalid color format (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}

Edit a repository's properties. Only fields that are set will be changed.

- **Auth:** bearer
- **ID:** `ep-369`

### Controller

- repository (serves)
- repo.Edit (serves)
- repo.Edit (data_flow)
- repo.updateBasicProperties (data_flow)
- repo.updateRepoUnits (data_flow)
- repo.updateRepoArchivedState (data_flow)
- repo.updateMirror (data_flow)
- repo.Get (calls)
- user.GetStarredRepos (calls)
- user.GetMyStarredRepos (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.GetWatchedRepos (calls)
- user.GetMyWatchedRepos (calls)

### Services

- convert.ToRepo (serves)
- user.getStarredRepos (calls)
- access_model.GetDoerRepoPermission (calls)
- user.getWatchedRepos (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- repository.ForcePrivate (configured_by)
- mirror.MinInterval (configured_by)

### Models

- repo_model.Repository (uses_model)
- repo_model.Mirror (uses_model)

### Error Handling

- 422 Name conflict on rename (handles_error)
- 422 Reserved name used (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}

Update a repo-level runner (enable/disable)

- **Auth:** bearer
- **ID:** `ep-276`

### Controller

- repository (serves)
- Action.UpdateRunner (serves)
- Action.UpdateRunner (data_flow)
- admin.UpdateRunner (calls)
- user.UpdateRunner (calls)
- admin.GetRunner (calls)

### Services

- shared.runners (serves)
- shared.getRunnerByID (calls)
- convert.ToActionRunner (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- ActionRunner (uses_model)

### Error Handling

- 422 Missing required Disabled field (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name}

Edit a branch protection rule for a repository. Only fields that are set will be changed

- **Auth:** bearer
- **ID:** `ep-315`

### Controller

- repository (serves)
- repo.EditBranchProtection (serves)
- repo.EditBranchProtection (data_flow)
- repo.GetBranchProtection (calls)

### Services

- pull_service.CheckPRsForBaseBranch (serves)
- convert.ToBranchProtection (serves)
- pull_service.CreateOrUpdateProtectedBranch (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- git_model.ProtectedBranch (uses_model)

### Error Handling

- 404 protectBranch == nil || protectBranch.RepoID != repo.ID (handles_error)
- 422 Username in whitelist not found (handles_error)
- 422 Team name in whitelist not found (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/branches/{branch}

Rename a branch in a repository

- **Auth:** bearer
- **ID:** `ep-311`

### Controller

- repository (serves)
- repo.RenameBranch (serves)
- repo.RenameBranch (data_flow)

### Services

- repo_service.RenameBranch (serves)
- notify_service.DeleteRef/CreateRef (data_flow)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- git_model.Branch (uses_model)
- git_model.ProtectedBranch (uses_model)

## PATCH /api/v1/repos/{owner}/{repo}/hooks/git/{id}

- **Auth:** none
- **ID:** `ep-388`

### Controller

- repository (serves)

## PATCH /api/v1/repos/{owner}/{repo}/hooks/{id}

Edit a webhook in a repository

- **Auth:** bearer
- **ID:** `ep-325`

### Controller

- repository (serves)
- repo.EditHook (serves)
- repo.EditHook (data_flow)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.EditHook (calls)
- user.EditHook (calls)
- admin.EditHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Hook ID not found for repo (handles_error)
- 422 Updated URL fails validation (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}

- **Auth:** none
- **ID:** `ep-440`

### Controller

- issue (serves)

## PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}

- **Auth:** none
- **ID:** `ep-427`

### Controller

- issue (serves)

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}

- **Auth:** none
- **ID:** `ep-473`

### Controller

- issue (serves)

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}

Edit an issue attachment (rename)

- **Auth:** token
- **ID:** `ep-260`

### Controller

- issue (serves)
- repo.EditIssueAttachment (serves)
- repo.EditIssueAttachment (data_flow)
- repo.DeleteIssueAttachment (calls)

### Services

- attachment_service.UpdateAttachment (data_flow)
- attachment_service (serves)
- convert (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- attachment.ALLOWED_TYPES (configured_by)
- attachment.ENABLED (configured_by)

### Models

- repo_model.Attachment (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 422 New name has forbidden extension (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}

- **Auth:** none
- **ID:** `ep-441`

### Controller

- issue (serves)

## PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position}

Move a pinned issue to a new position

- **Auth:** bearer
- **ID:** `ep-378`

### Controller

- issue (serves)
- repo.MoveIssuePin (serves)
- repo.MoveIssuePin (data_flow)

### Services

- issues_model.MovePin (data_flow)
- issues_model (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- issues_model.IssuePin (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 404 Issue not found (handles_error)
- 500 Position < 1 or pin not found (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/labels/{id}

Update a label for a repository

- **Auth:** bearer
- **ID:** `ep-360`

### Controller

- issue (serves)
- repo.EditLabel (serves)
- repo.EditLabel (data_flow)
- repo.CreateLabel (calls)
- org.GetLabel (calls)
- repo.GetLabel (calls)
- org.CreateLabel (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- issues_model.Label (uses_model)

### Error Handling

- 404 Label ID not found in repo (handles_error)
- 422 New color fails validation (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/milestones/{id}

- **Auth:** none
- **ID:** `ep-467`

### Controller

- issue (serves)

## PATCH /api/v1/repos/{owner}/{repo}/pulls/{index}

Update a pull request (title, body, assignees, labels, milestone, state, base branch, deadline, allow_maintainer_edit)

- **Auth:** bearer
- **ID:** `ep-227`

### Controller

- repository (serves)
- repo.EditPullRequest (serves)
- repo.EditPullRequest (data_flow)
- repo.ReplaceIssueLabels (calls)

### Services

- issue_service.ChangeTitle (data_flow)
- issue_service.ChangeContent (data_flow)
- issue_service.UpdateAssignees (data_flow)
- issue_service.ChangeMilestoneAssign (data_flow)
- pull_service.ChangeTargetBranch (data_flow)
- pull_service.SetAllowEdits (data_flow)
- pull_service (serves)
- issue_service (serves)
- convert (serves)
- attachment_service.UploadAttachmentForIssue (calls)
- issue_service.ReplaceLabels (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- issues_model.PullRequest (uses_model)
- issues_model.Issue (uses_model)

## PATCH /api/v1/repos/{owner}/{repo}/releases/{id}

Update a release's metadata (tag name, target, title, note, draft/prerelease status)

- **Auth:** bearer (write:repository scope)
- **ID:** `ep-244`

### Controller

- repository (serves)
- repo.EditRelease (serves)
- repo.EditRelease (data_flow)
- repo.GetLatestRelease (calls)
- repo.GetRelease (calls)
- GetReleaseByTag (calls)
- DeleteReleaseByTag (calls)

### Services

- release_service.UpdateRelease (serves)
- release_service.DeleteReleaseByID (calls)

### External APIs

- Git Repository (local filesystem) (integrates)

### Business Rules

- Pin position must be >= 1 (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- repo_model.Release (uses_model)
- repo_model.Attachment (uses_model)

## PATCH /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}

Update the name of a release attachment

- **Auth:** token (write access required)
- **ID:** `ep-355`

### Controller

- repository (serves)
- repo.EditReleaseAttachment (serves)
- repo.EditReleaseAttachment (data_flow)
- repo.GetReleaseAttachment (calls)
- repo.CreateReleaseAttachment (calls)
- repo.DeleteReleaseAttachment (calls)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.PinIssue (calls)
- repo.EditIssueAttachment (calls)
- repo.DeleteIssueAttachment (calls)

### Services

- attachment_service.UpdateAttachment (data_flow)
- attachment_service (serves)
- convert (serves)
- attachment_service.UploadAttachmentForRelease (calls)
- Repository.IsDependenciesEnabled (calls)
- issues_model.PinIssue (calls)
- issue_service.ChangeContent (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- repository.release.ALLOWED_TYPES (configured_by)
- server.APP_URL (configured_by)

### Models

- repo_model.Attachment (uses_model)
- repo_model.Release (uses_model)

### Error Handling

- 422 New filename extension not allowed (handles_error)

## PATCH /api/v1/repos/{owner}/{repo}/tag_protections/{id}

- **Auth:** none
- **ID:** `ep-422`

### Controller

- repository (serves)

## PATCH /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}

- **Auth:** none
- **ID:** `ep-446`

### Controller

- repository (serves)

## PATCH /api/v1/teams/{id}

Edit a team

- **Auth:** token
- **ID:** `ep-058`

### Controller

- organization (serves)
- org.EditTeam (serves)
- orgAssignment(false, true) (data_flow)
- org.EditTeam (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- org.ListMembers (calls)
- listMembers (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)

### Services

- org_service.UpdateTeam (serves)
- convert.ToTeam (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.NewTeam (calls)
- repo_service.HasRepository (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUnit (uses_model)

## PATCH /api/v1/user/actions/runners/{runner_id}

Update a user-level action runner (enable/disable)

- **Auth:** bearer
- **ID:** `ep-179`

### Controller

- user (serves)
- user.UpdateRunner (serves)
- user.UpdateRunner (data_flow)
- Action.UpdateRunner (calls)
- admin.UpdateRunner (calls)
- admin.GetRunner (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)

### Services

- convert.ToActionRunner (serves)
- shared.getRunnerByID (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- setting.PanicInDevOrTesting (configured_by)

### Models

- ActionRunner (uses_model)

## PATCH /api/v1/user/applications/oauth2/{id}

Update an OAuth2 application, regenerating the client secret

- **Auth:** bearer
- **ID:** `ep-171`

### Controller

- user (serves)
- user.UpdateOauth2Application (serves)
- user.UpdateOauth2Application (data_flow)
- user.ListOauth2Applications (calls)
- user.GetOauth2Application (calls)

### Services

- auth_model.UpdateOAuth2Application (data_flow)
- OAuth2Application.GenerateClientSecret (data_flow)
- convert.ToOAuth2Application (serves)
- forms.DetectInvalidOAuth2ApplicationRedirectURI (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- OAuth2.DefaultApplications (configured_by)
- OAuth2.CustomSchemes (configured_by)

### Models

- auth.OAuth2Application (uses_model)

### Error Handling

- 400 URI fails validation (handles_error)
- 404 App not found or UID mismatch (handles_error)
- 400 Error generating client secret (handles_error)

## PATCH /api/v1/user/hooks/{id}

Update a webhook owned by the authenticated user

- **Auth:** bearer
- **ID:** `ep-150`

### Controller

- user (serves)
- user.EditHook (serves)
- user.EditHook (data_flow)
- org.EditHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- admin.EditHook (calls)
- repo.EditHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- setting.DisableWebhooks (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 404 Webhook not found by owner_id+id (handles_error)
- 422 Invalid URL or content_type (handles_error)

## PATCH /api/v1/user/settings

Update the authenticated user's settings

- **Auth:** token
- **ID:** `ep-163`

### Controller

- user (serves)
- user.UpdateUserSettings (serves)
- user.UpdateUserSettings (data_flow)
- user.GetUserSettings (calls)
- org.Edit (calls)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)

### Services

- user_service.UpdateUser (serves)
- convert.User2UserSettings (serves)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)
- convert.ToUser (calls)
- user_model.SearchUsers (calls)
- organization.CreateOrganization (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateAuth (calls)
- mailer.SendRegisterNotifyMail (calls)
- shared.ListBlocks (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- user_model.User (uses_model)

### Error Handling

- 500 Database update failure or validation error (handles_error)

## POST /api/v1/admin/actions/runners/registration-token

Gets or creates a global actions runner registration token

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-113`

### Controller

- admin (serves)
- admin.CreateRegistrationToken (serves)
- admin.CreateRegistrationToken (data_flow)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- ActionRunnerToken (uses_model)

## POST /api/v1/admin/cron/{task}

Triggers a cron task to run immediately

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-111`

### Controller

- admin (serves)
- admin.PostCronTask (serves)
- admin.PostCronTask (data_flow)

### Services

- cron.Task.Run (data_flow)
- cron.GetTask (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

## POST /api/v1/admin/hooks

Create a new system or default webhook

- **Auth:** bearer (admin required)
- **ID:** `ep-093`

### Controller

- admin (serves)
- admin.CreateHook (serves)
- admin.CreateHook (data_flow)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.CreateHook (calls)
- user.CreateHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- webhook.Webhook (uses_model)

## POST /api/v1/admin/unadopted/{owner}/{repo}

Adopts unadopted files on disk as a repository tracked in the database

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-108`

### Controller

- admin (serves)
- admin.AdoptRepository (serves)
- admin.AdoptRepository (data_flow)

### Services

- repo_service.AdoptRepository (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- repository.root_path (configured_by)

### Models

- Repository (uses_model)
- User (uses_model)

### Error Handling

- 404 Owner username not found (handles_error)
- 404 Repo in DB or not on filesystem (handles_error)
- 500 Git operations or DB insert fails (handles_error)

## POST /api/v1/admin/users

Create a new user account (admin only)

- **Auth:** bearer (admin required)
- **ID:** `ep-098`

### Controller

- admin (serves)
- admin.CreateUser (serves)
- admin.CreateUser (data_flow)
- parseAuthSource (data_flow)
- user.GetInfo (calls)
- user.GetAuthenticatedUser (calls)
- user.UpdateUserSettings (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- org.ListBlocks (calls)
- user.ListBlocks (calls)
- repo.ListStargazers (calls)
- repo.ListSubscribers (calls)

### Services

- password.IsPwned (serves)
- mailer.SendRegisterNotifyMail (serves)
- convert.ToUser (serves)
- user_service.UpdateUser (calls)
- user_model.SearchUsers (calls)
- shared.ListBlocks (calls)
- org.UpdateOrgEmailAddress (calls)
- convert.ToOrganization (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### External APIs

- HaveIBeenPwned API (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)
- Cancel auto-merge requires being the scheduler or having merge permission (enforces)
- PR creator must be collaborator/member/org-member or have write on head repo (enforces)

### Config

- PasswordCheckPwn (configured_by)
- MinPasswordLength (configured_by)

### Models

- user_model.User (uses_model)
- user_model.EmailAddress (uses_model)

### Error Handling

- 422 Auth source ID not found (handles_error)
- 400 Password too short for plain auth (handles_error)
- 400 Password not complex enough (handles_error)
- 400 Password found in breach database (handles_error)
- 400 HaveIBeenPwned API call fails (handles_error)
- 422 Username already taken (handles_error)
- 422 Email already registered (handles_error)

## POST /api/v1/admin/users/{username}/badges

Add badges to a user by slug

- **Auth:** bearer
- **ID:** `ep-121`

### Controller

- admin (serves)
- admin.AddUserBadges (serves)
- admin.AddUserBadges (data_flow)
- org.ListUserOrgs (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- admin.ListUserBadges (calls)
- admin.DeleteUserBadges (calls)
- user.GetInfo (calls)
- user.GetUserHeatmapData (calls)
- user.ListUserActivityFeeds (calls)
- user.ListAccessTokens (calls)
- org.listUserOrgs (calls)

### Services

- user_model.AddUserBadges (serves)
- organization.HasOrgOrUserVisible (calls)
- user_model.RemoveUserBadges (calls)
- convert.ToUser (calls)
- activities_model.GetUserHeatmapDataByUser (calls)
- feed_service.GetFeeds (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- Badge (uses_model)
- UserBadge (uses_model)

## POST /api/v1/admin/users/{username}/keys

Add a public SSH key on behalf of a user

- **Auth:** bearer
- **ID:** `ep-101`

### Controller

- admin (serves)
- admin.CreatePublicKey (serves)
- admin.CreatePublicKey (data_flow)
- user.CreateUserPublicKey (data_flow)
- user.CreatePublicKey (calls)
- repo.CreateDeployKey (calls)

### Models

- asymkey_model.PublicKey (uses_model)

## POST /api/v1/admin/users/{username}/orgs

Create an organization owned by the specified user

- **Auth:** bearer (admin required)
- **ID:** `ep-096`

### Controller

- admin (serves)
- admin.CreateOrg (serves)
- admin.CreateOrg (data_flow)
- org.Create (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- organization.CreateOrganization (data_flow)
- convert.ToOrganization (serves)
- user_model.SearchUsers (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- convert.ToUser (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- Service.DefaultOrgMemberVisible (configured_by)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.Team (uses_model)

## POST /api/v1/admin/users/{username}/rename

Rename a user account

- **Auth:** bearer
- **ID:** `ep-104`

### Controller

- admin (serves)
- admin.RenameUser (serves)
- admin.RenameUser (data_flow)
- org.Rename (calls)

### Services

- user_service.RenameUser (serves)

### Business Rules

- Org repo creation requires user to have create permission in org (enforces)
- Cancel auto-merge requires being the scheduler or having merge permission (enforces)
- PR creator must be collaborator/member/org-member or have write on head repo (enforces)

### Models

- user_model.User (uses_model)
- user_model.Redirect (uses_model)

## POST /api/v1/admin/users/{username}/repos

Creates a repository on behalf of a user (admin only)

- **Auth:** bearer (token with AccessTokenScopeCategoryAdmin)
- **ID:** `ep-112`

### Controller

- admin (serves)
- admin.CreateRepo (serves)
- admin.CreateRepo (data_flow)
- repo.CreateUserRepo (serves)
- repo.Create (calls)
- prepareDoerCreateRepoInOrg (calls)
- repo.CreateOrgRepo (calls)

### Services

- repo_service.CreateRepository (data_flow)
- repo_service.CreateRepositoryDirectly (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Config

- repository.force_private (configured_by)

### Models

- Repository (uses_model)

## POST /api/v1/markdown

Render a markdown document as HTML

- **Auth:** bearer
- **ID:** `ep-009`

### Controller

- miscellaneous (serves)
- misc.Markdown (serves)
- misc.Markdown (data_flow)
- misc.Markup (calls)

### Services

- common.RenderMarkup (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- setting.AppSubURL (configured_by)

### Models

- MarkdownOption (uses_model)

### Error Handling

- 422 Invalid JSON body or missing required fields (handles_error)
- 422 Mode not in [empty, markdown, gfm, comment, wiki, file] (handles_error)
- 422 Unable to find renderer for content (handles_error)
- 500 Internal markdown rendering failure (handles_error)

## POST /api/v1/markdown/raw

Render raw markdown as HTML (no special link handling)

- **Auth:** bearer
- **ID:** `ep-010`

### Controller

- miscellaneous (serves)
- misc.MarkdownRaw (serves)
- misc.MarkdownRaw (data_flow)

### Services

- markdown.RenderRaw (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)

### Error Handling

- 500 Internal markdown rendering failure (handles_error)

## POST /api/v1/markup

Renders a markup document as HTML supporting multiple modes (markdown, comment, wiki, file, gfm)

- **Auth:** none
- **ID:** `ep-008`

### Controller

- miscellaneous (serves)
- misc.Markup (serves)
- misc.Markup (data_flow)
- misc.Markdown (calls)

### Services

- common.RenderMarkup (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- server.APP_URL (configured_by)

### Models

- structs.MarkupOption (uses_model)

## POST /api/v1/org/{org}/repos

Create a repository in an organization (deprecated)

- **Auth:** bearer
- **ID:** `ep-365`

### Controller

- organization (serves)
- repo.CreateOrgRepoDeprecated (serves)
- repo.CreateOrgRepoDeprecated (data_flow)
- repo.CreateOrgRepo (data_flow)
- prepareDoerCreateRepoInOrg (data_flow)
- repo.CreateUserRepo (data_flow)
- admin.CreateRepo (calls)
- repo.Create (calls)

### Services

- repo_service.CreateRepository (serves)
- repo_service.CreateRepositoryDirectly (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- repository.FORCE_PRIVATE (configured_by)

### Models

- repo_model.Repository (uses_model)
- user_model.User (uses_model)

## POST /api/v1/orgs

Create a new organization

- **Auth:** bearer (reqToken)
- **ID:** `ep-030`

### Controller

- organization (serves)
- org.Create (serves)
- org.Create (data_flow)
- admin.CreateOrg (calls)
- admin.GetAllOrgs (calls)
- admin.SearchUsers (calls)
- user.GetUserByPathParam(ctx, "org") (calls)
- org.Get (calls)
- user.UpdateUserSettings (calls)

### Services

- organization.CreateOrganization (serves)
- convert.ToOrganization (data_flow)
- user_model.SearchUsers (calls)
- organization.HasOrgOrUserVisible (calls)
- user_service.UpdateUser (calls)
- convert.ToUser (calls)
- org.UpdateOrgEmailAddress (calls)
- user_service.ReplacePrimaryEmailAddress (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- setting.Admin.DisableRegularOrgCreation (configured_by)
- setting.Service.DefaultOrgMemberVisible (configured_by)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.OrgUser (uses_model)
- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- organization.TeamUnit (uses_model)

### Error Handling

- 403 User cannot create orgs (handles_error)
- 422 Username taken (handles_error)
- 422 Username is reserved (handles_error)
- 422 Invalid characters in name (handles_error)

## POST /api/v1/orgs/{org}/actions/runners/registration-token

Get an organization's actions runner registration token

- **Auth:** bearer
- **ID:** `ep-042`

### Controller

- organization (serves)
- org.Action.CreateRegistrationToken (serves)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- ActionRunnerToken (uses_model)

### Error Handling

- 200 No existing token found (handles_error)
- 500 Database failure on insert/select (handles_error)

## POST /api/v1/orgs/{org}/actions/variables/{variablename}

Create an org-level variable

- **Auth:** bearer
- **ID:** `ep-046`

### Controller

- organization (serves)
- org.Action.CreateVariable (serves)
- Action.CreateVariable (data_flow)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (serves)
- actions_service.CreateVariable (serves)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- actions_service.UpdateVariableNameData (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- ActionVariable (uses_model)

### Error Handling

- 400 Invalid variable name format (handles_error)
- 409 Variable with same name exists (handles_error)

## POST /api/v1/orgs/{org}/avatar

Update the avatar of an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-037`

### Controller

- organization (serves)
- org.UpdateAvatar (serves)
- org.UpdateAvatar (data_flow)
- org.DeleteOrgRepos (calls)
- org.DeleteAvatar (calls)
- org.Action.ListActionsSecrets (calls)
- org.Action.CreateOrUpdateSecret (calls)
- org.Action.DeleteSecret (calls)
- user.UpdateAvatar (calls)

### Services

- user_service.UploadAvatar (data_flow)
- user_service (serves)
- org.deleteOrgReposBackground (calls)
- user_service.DeleteAvatar (calls)
- secret_service.CreateOrUpdateSecret (calls)
- secret_service.DeleteSecretByName (calls)
- repo_service.UploadAvatar (calls)

### External APIs

- Avatar Storage Backend (integrates)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- AVATAR_MAX_WIDTH (configured_by)
- AVATAR_MAX_HEIGHT (configured_by)
- AVATAR_MAX_ORIGIN_SIZE (configured_by)
- AVATAR_RENDERED_SIZE_FACTOR (configured_by)

### Models

- user_model.User (uses_model)

### Error Handling

- 400 invalid base64 in image field (handles_error)
- 500 unsupported type or too large (handles_error)

## POST /api/v1/orgs/{org}/hooks

Create a webhook for an organization

- **Auth:** token
- **ID:** `ep-079`

### Controller

- organization (serves)
- org.CreateHook (serves)
- org.CreateHook (data_flow)
- user.CreateHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- admin.CreateHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- setting.SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 422 Invalid hook type (handles_error)
- 422 Missing config option (handles_error)
- 422 Invalid URL (handles_error)
- 422 Invalid content type (handles_error)
- 400 Invalid slack channel (handles_error)

## POST /api/v1/orgs/{org}/labels

Create a label for an organization

- **Auth:** token
- **ID:** `ep-083`

### Controller

- organization (serves)
- org.CreateLabel (serves)
- org.CreateLabel (data_flow)
- repo.CreateLabel (calls)
- org.GetLabel (calls)
- repo.GetLabel (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Models

- issues_model.Label (uses_model)

## POST /api/v1/orgs/{org}/rename

Rename an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-032`

### Controller

- organization (serves)
- org.Rename (serves)
- org.Rename (data_flow)
- org.Delete (calls)
- admin.RenameUser (calls)
- org.Edit (calls)

### Services

- user_service.RenameUser (serves)
- org.DeleteOrganization (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- user_model.User (uses_model)
- organization.Organization (uses_model)
- organization.TeamUser (uses_model)

### Error Handling

- 422 New name already taken (handles_error)
- 422 New name is reserved (handles_error)
- 500 Cannot rename user directory (handles_error)

## POST /api/v1/orgs/{org}/repos

Create a repository in an organization

- **Auth:** bearer
- **ID:** `ep-366`

### Controller

- organization (serves)
- repo.CreateOrgRepo (serves)
- repo.CreateOrgRepo (data_flow)
- prepareDoerCreateRepoInOrg (data_flow)
- repo.CreateUserRepo (data_flow)
- repo.CreateOrgRepoDeprecated (calls)
- admin.CreateRepo (calls)
- repo.Create (calls)

### Services

- repo_service.CreateRepository (serves)
- repo_service.CreateRepositoryDirectly (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- repository.FORCE_PRIVATE (configured_by)

### Models

- repo_model.Repository (uses_model)
- user_model.User (uses_model)

## POST /api/v1/orgs/{org}/teams

Create a team in an organization

- **Auth:** token
- **ID:** `ep-057`

### Controller

- organization (serves)
- org.CreateTeam (serves)
- orgAssignment(true) (data_flow)
- org.CreateTeam (data_flow)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- reqTeamMembership (calls)
- org.Get (calls)
- org.SearchTeam (calls)
- org.ListMembers (calls)
- listMembers (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)

### Services

- org_service.NewTeam (serves)
- convert.ToTeam (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.UpdateTeam (calls)
- repo_service.HasRepository (calls)
- feed_service.GetFeeds (calls)
- actions_service.CreateVariable (calls)
- actions_service.UpdateVariableNameData (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- organization.Team (uses_model)
- organization.TeamUnit (uses_model)

### Error Handling

- 422 team name already exists in org (handles_error)
- 500 non-admin team with no units (handles_error)

## POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}

Link a package to a repository

- **Auth:** bearer
- **ID:** `ep-206`

### Controller

- package (serves)
- packages.LinkPackage (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.LinkPackage (data_flow)
- packages.DeletePackageVersion (calls)
- packages.ListPackageFiles (calls)
- packages.ListPackageVersions (calls)
- packages.GetLatestPackageVersion (calls)
- packages.UnlinkPackage (calls)

### Services

- packages_service.LinkToRepository (serves)
- packages_service.RemovePackageVersion (calls)
- packages_service.UnlinkFromRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.Package (uses_model)

### Error Handling

- 404 Package or repo not found (handles_error)
- 400 Package already linked (handles_error)
- 403 Owner mismatch or no write access (handles_error)

## POST /api/v1/packages/{owner}/{type}/{name}/-/unlink

Unlink a package from its repository

- **Auth:** bearer
- **ID:** `ep-207`

### Controller

- package (serves)
- packages.UnlinkPackage (serves)
- context.PackageAssignmentAPI (data_flow)
- packages.UnlinkPackage (data_flow)
- packages.DeletePackageVersion (calls)
- packages.ListPackageFiles (calls)
- packages.ListPackageVersions (calls)
- packages.GetLatestPackageVersion (calls)
- packages.LinkPackage (calls)

### Services

- packages_service.UnlinkFromRepository (serves)
- packages_service.RemovePackageVersion (calls)
- packages_service.LinkToRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- packages.ENABLED (configured_by)
- service.REQUIRE_SIGNIN_VIEW (configured_by)

### Models

- packages_model.Package (uses_model)

### Error Handling

- 404 Package not found (handles_error)
- 403 No write access to repo (handles_error)
- 400 Package not linked (RepoID==0) (handles_error)

## POST /api/v1/repos/migrate

- **Auth:** none
- **ID:** `ep-444`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/actions/runners/registration-token

Get a repository's actions runner registration token

- **Auth:** bearer
- **ID:** `ep-272`

### Controller

- repository (serves)
- Action.CreateRegistrationToken (serves)
- Action.CreateRegistrationToken (data_flow)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- shared.runners (serves)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- ActionRunnerToken (uses_model)

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun

Reruns a specific workflow job in a run

- **Auth:** bearer
- **ID:** `ep-289`

### Controller

- repository (serves)
- repo.Action.RerunWorkflowJob (serves)
- getCurrentRepoActionRunJobsByID (data_flow)
- RerunWorkflowJob (find job) (data_flow)
- GetWorkflowJob (calls)
- GetWorkflowRun (calls)
- Action.ListWorkflowJobs (calls)
- admin.ListWorkflowJobs (calls)
- user.ListWorkflowJobs (calls)
- ListWorkflowRunJobs (calls)
- getCurrentRepoActionRunAttemptByNumber (calls)

### Services

- actions_service.RerunWorkflowRunJobs (serves)
- convert.ToActionWorkflowJob (serves)
- actions_service.GetFailedJobsForRerun (calls)
- convert.ToActionWorkflowRun (calls)
- shared.ListJobs (calls)
- shared.ListRuns (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- actions.MAX_RERUN_ATTEMPTS (configured_by)

### Models

- ActionRun (uses_model)
- ActionRunAttempt (uses_model)
- ActionRunJob (uses_model)

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun

Reruns an entire workflow run creating a new attempt

- **Auth:** bearer
- **ID:** `ep-287`

### Controller

- repository (serves)
- repo.Action.RerunWorkflowRun (serves)
- getCurrentRepoActionRunJobsByID (data_flow)
- RerunWorkflowJob (find job) (calls)
- GetWorkflowRun (calls)
- Action.ListWorkflowRuns (calls)
- admin.ListWorkflowRuns (calls)
- user.ListWorkflowRuns (calls)

### Services

- actions_service.RerunWorkflowRunJobs (serves)
- convert.ToActionWorkflowRun (serves)
- actions_service.GetFailedJobsForRerun (calls)
- shared.ListRuns (calls)
- convert.ToActionWorkflowJob (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- actions.MAX_RERUN_ATTEMPTS (configured_by)

### Models

- ActionRun (uses_model)
- ActionRunAttempt (uses_model)
- ActionRunJob (uses_model)

### Error Handling

- 400 Run not done, workflow disabled, max attempts (handles_error)
- 409 Concurrent rerun attempt (handles_error)
- 404 Run or template not found (handles_error)

## POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs

Reruns all failed or cancelled jobs in a workflow run

- **Auth:** bearer
- **ID:** `ep-288`

### Controller

- repository (serves)
- repo.Action.RerunFailedWorkflowRun (serves)
- getCurrentRepoActionRunJobsByID (data_flow)
- RerunWorkflowJob (find job) (calls)
- GetWorkflowRun (calls)

### Services

- actions_service.GetFailedJobsForRerun (serves)
- actions_service.RerunWorkflowRunJobs (serves)
- convert.ToActionWorkflowRun (calls)
- shared.ListRuns (calls)
- convert.ToActionWorkflowJob (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- actions.MAX_RERUN_ATTEMPTS (configured_by)

### Models

- ActionRun (uses_model)
- ActionRunAttempt (uses_model)
- ActionRunJob (uses_model)

## POST /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

Create a repo-level variable

- **Auth:** bearer
- **ID:** `ep-269`

### Controller

- repository (serves)
- Action.CreateVariable (serves)
- Action.CreateVariable (data_flow)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- Action.UpdateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service.CreateVariable (data_flow)
- actions_service (serves)
- actions_service.UpdateVariableNameData (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- ActionVariable (uses_model)

### Error Handling

- 400 Invalid variable name (handles_error)
- 409 Variable already exists (handles_error)

## POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches

Create a workflow dispatch event to trigger a workflow run

- **Auth:** bearer
- **ID:** `ep-283`

### Controller

- repository (serves)
- repo.ActionsDispatchWorkflow (serves)
- ActionsDispatchWorkflow (data_flow)

### Services

- actions_service.DispatchActionWorkflow (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- actions.workflow_dirs (configured_by)

### Models

- ActionRun (uses_model)
- RepoUnit (uses_model)

### Error Handling

- 422 ref field is empty in request body (handles_error)
- 403 workflow is disabled in repo config (handles_error)
- 404 git ref doesn't exist (handles_error)
- 404 workflow file not in commit tree (handles_error)

## POST /api/v1/repos/{owner}/{repo}/avatar

Update repository avatar image

- **Auth:** bearer
- **ID:** `ep-262`

### Controller

- repository (serves)
- repo.UpdateAvatar (serves)
- repo.UpdateAvatar (data_flow)
- org.UpdateAvatar (calls)
- user.UpdateAvatar (calls)

### Services

- repo_service.UploadAvatar (data_flow)
- repo_service (services/repository) (serves)
- user_service.UploadAvatar (calls)

### External APIs

- File Storage (RepoAvatars) (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Config

- avatar.MAX_WIDTH (configured_by)
- avatar.MAX_HEIGHT (configured_by)
- avatar.MAX_ORIGIN_SIZE (configured_by)
- avatar.RENDERED_SIZE_FACTOR (configured_by)

### Models

- repo_model.Repository (uses_model)

### Error Handling

- 400 Invalid base64 in image field (handles_error)
- 500 Unsupported format or oversized image (handles_error)

## POST /api/v1/repos/{owner}/{repo}/branch_protections

Create a branch protection rule for a repository

- **Auth:** bearer
- **ID:** `ep-314`

### Controller

- repository (serves)
- repo.CreateBranchProtection (serves)
- repo.CreateBranchProtection (data_flow)
- repo.EditBranchProtection (calls)
- repo.GetBranchProtection (calls)

### Services

- pull_service.CreateOrUpdateProtectedBranch (serves)
- convert.ToBranchProtection (serves)
- pull_service.CheckPRsForBaseBranch (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- git_model.ProtectedBranch (uses_model)

### Error Handling

- 400 Both rule_name and branch_name empty (handles_error)
- 403 Rule with same name exists (handles_error)
- 422 Username in whitelist not found (handles_error)
- 422 Team name in whitelist not found (handles_error)

## POST /api/v1/repos/{owner}/{repo}/branch_protections/priority

Update the priorities of branch protection rules for a repository

- **Auth:** bearer
- **ID:** `ep-317`

### Controller

- repository (serves)
- repo.UpdateBranchProtectionPriories (serves)
- repo.UpdateBranchProtectionPriories (data_flow)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- git_model.ProtectedBranch (uses_model)

## POST /api/v1/repos/{owner}/{repo}/branches

Create a new branch in a repository

- **Auth:** bearer
- **ID:** `ep-308`

### Controller

- repository (serves)
- repo.CreateBranch (serves)
- repo.CreateBranch (data_flow)

### Services

- repo_service.CreateNewBranchFromCommit (serves)
- checkBranchName (data_flow)
- convert.ToBranch (serves)
- repository.GetUpstreamDivergingInfo (calls)
- pull.Update (calls)
- repository.MergeUpstream (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- git_model.Branch (uses_model)
- git_model.ProtectedBranch (uses_model)
- api.Branch (uses_model)

### Error Handling

- 409 Branch with same name exists (handles_error)
- 409 Tag with same name exists (handles_error)
- 409 Branch name conflicts with path prefix (handles_error)

## POST /api/v1/repos/{owner}/{repo}/contents

- **Auth:** none
- **ID:** `ep-394`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/contents/{filepath}

- **Auth:** none
- **ID:** `ep-395`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/diffpatch

Apply a diff patch to the repository, creating a new commit

- **Auth:** bearer
- **ID:** `ep-249`

### Controller

- repository (serves)
- repo.ApplyDiffPatch (serves)
- repo.ApplyDiffPatch (data_flow)
- repo.ReqChangeRepoFileOptionsAndCheck (data_flow)

### Services

- files.ApplyDiffPatch (data_flow)
- files_service.ApplyDiffPatch (serves)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- api.ApplyDiffPatchFileOptions (uses_model)

### Error Handling

- 500 Patch cannot be applied cleanly (handles_error)

## POST /api/v1/repos/{owner}/{repo}/file-contents

- **Auth:** none
- **ID:** `ep-402`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/forks

Fork a repository

- **Auth:** bearer
- **ID:** `ep-334`

### Controller

- repository (serves)
- repo.CreateFork (serves)
- repo.CreateFork (data_flow)
- repo.prepareDoerCreateRepoInOrg (data_flow)

### Services

- repo_service.ForkRepository (serves)

### External APIs

- Git CLI (fork clone) (integrates)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- repo_model.Repository (uses_model)

### Error Handling

- 409 fork already exists (handles_error)
- 409 repo limit reached (handles_error)
- 403 user blocked by repo owner (handles_error)

## POST /api/v1/repos/{owner}/{repo}/hooks

Create a webhook for a repository

- **Auth:** bearer
- **ID:** `ep-324`

### Controller

- repository (serves)
- repo.CreateHook (serves)
- repo.CreateHook (data_flow)
- repo.ListHooks (calls)
- repo.GetHook (calls)
- org.CreateHook (calls)
- user.CreateHook (calls)
- admin.CreateHook (calls)
- org.ListHooks (calls)
- user.ListHooks (calls)
- org.GetHook (calls)
- user.GetHook (calls)
- admin.GetHook (calls)

### Services

- webhook_service.ToHook (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 422 Type not in registered webhook types (handles_error)
- 422 url or content_type missing from config (handles_error)
- 422 URL fails validation (handles_error)
- 400 Slack channel name invalid (handles_error)

## POST /api/v1/repos/{owner}/{repo}/hooks/{id}/tests

Test a push webhook by sending a test push payload

- **Auth:** bearer
- **ID:** `ep-323`

### Controller

- repository (serves)
- repo.TestHook (serves)
- repo.TestHook (data_flow)

### Services

- convert.ToPayloadCommit (data_flow)
- webhook_service.PrepareWebhook (serves)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- Webhook (uses_model)
- HookTask (uses_model)

## POST /api/v1/repos/{owner}/{repo}/issues

- **Auth:** none
- **ID:** `ep-472`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets

- **Auth:** none
- **ID:** `ep-426`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions

Add a reaction to a comment of an issue

- **Auth:** token
- **ID:** `ep-301`

### Controller

- issue (serves)
- repo.PostIssueCommentReaction (serves)
- repo.PostIssueCommentReaction (data_flow)
- repo.changeIssueCommentReaction (data_flow)
- repo.DeleteIssueCommentReaction (calls)
- repo.changeIssueReaction (calls)

### Services

- issue_service.CreateCommentReaction (serves)
- issue_service.CreateIssueReaction (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- ui.REACTIONS (configured_by)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Comment (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 403 reaction type not in allowed list (handles_error)
- 200 duplicate reaction (handles_error)
- 403 doer is blocked by poster/owner (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets

Create an issue attachment by uploading a file

- **Auth:** token
- **ID:** `ep-259`

### Controller

- issue (serves)
- repo.CreateIssueAttachment (serves)
- repo.CreateIssueAttachment (data_flow)
- repo.EditPullRequest (calls)

### Services

- attachment_service.UploadAttachmentForIssue (data_flow)
- issue_service.ChangeContent (data_flow)
- attachment_service (serves)
- issue_service (serves)
- convert (serves)
- issue_service.ChangeTitle (calls)
- issue_service.UpdateAssignees (calls)
- attachment_service.UpdateAttachment (calls)

### External APIs

- Object Storage (Attachments) (integrates)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Config

- attachment.ALLOWED_TYPES (configured_by)
- attachment.MAX_SIZE (configured_by)
- attachment.ENABLED (configured_by)

### Models

- repo_model.Attachment (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 422 File type not in allowed list (handles_error)
- 413 File exceeds MaxSize (handles_error)
- 403 No write permission on issue (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks

Block the issue given in the body by the issue in the URL path

- **Auth:** bearer
- **ID:** `ep-212`

### Controller

- issue (serves)
- repo.CreateIssueBlocking (serves)
- repo.CreateIssueBlocking (data_flow)
- repo.getParamsIssue (data_flow)
- repo.getFormIssue (data_flow)
- repo.createIssueDependency (data_flow)
- repo.CreateIssueDependency (calls)
- repo.RemoveIssueDependency (calls)
- repo.GetIssueBlocks (calls)
- repo.RemoveIssueBlocking (calls)
- repo.getPermissionForRepo (calls)
- repo.removeIssueDependency (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)

### Services

- access_model.GetDoerRepoPermission (serves)
- convert.ToRepo (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- service.DEFAULT_ENABLE_DEPENDENCIES (configured_by)
- service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- IssueMeta (uses_model)

### Error Handling

- 500 Blocking relationship already exists (handles_error)
- 500 Would create circular dependency (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/comments

- **Auth:** none
- **ID:** `ep-438`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/deadline

- **Auth:** none
- **ID:** `ep-475`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies

Make the issue in the URL depend on the issue specified in the body

- **Auth:** bearer
- **ID:** `ep-209`

### Controller

- issue (serves)
- repo.CreateIssueDependency (serves)
- repo.CreateIssueDependency (data_flow)
- repo.getParamsIssue (data_flow)
- repo.getFormIssue (data_flow)
- repo.getPermissionForRepo (data_flow)
- repo.createIssueDependency (data_flow)
- repo.RemoveIssueDependency (calls)
- repo.GetIssueBlocks (calls)
- repo.CreateIssueBlocking (calls)
- repo.RemoveIssueBlocking (calls)
- repo.removeIssueDependency (calls)
- user.listUserRepos (calls)
- user.ListMyRepos (calls)
- repo.GetByID (calls)
- user.ListUserRepos (calls)
- user.ListOrgRepos (calls)
- repo.Get (calls)

### Services

- access_model.GetDoerRepoPermission (serves)
- convert.ToRepo (calls)
- user.getStarredRepos (calls)
- user.getWatchedRepos (calls)
- repo_service.FindForks (calls)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- service.DEFAULT_ENABLE_DEPENDENCIES (configured_by)
- service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES (configured_by)

### Models

- IssueDependency (uses_model)
- Issue (uses_model)
- IssueMeta (uses_model)

### Error Handling

- 400 Different repo and AllowCrossRepositoryDependencies=false (handles_error)
- 500 Dependency already exists (handles_error)
- 500 Would create circular dependency (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels

Add labels to an issue

- **Auth:** bearer
- **ID:** `ep-336`

### Controller

- issue (serves)
- repo.AddIssueLabels (serves)
- repo.AddIssueLabels (data_flow)

### Services

- issue_service.AddLabels (data_flow)
- issue_service (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- issues_model.Label (uses_model)
- issues_model.IssueLabel (uses_model)

### Error Handling

- 404 Invalid issue index (handles_error)
- 403 No write access (handles_error)
- 400 Non-int/string in labels array (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/pin

Pin an issue to the repository

- **Auth:** bearer
- **ID:** `ep-376`

### Controller

- issue (serves)
- repo.PinIssue (serves)
- repo.PinIssue (data_flow)
- repo.CheckIssueSubscription (calls)
- repo.GetIssueSubscribers (calls)
- repo.GetIssueAttachment (calls)
- repo.ListIssueAttachments (calls)
- repo.ListIssueLabels (calls)
- repo.GetIssueDependencies (calls)

### Services

- issues_model.PinIssue (data_flow)
- issues_model (serves)
- Repository.IsDependenciesEnabled (calls)
- access_model.GetDoerRepoPermission (calls)
- attachment_service.UpdateAttachment (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- repository.issue.MAX_PINNED (configured_by)

### Models

- issues_model.IssuePin (uses_model)
- issues_model.Issue (uses_model)

### Error Handling

- 404 Issue index not found in repo (handles_error)
- 400 Max pin count reached (handles_error)
- 500 DB failure (handles_error)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions

Add a reaction to an issue

- **Auth:** token
- **ID:** `ep-304`

### Controller

- issue (serves)
- repo.PostIssueReaction (serves)
- repo.PostIssueReaction (data_flow)
- repo.changeIssueReaction (data_flow)
- repo.DeleteIssueReaction (calls)
- repo.changeIssueCommentReaction (calls)

### Services

- issue_service.CreateIssueReaction (serves)
- issue_service.CreateCommentReaction (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- ui.REACTIONS (configured_by)

### Models

- issues_model.Reaction (uses_model)
- issues_model.Issue (uses_model)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start

- **Auth:** none
- **ID:** `ep-382`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop

- **Auth:** none
- **ID:** `ep-383`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/issues/{index}/times

- **Auth:** none
- **ID:** `ep-408`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/keys

Add a deploy key to a repository

- **Auth:** bearer
- **ID:** `ep-342`

### Controller

- repository (serves)
- repo.CreateDeployKey (serves)
- repo.CreateDeployKey (data_flow)
- user.CreateUserPublicKey (calls)
- admin.CreatePublicKey (calls)
- user.CreatePublicKey (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Config

- SSH.MinimumKeySizeCheck (configured_by)

### Models

- asymkey_model.DeployKey (uses_model)
- asymkey_model.PublicKey (uses_model)

### Error Handling

- 422 SSH is disabled in config (handles_error)
- 422 Cannot verify key content (handles_error)
- 422 Same key already added to repo (handles_error)
- 422 Key name already used in repo (handles_error)

## POST /api/v1/repos/{owner}/{repo}/labels

Create a label for a repository

- **Auth:** bearer
- **ID:** `ep-359`

### Controller

- issue (serves)
- repo.CreateLabel (serves)
- repo.CreateLabel (data_flow)
- org.CreateLabel (calls)
- org.EditLabel (calls)
- org.GetLabel (calls)
- repo.GetLabel (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)

### Models

- issues_model.Label (uses_model)

### Error Handling

- 422 Color fails regex validation (handles_error)
- 500 Insert fails (handles_error)

## POST /api/v1/repos/{owner}/{repo}/merge-upstream

Merge a branch from the upstream (base) repository into the fork

- **Auth:** bearer
- **ID:** `ep-318`

### Controller

- repository (serves)
- repo.MergeUpstream (serves)
- repo.MergeUpstream (data_flow)

### Services

- repository.MergeUpstream (serves)
- repository.GetUpstreamDivergingInfo (data_flow)
- pull.Update (data_flow)
- checkBranchName (calls)
- convert.ToBranch (calls)
- repo_service.CreateNewBranchFromCommit (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- Repository (uses_model)

### Error Handling

- 400 Repo not a fork, archived, or ff_only failed (handles_error)
- 404 Branch or repo not found (handles_error)

## POST /api/v1/repos/{owner}/{repo}/milestones

- **Auth:** none
- **ID:** `ep-466`

### Controller

- issue (serves)

## POST /api/v1/repos/{owner}/{repo}/mirror-sync

Adds a mirrored (pull) repository to the sync queue

- **Auth:** bearer
- **ID:** `ep-234`

### Controller

- repository (serves)
- repo.MirrorSync (serves)
- repo.MirrorSync (data_flow)

### Services

- mirror_service.AddPullMirrorToQueue (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Config

- mirror.ENABLED (configured_by)

### Models

- repo_model.Mirror (uses_model)

### Error Handling

- 400 Repo has no mirror record (handles_error)
- 500 GetMirrorByRepoID fails (handles_error)

## POST /api/v1/repos/{owner}/{repo}/pulls

Create a new pull request

- **Auth:** bearer
- **ID:** `ep-226`

### Controller

- repository (serves)
- repo.CreatePullRequest (serves)
- repo.CreatePullRequest (data_flow)
- repo.GetCommitPullRequest (calls)

### Services

- pull_service.NewPullRequest (data_flow)
- pull_service (serves)
- convert (serves)
- git_service (serves)
- pull_service.StartPullRequestCheckOnView (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- PR creator must be collaborator/member/org-member or have write on head repo (enforces)

### Models

- issues_model.PullRequest (uses_model)
- issues_model.Issue (uses_model)
- git_service.CompareInfo (uses_model)

### Error Handling

- 409 Unmerged PR with same targets exists (handles_error)
- 403 Poster blocked by repo owner (handles_error)
- 403 User not collaborator/member (handles_error)

## POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/resolve

- **Auth:** none
- **ID:** `ep-455`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/unresolve

- **Auth:** none
- **ID:** `ep-456`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies

- **Auth:** none
- **ID:** `ep-454`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

Merge a pull request or schedule auto-merge

- **Auth:** bearer
- **ID:** `ep-229`

### Controller

- repository (serves)
- repo.MergePullRequest (serves)
- repo.MergePullRequest (data_flow)

### Services

- pull_service.CheckPullMergeable (data_flow)
- pull_service.MergedManually (data_flow)
- pull_service.GetDefaultMergeMessage (data_flow)
- automerge.ScheduleAutoMerge (data_flow)
- pull_service.Merge (data_flow)
- repo_service.DeleteBranchAfterMerge (data_flow)
- pull_service (serves)
- automerge (serves)

### Business Rules

- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- repository.PULL_REQUEST_DEFAULT_MERGE_STYLE (configured_by)

### Models

- issues_model.PullRequest (uses_model)
- issues_model.Issue (uses_model)
- pull_model.AutoMerge (uses_model)

### Error Handling

- 404 PR issue is closed (handles_error)
- 405 User lacks merge permission (handles_error)
- 405 PR title has WIP prefix (handles_error)
- 409 Git merge conflict (handles_error)
- 405 Merge style not allowed for repo (handles_error)
- 409 Auto-merge already scheduled (handles_error)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers

- **Auth:** none
- **ID:** `ep-460`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews

- **Auth:** none
- **ID:** `ep-458`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}

- **Auth:** none
- **ID:** `ep-459`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals

- **Auth:** none
- **ID:** `ep-462`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals

- **Auth:** none
- **ID:** `ep-463`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update

Merge PR's base branch into head branch (update PR)

- **Auth:** bearer
- **ID:** `ep-230`

### Controller

- repository (serves)
- repo.UpdatePullRequest (serves)
- repo.UpdatePullRequest (data_flow)

### Services

- pull_service.IsUserAllowedToUpdate (data_flow)
- pull_service.Update (data_flow)
- pull_service (serves)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- issues_model.PullRequest (uses_model)

## POST /api/v1/repos/{owner}/{repo}/push_mirrors

Creates a new push mirror for a repository

- **Auth:** bearer
- **ID:** `ep-238`

### Controller

- repository (serves)
- repo.AddPushMirror (serves)
- repo.AddPushMirror (data_flow)
- repo.CreatePushMirror (data_flow)
- repo.ListPushMirrors (calls)
- repo.GetPushMirrorByName (calls)

### Services

- mirror_service.AddPushMirrorRemote (serves)
- convert.ToPushMirror (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- mirror.ENABLED (configured_by)
- mirror.MIN_INTERVAL (configured_by)

### Models

- repo_model.PushMirror (uses_model)
- api.PushMirror (uses_model)
- api.CreatePushMirrorOption (uses_model)

## POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync

Syncs all push mirrors of a repository by triggering each one

- **Auth:** bearer
- **ID:** `ep-235`

### Controller

- repository (serves)
- repo.PushMirrorSync (serves)
- repo.PushMirrorSync (data_flow)

### Services

- mirror_service.SyncPushMirror (serves)

### External APIs

- Git Remote (Push Mirror Target) (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- mirror.ENABLED (configured_by)
- git.TIMEOUT.MIRROR (configured_by)
- lfs.START_SERVER (configured_by)

### Models

- repo_model.PushMirror (uses_model)

### Error Handling

- 404 GetPushMirrorsByRepoID fails (handles_error)
- 500 SyncPushMirror returns false (handles_error)

## POST /api/v1/repos/{owner}/{repo}/releases

Create a new release or convert an existing tag to a release

- **Auth:** bearer (write:repository scope)
- **ID:** `ep-243`

### Controller

- repository (serves)
- repo.CreateRelease (serves)
- repo.CreateRelease (data_flow)
- repo.EditRelease (calls)
- repo.GetLatestRelease (calls)

### Services

- release_service.CreateRelease (serves)
- createTag (data_flow)
- release_service.UpdateRelease (tag-to-release path) (data_flow)
- release_service.UpdateRelease (serves)

### External APIs

- Git Repository (local filesystem) (integrates)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- repo_model.Release (uses_model)
- git_model.ProtectedTag (uses_model)

### Error Handling

- 409 Tag name already has a release (handles_error)
- 422 Tag is protected (handles_error)
- 404 Target commit/branch not found (handles_error)

## POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets

Upload a file attachment to a release

- **Auth:** token (write access required)
- **ID:** `ep-354`

### Controller

- repository (serves)
- repo.CreateReleaseAttachment (serves)
- repo.CreateReleaseAttachment (data_flow)
- repo.GetReleaseAttachment (calls)
- repo.EditReleaseAttachment (calls)
- repo.DeleteReleaseAttachment (calls)

### Services

- attachment_service.UploadAttachmentForRelease (data_flow)
- attachment_service (serves)
- convert (serves)
- attachment_service.UpdateAttachment (calls)

### External APIs

- Object Storage (Attachments) (integrates)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- attachment.ENABLED (configured_by)
- repository.release.ALLOWED_TYPES (configured_by)
- repository.release.FILE_MAX_SIZE (configured_by)
- server.APP_URL (configured_by)

### Models

- repo_model.Attachment (uses_model)
- repo_model.Release (uses_model)

### Error Handling

- 400 File type not in allowed list (handles_error)
- 413 File exceeds max size (handles_error)

## POST /api/v1/repos/{owner}/{repo}/statuses/{sha}

- **Auth:** none
- **ID:** `ep-429`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/tag_protections

- **Auth:** none
- **ID:** `ep-421`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/tags

- **Auth:** none
- **ID:** `ep-417`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/transfer

- **Auth:** none
- **ID:** `ep-404`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/transfer/accept

- **Auth:** none
- **ID:** `ep-405`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/transfer/reject

- **Auth:** none
- **ID:** `ep-406`

### Controller

- repository (serves)

## POST /api/v1/repos/{owner}/{repo}/wiki/new

- **Auth:** none
- **ID:** `ep-445`

### Controller

- repository (serves)

## POST /api/v1/repos/{template_owner}/{template_repo}/generate

Create a repository using a template

- **Auth:** bearer
- **ID:** `ep-364`

### Controller

- repository (serves)
- repo.Generate (serves)
- repo.Generate (data_flow)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- org.CheckUserBlock (calls)
- user.CheckUserBlock (calls)
- org.BlockUser (calls)
- user.BlockUser (calls)
- org.UnblockUser (calls)
- user.UnblockUser (calls)

### Services

- repo_service.GenerateRepository (serves)
- shared.CheckUserBlock (calls)
- shared.BlockUser (calls)
- user_service.BlockUser (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Config

- repository.FORCE_PRIVATE (configured_by)

### Models

- repo_model.Repository (uses_model)
- user_model.User (uses_model)

## POST /api/v1/user/actions/runners/registration-token

Get a user's actions runner registration token

- **Auth:** bearer
- **ID:** `ep-175`

### Controller

- user (serves)
- user.CreateRegistrationToken (serves)
- user.CreateRegistrationToken (data_flow)
- admin.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- actions_model.ActionRunnerToken (uses_model)

## POST /api/v1/user/actions/variables/{variablename}

Creates a user-level variable

- **Auth:** bearer
- **ID:** `ep-132`

### Controller

- user (serves)
- user.CreateVariable (serves)
- user.CreateVariable (data_flow)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service.CreateVariable (data_flow)
- actions_service (serves)
- actions_service.UpdateVariableNameData (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- ActionVariable (uses_model)

## POST /api/v1/user/applications/oauth2

Create a new OAuth2 application for the authenticated user

- **Auth:** token
- **ID:** `ep-167`

### Controller

- user (serves)
- user.CreateOauth2Application (serves)
- user.CreateOauth2Application (data_flow)
- user.ListOauth2Applications (calls)
- user.GetOauth2Application (calls)
- user.UpdateOauth2Application (calls)

### Services

- forms.DetectInvalidOAuth2ApplicationRedirectURI (serves)
- OAuth2Application.GenerateClientSecret (data_flow)
- convert.ToOAuth2Application (serves)
- auth_model.UpdateOAuth2Application (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- setting.OAuth2.CustomSchemes (configured_by)

### Models

- auth_model.OAuth2Application (uses_model)

### Error Handling

- 400 Redirect URI fails validation (handles_error)
- 400 DB insert fails (handles_error)
- 400 bcrypt or DB update fails (handles_error)

## POST /api/v1/user/avatar

Update the authenticated user's avatar with a base64-encoded image

- **Auth:** bearer|basic (required)
- **ID:** `ep-128`

### Controller

- user (serves)
- user.UpdateAvatar (serves)
- user.UpdateAvatar (data_flow)
- org.UpdateAvatar (calls)
- repo.UpdateAvatar (calls)

### Services

- user_service.UploadAvatar (serves)
- repo_service.UploadAvatar (calls)

### External APIs

- Avatar Storage (integrates)

### Business Rules

- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- Avatar.MaxWidth (configured_by)
- Avatar.MaxHeight (configured_by)
- Avatar.MaxOriginSize (configured_by)

### Models

- user_model.User (uses_model)

### Error Handling

- 400 Invalid base64 in image field (handles_error)
- 500 Unsupported type or oversized image (handles_error)
- 500 Failed to save avatar to storage (handles_error)

## POST /api/v1/user/emails

Add email addresses to the authenticated user

- **Auth:** bearer
- **ID:** `ep-181`

### Controller

- user (serves)
- user.AddEmail (serves)
- user.AddEmail (data_flow)
- user.ListEmails (calls)

### Services

- user_service.AddEmailAddresses (serves)
- convert.ToEmail (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- service.RegisterEmailConfirm (configured_by)

### Models

- EmailAddress (uses_model)

### Error Handling

- 422 Email already registered (handles_error)
- 422 Invalid email format (handles_error)

## POST /api/v1/user/gpg_key_verify

Verify a GPG key by providing a signed token

- **Auth:** bearer
- **ID:** `ep-187`

### Controller

- user (serves)
- user.VerifyUserGPGKey (serves)
- user.VerifyUserGPGKey (data_flow)
- user.listGPGKeys (calls)
- user.GetVerificationToken (calls)
- user.ListGPGKeys (calls)
- user.ListMyGPGKeys (calls)

### Services

- asymkey_model.VerifyGPGKey (serves)
- convert.ToGPGKey (serves)
- asymkey_model.VerificationToken (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)

### Models

- asymkey_model.GPGKey (uses_model)
- api.GPGKey (uses_model)
- api.VerifyGPGKeyOption (uses_model)

### Error Handling

- 404 KeyID is all zeros (handles_error)
- 422 Signature doesn't match token (handles_error)
- 404 Key not found after verification (handles_error)

## POST /api/v1/user/gpg_keys

Create a GPG key for the authenticated user

- **Auth:** bearer
- **ID:** `ep-188`

### Controller

- user (serves)
- user.CreateGPGKey (serves)
- user.CreateGPGKey (data_flow)
- user.CreateUserGPGKey (data_flow)
- user.listGPGKeys (calls)
- user.GetVerificationToken (calls)
- user.ListGPGKeys (calls)
- user.ListMyGPGKeys (calls)

### Services

- asymkey_model.AddGPGKey (serves)
- convert.ToGPGKey (serves)
- asymkey_model.VerificationToken (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- admin.USER_DISABLED_FEATURES / admin.EXTERNAL_USER_DISABLE_FEATURES (configured_by)
- setting.UserFeatureManageGPGKeys (configured_by)

### Models

- asymkey_model.GPGKey (uses_model)
- asymkey_model.GPGKeyImport (uses_model)
- api.GPGKey (uses_model)
- api.CreateGPGKeyOption (uses_model)

### Error Handling

- 404 manage_gpg_keys in disabled features (handles_error)
- 422 Duplicate key_id (handles_error)
- 422 Invalid armored key format (handles_error)
- 404 No matching activated email (handles_error)
- 422 Signature verification failed (handles_error)

## POST /api/v1/user/hooks

Create a webhook for the authenticated user

- **Auth:** bearer
- **ID:** `ep-149`

### Controller

- user (serves)
- user.CreateHook (serves)
- user.CreateHook (data_flow)
- org.CreateHook (calls)
- admin.CreateHook (calls)
- repo.ListHooks (calls)
- repo.GetHook (calls)

### Services

- webhook_service (serves)
- utils (serves)
- webhook_service.ToHook (calls)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- SecretKey (configured_by)

### Models

- webhook.Webhook (uses_model)

### Error Handling

- 422 invalid type/url/content_type (handles_error)
- 400 invalid slack channel (handles_error)

## POST /api/v1/user/keys

Create a public SSH key for the authenticated user

- **Auth:** bearer
- **ID:** `ep-160`

### Controller

- user (serves)
- user.CreatePublicKey (serves)
- user.CreatePublicKey (data_flow)
- user.CreateUserPublicKey (data_flow)
- admin.CreatePublicKey (calls)
- repo.CreateDeployKey (calls)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Config

- admin.USER_DISABLED_FEATURES (configured_by)
- admin.EXTERNAL_USER_DISABLE_FEATURES (configured_by)
- ssh.MINIMUM_KEY_SIZE_CHECK (configured_by)

### Models

- asymkey_model.PublicKey (uses_model)

### Error Handling

- 404 IsFeatureDisabledWithLoginType returns true (handles_error)
- 422 Key content cannot be verified (handles_error)
- 422 Fingerprint already exists (handles_error)
- 422 Name already used by owner (handles_error)

## POST /api/v1/user/repos

Create a repository for the authenticated user

- **Auth:** bearer
- **ID:** `ep-363`

### Controller

- repository (serves)
- repo.Create (serves)
- repo.Create (data_flow)
- repo.CreateUserRepo (data_flow)
- admin.CreateRepo (calls)
- prepareDoerCreateRepoInOrg (calls)
- repo.CreateOrgRepo (calls)

### Services

- repo_service.CreateRepository (serves)
- repo_service.CreateRepositoryDirectly (data_flow)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Config

- repository.FORCE_PRIVATE (configured_by)

### Models

- repo_model.Repository (uses_model)

### Error Handling

- 409 Repo with same name exists (handles_error)
- 422 Name is reserved (handles_error)

## POST /api/v1/users/{username}/tokens

Create a new access token for the user

- **Auth:** basic_or_reverse_proxy+token
- **ID:** `ep-165`

### Controller

- user (serves)
- user.CreateAccessToken (serves)
- user.CreateAccessToken (data_flow)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.SuccessfulTokensCacheSize (configured_by)

### Models

- auth_model.AccessToken (uses_model)

### Error Handling

- 400 Token name already used by this user (handles_error)
- 400 Scope string contains invalid scope names (handles_error)
- 400 No valid scopes after normalization (handles_error)

## PUT /api/v1/notifications

Mark notification threads as read, unread, or pinned for the current user

- **Auth:** bearer (notification scope, write)
- **ID:** `ep-020`

### Controller

- notification (serves)
- notify.ReadNotifications (serves)
- notify.ReadNotifications (data_flow)
- notify.ListRepoNotifications (set RepoID) (calls)
- notify.ReadRepoNotifications (calls)
- notify.getThread (calls)

### Services

- convert.ToNotificationThread (serves)
- convert.ToNotifications (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- Notification (uses_model)
- NotificationThread (uses_model)

### Error Handling

- 400 Invalid RFC3339 last_read_at parameter (handles_error)
- 500 DB failure during find or update (handles_error)
- 500 SetNotificationStatus called for notification not owned by u (handles_error)

## PUT /api/v1/orgs/{org}/actions/secrets/{secretname}

Create or update a secret value in an organization

- **Auth:** bearer (reqToken + reqOrgOwnership)
- **ID:** `ep-040`

### Controller

- organization (serves)
- org.Action.CreateOrUpdateSecret (serves)
- org.Action.CreateOrUpdateSecret (data_flow)
- org.DeleteOrgRepos (calls)
- org.UpdateAvatar (calls)
- org.DeleteAvatar (calls)
- org.Action.ListActionsSecrets (calls)
- org.Action.DeleteSecret (calls)
- user.CreateOrUpdateSecret (calls)
- Action.CreateOrUpdateSecret (calls)

### Services

- secret_service.CreateOrUpdateSecret (data_flow)
- secret_service (serves)
- org.deleteOrgReposBackground (calls)
- user_service.UploadAvatar (calls)
- user_service.DeleteAvatar (calls)
- secret_service.DeleteSecretByName (calls)

### Business Rules

- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Config

- SECRET_KEY (configured_by)

### Models

- secret_model.Secret (uses_model)

### Error Handling

- 400 invalid secret name or data too long (handles_error)
- 404 secret not found (should not happen for create) (handles_error)

## PUT /api/v1/orgs/{org}/actions/variables/{variablename}

Update an org-level variable

- **Auth:** bearer
- **ID:** `ep-047`

### Controller

- organization (serves)
- org.Action.UpdateVariable (serves)
- Action.UpdateVariable (data_flow)
- org.ListMembers (calls)
- listMembers (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- admin.CreateRegistrationToken (calls)
- user.CreateRegistrationToken (calls)
- Action.CreateRegistrationToken (calls)
- user.DeleteVariable (calls)
- Action.DeleteVariable (calls)
- admin.ListRunners (calls)
- user.ListRunners (calls)
- Action.ListRunners (calls)
- user.GetRunner (calls)
- Action.GetRunner (calls)
- org.ListOrgActivityFeeds (calls)
- reqOrgMembership() (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- actions_service.GetVariable (serves)
- actions_service.UpdateVariableNameData (serves)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- actions_service.CreateVariable (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToActionRunner (calls)
- shared.getRunnerByID (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- ActionVariable (uses_model)

### Error Handling

- 404 Variable not found by name (handles_error)
- 400 Invalid new name or data too long (handles_error)

## PUT /api/v1/orgs/{org}/blocks/{username}

Block a user from the organization

- **Auth:** token
- **ID:** `ep-089`

### Controller

- organization (serves)
- org.BlockUser (serves)
- org.BlockUser (data_flow)
- user.BlockUser (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)
- org.CheckUserBlock (calls)
- user.CheckUserBlock (calls)
- org.UnblockUser (calls)
- user.UnblockUser (calls)

### Services

- shared.BlockUser (data_flow)
- user_service.BlockUser (serves)
- shared.CheckUserBlock (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 400 Block not permitted (self, member, already blocked) (handles_error)
- 400 Target is an organization (handles_error)

## PUT /api/v1/orgs/{org}/public_members/{username}

Publicize a user's membership in an organization. Sets is_public=true on the org_user record.

- **Auth:** bearer
- **ID:** `ep-074`

### Controller

- organization (serves)
- org.PublicizeMember (serves)
- org.ListMembers (calls)
- listMembers (calls)
- orgAssignment(false, true) (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)

### Services

- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)

### Models

- organization.OrgUser (uses_model)
- user_model.User (uses_model)

### Error Handling

- 403 Doer is not target, not admin, not org owner (handles_error)
- 500 ChangeOrgUserStatus fails (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}

Create or update a secret value in a repository

- **Auth:** bearer
- **ID:** `ep-265`

### Controller

- repository (serves)
- Action.CreateOrUpdateSecret (serves)
- Action.CreateOrUpdateSecret (data_flow)
- org.Action.CreateOrUpdateSecret (calls)
- user.CreateOrUpdateSecret (calls)

### Services

- secret_service.CreateOrUpdateSecret (data_flow)
- secret_service (services/secrets) (serves)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- secret_model.Secret (uses_model)

### Error Handling

- 400 Invalid secret name format (handles_error)
- 404 Secret not found for update (handles_error)
- 500 Secret key misconfiguration (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}

Update a repo-level variable

- **Auth:** bearer
- **ID:** `ep-270`

### Controller

- repository (serves)
- Action.UpdateVariable (serves)
- Action.UpdateVariable (data_flow)
- user.CreateVariable (calls)
- user.UpdateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- Action.CreateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service.UpdateVariableNameData (data_flow)
- actions_service (serves)
- actions_service.CreateVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- ActionVariable (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable

Disable a workflow

- **Auth:** bearer
- **ID:** `ep-282`

### Controller

- repository (serves)
- repo.ActionsDisableWorkflow (serves)
- ActionsDisableWorkflow (data_flow)
- ActionsEnableWorkflow (calls)

### Services

- actions_service.EnableOrDisableWorkflow (serves)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- RepoUnit (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable

Enable a workflow

- **Auth:** bearer
- **ID:** `ep-284`

### Controller

- repository (serves)
- repo.ActionsEnableWorkflow (serves)
- ActionsEnableWorkflow (data_flow)
- ActionsDisableWorkflow (calls)

### Services

- actions_service.EnableOrDisableWorkflow (serves)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Models

- RepoUnit (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/branches/{branch}

Update a branch reference to a new commit

- **Auth:** bearer
- **ID:** `ep-310`

### Controller

- repository (serves)
- repo.UpdateBranch (serves)
- repo.UpdateBranch (data_flow)

### Services

- repo_service.UpdateBranch (serves)
- checkBranchName (calls)
- convert.ToBranch (calls)
- repository.GetUpstreamDivergingInfo (calls)
- pull.Update (calls)
- repo_service.CreateNewBranchFromCommit (calls)
- repository.MergeUpstream (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- git_model.Branch (uses_model)

### Error Handling

- 404 Branch not found or deleted (handles_error)
- 422 Commit mismatch or force push without flag (handles_error)
- 403 Pre-receive hook rejects push (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}

Add or update a collaborator to a repository with specified permission level

- **Auth:** bearer
- **ID:** `ep-252`

### Controller

- repository (serves)
- repo.AddOrUpdateCollaborator (serves)
- repo.AddOrUpdateCollaborator (data_flow)

### Services

- repo_service.AddOrUpdateCollaborator (serves)

### Business Rules

- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)

### Models

- repo_model.Collaboration (uses_model)
- api.AddCollaboratorOption (uses_model)

### Error Handling

- 403 User blocked by repo owner or vice versa (handles_error)
- 500 Collaborator account is not active (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/contents/{filepath}

- **Auth:** none
- **ID:** `ep-396`

### Controller

- repository (serves)

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/labels

Replace all labels on an issue

- **Auth:** bearer
- **ID:** `ep-338`

### Controller

- issue (serves)
- repo.ReplaceIssueLabels (serves)
- repo.ReplaceIssueLabels (data_flow)

### Services

- issue_service.ReplaceLabels (data_flow)
- issue_service (serves)
- issue_service.ChangeMilestoneAssign (calls)
- pull_service.ChangeTargetBranch (calls)
- issue_service.UpdateAssignees (calls)
- pull_service.SetAllowEdits (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- issues_model.Label (uses_model)
- issues_model.IssueLabel (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/lock

Lock an issue to restrict commenting to users with write access

- **Auth:** bearer
- **ID:** `ep-319`

### Controller

- issue (serves)
- repo.LockIssue (serves)
- repo.LockIssue (data_flow)

### Services

- issues_model.LockIssue (serves)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Models

- Issue (uses_model)

### Error Handling

- 404 Issue index not found in repo (handles_error)
- 403 No write access to issues/pulls (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}

Subscribe a user to an issue

- **Auth:** token
- **ID:** `ep-218`

### Controller

- issue (serves)
- repo.AddIssueSubscription (serves)
- repo.AddIssueSubscription (data_flow)
- repo.DelIssueSubscription (calls)

### Services

- repo.setIssueSubscription (data_flow)

### Business Rules

- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Models

- issues.IssueWatch (uses_model)
- issues.Issue (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/notifications

Mark notification threads as read, pinned or unread on a specific repo

- **Auth:** token
- **ID:** `ep-023`

### Controller

- notification (serves)
- notify.ReadRepoNotifications (serves)
- notify.ReadRepoNotifications (data_flow)
- notify.ReadNotifications (calls)
- notify.getThread (calls)

### Services

- convert.ToNotificationThread (serves)

### Business Rules

- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Models

- activities_model.Notification (uses_model)
- structs.NotificationThread (uses_model)

### Error Handling

- 400 Invalid RFC3339 last_read_at (handles_error)
- 500 db.Find or SetNotificationStatus fails (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/subscription

Watch a repo (subscribe to notifications)

- **Auth:** bearer
- **ID:** `ep-197`

### Controller

- repository (serves)
- user.Watch (serves)
- user.Watch (data_flow)
- user.Unwatch (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- service.auto_watch_on_changes (configured_by)

### Models

- repo_model.Watch (uses_model)
- api.WatchInfo (uses_model)

### Error Handling

- 403 User is blocked by repo owner (handles_error)
- 500 DB error in WatchRepo (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/teams/{team}

Add a team to a repository

- **Auth:** bearer
- **ID:** `ep-331`

### Controller

- repository (serves)
- repo.AddTeam (serves)
- repo.AddTeam (data_flow)
- repo.changeRepoTeam (data_flow)
- repo.DeleteTeam (calls)
- repo.IsTeam (calls)
- reqTeamMembership (calls)

### Services

- repo_service.TeamAddRepository (serves)
- repo_service.HasRepository (serves)
- repo_service.RemoveRepositoryFromTeam (calls)
- convert.ToTeam (calls)
- org_service.NewTeam (calls)
- org_service.UpdateTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)

### Config

- service.AUTO_WATCH_NEW_REPOS (configured_by)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)

### Error Handling

- 405 repo owner is not organization (handles_error)
- 403 user not admin/owner (handles_error)
- 422 team already assigned (handles_error)

## PUT /api/v1/repos/{owner}/{repo}/topics

Replace list of topics for a repository

- **Auth:** bearer (write access required)
- **ID:** `ep-348`

### Controller

- repository (serves)
- repo.UpdateTopics (serves)
- UpdateTopics (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- repo_model.Topic (uses_model)
- repo_model.RepoTopic (uses_model)

## PUT /api/v1/repos/{owner}/{repo}/topics/{topic}

Add a topic to a repository

- **Auth:** bearer (write access required)
- **ID:** `ep-349`

### Controller

- repository (serves)
- repo.AddTopic (serves)
- AddTopic (data_flow)

### Business Rules

- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Generate repo requires at least one template option to be selected (enforces)
- Org repo creation requires user to have create permission in org (enforces)

### Models

- repo_model.Topic (uses_model)
- repo_model.RepoTopic (uses_model)

## PUT /api/v1/teams/{id}/members/{username}

Add a team member

- **Auth:** token
- **ID:** `ep-062`

### Controller

- organization (serves)
- org.AddTeamMember (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- reqTeamMembership() (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.AddTeamRepository (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- org.ListMembers (calls)
- listMembers (calls)

### Services

- org_service.AddTeamMember (serves)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin position must be >= 1 (enforces)
- Unarchiving a repo re-detects action schedules (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- service.AutoWatchNewRepos (configured_by)

### Models

- organization.Team (uses_model)
- organization.TeamUser (uses_model)
- user_model.User (uses_model)

### Error Handling

- 403 user is blocked by org (handles_error)

## PUT /api/v1/teams/{id}/repos/{org}/{repo}

Add a repository to a team

- **Auth:** token
- **ID:** `ep-066`

### Controller

- organization (serves)
- org.AddTeamRepository (serves)
- orgAssignment(false, true) (data_flow)
- reqTeamMembership() (data_flow)
- org.AddTeamRepository (data_flow)
- reqTeamMembership (calls)
- org.GetTeamMembers (calls)
- org.GetTeamRepos (calls)
- org.GetTeamRepo (calls)
- org.RemoveTeamRepository (calls)
- org.ListTeamActivityFeeds (calls)
- repo.changeRepoTeam (calls)
- Action.ListVariables (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- org.EditTeam (calls)
- org.IsMember (calls)
- org.IsPublicMember (calls)
- repo.AddTeam (calls)
- repo.DeleteTeam (calls)

### Services

- repo_service.TeamAddRepository (serves)
- convert.ToTeam (calls)
- actions_service.GetVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)
- org_service.AddTeamMember (calls)
- org_service.RemoveTeamMember (calls)
- org_service.RemoveOrgUser (calls)
- repo_service.RemoveRepositoryFromTeam (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)

### Config

- service.AUTO_WATCH_NEW_REPOS (configured_by)

### Models

- organization.Team (uses_model)
- organization.TeamRepo (uses_model)
- repo_model.Repository (uses_model)

### Error Handling

- 404 repo name not found (handles_error)
- 403 user lacks admin access (handles_error)
- 500 TeamAddRepository fails (handles_error)

## PUT /api/v1/user/actions/secrets/{secretname}

Creates or updates a secret value in the user scope

- **Auth:** bearer
- **ID:** `ep-130`

### Controller

- user (serves)
- user.CreateOrUpdateSecret (serves)
- user.CreateOrUpdateSecret (data_flow)
- org.Action.CreateOrUpdateSecret (calls)
- Action.CreateOrUpdateSecret (calls)

### Services

- secret_service.CreateOrUpdateSecret (data_flow)
- secret_service (serves)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)

### Config

- SECRET_KEY (configured_by)

### Models

- Secret (uses_model)

### Error Handling

- 400 Invalid secret name format (handles_error)
- 404 Secret not found (unlikely in create/update) (handles_error)
- 500 EncryptSecret or DB operation fails (handles_error)

## PUT /api/v1/user/actions/variables/{variablename}

Updates a user-level variable created by current doer

- **Auth:** bearer
- **ID:** `ep-133`

### Controller

- user (serves)
- user.UpdateVariable (serves)
- user.UpdateVariable (data_flow)
- user.CreateVariable (calls)
- user.GetVariable (calls)
- Action.GetVariable (calls)
- Action.CreateVariable (calls)
- Action.UpdateVariable (calls)
- Action.ListVariables (calls)
- orgAssignment(true) (calls)
- org.CreateTeam (calls)
- orgAssignment(false, true) (calls)
- org.EditTeam (calls)

### Services

- actions_service.GetVariable (data_flow)
- actions_service.UpdateVariableNameData (data_flow)
- actions_service (serves)
- actions_service.CreateVariable (calls)
- actions_service.DeleteVariableByName (calls)
- org_service.DeleteTeam (calls)

### Business Rules

- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- ActionVariable (uses_model)

## PUT /api/v1/user/blocks/{username}

Block a user

- **Auth:** bearer
- **ID:** `ep-192`

### Controller

- user (serves)
- user.BlockUser (serves)
- user.BlockUser (data_flow)
- org.BlockUser (calls)
- repo.ListPullRequests (calls)
- repo.GetRepoPermissions (calls)
- repo.Generate (calls)

### Services

- shared.BlockUser (serves)
- user_service.BlockUser (serves)
- shared.CheckUserBlock (calls)
- shared.UnblockUser (calls)
- user_service.UnblockUser (calls)
- repo_service.GenerateRepository (calls)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)
- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Moving pin reorders other pins - shifts up or down depending on direction (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Unarchiving a repo re-detects action schedules (enforces)

### Models

- user_model.Blocking (uses_model)
- user_model.User (uses_model)

### Error Handling

- 404 GetUserByName returns error (handles_error)
- 400 CanBlockUser returns false (handles_error)
- 400 blockee is organization (handles_error)
- 500 Transaction fails (handles_error)

## PUT /api/v1/user/following/{username}

Follow a user

- **Auth:** bearer
- **ID:** `ep-145`

### Controller

- user (serves)
- user.Follow (serves)
- user.Follow (data_flow)

### Services

- user_model (serves)

### Business Rules

- Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M (enforces)
- Pin position must be >= 1 (enforces)
- Pin order is assigned as max existing order + 1 when pinning (enforces)

### Models

- user_model.Follow (uses_model)
- user_model.User (uses_model)

### Error Handling

- 403 user blocked by target or vice versa (handles_error)
- 500 DB failure (handles_error)

## PUT /api/v1/user/starred/{owner}/{repo}

Star the given repo as the authenticated user

- **Auth:** bearer
- **ID:** `ep-155`

### Controller

- user (serves)
- user.Star (serves)
- user.Star (data_flow)
- user.Unstar (calls)

### Services

- repo_model.StarRepo (serves)

### Business Rules

- Unpinning creates a comment of type CommentTypeUnpin in issue history (enforces)
- Pinned issues are separated by type (issues vs pull requests) (enforces)
- IsNewPinAllowed compares current pin count against MaxPinned setting (enforces)
- Language stats response is a custom JSON object mapping language name to byte co (enforces)
- Issue templates are parsed from multiple candidate directories in priority order (enforces)

### Config

- setting.Repository.DisableStars (configured_by)

### Models

- repo.Star (uses_model)
- user.Blocking (uses_model)

### Error Handling

- 403 User blocked by repo owner (handles_error)
