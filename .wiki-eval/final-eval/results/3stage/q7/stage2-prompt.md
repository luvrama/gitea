# Stage 2: Wiki-Based Query Answerer

You are a codebase expert. Answer the developer's query using ONLY the wiki pages provided below. Do not make assumptions beyond what is documented in the provided context.

## Rules

- Answer based solely on the provided wiki content
- Be specific: include file paths, function names, and configuration values when available
- Structure your answer clearly with headers and tables where appropriate

## Answer Validation

Before finalizing your answer, verify:
1. Did you address every part of the query? If the query asks for multiple things (e.g., "method, path, handler, permissions"), ensure each is covered.
2. If the query asks for "all" of something, cross-reference the project overview or module page to check if your answer is complete. If the wiki pages show N total items but you only found M, state: "Found M of N total."
3. If the wiki pages don't contain enough information to fully answer, explicitly state what's missing and what additional pages would be needed.
4. Check for contradictions between different wiki pages — flag any inconsistencies.

## Wiki Pages


--- FILE: README.md ---
# gitea

**Go** · **go-chi/chi v5 + XORM** · **Make** · 475 endpoints · 1 modules

## Modules

| Module | Endpoints | Dependencies |
|--------|-----------|--------------|
| [routers](modules/routers.md) | 475 | actions_service, asymkey_service, attachment_service, createTag, git, gitrepo, mailer, mirror_service, password, pull, release_service, repo_model, repo_service, storage, user_service |

## Quick Links

- [Database Tables](datastores/databases.md) (94 tables)
- [Cache Stores](datastores/caches.md) (1 stores)
- [Message Queues](datastores/queues.md) (4 queues)
- [External Services](external/overview.md) (7 integrations)
- [Configuration](config/overview.md) (109 properties)
- [Global Error Handlers](errors/global-handlers.md) (3 handlers)
- [Business Rules]() (570 rules)
- [Performance Analysis](performance/overview.md) (198 issues)
- [Resiliency Assessment](resiliency/overview.md) (351 findings)


--- FILE: external/overview.md ---
# External Services

**7 integrations**

- [GPG binary (gpg --export)](GPG_binary__gpg_--export_.md)
- [Object Storage (Minio/Azure/Local)](Object_Storage__Minio_Azure_Local_.md)
- [HaveIBeenPwned API](HaveIBeenPwned_API.md)
- [HaveIBeenPwned API](HaveIBeenPwned_API.md)
- [Avatar Storage Backend](Avatar_Storage_Backend.md)
- [Git Remote (Push Mirror Target)](Git_Remote__Push_Mirror_Target_.md)
- [Git Repository (local filesystem)](Git_Repository__local_filesystem_.md)


--- FILE: external/Git_Repository__local_filesystem_.md ---
# Git Repository (local filesystem)

**Client:** `git.Repository` · **Type:** filesystem

**File:** `modules/git/repo.go`

**Base URL:** `local git repo path`

**Auth:** none (local filesystem access)

## Resilience

| Setting | Value |
|---------|-------|
| Circuit breaker | ❌ Disabled |
| Level | — |
| Implementation | None |
| Open condition | — |
| Recovery | — |
| Impact when open | — |

## Methods Called

| Method | Path | Purpose |
|--------|------|---------|
| CLI | git tag | Create git tag on release publish |
| CLI | git tag -d | Delete git tag on release delete with delTag=true |
| CLI | git rev-parse / cat-file | Resolve target commit for tag creation |

## Used By (3 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-243](../endpoints/ep-243.md), [ep-244](../endpoints/ep-244.md), [ep-245](../endpoints/ep-245.md) |


--- FILE: external/Git_Remote__Push_Mirror_Target_.md ---
# Git Remote (Push Mirror Target)

**Client:** `gitrepo` · **Type:** http_api

**File:** `services/mirror/mirror_push.go`

**Base URL:** `configured per push mirror (remote_address)`

**Auth:** bearer

## Resilience

| Setting | Value |
|---------|-------|
| Circuit breaker | ❌ Disabled |
| Level | — |
| Implementation | None |
| Open condition | — |
| Recovery | — |
| Impact when open | — |
| Timeout | setting.Git.Timeout.Mirror * 1000ms |

## Methods Called

| Method | Path | Purpose |
|--------|------|---------|
| POST | git push --mirror | Push all refs to remote mirror |
| POST | LFS batch API | Upload LFS objects to remote |

## Used By (2 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-235](../endpoints/ep-235.md), [ep-334](../endpoints/ep-334.md) |


--- FILE: resiliency/overview.md ---
# Resiliency Assessment

**Overall Risk:** critical · **351 findings**

## Dependency Resiliency Matrix

| Dependency | Timeout | Retry | Circuit Breaker | Bulkhead | Fallback | Blast Radius |
|------------|---------|-------|-----------------|----------|----------|-------------|
| GPG binary (gpg --export) | ❌ | ❌ | ❌ | ❌ | ❌ | [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md) |
| Git config (git config --global --get) | ✅ | ❌ | ❌ | ❌ | ✅ | [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md), [ep-006](../endpoints/ep-006.md), [ep-007](../endpoints/ep-007.md) |
| SQL Database (notification table) | ✅ | ❌ | ❌ | ✅ | ❌ | [ep-019](../endpoints/ep-019.md), [ep-020](../endpoints/ep-020.md), [ep-021](../endpoints/ep-021.md), [ep-022](../endpoints/ep-022.md) |
| Avatar Storage Backend | ❌ | ❌ | ❌ | ❌ | ✅ | [ep-037](../endpoints/ep-037.md), [ep-038](../endpoints/ep-038.md), [ep-128](../endpoints/ep-128.md), [ep-259](../endpoints/ep-259.md), [ep-261](../endpoints/ep-261.md), [ep-262](../endpoints/ep-262.md), [ep-263](../endpoints/ep-263.md), [ep-294](../endpoints/ep-294.md), [ep-298](../endpoints/ep-298.md), [ep-354](../endpoints/ep-354.md), [ep-356](../endpoints/ep-356.md) |
| HaveIBeenPwned API | ❌ | ❌ | ❌ | ❌ | ✅ | [ep-098](../endpoints/ep-098.md) |
| HaveIBeenPwned API | ❌ | ❌ | ❌ | ❌ | ✅ | [ep-099](../endpoints/ep-099.md) |
| Avatar Storage Backend | ❌ | ❌ | ❌ | ❌ | ✅ | [ep-129](../endpoints/ep-129.md) |
| Git Remote (Push Mirror Target) | ✅ | ❌ | ❌ | ❌ | ❌ | [ep-235](../endpoints/ep-235.md) |
| Git Repository (local filesystem) | ✅ | ❌ | — | ❌ | ❌ | [ep-243](../endpoints/ep-243.md), [ep-244](../endpoints/ep-244.md), [ep-245](../endpoints/ep-245.md) |
| Git CLI (fork clone) | ✅ | ❌ | ❌ | ❌ | ✅ | [ep-334](../endpoints/ep-334.md) |

## Endpoint Risk Levels

