# Phase 2 Session Report

**Session:** 8
**Endpoints Analyzed:** ep-050 to ep-055
**Total Endpoints:** 6
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 6
- Business rules extracted: 8
- Database operations documented: 22
- External integrations used: 0
- Performance issues found: 5 (1 high, 3 medium, 1 low)
- Average workflow depth: 3.7 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-050 | DELETE | /api/v1/orgs/{org}/actions/runners/{runner_id} | 4 steps | 4 files | 1 (low) |
| ep-051 | PATCH | /api/v1/orgs/{org}/actions/runners/{runner_id} | 5 steps | 4 files | 1 (low) |
| ep-052 | GET | /api/v1/orgs/{org}/actions/jobs | 3 steps | 5 files | 1 (high) |
| ep-053 | GET | /api/v1/orgs/{org}/actions/runs | 3 steps | 5 files | 1 (medium) |
| ep-054 | GET | /api/v1/orgs/{org}/teams | 3 steps | 4 files | 1 (medium) |
| ep-055 | GET | /api/v1/user/teams | 3 steps | 4 files | 1 (medium) |

## Performance Issues Found

1. **HIGH** (ep-052): N+1 queries in ToActionWorkflowJob - loads task, steps, and runner per job individually. Up to 60 extra queries for a page of 20 jobs.
2. **MEDIUM** (ep-053): N+1 queries in ToActionWorkflowRun - loads latest attempt per run individually. 20 extra queries per page.
3. **MEDIUM** (ep-054, ep-055): N+1 queries in ToTeams - LoadUnits called per team individually. 20 extra queries per page.

## Files Read
- routers/api/v1/org/action.go
- routers/api/v1/shared/runners.go
- routers/api/v1/shared/action.go
- routers/api/v1/org/team.go
- models/actions/runner.go
- models/actions/run.go
- models/actions/run_list.go
- models/actions/run_job.go
- models/actions/run_job_list.go
- models/actions/tasks_version.go
- models/organization/team.go
- models/organization/team_list.go
- modules/structs/repo_actions.go
- modules/structs/org_team.go
- services/convert/convert.go
- routers/api/v1/utils/page.go
