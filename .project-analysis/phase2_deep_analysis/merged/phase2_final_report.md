# Phase 2 Deep Analysis - Final Report

**Analysis Date:** 2026-05-12
**Total Sessions:** 55
**Total Endpoints Analyzed:** 381

---

## Summary

- Total endpoints: 381
- Total business rules: 570
- Total database tables: 7
- Total external integrations: 7
- Total configuration properties: 109
- Total error patterns: 280
- Total performance issues: 198
- Total resiliency findings: 351

---

## Performance Issues Summary

- Critical: 2
- High: 36
- Medium: 105
- Low: 55

### Top Issues by Impact
| Severity | Type | Endpoint | Description |
|----------|------|----------|-------------|
| critical | unbounded_queries | ep-023 | db.Find called without ListOptions (no pagination), loading ALL matching notifications for the repo into memory |
| critical | n_plus_1_queries | ep-023 | For each notification: SetNotificationStatus does SELECT+UPDATE (2 queries), LoadAttributes does 4 SELECTs (repo, issue, user, comment), ToNotificationThread does GetIndividualUserRepoPermission + GetLastComment (2 more). Total: ~8 DB round-trips per notification. |
| high | n_plus_1_queries | ep-020 | SetNotificationStatus is called in a loop: each iteration does SELECT by ID + UPDATE. Then LoadAttributes does 4 individual queries per notification. |
| high | unbounded_queries | ep-020 | The initial db.Find has no pagination (ListOptions is zero-value). All matching notifications are loaded into memory. |
| high | n_plus_1_queries | ep-035 | convert.ToActivity calls GetDoerRepoPermission for each action in the result set |
| high | n_plus_1_queries | ep-052 | convert.ToActionWorkflowJob loads task, steps, and runner individually per job in a loop |
| high | n_plus_1_queries | ep-058 | When auth changes, RecalculateTeamAccesses is called per repo in a loop |
| high | n_plus_1_queries | ep-059 | RemoveAllRepositoriesFromTeam iterates all team repos, calling RecalculateTeamAccesses per repo, then iterates all members per repo for watch cleanup |
| high | n_plus_1_queries | ep-063 | Per-repo loop calling RecalculateUserAccess, ReconsiderWatches, and ReconsiderRepoIssuesAssignee |
| high | n_plus_1_queries | ep-064 | For each repository in the team, GetDoerRepoPermission is called individually, resulting in N+1 database queries |
| high | n_plus_1_queries | ep-067 | For each team member, HasAnyUnitAccess is called individually to check if they still have access, then WatchRepo/RemoveIssueWatchersByRepoID if not |
| high | n_plus_1_queries | ep-076 | RemoveOrgUser iterates over all user's repos calling WatchRepo per repo, then iterates over all teams calling removeTeamMember per team. Each removeTeamMember itself iterates over team repos calling RecalculateUserAccess per repo. |
| high | n_plus_1_queries | ep-089 | unstarRepos, unwatchRepos, unassignIssues, removeCollaborations all loop with page-by-page fetches and individual operations per item |
| high | n_plus_1_queries | ep-100 | Branch protection cleanup iterates ALL protected branches in batches, checking each for user ID |
| high | synchronous_blocking | ep-107 | Walks entire filesystem tree synchronously on each request |
| high | n_plus_1_queries | ep-127 | ToActivities calls GetDoerRepoPermission for each action's repo individually |
| high | n_plus_1_queries | ep-152 | For each starred repo, GetIndividualUserRepoPermission is called individually, loading units, checking collaborator status, and loading owner |
| high | n_plus_1_queries | ep-153 | Same N+1 pattern as ep-152 - individual permission check per starred repo |
| high | synchronous_blocking | ep-161 | RewriteAllPublicKeys rewrites the entire authorized_keys file from all keys in DB after every single key deletion |
| high | n_plus_1_queries | ep-172 | GetDoerRepoPermission called in a loop for each repository in the page |

---

## Resiliency Assessment Summary

**Overall Risk:** critical

### Dependency Resiliency
| Dependency | Has Timeout | Has Retry | Has Circuit Breaker | Blast Radius |
|------------|-------------|-----------|---------------------|--------------|
| process.GetManager().ExecDir | ❌ | ❌ | ❌ | ep-004, ep-005 |
| gitcmd.NewCommand.RunStdString | ❌ | ❌ | ❌ | ep-004, ep-005, ep-006, ep-007 |
| db.GetEngine / db.Find / db.Count | ❌ | ❌ | ❌ | ep-019, ep-020, ep-021, ep-022 |
| storage.ObjectStorage | ❌ | ❌ | ❌ | ep-037, ep-038, ep-128, ep-259, ep-261, ep-262, ep-263, ep-294, ep-298, ep-354, ep-356 |
| pwn.Client | ❌ | ❌ | ❌ | ep-098 |
| password.IsPwned | ❌ | ❌ | ❌ | ep-099 |
| ObjectStorage | ❌ | ❌ | ❌ | ep-129 |
| gitrepo.PushToExternal | ❌ | ❌ | ❌ | ep-235 |
| git.Repository | ❌ | ❌ | ❌ | ep-243, ep-244, ep-245 |
| gitrepo | ❌ | ❌ | ❌ | ep-334 |

### Single Points of Failure
- GPG binary availability for signing key endpoints
- SQL database - all notification endpoints depend on it with no fallback
- Database (all endpoints depend on it)
- Database (single connection, no read replicas configured by default)
- Database - all endpoints depend on it with no caching layer
- database
- Database (single XORM connection)
- Database (single point for all operations)
- Database (single connection pool)
- Database - all endpoints depend solely on the database
- HaveIBeenPwned API (for user creation with PasswordCheckPwn=true)
- HaveIBeenPwned API for password validation (when enabled)
- Filesystem (RepoRootPath) for unadopted repo operations
- Database - all endpoints depend on DB availability
- Database (all endpoints depend on it with no fallback)
- Database (single instance unless externally replicated)
- Filesystem for authorized_keys file (mitigated by builtin SSH server option)
- Database (all write operations depend on it)
- Database (single instance unless configured with replication)
- Database
- Database - all endpoints depend on single DB connection
- Git storage (filesystem) - required for diff/patch and branch SHA resolution
- Git repository storage (local filesystem or NFS)
- Mirror queue (single instance, no redundancy unless backed by Redis)
- Database (single DB connection for all operations)
- Local git repository filesystem
- Object storage backend for attachments
- Object storage backend - no redundancy or fallback if storage is unavailable
- Database (single instance typical in small deployments)
- authorized_keys file - single file rewritten on every key change
- Object storage backend - no redundancy or fallback configured

### Cascading Failure Paths
- Database down → all notification endpoints (ep-019 to ep-022) return errors → UI notification badge broken
- ep-023 unbounded query can overload database, affecting all other endpoints sharing the connection pool
- Database down → all 7 endpoints fail immediately
- Storage backend down → ep-037/ep-038 fail, others unaffected
- Database down → all 6 endpoints return 500
- HaveIBeenPwned API down → ep-098 user creation fails with 400
- HIBP API down → ep-099 password updates fail (when PASSWORD_CHECK_PWN enabled)
- Database overload from ep-127 N+1 queries → connection pool exhaustion → all API endpoints fail
- Database slow → ep-192 BlockUser transaction holds locks for extended time → other write operations blocked
- Git storage slow → ep-222 list timeout → client retries → increased load
- Git storage down → all PR create/merge/update/commits/files endpoints fail
- Remote git server down → ep-235 blocks for full timeout × N mirrors → HTTP timeout for caller
- Database down → all release endpoints fail
- Git repository filesystem unavailable → create/edit/delete fail, reads still work from DB
- Storage down → ep-259 upload fails → users cannot attach files to issues
- Storage down → ep-261 delete partially fails → orphaned files accumulate
- Storage outage → ep-298 download fails → CI/CD pipelines that depend on artifact downloads break
- Many concurrent fork requests → disk I/O saturation → all git operations slow down
- SSHOpLocker contention → all key operations blocked during rewrite
- Storage down → ep-354 upload fails → users cannot attach files to releases

---

## Endpoints by HTTP Method

- GET: 0
- POST: 0
- PUT: 0
- PATCH: 0
- DELETE: 0

---

## Database Operations

- Total tables: 7
- Total operations mapped: 381

---

## External Integrations

- Total integrations: 7

---

## Business Rules by Category

- validation: 190
- business_logic: 245
- authorization: 125
- state_transition: 8
- eligibility: 2

---

## Top 10 Most Complex Endpoints

| Rank | Endpoint | Method | Path | Workflow Steps | Files Involved |
|------|----------|--------|------|----------------|----------------|


---

## Impact Analysis

See `impact_analysis_index.json` for full cross-reference data mapping tables, services, and config properties to affected endpoints.

---

## Session Breakdown


---

## Session 1

# Phase 2 Session Report

**Session:** 1
**Endpoints Analyzed:** ep-001 to ep-008
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 7
- Database operations documented: 0
- External integrations used: 1 (GPG binary)
- Performance issues found: 7
- Average workflow depth: 2.1 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-001 | GET | /api/v1/version | 1 step | 2 files | 0 |
| ep-002 | GET | /api/v1/label/templates | 1 step | 3 files | 0 |
| ep-003 | GET | /api/v1/label/templates/{name} | 3 steps | 5 files | 1 |
| ep-004 | GET | /api/v1/signing-key.gpg | 3 steps | 4 files | 2 |
| ep-005 | GET | /api/v1/repos/{owner}/{repo}/signing-key.gpg | 2 steps | 4 files | 2 |
| ep-006 | GET | /api/v1/signing-key.pub | 2 steps | 4 files | 1 |
| ep-007 | GET | /api/v1/repos/{owner}/{repo}/signing-key.pub | 2 steps | 4 files | 1 |
| ep-008 | POST | /api/v1/markup | 3 steps | 5 files | 1 |

## Performance Issues Found

| Severity | Endpoint | Issue | Recommendation |
|----------|----------|-------|----------------|
| medium | ep-004, ep-005 | No timeout on gpg --export (-1 = infinite) | Add 10s timeout to ExecDir |
| medium | ep-004, ep-005 | No caching of GPG key export | Cache with TTL |
| medium | ep-008 | No render timeout/input size limit | Add context timeout |
| low | ep-003 | Label template file read per request | Cache parsed templates |
| low | ep-006, ep-007 | SSH key file read per request | Cache key content |

## Files Read
- routers/api/v1/misc/version.go
- routers/api/v1/misc/label_templates.go
- routers/api/v1/misc/signing.go
- routers/api/v1/misc/markup.go
- routers/api/v1/misc/gitignore.go
- routers/api/v1/misc/licenses.go
- routers/common/markup.go
- modules/structs/miscellaneous.go
- modules/structs/issue_label.go
- modules/repository/init.go
- modules/options/base.go
- modules/git/key.go
- modules/markup/render.go
- modules/markup/markdown/markdown.go
- services/asymkey/sign.go
- services/convert/issue.go
- services/context/api.go


---

## Session 2

# Phase 2 Session Report

**Session:** 2
**Endpoints Analyzed:** ep-009 to ep-014
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 0 (all stateless)
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 2.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-009 | POST | /api/v1/markdown | 4 steps | 6 files | 1 |
| ep-010 | POST | /api/v1/markdown/raw | 2 steps | 4 files | 1 |
| ep-011 | GET | /api/v1/gitignore/templates | 1 step | 3 files | 0 |
| ep-012 | GET | /api/v1/gitignore/templates/{name} | 3 steps | 4 files | 1 |
| ep-013 | GET | /api/v1/licenses | 1 step | 3 files | 0 |
| ep-014 | GET | /api/v1/licenses/{name} | 3 steps | 4 files | 1 |

## Performance Issues Found

| Severity | Endpoint | Issue | Recommendation |
|----------|----------|-------|----------------|
| medium | ep-009 | No timeout on markdown rendering | Add context.WithTimeout (30s) |
| medium | ep-010 | No timeout/size limit on raw body | Add io.LimitReader + context.WithTimeout |
| low | ep-012 | No HTTP caching for static gitignore files | Add Cache-Control headers |
| low | ep-014 | No HTTP caching for static license files | Add Cache-Control headers |

## Key Observations

1. All 6 endpoints are stateless - no database access, no external service calls
2. ep-011 and ep-013 return pre-loaded in-memory data (loaded at startup via LoadRepoConfig)
3. ep-012 and ep-014 read from a layered filesystem (custom path → bindata)
4. ep-009 and ep-010 are CPU-bound (markdown parsing + HTML sanitization)
5. Path traversal is prevented via util.PathJoinRelX sanitization
6. The deprecated Wiki field provides backward compatibility in ep-009

## Files Read

- routers/api/v1/misc/markup.go
- routers/api/v1/misc/gitignore.go
- routers/api/v1/misc/licenses.go
- routers/common/markup.go
- modules/structs/miscellaneous.go
- modules/repository/init.go
- modules/options/base.go
- modules/assetfs/layered.go
- modules/markup/markdown/markdown.go
- modules/markup/render.go
- modules/markup/sanitizer_default.go
- models/renderhelper/simple_document.go
- modules/util/path.go
- modules/setting/server.go
- modules/setting/repository.go
- routers/api/v1/api.go
- services/context/api.go


---

## Session 3

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


---

## Session 4

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


---

## Session 5

# Phase 2 Session Report

