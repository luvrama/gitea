# Stage 1: Wiki Page Selector

You are a page selection agent. Given a developer's query about a codebase and an index of pre-compiled wiki pages, select the most relevant pages that would help answer the query.

## Rules

- Return ONLY a JSON array of page paths
- Select between 3-15 pages depending on query scope
- Do NOT select more than 15 pages — quality over quantity

## Page Selection Strategy

1. **For "list all" or enumeration queries:** Select `modules/routers.md` (contains the COMPLETE endpoint listing with method, path, description, and auth for all 475 endpoints). Do NOT select dozens of individual endpoint pages — the module overview already has the listing.

2. **For specific endpoint detail queries:** Select the relevant individual endpoint pages (endpoints/ep-NNN.md) which contain workflow, database ops, and business rules.

3. **For cross-cutting queries** (resilience, external services, impact analysis): Select the relevant overview pages (external/overview.md, resiliency/overview.md, datastores/databases.md) PLUS specific endpoint pages that are most relevant.

4. **Always include README.md** for project context.

## Selection Validation

Before returning, verify:
- If the query asks for "all endpoints" of a type → did you include `modules/routers.md`?
- If the query is about external services or failures → did you include `external/overview.md`?
- If the query is about database/schema → did you include `datastores/databases.md`?
- Are you under 15 pages? If over, drop individual endpoint pages in favor of overview pages.

## Output Format

Return ONLY a JSON array. No explanation.
```json
["README.md", "modules/routers.md"]
```

## Wiki Page Index

