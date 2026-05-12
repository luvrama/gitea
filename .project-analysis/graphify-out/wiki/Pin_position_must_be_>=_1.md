# Pin position must be >= 1

> God node · 86 connections · `models/issues/issue_pin.go`

**Community:** [[Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M]]

## Connections by Relation

### enforces
- [[POST /api/v1/orgs]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/pulls]] `EXTRACTED`
- [[PATCH /api/v1/admin/users/{username}]] `EXTRACTED`
- [[PATCH /api/v1/repos/{owner}/{repo}]] `EXTRACTED`
- [[GET /api/v1/notifications]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/notifications]] `EXTRACTED`
- [[POST /api/v1/orgs/{org}/hooks]] `EXTRACTED`
- [[PUT /api/v1/user/blocks/{username}]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/commits]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/avatar]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/branch_protections]] `EXTRACTED`
- [[PUT /api/v1/teams/{id}/repos/{org}/{repo}]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun]] `EXTRACTED`
- [[PATCH /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}]] `EXTRACTED`
- [[PUT /api/v1/repos/{owner}/{repo}/notifications]] `EXTRACTED`
- [[POST /api/v1/orgs/{org}/actions/variables/{variablename}]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*