| Endpoint | Path | Risk | Dependencies | Findings |
|----------|------|------|-------------|----------|
| [ep-023](../endpoints/ep-023.md) | PUT /api/v1/repos/{owner}/{repo}/notifications | high | 0 | 2 |
| [ep-036](../endpoints/ep-036.md) | DELETE /api/v1/orgs/{org}/repos | high | 0 | 2 |
| [ep-089](../endpoints/ep-089.md) | PUT /api/v1/orgs/{org}/blocks/{username} | high | 0 | 3 |
| [ep-192](../endpoints/ep-192.md) | PUT /api/v1/user/blocks/{username} | high | 0 | 3 |
| [ep-235](../endpoints/ep-235.md) | POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync | high | 1 | 4 |
| [ep-334](../endpoints/ep-334.md) | POST /api/v1/repos/{owner}/{repo}/forks | high | 1 | 3 |
| [ep-343](../endpoints/ep-343.md) | DELETE /api/v1/repos/{owner}/{repo}/keys/{id} | high | 0 | 2 |
| [ep-004](../endpoints/ep-004.md) | GET /api/v1/signing-key.gpg | medium | 2 | 2 |
| [ep-005](../endpoints/ep-005.md) | GET /api/v1/repos/{owner}/{repo}/signing-key.gpg | medium | 2 | 1 |
| [ep-008](../endpoints/ep-008.md) | POST /api/v1/markup | medium | 0 | 1 |
| [ep-010](../endpoints/ep-010.md) | POST /api/v1/markdown/raw | medium | 0 | 1 |
| [ep-020](../endpoints/ep-020.md) | PUT /api/v1/notifications | medium | 1 | 2 |
| [ep-032](../endpoints/ep-032.md) | POST /api/v1/orgs/{org}/rename | medium | 0 | 2 |
| [ep-037](../endpoints/ep-037.md) | POST /api/v1/orgs/{org}/avatar | medium | 1 | 2 |
| [ep-058](../endpoints/ep-058.md) | PATCH /api/v1/teams/{id} | medium | 0 | 2 |
| [ep-059](../endpoints/ep-059.md) | DELETE /api/v1/teams/{id} | medium | 0 | 2 |
| [ep-062](../endpoints/ep-062.md) | PUT /api/v1/teams/{id}/members/{username} | medium | 0 | 2 |
| [ep-063](../endpoints/ep-063.md) | DELETE /api/v1/teams/{id}/members/{username} | medium | 0 | 2 |
| [ep-066](../endpoints/ep-066.md) | PUT /api/v1/teams/{id}/repos/{org}/{repo} | medium | 0 | 2 |
| [ep-067](../endpoints/ep-067.md) | DELETE /api/v1/teams/{id}/repos/{org}/{repo} | medium | 0 | 2 |
| [ep-076](../endpoints/ep-076.md) | DELETE /api/v1/orgs/{org}/members/{username} | medium | 0 | 3 |
| [ep-098](../endpoints/ep-098.md) | POST /api/v1/admin/users | medium | 1 | 4 |
| [ep-099](../endpoints/ep-099.md) | PATCH /api/v1/admin/users/{username} | medium | 1 | 1 |
| [ep-100](../endpoints/ep-100.md) | DELETE /api/v1/admin/users/{username} | medium | 0 | 1 |
| [ep-104](../endpoints/ep-104.md) | POST /api/v1/admin/users/{username}/rename | medium | 0 | 1 |
| [ep-107](../endpoints/ep-107.md) | GET /api/v1/admin/unadopted | medium | 0 | 1 |
| [ep-108](../endpoints/ep-108.md) | POST /api/v1/admin/unadopted/{owner}/{repo} | medium | 0 | 1 |
| [ep-121](../endpoints/ep-121.md) | POST /api/v1/admin/users/{username}/badges | medium | 0 | 2 |
| [ep-127](../endpoints/ep-127.md) | GET /api/v1/users/{username}/activities/feeds | medium | 1 | 1 |
| [ep-128](../endpoints/ep-128.md) | POST /api/v1/user/avatar | medium | 2 | 2 |
| [ep-160](../endpoints/ep-160.md) | POST /api/v1/user/keys | medium | 0 | 2 |
| [ep-161](../endpoints/ep-161.md) | DELETE /api/v1/user/keys/{id} | medium | 0 | 2 |
| [ep-167](../endpoints/ep-167.md) | POST /api/v1/user/applications/oauth2 | medium | 0 | 2 |
| [ep-171](../endpoints/ep-171.md) | PATCH /api/v1/user/applications/oauth2/{id} | medium | 0 | 1 |
| [ep-181](../endpoints/ep-181.md) | POST /api/v1/user/emails | medium | 0 | 1 |
| [ep-182](../endpoints/ep-182.md) | DELETE /api/v1/user/emails | medium | 0 | 1 |
| [ep-194](../endpoints/ep-194.md) | GET /api/v1/users/{username}/subscriptions | medium | 0 | 1 |
| [ep-195](../endpoints/ep-195.md) | GET /api/v1/user/subscriptions | medium | 0 | 1 |
| [ep-201](../endpoints/ep-201.md) | DELETE /api/v1/packages/{owner}/{type}/{name} | medium | 0 | 3 |
| [ep-202](../endpoints/ep-202.md) | DELETE /api/v1/packages/{owner}/{type}/{name}/{version} | medium | 0 | 1 |
| [ep-215](../endpoints/ep-215.md) | GET /api/v1/repos/{owner}/{repo}/commits | medium | 0 | 1 |
| [ep-216](../endpoints/ep-216.md) | GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType} | medium | 0 | 1 |
| [ep-222](../endpoints/ep-222.md) | GET /api/v1/repos/{owner}/{repo}/pulls | medium | 0 | 1 |
| [ep-225](../endpoints/ep-225.md) | GET /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType} | medium | 0 | 2 |
| [ep-226](../endpoints/ep-226.md) | POST /api/v1/repos/{owner}/{repo}/pulls | medium | 0 | 1 |
| [ep-227](../endpoints/ep-227.md) | PATCH /api/v1/repos/{owner}/{repo}/pulls/{index} | medium | 0 | 1 |
| [ep-238](../endpoints/ep-238.md) | POST /api/v1/repos/{owner}/{repo}/push_mirrors | medium | 0 | 2 |
| [ep-239](../endpoints/ep-239.md) | DELETE /api/v1/repos/{owner}/{repo}/push_mirrors/{name} | medium | 0 | 1 |
| [ep-243](../endpoints/ep-243.md) | POST /api/v1/repos/{owner}/{repo}/releases | medium | 2 | 2 |
| [ep-249](../endpoints/ep-249.md) | POST /api/v1/repos/{owner}/{repo}/diffpatch | medium | 0 | 2 |
| [ep-258](../endpoints/ep-258.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets | medium | 1 | 1 |
| [ep-259](../endpoints/ep-259.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets | medium | 2 | 2 |
| [ep-261](../endpoints/ep-261.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | medium | 2 | 1 |
| [ep-283](../endpoints/ep-283.md) | POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches | medium | 0 | 2 |
| [ep-287](../endpoints/ep-287.md) | POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun | medium | 0 | 2 |
| [ep-288](../endpoints/ep-288.md) | POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs | medium | 0 | 1 |
| [ep-289](../endpoints/ep-289.md) | POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun | medium | 0 | 1 |
| [ep-294](../endpoints/ep-294.md) | DELETE /api/v1/repos/{owner}/{repo}/actions/runs/{run} | medium | 2 | 2 |
| [ep-298](../endpoints/ep-298.md) | GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip | medium | 2 | 1 |
| [ep-307](../endpoints/ep-307.md) | DELETE /api/v1/repos/{owner}/{repo}/branches/{branch} | medium | 0 | 1 |
| [ep-308](../endpoints/ep-308.md) | POST /api/v1/repos/{owner}/{repo}/branches | medium | 0 | 1 |
| [ep-311](../endpoints/ep-311.md) | PATCH /api/v1/repos/{owner}/{repo}/branches/{branch} | medium | 0 | 1 |
| [ep-315](../endpoints/ep-315.md) | PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name} | medium | 0 | 1 |
| [ep-318](../endpoints/ep-318.md) | POST /api/v1/repos/{owner}/{repo}/merge-upstream | medium | 0 | 2 |
| [ep-339](../endpoints/ep-339.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels | medium | 0 | 1 |
| [ep-345](../endpoints/ep-345.md) | DELETE /api/v1/repos/{owner}/{repo}/releases/tags/{tag} | medium | 0 | 1 |
| [ep-354](../endpoints/ep-354.md) | POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets | medium | 1 | 2 |
| [ep-363](../endpoints/ep-363.md) | POST /api/v1/user/repos | medium | 0 | 1 |
| [ep-364](../endpoints/ep-364.md) | POST /api/v1/repos/{template_owner}/{template_repo}/generate | medium | 0 | 1 |
| [ep-365](../endpoints/ep-365.md) | POST /api/v1/org/{org}/repos | medium | 0 | 1 |
| [ep-366](../endpoints/ep-366.md) | POST /api/v1/orgs/{org}/repos | medium | 0 | 1 |
| [ep-369](../endpoints/ep-369.md) | PATCH /api/v1/repos/{owner}/{repo} | medium | 0 | 1 |
| [ep-001](../endpoints/ep-001.md) | GET /api/v1/version | low | 0 | 0 |
| [ep-002](../endpoints/ep-002.md) | GET /api/v1/label/templates | low | 0 | 0 |
| [ep-003](../endpoints/ep-003.md) | GET /api/v1/label/templates/{name} | low | 0 | 1 |
| [ep-006](../endpoints/ep-006.md) | GET /api/v1/signing-key.pub | low | 1 | 0 |
| [ep-007](../endpoints/ep-007.md) | GET /api/v1/repos/{owner}/{repo}/signing-key.pub | low | 1 | 0 |
| [ep-009](../endpoints/ep-009.md) | POST /api/v1/markdown | low | 0 | 1 |
| [ep-011](../endpoints/ep-011.md) | GET /api/v1/gitignore/templates | low | 0 | 0 |
| [ep-012](../endpoints/ep-012.md) | GET /api/v1/gitignore/templates/{name} | low | 0 | 1 |
| [ep-013](../endpoints/ep-013.md) | GET /api/v1/licenses | low | 0 | 0 |
| [ep-014](../endpoints/ep-014.md) | GET /api/v1/licenses/{name} | low | 0 | 1 |
| [ep-015](../endpoints/ep-015.md) | GET /api/v1/settings/ui | low | 0 | 0 |
| [ep-016](../endpoints/ep-016.md) | GET /api/v1/settings/api | low | 0 | 0 |
| [ep-017](../endpoints/ep-017.md) | GET /api/v1/settings/repository | low | 0 | 0 |
| [ep-018](../endpoints/ep-018.md) | GET /api/v1/settings/attachment | low | 0 | 0 |
| [ep-019](../endpoints/ep-019.md) | GET /api/v1/notifications | low | 1 | 1 |
| [ep-021](../endpoints/ep-021.md) | GET /api/v1/notifications/new | low | 1 | 1 |
| [ep-022](../endpoints/ep-022.md) | GET /api/v1/repos/{owner}/{repo}/notifications | low | 1 | 1 |
| [ep-024](../endpoints/ep-024.md) | GET /api/v1/notifications/threads/{id} | low | 0 | 1 |
| [ep-025](../endpoints/ep-025.md) | PATCH /api/v1/notifications/threads/{id} | low | 0 | 1 |
| [ep-026](../endpoints/ep-026.md) | GET /api/v1/user/orgs | low | 0 | 1 |
| [ep-027](../endpoints/ep-027.md) | GET /api/v1/users/{username}/orgs | low | 0 | 0 |
| [ep-028](../endpoints/ep-028.md) | GET /api/v1/users/{username}/orgs/{org}/permissions | low | 0 | 0 |
| [ep-029](../endpoints/ep-029.md) | GET /api/v1/orgs | low | 0 | 1 |
| [ep-030](../endpoints/ep-030.md) | POST /api/v1/orgs | low | 0 | 1 |
| [ep-031](../endpoints/ep-031.md) | GET /api/v1/orgs/{org} | low | 0 | 0 |
| [ep-033](../endpoints/ep-033.md) | PATCH /api/v1/orgs/{org} | low | 0 | 1 |
| [ep-034](../endpoints/ep-034.md) | DELETE /api/v1/orgs/{org} | low | 0 | 1 |
| [ep-035](../endpoints/ep-035.md) | GET /api/v1/orgs/{org}/activities/feeds | low | 0 | 1 |
| [ep-038](../endpoints/ep-038.md) | DELETE /api/v1/orgs/{org}/avatar | low | 1 | 1 |
| [ep-039](../endpoints/ep-039.md) | GET /api/v1/orgs/{org}/actions/secrets | low | 0 | 0 |
| [ep-040](../endpoints/ep-040.md) | PUT /api/v1/orgs/{org}/actions/secrets/{secretname} | low | 0 | 1 |
| [ep-041](../endpoints/ep-041.md) | DELETE /api/v1/orgs/{org}/actions/secrets/{secretname} | low | 0 | 0 |
| [ep-042](../endpoints/ep-042.md) | POST /api/v1/orgs/{org}/actions/runners/registration-token | low | 0 | 1 |
| [ep-043](../endpoints/ep-043.md) | GET /api/v1/orgs/{org}/actions/variables | low | 0 | 0 |
| [ep-044](../endpoints/ep-044.md) | GET /api/v1/orgs/{org}/actions/variables/{variablename} | low | 0 | 0 |
| [ep-045](../endpoints/ep-045.md) | DELETE /api/v1/orgs/{org}/actions/variables/{variablename} | low | 0 | 1 |
| [ep-046](../endpoints/ep-046.md) | POST /api/v1/orgs/{org}/actions/variables/{variablename} | low | 0 | 1 |
| [ep-047](../endpoints/ep-047.md) | PUT /api/v1/orgs/{org}/actions/variables/{variablename} | low | 0 | 1 |
| [ep-048](../endpoints/ep-048.md) | GET /api/v1/orgs/{org}/actions/runners | low | 0 | 0 |
| [ep-049](../endpoints/ep-049.md) | GET /api/v1/orgs/{org}/actions/runners/{runner_id} | low | 0 | 0 |
| [ep-050](../endpoints/ep-050.md) | DELETE /api/v1/orgs/{org}/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-051](../endpoints/ep-051.md) | PATCH /api/v1/orgs/{org}/actions/runners/{runner_id} | low | 0 | 2 |
| [ep-052](../endpoints/ep-052.md) | GET /api/v1/orgs/{org}/actions/jobs | low | 0 | 2 |
| [ep-053](../endpoints/ep-053.md) | GET /api/v1/orgs/{org}/actions/runs | low | 0 | 1 |
| [ep-054](../endpoints/ep-054.md) | GET /api/v1/orgs/{org}/teams | low | 0 | 1 |
| [ep-055](../endpoints/ep-055.md) | GET /api/v1/user/teams | low | 0 | 1 |
| [ep-056](../endpoints/ep-056.md) | GET /api/v1/teams/{id} | low | 0 | 0 |
| [ep-057](../endpoints/ep-057.md) | POST /api/v1/orgs/{org}/teams | low | 0 | 1 |
| [ep-060](../endpoints/ep-060.md) | GET /api/v1/teams/{id}/members | low | 0 | 0 |
| [ep-061](../endpoints/ep-061.md) | GET /api/v1/teams/{id}/members/{username} | low | 0 | 0 |
| [ep-064](../endpoints/ep-064.md) | GET /api/v1/teams/{id}/repos | low | 0 | 1 |
| [ep-065](../endpoints/ep-065.md) | GET /api/v1/teams/{id}/repos/{org}/{repo} | low | 0 | 1 |
| [ep-068](../endpoints/ep-068.md) | GET /api/v1/orgs/{org}/teams/search | low | 0 | 1 |
| [ep-069](../endpoints/ep-069.md) | GET /api/v1/teams/{id}/activities/feeds | low | 0 | 1 |
| [ep-070](../endpoints/ep-070.md) | GET /api/v1/orgs/{org}/members | low | 0 | 0 |
| [ep-071](../endpoints/ep-071.md) | GET /api/v1/orgs/{org}/public_members | low | 0 | 0 |
| [ep-072](../endpoints/ep-072.md) | GET /api/v1/orgs/{org}/members/{username} | low | 0 | 0 |
| [ep-073](../endpoints/ep-073.md) | GET /api/v1/orgs/{org}/public_members/{username} | low | 0 | 0 |
| [ep-074](../endpoints/ep-074.md) | PUT /api/v1/orgs/{org}/public_members/{username} | low | 0 | 1 |
| [ep-075](../endpoints/ep-075.md) | DELETE /api/v1/orgs/{org}/public_members/{username} | low | 0 | 1 |
| [ep-077](../endpoints/ep-077.md) | GET /api/v1/orgs/{org}/hooks | low | 0 | 1 |
| [ep-078](../endpoints/ep-078.md) | GET /api/v1/orgs/{org}/hooks/{id} | low | 0 | 1 |
| [ep-079](../endpoints/ep-079.md) | POST /api/v1/orgs/{org}/hooks | low | 0 | 1 |
| [ep-080](../endpoints/ep-080.md) | PATCH /api/v1/orgs/{org}/hooks/{id} | low | 0 | 1 |
| [ep-081](../endpoints/ep-081.md) | DELETE /api/v1/orgs/{org}/hooks/{id} | low | 0 | 1 |
| [ep-082](../endpoints/ep-082.md) | GET /api/v1/orgs/{org}/labels | low | 0 | 1 |
| [ep-083](../endpoints/ep-083.md) | POST /api/v1/orgs/{org}/labels | low | 0 | 1 |
| [ep-084](../endpoints/ep-084.md) | GET /api/v1/orgs/{org}/labels/{id} | low | 0 | 0 |
| [ep-085](../endpoints/ep-085.md) | PATCH /api/v1/orgs/{org}/labels/{id} | low | 0 | 0 |
| [ep-086](../endpoints/ep-086.md) | DELETE /api/v1/orgs/{org}/labels/{id} | low | 0 | 1 |
| [ep-087](../endpoints/ep-087.md) | GET /api/v1/orgs/{org}/blocks | low | 0 | 0 |
| [ep-088](../endpoints/ep-088.md) | GET /api/v1/orgs/{org}/blocks/{username} | low | 0 | 0 |
| [ep-090](../endpoints/ep-090.md) | DELETE /api/v1/orgs/{org}/blocks/{username} | low | 0 | 1 |
| [ep-091](../endpoints/ep-091.md) | GET /api/v1/admin/hooks | low | 0 | 0 |
| [ep-092](../endpoints/ep-092.md) | GET /api/v1/admin/hooks/{id} | low | 0 | 0 |
| [ep-093](../endpoints/ep-093.md) | POST /api/v1/admin/hooks | low | 0 | 0 |
| [ep-094](../endpoints/ep-094.md) | PATCH /api/v1/admin/hooks/{id} | low | 0 | 1 |
| [ep-095](../endpoints/ep-095.md) | DELETE /api/v1/admin/hooks/{id} | low | 0 | 0 |
| [ep-096](../endpoints/ep-096.md) | POST /api/v1/admin/users/{username}/orgs | low | 0 | 0 |
| [ep-097](../endpoints/ep-097.md) | GET /api/v1/admin/orgs | low | 0 | 0 |
| [ep-101](../endpoints/ep-101.md) | POST /api/v1/admin/users/{username}/keys | low | 0 | 0 |
| [ep-102](../endpoints/ep-102.md) | DELETE /api/v1/admin/users/{username}/keys/{id} | low | 0 | 1 |
| [ep-103](../endpoints/ep-103.md) | GET /api/v1/admin/users | low | 0 | 0 |
| [ep-105](../endpoints/ep-105.md) | GET /api/v1/admin/actions/jobs | low | 0 | 0 |
| [ep-106](../endpoints/ep-106.md) | GET /api/v1/admin/actions/runs | low | 0 | 1 |
| [ep-111](../endpoints/ep-111.md) | POST /api/v1/admin/cron/{task} | low | 0 | 1 |
| [ep-113](../endpoints/ep-113.md) | POST /api/v1/admin/actions/runners/registration-token | low | 0 | 1 |
| [ep-114](../endpoints/ep-114.md) | GET /api/v1/admin/actions/runners | low | 0 | 1 |
| [ep-115](../endpoints/ep-115.md) | GET /api/v1/admin/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-116](../endpoints/ep-116.md) | DELETE /api/v1/admin/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-117](../endpoints/ep-117.md) | PATCH /api/v1/admin/actions/runners/{runner_id} | low | 0 | 2 |
| [ep-118](../endpoints/ep-118.md) | GET /api/v1/admin/emails | low | 0 | 1 |
| [ep-119](../endpoints/ep-119.md) | GET /api/v1/admin/emails/search | low | 0 | 1 |
| [ep-120](../endpoints/ep-120.md) | GET /api/v1/admin/users/{username}/badges | low | 0 | 1 |
| [ep-122](../endpoints/ep-122.md) | DELETE /api/v1/admin/users/{username}/badges | low | 0 | 1 |
| [ep-123](../endpoints/ep-123.md) | GET /api/v1/users/search | low | 1 | 1 |
| [ep-124](../endpoints/ep-124.md) | GET /api/v1/users/{username} | low | 1 | 0 |
| [ep-125](../endpoints/ep-125.md) | GET /api/v1/user | low | 0 | 0 |
| [ep-126](../endpoints/ep-126.md) | GET /api/v1/users/{username}/heatmap | low | 1 | 1 |
| [ep-129](../endpoints/ep-129.md) | DELETE /api/v1/user/avatar | low | 1 | 1 |
| [ep-130](../endpoints/ep-130.md) | PUT /api/v1/user/actions/secrets/{secretname} | low | 0 | 1 |
| [ep-131](../endpoints/ep-131.md) | DELETE /api/v1/user/actions/secrets/{secretname} | low | 0 | 0 |
| [ep-132](../endpoints/ep-132.md) | POST /api/v1/user/actions/variables/{variablename} | low | 0 | 1 |
| [ep-133](../endpoints/ep-133.md) | PUT /api/v1/user/actions/variables/{variablename} | low | 0 | 0 |
| [ep-134](../endpoints/ep-134.md) | DELETE /api/v1/user/actions/variables/{variablename} | low | 0 | 0 |
| [ep-135](../endpoints/ep-135.md) | GET /api/v1/user/actions/variables/{variablename} | low | 0 | 1 |
| [ep-136](../endpoints/ep-136.md) | GET /api/v1/user/actions/variables | low | 0 | 1 |
| [ep-137](../endpoints/ep-137.md) | GET /api/v1/user/actions/runs | low | 0 | 1 |
| [ep-138](../endpoints/ep-138.md) | GET /api/v1/user/actions/jobs | low | 0 | 1 |
| [ep-139](../endpoints/ep-139.md) | GET /api/v1/user/followers | low | 0 | 1 |
| [ep-140](../endpoints/ep-140.md) | GET /api/v1/users/{username}/followers | low | 0 | 1 |
| [ep-141](../endpoints/ep-141.md) | GET /api/v1/user/following | low | 0 | 1 |
| [ep-142](../endpoints/ep-142.md) | GET /api/v1/users/{username}/following | low | 0 | 1 |
| [ep-143](../endpoints/ep-143.md) | GET /api/v1/user/following/{username} | low | 0 | 1 |
| [ep-144](../endpoints/ep-144.md) | GET /api/v1/users/{username}/following/{target} | low | 0 | 1 |
| [ep-145](../endpoints/ep-145.md) | PUT /api/v1/user/following/{username} | low | 0 | 2 |
| [ep-146](../endpoints/ep-146.md) | DELETE /api/v1/user/following/{username} | low | 0 | 2 |
| [ep-147](../endpoints/ep-147.md) | GET /api/v1/user/hooks | low | 0 | 1 |
| [ep-148](../endpoints/ep-148.md) | GET /api/v1/user/hooks/{id} | low | 0 | 1 |
| [ep-149](../endpoints/ep-149.md) | POST /api/v1/user/hooks | low | 0 | 1 |
| [ep-150](../endpoints/ep-150.md) | PATCH /api/v1/user/hooks/{id} | low | 0 | 1 |
| [ep-151](../endpoints/ep-151.md) | DELETE /api/v1/user/hooks/{id} | low | 0 | 1 |
| [ep-154](../endpoints/ep-154.md) | GET /api/v1/user/starred/{owner}/{repo} | low | 0 | 0 |
| [ep-155](../endpoints/ep-155.md) | PUT /api/v1/user/starred/{owner}/{repo} | low | 0 | 1 |
| [ep-156](../endpoints/ep-156.md) | DELETE /api/v1/user/starred/{owner}/{repo} | low | 0 | 1 |
| [ep-157](../endpoints/ep-157.md) | GET /api/v1/user/keys | low | 0 | 0 |
| [ep-158](../endpoints/ep-158.md) | GET /api/v1/users/{username}/keys | low | 0 | 0 |
| [ep-159](../endpoints/ep-159.md) | GET /api/v1/user/keys/{id} | low | 0 | 0 |
| [ep-162](../endpoints/ep-162.md) | GET /api/v1/user/settings | low | 0 | 0 |
| [ep-163](../endpoints/ep-163.md) | PATCH /api/v1/user/settings | low | 0 | 1 |
| [ep-165](../endpoints/ep-165.md) | POST /api/v1/users/{username}/tokens | low | 0 | 1 |
| [ep-168](../endpoints/ep-168.md) | GET /api/v1/user/applications/oauth2 | low | 0 | 0 |
| [ep-169](../endpoints/ep-169.md) | DELETE /api/v1/user/applications/oauth2/{id} | low | 0 | 1 |
| [ep-172](../endpoints/ep-172.md) | GET /api/v1/users/{username}/repos | low | 0 | 1 |
| [ep-175](../endpoints/ep-175.md) | POST /api/v1/user/actions/runners/registration-token | low | 0 | 1 |
| [ep-176](../endpoints/ep-176.md) | GET /api/v1/user/actions/runners | low | 0 | 1 |
| [ep-177](../endpoints/ep-177.md) | GET /api/v1/user/actions/runners/{runner_id} | low | 0 | 0 |
| [ep-178](../endpoints/ep-178.md) | DELETE /api/v1/user/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-179](../endpoints/ep-179.md) | PATCH /api/v1/user/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-180](../endpoints/ep-180.md) | GET /api/v1/user/emails | low | 0 | 0 |
| [ep-183](../endpoints/ep-183.md) | GET /api/v1/users/{username}/gpg_keys | low | 0 | 0 |
| [ep-184](../endpoints/ep-184.md) | GET /api/v1/user/gpg_keys | low | 1 | 1 |
| [ep-185](../endpoints/ep-185.md) | GET /api/v1/user/gpg_keys/{id} | low | 1 | 1 |
| [ep-186](../endpoints/ep-186.md) | GET /api/v1/user/gpg_key_token | low | 0 | 1 |
| [ep-187](../endpoints/ep-187.md) | POST /api/v1/user/gpg_key_verify | low | 1 | 1 |
| [ep-188](../endpoints/ep-188.md) | POST /api/v1/user/gpg_keys | low | 1 | 2 |
| [ep-189](../endpoints/ep-189.md) | DELETE /api/v1/user/gpg_keys/{id} | low | 1 | 2 |
| [ep-190](../endpoints/ep-190.md) | GET /api/v1/user/blocks | low | 0 | 1 |
| [ep-191](../endpoints/ep-191.md) | GET /api/v1/user/blocks/{username} | low | 0 | 1 |
| [ep-193](../endpoints/ep-193.md) | DELETE /api/v1/user/blocks/{username} | low | 0 | 1 |
| [ep-196](../endpoints/ep-196.md) | GET /api/v1/repos/{owner}/{repo}/subscription | low | 0 | 1 |
| [ep-197](../endpoints/ep-197.md) | PUT /api/v1/repos/{owner}/{repo}/subscription | low | 0 | 2 |
| [ep-198](../endpoints/ep-198.md) | DELETE /api/v1/repos/{owner}/{repo}/subscription | low | 0 | 1 |
| [ep-199](../endpoints/ep-199.md) | GET /api/v1/packages/{owner} | low | 0 | 1 |
| [ep-200](../endpoints/ep-200.md) | GET /api/v1/packages/{owner}/{type}/{name}/{version} | low | 0 | 1 |
| [ep-203](../endpoints/ep-203.md) | GET /api/v1/packages/{owner}/{type}/{name}/{version}/files | low | 0 | 1 |
| [ep-204](../endpoints/ep-204.md) | GET /api/v1/packages/{owner}/{type}/{name} | low | 0 | 1 |
| [ep-205](../endpoints/ep-205.md) | GET /api/v1/packages/{owner}/{type}/{name}/-/latest | low | 0 | 1 |
| [ep-206](../endpoints/ep-206.md) | POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name} | low | 0 | 1 |
| [ep-207](../endpoints/ep-207.md) | POST /api/v1/packages/{owner}/{type}/{name}/-/unlink | low | 0 | 1 |
| [ep-208](../endpoints/ep-208.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | low | 0 | 1 |
| [ep-209](../endpoints/ep-209.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | low | 0 | 2 |
| [ep-210](../endpoints/ep-210.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies | low | 0 | 1 |
| [ep-211](../endpoints/ep-211.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | low | 0 | 1 |
| [ep-212](../endpoints/ep-212.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | low | 0 | 1 |
| [ep-213](../endpoints/ep-213.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks | low | 0 | 1 |
| [ep-214](../endpoints/ep-214.md) | GET /api/v1/repos/{owner}/{repo}/git/commits/{sha} | low | 0 | 1 |
| [ep-217](../endpoints/ep-217.md) | GET /api/v1/repos/{owner}/{repo}/commits/{sha}/pull | low | 0 | 1 |
| [ep-218](../endpoints/ep-218.md) | PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | low | 0 | 1 |
| [ep-219](../endpoints/ep-219.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user} | low | 0 | 1 |
| [ep-220](../endpoints/ep-220.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check | low | 0 | 0 |
| [ep-221](../endpoints/ep-221.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions | low | 0 | 0 |
| [ep-223](../endpoints/ep-223.md) | GET /api/v1/repos/{owner}/{repo}/pulls/{index} | low | 0 | 1 |
| [ep-229](../endpoints/ep-229.md) | POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge | low | 0 | 1 |
| [ep-230](../endpoints/ep-230.md) | POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update | low | 0 | 1 |
| [ep-231](../endpoints/ep-231.md) | DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge | low | 0 | 1 |
| [ep-232](../endpoints/ep-232.md) | GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits | low | 0 | 0 |
| [ep-234](../endpoints/ep-234.md) | POST /api/v1/repos/{owner}/{repo}/mirror-sync | low | 0 | 1 |
| [ep-236](../endpoints/ep-236.md) | GET /api/v1/repos/{owner}/{repo}/push_mirrors | low | 0 | 0 |
| [ep-237](../endpoints/ep-237.md) | GET /api/v1/repos/{owner}/{repo}/push_mirrors/{name} | low | 0 | 0 |
| [ep-242](../endpoints/ep-242.md) | GET /api/v1/repos/{owner}/{repo}/releases | low | 1 | 1 |
| [ep-245](../endpoints/ep-245.md) | DELETE /api/v1/repos/{owner}/{repo}/releases/{id} | low | 2 | 1 |
| [ep-246](../endpoints/ep-246.md) | GET /api/v1/repos/{owner}/{repo}/git/trees/{sha} | low | 0 | 1 |
| [ep-247](../endpoints/ep-247.md) | GET /api/v1/repos/{owner}/{repo}/git/refs | low | 0 | 0 |
| [ep-248](../endpoints/ep-248.md) | GET /api/v1/repos/{owner}/{repo}/git/refs/{ref} | low | 0 | 0 |
| [ep-250](../endpoints/ep-250.md) | GET /api/v1/repos/{owner}/{repo}/collaborators | low | 0 | 0 |
| [ep-251](../endpoints/ep-251.md) | GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | low | 0 | 0 |
| [ep-252](../endpoints/ep-252.md) | PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | low | 0 | 1 |
| [ep-253](../endpoints/ep-253.md) | DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator} | low | 0 | 2 |
| [ep-254](../endpoints/ep-254.md) | GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission | low | 1 | 1 |
| [ep-262](../endpoints/ep-262.md) | POST /api/v1/repos/{owner}/{repo}/avatar | low | 1 | 1 |
| [ep-265](../endpoints/ep-265.md) | PUT /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname} | low | 0 | 1 |
| [ep-269](../endpoints/ep-269.md) | POST /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | low | 0 | 1 |
| [ep-270](../endpoints/ep-270.md) | PUT /api/v1/repos/{owner}/{repo}/actions/variables/{variablename} | low | 0 | 1 |
| [ep-271](../endpoints/ep-271.md) | GET /api/v1/repos/{owner}/{repo}/actions/variables | low | 0 | 1 |
| [ep-272](../endpoints/ep-272.md) | POST /api/v1/repos/{owner}/{repo}/actions/runners/registration-token | low | 0 | 1 |
| [ep-273](../endpoints/ep-273.md) | GET /api/v1/repos/{owner}/{repo}/actions/runners | low | 0 | 1 |
| [ep-274](../endpoints/ep-274.md) | GET /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-275](../endpoints/ep-275.md) | DELETE /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-276](../endpoints/ep-276.md) | PATCH /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id} | low | 0 | 1 |
| [ep-277](../endpoints/ep-277.md) | GET /api/v1/repos/{owner}/{repo}/actions/jobs | low | 0 | 1 |
| [ep-278](../endpoints/ep-278.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs | low | 0 | 1 |
| [ep-279](../endpoints/ep-279.md) | GET /api/v1/repos/{owner}/{repo}/actions/tasks | low | 0 | 1 |
| [ep-280](../endpoints/ep-280.md) | GET /api/v1/repos/{owner}/{repo}/actions/workflows | low | 0 | 1 |
| [ep-281](../endpoints/ep-281.md) | GET /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id} | low | 0 | 0 |
| [ep-282](../endpoints/ep-282.md) | PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable | low | 0 | 1 |
| [ep-284](../endpoints/ep-284.md) | PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable | low | 0 | 1 |
| [ep-285](../endpoints/ep-285.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs/{run} | low | 0 | 0 |
| [ep-286](../endpoints/ep-286.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt} | low | 0 | 0 |
| [ep-290](../endpoints/ep-290.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs | low | 0 | 0 |
| [ep-291](../endpoints/ep-291.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs | low | 0 | 0 |
| [ep-292](../endpoints/ep-292.md) | GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id} | low | 0 | 0 |
| [ep-293](../endpoints/ep-293.md) | GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts | low | 1 | 1 |
| [ep-295](../endpoints/ep-295.md) | GET /api/v1/repos/{owner}/{repo}/actions/artifacts | low | 1 | 0 |
| [ep-296](../endpoints/ep-296.md) | GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | low | 1 | 0 |
| [ep-297](../endpoints/ep-297.md) | DELETE /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id} | low | 1 | 1 |
| [ep-299](../endpoints/ep-299.md) | GET /api/v1/repos/{owner}/{repo}/git/notes/{sha} | low | 0 | 1 |
| [ep-300](../endpoints/ep-300.md) | GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | low | 0 | 1 |
| [ep-301](../endpoints/ep-301.md) | POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | low | 0 | 1 |
| [ep-302](../endpoints/ep-302.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions | low | 0 | 1 |
| [ep-303](../endpoints/ep-303.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | low | 0 | 1 |
| [ep-304](../endpoints/ep-304.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | low | 0 | 1 |
| [ep-305](../endpoints/ep-305.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/reactions | low | 0 | 1 |
| [ep-306](../endpoints/ep-306.md) | GET /api/v1/repos/{owner}/{repo}/branches/{branch} | low | 0 | 0 |
| [ep-309](../endpoints/ep-309.md) | GET /api/v1/repos/{owner}/{repo}/branches | low | 0 | 1 |
| [ep-310](../endpoints/ep-310.md) | PUT /api/v1/repos/{owner}/{repo}/branches/{branch} | low | 0 | 1 |
| [ep-312](../endpoints/ep-312.md) | GET /api/v1/repos/{owner}/{repo}/branch_protections/{name} | low | 0 | 1 |
| [ep-313](../endpoints/ep-313.md) | GET /api/v1/repos/{owner}/{repo}/branch_protections | low | 0 | 1 |
| [ep-314](../endpoints/ep-314.md) | POST /api/v1/repos/{owner}/{repo}/branch_protections | low | 0 | 1 |
| [ep-316](../endpoints/ep-316.md) | DELETE /api/v1/repos/{owner}/{repo}/branch_protections/{name} | low | 0 | 1 |
| [ep-317](../endpoints/ep-317.md) | POST /api/v1/repos/{owner}/{repo}/branch_protections/priority | low | 0 | 1 |
| [ep-319](../endpoints/ep-319.md) | PUT /api/v1/repos/{owner}/{repo}/issues/{index}/lock | low | 0 | 0 |
| [ep-320](../endpoints/ep-320.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/lock | low | 0 | 0 |
| [ep-323](../endpoints/ep-323.md) | POST /api/v1/repos/{owner}/{repo}/hooks/{id}/tests | low | 0 | 2 |
| [ep-324](../endpoints/ep-324.md) | POST /api/v1/repos/{owner}/{repo}/hooks | low | 0 | 1 |
| [ep-325](../endpoints/ep-325.md) | PATCH /api/v1/repos/{owner}/{repo}/hooks/{id} | low | 0 | 1 |
| [ep-326](../endpoints/ep-326.md) | DELETE /api/v1/repos/{owner}/{repo}/hooks/{id} | low | 0 | 1 |
| [ep-327](../endpoints/ep-327.md) | GET /api/v1/repos/{owner}/{repo}/stargazers | low | 0 | 1 |
| [ep-328](../endpoints/ep-328.md) | GET /api/v1/repos/{owner}/{repo}/subscribers | low | 0 | 1 |
| [ep-329](../endpoints/ep-329.md) | GET /api/v1/repos/{owner}/{repo}/teams | low | 0 | 1 |
| [ep-330](../endpoints/ep-330.md) | GET /api/v1/repos/{owner}/{repo}/teams/{team} | low | 0 | 0 |
| [ep-331](../endpoints/ep-331.md) | PUT /api/v1/repos/{owner}/{repo}/teams/{team} | low | 0 | 1 |
| [ep-332](../endpoints/ep-332.md) | DELETE /api/v1/repos/{owner}/{repo}/teams/{team} | low | 0 | 1 |
| [ep-333](../endpoints/ep-333.md) | GET /api/v1/repos/{owner}/{repo}/forks | low | 0 | 0 |
| [ep-335](../endpoints/ep-335.md) | GET /api/v1/repos/{owner}/{repo}/issues/{index}/labels | low | 0 | 0 |
| [ep-336](../endpoints/ep-336.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels | low | 0 | 1 |
| [ep-337](../endpoints/ep-337.md) | DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id} | low | 0 | 1 |
| [ep-338](../endpoints/ep-338.md) | PUT /api/v1/repos/{owner}/{repo}/issues/{index}/labels | low | 0 | 1 |
| [ep-340](../endpoints/ep-340.md) | GET /api/v1/repos/{owner}/{repo}/keys | low | 0 | 1 |
| [ep-341](../endpoints/ep-341.md) | GET /api/v1/repos/{owner}/{repo}/keys/{id} | low | 0 | 0 |
| [ep-342](../endpoints/ep-342.md) | POST /api/v1/repos/{owner}/{repo}/keys | low | 0 | 1 |
| [ep-344](../endpoints/ep-344.md) | GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag} | low | 0 | 1 |
| [ep-346](../endpoints/ep-346.md) | GET /api/v1/repos/{owner}/{repo}/licenses | low | 0 | 1 |
| [ep-347](../endpoints/ep-347.md) | GET /api/v1/repos/{owner}/{repo}/topics | low | 0 | 1 |
| [ep-348](../endpoints/ep-348.md) | PUT /api/v1/repos/{owner}/{repo}/topics | low | 0 | 1 |
| [ep-349](../endpoints/ep-349.md) | PUT /api/v1/repos/{owner}/{repo}/topics/{topic} | low | 0 | 1 |
| [ep-350](../endpoints/ep-350.md) | DELETE /api/v1/repos/{owner}/{repo}/topics/{topic} | low | 0 | 1 |
| [ep-351](../endpoints/ep-351.md) | GET /api/v1/topics/search | low | 0 | 1 |
| [ep-356](../endpoints/ep-356.md) | DELETE /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id} | low | 1 | 1 |
| [ep-359](../endpoints/ep-359.md) | POST /api/v1/repos/{owner}/{repo}/labels | low | 0 | 0 |
| [ep-360](../endpoints/ep-360.md) | PATCH /api/v1/repos/{owner}/{repo}/labels/{id} | low | 0 | 0 |
| [ep-361](../endpoints/ep-361.md) | DELETE /api/v1/repos/{owner}/{repo}/labels/{id} | low | 0 | 1 |
| [ep-362](../endpoints/ep-362.md) | GET /api/v1/repos/search | low | 0 | 1 |
| [ep-367](../endpoints/ep-367.md) | GET /api/v1/repos/{owner}/{repo} | low | 0 | 1 |
| [ep-370](../endpoints/ep-370.md) | DELETE /api/v1/repos/{owner}/{repo} | low | 0 | 1 |
| [ep-374](../endpoints/ep-374.md) | GET /api/v1/repos/{owner}/{repo}/activities/feeds | low | 0 | 1 |
| [ep-376](../endpoints/ep-376.md) | POST /api/v1/repos/{owner}/{repo}/issues/{index}/pin | low | 0 | 1 |
| [ep-378](../endpoints/ep-378.md) | PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position} | low | 0 | 1 |
| [ep-380](../endpoints/ep-380.md) | GET /api/v1/repos/{owner}/{repo}/pulls/pinned | low | 0 | 1 |

## System-Level Assessment

- **Health Checks:** ✅ configured — Version endpoint serves as basic liveness. No dedicated readiness probe that checks DB connectivity.
- **Graceful Shutdown:** ✅ configured — Gitea uses graceful module (modules/graceful) for signal handling and request draining
- **Rate Limiting:** ❌ missing — No built-in API rate limiting. Relies on external reverse proxy.
- **Dead Letter Queues:** ❌ missing — Mirror queue has no DLQ - failed syncs are logged but not retried from queue

### Single Points of Failure

- ⚠️ GPG binary availability for signing key endpoints
- ⚠️ SQL database - all notification endpoints depend on it with no fallback
- ⚠️ Database (all endpoints depend on it)
- ⚠️ Database (single connection, no read replicas configured by default)
- ⚠️ Database - all endpoints depend on it with no caching layer
- ⚠️ database
- ⚠️ Database (single XORM connection)
- ⚠️ Database (single point for all operations)
- ⚠️ Database (single connection pool)
- ⚠️ Database - all endpoints depend solely on the database
- ⚠️ HaveIBeenPwned API (for user creation with PasswordCheckPwn=true)
- ⚠️ HaveIBeenPwned API for password validation (when enabled)
- ⚠️ Filesystem (RepoRootPath) for unadopted repo operations
- ⚠️ Database - all endpoints depend on DB availability
- ⚠️ Database (all endpoints depend on it with no fallback)
- ⚠️ Database (single instance unless externally replicated)
- ⚠️ Filesystem for authorized_keys file (mitigated by builtin SSH server option)
- ⚠️ Database (all write operations depend on it)
- ⚠️ Database (single instance unless configured with replication)
- ⚠️ Database
- ⚠️ Database - all endpoints depend on single DB connection
- ⚠️ Git storage (filesystem) - required for diff/patch and branch SHA resolution
- ⚠️ Git repository storage (local filesystem or NFS)
- ⚠️ Mirror queue (single instance, no redundancy unless backed by Redis)
- ⚠️ Database (single DB connection for all operations)
- ⚠️ Local git repository filesystem
- ⚠️ Object storage backend for attachments
- ⚠️ Object storage backend - no redundancy or fallback if storage is unavailable
- ⚠️ Database (single instance typical in small deployments)
- ⚠️ authorized_keys file - single file rewritten on every key change
- ⚠️ Object storage backend - no redundancy or fallback configured

### Cascading Failure Paths

- 🔗 Database down → all notification endpoints (ep-019 to ep-022) return errors → UI notification badge broken
- 🔗 ep-023 unbounded query can overload database, affecting all other endpoints sharing the connection pool
- 🔗 Database down → all 7 endpoints fail immediately
- 🔗 Storage backend down → ep-037/ep-038 fail, others unaffected
- 🔗 Database down → all 6 endpoints return 500
- 🔗 HaveIBeenPwned API down → ep-098 user creation fails with 400
- 🔗 HIBP API down → ep-099 password updates fail (when PASSWORD_CHECK_PWN enabled)
- 🔗 Database overload from ep-127 N+1 queries → connection pool exhaustion → all API endpoints fail
- 🔗 Database slow → ep-192 BlockUser transaction holds locks for extended time → other write operations blocked
- 🔗 Git storage slow → ep-222 list timeout → client retries → increased load
- 🔗 Git storage down → all PR create/merge/update/commits/files endpoints fail
- 🔗 Remote git server down → ep-235 blocks for full timeout × N mirrors → HTTP timeout for caller
- 🔗 Database down → all release endpoints fail
- 🔗 Git repository filesystem unavailable → create/edit/delete fail, reads still work from DB
- 🔗 Storage down → ep-259 upload fails → users cannot attach files to issues
- 🔗 Storage down → ep-261 delete partially fails → orphaned files accumulate
- 🔗 Storage outage → ep-298 download fails → CI/CD pipelines that depend on artifact downloads break
- 🔗 Many concurrent fork requests → disk I/O saturation → all git operations slow down
- 🔗 SSHOpLocker contention → all key operations blocked during rewrite
- 🔗 Storage down → ep-354 upload fails → users cannot attach files to releases


--- FILE: modules/routers.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# routers

**475 endpoints** · Go · go-chi/chi v5 + XORM

## Dependencies

| Client | Target Module |
|--------|---------------|
| actions_service | [services](services.md) |
| asymkey_service | [services](services.md) |
| attachment_service | [services](services.md) |
| createTag | [services](services.md) |
| git | [modules](modules.md) |
| gitrepo | [modules](modules.md) |
| mailer | [services](services.md) |
| mirror_service | [services](services.md) |
| password | [modules](modules.md) |
| pull | [services](services.md) |
| release_service | [services](services.md) |
| repo_model | [models](models.md) |
| repo_service | [services](services.md) |
| storage | [modules](modules.md) |
| user_service | [services](services.md) |

## Endpoints

### admin

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/admin/actions/jobs](../endpoints/ep-105.md) | List all workflow jobs across all repositories (admin only) |
| GET | [/api/v1/admin/actions/runners](../endpoints/ep-114.md) | List all global action runners with optional disabled filter |
| POST | [/api/v1/admin/actions/runners/registration-token](../endpoints/ep-113.md) | Gets or creates a global actions runner registration token |
| GET | [/api/v1/admin/actions/runners/{runner_id}](../endpoints/ep-115.md) | Get a specific global action runner by ID |
| DELETE | [/api/v1/admin/actions/runners/{runner_id}](../endpoints/ep-116.md) | Delete a global action runner by ID |
| PATCH | [/api/v1/admin/actions/runners/{runner_id}](../endpoints/ep-117.md) | Update a global action runner (currently only disable/enable) |
| GET | [/api/v1/admin/actions/runs](../endpoints/ep-106.md) | Lists all workflow runs across all repositories (admin-level) |
| GET | [/api/v1/admin/cron](../endpoints/ep-110.md) | Lists all registered cron tasks with their schedule and execution info |
| POST | [/api/v1/admin/cron/{task}](../endpoints/ep-111.md) | Triggers a cron task to run immediately |
| GET | [/api/v1/admin/emails](../endpoints/ep-118.md) | List all email addresses in the system with pagination |
| GET | [/api/v1/admin/emails/search](../endpoints/ep-119.md) | Search all emails by keyword (searches name, full_name, email) |
| GET | [/api/v1/admin/hooks](../endpoints/ep-091.md) | List system and/or default webhooks with pagination |
| POST | [/api/v1/admin/hooks](../endpoints/ep-093.md) | Create a new system or default webhook |
| GET | [/api/v1/admin/hooks/{id}](../endpoints/ep-092.md) | Get a single system or default webhook by ID |
| PATCH | [/api/v1/admin/hooks/{id}](../endpoints/ep-094.md) | Update an existing system or default webhook |
| DELETE | [/api/v1/admin/hooks/{id}](../endpoints/ep-095.md) | Delete a system or default webhook and its associated hook tasks |
| GET | [/api/v1/admin/orgs](../endpoints/ep-097.md) | List all organizations with pagination |
| GET | [/api/v1/admin/unadopted](../endpoints/ep-107.md) | Lists unadopted repositories (git repos on disk not tracked in DB) |
| POST | [/api/v1/admin/unadopted/{owner}/{repo}](../endpoints/ep-108.md) | Adopts unadopted files on disk as a repository tracked in the database |
| DELETE | [/api/v1/admin/unadopted/{owner}/{repo}](../endpoints/ep-109.md) | Deletes unadopted repository files from the filesystem |
| POST | [/api/v1/admin/users](../endpoints/ep-098.md) | Create a new user account (admin only) |
| GET | [/api/v1/admin/users](../endpoints/ep-103.md) | Search users with various filter conditions (admin only) |
| PATCH | [/api/v1/admin/users/{username}](../endpoints/ep-099.md) | Edit an existing user's profile, auth, and permission settings |
| DELETE | [/api/v1/admin/users/{username}](../endpoints/ep-100.md) | Delete a user account, optionally purging all owned data |
| GET | [/api/v1/admin/users/{username}/badges](../endpoints/ep-120.md) | List all badges belonging to a user |
| POST | [/api/v1/admin/users/{username}/badges](../endpoints/ep-121.md) | Add badges to a user by slug |
| DELETE | [/api/v1/admin/users/{username}/badges](../endpoints/ep-122.md) | Remove badges from a user by slug |
| POST | [/api/v1/admin/users/{username}/keys](../endpoints/ep-101.md) | Add a public SSH key on behalf of a user |
| DELETE | [/api/v1/admin/users/{username}/keys/{id}](../endpoints/ep-102.md) | Delete a user's public SSH key |
| POST | [/api/v1/admin/users/{username}/orgs](../endpoints/ep-096.md) | Create an organization owned by the specified user |
| POST | [/api/v1/admin/users/{username}/rename](../endpoints/ep-104.md) | Rename a user account |
| POST | [/api/v1/admin/users/{username}/repos](../endpoints/ep-112.md) | Creates a repository on behalf of a user (admin only) |

### issue

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/repos/issues/search](../endpoints/ep-469.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues](../endpoints/ep-470.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues](../endpoints/ep-472.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/comments](../endpoints/ep-437.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}](../endpoints/ep-439.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}](../endpoints/ep-440.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}](../endpoints/ep-442.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets](../endpoints/ep-425.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets](../endpoints/ep-426.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}](../endpoints/ep-424.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}](../endpoints/ep-427.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}](../endpoints/ep-428.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions](../endpoints/ep-300.md) | Get a list of reactions from a comment of an issue |
| POST | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions](../endpoints/ep-301.md) | Add a reaction to a comment of an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions](../endpoints/ep-302.md) | Remove a reaction from a comment of an issue |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}](../endpoints/ep-471.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/{index}](../endpoints/ep-473.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}](../endpoints/ep-474.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/assets](../endpoints/ep-258.md) | List all attachments of an issue |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/assets](../endpoints/ep-259.md) | Create an issue attachment by uploading a file |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}](../endpoints/ep-257.md) | Get a single issue attachment |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}](../endpoints/ep-260.md) | Edit an issue attachment (rename) |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}](../endpoints/ep-261.md) | Delete an issue attachment |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/blocks](../endpoints/ep-211.md) | List issues that are blocked by this issue (issues this issue blocks) |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/blocks](../endpoints/ep-212.md) | Block the issue given in the body by the issue in the URL path |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/blocks](../endpoints/ep-213.md) | Unblock the issue given in the body by the issue in the URL path |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/comments](../endpoints/ep-435.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/comments](../endpoints/ep-438.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}](../endpoints/ep-441.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}](../endpoints/ep-443.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/deadline](../endpoints/ep-475.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies](../endpoints/ep-208.md) | List issues that block the given issue (its dependencies) |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies](../endpoints/ep-209.md) | Make the issue in the URL depend on the issue specified in the body |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/dependencies](../endpoints/ep-210.md) | Remove a dependency from the issue in the URL |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/labels](../endpoints/ep-335.md) | Get an issue's labels |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/labels](../endpoints/ep-336.md) | Add labels to an issue |
| PUT | [/api/v1/repos/{owner}/{repo}/issues/{index}/labels](../endpoints/ep-338.md) | Replace all labels on an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/labels](../endpoints/ep-339.md) | Remove all labels from an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}](../endpoints/ep-337.md) | Remove a label from an issue |
| PUT | [/api/v1/repos/{owner}/{repo}/issues/{index}/lock](../endpoints/ep-319.md) | Lock an issue to restrict commenting to users with write access |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/lock](../endpoints/ep-320.md) | Unlock a previously locked issue |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/pin](../endpoints/ep-376.md) | Pin an issue to the repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/pin](../endpoints/ep-377.md) | Unpin an issue from the repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position}](../endpoints/ep-378.md) | Move a pinned issue to a new position |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/reactions](../endpoints/ep-303.md) | Get a list of reactions of an issue |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/reactions](../endpoints/ep-304.md) | Add a reaction to an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/reactions](../endpoints/ep-305.md) | Remove a reaction from an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete](../endpoints/ep-384.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start](../endpoints/ep-382.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop](../endpoints/ep-383.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions](../endpoints/ep-221.md) | Get users who subscribed to an issue |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check](../endpoints/ep-220.md) | Check if the authenticated user is subscribed to an issue |
| PUT | [/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}](../endpoints/ep-218.md) | Subscribe a user to an issue |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}](../endpoints/ep-219.md) | Unsubscribe a user from an issue |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/timeline](../endpoints/ep-436.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/issues/{index}/times](../endpoints/ep-407.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/issues/{index}/times](../endpoints/ep-408.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/times](../endpoints/ep-409.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/issues/{index}/times/{id}](../endpoints/ep-410.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/labels](../endpoints/ep-357.md) | Get all labels of a repository with pagination |
| POST | [/api/v1/repos/{owner}/{repo}/labels](../endpoints/ep-359.md) | Create a label for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/labels/{id}](../endpoints/ep-358.md) | Get a single label by ID or name |
| PATCH | [/api/v1/repos/{owner}/{repo}/labels/{id}](../endpoints/ep-360.md) | Update a label for a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/labels/{id}](../endpoints/ep-361.md) | Delete a label from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/milestones](../endpoints/ep-464.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/milestones](../endpoints/ep-466.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/milestones/{id}](../endpoints/ep-465.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/milestones/{id}](../endpoints/ep-467.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/milestones/{id}](../endpoints/ep-468.md) |  |