**Session:** 5
**Endpoints Analyzed:** ep-029 to ep-034
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 12
- Database operations documented: 37 (across all endpoints)
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-029 | GET | /api/v1/orgs | 5 steps | 6 files | 0 |
| ep-030 | POST | /api/v1/orgs | 5 steps | 5 files | 0 |
| ep-031 | GET | /api/v1/orgs/{org} | 5 steps | 4 files | 0 |
| ep-032 | POST | /api/v1/orgs/{org}/rename | 4 steps | 5 files | 1 |
| ep-033 | PATCH | /api/v1/orgs/{org} | 6 steps | 5 files | 0 |
| ep-034 | DELETE | /api/v1/orgs/{org} | 3 steps | 4 files | 1 |

## Performance Issues Found

1. **ep-032 (medium)**: Filesystem directory rename happens inside transaction commit path. If filesystem is slow (NFS), request blocks and transaction is held open.
2. **ep-034 (low)**: Filesystem removal and avatar storage deletion happen synchronously after transaction commit. Rare operation, minimal impact.

## Key Findings

- All 6 endpoints are database-only (no external service calls)
- Organization CRUD operations are well-structured with proper transaction usage
- The `orgAssignment(true)` middleware handles org resolution and user redirects transparently
- `reqOrgOwnership()` middleware provides consistent authorization (org owner or site admin)
- The `CreateOrganization` function is a well-designed atomic operation creating org + owner team + units + membership in a single transaction
- `DeleteOrganization` properly validates no repos/packages exist before deletion
- The rename operation has a known edge case where filesystem rename + DB commit are not fully atomic

## Files Read
- routers/api/v1/org/org.go
- routers/api/v1/api.go (lines 241-290, 455-585, 586-640, 1604-1680)
- routers/api/v1/utils/page.go
- models/organization/org.go
- models/organization/org_list.go
- models/organization/org_user.go
- models/organization/team.go
- models/organization/team_user.go
- models/organization/team_unit.go
- models/organization/team_repo.go
- models/user/user.go
- models/user/search.go
- models/user/email_address.go
- modules/structs/org.go
- services/convert/convert.go
- services/convert/utils.go
- services/user/user.go
- services/user/update.go
- services/org/org.go


---

## Session 6

# Phase 2 Session Report

**Session:** 6
**Endpoints Analyzed:** ep-035 to ep-041
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 12
- Database operations documented: 21
- External integrations used: 1 (Avatar Storage Backend)
- Performance issues found: 3
- Average workflow depth: 3.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-035 | GET | /api/v1/orgs/{org}/activities/feeds | 5 steps | 6 files | 1 (high) |
| ep-036 | DELETE | /api/v1/orgs/{org}/repos | 3 steps | 4 files | 2 (medium) |
| ep-037 | POST | /api/v1/orgs/{org}/avatar | 4 steps | 4 files | 1 (low) |
| ep-038 | DELETE | /api/v1/orgs/{org}/avatar | 4 steps | 3 files | 0 |
| ep-039 | GET | /api/v1/orgs/{org}/actions/secrets | 2 steps | 3 files | 0 |
| ep-040 | PUT | /api/v1/orgs/{org}/actions/secrets/{secretname} | 3 steps | 4 files | 0 |
| ep-041 | DELETE | /api/v1/orgs/{org}/actions/secrets/{secretname} | 3 steps | 3 files | 0 |

## Performance Issues Found

1. **HIGH** (ep-035): N+1 queries in convert.ToActivities - GetDoerRepoPermission called per action item. Fix: batch-load permissions for unique repos.
2. **MEDIUM** (ep-036): Unbounded query loads all org repo IDs at once (acceptable since only IDs, not full objects).
3. **MEDIUM** (ep-036): Background deletion loops repos one-by-one (acceptable for resilience - continues on failure).

## Key Findings

- ep-036 uses an excellent async pattern: returns 202 immediately, deletes in background with graceful shutdown context
- ep-037/ep-038 avatar operations use proper transactions to ensure DB/storage consistency
- Secret endpoints (ep-039 to ep-041) are simple CRUD with good validation (name regex, forbidden prefixes, size limits)
- Secret data is encrypted at rest using SECRET_KEY from app.ini

## Files Read
- routers/api/v1/org/org.go
- routers/api/v1/org/avatar.go
- routers/api/v1/org/action.go
- routers/api/v1/api.go
- services/feed/feed.go
- services/convert/activity.go
- services/user/avatar.go
- services/secrets/secrets.go
- services/secrets/validation.go
- services/repository/repository.go
- models/activities/action.go
- models/activities/action_list.go
- models/secret/secret.go
- models/repo/org_repo.go
- modules/avatar/avatar.go
- modules/structs/activity.go
- modules/structs/secret.go
- modules/structs/user.go
- routers/api/v1/utils/page.go


---

## Session 7

# Phase 2 Session Report

**Session:** 7
**Endpoints Analyzed:** ep-042 to ep-049
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 14
- External integrations used: 0
- Performance issues found: 1 (low severity)
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-042 | POST | /api/v1/orgs/{org}/actions/runners/registration-token | 3 steps | 4 files | 0 |
| ep-043 | GET | /api/v1/orgs/{org}/actions/variables | 3 steps | 4 files | 0 |
| ep-044 | GET | /api/v1/orgs/{org}/actions/variables/{variablename} | 3 steps | 4 files | 0 |
| ep-045 | DELETE | /api/v1/orgs/{org}/actions/variables/{variablename} | 3 steps | 4 files | 0 |
| ep-046 | POST | /api/v1/orgs/{org}/actions/variables/{variablename} | 3 steps | 5 files | 1 |
| ep-047 | PUT | /api/v1/orgs/{org}/actions/variables/{variablename} | 3 steps | 5 files | 0 |
| ep-048 | GET | /api/v1/orgs/{org}/actions/runners | 3 steps | 4 files | 0 |
| ep-049 | GET | /api/v1/orgs/{org}/actions/runners/{runner_id} | 3 steps | 4 files | 0 |

## Performance Issues Found
- **ep-046 (low)**: Existence check before insert could rely on DB unique constraint instead of pre-check SELECT. Minor optimization opportunity.

## Resiliency Findings
- **ep-046**: TOCTOU race condition on create (check existence then insert without transaction). Mitigated by DB unique constraint.
- **ep-047**: Read-then-update without transaction. Low risk due to org ownership requirement.
- All endpoints are database-only with no external dependencies, making them inherently resilient.

## Key Patterns Observed
- All 8 endpoints share the same middleware chain: tokenRequiresScopes → orgAssignment(true) → reqToken → reqOrgOwnership
- Variables and runners use a shared `addActionsRoutes` function that provides consistent route structure across org/repo/user/admin levels
- The `shared` package (routers/api/v1/shared/) contains reusable handler logic for runners that works across all ownership contexts
- Variable names are always uppercased and validated against GitHub Actions naming conventions

## Files Read
- routers/api/v1/org/action.go
- routers/api/v1/shared/runners.go
- routers/api/v1/shared/action.go
- routers/api/v1/api.go (partial - route registration, middleware)
- routers/api/v1/utils/page.go
- services/actions/variables.go
- services/actions/interface.go
- services/secrets/validation.go
- services/convert/convert.go (partial - ToActionRunner)
- services/convert/utils.go (partial - ToCorrectPageSize)
- models/actions/variable.go
- models/actions/runner.go
- models/actions/runner_token.go
- modules/structs/repo_actions.go
- modules/structs/variable.go


---

## Session 8

# Phase 2 Session Report

**Session:** 8
**Endpoints Analyzed:** ep-050 to ep-055
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 22
- External integrations used: 0
- Performance issues found: 5 (1 high, 3 medium, 1 low)
- Average workflow depth: 3.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-050 | DELETE | /api/v1/orgs/{org}/actions/runners/{runner_id} | 4 steps | 4 files | 1 (low) |
| ep-051 | PATCH | /api/v1/orgs/{org}/actions/runners/{runner_id} | 5 steps | 4 files | 1 (low) |
| ep-052 | GET | /api/v1/orgs/{org}/actions/jobs | 3 steps | 5 files | 1 (high) |
| ep-053 | GET | /api/v1/orgs/{org}/actions/runs | 3 steps | 5 files | 1 (medium) |
| ep-054 | GET | /api/v1/orgs/{org}/teams | 3 steps | 4 files | 1 (medium) |
| ep-055 | GET | /api/v1/user/teams | 3 steps | 4 files | 1 (medium) |

## Performance Issues Found

1. **HIGH** (ep-052): N+1 queries in ToActionWorkflowJob - loads task, steps, and runner per job individually. Up to 60 extra queries for a page of 20 jobs.
2. **MEDIUM** (ep-053): N+1 queries in ToActionWorkflowRun - loads latest attempt per run individually. 20 extra queries per page.
3. **MEDIUM** (ep-054, ep-055): N+1 queries in ToTeams - LoadUnits called per team individually. 20 extra queries per page.

## Files Read
- routers/api/v1/org/action.go
- routers/api/v1/shared/runners.go
- routers/api/v1/shared/action.go
- routers/api/v1/org/team.go
- models/actions/runner.go
- models/actions/run.go
- models/actions/run_list.go
- models/actions/run_job.go
- models/actions/run_job_list.go
- models/actions/tasks_version.go
- models/organization/team.go
- models/organization/team_list.go
- modules/structs/repo_actions.go
- modules/structs/org_team.go
- services/convert/convert.go
- routers/api/v1/utils/page.go


---

## Session 9

# Phase 2 Session Report

**Session:** 9
**Endpoints Analyzed:** ep-056 to ep-063
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 7 tables involved
- External integrations used: 0
- Performance issues found: 6 (2 high, 3 medium, 1 low)
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-056 | GET | /api/v1/teams/{id} | 3 steps | 5 files | 1 (low) |
| ep-057 | POST | /api/v1/orgs/{org}/teams | 5 steps | 6 files | 1 (medium) |
| ep-058 | PATCH | /api/v1/teams/{id} | 5 steps | 6 files | 1 (high) |
| ep-059 | DELETE | /api/v1/teams/{id} | 3 steps | 7 files | 3 (high+2 medium) |
| ep-060 | GET | /api/v1/teams/{id}/members | 2 steps | 4 files | 0 |
| ep-061 | GET | /api/v1/teams/{id}/members/{username} | 3 steps | 4 files | 0 |
| ep-062 | PUT | /api/v1/teams/{id}/members/{username} | 3 steps | 6 files | 1 (medium) |
| ep-063 | DELETE | /api/v1/teams/{id}/members/{username} | 3 steps | 6 files | 1 (high) |

## Performance Issues Found

1. **HIGH** (ep-058): EditTeam with auth change triggers per-repo RecalculateTeamAccesses in a loop - O(N) repos
2. **HIGH** (ep-059): DeleteTeam does per-repo access recalculation + per-member watch cleanup - O(R*M) queries
3. **HIGH** (ep-063): RemoveTeamMember does per-repo RecalculateUserAccess + ReconsiderWatches + ReconsiderRepoIssuesAssignee - O(3*N) repos
4. **MEDIUM** (ep-057): CreateTeam with IncludesAllRepositories loads all org repos unbounded
5. **MEDIUM** (ep-059): RemoveTeamIDFromProtectedBranch called per branch protection in loop
6. **MEDIUM** (ep-062): Auto-watch goroutine calls WatchRepo per team repo (async, non-blocking)

## Key Findings

- All team mutation operations (create/edit/delete/add member/remove member) use database transactions correctly
- The N+1 pattern in access recalculation is a systemic issue across team operations
- Auto-watch on AddTeamMember runs in a goroutine, preventing response blocking but creating background DB load
- Owner team has special protections: cannot change permissions, cannot remove last member
- Team name "new" is reserved (only reserved name)

## Files Read
- routers/api/v1/org/team.go
- routers/api/v1/api.go
- services/org/team.go
- services/convert/convert.go
- services/convert/user.go
- services/org/user.go
- services/repository/repo_team.go
- models/organization/team.go
- models/organization/team_user.go
- models/organization/team_unit.go
- models/organization/team_list.go
- models/organization/org.go
- models/organization/org_user.go
- models/user/block.go
- modules/structs/org_team.go
- routers/api/v1/user/helper.go


---

## Session 10

# Phase 2 Session Report

**Session:** 10
**Endpoints Analyzed:** ep-064 to ep-069
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 39
- External integrations used: 0
- Performance issues found: 5
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-064 | GET | /api/v1/teams/{id}/repos | 3 steps | 6 files | 1 (high) |
| ep-065 | GET | /api/v1/teams/{id}/repos/{org}/{repo} | 3 steps | 5 files | 0 |
| ep-066 | PUT | /api/v1/teams/{id}/repos/{org}/{repo} | 3 steps | 6 files | 1 (medium) |
| ep-067 | DELETE | /api/v1/teams/{id}/repos/{org}/{repo} | 3 steps | 6 files | 1 (high) |
| ep-068 | GET | /api/v1/orgs/{org}/teams/search | 3 steps | 5 files | 1 (medium) |
| ep-069 | GET | /api/v1/teams/{id}/activities/feeds | 3 steps | 6 files | 1 (medium) |

## Performance Issues Found

1. **ep-064 (HIGH)**: N+1 queries - GetDoerRepoPermission called per repo in loop
2. **ep-067 (HIGH)**: N+1 queries - HasAnyUnitAccess called per team member when removing repo
3. **ep-066 (MEDIUM)**: N+1 queries - WatchRepo called per team member when AutoWatchNewRepos enabled
4. **ep-068 (MEDIUM)**: N+1 queries - LoadUnits called per team in convert.ToTeams
5. **ep-069 (MEDIUM)**: Unbounded query - all team repo IDs materialized into IN clause

## Files Read
- routers/api/v1/org/team.go
- routers/api/v1/api.go
- models/organization/team_repo.go
- models/organization/team_list.go
- models/organization/team.go
- models/repo/org_repo.go
- models/repo/repo.go
- models/perm/access/repo_permission.go
- models/activities/action.go
- models/activities/action_list.go
- services/repository/repo_team.go
- services/feed/feed.go
- services/convert/convert.go
- services/convert/activity.go
- services/convert/repository.go
- routers/api/v1/utils/page.go
- modules/structs/org_team.go
- modules/structs/activity.go


