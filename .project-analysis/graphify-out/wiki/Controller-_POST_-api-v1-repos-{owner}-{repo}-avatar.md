# Controller: POST /api/v1/repos/{owner}/{repo}/avatar

> 54 nodes · cohesion 0.05

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/avatar** (19 connections) — `session_39/api_contracts.json`
- **POST /api/v1/orgs/{org}/avatar** (18 connections) — `session_6/api_contracts.json`
- **POST /api/v1/user/avatar** (16 connections) — `session_18/api_contracts.json`
- **DELETE /api/v1/user/avatar** (12 connections) — `session_19/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/avatar** (9 connections) — `session_6/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/avatar** (8 connections) — `session_39/api_contracts.json`
- **avatar.ProcessAvatarImage** (6 connections) — `modules/avatar/avatar.go`
- **user_service.UploadAvatar** (6 connections) — `session_18/impact_analysis_index.json`
- **user_service.DeleteAvatar** (5 connections) — `services/user/avatar.go`
- **storage.SaveFrom(storage.Avatars, ...)** (4 connections) — `modules/storage/storage.go`
- **organization** (3 connections) — `routers/api/v1/org/avatar.go`
- **repository** (3 connections) — `routers/api/v1/repo/avatar.go`
- **user** (3 connections) — `routers/api/v1/user/avatar.go`
- **Avatar Storage Backend** (3 connections) — `modules/storage/storage.go`
- **org.DeleteAvatar** (3 connections) — `routers/api/v1/org/avatar.go`
- **org.UpdateAvatar** (3 connections) — `routers/api/v1/org/avatar.go`
- **repo_service.UploadAvatar** (3 connections) — `services/repository/avatar.go`
- **storage.Avatars.Delete** (3 connections) — `modules/storage/storage.go`
- **user_service** (3 connections) — `session_19/impact_analysis_index.json`
- **File Storage (RepoAvatars)** (2 connections) — `modules/storage/storage.go`
- **avatar.HashAvatar** (2 connections) — `modules/avatar/hash.go`
- **repo.DeleteAvatar** (2 connections) — `routers/api/v1/repo/avatar.go`
- **repo.UpdateAvatar** (2 connections) — `routers/api/v1/repo/avatar.go`
- **repo_service (services/repository)** (2 connections) — `session_39/impact_analysis_index.json`
- **repo_service.DeleteAvatar** (2 connections) — `services/repository/avatar.go`
- *... and 29 more nodes in this community*

## Relationships

- [[Controller: POST /api/v1/orgs]] (5 shared connections)
- [[Controller: user_model.User]] (5 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (5 shared connections)
- [[Endpoint: routers]] (3 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (3 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (2 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (1 shared connections)

## Source Files

- `app.ini [picture]`
- `modules/avatar/avatar.go`
- `modules/avatar/hash.go`
- `modules/setting/picture.go`
- `modules/storage/storage.go`
- `routers/api/v1/org/avatar.go`
- `routers/api/v1/repo/avatar.go`
- `routers/api/v1/user/avatar.go`
- `services/repository/avatar.go`
- `services/user/avatar.go`
- `session_18/api_contracts.json`
- `session_18/error_handling.json`
- `session_18/impact_analysis_index.json`
- `session_19/api_contracts.json`
- `session_19/error_handling.json`
- `session_19/impact_analysis_index.json`
- `session_39/api_contracts.json`
- `session_39/error_handling.json`
- `session_39/impact_analysis_index.json`
- `session_6/api_contracts.json`

## Audit Trail

- EXTRACTED: 173 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*