### miscellaneous

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/gitignore/templates](../endpoints/ep-011.md) | Returns a list of all gitignore template names |
| GET | [/api/v1/gitignore/templates/{name}](../endpoints/ep-012.md) | Returns information about a specific gitignore template |
| GET | [/api/v1/label/templates](../endpoints/ep-002.md) | Returns a list of all label template display names |
| GET | [/api/v1/label/templates/{name}](../endpoints/ep-003.md) | Returns all labels in a specific label template |
| GET | [/api/v1/licenses](../endpoints/ep-013.md) | Returns a list of all license templates with metadata |
| GET | [/api/v1/licenses/{name}](../endpoints/ep-014.md) | Returns full information about a specific license template including body text |
| POST | [/api/v1/markdown](../endpoints/ep-009.md) | Render a markdown document as HTML |
| POST | [/api/v1/markdown/raw](../endpoints/ep-010.md) | Render raw markdown as HTML (no special link handling) |
| POST | [/api/v1/markup](../endpoints/ep-008.md) | Renders a markup document as HTML supporting multiple modes (markdown, comment, wiki, file, gfm) |
| GET | [/api/v1/signing-key.gpg](../endpoints/ep-004.md) | Returns the GPG public key of the default signing key |
| GET | [/api/v1/signing-key.pub](../endpoints/ep-006.md) | Returns the SSH public key of the default signing key |
| GET | [/api/v1/version](../endpoints/ep-001.md) | Returns the version of the Gitea application |

