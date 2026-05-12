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
