# Final Evaluation Summary

## Queries

**Q1:** List all API endpoints related to repository management. For each, provide: HTTP method, URL path, handler function, file location, and what authentication/permissions are required.

**Q2:** If I need to add a new webhook event type, what files across routers, services, and models need to change? Trace the full webhook delivery pipeline.

**Q3:** What is the complete data flow when a user creates a pull request via the API? Trace from the HTTP handler through services, git operations, notifications, and database writes.

**Q4:** What are all the external services called during a repository fork operation? List every network call, timeout configuration, and error handling for each.

**Q5:** If I change the user table schema to add a "department" field, list every API endpoint, service, model, and DTO that references the user entity.

**Q6:** Document the complete permission checking chain for the repository API. How does a request go from authentication through org membership, team permissions, collaborator checks, to the final allow/deny?

**Q7:** What are all the API endpoints that trigger git operations? For each, list the git command executed, timeout configured, and what happens on failure.

**Q8:** Map the complete notification system: what events trigger notifications, how are they stored, and which API endpoints serve them? List every file involved.

**Q9:** If the database connection pool is exhausted, which API endpoints are affected and how do they handle it? Trace the error propagation path.

**Q10:** List every API endpoint that performs file I/O operations (reading/writing to disk). What happens to each endpoint if the filesystem becomes read-only?

**Q11:** If the convert.ToUser function changes its signature, which API endpoints directly call this function and would need to be updated? List only endpoints that directly invoke convert.ToUser.

**Q12:** Which controllers share the most service dependencies? Identify the top 5 most tightly coupled controller pairs and list what services they share.

**Q13:** What is the complete dependency chain from the admin hooks endpoint (DELETE /api/v1/admin/hooks/{id}) down to the database layer? List every function call in the chain.

**Q14:** Which API endpoints are in the same code community as the repository model (repo_model.Repository)? What do they have in common?

**Q15:** What are the top 5 most connected components (god nodes) in the codebase and which API endpoints depend on each?

**Q16:** Bug: GET /repos/{owner}/{repo}/actions/runs and GET /repos/{owner}/{repo}/actions/jobs require owner permissions but should only require read access. The routes are declared via addActionsRoutes which uses reqOwner() or reqOrgOwnership(). Which file(s) need to change to fix this permissions issue?

**Q17:** Bug: The workflow job API response does not report individual step statuses correctly - all steps show the same status as the overall job. Which file in the convert/services layer handles the conversion of action job data to API response format?

**Q18:** Bug: When merging a pull request with an invalid commit ID, the API returns an empty JSON response instead of a proper 409 error. Which file handles the pull request merge API endpoint?

**Q19:** Bug: Smart HTTP git requests are not checking the correct permission scope - they use repo-level scope when they should check specific unit scope. Which file handles the permission context for git operations?

**Q20:** Bug: The API for listing packages does not correctly filter by private/internal visibility - it shows private packages to users who should not see them. Which file handles package source permission checks?

**Q21:** Bug: Actions API route for listing runners at the organization level requires owner permission but should only require admin permission on the org. Which file defines the API route groups and their middleware?


## Cost Comparison (All 21 Queries)

| Q | Baseline Credits | 3-Stage Credits | Source | Savings |
|---|-----------------|----------------|--------|---------|
| Q1 | 3.52 | 1.58 | wiki | 55% |
| Q2 | 3.23 | 0.91 | wiki | 72% |
| Q3 | 3.66 | 0.88 | wiki | 76% |
| Q4 | 6.28 | 0.63 | wiki | 90% |
| Q5 | 3.82 | 1.14 | wiki | 70% |
| Q6 | 5.10 | 1.03 | wiki | 80% |
| Q7 | 15.47 | 1.05 | wiki | 93% |
| Q8 | 2.69 | 0.90 | wiki | 67% |
| Q9 | 3.76 | 1.01 | wiki | 73% |
| Q10 | 7.85 | 1.27 | wiki | 84% |
| Q11 | 4.08 | 1.15 | graph | 72% |
| Q12 | 1.06 | 2.66 | graph | -151% |
| Q13 | 1.85 | 1.47 | graph | 21% |
| Q14 | 2.20 | 0.67 | graph | 70% |
| Q15 | 4.12 | 1.80 | graph | 56% |
| Q16 | 1.48 | 0.78 | graph | 47% |
| Q17 | 0.38 | 0.29 | graph | 24% |
| Q18 | 0.20 | 0.17 | graph | 15% |
| Q19 | 1.14 | 1.52 | graph | -33% |
| Q20 | 1.16 | 0.41 | graph | 65% |
| Q21 | 0.79 | 0.28 | graph | 65% |
| **Avg** | **3.52** | **1.03** | | **71%** |

## Aggregate Metrics

- Total baseline credits: 73.84
- Total 3-stage credits: 21.60
- Average baseline: 3.52 credits/query
- Average 3-stage: 1.03 credits/query
- Cost reduction: 71%
- Queries where 3-stage is cheaper: 19/21