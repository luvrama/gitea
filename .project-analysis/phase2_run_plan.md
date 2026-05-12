# Phase 2 Run Plan

This is a large single-module project with 1,996 Go source files. Run Phase 2 separately for each logical module in priority order:

| # | Module | Files | Endpoints | Recommended? | Command |
|---|--------|-------|-----------|-------------|---------|
| 1 | routers/api/v1 | 155 | 475 | ✅ Yes | `Analyze module: api-v1 (path: routers/api/v1/)` |
| 2 | models | 221 | - | ✅ Yes | `Analyze module: models (path: models/)` |
| 3 | services | 343 | - | ✅ Yes | `Analyze module: services (path: services/)` |
| 4 | modules | 713 | - | ✅ Yes | `Analyze module: modules (path: modules/)` |
| 5 | routers/web | 184 | ~500+ web routes | ✅ Yes | `Analyze module: web-routes (path: routers/web/)` |
| 6 | routers/api/packages | 47 | ~200+ package API routes | ✅ Yes | `Analyze module: packages-api (path: routers/api/packages/)` |
| 7 | cmd | 52 | - | ⚠️ Optional | `Analyze module: cmd (path: cmd/)` |

Run each in a separate kiro-cli session. Paste the Phase 2 prompt and specify the module.

## Notes

- The `routers/api/v1/` module is the highest priority as it contains the full REST API surface.
- The `models/` module should be analyzed second to understand entity relationships and data flow.
- The `services/` module contains business logic that bridges routers and models.
- The `modules/` module is the largest (713 files) and contains infrastructure code (queue, storage, indexer, git operations, etc.).
- The `routers/web/` module handles the web UI and has its own route registration in `routers/web/web.go`.
- The `routers/api/packages/` module implements 20+ package manager protocol APIs (npm, PyPI, Docker, etc.).
