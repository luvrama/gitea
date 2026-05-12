# Controller: Issue templates are parsed from multiple candidate directories in priority order

> 85 nodes · cohesion 0.04

## Key Concepts

- **Issue templates are parsed from multiple candidate directories in priority order** (63 connections) — `services/issue/template.go`
- **context.UserAssignmentAPI** (18 connections) — `services/context/api.go`
- **POST /api/v1/users/{username}/tokens** (16 connections) — `session_24/api_contracts.json`
- **PATCH /api/v1/user/applications/oauth2/{id}** (15 connections) — `session_25/api_contracts.json`
- **DELETE /api/v1/users/{username}/tokens/{token}** (13 connections) — `session_24/api_contracts.json`
- **POST /api/v1/user/applications/oauth2** (13 connections) — `session_24/api_contracts.json`
- **POST /api/v1/admin/users/{username}/badges** (10 connections) — `session_17/api_contracts.json`
- **user** (9 connections) — `routers/api/v1/user/app.go`
- **DELETE /api/v1/admin/users/{username}/badges** (9 connections) — `session_17/api_contracts.json`
- **DELETE /api/v1/user/applications/oauth2/{id}** (9 connections) — `session_25/api_contracts.json`
- **GET /api/v1/user/applications/oauth2/{id}** (9 connections) — `session_25/api_contracts.json`
- **GET /api/v1/admin/users/{username}/badges** (8 connections) — `session_17/api_contracts.json`
- **GET /api/v1/users/{username}/tokens** (8 connections) — `session_24/api_contracts.json`
- **GET /api/v1/user/applications/oauth2** (7 connections) — `session_25/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}** (7 connections) — `session_39/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}** (7 connections) — `session_39/api_contracts.json`
- **convert.ToOAuth2Application** (7 connections) — `session_25/impact_analysis_index.json`
- **actions_service.DeleteVariableByName** (6 connections) — `services/actions/variables.go`
- **OAuth2Application.GenerateClientSecret** (5 connections) — `models/auth/oauth2.go`
- **admin** (4 connections) — `routers/api/v1/admin/user_badge.go`
- **auth.OAuth2Application** (4 connections) — `session_25/impact_analysis_index.json`
- **setting.SuccessfulTokensCacheSize** (3 connections) — `custom/conf/app.ini`
- **Badge** (3 connections) — `session_17/impact_analysis_index.json`
- **UserBadge** (3 connections) — `session_17/impact_analysis_index.json`
- **auth_model.AccessToken** (3 connections) — `session_24/impact_analysis_index.json`
- *... and 60 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (11 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (11 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (8 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (8 shared connections)
- [[Controller: convert]] (8 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (7 shared connections)
- [[Controller: POST /api/v1/orgs]] (6 shared connections)
- [[Controller: reqOrgOwnership]] (6 shared connections)
- [[Controller: user_model.User]] (6 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (4 shared connections)
- [[Controller: POST /api/v1/user/keys]] (3 shared connections)
- [[Endpoint: routers]] (2 shared connections)

## Source Files

- `custom/conf/app.ini`
- `custom/conf/app.ini [oauth2]`
- `models/auth/access_token.go`
- `models/auth/access_token_scope.go`
- `models/auth/oauth2.go`
- `modules/setting/oauth2.go`
- `routers/api/v1/admin/user_badge.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/user/action.go`
- `routers/api/v1/user/app.go`
- `services/actions/variables.go`
- `services/context/api.go`
- `services/issue/template.go`
- `session_17/api_contracts.json`
- `session_17/impact_analysis_index.json`
- `session_24/api_contracts.json`
- `session_24/error_handling.json`
- `session_24/impact_analysis_index.json`
- `session_25/api_contracts.json`
- `session_25/error_handling.json`

## Audit Trail

- EXTRACTED: 354 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*