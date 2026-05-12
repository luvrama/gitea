# Controller: issues_model.Issue

> 68 nodes · cohesion 0.05

## Key Concepts

- **issues_model.Issue** (20 connections) — `session_55/impact_analysis_index.json`
- **POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions** (19 connections) — `session_44/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions** (14 connections) — `session_44/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/pin** (14 connections) — `session_55/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/pulls/pinned** (12 connections) — `session_55/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position}** (11 connections) — `session_55/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions** (10 connections) — `session_44/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/pinned** (10 connections) — `session_55/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/new_pin_allowed** (10 connections) — `session_55/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions** (9 connections) — `session_44/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/pin** (8 connections) — `session_55/api_contracts.json`
- **issue** (7 connections) — `routers/api/v1/repo/issue_reaction.go`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions** (7 connections) — `session_44/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/reactions** (7 connections) — `session_44/api_contracts.json`
- **issues_model.IssuePin** (6 connections) — `session_55/impact_analysis_index.json`
- **issues_model.Reaction** (6 connections) — `session_44/impact_analysis_index.json`
- **issues_model** (6 connections) — `session_55/impact_analysis_index.json`
- **issues_model.GetPinnedIssues** (6 connections) — `models/issues/issue_pin.go`
- **ui.REACTIONS** (5 connections) — `modules/setting/ui.go`
- **convert.ToAPIIssueList** (5 connections) — `services/convert/issue.go`
- **repo.changeIssueCommentReaction** (5 connections) — `routers/api/v1/repo/issue_reaction.go`
- **repo.changeIssueReaction** (5 connections) — `routers/api/v1/repo/issue_reaction.go`
- **issue** (4 connections) — `routers/api/v1/repo/issue_pin.go`
- **repository** (4 connections) — `routers/api/v1/repo/issue_pin.go`
- **issues_model.CreateReaction** (4 connections) — `models/issues/reaction.go`
- *... and 43 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (10 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (8 shared connections)
- [[Controller: convert]] (7 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (5 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (5 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (4 shared connections)
- [[Endpoint: routers]] (3 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (3 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors]] (1 shared connections)

## Source Files

- `models/issues/issue_list.go`
- `models/issues/issue_pin.go`
- `models/issues/reaction.go`
- `modules/setting/repository.go`
- `modules/setting/ui.go`
- `routers/api/v1/repo/issue_pin.go`
- `routers/api/v1/repo/issue_reaction.go`
- `services/convert/issue.go`
- `session_44/api_contracts.json`
- `session_44/error_handling.json`
- `session_44/impact_analysis_index.json`
- `session_55/api_contracts.json`
- `session_55/error_handling.json`
- `session_55/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 280 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*