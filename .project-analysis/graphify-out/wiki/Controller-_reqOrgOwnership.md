# Controller: reqOrgOwnership

> 109 nodes · cohesion 0.04

## Key Concepts

- **reqOrgOwnership** (27 connections) — `routers/api/v1/api.go`
- **organization.Team** (23 connections) — `session_49/impact_analysis_index.json`
- **PUT /api/v1/teams/{id}/repos/{org}/{repo}** (18 connections) — `session_10/api_contracts.json`
- **orgAssignment(false, true)** (17 connections) — `routers/api/v1/api.go`
- **organization** (16 connections) — `routers/api/v1/org/team.go`
- **POST /api/v1/orgs/{org}/teams** (16 connections) — `session_9/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/teams/{team}** (16 connections) — `session_49/api_contracts.json`
- **PATCH /api/v1/teams/{id}** (15 connections) — `session_9/api_contracts.json`
- **PUT /api/v1/teams/{id}/members/{username}** (13 connections) — `session_9/api_contracts.json`
- **GET /api/v1/teams/{id}/repos** (13 connections) — `session_10/api_contracts.json`
- **DELETE /api/v1/teams/{id}/repos/{org}/{repo}** (13 connections) — `session_10/api_contracts.json`
- **GET /api/v1/orgs/{org}/activities/feeds** (12 connections) — `session_6/api_contracts.json`
- **DELETE /api/v1/teams/{id}/members/{username}** (12 connections) — `session_9/api_contracts.json`
- **GET /api/v1/users/{username}/activities/feeds** (12 connections) — `session_18/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/teams/{team}** (12 connections) — `session_49/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/teams/{team}** (12 connections) — `session_49/api_contracts.json`
- **reqTeamMembership()** (11 connections) — `routers/api/v1/api.go`
- **GET /api/v1/teams/{id}/members/{username}** (10 connections) — `session_9/api_contracts.json`
- **GET /api/v1/teams/{id}/repos/{org}/{repo}** (10 connections) — `session_10/api_contracts.json`
- **GET /api/v1/orgs/{org}/teams/search** (10 connections) — `session_10/api_contracts.json`
- **GET /api/v1/teams/{id}/activities/feeds** (10 connections) — `session_10/api_contracts.json`
- **organization.TeamUser** (10 connections) — `session_11/impact_analysis_index.json`
- **GET /api/v1/teams/{id}/members** (9 connections) — `session_9/api_contracts.json`
- **feed_service.GetFeeds** (9 connections) — `session_54/impact_analysis_index.json`
- **GET /api/v1/teams/{id}** (8 connections) — `session_9/api_contracts.json`
- *... and 84 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (29 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (26 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (18 shared connections)
- [[Controller: POST /api/v1/orgs]] (15 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (11 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (6 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (4 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (3 shared connections)
- [[Endpoint: routers]] (2 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Controller: GET /api/v1/repos/search]] (1 shared connections)

## Source Files

- `models/activities/action_list.go`
- `models/organization/team_list.go`
- `models/organization/team_user.go`
- `modules/setting/service.go`
- `routers/api/v1/api.go`
- `routers/api/v1/org/org.go`
- `routers/api/v1/org/team.go`
- `routers/api/v1/repo/repo.go`
- `routers/api/v1/repo/teams.go`
- `routers/api/v1/user/user.go`
- `services/convert/activity.go`
- `session_10/api_contracts.json`
- `session_10/error_handling.json`
- `session_11/impact_analysis_index.json`
- `session_18/api_contracts.json`
- `session_48/api_contracts.json`
- `session_48/impact_analysis_index.json`
- `session_49/api_contracts.json`
- `session_49/error_handling.json`
- `session_49/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 533 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*