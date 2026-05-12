# Controller: GET /api/v1/repos/{owner}/{repo}/commits

> 38 nodes · cohesion 0.08

## Key Concepts

- **GET /api/v1/repos/{owner}/{repo}/commits** (19 connections) — `session_32/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}** (12 connections) — `session_32/api_contracts.json`
- **GET /api/v1/repos/{owner}/{repo}/git/notes/{sha}** (12 connections) — `session_44/api_contracts.json`
- **convert.ToCommit** (7 connections) — `session_44/impact_analysis_index.json`
- **repository** (5 connections) — `routers/api/v1/repo/commits.go`
- **GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}** (5 connections) — `session_32/api_contracts.json`
- **git.Commit** (3 connections) — `session_32/impact_analysis_index.json`
- **git.Commit.CommitsByRange / CommitsByFileAndRange** (3 connections) — `modules/git/commit.go`
- **git.GetNote** (3 connections) — `modules/git/notes_nogogit.go`
- **git.Repository.ConvertToGitID** (3 connections) — `modules/git/repo.go`
- **git.Repository.GetBranchCommit / GetCommit** (3 connections) — `modules/git/repo_commit.go`
- **git.Repository.GetCommit** (3 connections) — `modules/git/repo_commit.go`
- **gitrepo.CommitsCount** (3 connections) — `modules/gitrepo/commit.go`
- **repo.getCommit** (3 connections) — `routers/api/v1/repo/commits.go`
- **repo.getNote** (3 connections) — `routers/api/v1/repo/notes.go`
- **repository** (2 connections) — `routers/api/v1/repo/notes.go`
- **api.Commit** (2 connections) — `session_32/impact_analysis_index.json`
- **convert.ToCommit (loop)** (2 connections) — `services/convert/git_commit.go`
- **git.GetRawDiff** (2 connections) — `session_32/impact_analysis_index.json`
- **repo.DownloadCommitDiffOrPatch** (2 connections) — `routers/api/v1/repo/commits.go`
- **repo.GetAllCommits** (2 connections) — `routers/api/v1/repo/commits.go`
- **repo.GetNote** (2 connections) — `routers/api/v1/repo/notes.go`
- **repo.GetSingleCommit** (2 connections) — `routers/api/v1/repo/commits.go`
- **api.SwaggerURL** (1 connections) — `modules/setting/api.go`
- **git.CommitsRangeSize** (1 connections) — `modules/setting/git.go`
- *... and 13 more nodes in this community*

## Relationships

- [[Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge]] (3 shared connections)
- [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]] (3 shared connections)
- [[Endpoint: routers]] (2 shared connections)
- [[Controller: IsNewPinAllowed compares current pin count against MaxPinned setting]] (2 shared connections)
- [[Controller: Pin order is assigned as max existing order + 1 when pinning]] (2 shared connections)

## Source Files

- `modules/git/commit.go`
- `modules/git/notes_nogogit.go`
- `modules/git/repo.go`
- `modules/git/repo_commit.go`
- `modules/gitrepo/commit.go`
- `modules/setting/api.go`
- `modules/setting/git.go`
- `routers/api/v1/repo/commits.go`
- `routers/api/v1/repo/notes.go`
- `services/convert/git_commit.go`
- `session_32/api_contracts.json`
- `session_32/error_handling.json`
- `session_32/impact_analysis_index.json`
- `session_44/api_contracts.json`
- `session_44/error_handling.json`
- `session_44/impact_analysis_index.json`

## Audit Trail

- EXTRACTED: 118 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*