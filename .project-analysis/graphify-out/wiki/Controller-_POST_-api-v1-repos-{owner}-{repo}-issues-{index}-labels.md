# Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels

> 116 nodes · cohesion 0.03

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels** (20 connections) — `session_50/api_contracts.json`
- **issues_model.GetIssueByIndex** (20 connections) — `models/issues/issue.go`
- **PATCH /api/v1/repos/{owner}/{repo}/pulls/{index}** (19 connections) — `session_34/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions** (16 connections) — `session_33/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/issues/{index}/labels** (15 connections) — `session_50/api_contracts.json`
- **issues_model.Label** (15 connections) — `session_53/impact_analysis_index.json`
- **PATCH /api/v1/orgs/{org}/labels/{id}** (13 connections) — `session_13/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}** (12 connections) — `session_50/api_contracts.json`
- **PATCH /api/v1/repos/{owner}/{repo}/labels/{id}** (12 connections) — `session_53/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check** (11 connections) — `session_33/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/labels** (11 connections) — `session_53/api_contracts.json`
- **convert.ToLabel** (11 connections) — `services/convert/issue.go`
- **GET /api/v1/orgs/{org}/labels** (9 connections) — `session_12/api_contracts.json`
- **POST /api/v1/orgs/{org}/labels** (9 connections) — `session_12/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}** (9 connections) — `session_32/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}** (9 connections) — `session_32/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issues/{index}/labels** (9 connections) — `session_49/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels** (9 connections) — `session_50/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/labels** (9 connections) — `session_52/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/labels/{id}** (8 connections) — `session_52/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/labels/{id}** (7 connections) — `session_13/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/labels/{id}** (7 connections) — `session_53/api_contracts.json`
- **issue_service** (7 connections) — `session_50/impact_analysis_index.json`
- **issue** (6 connections) — `routers/api/v1/repo/issue_label.go`
- **issue** (6 connections) — `routers/api/v1/repo/label.go`
- *... and 91 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (17 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (14 shared connections)
- [[Controller: convert]] (14 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (13 shared connections)
- [[Controller: user_model.User]] (9 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (5 shared connections)
- [[Controller: issues_model.Issue]] (5 shared connections)
- [[Endpoint: routers]] (4 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (3 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (3 shared connections)
- [[Controller: POST /api/v1/orgs]] (2 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)

## Source Files

- `models/issues/issue.go`
- `models/issues/issue_label.go`
- `models/issues/issue_update.go`
- `models/issues/issue_watch.go`
- `models/issues/label.go`
- `models/user/user.go`
- `modules/label/label.go`
- `routers/api/v1/org/label.go`
- `routers/api/v1/repo/issue_label.go`
- `routers/api/v1/repo/issue_subscription.go`
- `routers/api/v1/repo/label.go`
- `routers/api/v1/repo/pull.go`
- `services/convert/issue.go`
- `services/issue/assignee.go`
- `services/issue/content.go`
- `services/issue/issue.go`
- `services/issue/label.go`
- `services/issue/milestone.go`
- `services/pull/edits.go`
- `services/pull/pull.go`

## Audit Trail

- EXTRACTED: 478 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*