---

## Session 11

# Phase 2 Session Report

**Session:** 11
**Endpoints Analyzed:** ep-070 to ep-076
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 10
- Database operations documented: 5 tables
- External integrations used: 0
- Performance issues found: 2 (both on ep-076)
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-070 | GET | /api/v1/orgs/{org}/members | 3 steps | 6 files | 0 |
| ep-071 | GET | /api/v1/orgs/{org}/public_members | 2 steps | 5 files | 0 |
| ep-072 | GET | /api/v1/orgs/{org}/members/{username} | 3 steps | 5 files | 0 |
| ep-073 | GET | /api/v1/orgs/{org}/public_members/{username} | 3 steps | 5 files | 0 |
| ep-074 | PUT | /api/v1/orgs/{org}/public_members/{username} | 5 steps | 6 files | 0 |
| ep-075 | DELETE | /api/v1/orgs/{org}/public_members/{username} | 5 steps | 6 files | 0 |
| ep-076 | DELETE | /api/v1/orgs/{org}/members/{username} | 4 steps | 7 files | 2 |

## Performance Issues Found

1. **HIGH** (ep-076): N+1 queries in RemoveOrgUser - iterates repos calling WatchRepo per repo, iterates teams calling removeTeamMember per team (which itself iterates repos for RecalculateUserAccess)
2. **MEDIUM** (ep-076): Long-running transaction - entire member removal with all team/repo cleanup in single transaction

## Key Patterns

- All 7 endpoints share the same orgAssignment(true) middleware for org resolution
- ep-070/071 use a shared `listMembers` helper with visibility filtering via `PublicOnly()` method
- ep-072 has unique 303 redirect behavior for non-member doers
- ep-074/075 share `checkCanChangeOrgUserStatus` authorization helper
- ep-076 is the most complex with cascading deletions across multiple tables

## Files Read
- routers/api/v1/org/member.go
- routers/api/v1/api.go (lines 455-560, 1610-1670)
- routers/api/v1/user/helper.go
- models/organization/org.go (lines 45-60, 91-270, 450-510, 591-600)
- models/organization/org_user.go
- models/repo/org_repo.go
- services/org/user.go
- services/org/team.go (lines 276-340)
- services/convert/user.go
- services/convert/utils.go
- routers/api/v1/utils/page.go


---

## Session 12

# Phase 2 Session Report

**Session:** 12
**Endpoints Analyzed:** ep-077 to ep-083
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 12
- Database operations documented: 13
- External integrations used: 0
- Performance issues found: 1
- Average workflow depth: 2.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-077 | GET | /api/v1/orgs/{org}/hooks | 3 steps | 4 files | 0 |
| ep-078 | GET | /api/v1/orgs/{org}/hooks/{id} | 3 steps | 4 files | 0 |
| ep-079 | POST | /api/v1/orgs/{org}/hooks | 3 steps | 4 files | 0 |
| ep-080 | PATCH | /api/v1/orgs/{org}/hooks/{id} | 3 steps | 4 files | 1 |
| ep-081 | DELETE | /api/v1/orgs/{org}/hooks/{id} | 3 steps | 4 files | 0 |
| ep-082 | GET | /api/v1/orgs/{org}/labels | 2 steps | 3 files | 0 |
| ep-083 | POST | /api/v1/orgs/{org}/labels | 2 steps | 3 files | 0 |

## Performance Issues Found
- **ep-080 (low)**: Re-fetches webhook from DB after update instead of using in-memory object. Extra query per edit.

## Files Read
- routers/api/v1/org/hook.go
- routers/api/v1/org/label.go
- routers/api/v1/org/block.go
- routers/api/v1/utils/hook.go
- routers/api/v1/utils/page.go
- routers/api/v1/shared/block.go
- models/webhook/webhook.go
- models/issues/label.go
- models/user/block.go
- modules/structs/hook.go
- modules/structs/issue_label.go
- modules/label/label.go
- services/webhook/webhook.go
- services/webhook/general.go
- services/convert/issue.go
- services/convert/utils.go
- services/user/block.go


---

## Session 13

# Phase 2 Session Report

**Session:** 13
**Endpoints Analyzed:** ep-084 to ep-090
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 12
- Database operations documented: 28
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-084 | GET | /api/v1/orgs/{org}/labels/{id} | 3 steps | 4 files | 0 |
| ep-085 | PATCH | /api/v1/orgs/{org}/labels/{id} | 5 steps | 4 files | 1 |
| ep-086 | DELETE | /api/v1/orgs/{org}/labels/{id} | 2 steps | 3 files | 1 |
| ep-087 | GET | /api/v1/orgs/{org}/blocks | 5 steps | 4 files | 0 |
| ep-088 | GET | /api/v1/orgs/{org}/blocks/{username} | 4 steps | 4 files | 0 |
| ep-089 | PUT | /api/v1/orgs/{org}/blocks/{username} | 4 steps | 5 files | 2 |
| ep-090 | DELETE | /api/v1/orgs/{org}/blocks/{username} | 4 steps | 5 files | 0 |

## Performance Issues Found

1. **HIGH** (ep-089): N+1 queries in BlockUser - iterative unstar/unwatch/unassign loops generate many sequential DB operations per item
2. **MEDIUM** (ep-089): Long-running single transaction for block operation with many sequential writes
3. **MEDIUM** (ep-086): Potential missing index on comment.label_id for DELETE during label deletion

## Files Read
- routers/api/v1/org/label.go
- routers/api/v1/org/block.go
- routers/api/v1/shared/block.go
- models/user/block.go
- services/user/block.go
- models/issues/label.go
- services/convert/issue.go
- services/convert/utils.go
- modules/structs/issue_label.go
- modules/label/label.go
- routers/api/v1/utils/page.go


---

## Session 14

# Phase 2 Session Report

**Session:** 14
**Endpoints Analyzed:** ep-091 to ep-098
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 14
- Database operations documented: 18
- External integrations used: 1 (HaveIBeenPwned API)
- Performance issues found: 4
- Resiliency findings: 6
- Average workflow depth: 3.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-091 | GET | /api/v1/admin/hooks | 4 steps | 5 files | 1 |
| ep-092 | GET | /api/v1/admin/hooks/{id} | 3 steps | 4 files | 0 |
| ep-093 | POST | /api/v1/admin/hooks | 3 steps | 4 files | 0 |
| ep-094 | PATCH | /api/v1/admin/hooks/{id} | 3 steps | 4 files | 1 |
| ep-095 | DELETE | /api/v1/admin/hooks/{id} | 2 steps | 3 files | 0 |
| ep-096 | POST | /api/v1/admin/users/{username}/orgs | 3 steps | 4 files | 0 |
| ep-097 | GET | /api/v1/admin/orgs | 3 steps | 4 files | 1 |
| ep-098 | POST | /api/v1/admin/users | 6 steps | 7 files | 1 |

## Performance Issues Found
- **ep-098 (medium)**: HaveIBeenPwned API call uses http.DefaultClient with no timeout - can block indefinitely
- **ep-094 (low)**: Re-fetches webhook after update instead of returning mutated object
- **ep-091 (low)**: Loop decrypts auth headers for each webhook
- **ep-097 (low)**: No caching on org list (acceptable for admin endpoint)

## Key Findings
- All 8 endpoints are admin-only, reducing blast radius of any issues
- The HaveIBeenPwned integration is the only external dependency and lacks timeout/retry
- Organization creation is well-designed with full transactional integrity (7 operations in 1 tx)
- Webhook delete properly cascades to hook_task records in a transaction

## Files Read
- routers/api/v1/admin/hooks.go
- routers/api/v1/admin/org.go
- routers/api/v1/admin/user.go
- routers/api/v1/utils/hook.go
- routers/api/v1/utils/page.go
- models/webhook/webhook.go
- models/webhook/webhook_system.go
- models/organization/org.go
- models/user/user.go
- models/user/search.go
- modules/structs/hook.go
- modules/structs/admin_user.go
- modules/structs/org.go
- modules/auth/password/pwn.go
- modules/auth/password/pwn/pwn.go
- services/webhook/general.go
- services/convert/convert.go


---

## Session 15

# Phase 2 Session Report

**Session:** 15
**Endpoints Analyzed:** ep-099 to ep-105
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 14
- Database operations documented: 7 tables
- External integrations used: 1 (HaveIBeenPwned API)
- Performance issues found: 6
- Average workflow depth: 3.4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-099 | PATCH | /api/v1/admin/users/{username} | 5 steps | 5 files | 1 |
| ep-100 | DELETE | /api/v1/admin/users/{username} | 3 steps | 4 files | 3 |
| ep-101 | POST | /api/v1/admin/users/{username}/keys | 3 steps | 3 files | 0 |
| ep-102 | DELETE | /api/v1/admin/users/{username}/keys/{id} | 3 steps | 2 files | 1 |
| ep-103 | GET | /api/v1/admin/users | 3 steps | 3 files | 1 |
| ep-104 | POST | /api/v1/admin/users/{username}/rename | 2 steps | 3 files | 0 |
| ep-105 | GET | /api/v1/admin/actions/jobs | 3 steps | 3 files | 1 |

## Performance Issues Found
- **HIGH** ep-100: Branch protection cleanup iterates ALL protected branches (N+1 pattern)
- **MEDIUM** ep-100: Comment deletion in purge mode is one-by-one
- **MEDIUM** ep-100: Purge mode deletes repos synchronously (blocking)
- **MEDIUM** ep-099: No timeout on HaveIBeenPwned API call
- **MEDIUM** ep-102: authorized_keys full rewrite on every key deletion
- **MEDIUM** ep-105: LoadAttributes for jobs is N+1

## Files Read
- routers/api/v1/admin/user.go
- routers/api/v1/admin/action.go
- routers/api/v1/shared/action.go
- routers/api/v1/user/key.go
- routers/api/v1/utils/page.go
- services/user/update.go
- services/user/delete.go
- services/user/user.go
- services/user/email.go
- services/asymkey/ssh_key.go
- services/convert/user.go
- models/user/user.go
- models/user/search.go
- models/actions/run_job_list.go
- models/actions/run_list.go
- modules/structs/admin_user.go
- modules/structs/user.go


---

## Session 16

# Phase 2 Session Report

**Session:** 16
**Endpoints Analyzed:** ep-106 to ep-113
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 18
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 2.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-106 | GET | /api/v1/admin/actions/runs | 3 steps | 4 files | 1 |
| ep-107 | GET | /api/v1/admin/unadopted | 2 steps | 3 files | 2 |
| ep-108 | POST | /api/v1/admin/unadopted/{owner}/{repo} | 2 steps | 3 files | 0 |
| ep-109 | DELETE | /api/v1/admin/unadopted/{owner}/{repo} | 2 steps | 3 files | 0 |
| ep-110 | GET | /api/v1/admin/cron | 2 steps | 2 files | 0 |
| ep-111 | POST | /api/v1/admin/cron/{task} | 2 steps | 2 files | 0 |
| ep-112 | POST | /api/v1/admin/users/{username}/repos | 3 steps | 3 files | 0 |
| ep-113 | POST | /api/v1/admin/actions/runners/registration-token | 2 steps | 3 files | 0 |

## Performance Issues Found
1. **ep-106** (medium): N+1 queries for run attempts - TODO comment in code acknowledges this
2. **ep-107** (high): Synchronous filesystem walk of entire RepoRootPath with no timeout
3. **ep-107** (medium): N+1 DB queries per user directory during filesystem walk

## Files Read
- routers/api/v1/admin/action.go
- routers/api/v1/admin/adopt.go
- routers/api/v1/admin/cron.go
- routers/api/v1/admin/repo.go
- routers/api/v1/admin/runners.go
- routers/api/v1/shared/action.go
- routers/api/v1/shared/runners.go
- routers/api/v1/repo/repo.go
- routers/api/v1/api.go
- routers/api/v1/utils/page.go
- services/repository/adopt.go
- services/repository/create.go
- services/cron/cron.go
- services/cron/tasks.go
- services/convert/convert.go
- models/actions/run.go
- models/actions/run_list.go
- models/actions/run_job_list.go
- models/actions/runner.go
- models/actions/runner_token.go
- modules/structs/repo_actions.go
- modules/structs/cron.go
- modules/structs/repo.go


---

## Session 17

# Phase 2 Session Report

**Session:** 17
**Endpoints Analyzed:** ep-114 to ep-122
**Total Endpoints:** 9
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 9
- Business rules extracted: 10
- Database operations documented: 4 tables (action_runner, email_address, badge, user_badge)
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 2.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-114 | GET | /api/v1/admin/actions/runners | 3 steps | 5 files | 0 |
| ep-115 | GET | /api/v1/admin/actions/runners/{runner_id} | 3 steps | 5 files | 0 |
| ep-116 | DELETE | /api/v1/admin/actions/runners/{runner_id} | 2 steps | 5 files | 1 |
| ep-117 | PATCH | /api/v1/admin/actions/runners/{runner_id} | 2 steps | 5 files | 1 |
| ep-118 | GET | /api/v1/admin/emails | 2 steps | 4 files | 0 |
| ep-119 | GET | /api/v1/admin/emails/search | 2 steps | 4 files | 1 |
| ep-120 | GET | /api/v1/admin/users/{username}/badges | 2 steps | 4 files | 1 |
| ep-121 | POST | /api/v1/admin/users/{username}/badges | 3 steps | 4 files | 1 |
| ep-122 | DELETE | /api/v1/admin/users/{username}/badges | 3 steps | 4 files | 0 |

