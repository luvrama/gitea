# Endpoint: routers

> 149 nodes · cohesion 0.01

## Key Concepts

- **routers** (103 connections) — `routers/`
- **repository** (14 connections) — `routers/api/v1/repo/file.go`
- **repository** (14 connections) — `routers/api/v1/repo/pull_review.go`
- **repository** (11 connections) — `routers/api/v1/repo/tag.go`
- **issue** (10 connections) — `routers/api/v1/repo/issue_comment.go`
- **GET /api/v1/repos/{owner}/{repo}/git/trees/{sha}** (10 connections) — `session_37/api_contracts.json`
- **GET /api/v1/label/templates/{name}** (9 connections) — `session_1/api_contracts.json`
- **issue** (8 connections) — `routers/api/v1/repo/issue.go`
- **repository** (7 connections) — `routers/api/v1/repo/wiki.go`
- **issue** (6 connections) — `routers/api/v1/repo/issue_comment_attachment.go`
- **issue** (6 connections) — `routers/api/v1/repo/milestone.go`
- **issue** (5 connections) — `routers/api/v1/repo/issue_tracked_time.go`
- **repository** (5 connections) — `routers/api/v1/repo/git_hook.go`
- **repository** (5 connections) — `routers/api/v1/repo/status.go`
- **GET /api/v1/version** (5 connections) — `session_1/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/licenses** (5 connections) — `session_51/api_contracts.json`
- **issue** (4 connections) — `routers/api/v1/repo/issue_stopwatch.go`
- **repository** (4 connections) — `routers/api/v1/repo/transfer.go`
- **GET /api/v1/label/templates** (4 connections) — `session_1/api_contracts.json`
- **miscellaneous** (3 connections) — `routers/api/v1/misc/label_templates.go`
- **repository** (3 connections) — `routers/api/v1/repo/issue_tracked_time.go`
- **repo_module.LoadTemplateLabelsByDisplayName** (3 connections) — `modules/repository/init.go`
- **miscellaneous** (2 connections) — `routers/api/v1/misc/version.go`
- **repository** (2 connections) — `routers/api/v1/repo/actions_run.go`
- **repository** (2 connections) — `routers/api/v1/repo/blob.go`
- *... and 124 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (8 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (8 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (7 shared connections)
- [[Controller: user_model.User]] (7 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (4 shared connections)
- [[Controller: webhook_service.ToHook]] (4 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (4 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (4 shared connections)
- [[Controller: convert]] (4 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/avatar]] (3 shared connections)
- [[Controller: POST /api/v1/user/keys]] (3 shared connections)
- [[Controller: issues_model.Issue]] (3 shared connections)

## Source Files

- `models/repo/license.go`
- `modules/repository/init.go`
- `modules/setting/api.go`
- `modules/setting/repository.go`
- `modules/setting/setting.go`
- `routers/`
- `routers/api/v1/misc/label_templates.go`
- `routers/api/v1/misc/version.go`
- `routers/api/v1/repo/actions_run.go`
- `routers/api/v1/repo/blob.go`
- `routers/api/v1/repo/compare.go`
- `routers/api/v1/repo/file.go`
- `routers/api/v1/repo/git_hook.go`
- `routers/api/v1/repo/issue.go`
- `routers/api/v1/repo/issue_comment.go`
- `routers/api/v1/repo/issue_comment_attachment.go`
- `routers/api/v1/repo/issue_stopwatch.go`
- `routers/api/v1/repo/issue_tracked_time.go`
- `routers/api/v1/repo/license.go`
- `routers/api/v1/repo/migrate.go`

## Audit Trail

- EXTRACTED: 386 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*