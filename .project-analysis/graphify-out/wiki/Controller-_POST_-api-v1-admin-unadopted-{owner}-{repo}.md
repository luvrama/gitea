# Controller: POST /api/v1/admin/unadopted/{owner}/{repo}

> 19 nodes · cohesion 0.15

## Key Concepts

- **POST /api/v1/admin/unadopted/{owner}/{repo}** (14 connections) — `session_16/api_contracts.json`
- **GET /api/v1/admin/unadopted** (10 connections) — `session_16/api_contracts.json`
- **DELETE /api/v1/admin/unadopted/{owner}/{repo}** (9 connections) — `session_16/api_contracts.json`
- **Repository** (5 connections) — `session_47/impact_analysis_index.json`
- **admin** (4 connections) — `routers/api/v1/admin/adopt.go`
- **repository.root_path** (3 connections) — `modules/setting/repository.go`
- **admin.AdoptRepository** (2 connections) — `routers/api/v1/admin/adopt.go`
- **admin.DeleteUnadoptedRepository** (2 connections) — `routers/api/v1/admin/adopt.go`
- **admin.ListUnadoptedRepositories** (2 connections) — `routers/api/v1/admin/adopt.go`
- **repo_service.AdoptRepository** (2 connections) — `session_16/impact_analysis_index.json`
- **repo_service.DeleteUnadoptedRepository** (2 connections) — `session_16/impact_analysis_index.json`
- **repo_service.ListUnadoptedRepositories** (2 connections) — `session_16/impact_analysis_index.json`
- **database.iterate_buffer_size** (1 connections) — `modules/setting/database.go`
- **admin.AdoptRepository** (1 connections) — `session_16/api_contracts.json`
- **admin.DeleteUnadoptedRepository** (1 connections) — `session_16/api_contracts.json`
- **admin.ListUnadoptedRepositories** (1 connections) — `session_16/api_contracts.json`
- **404 Owner username not found** (1 connections) — `session_16/error_handling.json`
- **404 Repo in DB or not on filesystem** (1 connections) — `session_16/error_handling.json`
- **500 Git operations or DB insert fails** (1 connections) — `session_16/error_handling.json`

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (6 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (3 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (1 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (1 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections]] (1 shared connections)

## Source Files

- `modules/setting/database.go`
- `modules/setting/repository.go`
- `routers/api/v1/admin/adopt.go`
- `session_16/api_contracts.json`
- `session_16/error_handling.json`
- `session_16/impact_analysis_index.json`
- `session_47/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*