## Performance Issues Found

1. **ep-116 (low)**: DeleteRunner model re-fetches runner by ID redundantly
2. **ep-117 (low)**: UpdateRunner re-fetches runner after update instead of using in-memory object
3. **ep-119 (medium)**: Email search uses LIKE on lower(full_name) which may not use indexes
4. **ep-121 (medium)**: AddUserBadges has N+1 pattern - 3 queries per badge in a loop

## Files Read
- routers/api/v1/admin/runners.go
- routers/api/v1/admin/email.go
- routers/api/v1/admin/user_badge.go
- routers/api/v1/shared/runners.go
- routers/api/v1/utils/page.go
- models/actions/runner.go
- models/actions/runner_token.go
- models/actions/tasks_version.go
- models/user/email_address.go
- models/user/badge.go
- models/db/list.go
- modules/structs/repo_actions.go
- modules/structs/user.go
- modules/structs/user_email.go
- services/convert/convert.go
- services/context/user.go
- services/context/base_form.go
- routers/api/v1/api.go


---

## Session 18

# Phase 2 Session Report

**Session:** 18
**Endpoints Analyzed:** ep-123 to ep-128
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 12
- Database operations documented: 10
- External integrations used: 1 (Avatar Storage)
- Performance issues found: 5
- Average workflow depth: 3.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-123 | GET | /api/v1/users/search | 4 steps | 5 files | 1 |
| ep-124 | GET | /api/v1/users/{username} | 3 steps | 4 files | 0 |
| ep-125 | GET | /api/v1/user | 2 steps | 2 files | 0 |
| ep-126 | GET | /api/v1/users/{username}/heatmap | 3 steps | 3 files | 2 |
| ep-127 | GET | /api/v1/users/{username}/activities/feeds | 5 steps | 5 files | 2 |
| ep-128 | POST | /api/v1/user/avatar | 4 steps | 4 files | 1 |

## Performance Issues Found

| Severity | Endpoint | Issue | Recommendation |
|----------|----------|-------|----------------|
| high | ep-127 | N+1 queries in ToActivities (GetDoerRepoPermission per action) | Batch permission checks |
| medium | ep-126 | No caching on expensive heatmap aggregation query | Cache with 5-15 min TTL |
| medium | ep-127 | No caching on activity feeds | Cache with short TTL |
| medium | ep-123 | LIKE on LOWER(full_name) cannot use index | Add functional index |
| low | ep-126 | Missing composite index on action(user_id, created_unix) | Add composite index |

## Files Read
- routers/api/v1/user/user.go
- routers/api/v1/user/avatar.go
- models/user/search.go
- models/user/user.go (lines 1-200, 955-975, 1384-1470)
- models/activities/user_heatmap.go
- models/activities/action.go (lines 1-150, 425-570)
- models/activities/action_list.go (lines 180-310)
- services/feed/feed.go
- services/user/avatar.go
- services/convert/user.go
- services/convert/activity.go
- services/convert/utils.go
- services/context/user.go
- services/context/api.go (lines 30-50)
- modules/avatar/avatar.go
- modules/avatar/hash.go
- modules/structs/user.go (lines 1-120)
- modules/setting/api.go
- modules/storage/storage.go (search)
- routers/api/v1/utils/page.go


---

## Session 19

# Phase 2 Session Report

**Session:** 19
**Endpoints Analyzed:** ep-129 to ep-134
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 12
- External integrations used: 1 (Avatar Storage)
- Performance issues found: 0
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-129 | DELETE | /api/v1/user/avatar | 3 steps | 4 files | 0 |
| ep-130 | PUT | /api/v1/user/actions/secrets/{secretname} | 4 steps | 4 files | 0 |
| ep-131 | DELETE | /api/v1/user/actions/secrets/{secretname} | 2 steps | 3 files | 0 |
| ep-132 | POST | /api/v1/user/actions/variables/{variablename} | 4 steps | 4 files | 0 |
| ep-133 | PUT | /api/v1/user/actions/variables/{variablename} | 4 steps | 4 files | 0 |
| ep-134 | DELETE | /api/v1/user/actions/variables/{variablename} | 2 steps | 3 files | 0 |

## Performance Issues Found
No critical or high performance issues found. All endpoints perform minimal DB operations (2 per request) with proper indexed lookups via unique constraints.

## Key Observations
- All secret/variable endpoints share the same name validation logic (ValidateName)
- Secrets are encrypted at rest using setting.SecretKey
- Variables are stored in plaintext (not encrypted)
- Avatar deletion is transactional but has a minor inconsistency risk if storage delete fails after DB commit (mitigated by transaction rollback)
- Variable creation has a TOCTOU race condition (check-then-insert without transaction)

## Files Read
- routers/api/v1/user/avatar.go
- routers/api/v1/user/action.go
- services/user/avatar.go
- services/secrets/secrets.go
- services/secrets/validation.go
- services/actions/variables.go
- models/secret/secret.go
- models/actions/variable.go
- models/user/avatar.go
- models/user/user.go
- modules/structs/secret.go
- modules/structs/variable.go
- modules/storage/storage.go
- services/context/api.go


---

## Session 20

# Phase 2 Session Report

**Session:** 20
**Endpoints Analyzed:** ep-135 to ep-141
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 8
- Database operations documented: 10
- External integrations used: 0
- Performance issues found: 5
- Average workflow depth: 2.4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-135 | GET | /api/v1/user/actions/variables/{variablename} | 2 steps | 4 files | 0 |
| ep-136 | GET | /api/v1/user/actions/variables | 2 steps | 4 files | 0 |
| ep-137 | GET | /api/v1/user/actions/runs | 2 steps | 5 files | 1 |
| ep-138 | GET | /api/v1/user/actions/jobs | 2 steps | 5 files | 1 |
| ep-139 | GET | /api/v1/user/followers | 3 steps | 4 files | 1 |
| ep-140 | GET | /api/v1/users/{username}/followers | 3 steps | 5 files | 1 |
| ep-141 | GET | /api/v1/user/following | 3 steps | 4 files | 1 |

## Performance Issues Found
- ep-137 (medium): N+1 queries - run attempts loaded per-run in loop (TODO comment in code)
- ep-138 (medium): Potential N+1 in ToActionWorkflowJob conversion loop
- ep-139/140/141 (low): Visibility subqueries on team_user may be slow for large orgs

## Files Read
- routers/api/v1/user/action.go
- routers/api/v1/user/follower.go
- routers/api/v1/user/helper.go
- routers/api/v1/shared/action.go
- routers/api/v1/utils/page.go
- services/actions/variables.go
- services/secrets/validation.go
- services/convert/utils.go
- services/convert/user.go
- models/actions/variable.go
- models/actions/run_list.go
- models/actions/run_job_list.go
- models/user/follow.go
- models/user/user.go (lines 333-380, 1384-1420)


---

## Session 21

# Phase 2 Session Report

**Session:** 21
**Endpoints Analyzed:** ep-142 to ep-149
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 15
- External integrations used: 0
- Performance issues found: 2 (both low severity)
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-142 | GET | /api/v1/users/{username}/following | 4 steps | 5 files | 0 |
| ep-143 | GET | /api/v1/user/following/{username} | 3 steps | 3 files | 0 |
| ep-144 | GET | /api/v1/users/{username}/following/{target} | 2 steps | 4 files | 0 |
| ep-145 | PUT | /api/v1/user/following/{username} | 2 steps | 4 files | 1 |
| ep-146 | DELETE | /api/v1/user/following/{username} | 2 steps | 3 files | 0 |
| ep-147 | GET | /api/v1/user/hooks | 3 steps | 5 files | 1 |
| ep-148 | GET | /api/v1/user/hooks/{id} | 3 steps | 5 files | 0 |
| ep-149 | POST | /api/v1/user/hooks | 3 steps | 5 files | 0 |

## Performance Issues Found
- **ep-145** (low): TOCTOU race in IsFollowing pre-check before transaction (mitigated by UNIQUE constraint)
- **ep-147** (low): Synchronous decryption of authorization headers in loop for each webhook

## Files Read
- routers/api/v1/user/follower.go
- routers/api/v1/user/hook.go
- routers/api/v1/user/helper.go
- routers/api/v1/utils/hook.go
- routers/api/v1/utils/page.go
- models/user/follow.go
- models/user/user.go (lines 333-380)
- models/user/block.go (grep)
- models/webhook/webhook.go
- services/webhook/general.go (lines 394-427)
- services/webhook/webhook.go (lines 37-50)
- services/webhook/slack.go (line 326)
- services/convert/user.go (lines 1-80)
- services/convert/utils.go (lines 15-23)
- modules/structs/hook.go


---

## Session 22

# Phase 2 Session Report

**Session:** 22
**Endpoints Analyzed:** ep-150 to ep-155
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 2 (both N+1 queries)
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-150 | PATCH | /api/v1/user/hooks/{id} | 4 steps | 5 files | 0 |
| ep-151 | DELETE | /api/v1/user/hooks/{id} | 3 steps | 4 files | 0 |
| ep-152 | GET | /api/v1/users/{username}/starred | 3 steps | 5 files | 1 |
| ep-153 | GET | /api/v1/user/starred | 2 steps | 4 files | 1 |
| ep-154 | GET | /api/v1/user/starred/{owner}/{repo} | 1 step | 3 files | 0 |
| ep-155 | PUT | /api/v1/user/starred/{owner}/{repo} | 2 steps | 4 files | 0 |

## Performance Issues Found
- **HIGH** (ep-152, ep-153): N+1 query pattern in getStarredRepos - calls GetIndividualUserRepoPermission per repo in a loop, resulting in ~150+ queries per page. Recommend batch permission loading.

## Files Read
- routers/api/v1/user/hook.go
- routers/api/v1/utils/hook.go
- routers/api/v1/user/star.go
- routers/api/v1/utils/page.go
- routers/api/v1/api.go
- models/webhook/webhook.go
- models/repo/star.go
- models/repo/user_repo.go
- models/user/block.go
- models/perm/access/repo_permission.go
- services/webhook/general.go
- services/convert/repository.go
- modules/structs/hook.go


---

## Session 23

# Phase 2 Session Report

**Session:** 23
**Endpoints Analyzed:** ep-156 to ep-161
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-156 | DELETE | /api/v1/user/starred/{owner}/{repo} | 2 steps | 2 files | 0 |
| ep-157 | GET | /api/v1/user/keys | 3 steps | 4 files | 1 |
| ep-158 | GET | /api/v1/users/{username}/keys | 3 steps | 4 files | 0 |
| ep-159 | GET | /api/v1/user/keys/{id} | 2 steps | 4 files | 0 |
| ep-160 | POST | /api/v1/user/keys | 4 steps | 6 files | 1 |
| ep-161 | DELETE | /api/v1/user/keys/{id} | 4 steps | 5 files | 1 |

## Performance Issues Found
- **ep-161 (HIGH)**: RewriteAllPublicKeys rewrites entire authorized_keys file from all keys in DB after every single key deletion. Full table scan + file rewrite with global lock.
- **ep-160 (MEDIUM)**: appendAuthorizedKeysToFile performs synchronous filesystem I/O during request.
- **ep-157 (MEDIUM)**: Potential N+1 for appendPrivateInformation, but minimal impact since keys belong to same user.

## Files Read
- routers/api/v1/user/star.go
- routers/api/v1/user/key.go
- models/repo/star.go
- models/asymkey/ssh_key.go
- models/asymkey/ssh_key_parse.go
- models/asymkey/error.go
- services/asymkey/ssh_key.go
- services/asymkey/ssh_key_authorized_keys.go
- services/convert/convert.go
- modules/structs/user_key.go
- modules/structs/repo_key.go
- modules/setting/admin.go
- routers/api/v1/repo/key.go
- models/user/user.go


---

## Session 24

# Phase 2 Session Report

**Session:** 24
**Endpoints Analyzed:** ep-162 to ep-167
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 9
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-162 | GET | /api/v1/user/settings | 2 steps | 3 files | 0 |
| ep-163 | PATCH | /api/v1/user/settings | 4 steps | 4 files | 0 |
| ep-164 | GET | /api/v1/users/{username}/tokens | 2 steps | 3 files | 0 |
| ep-165 | POST | /api/v1/users/{username}/tokens | 4 steps | 4 files | 0 |
| ep-166 | DELETE | /api/v1/users/{username}/tokens/{token} | 3 steps | 3 files | 1 |
| ep-167 | POST | /api/v1/user/applications/oauth2 | 5 steps | 5 files | 1 |

## Performance Issues Found
- ep-166 (low): Token name column not indexed for name-based deletion lookups
- ep-167 (medium): bcrypt hashing is CPU-intensive (~100ms) but acceptable for low-frequency OAuth2 app creation

## Key Findings
- ep-162 is zero-cost (pure in-memory read from already-loaded user)
- Token management endpoints (ep-164/165/166) require basic auth or reverse proxy auth, not just token auth
- ep-167 has a non-atomic pattern: INSERT app then UPDATE secret are separate operations
- OAuth2 app creation doesn't check for duplicate names (unlike access tokens)

## Files Read
- routers/api/v1/user/settings.go
- routers/api/v1/user/app.go
- routers/api/v1/api.go (lines 975-1090)
- services/convert/user.go
- services/convert/convert.go (lines 825-845)
- services/user/update.go
- services/forms/user_form.go (lines 368-395)
- models/auth/access_token.go
- models/auth/access_token_scope.go
- models/auth/oauth2.go
- models/auth/oauth2_list.go
- models/user/user.go (lines 956-975)
- modules/structs/user.go (lines 72-110)
- modules/structs/user_app.go


---

## Session 25

