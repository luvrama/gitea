# Phase 2 Session Report

**Session:** 4
**Endpoints Analyzed:** ep-023 to ep-028
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 5 tables involved
- External integrations used: 0
- Performance issues found: 3 (2 critical, 1 low)
- Average workflow depth: 4.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-023 | PUT | /api/v1/repos/{owner}/{repo}/notifications | 5 steps | 7 files | 2 (critical) |
| ep-024 | GET | /api/v1/notifications/threads/{id} | 3 steps | 5 files | 0 |
| ep-025 | PATCH | /api/v1/notifications/threads/{id} | 4 steps | 5 files | 1 (low) |
| ep-026 | GET | /api/v1/user/orgs | 3 steps | 4 files | 0 |
| ep-027 | GET | /api/v1/users/{username}/orgs | 4 steps | 5 files | 0 |
| ep-028 | GET | /api/v1/users/{username}/orgs/{org}/permissions | 5 steps | 6 files | 0 |

## Performance Issues Found

1. **CRITICAL** (ep-023): Unbounded query - `db.Find` without pagination loads ALL matching notifications
2. **CRITICAL** (ep-023): N+1 queries - per-notification loop with ~8 DB round-trips each (SetNotificationStatus + LoadAttributes + ToNotificationThread)
3. **LOW** (ep-025): Redundant fetch - `GetNotificationByID` called twice (once in getThread, once in SetNotificationStatus)

## Key Findings

- ep-023 has the same critical unbounded query + N+1 pattern as ep-020 (ReadNotifications). Both are "mark all as read" operations that should use batch UPDATE.
- Organization list endpoints (ep-026, ep-027) are well-designed with proper pagination via FindAndCount.
- ep-028 (GetUserOrgsPermissions) is efficient with only 2 targeted JOIN queries for permission resolution.
- The notification convert layer (ToNotificationThread) adds hidden N+1 queries via GetIndividualUserRepoPermission and GetLastComment per notification.

## Files Read
- routers/api/v1/notify/repo.go
- routers/api/v1/notify/threads.go
- routers/api/v1/notify/user.go
- routers/api/v1/notify/notifications.go
- routers/api/v1/org/org.go
- routers/api/v1/user/helper.go
- routers/api/v1/utils/page.go
- models/activities/notification.go
- models/activities/notification_list.go
- models/organization/org.go
- models/organization/org_list.go
- models/organization/org_user.go
- services/convert/notification.go
- services/convert/convert.go (lines 701-730)
- services/convert/utils.go (lines 15-22)
- services/context/user.go (lines 34-65)
- modules/structs/notifications.go
- modules/structs/org.go
- routers/api/v1/api.go (relevant sections)
