# GPG binary (gpg --export)

**Client:** `process.GetManager().ExecDir` · **Type:** process_exec

**File:** `services/asymkey/sign.go`

**Base URL:** `local process`

**Auth:** none

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
| EXEC | gpg --export -a <keyID> | Export GPG public key in ASCII armor format |

## Used By (2 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md) |
