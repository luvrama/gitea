# Controller: GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}

> 11 nodes · cohesion 0.29

## Key Concepts

- **GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}** (8 connections) — `session_37/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/git/refs** (7 connections) — `session_37/api_contracts.json`
- **repo.getGitRefsInternal** (5 connections) — `routers/api/v1/repo/git_ref.go`
- **repository** (3 connections) — `routers/api/v1/repo/git_ref.go`
- **utils.GetGitRefs** (3 connections) — `routers/api/v1/utils/git.go`
- **api.Reference** (2 connections) — `session_37/impact_analysis_index.json`
- **repo.GetGitAllRefs** (2 connections) — `routers/api/v1/repo/git_ref.go`
- **repo.GetGitRefs** (2 connections) — `routers/api/v1/repo/git_ref.go`
- **repo.GetGitAllRefs** (1 connections) — `session_37/api_contracts.json`
- **repo.GetGitRefs** (1 connections) — `session_37/api_contracts.json`
- **404 Empty refs list** (1 connections) — `session_37/error_handling.json`

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)

## Source Files

- `routers/api/v1/repo/git_ref.go`
- `routers/api/v1/utils/git.go`
- `session_37/api_contracts.json`
- `session_37/error_handling.json`
- `session_37/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 35 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*