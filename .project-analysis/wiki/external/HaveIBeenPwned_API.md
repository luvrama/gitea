# HaveIBeenPwned API

**Client:** `password.IsPwned` · **Type:** http_api

**File:** `modules/auth/password/pwn/pwn.go`

**Base URL:** `https://api.pwnedpasswords.com`

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
| Fallback | If request fails, error is returned but treated as non-blocking in some contexts |

## Methods Called

| Method | Path | Purpose |
|--------|------|---------|
| GET | /range/{hash_prefix} | Check if password has been compromised |

## Used By (1 endpoints)

| Module | Endpoints |
|--------|-----------|
| [routers](../modules/routers.md) | [ep-099](../endpoints/ep-099.md) |
