# Controller: GET /api/v1/gitignore/templates/{name}

> 25 nodes · cohesion 0.10

## Key Concepts

- **GET /api/v1/gitignore/templates/{name}** (11 connections) — `session_2/api_contracts.json`
- **GET /api/v1/licenses/{name}** (11 connections) — `session_2/api_contracts.json`
- **GET /api/v1/licenses** (7 connections) — `session_2/api_contracts.json`
- **LayeredFS.ReadFile** (4 connections) — `modules/assetfs/layered.go`
- **miscellaneous** (3 connections) — `routers/api/v1/misc/gitignore.go`
- **miscellaneous** (3 connections) — `routers/api/v1/misc/licenses.go`
- **GET /api/v1/gitignore/templates** (3 connections) — `session_2/api_contracts.json`
- **options.Gitignore** (3 connections) — `session_2/impact_analysis_index.json`
- **options.License** (3 connections) — `session_2/impact_analysis_index.json`
- **setting.AppURL** (2 connections) — `modules/setting/server.go`
- **setting.CustomPath** (2 connections) — `modules/setting/setting.go`
- **misc.GetGitignoreTemplateInfo** (2 connections) — `routers/api/v1/misc/gitignore.go`
- **misc.GetLicenseTemplateInfo** (2 connections) — `routers/api/v1/misc/licenses.go`
- **setting.Repository.PreferredLicenses** (1 connections) — `modules/setting/repository.go`
- **misc.GetGitignoreTemplateInfo** (1 connections) — `session_2/api_contracts.json`
- **misc.GetLicenseTemplateInfo** (1 connections) — `session_2/api_contracts.json`
- **misc.ListGitignoresTemplates** (1 connections) — `session_2/api_contracts.json`
- **misc.ListLicenseTemplates** (1 connections) — `session_2/api_contracts.json`
- **404 Gitignore template name doesn't exist in any layer** (1 connections) — `session_2/error_handling.json`
- **404 License template name doesn't exist in any layer** (1 connections) — `session_2/error_handling.json`
- **GitignoreTemplateInfo** (1 connections) — `session_2/impact_analysis_index.json`
- **LicenseTemplateInfo** (1 connections) — `session_2/impact_analysis_index.json`
- **LicensesTemplateListEntry** (1 connections) — `session_2/impact_analysis_index.json`
- **misc.ListGitignoresTemplates** (1 connections) — `routers/api/v1/misc/gitignore.go`
- **misc.ListLicenseTemplates** (1 connections) — `routers/api/v1/misc/licenses.go`

## Relationships

- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (3 shared connections)
- [[Endpoint: routers]] (2 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (1 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)

## Source Files

- `modules/assetfs/layered.go`
- `modules/setting/repository.go`
- `modules/setting/server.go`
- `modules/setting/setting.go`
- `routers/api/v1/misc/gitignore.go`
- `routers/api/v1/misc/licenses.go`
- `session_2/api_contracts.json`
- `session_2/error_handling.json`
- `session_2/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*