```json
[
  {
    "path": "README.md",
    "title": "gitea",
    "summary": "**Go** \u00b7 **go-chi/chi v5 + XORM** \u00b7 **Make** \u00b7 475 endpoints \u00b7 1 modules"
  },
  {
    "path": "config/overview.md",
    "title": "Configuration",
    "summary": "**109 properties**"
  },
  {
    "path": "datastores/caches.md",
    "title": "Cache Stores",
    "summary": "**1 stores**"
  },
  {
    "path": "datastores/databases.md",
    "title": "Database Tables",
    "summary": "**94 stores**"
  },
  {
    "path": "datastores/queues.md",
    "title": "Message Queues",
    "summary": "**4 stores**"
  },
  {
    "path": "endpoints/ep-001.md",
    "title": "GET /api/v1/version",
    "summary": "Returns the version of the Gitea application"
  },
  {
    "path": "endpoints/ep-002.md",
    "title": "GET /api/v1/label/templates",
    "summary": "Returns a list of all label template display names"
  },
  {
    "path": "endpoints/ep-003.md",
    "title": "GET /api/v1/label/templates/{name}",
    "summary": "Returns all labels in a specific label template"
  },
  {
    "path": "endpoints/ep-004.md",
    "title": "GET /api/v1/signing-key.gpg",
    "summary": "Returns the GPG public key of the default signing key"
  },
  {
    "path": "endpoints/ep-005.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/signing-key.gpg",
    "summary": "Returns the GPG signing key for a given repository"
  },
  {
    "path": "endpoints/ep-006.md",
    "title": "GET /api/v1/signing-key.pub",
    "summary": "Returns the SSH public key of the default signing key"
  },
  {
    "path": "endpoints/ep-007.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/signing-key.pub",
    "summary": "Returns the SSH signing key for a given repository"
  },
  {
    "path": "endpoints/ep-008.md",
    "title": "POST /api/v1/markup",
    "summary": "Renders a markup document as HTML supporting multiple modes (markdown, comment, wiki, file, gfm)"
  },
  {
    "path": "endpoints/ep-009.md",
    "title": "POST /api/v1/markdown",
    "summary": "Render a markdown document as HTML"
  },
  {
    "path": "endpoints/ep-010.md",
    "title": "POST /api/v1/markdown/raw",
    "summary": "Render raw markdown as HTML (no special link handling)"
  },
  {
    "path": "endpoints/ep-011.md",
    "title": "GET /api/v1/gitignore/templates",
    "summary": "Returns a list of all gitignore template names"
  },
  {
    "path": "endpoints/ep-012.md",
    "title": "GET /api/v1/gitignore/templates/{name}",
    "summary": "Returns information about a specific gitignore template"
  },
  {
    "path": "endpoints/ep-013.md",
    "title": "GET /api/v1/licenses",
    "summary": "Returns a list of all license templates with metadata"
  },
  {
    "path": "endpoints/ep-014.md",
    "title": "GET /api/v1/licenses/{name}",
    "summary": "Returns full information about a specific license template including body text"
  },
  {
    "path": "endpoints/ep-015.md",
    "title": "GET /api/v1/settings/ui",
    "summary": "Returns instance's global UI settings including default theme, allowed reactions, and custom emojis"
  },
  {
    "path": "endpoints/ep-016.md",
    "title": "GET /api/v1/settings/api",
    "summary": "Returns instance's global API settings including pagination defaults and size limits"
  },
  {
    "path": "endpoints/ep-017.md",
    "title": "GET /api/v1/settings/repository",
    "summary": "Returns instance's global repository settings indicating which features are disabled"
  },
  {
    "path": "endpoints/ep-018.md",
    "title": "GET /api/v1/settings/attachment",
    "summary": "Returns instance's global attachment settings including allowed types, max size, and max files"
  },
  {
    "path": "endpoints/ep-019.md",
    "title": "GET /api/v1/notifications",
    "summary": "List current user's notification threads with filtering by status, subject type, and time range"
  },
  {
    "path": "endpoints/ep-020.md",
    "title": "PUT /api/v1/notifications",
    "summary": "Mark notification threads as read, unread, or pinned for the current user"
  },
  {
    "path": "endpoints/ep-021.md",
    "title": "GET /api/v1/notifications/new",
    "summary": "Check if unread notifications exist and return the count"
  },
  {
    "path": "endpoints/ep-022.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/notifications",
    "summary": "List current user's notification threads for a specific repository"
  },
  {
    "path": "endpoints/ep-023.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/notifications",
    "summary": "Mark notification threads as read, pinned or unread on a specific repo"
  },
  {
    "path": "endpoints/ep-024.md",
    "title": "GET /api/v1/notifications/threads/{id}",
    "summary": "Get notification thread by ID"
  },
  {
    "path": "endpoints/ep-025.md",
    "title": "PATCH /api/v1/notifications/threads/{id}",
    "summary": "Mark notification thread as read by ID"
  },
  {
    "path": "endpoints/ep-026.md",
    "title": "GET /api/v1/user/orgs",
    "summary": "List the current user's organizations"
  },
  {
    "path": "endpoints/ep-027.md",
    "title": "GET /api/v1/users/{username}/orgs",
    "summary": "List a user's organizations"
  },
  {
    "path": "endpoints/ep-028.md",
    "title": "GET /api/v1/users/{username}/orgs/{org}/permissions",
    "summary": "Get user permissions in organization"
  },
  {
    "path": "endpoints/ep-029.md",
    "title": "GET /api/v1/orgs",
    "summary": "Get list of all organizations visible to the current user"
  },
  {
    "path": "endpoints/ep-030.md",
    "title": "POST /api/v1/orgs",
    "summary": "Create a new organization"
  },
  {
    "path": "endpoints/ep-031.md",
    "title": "GET /api/v1/orgs/{org}",
    "summary": "Get details of a specific organization"
  },
  {
    "path": "endpoints/ep-032.md",
    "title": "POST /api/v1/orgs/{org}/rename",
    "summary": "Rename an organization"
  },
  {
    "path": "endpoints/ep-033.md",
    "title": "PATCH /api/v1/orgs/{org}",
    "summary": "Edit an organization's information"
  },
  {
    "path": "endpoints/ep-034.md",
    "title": "DELETE /api/v1/orgs/{org}",
    "summary": "Delete an organization"
  },
  {
    "path": "endpoints/ep-035.md",
    "title": "GET /api/v1/orgs/{org}/activities/feeds",
    "summary": "List an organization's activity feeds"
  },
  {
    "path": "endpoints/ep-036.md",
    "title": "DELETE /api/v1/orgs/{org}/repos",
    "summary": "Delete all repositories in an organization (async background deletion)"
  },
  {
    "path": "endpoints/ep-037.md",
    "title": "POST /api/v1/orgs/{org}/avatar",
    "summary": "Update the avatar of an organization"
  },
  {
    "path": "endpoints/ep-038.md",
    "title": "DELETE /api/v1/orgs/{org}/avatar",
    "summary": "Delete the avatar of an organization"
  },
  {
    "path": "endpoints/ep-039.md",
    "title": "GET /api/v1/orgs/{org}/actions/secrets",
    "summary": "List an organization's actions secrets"
  },
  {
    "path": "endpoints/ep-040.md",
    "title": "PUT /api/v1/orgs/{org}/actions/secrets/{secretname}",
    "summary": "Create or update a secret value in an organization"
  },
  {
    "path": "endpoints/ep-041.md",
    "title": "DELETE /api/v1/orgs/{org}/actions/secrets/{secretname}",
    "summary": "Delete a secret in an organization"
  },
  {
    "path": "endpoints/ep-042.md",
    "title": "POST /api/v1/orgs/{org}/actions/runners/registration-token",
    "summary": "Get an organization's actions runner registration token"
  },
  {
    "path": "endpoints/ep-043.md",
    "title": "GET /api/v1/orgs/{org}/actions/variables",
    "summary": "Get an org-level variables list"
  },
  {
    "path": "endpoints/ep-044.md",
    "title": "GET /api/v1/orgs/{org}/actions/variables/{variablename}",
    "summary": "Get an org-level variable by name"
  },
  {
    "path": "endpoints/ep-045.md",
    "title": "DELETE /api/v1/orgs/{org}/actions/variables/{variablename}",
    "summary": "Delete an org-level variable by name"
  },
  {
    "path": "endpoints/ep-046.md",
    "title": "POST /api/v1/orgs/{org}/actions/variables/{variablename}",
    "summary": "Create an org-level variable"
  },
  {
    "path": "endpoints/ep-047.md",
    "title": "PUT /api/v1/orgs/{org}/actions/variables/{variablename}",
    "summary": "Update an org-level variable"
  },
  {
    "path": "endpoints/ep-048.md",
    "title": "GET /api/v1/orgs/{org}/actions/runners",
    "summary": "Get org-level runners list"
  },
  {
    "path": "endpoints/ep-049.md",
    "title": "GET /api/v1/orgs/{org}/actions/runners/{runner_id}",
    "summary": "Get a specific org-level runner by ID"
  },
  {
    "path": "endpoints/ep-050.md",
    "title": "DELETE /api/v1/orgs/{org}/actions/runners/{runner_id}",
    "summary": "Delete an org-level runner"
  },
  {
    "path": "endpoints/ep-051.md",
    "title": "PATCH /api/v1/orgs/{org}/actions/runners/{runner_id}",
    "summary": "Update an org-level runner (enable/disable)"
  },
  {
    "path": "endpoints/ep-052.md",
    "title": "GET /api/v1/orgs/{org}/actions/jobs",
    "summary": "Get org-level workflow jobs"
  },
  {
    "path": "endpoints/ep-053.md",
    "title": "GET /api/v1/orgs/{org}/actions/runs",
    "summary": "Get org-level workflow runs"
  },
  {
    "path": "endpoints/ep-054.md",
    "title": "GET /api/v1/orgs/{org}/teams",
    "summary": "List an organization's teams"
  },
  {
    "path": "endpoints/ep-055.md",
    "title": "GET /api/v1/user/teams",
    "summary": "List all the teams a user belongs to"
  },
  {
    "path": "endpoints/ep-056.md",
    "title": "GET /api/v1/teams/{id}",
    "summary": "Get a team by its ID"
  },
  {
    "path": "endpoints/ep-057.md",
    "title": "POST /api/v1/orgs/{org}/teams",
    "summary": "Create a team in an organization"
  },
  {
    "path": "endpoints/ep-058.md",
    "title": "PATCH /api/v1/teams/{id}",
    "summary": "Edit a team"
  },
  {
    "path": "endpoints/ep-059.md",
    "title": "DELETE /api/v1/teams/{id}",
    "summary": "Delete a team"
  },
  {
    "path": "endpoints/ep-060.md",
    "title": "GET /api/v1/teams/{id}/members",
    "summary": "List a team's members"
  },
  {
    "path": "endpoints/ep-061.md",
    "title": "GET /api/v1/teams/{id}/members/{username}",
    "summary": "Get a particular member of a team"
  },
  {
    "path": "endpoints/ep-062.md",
    "title": "PUT /api/v1/teams/{id}/members/{username}",
    "summary": "Add a team member"
  },
  {
    "path": "endpoints/ep-063.md",
    "title": "DELETE /api/v1/teams/{id}/members/{username}",
    "summary": "Remove a team member"
  },
  {
    "path": "endpoints/ep-064.md",
    "title": "GET /api/v1/teams/{id}/repos",
    "summary": "List all repositories belonging to a team"
  },
  {
    "path": "endpoints/ep-065.md",
    "title": "GET /api/v1/teams/{id}/repos/{org}/{repo}",
    "summary": "Get a particular repository of a team"
  },
  {
    "path": "endpoints/ep-066.md",
    "title": "PUT /api/v1/teams/{id}/repos/{org}/{repo}",
    "summary": "Add a repository to a team"
  },
  {
    "path": "endpoints/ep-067.md",
    "title": "DELETE /api/v1/teams/{id}/repos/{org}/{repo}",
    "summary": "Remove a repository from a team (does not delete the repository)"
  },
  {
    "path": "endpoints/ep-068.md",
    "title": "GET /api/v1/orgs/{org}/teams/search",
    "summary": "Search for teams within an organization"
  },
  {
    "path": "endpoints/ep-069.md",
    "title": "GET /api/v1/teams/{id}/activities/feeds",
    "summary": "List a team's activity feeds"
  },
  {
    "path": "endpoints/ep-070.md",
    "title": "GET /api/v1/orgs/{org}/members",
    "summary": "List an organization's members. If the doer is a member or admin, shows all members; otherwise shows only public members"
  },
  {
    "path": "endpoints/ep-071.md",
    "title": "GET /api/v1/orgs/{org}/public_members",
    "summary": "List an organization's public members. Always shows only public members regardless of authentication."
  },
  {
    "path": "endpoints/ep-072.md",
    "title": "GET /api/v1/orgs/{org}/members/{username}",
    "summary": "Check if a user is a member of an organization. Returns 204 if member, 303 redirect to public_members check if doer is n"
  },
  {
    "path": "endpoints/ep-073.md",
    "title": "GET /api/v1/orgs/{org}/public_members/{username}",
    "summary": "Check if a user is a public member of an organization. Returns 204 if public member, 404 otherwise."
  },
  {
    "path": "endpoints/ep-074.md",
    "title": "PUT /api/v1/orgs/{org}/public_members/{username}",
    "summary": "Publicize a user's membership in an organization. Sets is_public=true on the org_user record."
  },
  {
    "path": "endpoints/ep-075.md",
    "title": "DELETE /api/v1/orgs/{org}/public_members/{username}",
    "summary": "Conceal a user's membership in an organization. Sets is_public=false on the org_user record."
  },
  {
    "path": "endpoints/ep-076.md",
    "title": "DELETE /api/v1/orgs/{org}/members/{username}",
    "summary": "Remove a member from an organization. Removes from all teams, deletes repo access, unwatches repos."
  },
  {
    "path": "endpoints/ep-077.md",
    "title": "GET /api/v1/orgs/{org}/hooks",
    "summary": "List an organization's webhooks"
  },
  {
    "path": "endpoints/ep-078.md",
    "title": "GET /api/v1/orgs/{org}/hooks/{id}",
    "summary": "Get a single organization webhook by ID"
  },
  {
    "path": "endpoints/ep-079.md",
    "title": "POST /api/v1/orgs/{org}/hooks",
    "summary": "Create a webhook for an organization"
  },
  {
    "path": "endpoints/ep-080.md",
    "title": "PATCH /api/v1/orgs/{org}/hooks/{id}",
    "summary": "Update an organization webhook"
  },
  {
    "path": "endpoints/ep-081.md",
    "title": "DELETE /api/v1/orgs/{org}/hooks/{id}",
    "summary": "Delete an organization webhook"
  },
  {
    "path": "endpoints/ep-082.md",
    "title": "GET /api/v1/orgs/{org}/labels",
    "summary": "List an organization's labels"
  },
  {
    "path": "endpoints/ep-083.md",
    "title": "POST /api/v1/orgs/{org}/labels",
    "summary": "Create a label for an organization"
  },
  {
    "path": "endpoints/ep-084.md",
    "title": "GET /api/v1/orgs/{org}/labels/{id}",
    "summary": "Get a single label by ID or name in an organization"
  },
  {
    "path": "endpoints/ep-085.md",
    "title": "PATCH /api/v1/orgs/{org}/labels/{id}",
    "summary": "Update a label in an organization"
  },
  {
    "path": "endpoints/ep-086.md",
    "title": "DELETE /api/v1/orgs/{org}/labels/{id}",
    "summary": "Delete a label from an organization"
  },
  {
    "path": "endpoints/ep-087.md",
    "title": "GET /api/v1/orgs/{org}/blocks",
    "summary": "List users blocked by the organization"
  },
  {
    "path": "endpoints/ep-088.md",
    "title": "GET /api/v1/orgs/{org}/blocks/{username}",
    "summary": "Check if a user is blocked by the organization"
  },
  {
    "path": "endpoints/ep-089.md",
    "title": "PUT /api/v1/orgs/{org}/blocks/{username}",
    "summary": "Block a user from the organization"
  },
  {
    "path": "endpoints/ep-090.md",
    "title": "DELETE /api/v1/orgs/{org}/blocks/{username}",
    "summary": "Unblock a user from the organization"
  },
  {
    "path": "endpoints/ep-091.md",
    "title": "GET /api/v1/admin/hooks",
    "summary": "List system and/or default webhooks with pagination"
  },
  {
    "path": "endpoints/ep-092.md",
    "title": "GET /api/v1/admin/hooks/{id}",
    "summary": "Get a single system or default webhook by ID"
  },
  {
    "path": "endpoints/ep-093.md",
    "title": "POST /api/v1/admin/hooks",
    "summary": "Create a new system or default webhook"
  },
  {
    "path": "endpoints/ep-094.md",
    "title": "PATCH /api/v1/admin/hooks/{id}",
    "summary": "Update an existing system or default webhook"
  },
  {
    "path": "endpoints/ep-095.md",
    "title": "DELETE /api/v1/admin/hooks/{id}",
    "summary": "Delete a system or default webhook and its associated hook tasks"
  },
  {
    "path": "endpoints/ep-096.md",
    "title": "POST /api/v1/admin/users/{username}/orgs",
    "summary": "Create an organization owned by the specified user"
  },
  {
    "path": "endpoints/ep-097.md",
    "title": "GET /api/v1/admin/orgs",
    "summary": "List all organizations with pagination"
  },
  {
    "path": "endpoints/ep-098.md",
    "title": "POST /api/v1/admin/users",
    "summary": "Create a new user account (admin only)"
  },
  {
    "path": "endpoints/ep-099.md",
    "title": "PATCH /api/v1/admin/users/{username}",
    "summary": "Edit an existing user's profile, auth, and permission settings"
  },
  {
    "path": "endpoints/ep-100.md",
    "title": "DELETE /api/v1/admin/users/{username}",
    "summary": "Delete a user account, optionally purging all owned data"
  },
  {
    "path": "endpoints/ep-101.md",
    "title": "POST /api/v1/admin/users/{username}/keys",
    "summary": "Add a public SSH key on behalf of a user"
  },
  {
    "path": "endpoints/ep-102.md",
    "title": "DELETE /api/v1/admin/users/{username}/keys/{id}",
    "summary": "Delete a user's public SSH key"
  },
  {
    "path": "endpoints/ep-103.md",
    "title": "GET /api/v1/admin/users",
    "summary": "Search users with various filter conditions (admin only)"
  },
  {
    "path": "endpoints/ep-104.md",
    "title": "POST /api/v1/admin/users/{username}/rename",
    "summary": "Rename a user account"
  },
  {
    "path": "endpoints/ep-105.md",
    "title": "GET /api/v1/admin/actions/jobs",
    "summary": "List all workflow jobs across all repositories (admin only)"
  },
  {
    "path": "endpoints/ep-106.md",
    "title": "GET /api/v1/admin/actions/runs",
    "summary": "Lists all workflow runs across all repositories (admin-level)"
  },
  {
    "path": "endpoints/ep-107.md",
    "title": "GET /api/v1/admin/unadopted",
    "summary": "Lists unadopted repositories (git repos on disk not tracked in DB)"
  },
  {
    "path": "endpoints/ep-108.md",
    "title": "POST /api/v1/admin/unadopted/{owner}/{repo}",
    "summary": "Adopts unadopted files on disk as a repository tracked in the database"
  },
  {
    "path": "endpoints/ep-109.md",
    "title": "DELETE /api/v1/admin/unadopted/{owner}/{repo}",
    "summary": "Deletes unadopted repository files from the filesystem"
  },
  {
    "path": "endpoints/ep-110.md",
    "title": "GET /api/v1/admin/cron",
    "summary": "Lists all registered cron tasks with their schedule and execution info"
  },
  {
    "path": "endpoints/ep-111.md",
    "title": "POST /api/v1/admin/cron/{task}",
    "summary": "Triggers a cron task to run immediately"
  },
  {
    "path": "endpoints/ep-112.md",
    "title": "POST /api/v1/admin/users/{username}/repos",
    "summary": "Creates a repository on behalf of a user (admin only)"
  },
  {
    "path": "endpoints/ep-113.md",
    "title": "POST /api/v1/admin/actions/runners/registration-token",
    "summary": "Gets or creates a global actions runner registration token"
  },
  {
    "path": "endpoints/ep-114.md",
    "title": "GET /api/v1/admin/actions/runners",
    "summary": "List all global action runners with optional disabled filter"
  },
  {
    "path": "endpoints/ep-115.md",
    "title": "GET /api/v1/admin/actions/runners/{runner_id}",
    "summary": "Get a specific global action runner by ID"
  },
  {
    "path": "endpoints/ep-116.md",
    "title": "DELETE /api/v1/admin/actions/runners/{runner_id}",
    "summary": "Delete a global action runner by ID"
  },
  {
    "path": "endpoints/ep-117.md",
    "title": "PATCH /api/v1/admin/actions/runners/{runner_id}",
    "summary": "Update a global action runner (currently only disable/enable)"
  },
  {
    "path": "endpoints/ep-118.md",
    "title": "GET /api/v1/admin/emails",
    "summary": "List all email addresses in the system with pagination"
  },
  {
    "path": "endpoints/ep-119.md",
    "title": "GET /api/v1/admin/emails/search",
    "summary": "Search all emails by keyword (searches name, full_name, email)"
  },
  {
    "path": "endpoints/ep-120.md",
    "title": "GET /api/v1/admin/users/{username}/badges",
    "summary": "List all badges belonging to a user"
  },
  {
    "path": "endpoints/ep-121.md",
    "title": "POST /api/v1/admin/users/{username}/badges",
    "summary": "Add badges to a user by slug"
  },
  {
    "path": "endpoints/ep-122.md",
    "title": "DELETE /api/v1/admin/users/{username}/badges",
    "summary": "Remove badges from a user by slug"
  },
  {
    "path": "endpoints/ep-123.md",
    "title": "GET /api/v1/users/search",
    "summary": "Search for users by keyword, uid, with pagination"
  },
  {
    "path": "endpoints/ep-124.md",
    "title": "GET /api/v1/users/{username}",
    "summary": "Get a user's public profile information"
  },
  {
    "path": "endpoints/ep-125.md",
    "title": "GET /api/v1/user",
    "summary": "Get the currently authenticated user's full profile"
  },
  {
    "path": "endpoints/ep-126.md",
    "title": "GET /api/v1/users/{username}/heatmap",
    "summary": "Get a user's contribution heatmap data for the past year"
  },
  {
    "path": "endpoints/ep-127.md",
    "title": "GET /api/v1/users/{username}/activities/feeds",
    "summary": "List a user's activity feeds with optional date and performer filters"
  },
  {
    "path": "endpoints/ep-128.md",
    "title": "POST /api/v1/user/avatar",
    "summary": "Update the authenticated user's avatar with a base64-encoded image"
  },
  {
    "path": "endpoints/ep-129.md",
    "title": "DELETE /api/v1/user/avatar",
    "summary": "Deletes the current user's custom avatar"
  },
  {
    "path": "endpoints/ep-130.md",
    "title": "PUT /api/v1/user/actions/secrets/{secretname}",
    "summary": "Creates or updates a secret value in the user scope"
  },
  {
    "path": "endpoints/ep-131.md",
    "title": "DELETE /api/v1/user/actions/secrets/{secretname}",
    "summary": "Deletes a secret in the user scope"
  },
  {
    "path": "endpoints/ep-132.md",
    "title": "POST /api/v1/user/actions/variables/{variablename}",
    "summary": "Creates a user-level variable"
  },
  {
    "path": "endpoints/ep-133.md",
    "title": "PUT /api/v1/user/actions/variables/{variablename}",
    "summary": "Updates a user-level variable created by current doer"
  },
  {
    "path": "endpoints/ep-134.md",
    "title": "DELETE /api/v1/user/actions/variables/{variablename}",
    "summary": "Deletes a user-level variable created by current doer"
  },
  {
    "path": "endpoints/ep-135.md",
    "title": "GET /api/v1/user/actions/variables/{variablename}",
    "summary": "Get a user-level variable which is created by current doer"
  },
  {
    "path": "endpoints/ep-136.md",
    "title": "GET /api/v1/user/actions/variables",
    "summary": "Get the user-level list of variables which is created by current doer"
  },
  {
    "path": "endpoints/ep-137.md",
    "title": "GET /api/v1/user/actions/runs",
    "summary": "Get workflow runs for the authenticated user"
  },
  {
    "path": "endpoints/ep-138.md",
    "title": "GET /api/v1/user/actions/jobs",
    "summary": "Get workflow jobs for the authenticated user"
  },
  {
    "path": "endpoints/ep-139.md",
    "title": "GET /api/v1/user/followers",
    "summary": "List the authenticated user's followers"
  },
  {
    "path": "endpoints/ep-140.md",
    "title": "GET /api/v1/users/{username}/followers",
    "summary": "List the given user's followers"
  },
  {
    "path": "endpoints/ep-141.md",
    "title": "GET /api/v1/user/following",
    "summary": "List the users that the authenticated user is following"
  },
  {
    "path": "endpoints/ep-142.md",
    "title": "GET /api/v1/users/{username}/following",
    "summary": "List the users that the given user is following"
  },
  {
    "path": "endpoints/ep-143.md",
    "title": "GET /api/v1/user/following/{username}",
    "summary": "Check whether a user is followed by the authenticated user"
  },
  {
    "path": "endpoints/ep-144.md",
    "title": "GET /api/v1/users/{username}/following/{target}",
    "summary": "Check if one user is following another user"
  },
  {
    "path": "endpoints/ep-145.md",
    "title": "PUT /api/v1/user/following/{username}",
    "summary": "Follow a user"
  },
  {
    "path": "endpoints/ep-146.md",
    "title": "DELETE /api/v1/user/following/{username}",
    "summary": "Unfollow a user"
  },
  {
    "path": "endpoints/ep-147.md",
    "title": "GET /api/v1/user/hooks",
    "summary": "List the authenticated user's webhooks"
  },
  {
    "path": "endpoints/ep-148.md",
    "title": "GET /api/v1/user/hooks/{id}",
    "summary": "Get a specific webhook of the authenticated user"
  },
  {
    "path": "endpoints/ep-149.md",
    "title": "POST /api/v1/user/hooks",
    "summary": "Create a webhook for the authenticated user"
  },
  {
    "path": "endpoints/ep-150.md",
    "title": "PATCH /api/v1/user/hooks/{id}",
    "summary": "Update a webhook owned by the authenticated user"
  },
  {
    "path": "endpoints/ep-151.md",
    "title": "DELETE /api/v1/user/hooks/{id}",
    "summary": "Delete a webhook owned by the authenticated user"
  },
  {
    "path": "endpoints/ep-152.md",
    "title": "GET /api/v1/users/{username}/starred",
    "summary": "List repos that the given user has starred"
  },
  {
    "path": "endpoints/ep-153.md",
    "title": "GET /api/v1/user/starred",
    "summary": "List repos that the authenticated user has starred"
  },
  {
    "path": "endpoints/ep-154.md",
    "title": "GET /api/v1/user/starred/{owner}/{repo}",
    "summary": "Check whether the authenticated user is starring a repo"
  },
  {
    "path": "endpoints/ep-155.md",
    "title": "PUT /api/v1/user/starred/{owner}/{repo}",
    "summary": "Star the given repo as the authenticated user"
  },
  {
    "path": "endpoints/ep-156.md",
    "title": "DELETE /api/v1/user/starred/{owner}/{repo}",
    "summary": "Unstar the given repo for the authenticated user"
  },
  {
    "path": "endpoints/ep-157.md",
    "title": "GET /api/v1/user/keys",
    "summary": "List the authenticated user's public SSH keys"
  },
  {
    "path": "endpoints/ep-158.md",
    "title": "GET /api/v1/users/{username}/keys",
    "summary": "List the given user's public SSH keys"
  },
  {
    "path": "endpoints/ep-159.md",
    "title": "GET /api/v1/user/keys/{id}",
    "summary": "Get a public key by ID"
  },
  {
    "path": "endpoints/ep-160.md",
    "title": "POST /api/v1/user/keys",
    "summary": "Create a public SSH key for the authenticated user"
  },
  {
    "path": "endpoints/ep-161.md",
    "title": "DELETE /api/v1/user/keys/{id}",
    "summary": "Delete a public SSH key for the authenticated user"
  },
  {
    "path": "endpoints/ep-162.md",
    "title": "GET /api/v1/user/settings",
    "summary": "Get the authenticated user's settings (profile fields and privacy preferences)"
  },
  {
    "path": "endpoints/ep-163.md",
    "title": "PATCH /api/v1/user/settings",
    "summary": "Update the authenticated user's settings"
  },
  {
    "path": "endpoints/ep-164.md",
    "title": "GET /api/v1/users/{username}/tokens",
    "summary": "List the authenticated user's access tokens (requires basic auth or reverse proxy auth)"
  },
  {
    "path": "endpoints/ep-165.md",
    "title": "POST /api/v1/users/{username}/tokens",
    "summary": "Create a new access token for the user"
  },
  {
    "path": "endpoints/ep-166.md",
    "title": "DELETE /api/v1/users/{username}/tokens/{token}",
    "summary": "Delete an access token by ID or name"
  },
  {
    "path": "endpoints/ep-167.md",
    "title": "POST /api/v1/user/applications/oauth2",
    "summary": "Create a new OAuth2 application for the authenticated user"
  },
  {
    "path": "endpoints/ep-168.md",
    "title": "GET /api/v1/user/applications/oauth2",
    "summary": "List the authenticated user's OAuth2 applications"
  },
  {
    "path": "endpoints/ep-169.md",
    "title": "DELETE /api/v1/user/applications/oauth2/{id}",
    "summary": "Delete an OAuth2 application by ID"
  },
  {
    "path": "endpoints/ep-170.md",
    "title": "GET /api/v1/user/applications/oauth2/{id}",
    "summary": "Get a specific OAuth2 application by ID"
  },
  {
    "path": "endpoints/ep-171.md",
    "title": "PATCH /api/v1/user/applications/oauth2/{id}",
    "summary": "Update an OAuth2 application, regenerating the client secret"
  },
  {
    "path": "endpoints/ep-172.md",
    "title": "GET /api/v1/users/{username}/repos",
    "summary": "List the repos owned by the given user"
  },
  {
    "path": "endpoints/ep-173.md",
    "title": "GET /api/v1/user/repos",
    "summary": "List the repos that the authenticated user owns"
  },
  {
    "path": "endpoints/ep-174.md",
    "title": "GET /api/v1/orgs/{org}/repos",
    "summary": "List an organization's repos"
  },
  {
    "path": "endpoints/ep-175.md",
    "title": "POST /api/v1/user/actions/runners/registration-token",
    "summary": "Get a user's actions runner registration token"
  },
  {
    "path": "endpoints/ep-176.md",
    "title": "GET /api/v1/user/actions/runners",
    "summary": "Get user-level action runners"
  },
  {
    "path": "endpoints/ep-177.md",
    "title": "GET /api/v1/user/actions/runners/{runner_id}",
    "summary": "Get a specific user-level action runner by ID"
  },
  {
    "path": "endpoints/ep-178.md",
    "title": "DELETE /api/v1/user/actions/runners/{runner_id}",
    "summary": "Delete a user-level action runner"
  },
  {
    "path": "endpoints/ep-179.md",
    "title": "PATCH /api/v1/user/actions/runners/{runner_id}",
    "summary": "Update a user-level action runner (enable/disable)"
  },
  {
    "path": "endpoints/ep-180.md",
    "title": "GET /api/v1/user/emails",
    "summary": "List the authenticated user's email addresses"
  },
  {
    "path": "endpoints/ep-181.md",
    "title": "POST /api/v1/user/emails",
    "summary": "Add email addresses to the authenticated user"
  },
  {
    "path": "endpoints/ep-182.md",
    "title": "DELETE /api/v1/user/emails",
    "summary": "Delete email addresses from the authenticated user"
  },
  {
    "path": "endpoints/ep-183.md",
    "title": "GET /api/v1/users/{username}/gpg_keys",
    "summary": "List the given user's GPG keys"
  },
  {
    "path": "endpoints/ep-184.md",
    "title": "GET /api/v1/user/gpg_keys",
    "summary": "List the authenticated user's GPG keys"
  },
  {
    "path": "endpoints/ep-185.md",
    "title": "GET /api/v1/user/gpg_keys/{id}",
    "summary": "Get a specific GPG key by ID for the authenticated user"
  },
  {
    "path": "endpoints/ep-186.md",
    "title": "GET /api/v1/user/gpg_key_token",
    "summary": "Get a token to verify GPG key ownership via signature"
  },
  {
    "path": "endpoints/ep-187.md",
    "title": "POST /api/v1/user/gpg_key_verify",
    "summary": "Verify a GPG key by providing a signed token"
  },
  {
    "path": "endpoints/ep-188.md",
    "title": "POST /api/v1/user/gpg_keys",
    "summary": "Create a GPG key for the authenticated user"
  },
  {
    "path": "endpoints/ep-189.md",
    "title": "DELETE /api/v1/user/gpg_keys/{id}",
    "summary": "Remove a GPG key belonging to the authenticated user"
  },
  {
    "path": "endpoints/ep-190.md",
    "title": "GET /api/v1/user/blocks",
    "summary": "List users blocked by the authenticated user"
  },
  {
    "path": "endpoints/ep-191.md",
    "title": "GET /api/v1/user/blocks/{username}",
    "summary": "Check if a user is blocked by the authenticated user"
  },
  {
    "path": "endpoints/ep-192.md",
    "title": "PUT /api/v1/user/blocks/{username}",
    "summary": "Block a user"
  },
  {
    "path": "endpoints/ep-193.md",
    "title": "DELETE /api/v1/user/blocks/{username}",
    "summary": "Unblock a user"
  },
  {
    "path": "endpoints/ep-194.md",
    "title": "GET /api/v1/users/{username}/subscriptions",
    "summary": "List the repositories watched by a user"
  },
  {
    "path": "endpoints/ep-195.md",
    "title": "GET /api/v1/user/subscriptions",
    "summary": "List repositories watched by the authenticated user"
  },
  {
    "path": "endpoints/ep-196.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/subscription",
    "summary": "Check if the current user is watching a repo"
  },
  {
    "path": "endpoints/ep-197.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/subscription",
    "summary": "Watch a repo (subscribe to notifications)"
  },
  {
    "path": "endpoints/ep-198.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/subscription",
    "summary": "Unwatch a repo (unsubscribe from notifications)"
  },
  {
    "path": "endpoints/ep-199.md",
    "title": "GET /api/v1/packages/{owner}",
    "summary": "Gets all packages of an owner"
  },
  {
    "path": "endpoints/ep-200.md",
    "title": "GET /api/v1/packages/{owner}/{type}/{name}/{version}",
    "summary": "Gets a specific package version"
  },
  {
    "path": "endpoints/ep-201.md",
    "title": "DELETE /api/v1/packages/{owner}/{type}/{name}",
    "summary": "Delete a package and all its versions"
  },
  {
    "path": "endpoints/ep-202.md",
    "title": "DELETE /api/v1/packages/{owner}/{type}/{name}/{version}",
    "summary": "Delete a specific version of a package"
  },
  {
    "path": "endpoints/ep-203.md",
    "title": "GET /api/v1/packages/{owner}/{type}/{name}/{version}/files",
    "summary": "Gets all files of a specific package version"
  },
  {
    "path": "endpoints/ep-204.md",
    "title": "GET /api/v1/packages/{owner}/{type}/{name}",
    "summary": "Gets all versions of a specific package"
  },
  {
    "path": "endpoints/ep-205.md",
    "title": "GET /api/v1/packages/{owner}/{type}/{name}/-/latest",
    "summary": "Gets the latest version of a package"
  },
  {
    "path": "endpoints/ep-206.md",
    "title": "POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}",
    "summary": "Link a package to a repository"
  },
  {
    "path": "endpoints/ep-207.md",
    "title": "POST /api/v1/packages/{owner}/{type}/{name}/-/unlink",
    "summary": "Unlink a package from its repository"
  },
  {
    "path": "endpoints/ep-208.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies",
    "summary": "List issues that block the given issue (its dependencies)"
  },
  {
    "path": "endpoints/ep-209.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies",
    "summary": "Make the issue in the URL depend on the issue specified in the body"
  },
  {
    "path": "endpoints/ep-210.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/dependencies",
    "summary": "Remove a dependency from the issue in the URL"
  },
  {
    "path": "endpoints/ep-211.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/blocks",
    "summary": "List issues that are blocked by this issue (issues this issue blocks)"
  },
  {
    "path": "endpoints/ep-212.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/blocks",
    "summary": "Block the issue given in the body by the issue in the URL path"
  },
  {
    "path": "endpoints/ep-213.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/blocks",
    "summary": "Unblock the issue given in the body by the issue in the URL path"
  },
  {
    "path": "endpoints/ep-214.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}",
    "summary": "Get a single commit from a repository by SHA or ref"
  },
  {
    "path": "endpoints/ep-215.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/commits",
    "summary": "Get a list of all commits from a repository with pagination"
  },
  {
    "path": "endpoints/ep-216.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}",
    "summary": "Get a commit's diff or patch output as plain text"
  },
  {
    "path": "endpoints/ep-217.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/commits/{sha}/pull",
    "summary": "Get the merged pull request associated with a commit SHA"
  },
  {
    "path": "endpoints/ep-218.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}",
    "summary": "Subscribe a user to an issue"
  },
  {
    "path": "endpoints/ep-219.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}",
    "summary": "Unsubscribe a user from an issue"
  },
  {
    "path": "endpoints/ep-220.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check",
    "summary": "Check if the authenticated user is subscribed to an issue"
  },
  {
    "path": "endpoints/ep-221.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions",
    "summary": "Get users who subscribed to an issue"
  },
  {
    "path": "endpoints/ep-222.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls",
    "summary": "List a repo's pull requests with filtering and pagination"
  },
  {
    "path": "endpoints/ep-223.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}",
    "summary": "Get a single pull request by index"
  },
  {
    "path": "endpoints/ep-224.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{base}/{head}",
    "summary": "Get a pull request by base and head branch references"
  },
  {
    "path": "endpoints/ep-225.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}",
    "summary": "Get a pull request diff or patch file"
  },
  {
    "path": "endpoints/ep-226.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls",
    "summary": "Create a new pull request"
  },
  {
    "path": "endpoints/ep-227.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/pulls/{index}",
    "summary": "Update a pull request (title, body, assignees, labels, milestone, state, base branch, deadline, allow_maintainer_edit)"
  },
  {
    "path": "endpoints/ep-228.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/merge",
    "summary": "Check if a pull request has been merged"
  },
  {
    "path": "endpoints/ep-229.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge",
    "summary": "Merge a pull request or schedule auto-merge"
  },
  {
    "path": "endpoints/ep-230.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update",
    "summary": "Merge PR's base branch into head branch (update PR)"
  },
  {
    "path": "endpoints/ep-231.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge",
    "summary": "Cancel a scheduled auto-merge for a pull request"
  },
  {
    "path": "endpoints/ep-232.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits",
    "summary": "Get commits for a pull request"
  },
  {
    "path": "endpoints/ep-233.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/files",
    "summary": "Get changed files for a pull request"
  },
  {
    "path": "endpoints/ep-234.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/mirror-sync",
    "summary": "Adds a mirrored (pull) repository to the sync queue"
  },
  {
    "path": "endpoints/ep-235.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/push_mirrors-sync",
    "summary": "Syncs all push mirrors of a repository by triggering each one"
  },
  {
    "path": "endpoints/ep-236.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/push_mirrors",
    "summary": "Lists all push mirrors of a repository with pagination"
  },
  {
    "path": "endpoints/ep-237.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/push_mirrors/{name}",
    "summary": "Gets a specific push mirror by its remote name"
  },
  {
    "path": "endpoints/ep-238.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/push_mirrors",
    "summary": "Creates a new push mirror for a repository"
  },
  {
    "path": "endpoints/ep-239.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/push_mirrors/{name}",
    "summary": "Deletes a push mirror from a repository by its remote name"
  },
  {
    "path": "endpoints/ep-240.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases/{id}",
    "summary": "Get a single release by ID for a repository"
  },
  {
    "path": "endpoints/ep-241.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases/latest",
    "summary": "Get the most recent non-prerelease, non-draft release sorted by created_at"
  },
  {
    "path": "endpoints/ep-242.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases",
    "summary": "List a repository's releases with pagination and optional draft/pre-release filters"
  },
  {
    "path": "endpoints/ep-243.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/releases",
    "summary": "Create a new release or convert an existing tag to a release"
  },
  {
    "path": "endpoints/ep-244.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/releases/{id}",
    "summary": "Update a release's metadata (tag name, target, title, note, draft/prerelease status)"
  },
  {
    "path": "endpoints/ep-245.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/releases/{id}",
    "summary": "Delete a release (keeps the git tag, deletes attachments from storage)"
  },
  {
    "path": "endpoints/ep-246.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/trees/{sha}",
    "summary": "Gets the tree of a repository by SHA hash with pagination support"
  },
  {
    "path": "endpoints/ep-247.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/refs",
    "summary": "List all git references (branches, tags) of a repository"
  },
  {
    "path": "endpoints/ep-248.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}",
    "summary": "Get specified ref or filtered list of refs by prefix"
  },
  {
    "path": "endpoints/ep-249.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/diffpatch",
    "summary": "Apply a diff patch to the repository, creating a new commit"
  },
  {
    "path": "endpoints/ep-250.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/collaborators",
    "summary": "List all collaborators of a repository with pagination"
  },
  {
    "path": "endpoints/ep-251.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}",
    "summary": "Check if a user is a collaborator of a repository"
  },
  {
    "path": "endpoints/ep-252.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}",
    "summary": "Add or update a collaborator to a repository with specified permission level"
  },
  {
    "path": "endpoints/ep-253.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}",
    "summary": "Remove a collaborator from a repository"
  },
  {
    "path": "endpoints/ep-254.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission",
    "summary": "Get repository permissions for a user"
  },
  {
    "path": "endpoints/ep-255.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/reviewers",
    "summary": "Return all users that can be requested to review in this repo"
  },
  {
    "path": "endpoints/ep-256.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/assignees",
    "summary": "Return all users that have write access and can be assigned to issues"
  },
  {
    "path": "endpoints/ep-257.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    "summary": "Get a single issue attachment"
  },
  {
    "path": "endpoints/ep-258.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/assets",
    "summary": "List all attachments of an issue"
  },
  {
    "path": "endpoints/ep-259.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets",
    "summary": "Create an issue attachment by uploading a file"
  },
  {
    "path": "endpoints/ep-260.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    "summary": "Edit an issue attachment (rename)"
  },
  {
    "path": "endpoints/ep-261.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}",
    "summary": "Delete an issue attachment"
  },
  {
    "path": "endpoints/ep-262.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/avatar",
    "summary": "Update repository avatar image"
  },
  {
    "path": "endpoints/ep-263.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/avatar",
    "summary": "Delete repository custom avatar"
  },
  {
    "path": "endpoints/ep-264.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/secrets",
    "summary": "List repository actions secrets (names only, not values)"
  },
  {
    "path": "endpoints/ep-265.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}",
    "summary": "Create or update a secret value in a repository"
  },
  {
    "path": "endpoints/ep-266.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}",
    "summary": "Delete a secret in a repository"
  },
  {
    "path": "endpoints/ep-267.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}",
    "summary": "Get a repo-level variable by name"
  },
  {
    "path": "endpoints/ep-268.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}",
    "summary": "Delete a repo-level variable by name"
  },
  {
    "path": "endpoints/ep-269.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}",
    "summary": "Create a repo-level variable"
  },
  {
    "path": "endpoints/ep-270.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}",
    "summary": "Update a repo-level variable"
  },
  {
    "path": "endpoints/ep-271.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/variables",
    "summary": "Get repo-level variables list"
  },
  {
    "path": "endpoints/ep-272.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/runners/registration-token",
    "summary": "Get a repository's actions runner registration token"
  },
  {
    "path": "endpoints/ep-273.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runners",
    "summary": "Get repo-level runners"
  },
  {
    "path": "endpoints/ep-274.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}",
    "summary": "Get a repo-level runner"
  },
  {
    "path": "endpoints/ep-275.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}",
    "summary": "Delete a repo-level runner"
  },
  {
    "path": "endpoints/ep-276.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}",
    "summary": "Update a repo-level runner (enable/disable)"
  },
  {
    "path": "endpoints/ep-277.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/jobs",
    "summary": "Lists all jobs for a repository"
  },
  {
    "path": "endpoints/ep-278.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs",
    "summary": "Lists all runs for a repository"
  },
  {
    "path": "endpoints/ep-279.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/tasks",
    "summary": "List a repository's action tasks"
  },
  {
    "path": "endpoints/ep-280.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/workflows",
    "summary": "List repository workflows from default branch"
  },
  {
    "path": "endpoints/ep-281.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
    "summary": "Get a specific workflow by ID (filename)"
  },
  {
    "path": "endpoints/ep-282.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable",
    "summary": "Disable a workflow"
  },
  {
    "path": "endpoints/ep-283.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches",
    "summary": "Create a workflow dispatch event to trigger a workflow run"
  },
  {
    "path": "endpoints/ep-284.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable",
    "summary": "Enable a workflow"
  },
  {
    "path": "endpoints/ep-285.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}",
    "summary": "Gets a specific workflow run by ID"
  },
  {
    "path": "endpoints/ep-286.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}",
    "summary": "Gets a specific workflow run attempt by run ID and attempt number"
  },
  {
    "path": "endpoints/ep-287.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun",
    "summary": "Reruns an entire workflow run creating a new attempt"
  },
  {
    "path": "endpoints/ep-288.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs",
    "summary": "Reruns all failed or cancelled jobs in a workflow run"
  },
  {
    "path": "endpoints/ep-289.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun",
    "summary": "Reruns a specific workflow job in a run"
  },
  {
    "path": "endpoints/ep-290.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs",
    "summary": "Lists all jobs for a workflow run (latest attempt)"
  },
  {
    "path": "endpoints/ep-291.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs",
    "summary": "Lists all jobs for a specific workflow run attempt"
  },
  {
    "path": "endpoints/ep-292.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}",
    "summary": "Gets a specific workflow job for a workflow run"
  },
  {
    "path": "endpoints/ep-293.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts",
    "summary": "Lists all artifacts for a specific workflow run in a repository"
  },
  {
    "path": "endpoints/ep-294.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/actions/runs/{run}",
    "summary": "Deletes a workflow run including all logs and artifacts"
  },
  {
    "path": "endpoints/ep-295.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/artifacts",
    "summary": "Lists all artifacts for a repository"
  },
  {
    "path": "endpoints/ep-296.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
    "summary": "Gets a specific artifact by ID for a workflow run (v4 only)"
  },
  {
    "path": "endpoints/ep-297.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
    "summary": "Marks a specific artifact for deletion (v4 only)"
  },
  {
    "path": "endpoints/ep-298.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip",
    "summary": "Downloads a specific artifact, redirecting to blob URL or serving directly"
  },
  {
    "path": "endpoints/ep-299.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/notes/{sha}",
    "summary": "Get a note corresponding to a single commit from a repository"
  },
  {
    "path": "endpoints/ep-300.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    "summary": "Get a list of reactions from a comment of an issue"
  },
  {
    "path": "endpoints/ep-301.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    "summary": "Add a reaction to a comment of an issue"
  },
  {
    "path": "endpoints/ep-302.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions",
    "summary": "Remove a reaction from a comment of an issue"
  },
  {
    "path": "endpoints/ep-303.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions",
    "summary": "Get a list of reactions of an issue"
  },
  {
    "path": "endpoints/ep-304.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions",
    "summary": "Add a reaction to an issue"
  },
  {
    "path": "endpoints/ep-305.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/reactions",
    "summary": "Remove a reaction from an issue"
  },
  {
    "path": "endpoints/ep-306.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/branches/{branch}",
    "summary": "Retrieve a specific branch from a repository, including its effective branch protection"
  },
  {
    "path": "endpoints/ep-307.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/branches/{branch}",
    "summary": "Delete a specific branch from a repository"
  },
  {
    "path": "endpoints/ep-308.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/branches",
    "summary": "Create a new branch in a repository"
  },
  {
    "path": "endpoints/ep-309.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/branches",
    "summary": "List a repository's branches with pagination"
  },
  {
    "path": "endpoints/ep-310.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/branches/{branch}",
    "summary": "Update a branch reference to a new commit"
  },
  {
    "path": "endpoints/ep-311.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/branches/{branch}",
    "summary": "Rename a branch in a repository"
  },
  {
    "path": "endpoints/ep-312.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/branch_protections/{name}",
    "summary": "Get a specific branch protection rule for the repository"
  },
  {
    "path": "endpoints/ep-313.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/branch_protections",
    "summary": "List all branch protection rules for a repository"
  },
  {
    "path": "endpoints/ep-314.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/branch_protections",
    "summary": "Create a branch protection rule for a repository"
  },
  {
    "path": "endpoints/ep-315.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name}",
    "summary": "Edit a branch protection rule for a repository. Only fields that are set will be changed"
  },
  {
    "path": "endpoints/ep-316.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/branch_protections/{name}",
    "summary": "Delete a specific branch protection rule for the repository"
  },
  {
    "path": "endpoints/ep-317.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/branch_protections/priority",
    "summary": "Update the priorities of branch protection rules for a repository"
  },
  {
    "path": "endpoints/ep-318.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/merge-upstream",
    "summary": "Merge a branch from the upstream (base) repository into the fork"
  },
  {
    "path": "endpoints/ep-319.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/issues/{index}/lock",
    "summary": "Lock an issue to restrict commenting to users with write access"
  },
  {
    "path": "endpoints/ep-320.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/lock",
    "summary": "Unlock a previously locked issue"
  },
  {
    "path": "endpoints/ep-321.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/hooks",
    "summary": "List all webhooks configured for a repository"
  },
  {
    "path": "endpoints/ep-322.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/hooks/{id}",
    "summary": "Get a specific webhook by ID for a repository"
  },
  {
    "path": "endpoints/ep-323.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/hooks/{id}/tests",
    "summary": "Test a push webhook by sending a test push payload"
  },
  {
    "path": "endpoints/ep-324.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/hooks",
    "summary": "Create a webhook for a repository"
  },
  {
    "path": "endpoints/ep-325.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/hooks/{id}",
    "summary": "Edit a webhook in a repository"
  },
  {
    "path": "endpoints/ep-326.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/hooks/{id}",
    "summary": "Delete a webhook from a repository"
  },
  {
    "path": "endpoints/ep-327.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/stargazers",
    "summary": "List users who starred the repository"
  },
  {
    "path": "endpoints/ep-328.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/subscribers",
    "summary": "List users watching (subscribed to) the repository"
  },
  {
    "path": "endpoints/ep-329.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/teams",
    "summary": "List teams that have access to the repository (org repos only)"
  },
  {
    "path": "endpoints/ep-330.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/teams/{team}",
    "summary": "Check if a team is assigned to a repository"
  },
  {
    "path": "endpoints/ep-331.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/teams/{team}",
    "summary": "Add a team to a repository"
  },
  {
    "path": "endpoints/ep-332.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/teams/{team}",
    "summary": "Delete a team from a repository"
  },
  {
    "path": "endpoints/ep-333.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/forks",
    "summary": "List a repository's forks"
  },
  {
    "path": "endpoints/ep-334.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/forks",
    "summary": "Fork a repository"
  },
  {
    "path": "endpoints/ep-335.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/labels",
    "summary": "Get an issue's labels"
  },
  {
    "path": "endpoints/ep-336.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels",
    "summary": "Add labels to an issue"
  },
  {
    "path": "endpoints/ep-337.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels/{id}",
    "summary": "Remove a label from an issue"
  },
  {
    "path": "endpoints/ep-338.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/issues/{index}/labels",
    "summary": "Replace all labels on an issue"
  },
  {
    "path": "endpoints/ep-339.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/labels",
    "summary": "Remove all labels from an issue"
  },
  {
    "path": "endpoints/ep-340.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/keys",
    "summary": "List a repository's deploy keys"
  },
  {
    "path": "endpoints/ep-341.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/keys/{id}",
    "summary": "Get a repository's deploy key by id"
  },
  {
    "path": "endpoints/ep-342.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/keys",
    "summary": "Add a deploy key to a repository"
  },
  {
    "path": "endpoints/ep-343.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/keys/{id}",
    "summary": "Delete a deploy key from a repository"
  },
  {
    "path": "endpoints/ep-344.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag}",
    "summary": "Get a single release of a repository by tag name"
  },
  {
    "path": "endpoints/ep-345.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/releases/tags/{tag}",
    "summary": "Delete a release from a repository by tag name"
  },
  {
    "path": "endpoints/ep-346.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/licenses",
    "summary": "Get the detected licenses for a repository"
  },
  {
    "path": "endpoints/ep-347.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/topics",
    "summary": "Get list of topics that a repository has"
  },
  {
    "path": "endpoints/ep-348.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/topics",
    "summary": "Replace list of topics for a repository"
  },
  {
    "path": "endpoints/ep-349.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/topics/{topic}",
    "summary": "Add a topic to a repository"
  },
  {
    "path": "endpoints/ep-350.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/topics/{topic}",
    "summary": "Delete a topic from a repository"
  },
  {
    "path": "endpoints/ep-351.md",
    "title": "GET /api/v1/topics/search",
    "summary": "Search topics via keyword"
  },
  {
    "path": "endpoints/ep-352.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    "summary": "Get a single attachment of a release by its ID"
  },
  {
    "path": "endpoints/ep-353.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/releases/{id}/assets",
    "summary": "List all attachments of a release"
  },
  {
    "path": "endpoints/ep-354.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/releases/{id}/assets",
    "summary": "Upload a file attachment to a release"
  },
  {
    "path": "endpoints/ep-355.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    "summary": "Update the name of a release attachment"
  },
  {
    "path": "endpoints/ep-356.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}",
    "summary": "Delete a release attachment and its file from storage"
  },
  {
    "path": "endpoints/ep-357.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/labels",
    "summary": "Get all labels of a repository with pagination"
  },
  {
    "path": "endpoints/ep-358.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/labels/{id}",
    "summary": "Get a single label by ID or name"
  },
  {
    "path": "endpoints/ep-359.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/labels",
    "summary": "Create a label for a repository"
  },
  {
    "path": "endpoints/ep-360.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/labels/{id}",
    "summary": "Update a label for a repository"
  },
  {
    "path": "endpoints/ep-361.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/labels/{id}",
    "summary": "Delete a label from a repository"
  },
  {
    "path": "endpoints/ep-362.md",
    "title": "GET /api/v1/repos/search",
    "summary": "Search for repositories"
  },
  {
    "path": "endpoints/ep-363.md",
    "title": "POST /api/v1/user/repos",
    "summary": "Create a repository for the authenticated user"
  },
  {
    "path": "endpoints/ep-364.md",
    "title": "POST /api/v1/repos/{template_owner}/{template_repo}/generate",
    "summary": "Create a repository using a template"
  },
  {
    "path": "endpoints/ep-365.md",
    "title": "POST /api/v1/org/{org}/repos",
    "summary": "Create a repository in an organization (deprecated)"
  },
  {
    "path": "endpoints/ep-366.md",
    "title": "POST /api/v1/orgs/{org}/repos",
    "summary": "Create a repository in an organization"
  },
  {
    "path": "endpoints/ep-367.md",
    "title": "GET /api/v1/repos/{owner}/{repo}",
    "summary": "Get a repository by owner and name"
  },
  {
    "path": "endpoints/ep-368.md",
    "title": "GET /api/v1/repositories/{id}",
    "summary": "Get a repository by its numeric ID"
  },
  {
    "path": "endpoints/ep-369.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}",
    "summary": "Edit a repository's properties. Only fields that are set will be changed."
  },
  {
    "path": "endpoints/ep-370.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}",
    "summary": "Delete a repository"
  },
  {
    "path": "endpoints/ep-371.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issue_templates",
    "summary": "Get available issue templates for a repository"
  },
  {
    "path": "endpoints/ep-372.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issue_config",
    "summary": "Returns the issue config for a repo"
  },
  {
    "path": "endpoints/ep-373.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issue_config/validate",
    "summary": "Returns validation information for the issue config"
  },
  {
    "path": "endpoints/ep-374.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/activities/feeds",
    "summary": "List a repository's activity feeds"
  },
  {
    "path": "endpoints/ep-375.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/languages",
    "summary": "Get languages and number of bytes of code written in the repository"
  },
  {
    "path": "endpoints/ep-376.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/pin",
    "summary": "Pin an issue to the repository"
  },
  {
    "path": "endpoints/ep-377.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/pin",
    "summary": "Unpin an issue from the repository"
  },
  {
    "path": "endpoints/ep-378.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/pin/{position}",
    "summary": "Move a pinned issue to a new position"
  },
  {
    "path": "endpoints/ep-379.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/pinned",
    "summary": "List a repository's pinned issues (non-pull requests)"
  },
  {
    "path": "endpoints/ep-380.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/pinned",
    "summary": "List a repository's pinned pull requests"
  },
  {
    "path": "endpoints/ep-381.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/new_pin_allowed",
    "summary": "Returns whether new issue/PR pins are allowed (based on max pin limit)"
  },
  {
    "path": "endpoints/ep-382.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-382`"
  },
  {
    "path": "endpoints/ep-383.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-383`"
  },
  {
    "path": "endpoints/ep-384.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-384`"
  },
  {
    "path": "endpoints/ep-385.md",
    "title": "GET /api/v1/user/stopwatches",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-385`"
  },
  {
    "path": "endpoints/ep-386.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/hooks/git",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-386`"
  },
  {
    "path": "endpoints/ep-387.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/hooks/git/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-387`"
  },
  {
    "path": "endpoints/ep-388.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/hooks/git/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-388`"
  },
  {
    "path": "endpoints/ep-389.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/hooks/git/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-389`"
  },
  {
    "path": "endpoints/ep-390.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/raw/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-390`"
  },
  {
    "path": "endpoints/ep-391.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/media/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-391`"
  },
  {
    "path": "endpoints/ep-392.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/archive/{archive}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-392`"
  },
  {
    "path": "endpoints/ep-393.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/editorconfig/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-393`"
  },
  {
    "path": "endpoints/ep-394.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/contents",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-394`"
  },
  {
    "path": "endpoints/ep-395.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/contents/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-395`"
  },
  {
    "path": "endpoints/ep-396.md",
    "title": "PUT /api/v1/repos/{owner}/{repo}/contents/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-396`"
  },
  {
    "path": "endpoints/ep-397.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/contents/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-397`"
  },
  {
    "path": "endpoints/ep-398.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/contents-ext/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-398`"
  },
  {
    "path": "endpoints/ep-399.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/contents/{filepath}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-399`"
  },
  {
    "path": "endpoints/ep-400.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/contents",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-400`"
  },
  {
    "path": "endpoints/ep-401.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/file-contents",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-401`"
  },
  {
    "path": "endpoints/ep-402.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/file-contents",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-402`"
  },
  {
    "path": "endpoints/ep-403.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-403`"
  },
  {
    "path": "endpoints/ep-404.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/transfer",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-404`"
  },
  {
    "path": "endpoints/ep-405.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/transfer/accept",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-405`"
  },
  {
    "path": "endpoints/ep-406.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/transfer/reject",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-406`"
  },
  {
    "path": "endpoints/ep-407.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/times",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-407`"
  },
  {
    "path": "endpoints/ep-408.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/times",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-408`"
  },
  {
    "path": "endpoints/ep-409.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-409`"
  },
  {
    "path": "endpoints/ep-410.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/times/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-410`"
  },
  {
    "path": "endpoints/ep-411.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/times/{user}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-411`"
  },
  {
    "path": "endpoints/ep-412.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/times",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-412`"
  },
  {
    "path": "endpoints/ep-413.md",
    "title": "GET /api/v1/user/times",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-413`"
  },
  {
    "path": "endpoints/ep-414.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/tags",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-414`"
  },
  {
    "path": "endpoints/ep-415.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/tags/{sha}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-415`"
  },
  {
    "path": "endpoints/ep-416.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/tags/{tag}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-416`"
  },
  {
    "path": "endpoints/ep-417.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/tags",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-417`"
  },
  {
    "path": "endpoints/ep-418.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/tags/{tag}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-418`"
  },
  {
    "path": "endpoints/ep-419.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/tag_protections",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-419`"
  },
  {
    "path": "endpoints/ep-420.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/tag_protections/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-420`"
  },
  {
    "path": "endpoints/ep-421.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/tag_protections",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-421`"
  },
  {
    "path": "endpoints/ep-422.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/tag_protections/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-422`"
  },
  {
    "path": "endpoints/ep-423.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/tag_protections/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-423`"
  },
  {
    "path": "endpoints/ep-424.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-424`"
  },
  {
    "path": "endpoints/ep-425.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-425`"
  },
  {
    "path": "endpoints/ep-426.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-426`"
  },
  {
    "path": "endpoints/ep-427.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-427`"
  },
  {
    "path": "endpoints/ep-428.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-428`"
  },
  {
    "path": "endpoints/ep-429.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/statuses/{sha}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-429`"
  },
  {
    "path": "endpoints/ep-430.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/statuses/{sha}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-430`"
  },
  {
    "path": "endpoints/ep-431.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/commits/{ref}/statuses",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-431`"
  },
  {
    "path": "endpoints/ep-432.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/commits/{ref}/status",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-432`"
  },
  {
    "path": "endpoints/ep-433.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/git/blobs/{sha}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-433`"
  },
  {
    "path": "endpoints/ep-434.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/compare/{basehead}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-434`"
  },
  {
    "path": "endpoints/ep-435.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/comments",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-435`"
  },
  {
    "path": "endpoints/ep-436.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}/timeline",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-436`"
  },
  {
    "path": "endpoints/ep-437.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/comments",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-437`"
  },
  {
    "path": "endpoints/ep-438.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/comments",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-438`"
  },
  {
    "path": "endpoints/ep-439.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-439`"
  },
  {
    "path": "endpoints/ep-440.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/comments/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-440`"
  },
  {
    "path": "endpoints/ep-441.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-441`"
  },
  {
    "path": "endpoints/ep-442.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/comments/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-442`"
  },
  {
    "path": "endpoints/ep-443.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/comments/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-443`"
  },
  {
    "path": "endpoints/ep-444.md",
    "title": "POST /api/v1/repos/migrate",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-444`"
  },
  {
    "path": "endpoints/ep-445.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/wiki/new",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-445`"
  },
  {
    "path": "endpoints/ep-446.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-446`"
  },
  {
    "path": "endpoints/ep-447.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-447`"
  },
  {
    "path": "endpoints/ep-448.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/wiki/pages",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-448`"
  },
  {
    "path": "endpoints/ep-449.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/wiki/page/{pageName}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-449`"
  },
  {
    "path": "endpoints/ep-450.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/wiki/revisions/{pageName}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-450`"
  },
  {
    "path": "endpoints/ep-451.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-451`"
  },
  {
    "path": "endpoints/ep-452.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-452`"
  },
  {
    "path": "endpoints/ep-453.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-453`"
  },
  {
    "path": "endpoints/ep-454.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-454`"
  },
  {
    "path": "endpoints/ep-455.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/resolve",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-455`"
  },
  {
    "path": "endpoints/ep-456.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/comments/{id}/unresolve",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-456`"
  },
  {
    "path": "endpoints/ep-457.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-457`"
  },
  {
    "path": "endpoints/ep-458.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-458`"
  },
  {
    "path": "endpoints/ep-459.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-459`"
  },
  {
    "path": "endpoints/ep-460.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-460`"
  },
  {
    "path": "endpoints/ep-461.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-461`"
  },
  {
    "path": "endpoints/ep-462.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-462`"
  },
  {
    "path": "endpoints/ep-463.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-463`"
  },
  {
    "path": "endpoints/ep-464.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/milestones",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-464`"
  },
  {
    "path": "endpoints/ep-465.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/milestones/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-465`"
  },
  {
    "path": "endpoints/ep-466.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/milestones",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-466`"
  },
  {
    "path": "endpoints/ep-467.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/milestones/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-467`"
  },
  {
    "path": "endpoints/ep-468.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/milestones/{id}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-468`"
  },
  {
    "path": "endpoints/ep-469.md",
    "title": "GET /api/v1/repos/issues/search",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-469`"
  },
  {
    "path": "endpoints/ep-470.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-470`"
  },
  {
    "path": "endpoints/ep-471.md",
    "title": "GET /api/v1/repos/{owner}/{repo}/issues/{index}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-471`"
  },
  {
    "path": "endpoints/ep-472.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-472`"
  },
  {
    "path": "endpoints/ep-473.md",
    "title": "PATCH /api/v1/repos/{owner}/{repo}/issues/{index}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-473`"
  },
  {
    "path": "endpoints/ep-474.md",
    "title": "DELETE /api/v1/repos/{owner}/{repo}/issues/{index}",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-474`"
  },
  {
    "path": "endpoints/ep-475.md",
    "title": "POST /api/v1/repos/{owner}/{repo}/issues/{index}/deadline",
    "summary": "**Module:** [routers](../modules/routers.md) \u00b7 **Auth:** none \u00b7 **ID:** `ep-475`"
  },
  {
    "path": "errors/global-handlers.md",
    "title": "Global Error Handlers",
    "summary": "**3 handlers**"
  },
  {
    "path": "external/Avatar_Storage_Backend.md",
    "title": "Avatar Storage Backend",
    "summary": "**Client:** `ObjectStorage` \u00b7 **Type:** cloud_service"
  },
  {
    "path": "external/GPG_binary__gpg_--export_.md",
    "title": "GPG binary (gpg --export)",
    "summary": "**Client:** `process.GetManager().ExecDir` \u00b7 **Type:** process_exec"
  },
  {
    "path": "external/Git_Remote__Push_Mirror_Target_.md",
    "title": "Git Remote (Push Mirror Target)",
    "summary": "**Client:** `gitrepo` \u00b7 **Type:** http_api"
  },
  {
    "path": "external/Git_Repository__local_filesystem_.md",
    "title": "Git Repository (local filesystem)",
    "summary": "**Client:** `git.Repository` \u00b7 **Type:** filesystem"
  },
  {
    "path": "external/HaveIBeenPwned_API.md",
    "title": "HaveIBeenPwned API",
    "summary": "**Client:** `password.IsPwned` \u00b7 **Type:** http_api"
  },
  {
    "path": "external/Object_Storage__Minio_Azure_Local_.md",
    "title": "Object Storage (Minio/Azure/Local)",
    "summary": "**Client:** `storage.ObjectStorage` \u00b7 **Type:** cloud_service"
  },
  {
    "path": "external/overview.md",
    "title": "External Services",
    "summary": "**7 integrations**"
  },
  {
    "path": "modules/routers.md",
    "title": "routers",
    "summary": "**475 endpoints** \u00b7 Go \u00b7 go-chi/chi v5 + XORM"
  },
  {
    "path": "performance/overview.md",
    "title": "Performance Analysis",
    "summary": "**381 endpoints analyzed** \u00b7 **198 issues found**"
  },
  {
    "path": "resiliency/overview.md",
    "title": "Resiliency Assessment",
    "summary": "**Overall Risk:** critical \u00b7 **351 findings**"
  }
]
```

## Developer Query

If I need to add a new webhook event type, what files across routers, services, and models need to change? Trace the full webhook delivery pipeline.
