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
