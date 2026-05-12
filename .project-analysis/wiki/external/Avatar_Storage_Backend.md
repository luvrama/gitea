# Avatar Storage Backend

**Client:** `ObjectStorage` · **Type:** cloud_service

**File:** `modules/storage/storage.go`

**Base URL:** `configured via setting.Avatar.Storage`

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
| Fallback | Logs warning if file doesn't exist (ErrNotExist), otherwise propagates error |

## Methods Called

| Method | Path | Purpose |
|--------|------|---------|
| DELETE | <avatar_relative_path> | Delete avatar file from storage |

## Used By (1 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-129](../endpoints/ep-129.md) |
