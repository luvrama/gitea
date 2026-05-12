# Controller: POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches

> 16 nodes · cohesion 0.16

## Key Concepts

- **POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches** (16 connections) — `session_41/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable** (6 connections) — `session_41/api_contracts.json`
- **PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable** (6 connections) — `session_41/api_contracts.json`
- **actions_service.EnableOrDisableWorkflow** (4 connections) — `session_41/impact_analysis_index.json`
- **RepoUnit** (3 connections) — `session_41/impact_analysis_index.json`
- **ActionsDisableWorkflow** (2 connections) — `routers/api/v1/repo/action.go`
- **ActionsDispatchWorkflow** (2 connections) — `routers/api/v1/repo/action.go`
- **ActionsEnableWorkflow** (2 connections) — `routers/api/v1/repo/action.go`
- **actions_service.DispatchActionWorkflow** (2 connections) — `session_41/impact_analysis_index.json`
- **repo.ActionsDisableWorkflow** (1 connections) — `session_41/api_contracts.json`
- **repo.ActionsDispatchWorkflow** (1 connections) — `session_41/api_contracts.json`
- **repo.ActionsEnableWorkflow** (1 connections) — `session_41/api_contracts.json`
- **403 workflow is disabled in repo config** (1 connections) — `session_41/error_handling.json`
- **404 git ref doesn't exist** (1 connections) — `session_41/error_handling.json`
- **404 workflow file not in commit tree** (1 connections) — `session_41/error_handling.json`
- **422 ref field is empty in request body** (1 connections) — `session_41/error_handling.json`

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (4 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (3 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (2 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (1 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (1 shared connections)

## Source Files

- `routers/api/v1/repo/action.go`
- `session_41/api_contracts.json`
- `session_41/error_handling.json`
- `session_41/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 50 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*