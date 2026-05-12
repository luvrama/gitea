# Controller: POST /api/v1/orgs

> 128 nodes · cohesion 0.03

## Key Concepts

- **POST /api/v1/orgs** (24 connections) — `session_5/api_contracts.json`
- **Generate repo requires at least one template option to be selected** (21 connections) — `services/repository/generate.go`
- **GET /api/v1/users/{username}/orgs/{org}/permissions** (17 connections) — `session_4/api_contracts.json`
- **PUT /api/v1/user/actions/secrets/{secretname}** (17 connections) — `session_19/api_contracts.json`
- **GET /api/v1/users/{username}/orgs** (16 connections) — `session_4/api_contracts.json`
- **POST /api/v1/orgs/{org}/rename** (16 connections) — `session_5/api_contracts.json`
- **PATCH /api/v1/orgs/{org}** (15 connections) — `session_5/api_contracts.json`
- **DELETE /api/v1/orgs/{org}** (15 connections) — `session_5/api_contracts.json`
- **GET /api/v1/user/orgs** (14 connections) — `session_4/api_contracts.json`
- **PUT /api/v1/orgs/{org}/actions/secrets/{secretname}** (14 connections) — `session_6/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}** (14 connections) — `session_39/api_contracts.json`
- **GET /api/v1/orgs** (13 connections) — `session_5/api_contracts.json`
- **organization** (12 connections) — `routers/api/v1/org/org.go`
- **GET /api/v1/orgs/{org}** (12 connections) — `session_5/api_contracts.json`
- **POST /api/v1/admin/users/{username}/orgs** (12 connections) — `session_14/api_contracts.json`
- **convert.ToOrganization** (12 connections) — `session_14/impact_analysis_index.json`
- **orgAssignment(true) + reqOrgOwnership()** (12 connections) — `routers/api/v1/api.go`
- **DELETE /api/v1/orgs/{org}/repos** (11 connections) — `session_6/api_contracts.json`
- **DELETE /api/v1/user/actions/secrets/{secretname}** (11 connections) — `session_19/api_contracts.json`
- **organization.Organization** (11 connections) — `session_14/impact_analysis_index.json`
- **user_model.SearchUsers** (10 connections) — `session_18/impact_analysis_index.json`
- **DELETE /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}** (9 connections) — `session_39/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/actions/secrets/{secretname}** (8 connections) — `session_6/api_contracts.json`
- **GET /api/v1/admin/orgs** (8 connections) — `session_14/api_contracts.json`
- **GET /api/v1/admin/users** (7 connections) — `session_15/api_contracts.json`
- *... and 103 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (21 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (16 shared connections)
- [[Controller: reqOrgOwnership]] (15 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (12 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (11 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (10 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (7 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (6 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (5 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/avatar]] (5 shared connections)
- [[Error Scenario: POST /api/v1/admin/users]] (4 shared connections)
- [[Controller: webhook_service.ToHook]] (3 shared connections)

## Source Files

- `custom/conf/app.ini [admin]`
- `custom/conf/app.ini [api]`
- `custom/conf/app.ini [service]`
- `models/organization/org.go`
- `models/organization/org_user.go`
- `models/secret/secret.go`
- `modules/setting/security.go`
- `modules/setting/service.go`
- `modules/web/middleware/binding.go`
- `routers/api/v1/admin/org.go`
- `routers/api/v1/admin/user.go`
- `routers/api/v1/api.go`
- `routers/api/v1/org/action.go`
- `routers/api/v1/org/org.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/user/action.go`
- `routers/api/v1/user/helper.go`
- `services/convert/convert.go`
- `services/repository/generate.go`
- `services/secrets/secrets.go`

## Audit Trail

- EXTRACTED: 537 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*