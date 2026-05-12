# Controller: Pinned issues are separated by type (issues vs pull requests)

> 100 nodes · cohesion 0.03

## Key Concepts

- **Pinned issues are separated by type (issues vs pull requests)** (88 connections) — `models/issues/issue_pin.go`
- **GET /api/v1/notifications** (20 connections) — `session_3/api_contracts.json`
- **PUT /api/v1/notifications** (20 connections) — `session_3/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/notifications** (20 connections) — `session_3/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/notifications** (17 connections) — `session_4/api_contracts.json`
- **PATCH /api/v1/notifications/threads/{id}** (15 connections) — `session_4/api_contracts.json`
- **POST /api/v1/user/emails** (13 connections) — `session_26/api_contracts.json`
- **GET /api/v1/notifications/threads/{id}** (12 connections) — `session_4/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/diffpatch** (11 connections) — `session_37/api_contracts.json`
- **GET /api/v1/admin/emails/search** (10 connections) — `session_17/api_contracts.json`
- **GET /api/v1/settings/api** (9 connections) — `session_3/api_contracts.json`
- **GET /api/v1/admin/emails** (8 connections) — `session_17/api_contracts.json`
- **api.DEFAULT_PAGING_NUM** (7 connections) — `modules/setting/api.go`
- **GET /api/v1/notifications/new** (7 connections) — `session_3/api_contracts.json`
- **convert.ToNotificationThread** (7 connections) — `session_4/impact_analysis_index.json`
- **db.Find[Notification]** (7 connections) — `models/db/list.go`
- **db.Count[Notification]** (6 connections) — `models/db/list.go`
- **GET /api/v1/user/emails** (5 connections) — `session_26/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/actions/secrets** (5 connections) — `session_39/api_contracts.json`
- **EmailAddress** (5 connections) — `session_26/impact_analysis_index.json`
- **Notification.LoadAttributes** (5 connections) — `models/activities/notification.go`
- **activities_model.SetNotificationStatus (loop)** (5 connections) — `models/activities/notification.go`
- **api.MAX_RESPONSE_ITEMS** (4 connections) — `modules/setting/api.go`
- **user** (4 connections) — `routers/api/v1/user/email.go`
- **Notification** (4 connections) — `session_3/impact_analysis_index.json`
- *... and 75 more nodes in this community*

## Relationships

- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (15 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (15 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (14 shared connections)
- [[Controller: convert]] (9 shared connections)
- [[Controller: user_model.User]] (8 shared connections)
- [[Endpoint: routers]] (7 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (7 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (7 shared connections)
- [[Controller: POST /api/v1/orgs]] (7 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (5 shared connections)
- [[Controller: issues_model.Issue]] (5 shared connections)
- [[Controller: reqOrgOwnership]] (4 shared connections)

## Source Files

- `models/activities/notification.go`
- `models/activities/notification_list.go`
- `models/db/list.go`
- `models/issues/issue_pin.go`
- `models/user/email_address.go`
- `modules/setting/api.go`
- `modules/setting/service.go`
- `routers/api/v1/admin/email.go`
- `routers/api/v1/notify/notifications.go`
- `routers/api/v1/notify/repo.go`
- `routers/api/v1/notify/threads.go`
- `routers/api/v1/notify/user.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/repo/file.go`
- `routers/api/v1/repo/patch.go`
- `routers/api/v1/settings/settings.go`
- `routers/api/v1/user/email.go`
- `services/convert/notification.go`
- `services/repository/files/patch.go`
- `session_17/api_contracts.json`

## Audit Trail

- EXTRACTED: 447 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*