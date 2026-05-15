# Object Storage (Minio/Azure/Local)

**Client:** `storage.ObjectStorage` · **Type:** cloud_service

**File:** `modules/storage/storage.go`

**Base URL:** `configured via app.ini [actions.artifact_storage]`

**Auth:** api-key

## Resilience

| Setting | Value |
|---------|-------|
| Circuit breaker | ❌ Disabled |
| Level | — |
| Implementation | None |
| Open condition | — |
| Recovery | — |
| Impact when open | — |
| Fallback | If ServeDirect fails, falls back to reading from storage and serving via app |

## Methods Called

| Method | Path | Purpose |
|--------|------|---------|
| GET | ServeDirectURL | Generate presigned download URL for direct serve |
| DELETE | Delete | Delete artifact file from storage |
| GET | Open | Open artifact file for streaming |

## Used By (11 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-037](../endpoints/ep-037.md), [ep-038](../endpoints/ep-038.md), [ep-128](../endpoints/ep-128.md), [ep-259](../endpoints/ep-259.md), [ep-261](../endpoints/ep-261.md), [ep-262](../endpoints/ep-262.md), [ep-263](../endpoints/ep-263.md), [ep-294](../endpoints/ep-294.md), [ep-298](../endpoints/ep-298.md), [ep-354](../endpoints/ep-354.md), [ep-356](../endpoints/ep-356.md) |