### notification

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/notifications](../endpoints/ep-019.md) | List current user's notification threads with filtering by status, subject type, and time range |
| PUT | [/api/v1/notifications](../endpoints/ep-020.md) | Mark notification threads as read, unread, or pinned for the current user |
| GET | [/api/v1/notifications/new](../endpoints/ep-021.md) | Check if unread notifications exist and return the count |
| GET | [/api/v1/notifications/threads/{id}](../endpoints/ep-024.md) | Get notification thread by ID |
| PATCH | [/api/v1/notifications/threads/{id}](../endpoints/ep-025.md) | Mark notification thread as read by ID |
| GET | [/api/v1/repos/{owner}/{repo}/notifications](../endpoints/ep-022.md) | List current user's notification threads for a specific repository |
| PUT | [/api/v1/repos/{owner}/{repo}/notifications](../endpoints/ep-023.md) | Mark notification threads as read, pinned or unread on a specific repo |

### organization

| Method | Path | Description |
|--------|------|-------------|
| POST | [/api/v1/org/{org}/repos](../endpoints/ep-365.md) | Create a repository in an organization (deprecated) |
| GET | [/api/v1/orgs](../endpoints/ep-029.md) | Get list of all organizations visible to the current user |
| POST | [/api/v1/orgs](../endpoints/ep-030.md) | Create a new organization |
| GET | [/api/v1/orgs/{org}](../endpoints/ep-031.md) | Get details of a specific organization |
| PATCH | [/api/v1/orgs/{org}](../endpoints/ep-033.md) | Edit an organization's information |
| DELETE | [/api/v1/orgs/{org}](../endpoints/ep-034.md) | Delete an organization |
| GET | [/api/v1/orgs/{org}/actions/jobs](../endpoints/ep-052.md) | Get org-level workflow jobs |
| GET | [/api/v1/orgs/{org}/actions/runners](../endpoints/ep-048.md) | Get org-level runners list |
| POST | [/api/v1/orgs/{org}/actions/runners/registration-token](../endpoints/ep-042.md) | Get an organization's actions runner registration token |
| GET | [/api/v1/orgs/{org}/actions/runners/{runner_id}](../endpoints/ep-049.md) | Get a specific org-level runner by ID |
| DELETE | [/api/v1/orgs/{org}/actions/runners/{runner_id}](../endpoints/ep-050.md) | Delete an org-level runner |
| PATCH | [/api/v1/orgs/{org}/actions/runners/{runner_id}](../endpoints/ep-051.md) | Update an org-level runner (enable/disable) |
| GET | [/api/v1/orgs/{org}/actions/runs](../endpoints/ep-053.md) | Get org-level workflow runs |
| GET | [/api/v1/orgs/{org}/actions/secrets](../endpoints/ep-039.md) | List an organization's actions secrets |
| PUT | [/api/v1/orgs/{org}/actions/secrets/{secretname}](../endpoints/ep-040.md) | Create or update a secret value in an organization |
| DELETE | [/api/v1/orgs/{org}/actions/secrets/{secretname}](../endpoints/ep-041.md) | Delete a secret in an organization |
| GET | [/api/v1/orgs/{org}/actions/variables](../endpoints/ep-043.md) | Get an org-level variables list |
| GET | [/api/v1/orgs/{org}/actions/variables/{variablename}](../endpoints/ep-044.md) | Get an org-level variable by name |
| DELETE | [/api/v1/orgs/{org}/actions/variables/{variablename}](../endpoints/ep-045.md) | Delete an org-level variable by name |
| POST | [/api/v1/orgs/{org}/actions/variables/{variablename}](../endpoints/ep-046.md) | Create an org-level variable |
| PUT | [/api/v1/orgs/{org}/actions/variables/{variablename}](../endpoints/ep-047.md) | Update an org-level variable |
| GET | [/api/v1/orgs/{org}/activities/feeds](../endpoints/ep-035.md) | List an organization's activity feeds |
| POST | [/api/v1/orgs/{org}/avatar](../endpoints/ep-037.md) | Update the avatar of an organization |
| DELETE | [/api/v1/orgs/{org}/avatar](../endpoints/ep-038.md) | Delete the avatar of an organization |
| GET | [/api/v1/orgs/{org}/blocks](../endpoints/ep-087.md) | List users blocked by the organization |
| GET | [/api/v1/orgs/{org}/blocks/{username}](../endpoints/ep-088.md) | Check if a user is blocked by the organization |
| PUT | [/api/v1/orgs/{org}/blocks/{username}](../endpoints/ep-089.md) | Block a user from the organization |
| DELETE | [/api/v1/orgs/{org}/blocks/{username}](../endpoints/ep-090.md) | Unblock a user from the organization |
| GET | [/api/v1/orgs/{org}/hooks](../endpoints/ep-077.md) | List an organization's webhooks |
| POST | [/api/v1/orgs/{org}/hooks](../endpoints/ep-079.md) | Create a webhook for an organization |
| GET | [/api/v1/orgs/{org}/hooks/{id}](../endpoints/ep-078.md) | Get a single organization webhook by ID |
| PATCH | [/api/v1/orgs/{org}/hooks/{id}](../endpoints/ep-080.md) | Update an organization webhook |
| DELETE | [/api/v1/orgs/{org}/hooks/{id}](../endpoints/ep-081.md) | Delete an organization webhook |
| GET | [/api/v1/orgs/{org}/labels](../endpoints/ep-082.md) | List an organization's labels |
| POST | [/api/v1/orgs/{org}/labels](../endpoints/ep-083.md) | Create a label for an organization |
| GET | [/api/v1/orgs/{org}/labels/{id}](../endpoints/ep-084.md) | Get a single label by ID or name in an organization |
| PATCH | [/api/v1/orgs/{org}/labels/{id}](../endpoints/ep-085.md) | Update a label in an organization |
| DELETE | [/api/v1/orgs/{org}/labels/{id}](../endpoints/ep-086.md) | Delete a label from an organization |
| GET | [/api/v1/orgs/{org}/members](../endpoints/ep-070.md) | List an organization's members. If the doer is a member or admin, shows all members; otherwise shows only public members. |
| GET | [/api/v1/orgs/{org}/members/{username}](../endpoints/ep-072.md) | Check if a user is a member of an organization. Returns 204 if member, 303 redirect to public_members check if doer is not a member/admin, 404 if not a member. |
| DELETE | [/api/v1/orgs/{org}/members/{username}](../endpoints/ep-076.md) | Remove a member from an organization. Removes from all teams, deletes repo access, unwatches repos. |
| GET | [/api/v1/orgs/{org}/public_members](../endpoints/ep-071.md) | List an organization's public members. Always shows only public members regardless of authentication. |
| GET | [/api/v1/orgs/{org}/public_members/{username}](../endpoints/ep-073.md) | Check if a user is a public member of an organization. Returns 204 if public member, 404 otherwise. |
| PUT | [/api/v1/orgs/{org}/public_members/{username}](../endpoints/ep-074.md) | Publicize a user's membership in an organization. Sets is_public=true on the org_user record. |
| DELETE | [/api/v1/orgs/{org}/public_members/{username}](../endpoints/ep-075.md) | Conceal a user's membership in an organization. Sets is_public=false on the org_user record. |
| POST | [/api/v1/orgs/{org}/rename](../endpoints/ep-032.md) | Rename an organization |
| DELETE | [/api/v1/orgs/{org}/repos](../endpoints/ep-036.md) | Delete all repositories in an organization (async background deletion) |
| GET | [/api/v1/orgs/{org}/repos](../endpoints/ep-174.md) | List an organization's repos |
| POST | [/api/v1/orgs/{org}/repos](../endpoints/ep-366.md) | Create a repository in an organization |
| GET | [/api/v1/orgs/{org}/teams](../endpoints/ep-054.md) | List an organization's teams |
| POST | [/api/v1/orgs/{org}/teams](../endpoints/ep-057.md) | Create a team in an organization |
| GET | [/api/v1/orgs/{org}/teams/search](../endpoints/ep-068.md) | Search for teams within an organization |
| GET | [/api/v1/teams/{id}](../endpoints/ep-056.md) | Get a team by its ID |
| PATCH | [/api/v1/teams/{id}](../endpoints/ep-058.md) | Edit a team |
| DELETE | [/api/v1/teams/{id}](../endpoints/ep-059.md) | Delete a team |
| GET | [/api/v1/teams/{id}/activities/feeds](../endpoints/ep-069.md) | List a team's activity feeds |
| GET | [/api/v1/teams/{id}/members](../endpoints/ep-060.md) | List a team's members |
| GET | [/api/v1/teams/{id}/members/{username}](../endpoints/ep-061.md) | Get a particular member of a team |
| PUT | [/api/v1/teams/{id}/members/{username}](../endpoints/ep-062.md) | Add a team member |
| DELETE | [/api/v1/teams/{id}/members/{username}](../endpoints/ep-063.md) | Remove a team member |
| GET | [/api/v1/teams/{id}/repos](../endpoints/ep-064.md) | List all repositories belonging to a team |
| GET | [/api/v1/teams/{id}/repos/{org}/{repo}](../endpoints/ep-065.md) | Get a particular repository of a team |
| PUT | [/api/v1/teams/{id}/repos/{org}/{repo}](../endpoints/ep-066.md) | Add a repository to a team |
| DELETE | [/api/v1/teams/{id}/repos/{org}/{repo}](../endpoints/ep-067.md) | Remove a repository from a team (does not delete the repository) |
| GET | [/api/v1/user/orgs](../endpoints/ep-026.md) | List the current user's organizations |
| GET | [/api/v1/users/{username}/orgs](../endpoints/ep-027.md) | List a user's organizations |
| GET | [/api/v1/users/{username}/orgs/{org}/permissions](../endpoints/ep-028.md) | Get user permissions in organization |