# Phase 2 Session Report

**Session:** 25
**Endpoints Analyzed:** ep-168 to ep-175
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 2.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-168 | GET | /api/v1/user/applications/oauth2 | 2 steps | 4 files | 0 |
| ep-169 | DELETE | /api/v1/user/applications/oauth2/{id} | 2 steps | 3 files | 0 |
| ep-170 | GET | /api/v1/user/applications/oauth2/{id} | 2 steps | 3 files | 0 |
| ep-171 | PATCH | /api/v1/user/applications/oauth2/{id} | 3 steps | 4 files | 1 |
| ep-172 | GET | /api/v1/users/{username}/repos | 4 steps | 4 files | 1 |
| ep-173 | GET | /api/v1/user/repos | 3 steps | 4 files | 1 |
| ep-174 | GET | /api/v1/orgs/{org}/repos | 2 steps | 3 files | 1 |
| ep-175 | POST | /api/v1/user/actions/runners/registration-token | 2 steps | 3 files | 0 |

## Performance Issues Found
- **HIGH** (ep-172, ep-173, ep-174): N+1 queries - GetDoerRepoPermission called in loop for each repo. For 50 repos = 50+ extra DB queries per request.
- **LOW** (ep-171): bcrypt computation (~100ms) blocks request thread during secret generation.

## Files Read
- routers/api/v1/user/app.go
- routers/api/v1/user/repo.go
- routers/api/v1/user/runners.go
- routers/api/v1/shared/runners.go
- routers/api/v1/user/email.go
- models/auth/oauth2.go
- models/auth/oauth2_list.go
- models/user/email_address.go
- models/actions/runner_token.go
- models/actions/runner.go
- models/repo/repo_list.go
- services/convert/convert.go
- services/forms/user_form.go
- services/user/email.go
- modules/structs/user_app.go
- modules/structs/user_email.go
- modules/structs/repo_actions.go


---

## Session 26

# Phase 2 Session Report

**Session:** 26
**Endpoints Analyzed:** ep-176 to ep-183
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 15
- External integrations used: 0
- Performance issues found: 4
- Resiliency findings: 8
- Average workflow depth: 2.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-176 | GET | /api/v1/user/actions/runners | 3 steps | 4 files | 0 |
| ep-177 | GET | /api/v1/user/actions/runners/{runner_id} | 3 steps | 4 files | 0 |
| ep-178 | DELETE | /api/v1/user/actions/runners/{runner_id} | 2 steps | 4 files | 1 |
| ep-179 | PATCH | /api/v1/user/actions/runners/{runner_id} | 3 steps | 5 files | 0 |
| ep-180 | GET | /api/v1/user/emails | 2 steps | 3 files | 1 |
| ep-181 | POST | /api/v1/user/emails | 3 steps | 4 files | 1 |
| ep-182 | DELETE | /api/v1/user/emails | 2 steps | 3 files | 1 |
| ep-183 | GET | /api/v1/users/{username}/gpg_keys | 3 steps | 4 files | 0 |

## Performance Issues Found
- **ep-178** (low): Redundant GetRunnerByID call in DeleteRunner model function
- **ep-180** (low): No pagination on email listing (minimal practical impact)
- **ep-181** (medium): N+1 queries pattern - each email triggers separate SELECT + INSERT
- **ep-182** (medium): N+1 queries pattern - each email triggers separate SELECT + DELETE

## Resiliency Findings
- **ep-181** (medium): Non-atomic multi-email insertion - partial failure leaves inconsistent state
- **ep-182** (medium): Non-atomic multi-email deletion - partial failure leaves inconsistent state

## Files Read
- routers/api/v1/user/runners.go
- routers/api/v1/shared/runners.go
- models/actions/runner.go
- models/actions/runner_token.go
- models/actions/tasks_version.go
- services/convert/convert.go
- modules/structs/repo_actions.go
- routers/api/v1/user/email.go
- models/user/email_address.go
- services/user/email.go
- modules/structs/user_email.go
- routers/api/v1/user/gpg_key.go
- models/asymkey/gpg_key.go
- models/asymkey/gpg_key_list.go
- modules/structs/user_gpgkey.go
- routers/api/v1/utils/page.go
- modules/setting/service.go


---

## Session 27

# Phase 2 Session Report

**Session:** 27
**Endpoints Analyzed:** ep-184 to ep-189
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 2 (both low severity)
- Average workflow depth: 2.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-184 | GET | /api/v1/user/gpg_keys | 2 steps | 5 files | 0 |
| ep-185 | GET | /api/v1/user/gpg_keys/{id} | 1 step | 5 files | 0 |
| ep-186 | GET | /api/v1/user/gpg_key_token | 2 steps | 3 files | 0 |
| ep-187 | POST | /api/v1/user/gpg_key_verify | 3 steps | 5 files | 1 |
| ep-188 | POST | /api/v1/user/gpg_keys | 3 steps | 6 files | 1 |
| ep-189 | DELETE | /api/v1/user/gpg_keys/{id} | 2 steps | 5 files | 0 |

## Performance Issues Found
- ep-187 (low): CPU-intensive crypto verification runs synchronously with up to 3 retry variants
- ep-188 (low): OpenPGP key parsing is CPU-intensive but acceptable for infrequent operation

## Key Findings
- GPG key endpoints are well-structured with proper transactional safety
- Batch loading of subkeys (GPGKeyList.LoadSubKeys) avoids N+1 for list endpoint
- Verification token is time-based with 1-minute granularity, supports current + previous minute
- Feature flag system allows disabling GPG key management per user login type
- Delete operation is idempotent (returns success if key doesn't exist)

## Files Read
- routers/api/v1/user/gpg_key.go
- models/asymkey/gpg_key.go
- models/asymkey/gpg_key_add.go
- models/asymkey/gpg_key_verify.go
- models/asymkey/gpg_key_list.go
- models/asymkey/gpg_key_import.go
- models/asymkey/error.go
- modules/structs/user_gpgkey.go
- services/convert/convert.go (lines 632-680)
- routers/api/v1/utils/page.go
- models/user/user.go (lines 1480-1498)
- modules/setting/admin.go


---

## Session 28

# Phase 2 Session Report

**Session:** 28
**Endpoints Analyzed:** ep-190 to ep-195
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 23
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-190 | GET | /api/v1/user/blocks | 3 steps | 4 files | 0 |
| ep-191 | GET | /api/v1/user/blocks/{username} | 2 steps | 4 files | 0 |
| ep-192 | PUT | /api/v1/user/blocks/{username} | 3 steps | 5 files | 2 |
| ep-193 | DELETE | /api/v1/user/blocks/{username} | 3 steps | 5 files | 0 |
| ep-194 | GET | /api/v1/users/{username}/subscriptions | 3 steps | 5 files | 1 |
| ep-195 | GET | /api/v1/user/subscriptions | 3 steps | 5 files | 1 |

## Performance Issues Found
- **ep-192 (HIGH)**: BlockUser performs paginated per-item loops for cleanup (unstar, unwatch, unassign, remove collaborations) generating potentially hundreds of queries in a single transaction
- **ep-192 (MEDIUM)**: All cleanup operations run synchronously in one transaction, risking timeouts
- **ep-194 (HIGH)**: N+1 query pattern - GetIndividualUserRepoPermission called per repo (~90 extra queries for page of 30)
- **ep-195 (HIGH)**: Same N+1 pattern as ep-194

## Files Read
- routers/api/v1/user/block.go
- routers/api/v1/shared/block.go
- models/user/block.go
- services/user/block.go
- routers/api/v1/user/watch.go
- models/repo/watch.go
- models/repo/user_repo.go (lines 55-100)
- models/perm/access/repo_permission.go (lines 394-430)
- routers/api/v1/utils/page.go
- services/convert/utils.go (lines 15-30)


---

## Session 29

# Phase 2 Session Report

**Session:** 29
**Endpoints Analyzed:** ep-196 to ep-201
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 24
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-196 | GET | /api/v1/repos/{owner}/{repo}/subscription | 2 steps | 3 files | 0 |
| ep-197 | PUT | /api/v1/repos/{owner}/{repo}/subscription | 2 steps | 4 files | 0 |
| ep-198 | DELETE | /api/v1/repos/{owner}/{repo}/subscription | 2 steps | 3 files | 0 |
| ep-199 | GET | /api/v1/packages/{owner} | 5 steps | 6 files | 1 |
| ep-200 | GET | /api/v1/packages/{owner}/{type}/{name}/{version} | 3 steps | 5 files | 0 |
| ep-201 | DELETE | /api/v1/packages/{owner}/{type}/{name} | 3 steps | 6 files | 1 |

## Performance Issues Found
- **ep-199 (medium)**: N+1 queries in GetPackageDescriptors - iterates versions individually for properties/files. Mitigated by EphemeralCache but still multiple round-trips.
- **ep-201 (medium)**: GetAllPackageDescriptors loads full descriptors for all versions before deletion, though only minimal info needed for notifications.

## Files Read
- routers/api/v1/user/watch.go
- routers/api/v1/packages/package.go
- models/repo/watch.go
- models/repo/user_repo.go
- models/packages/package.go
- models/packages/package_version.go
- models/packages/package_file.go
- models/packages/descriptor.go
- models/user/block.go
- services/packages/packages.go
- services/packages/package_update.go
- services/packages/spec.go
- services/convert/package.go
- services/context/package.go
- modules/structs/repo_watch.go
- modules/structs/package.go


---

## Session 30

# Phase 2 Session Report

**Session:** 30
**Endpoints Analyzed:** ep-202 to ep-207
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 28
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-202 | DELETE | /api/v1/packages/{owner}/{type}/{name}/{version} | 3 steps | 8 files | 1 |
| ep-203 | GET | /api/v1/packages/{owner}/{type}/{name}/{version}/files | 2 steps | 8 files | 1 |
| ep-204 | GET | /api/v1/packages/{owner}/{type}/{name} | 3 steps | 8 files | 1 |
| ep-205 | GET | /api/v1/packages/{owner}/{type}/{name}/-/latest | 2 steps | 8 files | 0 |
| ep-206 | POST | /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name} | 3 steps | 9 files | 0 |
| ep-207 | POST | /api/v1/packages/{owner}/{type}/{name}/-/unlink | 3 steps | 9 files | 0 |

## Performance Issues Found
- **HIGH** (ep-204): N+1 queries in GetPackageDescriptors - each version loads full descriptor individually
- **MEDIUM** (ep-202, ep-203): N+1 queries in PackageDescriptor file blob loading - each file's blob loaded individually

## Files Read
- routers/api/v1/packages/package.go
- routers/api/v1/api.go
- services/packages/packages.go
- services/packages/package_update.go
- services/context/package.go
- services/convert/package.go
- models/packages/package.go
- models/packages/package_version.go
- models/packages/package_file.go
- models/packages/package_blob.go
- models/packages/descriptor.go
- modules/structs/package.go
- modules/setting/packages.go


---

## Session 31

# Phase 2 Session Report

**Session:** 31
**Endpoints Analyzed:** ep-208 to ep-213
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 6 endpoint operation sets
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 6 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-208 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | 6 steps | 6 files | 1 |
| ep-209 | POST | /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | 7 steps | 6 files | 0 |
| ep-210 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | 6 steps | 6 files | 0 |
| ep-211 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | 5 steps | 6 files | 2 |
| ep-212 | POST | /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | 6 steps | 6 files | 0 |
| ep-213 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | 6 steps | 6 files | 0 |

## Performance Issues Found

1. **HIGH - ep-211**: `BlockingDependencies()` fetches ALL blocked issues without DB-level pagination. Manual pagination is applied after loading all results into memory. Fix: Add ListOptions parameter with LIMIT/OFFSET.
2. **MEDIUM - ep-208**: N+1 permission queries for each unique repo in dependency list (mitigated by in-memory cache per request).
3. **MEDIUM - ep-211**: Same N+1 permission pattern as ep-208.

## Files Read
- routers/api/v1/repo/issue_dependency.go
- models/issues/dependency.go
- models/issues/issue.go (lines 647-720)
- models/issues/comment.go (lines 964-1000)
- models/repo/issue.go (lines 51-60)
- modules/structs/issue.go (lines 275-283)
- routers/api/v1/utils/page.go
- services/convert/utils.go
- services/convert/issue.go (lines 32-165)
- models/perm/access/repo_permission.go (lines 384-400)
- modules/setting/service.go (lines 76-77, 212-213)


---

## Session 32

# Phase 2 Session Report

**Session:** 32
**Endpoints Analyzed:** ep-214 to ep-219
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 12
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-214 | GET | /api/v1/repos/{owner}/{repo}/git/commits/{sha} | 4 steps | 4 files | 1 |
| ep-215 | GET | /api/v1/repos/{owner}/{repo}/commits | 5 steps | 5 files | 2 |
| ep-216 | GET | /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType} | 2 steps | 3 files | 1 |
| ep-217 | GET | /api/v1/repos/{owner}/{repo}/commits/{sha}/pull | 3 steps | 3 files | 1 |
| ep-218 | PUT | /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | 2 steps | 3 files | 0 |
| ep-219 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | 2 steps | 3 files | 0 |

## Performance Issues Found
- **HIGH** ep-215: N+1 git subprocess calls - each commit triggers separate file status and diff stat operations (up to 100 git calls per request)
- **MEDIUM** ep-215: No caching for git rev-list --count on large repos
- **MEDIUM** ep-216: Unbounded diff streaming with no size limit
- **MEDIUM** ep-217: Missing index on pull_request(base_repo_id, merged_commit_id)

