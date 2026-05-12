# Controller: GET /api/v1/packages/{owner}

> 64 nodes · cohesion 0.06

## Key Concepts

- **GET /api/v1/packages/{owner}** (17 connections) — `session_29/api_contracts.json`
- **DELETE /api/v1/packages/{owner}/{type}/{name}/{version}** (16 connections) — `session_30/api_contracts.json`
- **POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}** (15 connections) — `session_30/api_contracts.json`
- **GET /api/v1/packages/{owner}/{type}/{name}/{version}** (14 connections) — `session_29/api_contracts.json`
- **DELETE /api/v1/packages/{owner}/{type}/{name}** (14 connections) — `session_29/api_contracts.json`
- **POST /api/v1/packages/{owner}/{type}/{name}/-/unlink** (14 connections) — `session_30/api_contracts.json`
- **GET /api/v1/packages/{owner}/{type}/{name}/{version}/files** (13 connections) — `session_30/api_contracts.json`
- **GET /api/v1/packages/{owner}/{type}/{name}** (12 connections) — `session_30/api_contracts.json`
- **GET /api/v1/packages/{owner}/{type}/{name}/-/latest** (12 connections) — `session_30/api_contracts.json`
- **context.PackageAssignmentAPI** (12 connections) — `services/context/package.go`
- **package** (10 connections) — `routers/api/v1/packages/package.go`
- **packages_model.Package** (7 connections) — `session_30/impact_analysis_index.json`
- **packages_model.PackageDescriptor** (7 connections) — `session_30/impact_analysis_index.json`
- **packages_model.PackageVersion** (7 connections) — `session_30/impact_analysis_index.json`
- **packages.ENABLED** (6 connections) — `modules/setting/packages.go`
- **service.REQUIRE_SIGNIN_VIEW** (6 connections) — `modules/setting/service.go`
- **convert.ToPackage** (6 connections) — `session_30/impact_analysis_index.json`
- **packages_model.PackageFile** (5 connections) — `session_30/impact_analysis_index.json`
- **PackageAssignmentAPI middleware** (4 connections) — `services/context/package.go`
- **packages_model.GetPackageDescriptors** (4 connections) — `models/packages/descriptor.go`
- **packages.DeletePackage** (3 connections) — `routers/api/v1/packages/package.go`
- **packages.DeletePackageVersion** (3 connections) — `routers/api/v1/packages/package.go`
- **packages.GetPackage** (3 connections) — `routers/api/v1/packages/package.go`
- **packages.LinkPackage** (3 connections) — `routers/api/v1/packages/package.go`
- **packages.ListPackageVersions** (3 connections) — `routers/api/v1/packages/package.go`
- *... and 39 more nodes in this community*

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (7 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (4 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (4 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (3 shared connections)
- [[Controller: Issue templates are parsed from multiple candidate directories in priority order]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Unarchiving a repo re-detects action schedules]] (1 shared connections)

## Source Files

- `models/packages/descriptor.go`
- `models/packages/package_version.go`
- `modules/setting/packages.go`
- `modules/setting/service.go`
- `routers/api/v1/packages/package.go`
- `services/context/package.go`
- `session_29/api_contracts.json`
- `session_29/database_schema.json`
- `session_29/error_handling.json`
- `session_29/impact_analysis_index.json`
- `session_30/api_contracts.json`
- `session_30/error_handling.json`
- `session_30/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 272 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*