# Controller: POST /api/v1/user/keys

> 83 nodes · cohesion 0.04

## Key Concepts

- **POST /api/v1/user/keys** (18 connections) — `session_23/api_contracts.json`
- **DELETE /api/v1/user/keys/{id}** (18 connections) — `session_23/api_contracts.json`
- **DELETE /api/v1/admin/users/{username}** (14 connections) — `session_15/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/keys** (14 connections) — `session_50/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/keys/{id}** (11 connections) — `session_50/api_contracts.json`
- **asymkey_model.PublicKey** (11 connections) — `session_50/impact_analysis_index.json`
- **DELETE /api/v1/admin/users/{username}/keys/{id}** (9 connections) — `session_15/api_contracts.json`
- **admin** (8 connections) — `routers/api/v1/admin/user.go`
- **GET /api/v1/user/keys** (8 connections) — `session_23/api_contracts.json`
- **GET /api/v1/users/{username}/keys** (8 connections) — `session_23/api_contracts.json`
- **GET /api/v1/user/keys/{id}** (7 connections) — `session_23/api_contracts.json`
- **user** (6 connections) — `routers/api/v1/user/key.go`
- **POST /api/v1/admin/users/{username}/keys** (6 connections) — `session_15/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/keys** (6 connections) — `session_50/api_contracts.json`
- **asymkey_model.CheckPublicKeyString** (6 connections) — `models/asymkey/ssh_key_parse.go`
- **user.CreateUserPublicKey** (6 connections) — `routers/api/v1/user/key.go`
- **repository** (5 connections) — `routers/api/v1/repo/key.go`
- **GET /api/v1/repos/{owner}/{repo}/keys/{id}** (5 connections) — `session_50/api_contracts.json`
- **asymkey_service.DeletePublicKey** (5 connections) — `session_23/impact_analysis_index.json`
- **asymkey_service.RewriteAllPublicKeys** (5 connections) — `services/asymkey/ssh_key_authorized_keys.go`
- **user.appendPrivateInformation** (5 connections) — `routers/api/v1/user/key.go`
- **user.listPublicKeys** (5 connections) — `routers/api/v1/user/key.go`
- **asymkey_model.DeployKey** (4 connections) — `session_50/impact_analysis_index.json`
- **asymkey_model.PublicKeyIsExternallyManaged** (3 connections) — `models/asymkey/ssh_key.go`
- **asymkey_service.DeleteDeployKey** (3 connections) — `services/asymkey/deploy_key.go`
- *... and 58 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (7 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (4 shared connections)
- [[Endpoint: routers]] (3 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (3 shared connections)
- [[Error Scenario: POST /api/v1/admin/users]] (2 shared connections)
- [[Controller: POST /api/v1/orgs]] (2 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (2 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (1 shared connections)
- [[Controller: user_model.User]] (1 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (1 shared connections)

## Source Files

- `models/asymkey/ssh_key.go`
- `models/asymkey/ssh_key_deploy.go`
- `models/asymkey/ssh_key_parse.go`
- `modules/setting/admin.go`
- `modules/setting/service.go`
- `modules/setting/ssh.go`
- `routers/api/v1/admin/user.go`
- `routers/api/v1/repo/key.go`
- `routers/api/v1/user/key.go`
- `services/asymkey/deploy_key.go`
- `services/asymkey/ssh_key_authorized_keys.go`
- `services/convert/convert.go`
- `services/user/delete.go`
- `session_15/api_contracts.json`
- `session_15/error_handling.json`
- `session_15/impact_analysis_index.json`
- `session_23/api_contracts.json`
- `session_23/error_handling.json`
- `session_23/impact_analysis_index.json`
- `session_50/api_contracts.json`

## Audit Trail

- EXTRACTED: 274 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*