### package

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/packages/{owner}](../endpoints/ep-199.md) | Gets all packages of an owner |
| DELETE | [/api/v1/packages/{owner}/{type}/{name}](../endpoints/ep-201.md) | Delete a package and all its versions |
| GET | [/api/v1/packages/{owner}/{type}/{name}](../endpoints/ep-204.md) | Gets all versions of a specific package |
| GET | [/api/v1/packages/{owner}/{type}/{name}/-/latest](../endpoints/ep-205.md) | Gets the latest version of a package |
| POST | [/api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}](../endpoints/ep-206.md) | Link a package to a repository |
| POST | [/api/v1/packages/{owner}/{type}/{name}/-/unlink](../endpoints/ep-207.md) | Unlink a package from its repository |
| GET | [/api/v1/packages/{owner}/{type}/{name}/{version}](../endpoints/ep-200.md) | Gets a specific package version |
| DELETE | [/api/v1/packages/{owner}/{type}/{name}/{version}](../endpoints/ep-202.md) | Delete a specific version of a package |
| GET | [/api/v1/packages/{owner}/{type}/{name}/{version}/files](../endpoints/ep-203.md) | Gets all files of a specific package version |

### repository

| Method | Path | Description |
|--------|------|-------------|
| POST | [/api/v1/repos/migrate](../endpoints/ep-444.md) |  |
| GET | [/api/v1/repos/search](../endpoints/ep-362.md) | Search for repositories |
| GET | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-367.md) | Get a repository by owner and name |
| PATCH | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-369.md) | Edit a repository's properties. Only fields that are set will be changed. |
| DELETE | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-370.md) | Delete a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts](../endpoints/ep-295.md) | Lists all artifacts for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}](../endpoints/ep-296.md) | Gets a specific artifact by ID for a workflow run (v4 only) |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}](../endpoints/ep-297.md) | Marks a specific artifact for deletion (v4 only) |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip](../endpoints/ep-298.md) | Downloads a specific artifact, redirecting to blob URL or serving directly |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs](../endpoints/ep-277.md) | Lists all jobs for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}](../endpoints/ep-292.md) | Gets a specific workflow job for a workflow run |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs](../endpoints/ep-403.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runners](../endpoints/ep-273.md) | Get repo-level runners |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runners/registration-token](../endpoints/ep-272.md) | Get a repository's actions runner registration token |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-274.md) | Get a repo-level runner |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-275.md) | Delete a repo-level runner |
| PATCH | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-276.md) | Update a repo-level runner (enable/disable) |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs](../endpoints/ep-278.md) | Lists all runs for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}](../endpoints/ep-285.md) | Gets a specific workflow run by ID |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}](../endpoints/ep-294.md) | Deletes a workflow run including all logs and artifacts |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts](../endpoints/ep-293.md) | Lists all artifacts for a specific workflow run in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}](../endpoints/ep-286.md) | Gets a specific workflow run attempt by run ID and attempt number |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs](../endpoints/ep-291.md) | Lists all jobs for a specific workflow run attempt |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs](../endpoints/ep-290.md) | Lists all jobs for a workflow run (latest attempt) |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun](../endpoints/ep-289.md) | Reruns a specific workflow job in a run |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun](../endpoints/ep-287.md) | Reruns an entire workflow run creating a new attempt |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs](../endpoints/ep-288.md) | Reruns all failed or cancelled jobs in a workflow run |
| GET | [/api/v1/repos/{owner}/{repo}/actions/secrets](../endpoints/ep-264.md) | List repository actions secrets (names only, not values) |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}](../endpoints/ep-265.md) | Create or update a secret value in a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}](../endpoints/ep-266.md) | Delete a secret in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/tasks](../endpoints/ep-279.md) | List a repository's action tasks |
| GET | [/api/v1/repos/{owner}/{repo}/actions/variables](../endpoints/ep-271.md) | Get repo-level variables list |
| GET | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-267.md) | Get a repo-level variable by name |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-268.md) | Delete a repo-level variable by name |
| POST | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-269.md) | Create a repo-level variable |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-270.md) | Update a repo-level variable |
| GET | [/api/v1/repos/{owner}/{repo}/actions/workflows](../endpoints/ep-280.md) | List repository workflows from default branch |
| GET | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}](../endpoints/ep-281.md) | Get a specific workflow by ID (filename) |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable](../endpoints/ep-282.md) | Disable a workflow |
| POST | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches](../endpoints/ep-283.md) | Create a workflow dispatch event to trigger a workflow run |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable](../endpoints/ep-284.md) | Enable a workflow |
| GET | [/api/v1/repos/{owner}/{repo}/activities/feeds](../endpoints/ep-374.md) | List a repository's activity feeds |
| GET | [/api/v1/repos/{owner}/{repo}/archive/{archive}](../endpoints/ep-392.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/assignees](../endpoints/ep-256.md) | Return all users that have write access and can be assigned to issues |
| POST | [/api/v1/repos/{owner}/{repo}/avatar](../endpoints/ep-262.md) | Update repository avatar image |
| DELETE | [/api/v1/repos/{owner}/{repo}/avatar](../endpoints/ep-263.md) | Delete repository custom avatar |
| GET | [/api/v1/repos/{owner}/{repo}/branch_protections](../endpoints/ep-313.md) | List all branch protection rules for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/branch_protections](../endpoints/ep-314.md) | Create a branch protection rule for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/branch_protections/priority](../endpoints/ep-317.md) | Update the priorities of branch protection rules for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-312.md) | Get a specific branch protection rule for the repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-315.md) | Edit a branch protection rule for a repository. Only fields that are set will be changed |
| DELETE | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-316.md) | Delete a specific branch protection rule for the repository |
| POST | [/api/v1/repos/{owner}/{repo}/branches](../endpoints/ep-308.md) | Create a new branch in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/branches](../endpoints/ep-309.md) | List a repository's branches with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-306.md) | Retrieve a specific branch from a repository, including its effective branch protection |
| DELETE | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-307.md) | Delete a specific branch from a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-310.md) | Update a branch reference to a new commit |
| PATCH | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-311.md) | Rename a branch in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators](../endpoints/ep-250.md) | List all collaborators of a repository with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-251.md) | Check if a user is a collaborator of a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-252.md) | Add or update a collaborator to a repository with specified permission level |
| DELETE | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-253.md) | Remove a collaborator from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission](../endpoints/ep-254.md) | Get repository permissions for a user |
| GET | [/api/v1/repos/{owner}/{repo}/commits](../endpoints/ep-215.md) | Get a list of all commits from a repository with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{ref}/status](../endpoints/ep-432.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{ref}/statuses](../endpoints/ep-431.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{sha}/pull](../endpoints/ep-217.md) | Get the merged pull request associated with a commit SHA |
| GET | [/api/v1/repos/{owner}/{repo}/compare/{basehead}](../endpoints/ep-434.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/contents](../endpoints/ep-394.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents](../endpoints/ep-400.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents-ext/{filepath}](../endpoints/ep-398.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-395.md) |  |
| PUT | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-396.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-397.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-399.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/diffpatch](../endpoints/ep-249.md) | Apply a diff patch to the repository, creating a new commit |
| GET | [/api/v1/repos/{owner}/{repo}/editorconfig/{filepath}](../endpoints/ep-393.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/file-contents](../endpoints/ep-401.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/file-contents](../endpoints/ep-402.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/forks](../endpoints/ep-333.md) | List a repository's forks |
| POST | [/api/v1/repos/{owner}/{repo}/forks](../endpoints/ep-334.md) | Fork a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/blobs/{sha}](../endpoints/ep-433.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/git/commits/{sha}](../endpoints/ep-214.md) | Get a single commit from a repository by SHA or ref |
| GET | [/api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}](../endpoints/ep-216.md) | Get a commit's diff or patch output as plain text |
| GET | [/api/v1/repos/{owner}/{repo}/git/notes/{sha}](../endpoints/ep-299.md) | Get a note corresponding to a single commit from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/refs](../endpoints/ep-247.md) | List all git references (branches, tags) of a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/refs/{ref}](../endpoints/ep-248.md) | Get specified ref or filtered list of refs by prefix |
| GET | [/api/v1/repos/{owner}/{repo}/git/tags/{sha}](../endpoints/ep-415.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/git/trees/{sha}](../endpoints/ep-246.md) | Gets the tree of a repository by SHA hash with pagination support |
| GET | [/api/v1/repos/{owner}/{repo}/hooks](../endpoints/ep-321.md) | List all webhooks configured for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/hooks](../endpoints/ep-324.md) | Create a webhook for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/git](../endpoints/ep-386.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-387.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-388.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-389.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-322.md) | Get a specific webhook by ID for a repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-325.md) | Edit a webhook in a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-326.md) | Delete a webhook from a repository |
| POST | [/api/v1/repos/{owner}/{repo}/hooks/{id}/tests](../endpoints/ep-323.md) | Test a push webhook by sending a test push payload |
| GET | [/api/v1/repos/{owner}/{repo}/issue_config](../endpoints/ep-372.md) | Returns the issue config for a repo |
| GET | [/api/v1/repos/{owner}/{repo}/issue_config/validate](../endpoints/ep-373.md) | Returns validation information for the issue config |
| GET | [/api/v1/repos/{owner}/{repo}/issue_templates](../endpoints/ep-371.md) | Get available issue templates for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/issues/pinned](../endpoints/ep-379.md) | List a repository's pinned issues (non-pull requests) |
| GET | [/api/v1/repos/{owner}/{repo}/keys](../endpoints/ep-340.md) | List a repository's deploy keys |
| POST | [/api/v1/repos/{owner}/{repo}/keys](../endpoints/ep-342.md) | Add a deploy key to a repository |
| GET | [/api/v1/repos/{owner}/{repo}/keys/{id}](../endpoints/ep-341.md) | Get a repository's deploy key by id |
| DELETE | [/api/v1/repos/{owner}/{repo}/keys/{id}](../endpoints/ep-343.md) | Delete a deploy key from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/languages](../endpoints/ep-375.md) | Get languages and number of bytes of code written in the repository |
| GET | [/api/v1/repos/{owner}/{repo}/licenses](../endpoints/ep-346.md) | Get the detected licenses for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/media/{filepath}](../endpoints/ep-391.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/merge-upstream](../endpoints/ep-318.md) | Merge a branch from the upstream (base) repository into the fork |
| POST | [/api/v1/repos/{owner}/{repo}/mirror-sync](../endpoints/ep-234.md) | Adds a mirrored (pull) repository to the sync queue |
| GET | [/api/v1/repos/{owner}/{repo}/new_pin_allowed](../endpoints/ep-381.md) | Returns whether new issue/PR pins are allowed (based on max pin limit) |
| GET | [/api/v1/repos/{owner}/{repo}/pulls](../endpoints/ep-222.md) | List a repo's pull requests with filtering and pagination |
| POST | [/api/v1/repos/{owner}/{repo}/pulls](../endpoints/ep-226.md) | Create a new pull request |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/comments/{id}/resolve](../endpoints/ep-455.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/comments/{id}/unresolve](../endpoints/ep-456.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/pinned](../endpoints/ep-380.md) | List a repository's pinned pull requests |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{base}/{head}](../endpoints/ep-224.md) | Get a pull request by base and head branch references |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}](../endpoints/ep-223.md) | Get a single pull request by index |
| PATCH | [/api/v1/repos/{owner}/{repo}/pulls/{index}](../endpoints/ep-227.md) | Update a pull request (title, body, assignees, labels, milestone, state, base branch, deadline, allow_maintainer_edit) |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}](../endpoints/ep-225.md) | Get a pull request diff or patch file |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies](../endpoints/ep-454.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/commits](../endpoints/ep-232.md) | Get commits for a pull request |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/files](../endpoints/ep-233.md) | Get changed files for a pull request |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-228.md) | Check if a pull request has been merged |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-229.md) | Merge a pull request or schedule auto-merge |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-231.md) | Cancel a scheduled auto-merge for a pull request |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers](../endpoints/ep-460.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers](../endpoints/ep-461.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews](../endpoints/ep-451.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews](../endpoints/ep-458.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-452.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-457.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-459.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments](../endpoints/ep-453.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals](../endpoints/ep-462.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals](../endpoints/ep-463.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/update](../endpoints/ep-230.md) | Merge PR's base branch into head branch (update PR) |
| GET | [/api/v1/repos/{owner}/{repo}/push_mirrors](../endpoints/ep-236.md) | Lists all push mirrors of a repository with pagination |
| POST | [/api/v1/repos/{owner}/{repo}/push_mirrors](../endpoints/ep-238.md) | Creates a new push mirror for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/push_mirrors-sync](../endpoints/ep-235.md) | Syncs all push mirrors of a repository by triggering each one |
| GET | [/api/v1/repos/{owner}/{repo}/push_mirrors/{name}](../endpoints/ep-237.md) | Gets a specific push mirror by its remote name |
| DELETE | [/api/v1/repos/{owner}/{repo}/push_mirrors/{name}](../endpoints/ep-239.md) | Deletes a push mirror from a repository by its remote name |
| GET | [/api/v1/repos/{owner}/{repo}/raw/{filepath}](../endpoints/ep-390.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/releases](../endpoints/ep-242.md) | List a repository's releases with pagination and optional draft/pre-release filters |
| POST | [/api/v1/repos/{owner}/{repo}/releases](../endpoints/ep-243.md) | Create a new release or convert an existing tag to a release |
| GET | [/api/v1/repos/{owner}/{repo}/releases/latest](../endpoints/ep-241.md) | Get the most recent non-prerelease, non-draft release sorted by created_at |
| GET | [/api/v1/repos/{owner}/{repo}/releases/tags/{tag}](../endpoints/ep-344.md) | Get a single release of a repository by tag name |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/tags/{tag}](../endpoints/ep-345.md) | Delete a release from a repository by tag name |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-240.md) | Get a single release by ID for a repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-244.md) | Update a release's metadata (tag name, target, title, note, draft/prerelease status) |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-245.md) | Delete a release (keeps the git tag, deletes attachments from storage) |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets](../endpoints/ep-353.md) | List all attachments of a release |
| POST | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets](../endpoints/ep-354.md) | Upload a file attachment to a release |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-352.md) | Get a single attachment of a release by its ID |
| PATCH | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-355.md) | Update the name of a release attachment |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-356.md) | Delete a release attachment and its file from storage |
| GET | [/api/v1/repos/{owner}/{repo}/reviewers](../endpoints/ep-255.md) | Return all users that can be requested to review in this repo |
| GET | [/api/v1/repos/{owner}/{repo}/signing-key.gpg](../endpoints/ep-005.md) | Returns the GPG signing key for a given repository |
| GET | [/api/v1/repos/{owner}/{repo}/signing-key.pub](../endpoints/ep-007.md) | Returns the SSH signing key for a given repository |
| GET | [/api/v1/repos/{owner}/{repo}/stargazers](../endpoints/ep-327.md) | List users who starred the repository |
| POST | [/api/v1/repos/{owner}/{repo}/statuses/{sha}](../endpoints/ep-429.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/statuses/{sha}](../endpoints/ep-430.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/subscribers](../endpoints/ep-328.md) | List users watching (subscribed to) the repository |
| GET | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-196.md) | Check if the current user is watching a repo |
| PUT | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-197.md) | Watch a repo (subscribe to notifications) |
| DELETE | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-198.md) | Unwatch a repo (unsubscribe from notifications) |
| GET | [/api/v1/repos/{owner}/{repo}/tag_protections](../endpoints/ep-419.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/tag_protections](../endpoints/ep-421.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-420.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-422.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-423.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tags](../endpoints/ep-414.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/tags](../endpoints/ep-417.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tags/{tag}](../endpoints/ep-416.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/tags/{tag}](../endpoints/ep-418.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/teams](../endpoints/ep-329.md) | List teams that have access to the repository (org repos only) |
| GET | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-330.md) | Check if a team is assigned to a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-331.md) | Add a team to a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-332.md) | Delete a team from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/times](../endpoints/ep-412.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/times/{user}](../endpoints/ep-411.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/topics](../endpoints/ep-347.md) | Get list of topics that a repository has |
| PUT | [/api/v1/repos/{owner}/{repo}/topics](../endpoints/ep-348.md) | Replace list of topics for a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/topics/{topic}](../endpoints/ep-349.md) | Add a topic to a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/topics/{topic}](../endpoints/ep-350.md) | Delete a topic from a repository |
| POST | [/api/v1/repos/{owner}/{repo}/transfer](../endpoints/ep-404.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/transfer/accept](../endpoints/ep-405.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/transfer/reject](../endpoints/ep-406.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/wiki/new](../endpoints/ep-445.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-446.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-447.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-449.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/pages](../endpoints/ep-448.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/revisions/{pageName}](../endpoints/ep-450.md) |  |
| POST | [/api/v1/repos/{template_owner}/{template_repo}/generate](../endpoints/ep-364.md) | Create a repository using a template |
| GET | [/api/v1/repositories/{id}](../endpoints/ep-368.md) | Get a repository by its numeric ID |
| GET | [/api/v1/topics/search](../endpoints/ep-351.md) | Search topics via keyword |
| POST | [/api/v1/user/repos](../endpoints/ep-363.md) | Create a repository for the authenticated user |

