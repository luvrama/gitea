# Controller: POST /api/v1/user/gpg_keys

> 51 nodes · cohesion 0.06

## Key Concepts

- **POST /api/v1/user/gpg_keys** (25 connections) — `session_27/api_contracts.json`
- **POST /api/v1/user/gpg_key_verify** (16 connections) — `session_27/api_contracts.json`
- **DELETE /api/v1/user/gpg_keys/{id}** (13 connections) — `session_27/api_contracts.json`
- **GET /api/v1/user/gpg_keys/{id}** (9 connections) — `session_27/api_contracts.json`
- **user** (8 connections) — `routers/api/v1/user/gpg_key.go`
- **GET /api/v1/user/gpg_keys** (8 connections) — `session_27/api_contracts.json`
- **GET /api/v1/users/{username}/gpg_keys** (7 connections) — `session_26/api_contracts.json`
- **convert.ToGPGKey** (6 connections) — `session_27/impact_analysis_index.json`
- **GET /api/v1/user/gpg_key_token** (5 connections) — `session_27/api_contracts.json`
- **asymkey_model.GPGKey** (5 connections) — `session_27/impact_analysis_index.json`
- **user.listGPGKeys** (5 connections) — `routers/api/v1/user/gpg_key.go`
- **api.GPGKey** (4 connections) — `session_27/impact_analysis_index.json`
- **asymkey_model.VerificationToken** (4 connections) — `session_27/impact_analysis_index.json`
- **asymkey_model.VerifyGPGKey** (3 connections) — `session_27/impact_analysis_index.json`
- **user.CreateUserGPGKey** (3 connections) — `routers/api/v1/user/gpg_key.go`
- **admin.USER_DISABLED_FEATURES / admin.EXTERNAL_USER_DISABLE_FEATURES** (2 connections) — `modules/setting/admin.go`
- **setting.UserFeatureManageGPGKeys** (2 connections) — `modules/setting/admin.go`
- **asymkey_model.GPGKeyImport** (2 connections) — `session_27/impact_analysis_index.json`
- **asymkey_model.AddGPGKey** (2 connections) — `session_27/impact_analysis_index.json`
- **asymkey_model.DeleteGPGKey** (2 connections) — `session_27/impact_analysis_index.json`
- **db.Find[GPGKey]** (2 connections) — `models/asymkey/gpg_key.go`
- **user.CreateGPGKey** (2 connections) — `routers/api/v1/user/gpg_key.go`
- **user.DeleteGPGKey** (2 connections) — `routers/api/v1/user/gpg_key.go`
- **user.GetVerificationToken** (2 connections) — `routers/api/v1/user/gpg_key.go`
- **user.ListGPGKeys** (2 connections) — `routers/api/v1/user/gpg_key.go`
- *... and 26 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (6 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (3 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)

## Source Files

- `models/asymkey/gpg_key.go`
- `modules/setting/admin.go`
- `routers/api/v1/user/gpg_key.go`
- `session_26/api_contracts.json`
- `session_26/impact_analysis_index.json`
- `session_27/api_contracts.json`
- `session_27/error_handling.json`
- `session_27/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 169 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*