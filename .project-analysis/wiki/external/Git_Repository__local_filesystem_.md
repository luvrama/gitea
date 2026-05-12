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
