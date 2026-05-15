One or more mcp server did not load correctly. See $TMPDIR/kiro-log/kiro-chat.log for more details.
------
All tools are now trusted (!). Kiro will execute tools without asking for confirmation.
Agents can sometimes do unexpected things so understand the risks.

Learn more at https://kiro.dev/docs/cli/chat/security/#using-tools-trust-all-safely


📷 Checkpoints are enabled! (took 6.09s)


I'll share my reasoning process (using tool: thinking): The user wants a list of all API endpoints related to repository management in the Gitea codebase. This is a large codebase and the API routes are likely defined in a router file. Let me find where the API routes are defined.
 - Completed in 0.152s

> This is a massive request — Gitea has hundreds of repository API endpoints. Let me find the route definitions to give you a comprehensive answer.

Searching for: func registerAPIRoutes (*.go) (using tool: grep)Searching for files: routers/api/v1/**/*.go (using tool: glob)
 ❗ No matches found for pattern: func registerAPIRoutes under current directory
 - Completed in 0.468s


 ✓ Successfully found 125 files under current directory
 - Completed in 0.96s

Searching for: func Routes in /Users/relumalai/workshop/gitea/routers/api/v1 (*.go) (using tool: grep)
 ✓ Successfully found 1 matches in 1 files under /Users/relumalai/workshop/gitea/routers/api/v1
 - Completed in 0.143s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 1 to 50 (using tool: read)
 ✓ Successfully read 1375 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.119s

I'll share my reasoning process (using tool: thinking): The api.go file is the main router file. It's likely very large. Let me look at the repo-related route registrations. The file is probably hundreds of lines. Let me find the section that registers repo routes.
 - Completed in 0.134s

Searching for: m\.(Get|Post|Put|Delete|Patch)\( in /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: grep)
 ✓ Successfully found 254 matches in 1 files under /Users/relumalai/workshop/gitea/routers/api/v1/api.go (result is truncated)
 - Completed in 0.141s

I'll share my reasoning process (using tool: thinking): This file is very large with 254+ route definitions. The user is asking for ALL repository management endpoints. This is going to be an enormous list. Let me delegate this to a subagent that can read the full api.go file and extract all the repo-related routes. Actually, let me first check how long the file is and then read the relevant sections.
 - Completed in 0.134s

I will run the following command: wc -l /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: shell)
Purpose: Check line count of api.go

    1751 /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.121s

Searching for: repos/\{owner\}/\{repo\}|\"repos\" in /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: grep)
 ❗ No matches found for pattern: repos/\{owner\}/\{repo\}|\"repos\" under /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.97s

Searching for: repos|repo in /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: grep)
 ✓ Successfully found 397 matches in 1 files under /Users/relumalai/workshop/gitea/routers/api/v1/api.go (result is truncated)
 - Completed in 0.160s

Searching for: Group.*repo in /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: grep)
 ✓ Successfully found 8 matches in 1 files under /Users/relumalai/workshop/gitea/routers/api/v1/api.go (result is truncated)
 - Completed in 0.136s

I'll share my reasoning process (using tool: thinking): The main repo routes are in the Group("/repos") sections starting around line 1143 and 1454. Let me also check the section around 1097. Let me read these sections to get the full picture. This is a 1751-line file, so I'll need to read it in chunks. Let me delegate this to a subagent since it's a large extraction task.
 - Completed in 0.147s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 865 to 930 (using tool: read)
 ✓ Successfully read 2468 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.129s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 1090 to 1200 (using tool: read)
 ✓ Successfully read 4832 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.138s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 1200 to 1450 (using tool: read)
 ✓ Successfully read 14505 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.136s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 1450 to 1600 (using tool: read)
 ✓ Successfully read 7562 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.147s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 1600 to end of file (using tool: read)
 ✓ Successfully read 6898 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.121s

> Now let me also check the middleware/permission helper functions to understand the auth requirements:
Searching for: ^func (reqToken|reqOwner|reqAdmin|reqRepoReader|reqRepoWriter|reqAnyRepoReader|reqSiteAdmin) in /Users/relumalai/workshop/gitea/routers/api/v1/api.go (using tool: grep)
 ✓ Successfully found 7 matches in 1 files under /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.124s