### settings

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/settings/api](../endpoints/ep-016.md) | Returns instance's global API settings including pagination defaults and size limits |
| GET | [/api/v1/settings/attachment](../endpoints/ep-018.md) | Returns instance's global attachment settings including allowed types, max size, and max files |
| GET | [/api/v1/settings/repository](../endpoints/ep-017.md) | Returns instance's global repository settings indicating which features are disabled |
| GET | [/api/v1/settings/ui](../endpoints/ep-015.md) | Returns instance's global UI settings including default theme, allowed reactions, and custom emojis |

### user

| Method | Path | Description |
|--------|------|-------------|
| GET | [/api/v1/user](../endpoints/ep-125.md) | Get the currently authenticated user's full profile |
| GET | [/api/v1/user/actions/jobs](../endpoints/ep-138.md) | Get workflow jobs for the authenticated user |
| GET | [/api/v1/user/actions/runners](../endpoints/ep-176.md) | Get user-level action runners |
| POST | [/api/v1/user/actions/runners/registration-token](../endpoints/ep-175.md) | Get a user's actions runner registration token |
| GET | [/api/v1/user/actions/runners/{runner_id}](../endpoints/ep-177.md) | Get a specific user-level action runner by ID |
| DELETE | [/api/v1/user/actions/runners/{runner_id}](../endpoints/ep-178.md) | Delete a user-level action runner |
| PATCH | [/api/v1/user/actions/runners/{runner_id}](../endpoints/ep-179.md) | Update a user-level action runner (enable/disable) |
| GET | [/api/v1/user/actions/runs](../endpoints/ep-137.md) | Get workflow runs for the authenticated user |
| PUT | [/api/v1/user/actions/secrets/{secretname}](../endpoints/ep-130.md) | Creates or updates a secret value in the user scope |
| DELETE | [/api/v1/user/actions/secrets/{secretname}](../endpoints/ep-131.md) | Deletes a secret in the user scope |
| GET | [/api/v1/user/actions/variables](../endpoints/ep-136.md) | Get the user-level list of variables which is created by current doer |
| POST | [/api/v1/user/actions/variables/{variablename}](../endpoints/ep-132.md) | Creates a user-level variable |
| PUT | [/api/v1/user/actions/variables/{variablename}](../endpoints/ep-133.md) | Updates a user-level variable created by current doer |
| DELETE | [/api/v1/user/actions/variables/{variablename}](../endpoints/ep-134.md) | Deletes a user-level variable created by current doer |
| GET | [/api/v1/user/actions/variables/{variablename}](../endpoints/ep-135.md) | Get a user-level variable which is created by current doer |
| POST | [/api/v1/user/applications/oauth2](../endpoints/ep-167.md) | Create a new OAuth2 application for the authenticated user |
| GET | [/api/v1/user/applications/oauth2](../endpoints/ep-168.md) | List the authenticated user's OAuth2 applications |
| DELETE | [/api/v1/user/applications/oauth2/{id}](../endpoints/ep-169.md) | Delete an OAuth2 application by ID |
| GET | [/api/v1/user/applications/oauth2/{id}](../endpoints/ep-170.md) | Get a specific OAuth2 application by ID |
| PATCH | [/api/v1/user/applications/oauth2/{id}](../endpoints/ep-171.md) | Update an OAuth2 application, regenerating the client secret |
| POST | [/api/v1/user/avatar](../endpoints/ep-128.md) | Update the authenticated user's avatar with a base64-encoded image |
| DELETE | [/api/v1/user/avatar](../endpoints/ep-129.md) | Deletes the current user's custom avatar |
| GET | [/api/v1/user/blocks](../endpoints/ep-190.md) | List users blocked by the authenticated user |
| GET | [/api/v1/user/blocks/{username}](../endpoints/ep-191.md) | Check if a user is blocked by the authenticated user |
| PUT | [/api/v1/user/blocks/{username}](../endpoints/ep-192.md) | Block a user |
| DELETE | [/api/v1/user/blocks/{username}](../endpoints/ep-193.md) | Unblock a user |
| GET | [/api/v1/user/emails](../endpoints/ep-180.md) | List the authenticated user's email addresses |
| POST | [/api/v1/user/emails](../endpoints/ep-181.md) | Add email addresses to the authenticated user |
| DELETE | [/api/v1/user/emails](../endpoints/ep-182.md) | Delete email addresses from the authenticated user |
| GET | [/api/v1/user/followers](../endpoints/ep-139.md) | List the authenticated user's followers |
| GET | [/api/v1/user/following](../endpoints/ep-141.md) | List the users that the authenticated user is following |
| GET | [/api/v1/user/following/{username}](../endpoints/ep-143.md) | Check whether a user is followed by the authenticated user |
| PUT | [/api/v1/user/following/{username}](../endpoints/ep-145.md) | Follow a user |
| DELETE | [/api/v1/user/following/{username}](../endpoints/ep-146.md) | Unfollow a user |
| GET | [/api/v1/user/gpg_key_token](../endpoints/ep-186.md) | Get a token to verify GPG key ownership via signature |
| POST | [/api/v1/user/gpg_key_verify](../endpoints/ep-187.md) | Verify a GPG key by providing a signed token |
| GET | [/api/v1/user/gpg_keys](../endpoints/ep-184.md) | List the authenticated user's GPG keys |
| POST | [/api/v1/user/gpg_keys](../endpoints/ep-188.md) | Create a GPG key for the authenticated user |
| GET | [/api/v1/user/gpg_keys/{id}](../endpoints/ep-185.md) | Get a specific GPG key by ID for the authenticated user |
| DELETE | [/api/v1/user/gpg_keys/{id}](../endpoints/ep-189.md) | Remove a GPG key belonging to the authenticated user |
| GET | [/api/v1/user/hooks](../endpoints/ep-147.md) | List the authenticated user's webhooks |
| POST | [/api/v1/user/hooks](../endpoints/ep-149.md) | Create a webhook for the authenticated user |
| GET | [/api/v1/user/hooks/{id}](../endpoints/ep-148.md) | Get a specific webhook of the authenticated user |
| PATCH | [/api/v1/user/hooks/{id}](../endpoints/ep-150.md) | Update a webhook owned by the authenticated user |
| DELETE | [/api/v1/user/hooks/{id}](../endpoints/ep-151.md) | Delete a webhook owned by the authenticated user |
| GET | [/api/v1/user/keys](../endpoints/ep-157.md) | List the authenticated user's public SSH keys |
| POST | [/api/v1/user/keys](../endpoints/ep-160.md) | Create a public SSH key for the authenticated user |
| GET | [/api/v1/user/keys/{id}](../endpoints/ep-159.md) | Get a public key by ID |
| DELETE | [/api/v1/user/keys/{id}](../endpoints/ep-161.md) | Delete a public SSH key for the authenticated user |
| GET | [/api/v1/user/repos](../endpoints/ep-173.md) | List the repos that the authenticated user owns |
| GET | [/api/v1/user/settings](../endpoints/ep-162.md) | Get the authenticated user's settings (profile fields and privacy preferences) |
| PATCH | [/api/v1/user/settings](../endpoints/ep-163.md) | Update the authenticated user's settings |
| GET | [/api/v1/user/starred](../endpoints/ep-153.md) | List repos that the authenticated user has starred |
| GET | [/api/v1/user/starred/{owner}/{repo}](../endpoints/ep-154.md) | Check whether the authenticated user is starring a repo |
| PUT | [/api/v1/user/starred/{owner}/{repo}](../endpoints/ep-155.md) | Star the given repo as the authenticated user |
| DELETE | [/api/v1/user/starred/{owner}/{repo}](../endpoints/ep-156.md) | Unstar the given repo for the authenticated user |
| GET | [/api/v1/user/stopwatches](../endpoints/ep-385.md) |  |
| GET | [/api/v1/user/subscriptions](../endpoints/ep-195.md) | List repositories watched by the authenticated user |
| GET | [/api/v1/user/teams](../endpoints/ep-055.md) | List all the teams a user belongs to |
| GET | [/api/v1/user/times](../endpoints/ep-413.md) |  |
| GET | [/api/v1/users/search](../endpoints/ep-123.md) | Search for users by keyword, uid, with pagination |
| GET | [/api/v1/users/{username}](../endpoints/ep-124.md) | Get a user's public profile information |
| GET | [/api/v1/users/{username}/activities/feeds](../endpoints/ep-127.md) | List a user's activity feeds with optional date and performer filters |
| GET | [/api/v1/users/{username}/followers](../endpoints/ep-140.md) | List the given user's followers |
| GET | [/api/v1/users/{username}/following](../endpoints/ep-142.md) | List the users that the given user is following |
| GET | [/api/v1/users/{username}/following/{target}](../endpoints/ep-144.md) | Check if one user is following another user |
| GET | [/api/v1/users/{username}/gpg_keys](../endpoints/ep-183.md) | List the given user's GPG keys |
| GET | [/api/v1/users/{username}/heatmap](../endpoints/ep-126.md) | Get a user's contribution heatmap data for the past year |
| GET | [/api/v1/users/{username}/keys](../endpoints/ep-158.md) | List the given user's public SSH keys |
| GET | [/api/v1/users/{username}/repos](../endpoints/ep-172.md) | List the repos owned by the given user |
| GET | [/api/v1/users/{username}/starred](../endpoints/ep-152.md) | List repos that the given user has starred |
| GET | [/api/v1/users/{username}/subscriptions](../endpoints/ep-194.md) | List the repositories watched by a user |
| GET | [/api/v1/users/{username}/tokens](../endpoints/ep-164.md) | List the authenticated user's access tokens (requires basic auth or reverse proxy auth) |
| POST | [/api/v1/users/{username}/tokens](../endpoints/ep-165.md) | Create a new access token for the user |
| DELETE | [/api/v1/users/{username}/tokens/{token}](../endpoints/ep-166.md) | Delete an access token by ID or name |


