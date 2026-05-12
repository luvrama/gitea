# Phase 2 Session Report

**Session:** 3
**Endpoints Analyzed:** ep-015 to ep-022
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 7 unique operation types
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3.25 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-015 | GET | /api/v1/settings/ui | 1 step | 3 files | 0 |
| ep-016 | GET | /api/v1/settings/api | 1 step | 3 files | 0 |
| ep-017 | GET | /api/v1/settings/repository | 1 step | 4 files | 0 |
| ep-018 | GET | /api/v1/settings/attachment | 1 step | 3 files | 0 |
| ep-019 | GET | /api/v1/notifications | 5 steps | 7 files | 1 |
| ep-020 | PUT | /api/v1/notifications | 5 steps | 7 files | 2 |
| ep-021 | GET | /api/v1/notifications/new | 1 step | 4 files | 0 |
| ep-022 | GET | /api/v1/repos/{owner}/{repo}/notifications | 6 steps | 7 files | 1 |

## Performance Issues Found

| Severity | Endpoint | Issue | Recommendation |
|----------|----------|-------|----------------|
| HIGH | ep-020 | N+1 writes: SetNotificationStatus called per notification in loop | Bulk UPDATE with WHERE id IN (...) |
| HIGH | ep-020 | Unbounded query: no pagination on initial find | Add limit or process in batches |
| MEDIUM | ep-019 | N+1 in convert: GetIndividualUserRepoPermission per notification | Batch permission check |
| MEDIUM | ep-022 | N+1 in convert: redundant permission checks for same repo | Compute permission once |

## Key Findings

1. **Settings endpoints (ep-015 to ep-018)** are trivial - pure in-memory reads from package-level variables loaded at startup. Zero database or external I/O. No authentication required.

2. **Notification list endpoints (ep-019, ep-022)** use a good batch-loading pattern for attributes (repos, issues, users, comments) but then lose the benefit in the convert layer where per-notification permission checks and GetLastComment calls create N+1 patterns.

3. **ReadNotifications (ep-020)** is the most problematic endpoint: unbounded query + per-item update loop + per-item attribute loading + per-item permission check. A user with many unread notifications could trigger hundreds of DB queries.

4. **NewAvailable (ep-021)** is well-optimized - single COUNT query using the composite index `u_s_uu` (user_id, status, updated_unix). Good candidate for short-lived caching if polling frequency is high.

## Files Read
- routers/api/v1/settings/settings.go
- routers/api/v1/notify/notifications.go
- routers/api/v1/notify/user.go
- routers/api/v1/notify/repo.go
- routers/api/v1/notify/threads.go
- routers/api/v1/api.go (lines 299-370, 948-970, 1450-1465)
- modules/structs/settings.go
- modules/structs/notifications.go
- modules/setting/ui.go
- modules/setting/api.go
- modules/setting/mirror.go
- modules/setting/repository.go
- modules/setting/attachment.go
- modules/setting/lfs.go
- modules/setting/service.go
- models/activities/notification.go
- models/activities/notification_list.go
- models/db/list.go
- services/convert/notification.go
- services/convert/utils.go
- services/context/utils.go
- routers/api/v1/utils/page.go