Reading file: /Users/relumalai/workshop/gitea/routers/api/v1/api.go, from line 346 to 460 (using tool: read)
 ✓ Successfully read 3882 bytes from /Users/relumalai/workshop/gitea/routers/api/v1/api.go
 - Completed in 0.118s

I'll share my reasoning process (using tool: thinking): Now I have a comprehensive picture of the repository management API endpoints. This is a massive list. Let me organize it by category. The main repo routes are under `/repos/{username}/{reponame}` with the `tokenRequiresScopes(auth_model.AccessTokenScopeCategoryRepository)` scope.

Let me compile the full list. I'll organize by functional area for readability. The file location for all handlers is in `routers/api/v1/repo/` with specific files for each area.

Key permission middleware:
- `reqToken()` - requires authentication (token or session)
- `reqOwner()` - repo owner or site admin
- `reqAdmin()` - repo admin (owner/collaborator with admin) or site admin
- `reqRepoWriter(unitTypes...)` - write permission to specific unit types
- `reqRepoReader(unitType)` - read permission to specific unit type
- `reqAnyRepoReader()` - any read permission on the repo
- `reqSiteAdmin()` - site admin only
- `tokenRequiresScopes(...)` - token must have specific scope

The base path for all repo endpoints is `/api/v1/repos/{username}/{reponame}` unless otherwise noted.

This is going to be a very long response. Let me structure it well.

 - Completed in 0.116s

> Here's the comprehensive list of repository management API endpoints from routers/api/v1/api.go. All paths are prefixed with /api/v1. Handler functions are in routers/api/v1/repo/ unless noted otherwise.

## Permission Legend

| Middleware | Meaning |
|---|---|
| reqToken() | Authenticated (token/session required) |
| reqOwner() | Repo owner or site admin |
| reqAdmin() | Repo admin (owner/collaborator with admin write) or site admin |
| reqRepoWriter(unit) | Write permission on specific unit type |
| reqRepoReader(unit) | Read permission on specific unit type |
| reqAnyRepoReader() | Any read permission on the repo |
| Token scope | All repo endpoints require AccessTokenScopeCategoryRepository |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


## Core Repository CRUD

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | /user/repos | user.ListMyRepos | user/repo.go | reqToken() |
| POST | /user/repos | repo.Create | repo/repo.go | reqToken() |
| POST | /org/{org}/repos | repo.CreateOrgRepoDeprecated | repo/repo.go | reqToken(), org+repo scope |
| GET | /repositories/{id} | repo.GetByID | repo/repo.go | reqToken() |
| GET | /repos/search | repo.Search | repo/repo.go | None (public) |
| POST | /repos/migrate | repo.Migrate | repo/migrate.go | reqToken() |
| GET | /repos/{username}/{reponame} | repo.Get | repo/repo.go | reqAnyRepoReader() |
| DELETE | /repos/{username}/{reponame} | repo.Delete | repo/repo.go | reqToken(), reqOwner() |
| PATCH | /repos/{username}/{reponame} | repo.Edit | repo/repo.go | reqToken(), reqAdmin() |
| POST | /repos/{username}/{reponame}/generate | repo.Generate | repo/repo.go | reqToken(), reqRepoReader(Code) |

## Transfer

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| POST | /repos/{username}/{reponame}/transfer | repo.Transfer | repo/transfer.go | reqToken(), reqOwner() |
| POST | /repos/{username}/{reponame}/transfer/accept | repo.AcceptTransfer | repo/transfer.go | reqToken() |
| POST | /repos/{username}/{reponame}/transfer/reject | repo.RejectTransfer | repo/transfer.go | reqToken() |

