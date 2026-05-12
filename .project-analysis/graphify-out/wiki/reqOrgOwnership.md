# reqOrgOwnership

> God node · 27 connections · `routers/api/v1/api.go`

**Community:** [[Controller: reqOrgOwnership]]

## Connections by Relation

### calls
- [[orgAssignment]] `EXTRACTED`
- [[actions_service.GetVariable]] `EXTRACTED`
- [[user.GetContextUserByPathParam]] `EXTRACTED`
- [[orgAssignment(false, true)]] `EXTRACTED`
- [[shared.GetRunner]] `EXTRACTED`
- [[shared.ListRunners]] `EXTRACTED`
- [[shared.GetRegistrationToken]] `EXTRACTED`
- [[orgAssignment(true)]] `EXTRACTED`
- [[actions_service.DeleteVariableByName]] `EXTRACTED`
- [[Action.CreateVariable]] `EXTRACTED`
- [[Action.UpdateVariable]] `EXTRACTED`
- [[Action.ListVariables]] `EXTRACTED`
- [[org.CreateTeam]] `EXTRACTED`
- [[org.EditTeam]] `EXTRACTED`
- [[org_service.DeleteTeam]] `EXTRACTED`

### data_flow
- [[POST /api/v1/orgs/{org}/actions/variables/{variablename}]] `EXTRACTED`
- [[PUT /api/v1/orgs/{org}/actions/variables/{variablename}]] `EXTRACTED`
- [[POST /api/v1/orgs/{org}/teams]] `EXTRACTED`
- [[PATCH /api/v1/teams/{id}]] `EXTRACTED`
- [[DELETE /api/v1/orgs/{org}/members/{username}]] `EXTRACTED`
- [[POST /api/v1/orgs/{org}/actions/runners/registration-token]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/actions/runners]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/actions/variables]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/actions/runners/{runner_id}]] `EXTRACTED`
- [[DELETE /api/v1/orgs/{org}/actions/variables/{variablename}]] `EXTRACTED`
- [[DELETE /api/v1/teams/{id}]] `EXTRACTED`
- [[GET /api/v1/orgs/{org}/actions/variables/{variablename}]] `EXTRACTED`

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*