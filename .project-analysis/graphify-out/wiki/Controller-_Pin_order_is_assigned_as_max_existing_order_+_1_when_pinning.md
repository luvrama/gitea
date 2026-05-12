# Controller: Pin order is assigned as max existing order + 1 when pinning

> 113 nodes · cohesion 0.04

## Key Concepts

- **Pin order is assigned as max existing order + 1 when pinning** (91 connections) — `models/issues/issue_pin.go`
- **Unpinning creates a comment of type CommentTypeUnpin in issue history** (90 connections) — `models/issues/issue_pin.go`
- **Moving pin reorders other pins - shifts up or down depending on direction** (78 connections) — `models/issues/issue_pin.go`
- **actions_service.GetVariable** (19 connections) — `services/actions/variables.go`
- **POST /api/v1/orgs/{org}/actions/variables/{variablename}** (17 connections) — `session_7/api_contracts.json`
- **PUT /api/v1/orgs/{org}/actions/variables/{variablename}** (17 connections) — `session_7/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/hooks** (17 connections) — `session_48/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}** (16 connections) — `session_40/api_contracts.json`
- **GET /api/v1/signing-key.gpg** (15 connections) — `session_1/api_contracts.json`
- **GET /api/v1/user/actions/variables/{variablename}** (15 connections) — `session_20/api_contracts.json`
- **POST /api/v1/user/actions/variables/{variablename}** (14 connections) — `session_19/api_contracts.json`
- **PUT /api/v1/user/actions/variables/{variablename}** (13 connections) — `session_19/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}** (13 connections) — `session_40/api_contracts.json`
- **ActionVariable** (13 connections) — `session_40/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/signing-key.gpg** (12 connections) — `session_1/api_contracts.json`
- **POST /api/v1/admin/hooks** (12 connections) — `session_14/api_contracts.json`
- **GET /api/v1/user/actions/variables** (12 connections) — `session_20/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/subscription** (12 connections) — `session_29/api_contracts.json`
- **user** (10 connections) — `routers/api/v1/user/action.go`
- **GET /api/v1/signing-key.pub** (10 connections) — `session_1/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/signing-key.pub** (10 connections) — `session_1/api_contracts.json`
- **DELETE /api/v1/user/actions/variables/{variablename}** (9 connections) — `session_19/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/actions/workflows** (9 connections) — `session_41/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/subscription** (8 connections) — `session_29/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/subscription** (8 connections) — `session_29/api_contracts.json`
- *... and 88 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (52 shared connections)
- [[Controller: user_model.User]] (23 shared connections)
- [[Controller: webhook_service.ToHook]] (20 shared connections)
- [[Controller: reqOrgOwnership]] (18 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (18 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (17 shared connections)
- [[Controller: POST /api/v1/orgs]] (16 shared connections)
- [[Controller: convert]] (16 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (15 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections]] (13 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (11 shared connections)
- [[Controller: issues_model.Issue]] (10 shared connections)

## Source Files

- `models/actions/variable.go`
- `models/db/list.go`
- `models/issues/issue_pin.go`
- `models/repo/watch.go`
- `modules/actions/workflows.go`
- `modules/git/key.go`
- `modules/setting/actions.go`
- `modules/setting/git.go`
- `modules/setting/repository.go`
- `modules/setting/service.go`
- `routers/api/v1/admin/hooks.go`
- `routers/api/v1/misc/signing.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/repo/hook.go`
- `routers/api/v1/user/action.go`
- `routers/api/v1/user/watch.go`
- `routers/api/v1/utils/hook.go`
- `services/actions/variables.go`
- `services/asymkey/sign.go`
- `session_1/api_contracts.json`

## Audit Trail

- EXTRACTED: 738 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*