## Actions (Secrets, Variables, Runners, Workflows)

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../actions/secrets | act.ListActionsSecrets | repo/action.go | reqToken(), reqOwner() |
| PUT | .../actions/secrets/{secretname} | act.CreateOrUpdateSecret | repo/action.go | reqToken(), reqOwner() |
| DELETE | .../actions/secrets/{secretname} | act.DeleteSecret | repo/action.go | reqToken(), reqOwner() |
| GET | .../actions/variables | act.ListVariables | repo/action.go | reqToken(), reqOwner() |
| GET | .../actions/variables/{variablename} | act.GetVariable | repo/action.go | reqToken(), reqOwner() |
| POST | .../actions/variables/{variablename} | act.CreateVariable | repo/action.go | reqToken(), reqOwner() |
| PUT | .../actions/variables/{variablename} | act.UpdateVariable | repo/action.go | reqToken(), reqOwner() |
| DELETE | .../actions/variables/{variablename} | act.DeleteVariable | repo/action.go | reqToken(), reqOwner() |
| GET | .../actions/runners | act.ListRunners | repo/action.go | reqToken(), reqOwner() |
| POST | .../actions/runners/registration-token | act.CreateRegistrationToken | repo/action.go | reqToken(), reqOwner() |
| GET | .../actions/runners/{runner_id} | act.GetRunner | repo/action.go | reqToken(), reqOwner() |
| DELETE | .../actions/runners/{runner_id} | act.DeleteRunner | repo/action.go | reqToken(), reqOwner() |
| PATCH | .../actions/runners/{runner_id} | act.UpdateRunner | repo/action.go | reqToken(), reqOwner() |
| GET | .../actions/runs | act.ListWorkflowRuns | repo/action.go | reqToken(), reqRepoReader(Actions) |
| GET | .../actions/jobs | act.ListWorkflowJobs | repo/action.go | reqToken(), reqRepoReader(Actions) |
| GET | .../actions/workflows | repo.ActionsListRepositoryWorkflows | repo/action.go | reqToken(), reqRepoReader(Actions) |
| GET | .../actions/workflows/{workflow_id} | repo.ActionsGetWorkflow | repo/action.go | reqToken(), reqRepoReader(Actions) |
| PUT | .../actions/workflows/{workflow_id}/disable | repo.ActionsDisableWorkflow | repo/action.go | reqToken(), reqRepoWriter(Actions) |
| PUT | .../actions/workflows/{workflow_id}/enable | repo.ActionsEnableWorkflow | repo/action.go | reqToken(), reqRepoWriter(Actions) |
| POST | .../actions/workflows/{workflow_id}/dispatches | repo.ActionsDispatchWorkflow | repo/action.go | reqToken(), reqRepoWriter(Actions) |
| GET | .../actions/jobs/{job_id} | repo.GetWorkflowJob | repo/actions_run.go | reqToken(), reqRepoReader(Actions) |
| GET | .../actions/jobs/{job_id}/logs | repo.DownloadActionsRunJobLogs | repo/actions_run.go | reqToken(), reqRepoReader(Actions) |
| GET | .../actions/tasks | repo.ListActionTasks | repo/action.go | reqRepoReader(Actions) |
| GET | .../actions/runs/{run} | repo.GetWorkflowRun | repo/actions_run.go | reqRepoReader(Actions) |
| DELETE | .../actions/runs/{run} | repo.DeleteActionRun | repo/actions_run.go | reqToken(), reqRepoWriter(Actions) |
| POST | .../actions/runs/{run}/rerun | repo.RerunWorkflowRun | repo/actions_run.go | reqToken(), reqRepoWriter(Actions) |
| POST | .../actions/runs/{run}/rerun-failed-jobs | repo.RerunFailedWorkflowRun | repo/actions_run.go | reqToken(), reqRepoWriter(Actions) |
| GET | .../actions/runs/{run}/jobs | repo.ListWorkflowRunJobs | repo/actions_run.go | reqRepoReader(Actions) |
| POST | .../actions/runs/{run}/jobs/{job_id}/rerun | repo.RerunWorkflowJob | repo/actions_run.go | reqToken(), reqRepoWriter(Actions) |
| GET | .../actions/runs/{run}/artifacts | repo.GetArtifactsOfRun | repo/actions_run.go | reqRepoReader(Actions) |
| GET | .../actions/runs/{run}/attempts/{attempt} | repo.GetWorkflowRunAttempt | repo/actions_run.go | reqRepoReader(Actions) |
| GET | .../actions/runs/{run}/attempts/{attempt}/jobs | repo.ListWorkflowRunAttemptJobs | repo/actions_run.go | reqRepoReader(Actions) |
| GET | .../actions/artifacts | repo.GetArtifacts | repo/actions_run.go | reqRepoReader(Actions) |
| GET | .../actions/artifacts/{artifact_id} | repo.GetArtifact | repo/actions_run.go | reqRepoReader(Actions) |
| DELETE | .../actions/artifacts/{artifact_id} | repo.DeleteArtifact | repo/actions_run.go | reqRepoWriter(Actions) |
| GET | .../actions/artifacts/{artifact_id}/zip | repo.DownloadArtifact | repo/actions_run.go | reqRepoReader(Actions) |
| GET | .../repos/{username}/{reponame}/actions/artifacts/{artifact_id}/zip/raw | repo.DownloadArtifactRaw | repo/actions_run.go | Signed URL (no middleware) |

