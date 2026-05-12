# Controller: Unarchiving a repo re-detects action schedules

> 108 nodes · cohesion 0.03

## Key Concepts

- **Unarchiving a repo re-detects action schedules** (62 connections) — `routers/api/v1/repo/repo.go`
- **PUT /api/v1/user/blocks/{username}** (20 connections) — `session_28/api_contracts.json`
- **user_model.GetUserByName** (18 connections) — `models/user/user.go`
- **PUT /api/v1/orgs/{org}/blocks/{username}** (15 connections) — `session_13/api_contracts.json`
- **POST /api/v1/user/repos** (13 connections) — `session_53/api_contracts.json`
- **POST /api/v1/org/{org}/repos** (13 connections) — `session_53/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}** (12 connections) — `session_37/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission** (12 connections) — `session_38/api_contracts.json`
- **POST /api/v1/orgs/{org}/repos** (12 connections) — `session_53/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/blocks/{username}** (11 connections) — `session_13/api_contracts.json`
- **DELETE /api/v1/user/blocks/{username}** (11 connections) — `session_28/api_contracts.json`
- **POST /api/v1/repos/{template_owner}/{template_repo}/generate** (11 connections) — `session_53/api_contracts.json`
- **POST /api/v1/admin/users/{username}/repos** (10 connections) — `session_16/api_contracts.json`
- **GET /api/v1/user/blocks/{username}** (9 connections) — `session_28/api_contracts.json`
- **repository** (8 connections) — `routers/api/v1/repo/collaborators.go`
- **GET /api/v1/orgs/{org}/blocks/{username}** (8 connections) — `session_13/api_contracts.json`
- **user_model.Blocking** (8 connections) — `session_28/impact_analysis_index.json`
- **repo.CreateUserRepo** (8 connections) — `routers/api/v1/repo/repo.go`
- **POST /api/v1/admin/cron/{task}** (7 connections) — `session_16/api_contracts.json`
- **DELETE /api/v1/user/emails** (7 connections) — `session_26/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/collaborators** (6 connections) — `session_37/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}** (6 connections) — `session_37/api_contracts.json`
- **repo_service.CreateRepository** (6 connections) — `session_53/impact_analysis_index.json`
- **shared.BlockUser** (6 connections) — `session_28/impact_analysis_index.json`
- **shared.UnblockUser** (6 connections) — `session_28/impact_analysis_index.json`
- *... and 83 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (23 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (16 shared connections)
- [[Controller: POST /api/v1/orgs]] (12 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (8 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (7 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (7 shared connections)
- [[Controller: convert]] (5 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (5 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (5 shared connections)
- [[Endpoint: routers]] (4 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (4 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (3 shared connections)

## Source Files

- `models/perm/access/repo_permission.go`
- `models/repo/repo.go`
- `models/user/block.go`
- `models/user/user.go`
- `modules/setting/api.go`
- `modules/setting/repository.go`
- `routers/api/v1/admin/cron.go`
- `routers/api/v1/admin/repo.go`
- `routers/api/v1/org/block.go`
- `routers/api/v1/repo/collaborators.go`
- `routers/api/v1/repo/fork.go`
- `routers/api/v1/repo/repo.go`
- `routers/api/v1/user/block.go`
- `routers/api/v1/user/email.go`
- `services/convert/user.go`
- `services/cron/tasks.go`
- `services/repository/create.go`
- `session_13/api_contracts.json`
- `session_13/error_handling.json`
- `session_16/api_contracts.json`

## Audit Trail

- EXTRACTED: 448 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*