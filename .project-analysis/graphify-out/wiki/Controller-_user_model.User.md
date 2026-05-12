# Controller: user_model.User

> 151 nodes · cohesion 0.02

## Key Concepts

- **user_model.User** (58 connections) — `session_53/impact_analysis_index.json`
- **convert.ToUser** (28 connections) — `session_48/impact_analysis_index.json`
- **repo_model.Repository** (27 connections) — `session_54/impact_analysis_index.json`
- **orgAssignment** (20 connections) — `routers/api/v1/api.go`
- **user.GetContextUserByPathParam** (19 connections) — `routers/api/v1/user/helper.go`
- **API.DefaultPagingNum** (15 connections) — `modules/setting/api.go`
- **GET /api/v1/users/search** (15 connections) — `session_18/api_contracts.json`
- **GET /api/v1/orgs/{org}/members** (14 connections) — `session_11/api_contracts.json`
- **PUT /api/v1/orgs/{org}/public_members/{username}** (14 connections) — `session_11/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/members/{username}** (14 connections) — `session_11/api_contracts.json`
- **GET /api/v1/users/{username}/followers** (14 connections) — `session_20/api_contracts.json`
- **API.MaxResponseItems** (13 connections) — `modules/setting/api.go`
- **GET /api/v1/user/followers** (13 connections) — `session_20/api_contracts.json`
- **GET /api/v1/user/following** (13 connections) — `session_20/api_contracts.json`
- **organization.OrgUser** (13 connections) — `session_11/impact_analysis_index.json`
- **GET /api/v1/orgs/{org}/members/{username}** (12 connections) — `session_11/api_contracts.json`
- **DELETE /api/v1/orgs/{org}/public_members/{username}** (12 connections) — `session_11/api_contracts.json`
- **GET /api/v1/users/{username}** (12 connections) — `session_18/api_contracts.json`
- **GET /api/v1/users/{username}/following** (12 connections) — `session_21/api_contracts.json`
- **PUT /api/v1/user/following/{username}** (12 connections) — `session_21/api_contracts.json`
- **GET /api/v1/orgs/{org}/blocks** (11 connections) — `session_13/api_contracts.json`
- **GET /api/v1/users/{username}/heatmap** (11 connections) — `session_18/api_contracts.json`
- **GET /api/v1/users/{username}/subscriptions** (11 connections) — `session_28/api_contracts.json`
- **setting.API.DefaultPagingNum** (10 connections) — `modules/setting/api.go`
- **setting.API.MaxResponseItems** (10 connections) — `modules/setting/api.go`
- *... and 126 more nodes in this community*

## Relationships

- [[Controller: reqOrgOwnership]] (29 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (23 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (23 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (23 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (22 shared connections)
- [[Controller: POST /api/v1/orgs]] (21 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (9 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (8 shared connections)
- [[Error Scenario: POST /api/v1/admin/users]] (8 shared connections)
- [[Endpoint: routers]] (7 shared connections)
- [[Controller: webhook_service.ToHook]] (6 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (6 shared connections)

## Source Files

- `models/issues/label.go`
- `models/organization/org.go`
- `models/repo/star.go`
- `models/repo/watch.go`
- `models/user/block.go`
- `models/user/follow.go`
- `models/user/user.go`
- `modules/setting/api.go`
- `routers/api/v1/api.go`
- `routers/api/v1/org/block.go`
- `routers/api/v1/org/label.go`
- `routers/api/v1/org/member.go`
- `routers/api/v1/repo/star.go`
- `routers/api/v1/repo/subscriber.go`
- `routers/api/v1/user/action.go`
- `routers/api/v1/user/block.go`
- `routers/api/v1/user/follower.go`
- `routers/api/v1/user/helper.go`
- `routers/api/v1/user/user.go`
- `routers/api/v1/user/watch.go`

## Audit Trail

- EXTRACTED: 755 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*