## Files Read
- routers/api/v1/repo/commits.go
- routers/api/v1/repo/issue_subscription.go
- routers/api/v1/repo/download.go
- services/convert/git_commit.go
- models/issues/issue_watch.go
- models/issues/pull.go
- models/issues/issue.go
- modules/git/diff.go
- modules/git/ref.go
- modules/gitrepo/commit.go
- routers/api/v1/utils/page.go


---

## Session 33

# Phase 2 Session Report

**Session:** 33
**Endpoints Analyzed:** ep-220 to ep-225
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 24
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 4.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-220 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check | 3 steps | 3 files | 0 |
| ep-221 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions | 6 steps | 3 files | 1 |
| ep-222 | GET | /api/v1/repos/{owner}/{repo}/pulls | 4 steps | 5 files | 2 |
| ep-223 | GET | /api/v1/repos/{owner}/{repo}/pulls/{index} | 5 steps | 4 files | 1 |
| ep-224 | GET | /api/v1/repos/{owner}/{repo}/pulls/{base}/{head} | 5 steps | 4 files | 0 |
| ep-225 | GET | /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType} | 3 steps | 3 files | 1 |

## Performance Issues Found
- **ep-222 (HIGH)**: N+1 pattern in ToAPIPullRequests - branch SHA lookups per PR (partially mitigated by baseBranchCache)
- **ep-222 (MEDIUM)**: No caching for expensive multi-query PR list conversion
- **ep-221 (MEDIUM)**: Redundant user fetch after JOIN already touches user table
- **ep-225 (MEDIUM)**: Unbounded diff output with no size limit

## Files Read
- routers/api/v1/repo/issue_subscription.go
- routers/api/v1/repo/pull.go
- models/issues/issue_watch.go
- models/issues/pull.go
- models/issues/pull_list.go
- services/pull/patch.go
- services/pull/check.go
- services/convert/pull.go
- modules/structs/pull.go
- modules/structs/repo_watch.go
- routers/api/v1/utils/page.go
- services/pull/pull.go


---

## Session 34

# Phase 2 Session Report

**Session:** 34
**Endpoints Analyzed:** ep-226 to ep-233
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 14
- Database operations documented: 7 tables
- External integrations used: 0
- Performance issues found: 5
- Average workflow depth: 5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-226 | POST | /api/v1/repos/{owner}/{repo}/pulls | 9 steps | 8 files | 1 |
| ep-227 | PATCH | /api/v1/repos/{owner}/{repo}/pulls/{index} | 9 steps | 6 files | 1 |
| ep-228 | GET | /api/v1/repos/{owner}/{repo}/pulls/{index}/merge | 1 step | 2 files | 0 |
| ep-229 | POST | /api/v1/repos/{owner}/{repo}/pulls/{index}/merge | 7 steps | 8 files | 1 |
| ep-230 | POST | /api/v1/repos/{owner}/{repo}/pulls/{index}/update | 3 steps | 4 files | 1 |
| ep-231 | DELETE | /api/v1/repos/{owner}/{repo}/pulls/{index}/merge | 3 steps | 4 files | 0 |
| ep-232 | GET | /api/v1/repos/{owner}/{repo}/pulls/{index}/commits | 3 steps | 4 files | 1 |
| ep-233 | GET | /api/v1/repos/{owner}/{repo}/pulls/{index}/files | 5 steps | 5 files | 1 |

## Performance Issues Found
- **ep-233 (HIGH)**: GetPullRequestFiles loads ALL diff files into memory before pagination (MaxFiles=-1)
- **ep-232 (MEDIUM)**: All commits loaded into memory before pagination applied
- **ep-227 (MEDIUM)**: Multiple mutations not wrapped in transaction (partial failure risk)
- **ep-226 (MEDIUM)**: N+1 queries for assignee validation

## Files Read
- routers/api/v1/repo/pull.go
- modules/structs/pull.go
- services/forms/repo_form.go
- services/pull/pull.go
- services/pull/check.go
- services/pull/merge.go
- services/pull/update.go
- services/automerge/automerge.go
- services/convert/pull.go
- services/convert/convert.go
- services/git/compare.go
- models/issues/pull.go
- models/pull/automerge.go
- services/gitdiff/gitdiff.go


---

## Session 35

# Phase 2 Session Report

**Session:** 35
**Endpoints Analyzed:** ep-234 to ep-239
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 9
- External integrations used: 1 (Git Remote for push mirror sync)
- Performance issues found: 4
- Resiliency findings: 8
- Average workflow depth: 2.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-234 | POST | /api/v1/repos/{owner}/{repo}/mirror-sync | 2 steps | 5 files | 0 |
| ep-235 | POST | /api/v1/repos/{owner}/{repo}/push_mirrors-sync | 2 steps | 5 files | 2 |
| ep-236 | GET | /api/v1/repos/{owner}/{repo}/push_mirrors | 2 steps | 5 files | 1 |
| ep-237 | GET | /api/v1/repos/{owner}/{repo}/push_mirrors/{name} | 2 steps | 5 files | 0 |
| ep-238 | POST | /api/v1/repos/{owner}/{repo}/push_mirrors | 4 steps | 7 files | 1 |
| ep-239 | DELETE | /api/v1/repos/{owner}/{repo}/push_mirrors/{name} | 1 step | 4 files | 1 |

## Performance Issues Found
- **HIGH** (ep-235): Synchronous blocking - push mirror sync blocks HTTP request for each mirror's git push
- **MEDIUM** (ep-235): N+1 queries - re-fetches push mirror by ID even though already loaded
- **MEDIUM** (ep-238): No timeout on DNS lookup during URL validation
- **MEDIUM** (ep-239): Delete does not clean up git remote config, leaving orphaned state

## Files Read
- routers/api/v1/repo/mirror.go
- routers/api/v1/api.go (lines 1325-1340)
- models/repo/pushmirror.go
- models/repo/mirror.go
- services/mirror/mirror.go
- services/mirror/queue.go
- services/mirror/mirror_push.go
- services/convert/mirror.go
- services/convert/utils.go
- modules/structs/mirror.go
- modules/setting/mirror.go
- modules/git/remote.go (lines 84-130)
- services/migrations/migrate.go (lines 43-108)
- routers/api/v1/utils/page.go


---

## Session 36

# Phase 2 Session Report

**Session:** 36
**Endpoints Analyzed:** ep-240 to ep-245
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 6 endpoints × multiple ops
- External integrations used: 1 (Git repository filesystem)
- Performance issues found: 2
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-240 | GET | /api/v1/repos/{owner}/{repo}/releases/{id} | 4 steps | 6 files | 0 |
| ep-241 | GET | /api/v1/repos/{owner}/{repo}/releases/latest | 3 steps | 6 files | 0 |
| ep-242 | GET | /api/v1/repos/{owner}/{repo}/releases | 5 steps | 6 files | 1 |
| ep-243 | POST | /api/v1/repos/{owner}/{repo}/releases | 4 steps | 7 files | 0 |
| ep-244 | PATCH | /api/v1/repos/{owner}/{repo}/releases/{id} | 4 steps | 7 files | 0 |
| ep-245 | DELETE | /api/v1/repos/{owner}/{repo}/releases/{id} | 2 steps | 7 files | 1 |

## Performance Issues Found
1. **ep-242 (medium)**: N+1 query pattern in ListReleases - LoadAttributes called per release in loop. Recommendation: batch load attachments and publishers.
2. **ep-245 (low)**: Synchronous storage file deletion in request path. Recommendation: async deletion via background queue.

## Files Read
- routers/api/v1/repo/release.go
- models/repo/release.go
- services/release/release.go
- services/convert/release.go
- modules/structs/release.go
- models/repo/attachment.go
- routers/api/v1/utils/page.go
- services/convert/utils.go
- models/git/protected_tag.go


---

## Session 37

# Phase 2 Session Report

**Session:** 37
**Endpoints Analyzed:** ep-246 to ep-253
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 22
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 2.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-246 | GET | /api/v1/repos/{owner}/{repo}/git/trees/{sha} | 2 steps | 3 files | 1 |
| ep-247 | GET | /api/v1/repos/{owner}/{repo}/git/refs | 3 steps | 2 files | 1 |
| ep-248 | GET | /api/v1/repos/{owner}/{repo}/git/refs/{ref} | 3 steps | 2 files | 0 |
| ep-249 | POST | /api/v1/repos/{owner}/{repo}/diffpatch | 3 steps | 4 files | 1 |
| ep-250 | GET | /api/v1/repos/{owner}/{repo}/collaborators | 1 step | 2 files | 0 |
| ep-251 | GET | /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | 1 step | 2 files | 0 |
| ep-252 | PUT | /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | 2 steps | 3 files | 0 |
| ep-253 | DELETE | /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | 2 steps | 3 files | 1 |

## Performance Issues Found
- **ep-246** (medium): Recursive tree listing loads all entries into memory before pagination
- **ep-247** (medium): All refs returned without pagination support
- **ep-249** (medium): No explicit timeout on git apply/push operations
- **ep-253** (low): Cascading deletes in transaction could be slow for heavily-assigned users

## Files Read
- routers/api/v1/repo/tree.go
- routers/api/v1/repo/git_ref.go
- routers/api/v1/repo/patch.go
- routers/api/v1/repo/collaborators.go
- routers/api/v1/repo/file.go
- routers/api/v1/utils/git.go
- services/repository/files/tree.go
- services/repository/files/patch.go
- services/repository/collaboration.go
- services/pull/reviewer.go
- services/issue/review_request.go
- services/convert/user.go
- models/repo/collaboration.go
- models/repo/user_repo.go
- models/perm/access/repo_permission.go
- modules/structs/repo_file.go
- modules/structs/repo_refs.go
- modules/structs/repo_tree.go
- modules/structs/repo_collaborator.go
- modules/setting/api.go


---

## Session 38

# Phase 2 Session Report

**Session:** 38
**Endpoints Analyzed:** ep-254 to ep-261
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 6 tables
- External integrations used: 1 (Object Storage)
- Performance issues found: 4
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-254 | GET | /repos/{owner}/{repo}/collaborators/{collaborator}/permission | 4 steps | 4 files | 1 |
| ep-255 | GET | /repos/{owner}/{repo}/reviewers | 4 steps | 3 files | 1 |
| ep-256 | GET | /repos/{owner}/{repo}/assignees | 3 steps | 2 files | 0 |
| ep-257 | GET | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 5 steps | 3 files | 0 |
| ep-258 | GET | /repos/{owner}/{repo}/issues/{index}/assets | 4 steps | 4 files | 1 |
| ep-259 | POST | /repos/{owner}/{repo}/issues/{index}/assets | 5 steps | 5 files | 1 |
| ep-260 | PATCH | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 3 steps | 4 files | 0 |
| ep-261 | DELETE | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 3 steps | 3 files | 0 |

## Performance Issues Found

1. **HIGH - ep-258**: ListIssueAttachments calls issue.LoadAttributes which loads ALL issue data (comments, labels, milestones, reactions) just to extract attachments. Should use LoadAttachments directly.
2. **MEDIUM - ep-254**: GetIndividualUserRepoPermission executes 4-6 DB queries per call with no caching.
3. **MEDIUM - ep-255**: CanDoerChangeReviewRequests iterates over teams calling IsTeamMember per team (N+1 pattern).
4. **LOW - ep-259**: ChangeContent called with unchanged content just to trigger notifications, adding 2 unnecessary DB queries.

## Files Read
- routers/api/v1/repo/collaborators.go
- routers/api/v1/repo/issue_attachment.go
- models/perm/access/repo_permission.go
- models/repo/attachment.go
- models/repo/user_repo.go
- models/issues/issue.go
- services/pull/reviewer.go
- services/issue/review_request.go
- services/issue/content.go
- services/attachment/attachment.go
- services/convert/attachment.go
- services/convert/user.go
- services/convert/issue.go
- services/context/upload/upload.go
- modules/setting/attachment.go
- modules/structs/attachment.go
- modules/structs/repo_collaborator.go


---

## Session 39

# Phase 2 Session Report

**Session:** 39
**Endpoints Analyzed:** ep-262 to ep-268
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 10
- Database operations documented: 12
- External integrations used: 1 (File Storage)
- Performance issues found: 1 (medium severity)
- Average workflow depth: 2.3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-262 | POST | /api/v1/repos/{owner}/{repo}/avatar | 4 steps | 5 files | 1 |
| ep-263 | DELETE | /api/v1/repos/{owner}/{repo}/avatar | 2 steps | 3 files | 0 |
| ep-264 | GET | /api/v1/repos/{owner}/{repo}/actions/secrets | 1 step | 3 files | 0 |
| ep-265 | PUT | /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname} | 3 steps | 4 files | 0 |
| ep-266 | DELETE | /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname} | 2 steps | 3 files | 0 |
| ep-267 | GET | /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | 2 steps | 3 files | 0 |
| ep-268 | DELETE | /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | 2 steps | 3 files | 0 |

## Performance Issues Found
- **ep-262 (medium)**: Synchronous image processing on request thread - acceptable given max dimension caps and infrequent usage

## Files Read
- routers/api/v1/repo/avatar.go
- routers/api/v1/repo/action.go
- services/repository/avatar.go
- services/secrets/secrets.go
- services/secrets/validation.go
- services/actions/variables.go
- models/secret/secret.go
- models/actions/variable.go
- modules/avatar/avatar.go
- modules/avatar/hash.go
- modules/structs/secret.go
- modules/structs/variable.go
- modules/structs/repo.go
- routers/api/v1/utils/page.go
- services/convert/utils.go
- models/repo/avatar.go
- models/repo/update.go


---

## Session 40

# Phase 2 Session Report

