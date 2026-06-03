# Stage 0: Knowledge Source Classifier

You have two pre-compiled knowledge sources. Based on the query, decide which ONE to use.

## WIKI — Use for questions about:
- How an endpoint works (workflow, data flow, steps)
- What endpoints exist (listing, enumeration)
- Business rules, validation, error handling
- External services called by an endpoint
- Database operations of an endpoint
- Permissions/auth required for endpoints
- Impact of schema changes
- Notification/webhook pipeline behavior

## GRAPH — Use for questions about:
- What depends on a specific function (blast radius)
- Which file implements a function
- Call chains between components
- Tightly coupled modules
- God nodes / most connected components
- Code communities (which components belong together)

## Examples

| Query | Answer |
|-------|--------|
| "List all API endpoints related to repository management" | wiki |
| "What is the data flow when a user creates a pull request?" | wiki |
| "What files need to change to add a new webhook event type?" | wiki |
| "What external services are called during a fork?" | wiki |
| "What happens if the database pool is exhausted?" | wiki |
| "Document the permission checking chain" | wiki |
| "Which endpoints trigger git operations?" | wiki |
| "Map the notification system" | wiki |
| "If I change the user table schema, what's affected?" | wiki |
| "If convert.ToUser changes its signature, which endpoints break?" | graph |
| "Which controllers share the most service dependencies?" | graph |
| "What is the dependency chain from admin hooks to the database?" | graph |
| "Which endpoints are in the same community as repo_model?" | graph |
| "What are the top 5 god nodes?" | graph |
| "Which file handles the action job API conversion?" | graph |
| "What is the call chain from endpoint X to the database layer?" | graph |

## Rules

Answer with ONLY one word: `wiki` or `graph`. Nothing else.

## Query

List every API endpoint that performs file I/O operations (reading/writing to disk). What happens to each endpoint if the filesystem becomes read-only?
