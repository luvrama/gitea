# Controller: GET /api/v1/repos/search

> 28 nodes · cohesion 0.10

## Key Concepts

- **GET /api/v1/repos/search** (13 connections) — `session_53/api_contracts.json`
- **repository** (12 connections) — `routers/api/v1/repo/repo.go`
- **DELETE /api/v1/repos/{owner}/{repo}** (8 connections) — `session_54/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issue_templates** (7 connections) — `session_54/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issue_config** (5 connections) — `session_54/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/issue_config/validate** (5 connections) — `session_54/api_contracts.json`
- **access_model.GetDoerRepoPermission (loop)** (3 connections) — `models/perm/access/repo_permission.go`
- **issue.GetTemplateConfigFromDefaultBranch** (3 connections) — `session_54/impact_analysis_index.json`
- **repo.LoadOwner (loop)** (3 connections) — `models/repo/repo.go`
- **repo_model.SearchRepository** (3 connections) — `session_53/impact_analysis_index.json`
- **repo_module.CanUserDelete** (3 connections) — `modules/repository/delete.go`
- **convert.ToRepo (loop)** (2 connections) — `services/convert/repository.go`
- **issue.ParseTemplatesFromDefaultBranch** (2 connections) — `session_54/impact_analysis_index.json`
- **repo.Delete** (2 connections) — `routers/api/v1/repo/repo.go`
- **repo.GetIssueConfig** (2 connections) — `routers/api/v1/repo/repo.go`
- **repo.GetIssueTemplates** (2 connections) — `routers/api/v1/repo/repo.go`
- **repo.Search** (2 connections) — `routers/api/v1/repo/repo.go`
- **repo_service.DeleteRepository** (2 connections) — `session_54/impact_analysis_index.json`
- **repository.issue.MaxPinned** (1 connections) — `modules/setting/repository.go`
- **repo.Delete** (1 connections) — `session_54/api_contracts.json`
- **repo.GetIssueConfig** (1 connections) — `session_54/api_contracts.json`
- **repo.GetIssueTemplates** (1 connections) — `session_54/api_contracts.json`
- **repo.Search** (1 connections) — `session_53/api_contracts.json`
- **repo.ValidateIssueConfig** (1 connections) — `session_54/api_contracts.json`
- **422 Mode not in allowed set** (1 connections) — `session_53/error_handling.json`
- *... and 3 more nodes in this community*

## Relationships

- [[Controller: user_model.User]] (6 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (4 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: reqOrgOwnership]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (1 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (1 shared connections)

## Source Files

- `models/perm/access/repo_permission.go`
- `models/repo/repo.go`
- `modules/repository/delete.go`
- `modules/setting/repository.go`
- `routers/api/v1/repo/repo.go`
- `services/convert/repository.go`
- `session_53/api_contracts.json`
- `session_53/error_handling.json`
- `session_53/impact_analysis_index.json`
- `session_54/api_contracts.json`
- `session_54/error_handling.json`
- `session_54/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 89 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*