## Git Hooks

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../hooks/git | repo.ListGitHooks | repo/git_hook.go | reqToken(), reqAdmin(), reqGitHook() |
| GET | .../hooks/git/{id} | repo.GetGitHook | repo/git_hook.go | reqToken(), reqAdmin(), reqGitHook() |
| PATCH | .../hooks/git/{id} | repo.EditGitHook | repo/git_hook.go | reqToken(), reqAdmin(), reqGitHook() |
| DELETE | .../hooks/git/{id} | repo.DeleteGitHook | repo/git_hook.go | reqToken(), reqAdmin(), reqGitHook() |

## Webhooks

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../hooks | repo.ListHooks | repo/hook.go | reqToken(), reqAdmin() |
| POST | .../hooks | repo.CreateHook | repo/hook.go | reqToken(), reqAdmin() |
| GET | .../hooks/{id} | repo.GetHook | repo/hook.go | reqToken(), reqAdmin() |
| PATCH | .../hooks/{id} | repo.EditHook | repo/hook.go | reqToken(), reqAdmin() |
| DELETE | .../hooks/{id} | repo.DeleteHook | repo/hook.go | reqToken(), reqAdmin() |
| POST | .../hooks/{id}/tests | repo.TestHook | repo/hook.go | reqToken(), reqAdmin() |

## Collaborators

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../collaborators | repo.ListCollaborators | repo/collaborators.go | reqToken(), reqAnyRepoReader() |
| GET | .../collaborators/{collaborator} | repo.IsCollaborator | repo/collaborators.go | reqToken(), reqAnyRepoReader() |
| PUT | .../collaborators/{collaborator} | repo.AddOrUpdateCollaborator | repo/collaborators.go | reqToken(), reqAdmin() |
| DELETE | .../collaborators/{collaborator} | repo.DeleteCollaborator | repo/collaborators.go | reqToken(), reqAdmin() |
| GET | .../collaborators/{collaborator}/permission | repo.GetRepoPermissions | repo/collaborators.go | reqToken() |

## Teams

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../teams | repo.ListTeams | repo/teams.go | reqToken(), reqAnyRepoReader() |
| GET | .../teams/{team} | repo.IsTeam | repo/teams.go | reqToken(), reqAnyRepoReader() |
| PUT | .../teams/{team} | repo.AddTeam | repo/teams.go | reqToken(), reqAdmin() |
| DELETE | .../teams/{team} | repo.DeleteTeam | repo/teams.go | reqToken(), reqAdmin() |

