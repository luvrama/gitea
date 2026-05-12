# Controller: webhook_service.ToHook

> 112 nodes · cohesion 0.03

## Key Concepts

- **webhook_service.ToHook** (23 connections) — `session_48/impact_analysis_index.json`
- **POST /api/v1/orgs/{org}/hooks** (20 connections) — `session_12/api_contracts.json`
- **webhook.Webhook** (18 connections) — `session_48/impact_analysis_index.json`
- **POST /api/v1/user/hooks** (14 connections) — `session_21/api_contracts.json`
- **PATCH /api/v1/orgs/{org}/hooks/{id}** (13 connections) — `session_12/api_contracts.json`
- **PATCH /api/v1/user/hooks/{id}** (13 connections) — `session_22/api_contracts.json`
- **GET /api/v1/admin/hooks** (12 connections) — `session_14/api_contracts.json`
- **GET /api/v1/user/hooks/{id}** (12 connections) — `session_21/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/hooks/{id}** (12 connections) — `session_48/api_contracts.json`
- **GET /api/v1/orgs/{org}/hooks** (11 connections) — `session_12/api_contracts.json`
- **GET /api/v1/user/hooks** (11 connections) — `session_21/api_contracts.json`
- **PATCH /api/v1/admin/hooks/{id}** (10 connections) — `session_14/api_contracts.json`
- **DELETE /api/v1/user/hooks/{id}** (10 connections) — `session_22/api_contracts.json`
- **utils.GetListOptions** (10 connections) — `routers/api/v1/utils/page.go`
- **GET /api/v1/admin/hooks/{id}** (9 connections) — `session_14/api_contracts.json`
- **DELETE /api/v1/admin/hooks/{id}** (9 connections) — `session_14/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/hooks/{id}/tests** (9 connections) — `session_47/api_contracts.json`
- **GET /api/v1/orgs/{org}/hooks/{id}** (8 connections) — `session_12/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/hooks/{id}** (8 connections) — `session_12/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/hooks/{id}** (8 connections) — `session_48/api_contracts.json`
- **utils.editHook** (8 connections) — `routers/api/v1/utils/hook.go`
- **repository** (7 connections) — `routers/api/v1/repo/hook.go`
- **admin** (6 connections) — `routers/api/v1/admin/hooks.go`
- **organization** (6 connections) — `routers/api/v1/org/hook.go`
- **user** (6 connections) — `routers/api/v1/user/hook.go`
- *... and 87 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (20 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (8 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (8 shared connections)
- [[Controller: user_model.User]] (6 shared connections)
- [[Endpoint: routers]] (4 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (4 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (3 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (3 shared connections)
- [[Controller: POST /api/v1/orgs]] (3 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)
- [[Controller: convert]] (2 shared connections)

## Source Files

- `models/webhook/webhook.go`
- `models/webhook/webhook_system.go`
- `modules/setting/security.go`
- `modules/setting/server.go`
- `modules/setting/webhook.go`
- `routers/api/v1/admin/hooks.go`
- `routers/api/v1/org/hook.go`
- `routers/api/v1/repo/hook.go`
- `routers/api/v1/user/hook.go`
- `routers/api/v1/user/user.go`
- `routers/api/v1/utils/hook.go`
- `routers/api/v1/utils/page.go`
- `services/convert/git_commit.go`
- `session_12/api_contracts.json`
- `session_12/error_handling.json`
- `session_14/api_contracts.json`
- `session_14/error_handling.json`
- `session_21/api_contracts.json`
- `session_21/error_handling.json`
- `session_21/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 437 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*