--- FILE: endpoints/ep-229.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge

Merge a pull request or schedule auto-merge

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-229`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |
| index | path | int64 | True |

**Headers:** `Authorization`

**Request Body** (`application/json`) — `MergePullRequestOption`

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `do` | string | True | Required, In(merge,rebase,rebase-merge,squash,fast-forward-only,manually-merged) |
| `merge_title_field` | string | False |  |
| `merge_message_field` | string | False |  |
| `merge_commit_id` | string | False |  |
| `head_commit_id` | string | False |  |
| `force_merge` | bool | False |  |
| `merge_when_checks_succeed` | bool | False |  |
| `delete_branch_after_merge` | *bool | False |  |

## Response

**200** — empty

- **403** — No permission to merge
- **404** — PR not found or closed
- **405** — Not allowed (WIP, not mergeable, wrong style, signing required)
- **409** — Merge conflict, push out of date, head out of date, already scheduled
- **423** — Repository is archived

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.MergePullRequest | controller | Parse form; Load PR; Set issue read |
| 2 | [services](../modules/services.md) | pull_service.CheckPullMergeable | service | Check merged/closed; Check permission; Check WIP; Check mergeable status; Check branch protection; Check signing requirements; Check dependencies |
| 3 | [services](../modules/services.md) | pull_service.MergedManually | service | Mark PR as manually merged (if manually-merged style) |
| 4 | [services](../modules/services.md) | pull_service.GetDefaultMergeMessage | service | Generate default merge commit message |
| 5 | [services](../modules/services.md) | automerge.ScheduleAutoMerge | service ⏳ | Schedule auto-merge in DB and queue (if merge_when_checks_succeed) |
| 6 | [services](../modules/services.md) | pull_service.Merge | service | Acquire lock; Validate merge style allowed; Do merge and push; Notify; Handle cross-references |
| 7 | [services](../modules/services.md) | repo_service.DeleteBranchAfterMerge | service | Delete head branch if configured |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [pull_request](../datastores/databases.md#pull_request) | database | SELECT | Get PR |
| [pull_request](../datastores/databases.md#pull_request) | database | UPDATE | Set merged |
| [pull_auto_merge](../datastores/databases.md#pull_auto_merge) | database | INSERT | Schedule auto-merge |
| [pr_auto_merge](../datastores/queues.md#pr_auto_merge) | message_queue | PUBLISH | Queue auto-merge check |

## Message Queues

| Topic | Operation | Description |
|-------|-----------|-------------|
| pr_auto_merge | PUBLISH | Queue auto-merge check |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Merge permission check with multiple conditions (WIP, status, branch protection, signing, dependencies) | authorization | Various: HasMerged, IsClosed, !AllowedToMerge, IsWIP, !Mergeable, BranchProtection, SigningRequired, DependenciesLeft |
| Admin force merge can bypass branch protection unless BlockAdminMergeOverride is set | authorization | adminForceMerge && isRepoAdmin && !blockAdminForceMerge |
| Merge style must be allowed by repository PR configuration | business_logic | !prConfig.IsMergeStyleAllowed(mergeStyle) |
| Delete branch after merge respects user option, then falls back to repo default | business_logic | userOption != nil uses user choice; otherwise uses prUnit.PullRequestsConfig().DefaultDeleteBranchAfterMerge |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| PR issue is closed | 404 | notFound | False |
| User lacks merge permission | 405 | empty | False |
| PR title has WIP prefix | 405 | empty | False |
| Git merge conflict | 409 | ErrMergeConflicts JSON | False |
| Merge style not allowed for repo | 405 | empty | False |
| Auto-merge already scheduled | 409 | error | False |

### Error Paths

- **PR closed** → pull_service.CheckPullMergeable → 404
- **No permission** → pull_service.CheckPullMergeable → 405
- **Merge conflict** → pull_service.Merge → 409
- **Already scheduled** → automerge.ScheduleAutoMerge → 409

## Configuration

| Key | Type | Default |
|-----|------|---------|
| [repository.PULL_REQUEST_DEFAULT_MERGE_STYLE](../config/overview.md) | String | merge |

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| low | synchronous_blocking | Git merge operation is synchronous and holds a global lock on the PR | Acceptable - lock is necessary for correctness |

## 🛡️ Resiliency

**Risk Level:** low

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| idempotency | ✅ configured | low | Merge operation uses global lock and checks HasMerged before proceeding; safe against double-merge |

**Cascading failure risk:** Git repo unavailability blocks all merges

**Graceful degradation:** Returns appropriate error codes for each failure mode


--- FILE: endpoints/ep-230.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update

Merge PR's base branch into head branch (update PR)

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-230`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |
| index | path | int64 | True |
| style | query | string | False |

**Headers:** `Authorization`

## Response

**200** — empty

