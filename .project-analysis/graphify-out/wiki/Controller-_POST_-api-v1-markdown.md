# Controller: POST /api/v1/markdown

> 23 nodes · cohesion 0.11

## Key Concepts

- **POST /api/v1/markdown** (16 connections) — `session_2/api_contracts.json`
- **POST /api/v1/markup** (9 connections) — `session_1/api_contracts.json`
- **POST /api/v1/markdown/raw** (6 connections) — `session_2/api_contracts.json`
- **common.RenderMarkup** (6 connections) — `session_2/impact_analysis_index.json`
- **miscellaneous** (4 connections) — `routers/api/v1/misc/markup.go`
- **misc.Markdown** (3 connections) — `routers/api/v1/misc/markup.go`
- **bind[MarkdownOption]** (2 connections) — `routers/api/v1/api.go`
- **markdown.RenderRaw** (2 connections) — `session_2/impact_analysis_index.json`
- **markdown.RenderRaw / markup.Render** (2 connections) — `modules/markup/markdown/markdown.go`
- **markup.Render** (2 connections) — `modules/markup/render.go`
- **misc.MarkdownRaw** (2 connections) — `routers/api/v1/misc/markup.go`
- **misc.Markup** (2 connections) — `routers/api/v1/misc/markup.go`
- **setting.AppSubURL** (1 connections) — `modules/setting/server.go`
- **misc.Markdown** (1 connections) — `session_2/api_contracts.json`
- **misc.MarkdownRaw** (1 connections) — `session_2/api_contracts.json`
- **misc.Markup** (1 connections) — `session_1/api_contracts.json`
- **422 Invalid JSON body or missing required fields** (1 connections) — `session_2/error_handling.json`
- **422 Mode not in [empty, markdown, gfm, comment, wiki, file]** (1 connections) — `session_2/error_handling.json`
- **422 Unable to find renderer for content** (1 connections) — `session_2/error_handling.json`
- **500 Internal markdown rendering failure** (1 connections) — `session_2/error_handling.json`
- **500 Internal markdown rendering failure** (1 connections) — `session_2/error_handling.json`
- **MarkdownOption** (1 connections) — `session_2/impact_analysis_index.json`
- **structs.MarkupOption** (1 connections) — `session_1/impact_analysis_index.json`

## Relationships

- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (3 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (2 shared connections)
- [[Endpoint: routers]] (1 shared connections)
- [[Controller: Pinned issues are separated by type (issues vs pull requests)]] (1 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (1 shared connections)
- [[Controller: convert]] (1 shared connections)

## Source Files

- `modules/markup/markdown/markdown.go`
- `modules/markup/render.go`
- `modules/setting/server.go`
- `routers/api/v1/api.go`
- `routers/api/v1/misc/markup.go`
- `session_1/api_contracts.json`
- `session_1/impact_analysis_index.json`
- `session_2/api_contracts.json`
- `session_2/error_handling.json`
- `session_2/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 67 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*