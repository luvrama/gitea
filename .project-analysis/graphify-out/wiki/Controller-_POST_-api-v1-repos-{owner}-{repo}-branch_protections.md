# Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections

> 101 nodes · cohesion 0.03

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/branch_protections** (19 connections) — `session_46/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/branches/{branch}** (17 connections) — `session_45/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/branches** (17 connections) — `session_45/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/branches/{branch}** (15 connections) — `session_45/api_contracts.json`
- **repository** (14 connections) — `routers/api/v1/repo/branch.go`
- **PATCH /api/v1/repos/{owner}/{repo}/branches/{branch}** (14 connections) — `session_45/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name}** (14 connections) — `session_46/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/merge-upstream** (14 connections) — `session_47/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/branches** (13 connections) — `session_45/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/branches/{branch}** (11 connections) — `session_45/api_contracts.json`
- **git_model.ProtectedBranch** (11 connections) — `session_46/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/branch_protections/{name}** (8 connections) — `session_46/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/branch_protections** (8 connections) — `session_46/api_contracts.json`
- **gitrepo.Push** (8 connections) — `modules/gitrepo/push.go`
- **DELETE /api/v1/repos/{owner}/{repo}/branch_protections/{name}** (7 connections) — `session_46/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/branch_protections/priority** (6 connections) — `session_46/api_contracts.json`
- **git_model.Branch** (6 connections) — `session_45/impact_analysis_index.json`
- **db.Count[git_model.Branch]** (6 connections) — `models/db/list.go`
- **git_model.FindRepoProtectedBranchRules** (6 connections) — `models/git/protected_branch_list.go`
- **convert.ToBranch** (5 connections) — `session_45/impact_analysis_index.json`
- **convert.ToBranchProtection** (5 connections) — `session_46/impact_analysis_index.json`
- **git_model.UpdateProtectBranch** (5 connections) — `models/git/protected_branch.go`
- **api.Branch** (3 connections) — `session_45/impact_analysis_index.json`
- **GitRepo.GetBranchCommit** (3 connections) — `modules/git/repo_branch.go`
- **GitRepo.GetBranchCommit (loop)** (3 connections) — `modules/git/repo_branch.go`
- *... and 76 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (13 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (9 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (5 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (2 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: POST /api/v1/orgs]] (1 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (1 shared connections)
- [[Controller: POST /api/v1/admin/unadopted/{owner}/{repo}]] (1 shared connections)

## Source Files

- `models/db/list.go`
- `models/git/branch.go`
- `models/git/protected_branch.go`
- `models/git/protected_branch_list.go`
- `models/organization/team.go`
- `models/user/user.go`
- `modules/git/commit.go`
- `modules/git/repo.go`
- `modules/git/repo_branch.go`
- `modules/git/repo_commit.go`
- `modules/gitrepo/branch.go`
- `modules/gitrepo/push.go`
- `modules/repository/branch.go`
- `routers/api/v1/repo/branch.go`
- `services/convert/convert.go`
- `services/notify/notify.go`
- `services/pull/update.go`
- `services/repository/branch.go`
- `services/repository/merge_upstream.go`
- `session_45/api_contracts.json`

## Audit Trail

- EXTRACTED: 375 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*