- **403** — User not allowed to update
- **404** — PR not found
- **409** — Merge or rebase conflict
- **422** — PR already merged or closed

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.UpdatePullRequest | controller | Load PR; Check not merged/closed; Load repos |
| 2 | [services](../modules/services.md) | pull_service.IsUserAllowedToUpdate | service | Check PR unit enabled; Check push permission on head repo; Check maintainer edit permission |
| 3 | [services](../modules/services.md) | pull_service.Update | service | Acquire global lock; Check divergence; Merge or rebase base into head; Trigger PR test task |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [pull_request](../datastores/databases.md#pull_request) | database | SELECT | Get PR |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Update PR requires push permission on head repo (or maintainer edit permission) | authorization | User must have push permission on head branch, or be maintainer with AllowMaintainerEdit |
| Cannot update a merged or closed PR | state_transition | pr.HasMerged || pr.Issue.IsClosed |

### Error Paths

- **PR already merged** → repo.UpdatePullRequest → 422
- **PR closed** → repo.UpdatePullRequest → 422
- **Merge conflict** → pull_service.Update → 409
- **Not allowed** → repo.UpdatePullRequest → 403

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| low | synchronous_blocking | Holds global lock during merge/rebase operation | Acceptable - lock is necessary for correctness |

## 🛡️ Resiliency

**Risk Level:** low

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| idempotency | ✅ configured | low | Uses global lock; checks divergence before update (returns error if already up to date) |

**Cascading failure risk:** Git repo unavailability blocks updates

**Graceful degradation:** Returns conflict error on merge/rebase failure


--- FILE: endpoints/ep-234.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/mirror-sync

Adds a mirrored (pull) repository to the sync queue

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-234`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |

**Headers:** `Authorization`

## Response

**200** — empty

- **403** — User lacks write access to code unit
- **400** — Mirror feature disabled or repo is not a mirror
- **404** — Repo not found

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.MirrorSync | controller | Check write permission on code unit; Check mirror feature enabled; Verify repo is a pull mirror |
| 2 | [services](../modules/services.md) | mirror_service.AddPullMirrorToQueue | service ⏳ | Push SyncRequest{PullMirrorType, repoID} to mirror queue in goroutine |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [mirror](../datastores/databases.md#mirror) | database | SELECT | Verify repo is a pull mirror |
| [mirror](../datastores/queues.md#mirror) | message_queue | PUBLISH | Add pull mirror sync request to queue |

## Message Queues

| Topic | Operation | Description |
|-------|-----------|-------------|
| mirror | PUBLISH | Add pull mirror sync request to queue |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Mirror feature must be enabled globally for all mirror endpoints | validation | !setting.Mirror.Enabled |
| Mirror sync requires write access to code unit | authorization | !ctx.Repo.Permission.CanWrite(unit.TypeCode) |
| Repository must be a pull mirror to trigger mirror-sync | validation | errors.Is(err, repo_model.ErrMirrorNotExist) |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| Repo has no mirror record | 400 | Repository is not a mirror | False |
| GetMirrorByRepoID fails | 500 | internal error | True |

### Error Paths

- **User lacks write access to code unit** → middleware reqRepoWriter → 403
- **Mirror.Enabled is false** → repo.MirrorSync → 400
- **No mirror record for repo** → repo.MirrorSync → 400
- **DB error on GetMirrorByRepoID** → repo.MirrorSync → 500

## Configuration

| Key | Type | Default |
|-----|------|---------|
| [mirror.ENABLED](../config/overview.md) | Boolean | true |

## 🛡️ Resiliency

**Risk Level:** low

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| fallback | — not_applicable | low | Async queue push - fire and forget pattern is resilient |

**Cascading failure risk:** None - async queue decouples from actual sync

**Graceful degradation:** Queue handles backpressure via unique queue deduplication


--- FILE: endpoints/ep-235.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync

Syncs all push mirrors of a repository by triggering each one

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-235`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |

**Headers:** `Authorization`

## Response

**200** — empty

- **400** — Mirror feature disabled
- **403** — User is not repo admin
- **404** — Repo not found or push mirrors not found
- **500** — Error syncing a push mirror

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.PushMirrorSync | controller | Check mirror feature enabled; Fetch all push mirrors for repo |
| 2 | [services](../modules/services.md) | mirror_service.SyncPushMirror | service ⚡ | Load push mirror by ID; Get repository; Run git push to remote; Optionally sync LFS objects; Update last_update timestamp |

### External Call Details

**Git Remote (Push Mirror Target)** (`gitrepo`) — Auth: bearer, Base URL: `configured per push mirror (remote_address)`

| Method | Path | Request | Response | Purpose |
|--------|------|---------|----------|---------|
| POST | `git push --mirror` | git protocol | git protocol | Push all refs to remote mirror |
| POST | `LFS batch API` | lfs.Pointer[] | lfs batch response | Upload LFS objects to remote |

**Resilience:** Timeout: setting.Git.Timeout.Mirror * 1000ms

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [push_mirror](../datastores/databases.md#push_mirror) | database | SELECT | Get all push mirrors for repo |
| [push_mirror](../datastores/databases.md#push_mirror) | database | SELECT | Load each mirror by ID during sync |
| [push_mirror](../datastores/databases.md#push_mirror) | database | UPDATE | Update last_update and last_error after sync |

## External Services

### [Git Remote (Push Mirror Target)](../external/Git_Remote__Push_Mirror_Target_.md)

**Client:** `gitrepo` · **Auth:** bearer

| Method | Path | Request Type | Response Type | Purpose |
|--------|------|-------------|---------------|---------|
| POST | `git push --mirror` | git protocol | git protocol | Push all refs to remote mirror |
| POST | `LFS batch API` | lfs.Pointer[] | lfs batch response | Upload LFS objects to remote |

**Resilience:**
- Timeout: setting.Git.Timeout.Mirror * 1000ms

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Mirror feature must be enabled globally for all mirror endpoints | validation | !setting.Mirror.Enabled |
| Push mirror operations require repo admin access | authorization | reqAdmin() middleware applied to push_mirrors group |
| Push mirror sync is synchronous - each mirror is synced sequentially in the request | business_logic | Always when push_mirrors-sync is called |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| GetPushMirrorsByRepoID fails | 404 | error message | True |
| SyncPushMirror returns false | 500 | error occurred when syncing push mirror <name> | True |

### Error Paths

- **Mirror.Enabled is false** → repo.PushMirrorSync → 400
- **Error fetching push mirrors** → repo.PushMirrorSync → 404
- **SyncPushMirror returns false** → repo.PushMirrorSync → 500

## Configuration

| Key | Type | Default |
|-----|------|---------|
| [mirror.ENABLED](../config/overview.md) | Boolean | true |
| [git.TIMEOUT.MIRROR](../config/overview.md) | Integer (seconds) | 300 |
| [lfs.START_SERVER](../config/overview.md) | Boolean | false |

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| high | synchronous_blocking | Push mirror sync is done synchronously in the HTTP request handler, blocking the request thread for each mirror's git push operation | Queue push mirror syncs asynchronously like pull mirror sync does, rather than blocking the HTTP request |
| medium | n_plus_1_queries | Each SyncPushMirror call loads the push mirror by ID again from DB, even though it was already loaded in the list | Pass the already-loaded PushMirror object directly instead of re-fetching by ID |

### Optimization Recommendations

- **[P1] async**: Make push mirror sync asynchronous by queuing each mirror sync — *Impact: Reduce request latency from O(N * timeout) to O(1)*

## 🛡️ Resiliency

**Risk Level:** high

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| timeout | ✅ configured | medium | Git push has timeout but total request time = N * timeout which can exceed HTTP timeouts |
| retry | ❌ missing | medium | No retry on transient push failures |
| circuit_breaker | ❌ missing | high | No circuit breaker - will attempt push to known-failing remotes |
| cascading_failure | ❌ missing | high | Fails on first mirror error, leaving remaining mirrors unsynced |

**Non-atomic operations:**
- ⚠️ Partial sync - some mirrors synced, some not, if error occurs mid-loop

**Cascading failure risk:** One slow/failing remote blocks all subsequent mirrors in the loop

**Graceful degradation:** Returns 500 on first failure, partial sync state


--- FILE: endpoints/ep-249.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/diffpatch

Apply a diff patch to the repository, creating a new commit

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-249`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |

**Request Body** (`application/json`) — `ApplyDiffPatchFileOptions`

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `content` | string | True |  |
| `message` | string | False |  |
| `branch` | string | False | GitRefName, MaxSize(100) |
| `new_branch` | string | False | GitRefName, MaxSize(100) |
| `author` | Identity | False |  |
| `committer` | Identity | False |  |
| `dates` | CommitDateOptions | False |  |
| `signoff` | boolean | False |  |

## Response

**201** — FileResponse

| Field | Type | Description |
|-------|------|-------------|
| `commit` | FileCommitResponse | Commit information |
| `verification` | PayloadCommitVerification | Commit signature verification |

- **403** — Push rejected or user cannot commit to protected branch
- **404** — Repository or branch not found
- **422** — Branch already exists, commit ID mismatch
- **423** — Repository is archived

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.ApplyDiffPatch | controller | Get form options via getAPIChangeRepoFileOptions; Build ApplyDiffPatchOptions; Call files.ApplyDiffPatch |
| 2 | [routers](../modules/routers.md) | repo.ReqChangeRepoFileOptionsAndCheck | controller | Parse common file options; Check write permission to target branch; Store options in context |
| 3 | [services](../modules/services.md) | files.ApplyDiffPatch | service | Check repo not archived; Open git repo; Validate options (branch exists, permissions); Create temp repo; Clone old branch; Apply patch with git apply; Write tree; Commit tree; Push to new branch |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [branch](../datastores/databases.md#branch) | database | SELECT | Check old branch exists |
| [branch](../datastores/databases.md#branch) | database | SELECT | Check new branch exists |
| [protected_branch](../datastores/databases.md#protected_branch) | database | SELECT | Check branch protection |

### Data Transformations

**ApplyDiffPatchFileOptions** → **ApplyDiffPatchOptions** (`repo.ApplyDiffPatch`)

| Source Field | Target Field | Transformation |
|-------------|--------------|----------------|
| `Content` | `Content` | direct_copy |
| `Message` | `Message` | computed |
| `FileOptions.BranchName` | `OldBranch` | direct_copy |
| `FileOptions.NewBranchName` | `NewBranch` | direct_copy |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| User must have write permission to target branch for diff patch | authorization | !ctx.Repo.CanWriteToBranch(ctx, ctx.Doer, commonOpts.NewBranchName) && !ctx.IsUserSiteAdmin() |
| Protected branch check prevents unauthorized commits | authorization | protectedBranch != nil && !protectedBranch.CanUserPush(ctx, doer) |
| New branch must not already exist when branching | validation | opts.NewBranch != opts.OldBranch && branch exists |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| Patch cannot be applied cleanly | 500 | internal error | False |

### Error Paths

- **Repo is archived** → handleChangeRepoFilesError → 423
- **Push rejected** → handleChangeRepoFilesError → 403
- **User cannot commit (protected branch)** → handleChangeRepoFilesError → 403
- **Branch already exists** → handleChangeRepoFilesError → 422
- **Branch not found** → handleChangeRepoFilesError → 404

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| medium | synchronous_blocking | Creates temporary repository clone, applies patch, and pushes - all synchronous on request thread | Consider async processing for large patches or add request timeout |

### Optimization Recommendations

- **[P3] timeout**: Add timeout for git apply operations — *Impact: Prevent hung requests from consuming resources indefinitely*

## 🛡️ Resiliency

**Risk Level:** medium

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| non_atomic | ✅ configured | medium | Multi-step operation (clone, apply, commit, push) uses temp repo with deferred cleanup. If push fails after commit, temp repo is cleaned up but no partial state persists. |
| timeout | ❌ missing | medium | No explicit timeout on git apply or push operations. Large patches could block indefinitely. |

**Non-atomic operations:**
- ⚠️ Clone + apply + commit + push sequence uses temp repo for atomicity

**Cascading failure risk:** Disk space exhaustion if many concurrent patch operations create temp repos

**Graceful degradation:** Temp repo cleanup via defer ensures no leaked state


--- FILE: endpoints/ep-308.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/branches

Create a new branch in a repository

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-308`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |

**Request Body** (`application/json`) — `CreateBranchRepoOption`

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `new_branch_name` | string | True | Required, GitRefName, MaxSize(100) |
| `old_branch_name` | string | False | GitRefName, MaxSize(100) |
| `old_ref_name` | string | False | GitRefName, MaxSize(100) |

## Response

**201** — api.Branch

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Branch name |
| `commit` | PayloadCommit | Latest commit on branch |
| `protected` | bool | Whether branch is protected |
| `required_approvals` | int64 | Number of required approvals |
| `enable_status_check` | bool | Whether status checks enabled |
| `status_check_contexts` | []string | Required status check contexts |
| `user_can_push` | bool | Whether current user can push |
| `user_can_merge` | bool | Whether current user can merge |
| `effective_branch_protection_name` | string | Name of effective branch protection rule |

- **403** — Repository is a mirror
- **404** — Old branch does not exist or repo is empty
- **409** — Branch already exists or tag with same name exists
- **423** — Repository is archived

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.CreateBranch | controller | Check repo not empty/mirror, resolve source ref |
| 2 | [modules](../modules/modules.md) | GitRepo.GetCommit/GetBranchCommit | utility | Resolve source commit from OldRefName, OldBranchName, or default branch |
| 3 | [services](../modules/services.md) | repo_service.CreateNewBranchFromCommit | service | Check archive status, check branch name conflicts, push new branch to git |
| 4 | [services](../modules/services.md) | checkBranchName | service | Walk all refs to check for name conflicts with existing branches and tags |
| 5 | [modules](../modules/modules.md) | gitrepo.Push | utility | Execute git push to create branch |
| 6 | [services](../modules/services.md) | convert.ToBranch | service | Convert new branch to API response |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [branch](../datastores/databases.md#branch) | database | SELECT | Check old branch exists (if OldBranchName used) |
| [protected_branch](../datastores/databases.md#protected_branch) | database | SELECT | Get protection for new branch |

### Data Transformations

**CreateBranchRepoOption** → **git push command** (`repo_service.CreateNewBranchFromCommit`)

| Source Field | Target Field | Transformation |
|-------------|--------------|----------------|
| `BranchName` | `branch ref` | computed |
| `OldRefName/OldBranchName` | `commitID` | computed |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Repository must not be empty for branch operations | validation | ctx.Repo.Repository.IsEmpty |
| Repository must not be a mirror for write branch operations | validation | ctx.Repo.Repository.IsMirror |
| New branch name must not conflict with existing branches or tags | validation | Branch name matches existing branch or has path prefix conflict or matches tag |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| Branch with same name exists | 409 | The branch already exists | False |
| Tag with same name exists | 409 | The branch with the same tag already exists | False |
| Branch name conflicts with path prefix | 409 | The branch with the same name already exists | False |

### Error Paths

- **Repo is empty** → ctx.APIError → 404
- **Repo is mirror** → ctx.APIError → 403
- **Old branch not exist** → ctx.APIError → 404
- **Branch already exists** → ctx.APIError → 409
- **Tag already exists** → ctx.APIError → 409
- **Branch name conflict** → ctx.APIError → 409

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| medium | unbounded_queries | checkBranchName walks ALL refs in the repository to check for name conflicts | Consider using git check-ref-format or targeted ref lookup instead of walking all refs |

### Optimization Recommendations

- **[P2] query_optimization**: Replace full ref walk with targeted git ref existence check — *Impact: Reduce branch creation time for large repos from O(n) to O(1)*

## 🛡️ Resiliency

**Risk Level:** medium

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| non_atomic | ❌ missing | medium | checkBranchName walks refs then push creates branch - race condition possible between check and create |

**Non-atomic operations:**
- ⚠️ Name conflict check and branch creation are not atomic - relies on git push failure for race condition handling

**Cascading failure risk:** None significant

**Graceful degradation:** Git push failure returns appropriate conflict error


--- FILE: endpoints/ep-318.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/merge-upstream

Merge a branch from the upstream (base) repository into the fork

**Module:** [routers](../modules/routers.md) · **Auth:** bearer · **ID:** `ep-318`

## Request

| Param | Location | Type | Required |
|-------|----------|------|----------|
| owner | path | string | True |
| repo | path | string | True |

**Headers:** `Authorization`

**Request Body** (`application/json`) — `MergeUpstreamRequest`

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `branch` | string | True |  |
| `ff_only` | bool | False |  |

## Response

**200** — MergeUpstreamResponse

| Field | Type | Description |
|-------|------|-------------|
| `merge_type` | string | The merge style used: up-to-date, fast-forward, or merge |

- **400** — Invalid argument (not a fork, archived, ff_only failed)
- **404** — Repository or branch not found

## Workflow

| Step | Module | Component | Type | Details |
|------|--------|-----------|------|---------|
| 1 | [routers](../modules/routers.md) | repo.MergeUpstream | controller | Parse form body; Call repo_service.MergeUpstream |
| 2 | [services](../modules/services.md) | repository.MergeUpstream | service | Check repo not archived; Load base repo; Get upstream diverging info; Attempt git push (fast-forward); If push fails and not ffOnly, create fake PR and call pull.Update |
| 3 | [services](../modules/services.md) | repository.GetUpstreamDivergingInfo | service | Validate repo is fork and not archived; Load base repo; Check if branch exists in base repo; Get branch diverging info |
| 4 | [modules](../modules/modules.md) | gitrepo.Push | utility ⚡ | Execute git push from base repo to fork repo |
| 5 | [services](../modules/services.md) | pull.Update | service ⚡ | Perform merge of base branch into head branch using fake PR |

### Datastore Operations

| Store | Type | Operation | Description |
|-------|------|-----------|-------------|
| [repository](../datastores/databases.md#repository) | database | SELECT | Load base repository for fork |

#### `repository` document schema

| Field | Type | Nullable | Indexed | Description |
|-------|------|----------|---------|-------------|
| `id` | int64 | False | True | pk |
| `owner_id` | int64 | False | True | INDEX |
| `owner_name` | string | True | False |  |

### Data Transformations

**MergeUpstreamRequest** → **MergeUpstreamResponse** (`repo.MergeUpstream`)

| Source Field | Target Field | Transformation |
|-------------|--------------|----------------|
| `branch` | `merge_type` | computed |

## Business Rules

| Rule | Category | Condition |
|------|----------|-----------|
| Repo must be a fork to merge upstream | validation | !forkRepo.IsFork |
| Repo must not be archived to merge upstream | validation | repo.MustNotBeArchived() returns error |
| If ff_only requested and fast-forward fails, return error instead of merge | business_logic | ffOnly && push failed with out-of-date/rejected |
| Branch resolution: if branch exists in base repo use it, otherwise use base default branch | business_logic | Branch not found in base repo (ErrNotExist) |

## Error Handling

| Trigger | Status | Response | Retryable |
|---------|--------|----------|-----------|
| Repo not a fork, archived, or ff_only failed | 400 | error | False |
| Branch or repo not found | 404 | notFound | False |

### Error Paths

- **Repo is not a fork or is archived** → repo.MergeUpstream → 400
- **Branch or repo not found** → repo.MergeUpstream → 404
- **Internal error during merge** → repo.MergeUpstream → 500

## ⚠️ Performance Issues

| Severity | Type | Description | Recommendation |
|----------|------|-------------|----------------|
| medium | synchronous_blocking | Git push and merge operations are synchronous and can be slow for large repos | Consider async merge with status polling for large repositories |

### Optimization Recommendations

- **[P2] async**: Consider making merge-upstream async for large repos — *Impact: Prevent request timeouts on large repositories*

## 🛡️ Resiliency

**Risk Level:** medium

| Pattern | Status | Severity | Detail |
|---------|--------|----------|--------|
| non_atomic | ❌ missing | medium | Git push attempt followed by fallback to merge via fake PR - if merge fails after push attempt, state may be inconsistent |
| timeout | — not_applicable | low | Git operations use context cancellation but no explicit timeout on the merge operation |

**Non-atomic operations:**
- ⚠️ Git push attempt + fallback merge via fake PR if push fails

**Cascading failure risk:** Git operations on disk could block if filesystem is slow

**Graceful degradation:** Returns error if merge fails


--- FILE: endpoints/ep-396.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# PUT /api/v1/repos/{owner}/{repo}/contents/{filepath}


**Module:** [routers](../modules/routers.md) · **Auth:** none · **ID:** `ep-396`


--- FILE: endpoints/ep-417.md ---
<!-- Generated by cai (Charter AI) — automated API documentation -->

# POST /api/v1/repos/{owner}/{repo}/tags


**Module:** [routers](../modules/routers.md) · **Auth:** none · **ID:** `ep-417`



## Developer Query

What are all the API endpoints that trigger git operations? For each, list the git command executed, timeout configured, and what happens on failure.

## Answer
