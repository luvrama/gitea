# Moving pin reorders other pins - shifts up or down depending on direction

> God node · 78 connections · `models/issues/issue_pin.go`

**Community:** [[Controller: Pin order is assigned as max existing order + 1 when pinning]]

## Connections by Relation

### enforces
- [[POST /api/v1/user/gpg_keys]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies]] `EXTRACTED`
- [[POST /api/v1/orgs]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks]] `EXTRACTED`
- [[PATCH /api/v1/admin/users/{username}]] `EXTRACTED`
- [[PATCH /api/v1/repos/{owner}/{repo}]] `EXTRACTED`
- [[PUT /api/v1/notifications]] `EXTRACTED`
- [[POST /api/v1/orgs/{org}/hooks]] `EXTRACTED`
- [[PUT /api/v1/user/blocks/{username}]] `EXTRACTED`
- [[DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies]] `EXTRACTED`
- [[DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/releases]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels]] `EXTRACTED`
- [[PATCH /api/v1/repos/{owner}/{repo}/pulls/{index}]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/branch_protections]] `EXTRACTED`
- [[POST /api/v1/user/keys]] `EXTRACTED`
- [[DELETE /api/v1/user/keys/{id}]] `EXTRACTED`
- [[POST /api/v1/repos/{owner}/{repo}/push_mirrors]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*