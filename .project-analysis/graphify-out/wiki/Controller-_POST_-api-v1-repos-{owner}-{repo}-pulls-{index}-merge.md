# Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

> 105 nodes · cohesion 0.03

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge** (25 connections) — `session_34/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/pulls** (24 connections) — `session_34/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{index}** (17 connections) — `session_33/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{base}/{head}** (17 connections) — `session_33/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls** (16 connections) — `session_33/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{index}/files** (14 connections) — `session_34/api_contracts.json`
- **repository** (13 connections) — `routers/api/v1/repo/pull.go`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}** (10 connections) — `session_33/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge** (10 connections) — `session_34/api_contracts.json`
- **POST /api/v1/admin/users/{username}/rename** (9 connections) — `session_15/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update** (9 connections) — `session_34/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits** (9 connections) — `session_34/api_contracts.json`
- **convert.ToAPIPullRequest** (9 connections) — `services/convert/pull.go`
- **pull_service** (9 connections) — `session_38/impact_analysis_index.json`
- **issues_model.PullRequest** (8 connections) — `session_34/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/commits/{sha}/pull** (7 connections) — `session_32/api_contracts.json`
- **git_service.GetCompareInfo** (6 connections) — `services/git/compare.go`
- **issues_model.GetPullRequestByIndex** (6 connections) — `models/issues/pull.go`
- **pull_service.StartPullRequestCheckOnView** (5 connections) — `services/pull/check.go`
- **GET /api/v1/repos/{owner}/{repo}/pulls/{index}/merge** (4 connections) — `session_34/api_contracts.json`
- **PullRequest** (4 connections) — `session_33/impact_analysis_index.json`
- **user_service.RenameUser** (4 connections) — `session_15/impact_analysis_index.json`
- **Branch** (3 connections) — `session_33/impact_analysis_index.json`
- **git_service.CompareInfo** (3 connections) — `session_34/impact_analysis_index.json`
- **Cancel auto-merge requires being the scheduler or having merge permission** (3 connections) — `routers/api/v1/repo/pull.go`
- *... and 80 more nodes in this community*

## Relationships

- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (9 shared connections)
- [[Controller: convert]] (7 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (5 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (4 shared connections)
- [[Controller: issues_model.Issue]] (4 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (3 shared connections)
- [[Controller: GET /api/v1/repos/{owner}/{repo}/commits]] (3 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (3 shared connections)
- [[Controller: POST /api/v1/orgs]] (3 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (2 shared connections)
- [[Controller: user_model.User]] (2 shared connections)
- [[Error Scenario: POST /api/v1/admin/users]] (2 shared connections)

## Source Files

- `models/issues/assignees.go`
- `models/issues/label.go`
- `models/issues/milestone.go`
- `models/issues/pull.go`
- `models/issues/pull_list.go`
- `models/perm/access/repo_permission.go`
- `models/repo/repo.go`
- `modules/setting/git.go`
- `modules/setting/repository.go`
- `modules/setting/testenv.go`
- `routers/api/v1/admin/user.go`
- `routers/api/v1/repo/commits.go`
- `routers/api/v1/repo/pull.go`
- `services/automerge/automerge.go`
- `services/convert/convert.go`
- `services/convert/pull.go`
- `services/git/compare.go`
- `services/gitdiff/gitdiff.go`
- `services/pull/check.go`
- `services/pull/merge.go`

## Audit Trail

- EXTRACTED: 391 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*