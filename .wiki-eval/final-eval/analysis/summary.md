# Final Evaluation Summary

## Cost Comparison (All 21 Queries)

| Q | Query | Baseline Credits | 3-Stage Credits | Source | Savings |
|---|-------|-----------------|----------------|--------|---------|
| Q1 | List all API endpoints related to repository manag... | 3.52 | 1.58 | wiki | 55% |
| Q2 | If I need to add a new webhook event type, what fi... | 3.23 | 0.91 | wiki | 72% |
| Q3 | What is the complete data flow when a user creates... | 3.66 | 0.88 | wiki | 76% |
| Q4 | What are all the external services called during a... | 6.28 | 0.63 | wiki | 90% |
| Q5 | If I change the user table schema to add a "depart... | 3.82 | 1.14 | wiki | 70% |
| Q6 | Document the complete permission checking chain fo... | 5.10 | 1.03 | wiki | 80% |
| Q7 | What are all the API endpoints that trigger git op... | 15.47 | 1.05 | wiki | 93% |
| Q8 | Map the complete notification system: what events ... | 2.69 | 0.90 | wiki | 67% |
| Q9 | If the database connection pool is exhausted, whic... | 3.76 | 1.01 | wiki | 73% |
| Q10 | List every API endpoint that performs file I/O ope... | 7.85 | 1.27 | wiki | 84% |
| Q11 | If the convert.ToUser function changes its signatu... | 4.08 | 1.15 | graph | 72% |
| Q12 | Which controllers share the most service dependenc... | 1.06 | 2.66 | graph | -151% |
| Q13 | What is the complete dependency chain from the adm... | 1.85 | 1.47 | graph | 21% |
| Q14 | Which API endpoints are in the same code community... | 2.20 | 0.67 | graph | 70% |
| Q15 | What are the top 5 most connected components (god ... | 4.12 | 1.80 | graph | 56% |
| Q16 | Bug: GET /repos/{owner}/{repo}/actions/runs and GE... | 1.48 | 0.78 | graph | 47% |
| Q17 | Bug: The workflow job API response does not report... | 0.38 | 0.29 | graph | 24% |
| Q18 | Bug: When merging a pull request with an invalid c... | 0.20 | 0.17 | graph | 15% |
| Q19 | Bug: Smart HTTP git requests are not checking the ... | 1.14 | 1.52 | graph | -33% |
| Q20 | Bug: The API for listing packages does not correct... | 1.16 | 0.41 | graph | 65% |
| Q21 | Bug: Actions API route for listing runners at the ... | 0.79 | 0.28 | graph | 65% |
| **Avg** | | **3.52** | **1.03** | | **71%** |

## Aggregate Metrics

- Total baseline credits: 73.84
- Total 3-stage credits: 21.60
- Average baseline: 3.52 credits/query
- Average 3-stage: 1.03 credits/query
- Cost reduction: 71%