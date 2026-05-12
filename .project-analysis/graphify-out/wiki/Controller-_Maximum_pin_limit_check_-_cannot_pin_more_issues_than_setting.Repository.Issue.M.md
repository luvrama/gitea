# Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M

> 189 nodes · cohesion 0.02

## Key Concepts

- **Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M** (125 connections) — `models/issues/issue_pin.go`
- **Pin position must be >= 1** (86 connections) — `models/issues/issue_pin.go`
- **repository** (36 connections) — `routers/api/v1/repo/action.go`
- **GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip** (19 connections) — `session_43/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun** (18 connections) — `session_42/api_contracts.json`
- **POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun** (18 connections) — `session_42/api_contracts.json`
- **ActionRunner** (17 connections) — `session_40/impact_analysis_index.json`
- **organization** (16 connections) — `routers/api/v1/org/action.go`
- **POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs** (16 connections) — `session_42/api_contracts.json`
- **DELETE /api/v1/repos/{owner}/{repo}/actions/runs/{run}** (16 connections) — `session_43/api_contracts.json`
- **PATCH /api/v1/orgs/{org}/actions/runners/{runner_id}** (15 connections) — `session_8/api_contracts.json`
- **ActionRun** (15 connections) — `session_43/impact_analysis_index.json`
- **PATCH /api/v1/admin/actions/runners/{runner_id}** (14 connections) — `session_17/api_contracts.json`
- **PATCH /api/v1/user/actions/runners/{runner_id}** (13 connections) — `session_26/api_contracts.json`
- **setting.PanicInDevOrTesting** (12 connections) — `modules/setting/global.go`
- **GET /api/v1/orgs/{org}/actions/jobs** (12 connections) — `session_8/api_contracts.json`
- **GET /api/v1/admin/actions/runs** (12 connections) — `session_16/api_contracts.json`
- **GET /api/v1/admin/actions/runners/{runner_id}** (12 connections) — `session_17/api_contracts.json`
- **GET /api/v1/user/actions/runners/{runner_id}** (12 connections) — `session_26/api_contracts.json`
- **shared.ListJobs** (12 connections) — `session_42/impact_analysis_index.json`
- **DELETE /api/v1/orgs/{org}/actions/runners/{runner_id}** (11 connections) — `session_8/api_contracts.json`
- **GET /api/v1/orgs/{org}/actions/runs** (11 connections) — `session_8/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs** (11 connections) — `session_42/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}** (11 connections) — `session_43/api_contracts.json`
- **User** (11 connections) — `session_33/impact_analysis_index.json`
- *... and 164 more nodes in this community*

## Relationships

- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (52 shared connections)
- [[Controller: reqOrgOwnership]] (26 shared connections)
- [[Controller: user_model.User]] (23 shared connections)
- [[Controller: convert]] (18 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (14 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] (13 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (12 shared connections)
- [[Controller: POST /api/v1/orgs]] (11 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (11 shared connections)
- [[Controller: Org repo creation requires user to have create permission in org]] (9 shared connections)
- [[Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections]] (9 shared connections)
- [[Endpoint: routers]] (8 shared connections)

## Source Files

- `app.ini`
- `models/actions/run_attempt.go`
- `models/actions/run_job.go`
- `models/actions/runner.go`
- `models/issues/issue_pin.go`
- `modules/setting/actions.go`
- `modules/setting/global.go`
- `modules/storage/storage.go`
- `routers/api/v1/admin/action.go`
- `routers/api/v1/admin/runners.go`
- `routers/api/v1/org/action.go`
- `routers/api/v1/repo/action.go`
- `routers/api/v1/shared/runners.go`
- `routers/api/v1/user/action.go`
- `routers/api/v1/user/runners.go`
- `session_15/api_contracts.json`
- `session_15/impact_analysis_index.json`
- `session_16/api_contracts.json`
- `session_16/error_handling.json`
- `session_17/api_contracts.json`

## Audit Trail

- EXTRACTED: 1065 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*