# Error Scenario: POST /api/v1/admin/users

> 41 nodes · cohesion 0.06

## Key Concepts

- **POST /api/v1/admin/users** (26 connections) — `session_14/api_contracts.json`
- **PATCH /api/v1/admin/users/{username}** (22 connections) — `session_15/api_contracts.json`
- **PATCH /api/v1/user/settings** (10 connections) — `session_24/api_contracts.json`
- **user_service.UpdateUser** (9 connections) — `session_24/impact_analysis_index.json`
- **GET /api/v1/user/settings** (5 connections) — `session_24/api_contracts.json`
- **convert.User2UserSettings** (4 connections) — `session_24/impact_analysis_index.json`
- **user** (3 connections) — `routers/api/v1/user/settings.go`
- **mailer.SendRegisterNotifyMail** (3 connections) — `session_14/impact_analysis_index.json`
- **parseAuthSource** (3 connections) — `routers/api/v1/admin/user.go`
- **password.IsPwned** (3 connections) — `session_14/impact_analysis_index.json`
- **user_model.AdminCreateUser** (3 connections) — `models/user/user.go`
- **user_model.UpdateUserCols** (3 connections) — `models/user/user.go`
- **user_service.ReplacePrimaryEmailAddress** (3 connections) — `session_15/impact_analysis_index.json`
- **user_service.UpdateAuth** (3 connections) — `session_15/impact_analysis_index.json`
- **HaveIBeenPwned API** (2 connections) — `modules/auth/password/pwn/pwn.go`
- **user_model.EmailAddress** (2 connections) — `session_15/impact_analysis_index.json`
- **admin.CreateUser** (2 connections) — `routers/api/v1/admin/user.go`
- **admin.EditUser** (2 connections) — `routers/api/v1/admin/user.go`
- **user.GetUserSettings** (2 connections) — `routers/api/v1/user/settings.go`
- **user.UpdateUserSettings** (2 connections) — `routers/api/v1/user/settings.go`
- **MIN_PASSWORD_LENGTH** (1 connections) — `modules/setting/security.go`
- **MinPasswordLength** (1 connections) — `modules/setting/security.go`
- **PASSWORD_CHECK_PWN** (1 connections) — `modules/setting/security.go`
- **PasswordCheckPwn** (1 connections) — `modules/setting/security.go`
- **admin.CreateUser** (1 connections) — `session_14/api_contracts.json`
- *... and 16 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (8 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (5 shared connections)
- [[Controller: POST /api/v1/orgs]] (4 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (3 shared connections)
- [[Controller: POST /api/v1/user/keys]] (2 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (1 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (1 shared connections)

## Source Files

- `models/user/user.go`
- `modules/auth/password/pwn/pwn.go`
- `modules/setting/security.go`
- `routers/api/v1/admin/user.go`
- `routers/api/v1/user/settings.go`
- `session_14/api_contracts.json`
- `session_14/error_handling.json`
- `session_14/impact_analysis_index.json`
- `session_15/api_contracts.json`
- `session_15/error_handling.json`
- `session_15/impact_analysis_index.json`
- `session_24/api_contracts.json`
- `session_24/error_handling.json`
- `session_24/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 133 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*