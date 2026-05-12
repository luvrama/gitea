# Controller: convert

> 135 nodes · cohesion 0.03

## Key Concepts

- **convert** (25 connections) — `session_55/impact_analysis_index.json`
- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets** (24 connections) — `session_38/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets** (24 connections) — `session_52/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/releases** (20 connections) — `session_36/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}** (18 connections) — `session_52/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}** (16 connections) — `session_52/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}** (15 connections) — `session_38/api_contracts.json`
- **repo_model.Attachment** (15 connections) — `session_52/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/reviewers** (14 connections) — `session_38/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/releases** (13 connections) — `session_36/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/releases/{id}** (13 connections) — `session_36/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}** (13 connections) — `session_38/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag}** (13 connections) — `session_51/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/releases/tags/{tag}** (13 connections) — `session_51/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets** (13 connections) — `session_52/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}** (13 connections) — `session_52/api_contracts.json`
- **repo_model.Release** (13 connections) — `session_52/impact_analysis_index.json`
- **GET /api/v1/repos/{owner}/{repo}/releases/{id}** (12 connections) — `session_36/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/releases/{id}** (12 connections) — `session_36/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}** (12 connections) — `session_38/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets** (10 connections) — `session_38/api_contracts.json`
- **repo.checkReleaseMatchRepo** (10 connections) — `routers/api/v1/repo/release_attachment.go`
- **repo_model.GetAttachmentByID** (10 connections) — `models/repo/attachment.go`
- **GET /api/v1/repos/{owner}/{repo}/releases/latest** (9 connections) — `session_36/api_contracts.json`
- **Release.LoadAttributes** (9 connections) — `models/repo/release.go`
- *... and 110 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (18 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (16 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (14 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (12 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (9 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (8 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (7 shared connections)
- [[Controller: issues_model.Issue]] (7 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (5 shared connections)
- [[Endpoint: routers]] (4 shared connections)
- [[Controller: user_model.User]] (3 shared connections)
- [[Controller: webhook_service.ToHook]] (2 shared connections)

## Source Files

- `models/db/list.go`
- `models/repo/attachment.go`
- `models/repo/release.go`
- `models/repo/user_repo.go`
- `modules/git/repo.go`
- `modules/setting/attachment.go`
- `modules/setting/repository.go`
- `modules/setting/server.go`
- `modules/storage/storage.go`
- `routers/api/v1/repo/collaborators.go`
- `routers/api/v1/repo/issue_attachment.go`
- `routers/api/v1/repo/release.go`
- `routers/api/v1/repo/release_attachment.go`
- `routers/api/v1/repo/release_tags.go`
- `routers/api/v1/settings/settings.go`
- `services/attachment/attachment.go`
- `services/convert/attachment.go`
- `services/convert/release.go`
- `services/convert/user.go`
- `services/issue/review_request.go`

## Audit Trail

- EXTRACTED: 613 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*