## Branches

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../branches | repo.ListBranches | repo/branch.go | reqRepoReader(Code) |
| GET | .../branches/* | repo.GetBranch | repo/branch.go | reqRepoReader(Code) |
| POST | .../branches | repo.CreateBranch | repo/branch.go | reqToken(), reqRepoWriter(Code) |
| DELETE | .../branches/* | repo.DeleteBranch | repo/branch.go | reqToken(), reqRepoWriter(Code) |
| PUT | .../branches/* | repo.UpdateBranch | repo/branch.go | reqToken(), reqRepoWriter(Code) |
| PATCH | .../branches/* | repo.RenameBranch | repo/branch.go | reqToken(), reqRepoWriter(Code) |

## Branch Protections

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../branch_protections | repo.ListBranchProtections | repo/branch.go | reqToken(), reqAdmin() |
| POST | .../branch_protections | repo.CreateBranchProtection | repo/branch.go | reqToken(), reqAdmin() |
| GET | .../branch_protections/* | repo.GetBranchProtection | repo/branch.go | reqToken(), reqAdmin() |
| PATCH | .../branch_protections/* | repo.EditBranchProtection | repo/branch.go | reqToken(), reqAdmin() |
| DELETE | .../branch_protections/* | repo.DeleteBranchProtection | repo/branch.go | reqToken(), reqAdmin() |
| POST | .../branch_protections/priority | repo.UpdateBranchProtectionPriories | repo/branch.go | reqToken(), reqAdmin() |

## Tags

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../tags | repo.ListTags | repo/tag.go | reqRepoReader(Code) |
| GET | .../tags/* | repo.GetTag | repo/tag.go | reqRepoReader(Code) |
| POST | .../tags | repo.CreateTag | repo/tag.go | reqToken(), reqRepoWriter(Code) |
| DELETE | .../tags/* | repo.DeleteTag | repo/tag.go | reqToken(), reqRepoWriter(Code) |

## Tag Protections

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../tag_protections | repo.ListTagProtection | repo/tag.go | reqToken(), reqAdmin() |
| POST | .../tag_protections | repo.CreateTagProtection | repo/tag.go | reqToken(), reqAdmin() |
| GET | .../tag_protections/{id} | repo.GetTagProtection | repo/tag.go | reqToken(), reqAdmin() |
| PATCH | .../tag_protections/{id} | repo.EditTagProtection | repo/tag.go | reqToken(), reqAdmin() |
| DELETE | .../tag_protections/{id} | repo.DeleteTagProtection | repo/tag.go | reqToken(), reqAdmin() |

## Deploy Keys

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../keys | repo.ListDeployKeys | repo/key.go | reqToken(), reqAdmin() |
| POST | .../keys | repo.CreateDeployKey | repo/key.go | reqToken(), reqAdmin() |
| GET | .../keys/{id} | repo.GetDeployKey | repo/key.go | reqToken(), reqAdmin() |
| DELETE | .../keys/{id} | repo.DeleteDeploykey | repo/key.go | reqToken(), reqAdmin() |

## File Contents & Operations

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../raw/* | repo.GetRawFile | repo/file.go | reqRepoReader(Code) |
| GET | .../media/* | repo.GetRawFileOrLFS | repo/file.go | reqRepoReader(Code) |
| HEAD,GET | .../archive/* | repo.GetArchive | repo/download.go | reqRepoReader(Code) |
| GET | .../contents | repo.GetContentsList | repo/file.go | reqRepoReader(Code) |
| GET | .../contents/* | repo.GetContents | repo/file.go | reqRepoReader(Code) |
| POST | .../contents | repo.ChangeFiles | repo/file.go | reqToken(), editor enabled |
| POST | .../contents/* | repo.CreateFile | repo/file.go | reqToken(), editor enabled |
| PUT | .../contents/* | repo.UpdateFile | repo/file.go | reqToken(), editor enabled |
| DELETE | .../contents/* | repo.DeleteFile | repo/file.go | reqToken(), editor enabled |
| GET | .../contents-ext | repo.GetContentsExt | repo/file.go | reqRepoReader(Code) |
| GET | .../contents-ext/* | repo.GetContentsExt | repo/file.go | reqRepoReader(Code) |
| GET | .../file-contents | repo.GetFileContentsGet | repo/file.go | reqRepoReader(Code) |
| POST | .../file-contents | repo.GetFileContentsPost | repo/file.go | reqRepoReader(Code) |
| POST | .../diffpatch | repo.ApplyDiffPatch | repo/patch.go | reqToken(), editor enabled |
| GET | .../editorconfig/{filename} | repo.GetEditorconfig | repo/file.go | reqRepoReader(Code) |
| HEAD,GET | .../tarball/* | repo.DownloadArchive | repo/download.go | reqRepoReader(Code) |
| HEAD,GET | .../zipball/* | repo.DownloadArchive | repo/download.go | reqRepoReader(Code) |
| HEAD,GET | .../bundle/* | repo.DownloadArchive | repo/download.go | reqRepoReader(Code) |

## Git Objects

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../git/commits/{sha} | repo.GetSingleCommit | repo/commits.go | reqRepoReader(Code) |
| GET | .../git/commits/{sha}.{diffType} | repo.DownloadCommitDiffOrPatch | repo/commits.go | reqRepoReader(Code) |
| GET | .../git/refs | repo.GetGitAllRefs | repo/git_ref.go | reqRepoReader(Code) |
| GET | .../git/refs/* | repo.GetGitRefs | repo/git_ref.go | reqRepoReader(Code) |
| GET | .../git/trees/{sha} | repo.GetTree | repo/tree.go | reqRepoReader(Code) |
| GET | .../git/blobs/{sha} | repo.GetBlob | repo/blob.go | reqRepoReader(Code) |
| GET | .../git/tags/{sha} | repo.GetAnnotatedTag | repo/tag.go | reqRepoReader(Code) |
| GET | .../git/notes/{sha} | repo.GetNote | repo/notes.go | reqRepoReader(Code) |

## Commits & Statuses

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../commits | repo.GetAllCommits | repo/commits.go | reqRepoReader(Code) |
| GET | .../commits/{ref}/status | repo.GetCombinedCommitStatusByRef | repo/status.go | reqRepoReader(Code) |
| GET | .../commits/{ref}/statuses | repo.GetCommitStatusesByRef | repo/status.go | reqRepoReader(Code) |
| GET | .../commits/{sha}/pull | repo.GetCommitPullRequest | repo/commits.go | reqRepoReader(Code) |
| GET | .../statuses/{sha} | repo.GetCommitStatuses | repo/status.go | reqRepoReader(Code) |
| POST | .../statuses/{sha} | repo.NewCommitStatus | repo/status.go | reqToken(), reqRepoWriter(Code) |
| GET | .../compare/* | repo.CompareDiff | repo/compare.go | reqRepoReader(Code) |

## Forks & Upstream

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../forks | repo.ListForks | repo/fork.go | None (public) |
| POST | .../forks | repo.CreateFork | repo/fork.go | reqToken(), reqRepoReader(Code) |
| POST | .../merge-upstream | repo.MergeUpstream | repo/branch.go | reqToken(), reqRepoWriter(Code) |

## Releases

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../releases | repo.ListReleases | repo/release.go | reqRepoReader(Releases) |
| POST | .../releases | repo.CreateRelease | repo/release.go | reqToken(), reqRepoWriter(Releases) |
| GET | .../releases/latest | repo.GetLatestRelease | repo/release.go | reqRepoReader(Releases) |
| GET | .../releases/{id} | repo.GetRelease | repo/release.go | reqRepoReader(Releases) |
| PATCH | .../releases/{id} | repo.EditRelease | repo/release.go | reqToken(), reqRepoWriter(Releases) |
| DELETE | .../releases/{id} | repo.DeleteRelease | repo/release.go | reqToken(), reqRepoWriter(Releases) |
| GET | .../releases/{id}/assets | repo.ListReleaseAttachments | repo/release_attachment.go | reqRepoReader(Releases) |
| POST | .../releases/{id}/assets | repo.CreateReleaseAttachment | repo/release_attachment.go | reqToken(), reqRepoWriter(Releases) |
| GET | .../releases/{id}/assets/{attachment_id} | repo.GetReleaseAttachment | repo/release_attachment.go | reqRepoReader(Releases) |
| PATCH | .../releases/{id}/assets/{attachment_id} | repo.EditReleaseAttachment | repo/release_attachment.go | reqToken(), reqRepoWriter(Releases) |
| DELETE | .../releases/{id}/assets/{attachment_id} | repo.DeleteReleaseAttachment | repo/release_attachment.go | reqToken(), reqRepoWriter(Releases) |
| GET | .../releases/tags/{tag} | repo.GetReleaseByTag | repo/release_tags.go | reqRepoReader(Releases) |
| DELETE | .../releases/tags/{tag} | repo.DeleteReleaseByTag | repo/release_tags.go | reqToken(), reqRepoWriter(Releases) |

## Mirrors

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| POST | .../mirror-sync | repo.MirrorSync | repo/mirror.go | reqToken(), reqRepoWriter(Code) |
| POST | .../push_mirrors-sync | repo.PushMirrorSync | repo/mirror.go | reqToken(), reqAdmin() |
| GET | .../push_mirrors | repo.ListPushMirrors | repo/mirror.go | reqToken(), reqAdmin() |
| POST | .../push_mirrors | repo.AddPushMirror | repo/mirror.go | reqToken(), reqAdmin() |
| GET | .../push_mirrors/{name} | repo.GetPushMirrorByName | repo/mirror.go | reqToken(), reqAdmin() |
| DELETE | .../push_mirrors/{name} | repo.DeletePushMirrorByRemoteName | repo/mirror.go | reqToken(), reqAdmin() |

## Pull Requests

| Method | Path | Handler | File | Auth/Permissions |
|---|---|---|---|---|
| GET | .../pulls | repo.ListPullRequests | repo/pull.go | reqRepoReader(Code), mustAllowPulls |
| POST | .../pulls | repo.CreatePullRequest | repo/pull.go | reqToken() |
| GET | .../pulls/pinned | repo.ListPinnedPullRequests | repo/pull.go | reqRepoReader(Code) |
| POST | .../pulls/comments/{id}/resolve | repo.ResolvePullReviewComment | repo/pull_review.go | reqToken() |
| POST | .../pulls/comments/{id}/unresolve | repo.UnresolvePullReviewComment | repo/pull_review.go | reqToken() |
| GET | .../pulls/{index} | repo.GetPullRequest | repo/pull.go | reqRepoReader(Code) |
| PATCH | .../pulls/{index} | repo.EditPullRequest | repo/pull.go | reqToken() |
| GET | .../pulls/{index}.diff | repo.DownloadPullDiffOrPatch | repo/pull.go | reqRepoReader(Code) |
| GET | .../pulls/{index}.patch | repo.DownloadPullDiffOrPatch | repo/pull.go | reqRepoReader(Code) |
| POST | .../pulls/{index}/update | repo.UpdatePullRequest | repo/pull.go | reqToken() |
| GET | .../pulls/{index}/commits | repo.GetPullRequestCommits | repo/pull.go | reqRepoReader(Code) |
| GET | .../pulls/{index}/files | repo.GetPullRequestFiles | repo/pull.go | reqRepoReader(Code) |
| GET | .../pulls/{index}/merge | repo.IsPullRequestMerged | repo/pull.go | reqRepoReader(Code) |
| POST | .../pulls/{index}/merge | repo.MergePullRequest | repo/pull.go | reqToken() |
| DELETE | .../pulls/{index}/merge | repo.CancelScheduledAutoMerge | repo/pull.go | reqToken() |
| GET | .../pulls/{index}/reviews | repo.ListPullReviews | repo/pull_review.go | reqRepoReader(Code) |
| POST | .../pulls/{index}/reviews | repo.CreatePullReview | repo/pull_review.go | reqToken() |
| GET | .../pulls/{index}/reviews/{id} | repo.GetPullReview | repo/pull_review.go | reqRepoReader(Code) |
| DELETE | .../pulls/{index}/reviews/{id} | repo.DeletePullReview | repo/pull_review.go | reqToken() |
| POST | .../pulls/{index}/reviews/{id} | repo.SubmitPullReview | repo/pull_review.go | reqToken() |
| GET | .../pulls/{index}/reviews/{id}/comments | repo.GetPullReviewComments | repo/pull_review.go | reqRepoReader(Code) |
| POST | .../pulls/{index}/reviews/{id}/dismissals | repo.DismissPullReview | repo/pull_review.go | reqToken() |
| POST | .../pulls/{index}/reviews/{id}/undismissals | repo.UnDismissPullReview | repo/pull_review.go | reqToken() |
| POST | .../pulls/{index}/requested_reviewers | repo.CreateReviewRequests | repo/pull_review.go | reqToken() |
| DELETE | .../pulls/{index}/requested_reviewers | repo.DeleteReviewRequests | repo/pull_review.go | reqToken() |
| POST | .../pulls/{index}/comments/{id}/replies | repo.CreatePullReviewCommentReply | repo/pull_review.go | reqToken() |
| GET | .../pulls/{base}/*

 ▸ Credits: 2.70 • Time: 2m 29s

