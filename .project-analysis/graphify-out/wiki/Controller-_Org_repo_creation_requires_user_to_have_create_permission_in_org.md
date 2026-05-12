# Controller: Org repo creation requires user to have create permission in org

> 42 nodes · cohesion 0.07

## Key Concepts

- **Org repo creation requires user to have create permission in org** (23 connections) — `routers/api/v1/repo/fork.go`
- **PUT /api/v1/repos/{owner}/{repo}/topics/{topic}** (13 connections) — `session_51/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/topics** (12 connections) — `session_51/api_contracts.json`
- **POST /api/v1/orgs/{org}/actions/runners/registration-token** (11 connections) — `session_7/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/topics/{topic}** (10 connections) — `session_51/api_contracts.json`
- **shared.GetRegistrationToken** (8 connections) — `routers/api/v1/shared/runners.go`
- **POST /api/v1/admin/actions/runners/registration-token** (7 connections) — `session_16/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/actions/runners/registration-token** (7 connections) — `session_40/api_contracts.json`
- **GET /api/v1/topics/search** (7 connections) — `session_51/api_contracts.json`
- **repository** (6 connections) — `routers/api/v1/repo/topic.go`
- **POST /api/v1/user/actions/runners/registration-token** (6 connections) — `session_25/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/topics** (6 connections) — `session_51/api_contracts.json`
- **repo_model.Topic** (5 connections) — `session_51/impact_analysis_index.json`
- **db.FindAndCount[repo_model.Topic]** (5 connections) — `models/db/find.go`
- **repo_model.RepoTopic** (4 connections) — `session_51/impact_analysis_index.json`
- **ActionRunnerToken** (3 connections) — `session_40/impact_analysis_index.json`
- **db.Count[repo_model.Topic]** (3 connections) — `models/db/find.go`
- **repo_model.SanitizeAndValidateTopics** (3 connections) — `models/repo/topic.go`
- **Action.CreateRegistrationToken** (2 connections) — `routers/api/v1/repo/action.go`
- **AddTopic** (2 connections) — `routers/api/v1/repo/topic.go`
- **DeleteTopic** (2 connections) — `routers/api/v1/repo/topic.go`
- **ListTopics** (2 connections) — `routers/api/v1/repo/topic.go`
- **TopicSearch** (2 connections) — `routers/api/v1/repo/topic.go`
- **UpdateTopics** (2 connections) — `routers/api/v1/repo/topic.go`
- **admin.CreateRegistrationToken** (2 connections) — `routers/api/v1/admin/runners.go`
- *... and 17 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (9 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (5 shared connections)
- [[Controller: POST /api/v1/orgs]] (5 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (4 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (4 shared connections)
- [[Controller: reqOrgOwnership]] (3 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (3 shared connections)
- [[Controller: webhook_service.ToHook]] (3 shared connections)
- [[Controller: convert]] (2 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: user_model.User]] (1 shared connections)

## Source Files

- `models/db/find.go`
- `models/repo/topic.go`
- `routers/api/v1/admin/runners.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/repo/fork.go`
- `routers/api/v1/repo/topic.go`
- `routers/api/v1/shared/runners.go`
- `routers/api/v1/user/runners.go`
- `services/convert/convert.go`
- `session_16/api_contracts.json`
- `session_25/api_contracts.json`
- `session_25/impact_analysis_index.json`
- `session_40/api_contracts.json`
- `session_40/impact_analysis_index.json`
- `session_51/api_contracts.json`
- `session_51/impact_analysis_index.json`
- `session_7/api_contracts.json`
- `session_7/error_handling.json`

## Audit Trail

- EXTRACTED: 175 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*