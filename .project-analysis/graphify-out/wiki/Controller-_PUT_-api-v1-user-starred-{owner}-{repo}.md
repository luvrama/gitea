# Controller: PUT /api/v1/user/starred/{owner}/{repo}

> 26 nodes · cohesion 0.11

## Key Concepts

- **PUT /api/v1/user/starred/{owner}/{repo}** (13 connections) — `session_22/api_contracts.json`
- **GET /api/v1/users/{username}/starred** (10 connections) — `session_22/api_contracts.json`
- **GET /api/v1/user/starred** (8 connections) — `session_22/api_contracts.json`
- **DELETE /api/v1/user/starred/{owner}/{repo}** (8 connections) — `session_23/api_contracts.json`
- **GET /api/v1/user/starred/{owner}/{repo}** (7 connections) — `session_22/api_contracts.json`
- **user** (6 connections) — `routers/api/v1/user/star.go`
- **user.getStarredRepos** (5 connections) — `routers/api/v1/user/star.go`
- **setting.Repository.DisableStars** (4 connections) — `modules/setting/repository.go`
- **repo.Star** (4 connections) — `session_22/impact_analysis_index.json`
- **repo_model.StarRepo** (4 connections) — `session_23/impact_analysis_index.json`
- **user.GetMyStarredRepos** (2 connections) — `routers/api/v1/user/star.go`
- **user.GetStarredRepos** (2 connections) — `routers/api/v1/user/star.go`
- **user.Star** (2 connections) — `routers/api/v1/user/star.go`
- **user.Unstar** (2 connections) — `routers/api/v1/user/star.go`
- **user.GetMyStarredRepos** (1 connections) — `session_22/api_contracts.json`
- **user.GetStarredRepos** (1 connections) — `session_22/api_contracts.json`
- **user.IsStarring** (1 connections) — `session_22/api_contracts.json`
- **user.Star** (1 connections) — `session_22/api_contracts.json`
- **user.Unstar** (1 connections) — `session_23/api_contracts.json`
- **500 Database query failure** (1 connections) — `session_22/error_handling.json`
- **403 User blocked by repo owner** (1 connections) — `session_22/error_handling.json`
- **500 StarRepo fails** (1 connections) — `session_23/error_handling.json`
- **repo_model.Star** (1 connections) — `session_23/impact_analysis_index.json`
- **user.Blocking** (1 connections) — `session_22/impact_analysis_index.json`
- **repo_model.IsStaring** (1 connections) — `session_22/impact_analysis_index.json`
- *... and 1 more nodes in this community*

## Relationships

- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (5 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (5 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (1 shared connections)

## Source Files

- `modules/setting/repository.go`
- `routers/api/v1/user/star.go`
- `session_22/api_contracts.json`
- `session_22/error_handling.json`
- `session_22/impact_analysis_index.json`
- `session_23/api_contracts.json`
- `session_23/error_handling.json`
- `session_23/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*