**Session:** 40
**Endpoints Analyzed:** ep-269 to ep-276
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 3 (all low severity)
- Average workflow depth: 2 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-269 | POST | /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | 3 steps | 4 files | 0 |
| ep-270 | PUT | /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | 3 steps | 4 files | 0 |
| ep-271 | GET | /api/v1/repos/{owner}/{repo}/actions/variables | 1 step | 3 files | 0 |
| ep-272 | POST | /api/v1/repos/{owner}/{repo}/actions/runners/registration-token | 2 steps | 3 files | 0 |
| ep-273 | GET | /api/v1/repos/{owner}/{repo}/actions/runners | 2 steps | 3 files | 1 |
| ep-274 | GET | /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | 2 steps | 3 files | 0 |
| ep-275 | DELETE | /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | 2 steps | 3 files | 1 |
| ep-276 | PATCH | /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | 2 steps | 4 files | 1 |

## Performance Issues Found
- ep-273 (low): No caching on runner list query - acceptable for typical scale
- ep-275 (low): Redundant re-fetch of runner before delete - minimal impact
- ep-276 (low): Re-fetches runner after update for response - could return in-memory object

## Files Read
- routers/api/v1/repo/action.go
- routers/api/v1/shared/runners.go
- routers/api/v1/shared/action.go
- services/actions/variables.go
- models/actions/variable.go
- models/actions/runner.go
- models/actions/runner_token.go
- services/secrets/validation.go
- modules/structs/variable.go
- modules/structs/repo_actions.go
- services/convert/convert.go


---

## Session 41

# Phase 2 Session Report

**Session:** 41
**Endpoints Analyzed:** ep-277 to ep-284
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 18
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 2.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-277 | GET | /api/v1/repos/{owner}/{repo}/actions/jobs | 2 steps | 5 files | 1 |
| ep-278 | GET | /api/v1/repos/{owner}/{repo}/actions/runs | 2 steps | 5 files | 1 |
| ep-279 | GET | /api/v1/repos/{owner}/{repo}/actions/tasks | 1 step | 4 files | 1 |
| ep-280 | GET | /api/v1/repos/{owner}/{repo}/actions/workflows | 3 steps | 4 files | 1 |
| ep-281 | GET | /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id} | 2 steps | 4 files | 0 |
| ep-282 | PUT | /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | 2 steps | 3 files | 0 |
| ep-283 | POST | /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | 2 steps | 5 files | 0 |
| ep-284 | PUT | /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | 2 steps | 3 files | 0 |

## Performance Issues Found
- **ep-277 (HIGH)**: N+1 queries loading task/steps/runner per job in ToActionWorkflowJob
- **ep-278 (MEDIUM)**: N+1 queries loading latest attempt per run in ToActionWorkflowRun
- **ep-279 (MEDIUM)**: N+1 queries loading job->run->repo chain per task
- **ep-280 (MEDIUM)**: Sequential git blob reads per workflow file to parse name

## Files Read
- routers/api/v1/repo/action.go
- routers/api/v1/shared/action.go
- services/actions/workflow.go
- services/actions/rerun.go
- services/convert/convert.go
- models/actions/run.go
- models/actions/run_job.go
- models/actions/run_list.go
- models/actions/run_job_list.go
- models/actions/task.go
- models/actions/task_list.go
- modules/actions/workflows.go


---

## Session 42

# Phase 2 Session Report

**Session:** 42
**Endpoints Analyzed:** ep-285 to ep-292
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 5 tables
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-285 | GET | /api/v1/repos/{owner}/{repo}/actions/runs/{run} | 2 steps | 6 files | 0 |
| ep-286 | GET | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt} | 3 steps | 6 files | 0 |
| ep-287 | POST | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun | 3 steps | 7 files | 1 |
| ep-288 | POST | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs | 3 steps | 7 files | 0 |
| ep-289 | POST | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun | 5 steps | 7 files | 0 |
| ep-290 | GET | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs | 2 steps | 6 files | 1 |
| ep-291 | GET | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs | 2 steps | 6 files | 1 |
| ep-292 | GET | /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id} | 2 steps | 6 files | 0 |

## Performance Issues Found
- **ep-290, ep-291 (medium)**: N+1 queries in ToActionWorkflowJob - task and steps loaded individually per job. Recommend batch-loading.
- **ep-287 (medium)**: YAML unmarshal on request thread for concurrency evaluation. Acceptable given small payloads.

## Files Read
- routers/api/v1/repo/action.go
- routers/api/v1/repo/actions_run.go
- routers/api/v1/shared/action.go
- models/actions/run.go
- models/actions/run_attempt.go
- models/actions/run_job.go
- models/actions/run_job_list.go
- models/actions/run_list.go
- services/actions/rerun.go
- services/actions/cleanup.go
- services/actions/interface.go
- services/convert/convert.go
- modules/setting/actions.go


---

## Session 43

# Phase 2 Session Report

**Session:** 43
**Endpoints Analyzed:** ep-293 to ep-298
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 11
- External integrations used: 1 (Object Storage)
- Performance issues found: 3
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-293 | GET | /api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts | 2 steps | 4 files | 0 |
| ep-294 | DELETE | /api/v1/repos/{owner}/{repo}/actions/runs/{run} | 3 steps | 5 files | 2 |
| ep-295 | GET | /api/v1/repos/{owner}/{repo}/actions/artifacts | 2 steps | 4 files | 0 |
| ep-296 | GET | /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | 3 steps | 4 files | 0 |
| ep-297 | DELETE | /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | 2 steps | 4 files | 0 |
| ep-298 | GET | /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip | 4 steps | 5 files | 1 |

## Performance Issues Found
- **ep-294 (medium)**: Storage file deletions (logs + artifacts) happen synchronously after DB transaction, blocking response
- **ep-294 (medium)**: All jobs/tasks/artifacts loaded into memory without limit for deletion
- **ep-298 (low)**: Storage operations have no explicit timeout

## Key Findings
- Artifact endpoints only support v4 format (content_encoding contains '/'); v3 artifacts return 404
- DeleteArtifact is a soft-delete (marks PendingDeletion); actual file removal is by cron job
- DeleteActionRun is a hard-delete within a transaction but storage cleanup is non-atomic (post-transaction)
- Download uses HMAC-SHA256 signed URLs with 60-minute expiry when ServeDirect is not available

## Files Read
- routers/api/v1/repo/action.go (lines 1667-2100)
- models/actions/artifact.go
- services/convert/convert.go (lines 550-590)
- services/actions/artifacts.go
- services/actions/cleanup.go (lines 175-265)
- models/actions/run.go (lines 343-355)
- models/actions/run_job.go (lines 203-212)
- models/actions/status.go (lines 50-55)
- modules/structs/repo_actions.go (lines 88-155)
- modules/setting/storage.go (lines 97-103)
- models/db/context.go (lines 283-300)


---

## Session 44

# Phase 2 Session Report

**Session:** 44
**Endpoints Analyzed:** ep-299 to ep-305
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 10
- Database operations documented: 24
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-299 | GET | /api/v1/repos/{owner}/{repo}/git/notes/{sha} | 5 steps | 4 files | 1 |
| ep-300 | GET | /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | 1 step | 3 files | 1 |
| ep-301 | POST | /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | 4 steps | 3 files | 0 |
| ep-302 | DELETE | /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | 2 steps | 3 files | 0 |
| ep-303 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | 1 step | 3 files | 0 |
| ep-304 | POST | /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | 4 steps | 3 files | 0 |
| ep-305 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | 2 steps | 3 files | 0 |

## Performance Issues Found
- **ep-299 (medium)**: Git note lookup involves multiple git operations with no caching
- **ep-300 (medium)**: Comment reactions endpoint has no pagination (unbounded result set)

## Files Read
- routers/api/v1/repo/notes.go
- routers/api/v1/repo/issue_reaction.go
- models/issues/reaction.go
- services/issue/reaction.go
- modules/structs/issue_reaction.go
- modules/structs/repo_note.go
- modules/git/notes.go
- modules/git/notes_nogogit.go
- services/convert/git_commit.go
- modules/setting/ui.go
- models/user/block.go
- routers/api/v1/utils/page.go


---

## Session 45

# Phase 2 Session Report

**Session:** 45
**Endpoints Analyzed:** ep-306 to ep-311
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 12
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-306 | GET | /api/v1/repos/{owner}/{repo}/branches/{branch} | 5 steps | 5 files | 0 |
| ep-307 | DELETE | /api/v1/repos/{owner}/{repo}/branches/{branch} | 5 steps | 5 files | 1 |
| ep-308 | POST | /api/v1/repos/{owner}/{repo}/branches | 6 steps | 5 files | 1 |
| ep-309 | GET | /api/v1/repos/{owner}/{repo}/branches | 6 steps | 5 files | 1 |
| ep-310 | PUT | /api/v1/repos/{owner}/{repo}/branches/{branch} | 5 steps | 5 files | 0 |
| ep-311 | PATCH | /api/v1/repos/{owner}/{repo}/branches/{branch} | 5 steps | 5 files | 0 |

## Performance Issues Found
- **ep-309 (HIGH)**: N+1 pattern - GetBranchCommit called per branch in loop, plus individual permission checks per branch
- **ep-308 (MEDIUM)**: checkBranchName walks ALL refs in repository for name conflict detection
- **ep-307 (MEDIUM)**: SyncRepoBranches called synchronously on first access if no branches in DB

## Files Read
- routers/api/v1/repo/branch.go
- services/repository/branch.go
- services/repository/merge_upstream.go
- services/convert/convert.go
- models/git/branch.go
- models/git/protected_branch.go
- modules/structs/repo_branch.go
- modules/structs/repo.go


---

## Session 46

# Phase 2 Session Report

**Session:** 46
**Endpoints Analyzed:** ep-312 to ep-317
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 6 endpoint operation sets
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-312 | GET | /api/v1/repos/{owner}/{repo}/branch_protections/{name} | 3 steps | 5 files | 0 |
| ep-313 | GET | /api/v1/repos/{owner}/{repo}/branch_protections | 3 steps | 5 files | 1 |
| ep-314 | POST | /api/v1/repos/{owner}/{repo}/branch_protections | 5 steps | 6 files | 1 |
| ep-315 | PATCH | /api/v1/repos/{owner}/{repo}/branch_protections/{name} | 3 steps | 6 files | 1 |
| ep-316 | DELETE | /api/v1/repos/{owner}/{repo}/branch_protections/{name} | 2 steps | 5 files | 0 |
| ep-317 | POST | /api/v1/repos/{owner}/{repo}/branch_protections/priority | 2 steps | 5 files | 1 |

## Performance Issues Found
- **ep-313 (medium)**: N+1 queries in ToBranchProtection - users/teams fetched per rule in list
- **ep-314 (medium)**: N+1 queries in updateUserWhitelist - per-user permission check
- **ep-315 (medium)**: N+1 queries in CheckPRsForBaseBranch for glob rules matching many branches
- **ep-317 (low)**: N separate UPDATE statements in transaction for priority reordering

## Files Read
- routers/api/v1/repo/branch.go
- models/git/protected_branch.go
- models/git/protected_branch_list.go
- services/convert/convert.go
- services/pull/protected_branch.go
- services/pull/check.go
- services/repository/merge_upstream.go
- modules/structs/repo_branch.go


---

## Session 47

# Phase 2 Session Report

**Session:** 47
**Endpoints Analyzed:** ep-318 to ep-323
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 12
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-318 | POST | /api/v1/repos/{owner}/{repo}/merge-upstream | 5 steps | 4 files | 1 |
| ep-319 | PUT | /api/v1/repos/{owner}/{repo}/issues/{index}/lock | 2 steps | 3 files | 0 |
| ep-320 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/lock | 2 steps | 3 files | 0 |
| ep-321 | GET | /api/v1/repos/{owner}/{repo}/hooks | 2 steps | 4 files | 1 |
| ep-322 | GET | /api/v1/repos/{owner}/{repo}/hooks/{id} | 2 steps | 4 files | 0 |
| ep-323 | POST | /api/v1/repos/{owner}/{repo}/hooks/{id}/tests | 3 steps | 4 files | 0 |

## Performance Issues Found
- ep-318 (medium): Synchronous git push/merge operations can block for large repos
- ep-321 (low): No caching on webhook list queries (acceptable for typical usage)

## Files Read
- routers/api/v1/repo/branch.go
- routers/api/v1/repo/issue_lock.go
- routers/api/v1/repo/hook.go
- routers/api/v1/utils/hook.go
- services/repository/merge_upstream.go
- models/issues/issue_lock.go
- models/webhook/webhook.go
- modules/structs/hook.go
- modules/structs/issue.go
- modules/structs/repo_branch.go
- services/webhook/general.go
- services/webhook/webhook.go


---

## Session 48

# Phase 2 Session Report

**Session:** 48
**Endpoints Analyzed:** ep-324 to ep-329
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 9
- Database operations documented: 10
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-324 | POST | /api/v1/repos/{owner}/{repo}/hooks | 5 steps | 5 files | 0 |
| ep-325 | PATCH | /api/v1/repos/{owner}/{repo}/hooks/{id} | 4 steps | 5 files | 1 |
| ep-326 | DELETE | /api/v1/repos/{owner}/{repo}/hooks/{id} | 2 steps | 3 files | 0 |
| ep-327 | GET | /api/v1/repos/{owner}/{repo}/stargazers | 3 steps | 3 files | 1 |
| ep-328 | GET | /api/v1/repos/{owner}/{repo}/subscribers | 3 steps | 3 files | 1 |
| ep-329 | GET | /api/v1/repos/{owner}/{repo}/teams | 3 steps | 4 files | 1 |

## Performance Issues Found
- **ep-327 (medium)**: Unbounded query when page=0 returns all stargazers without limit
- **ep-328 (medium)**: Unbounded query when page=0 returns all watchers without limit
- **ep-329 (medium)**: N+1 queries - LoadUnits called per team in convert.ToTeams loop
- **ep-325 (low)**: Unnecessary re-fetch of webhook after update

