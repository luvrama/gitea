# Controller: IsNewPinAllowed compares current pin count against MaxPinned setting

> 133 nodes · cohesion 0.03

## Key Concepts

- **IsNewPinAllowed compares current pin count against MaxPinned setting** (76 connections) — `models/issues/issue_pin.go`
- **Language stats response is a custom JSON object mapping language name to byte co** (70 connections) — `routers/api/v1/repo/language.go`
- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies** (25 connections) — `session_31/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks** (23 connections) — `session_31/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}** (21 connections) — `session_54/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies** (20 connections) — `session_31/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks** (20 connections) — `session_31/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies** (19 connections) — `session_31/api_contracts.json`
- **access_model.GetDoerRepoPermission** (18 connections) — `models/perm/access/repo_permission.go`
- **convert.ToRepo** (17 connections) — `session_54/impact_analysis_index.json`
- **Issue** (14 connections) — `session_47/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/blocks** (13 connections) — `session_31/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/forks** (13 connections) — `session_49/api_contracts.json`
- **repo.getParamsIssue** (12 connections) — `routers/api/v1/repo/issue_dependency.go`
- **GET /api/v1/repositories/{id}** (11 connections) — `session_54/api_contracts.json`
- **GET /api/v1/user/teams** (9 connections) — `session_8/api_contracts.json`
- **GET /api/v1/users/{username}/repos** (9 connections) — `session_25/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/issues/{index}/lock** (9 connections) — `session_47/api_contracts.json`
- **GET /api/v1/orgs/{org}/teams** (8 connections) — `session_8/api_contracts.json`
- **GET /api/v1/orgs/{org}/repos** (8 connections) — `session_25/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/forks** (8 connections) — `session_49/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}** (8 connections) — `session_54/api_contracts.json`
- **convert.ToAPIIssue** (8 connections) — `services/convert/issue.go`
- **repo.getFormIssue** (8 connections) — `routers/api/v1/repo/issue_dependency.go`
- **issue** (7 connections) — `routers/api/v1/repo/issue_dependency.go`
- *... and 108 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (22 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (18 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (16 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (15 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (14 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (12 shared connections)
- [[Controller: convert]] (12 shared connections)
- [[Controller: reqOrgOwnership]] (11 shared connections)
- [[Controller: POST /api/v1/orgs]] (10 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (9 shared connections)
- [[Endpoint: routers]] (8 shared connections)
- [[Controller: issues_model.Issue]] (8 shared connections)

## Source Files

- `models/issues/dependency.go`
- `models/issues/issue.go`
- `models/issues/issue_pin.go`
- `models/perm/access/repo_permission.go`
- `models/repo/issue.go`
- `models/repo/language_stats.go`
- `models/repo/repo_list.go`
- `modules/gitrepo/clone.go`
- `modules/setting/mirror.go`
- `modules/setting/repository.go`
- `modules/setting/service.go`
- `routers/api/v1/admin/cron.go`
- `routers/api/v1/org/team.go`
- `routers/api/v1/repo/fork.go`
- `routers/api/v1/repo/issue_dependency.go`
- `routers/api/v1/repo/issue_lock.go`
- `routers/api/v1/repo/language.go`
- `routers/api/v1/repo/repo.go`
- `routers/api/v1/user/repo.go`
- `services/convert/issue.go`

## Audit Trail

- EXTRACTED: 689 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*