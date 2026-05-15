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
