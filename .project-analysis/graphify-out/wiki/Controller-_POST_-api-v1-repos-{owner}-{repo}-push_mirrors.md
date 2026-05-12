# Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors

> 50 nodes · cohesion 0.06

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/push_mirrors** (18 connections) — `session_35/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync** (14 connections) — `session_35/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/mirror-sync** (11 connections) — `session_35/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/push_mirrors/{name}** (11 connections) — `session_35/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/push_mirrors** (9 connections) — `session_35/api_contracts.json`
- **mirror.ENABLED** (7 connections) — `modules/setting/mirror.go`
- **repository** (7 connections) — `routers/api/v1/repo/mirror.go`
- **GET /api/v1/settings/ui** (7 connections) — `session_3/api_contracts.json`
- **GET /api/v1/settings/repository** (7 connections) — `session_3/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/push_mirrors/{name}** (7 connections) — `session_35/api_contracts.json`
- **convert.ToPushMirror** (6 connections) — `session_35/impact_analysis_index.json`
- **settings** (5 connections) — `routers/api/v1/settings/settings.go`
- **repo_model.PushMirror** (5 connections) — `session_35/impact_analysis_index.json`
- **api.PushMirror** (3 connections) — `session_35/impact_analysis_index.json`
- **mirror_service.AddPushMirrorRemote** (3 connections) — `session_35/impact_analysis_index.json`
- **repo.CreatePushMirror** (3 connections) — `routers/api/v1/repo/mirror.go`
- **mirror_service.AddPullMirrorToQueue** (2 connections) — `session_35/impact_analysis_index.json`
- **mirror_service.SyncPushMirror** (2 connections) — `session_35/impact_analysis_index.json`
- **repo.AddPushMirror** (2 connections) — `routers/api/v1/repo/mirror.go`
- **repo.GetPushMirrorByName** (2 connections) — `routers/api/v1/repo/mirror.go`
- **repo.ListPushMirrors** (2 connections) — `routers/api/v1/repo/mirror.go`
- **repo.MirrorSync** (2 connections) — `routers/api/v1/repo/mirror.go`
- **repo.PushMirrorSync** (2 connections) — `routers/api/v1/repo/mirror.go`
- **git.TIMEOUT.MIRROR** (1 connections) — `modules/setting/git.go`
- **lfs.START_SERVER** (1 connections) — `modules/setting/lfs.go`
- *... and 25 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (8 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (7 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (3 shared connections)
- [[Endpoint: routers]] (2 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (2 shared connections)
- [[Controller: convert]] (1 shared connections)
- [[Controller: issues_model.Issue]] (1 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (1 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (1 shared connections)

## Source Files

- `modules/setting/git.go`
- `modules/setting/lfs.go`
- `modules/setting/mirror.go`
- `modules/setting/repository.go`
- `modules/setting/ui.go`
- `routers/api/v1/repo/mirror.go`
- `routers/api/v1/settings/settings.go`
- `services/mirror/mirror_push.go`
- `session_3/api_contracts.json`
- `session_3/impact_analysis_index.json`
- `session_35/api_contracts.json`
- `session_35/error_handling.json`
- `session_35/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 164 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*