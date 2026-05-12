# convert.ToUser

> God node · 28 connections · `session_48/impact_analysis_index.json`

**Community:** [[Controller: user_model.User]]

## Connections by Relation

### calls
- [[user_model.SearchUsers]] `EXTRACTED`
- [[user_service.UpdateUser]] `EXTRACTED`
- [[shared.ListBlocks]] `EXTRACTED`
- [[BlockingList.LoadAttributes]] `EXTRACTED`
- [[mailer.SendRegisterNotifyMail]] `EXTRACTED`
- [[user.GetInfo]] `EXTRACTED`
- [[issues_model.CountIssueWatchers]] `EXTRACTED`
- [[repo_model.GetStargazers]] `EXTRACTED`
- [[repo_model.GetRepoWatchers]] `EXTRACTED`
- [[user.GetAuthenticatedUser]] `EXTRACTED`

### data_flow
- [[PATCH /api/v1/admin/users/{username}]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions]] `EXTRACTED`
- [[GET /api/v1/user/blocks]] `EXTRACTED`
- [[GET /api/v1/admin/users]] `EXTRACTED`

### serves
- [[POST /api/v1/admin/users]] `EXTRACTED`
- [[GET /api/v1/users/search]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/members]] `EXTRACTED`
- [[GET /api/v1/users/{username}/followers]] `EXTRACTED`
- [[GET /api/v1/user/followers]] `EXTRACTED`
- [[GET /api/v1/user/following]] `EXTRACTED`
- [[GET /api/v1/users/{username}]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/blocks]] `EXTRACTED`
- [[GET /api/v1/teams/{id}/members/{username}]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/public_members]] `EXTRACTED`
- [[GET /api/v1/teams/{id}/members]] `EXTRACTED`
- [[GET /api/v1/user]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/stargazers]] `EXTRACTED`
- [[GET /api/v1/repos/{owner}/{repo}/subscribers]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*