## Files Read
- routers/api/v1/repo/hook.go
- routers/api/v1/utils/hook.go
- models/webhook/webhook.go
- modules/structs/hook.go
- services/webhook/general.go
- services/webhook/webhook.go
- routers/api/v1/repo/star.go
- routers/api/v1/repo/subscriber.go
- routers/api/v1/repo/teams.go
- models/repo/star.go
- models/repo/watch.go
- models/organization/team_list.go
- services/convert/convert.go


---

## Session 49

# Phase 2 Session Report

**Session:** 49
**Endpoints Analyzed:** ep-330 to ep-335
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 10
- Database operations documented: 26
- External integrations used: 1 (Git CLI for fork clone)
- Performance issues found: 5
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-330 | GET | /api/v1/repos/{owner}/{repo}/teams/{team} | 4 steps | 5 files | 0 |
| ep-331 | PUT | /api/v1/repos/{owner}/{repo}/teams/{team} | 3 steps | 5 files | 1 |
| ep-332 | DELETE | /api/v1/repos/{owner}/{repo}/teams/{team} | 3 steps | 5 files | 1 |
| ep-333 | GET | /api/v1/repos/{owner}/{repo}/forks | 5 steps | 4 files | 1 |
| ep-334 | POST | /api/v1/repos/{owner}/{repo}/forks | 3 steps | 5 files | 1 |
| ep-335 | GET | /api/v1/repos/{owner}/{repo}/issues/{index}/labels | 4 steps | 4 files | 1 |

## Performance Issues Found
- **ep-331 (medium)**: N+1 queries for auto-watch of team members
- **ep-332 (medium)**: N+1 queries for access check and watch removal per team member
- **ep-333 (medium)**: N+1 queries for permission check per fork
- **ep-334 (high)**: Synchronous blocking git clone with 10-minute timeout on request thread
- **ep-335 (low)**: LoadAttributes loads unnecessary relations when only labels needed

## Files Read
- routers/api/v1/repo/teams.go
- routers/api/v1/repo/fork.go
- routers/api/v1/repo/issue_label.go
- services/repository/repo_team.go
- services/repository/fork.go
- services/issue/label.go
- models/organization/team_repo.go
- models/organization/team.go
- models/organization/team_list.go
- models/repo/fork.go
- models/issues/issue_label.go
- models/issues/label.go
- services/convert/convert.go
- services/convert/issue.go
- modules/structs/fork.go
- modules/structs/issue_label.go


---

## Session 50

# Phase 2 Session Report

**Session:** 50
**Endpoints Analyzed:** ep-336 to ep-343
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 37
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 3.5 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-336 | POST | /api/v1/repos/{owner}/{repo}/issues/{index}/labels | 5 steps | 4 files | 1 |
| ep-337 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id} | 2 steps | 3 files | 1 |
| ep-338 | PUT | /api/v1/repos/{owner}/{repo}/issues/{index}/labels | 3 steps | 4 files | 0 |
| ep-339 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/labels | 3 steps | 3 files | 1 |
| ep-340 | GET | /api/v1/repos/{owner}/{repo}/keys | 2 steps | 3 files | 1 |
| ep-341 | GET | /api/v1/repos/{owner}/{repo}/keys/{id} | 1 step | 3 files | 0 |
| ep-342 | POST | /api/v1/repos/{owner}/{repo}/keys | 3 steps | 4 files | 0 |
| ep-343 | DELETE | /api/v1/repos/{owner}/{repo}/keys/{id} | 3 steps | 4 files | 1 |

## Performance Issues Found
- **HIGH** ep-339: ClearIssueLabels uses per-label deletion loop (3N queries for N labels)
- **HIGH** ep-343: RewriteAllPublicKeys rewrites entire authorized_keys file on every key deletion
- **MEDIUM** ep-336: N+1 HasIssueLabel check per label in add loop
- **MEDIUM** ep-340: N+1 GetContent per deploy key in list

## Files Read
- routers/api/v1/repo/issue_label.go
- routers/api/v1/repo/key.go
- services/issue/label.go
- services/asymkey/deploy_key.go
- services/asymkey/ssh_key_authorized_keys.go
- models/issues/issue_label.go
- models/issues/label.go
- models/asymkey/ssh_key_deploy.go
- models/asymkey/ssh_key_parse.go
- modules/structs/issue_label.go
- modules/structs/repo_key.go
- services/convert/convert.go
- services/convert/issue.go


---

## Session 51

# Phase 2 Session Report

**Session:** 51
**Endpoints Analyzed:** ep-344 to ep-351
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 30
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-344 | GET | /api/v1/repos/{owner}/{repo}/releases/tags/{tag} | 4 steps | 4 files | 0 |
| ep-345 | DELETE | /api/v1/repos/{owner}/{repo}/releases/tags/{tag} | 3 steps | 4 files | 0 |
| ep-346 | GET | /api/v1/repos/{owner}/{repo}/licenses | 2 steps | 2 files | 0 |
| ep-347 | GET | /api/v1/repos/{owner}/{repo}/topics | 2 steps | 2 files | 0 |
| ep-348 | PUT | /api/v1/repos/{owner}/{repo}/topics | 3 steps | 2 files | 1 |
| ep-349 | PUT | /api/v1/repos/{owner}/{repo}/topics/{topic} | 3 steps | 2 files | 0 |
| ep-350 | DELETE | /api/v1/repos/{owner}/{repo}/topics/{topic} | 2 steps | 2 files | 0 |
| ep-351 | GET | /api/v1/topics/search | 3 steps | 3 files | 1 |

## Performance Issues Found
- **ep-348 (medium)**: N+1 pattern in SaveTopics - iterates over added/removed topics with individual DB operations per topic
- **ep-351 (low)**: LIKE '%keyword%' search on topic.name cannot use B-tree indexes efficiently

## Files Read
- routers/api/v1/repo/release_tags.go
- routers/api/v1/repo/release.go
- routers/api/v1/repo/license.go
- routers/api/v1/repo/topic.go
- models/repo/release.go
- models/repo/license.go
- models/repo/topic.go
- services/release/release.go
- services/convert/release.go
- services/convert/convert.go
- modules/structs/repo_topic.go


---

## Session 52

# Phase 2 Session Report

**Session:** 52
**Endpoints Analyzed:** ep-352 to ep-358
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 10
- Database operations documented: 14
- External integrations used: 1 (Object Storage)
- Performance issues found: 3
- Average workflow depth: 3.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-352 | GET | /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | 4 steps | 5 files | 0 |
| ep-353 | GET | /api/v1/repos/{owner}/{repo}/releases/{id}/assets | 4 steps | 5 files | 1 |
| ep-354 | POST | /api/v1/repos/{owner}/{repo}/releases/{id}/assets | 4 steps | 6 files | 1 |
| ep-355 | PATCH | /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | 4 steps | 5 files | 0 |
| ep-356 | DELETE | /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | 4 steps | 5 files | 1 |
| ep-357 | GET | /api/v1/repos/{owner}/{repo}/labels | 4 steps | 4 files | 0 |
| ep-358 | GET | /api/v1/repos/{owner}/{repo}/labels/{id} | 3 steps | 4 files | 0 |

## Performance Issues Found
- **ep-353 (medium)**: LoadAttributes loads unnecessary data (repo, publisher) when only attachments needed
- **ep-354 (medium)**: No timeout on storage write operation for file uploads
- **ep-356 (low)**: Synchronous storage file deletion on request path

## Files Read
- routers/api/v1/repo/release_attachment.go
- routers/api/v1/repo/release.go
- routers/api/v1/repo/label.go
- models/repo/attachment.go
- models/issues/label.go
- services/attachment/attachment.go
- services/convert/attachment.go
- services/convert/issue.go
- services/context/upload/upload.go
- modules/structs/attachment.go
- modules/structs/issue_label.go
- modules/setting/attachment.go
- modules/setting/repository.go
- modules/label/label.go
- routers/api/v1/utils/page.go


---

## Session 53

# Phase 2 Session Report

**Session:** 53
**Endpoints Analyzed:** ep-359 to ep-366
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 16
- External integrations used: 0
- Performance issues found: 4
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-359 | POST | /api/v1/repos/{owner}/{repo}/labels | 4 steps | 5 files | 0 |
| ep-360 | PATCH | /api/v1/repos/{owner}/{repo}/labels/{id} | 4 steps | 5 files | 1 |
| ep-361 | DELETE | /api/v1/repos/{owner}/{repo}/labels/{id} | 2 steps | 3 files | 0 |
| ep-362 | GET | /api/v1/repos/search | 5 steps | 6 files | 2 |
| ep-363 | POST | /api/v1/user/repos | 5 steps | 5 files | 0 |
| ep-364 | POST | /api/v1/repos/{template_owner}/{template_repo}/generate | 3 steps | 5 files | 1 |
| ep-365 | POST | /api/v1/org/{org}/repos | 4 steps | 4 files | 0 |
| ep-366 | POST | /api/v1/orgs/{org}/repos | 4 steps | 4 files | 0 |

## Performance Issues Found
- **ep-362 (HIGH)**: N+1 queries - LoadOwner and GetDoerRepoPermission called per result in loop
- **ep-362 (MEDIUM)**: No caching on high-frequency search endpoint
- **ep-360 (LOW)**: UpdateLabel recalculates issue counts via subqueries on every edit
- **ep-364 (MEDIUM)**: Synchronous blocking on git content copy for large templates

## Files Read
- routers/api/v1/repo/label.go
- routers/api/v1/repo/repo.go
- routers/api/v1/repo/fork.go
- models/issues/label.go
- models/repo/repo_list.go
- models/repo/search.go
- modules/label/label.go
- modules/structs/issue_label.go
- modules/structs/repo.go
- modules/setting/repository.go
- services/convert/issue.go
- services/repository/repository.go
- services/repository/create.go
- services/repository/template.go
- services/repository/generate.go


---

## Session 54

# Phase 2 Session Report

**Session:** 54
**Endpoints Analyzed:** ep-367 to ep-374
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 10
- Database operations documented: 15
- External integrations used: 0
- Performance issues found: 3
- Average workflow depth: 3 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-367 | GET | /api/v1/repos/{owner}/{repo} | 2 steps | 4 files | 1 |
| ep-368 | GET | /api/v1/repositories/{id} | 3 steps | 4 files | 0 |
| ep-369 | PATCH | /api/v1/repos/{owner}/{repo} | 5 steps | 5 files | 0 |
| ep-370 | DELETE | /api/v1/repos/{owner}/{repo} | 3 steps | 4 files | 0 |
| ep-371 | GET | /api/v1/repos/{owner}/{repo}/issue_templates | 2 steps | 3 files | 1 |
| ep-372 | GET | /api/v1/repos/{owner}/{repo}/issue_config | 2 steps | 3 files | 0 |
| ep-373 | GET | /api/v1/repos/{owner}/{repo}/issue_config/validate | 1 step | 3 files | 0 |
| ep-374 | GET | /api/v1/repos/{owner}/{repo}/activities/feeds | 3 steps | 4 files | 1 |

## Performance Issues Found
- ep-367: ToRepo performs 7+ DB queries per call with no caching (medium)
- ep-371: Parses template files from git on every request (low)
- ep-374: Action table queries may be slow without proper composite index (medium)

## Files Read
- routers/api/v1/repo/repo.go
- routers/api/v1/repo/language.go
- routers/api/v1/repo/issue_pin.go
- services/convert/repository.go
- services/issue/template.go
- services/feed/feed.go
- models/repo/repo.go
- models/repo/language_stats.go
- models/issues/issue_pin.go
- models/activities/action_list.go
- models/perm/access/repo_permission.go
- modules/repository/delete.go
- modules/setting/repository.go
- modules/structs/repo.go


---

## Session 55

# Phase 2 Session Report

**Session:** 55
**Endpoints Analyzed:** ep-375 to ep-381
**Total Endpoints:** 7
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 7
- Business rules extracted: 8
- Database operations documented: 21
- External integrations used: 0
- Performance issues found: 2
- Average workflow depth: 2.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-375 | GET | /api/v1/repos/{owner}/{repo}/languages | 2 steps | 2 files | 0 |
| ep-376 | POST | /api/v1/repos/{owner}/{repo}/issues/{index}/pin | 3 steps | 3 files | 0 |
| ep-377 | DELETE | /api/v1/repos/{owner}/{repo}/issues/{index}/pin | 2 steps | 2 files | 0 |
| ep-378 | PATCH | /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position} | 2 steps | 2 files | 0 |
| ep-379 | GET | /api/v1/repos/{owner}/{repo}/issues/pinned | 3 steps | 3 files | 1 |
| ep-380 | GET | /api/v1/repos/{owner}/{repo}/pulls/pinned | 4 steps | 4 files | 1 |
| ep-381 | GET | /api/v1/repos/{owner}/{repo}/new_pin_allowed | 2 steps | 3 files | 0 |

## Performance Issues Found
- ep-380 (medium): N+1 queries in ListPinnedPullRequests - LoadAttributes/LoadBaseRepo/LoadHeadRepo called per PR in loop. Mitigated by MaxPinned=3 default.

## Files Read
- routers/api/v1/repo/language.go
- models/repo/language_stats.go
- routers/api/v1/repo/issue_pin.go
- models/issues/issue_pin.go
- modules/structs/repo.go
- modules/setting/repository.go
- routers/api/v1/repo/issue_stopwatch.go
- models/issues/stopwatch.go
- services/convert/issue.go
- modules/structs/issue_stopwatch.go
- services/context/repo.go

