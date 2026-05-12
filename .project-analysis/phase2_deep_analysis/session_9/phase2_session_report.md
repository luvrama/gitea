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
