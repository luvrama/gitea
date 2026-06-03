# Q5 Expected Answer: User Table Schema Impact

Source: endpoints with user in path or workflow + databases.md user tables

## User-related database tables (16)

## blocked_user {#blocked_user}
## org_user {#org_user}
## team JOIN team_user {#team_join_team_user}
## team/team_user {#team_team_user}
## team_user {#team_user}
## team_user+team {#team_user_team}
## team_user/org_user {#team_user_org_user}
## user {#user}
## user (org_user join) {#user__org_user_join_}
## user JOIN follow {#user_join_follow}
## user JOIN star {#user_join_star}
## user JOIN watch {#user_join_watch}
## user+follow {#user_follow}
## user_badge {#user_badge}
## user_blocking {#user_blocking}
## user_redirect {#user_redirect}

## Endpoints referencing user entity (206)

- ep-019.md: GET /api/v1/notifications
- ep-020.md: PUT /api/v1/notifications
- ep-021.md: GET /api/v1/notifications/new
- ep-022.md: GET /api/v1/repos/{owner}/{repo}/notifications
- ep-023.md: PUT /api/v1/repos/{owner}/{repo}/notifications
- ep-024.md: GET /api/v1/notifications/threads/{id}
- ep-025.md: PATCH /api/v1/notifications/threads/{id}
- ep-026.md: GET /api/v1/user/orgs
- ep-027.md: GET /api/v1/users/{username}/orgs
- ep-028.md: GET /api/v1/users/{username}/orgs/{org}/permissions
- ep-029.md: GET /api/v1/orgs
- ep-030.md: POST /api/v1/orgs
- ep-031.md: GET /api/v1/orgs/{org}
- ep-032.md: POST /api/v1/orgs/{org}/rename
- ep-033.md: PATCH /api/v1/orgs/{org}
- ep-034.md: DELETE /api/v1/orgs/{org}
- ep-035.md: GET /api/v1/orgs/{org}/activities/feeds
- ep-036.md: DELETE /api/v1/orgs/{org}/repos
- ep-037.md: POST /api/v1/orgs/{org}/avatar
- ep-038.md: DELETE /api/v1/orgs/{org}/avatar
- ep-039.md: GET /api/v1/orgs/{org}/actions/secrets
- ep-040.md: PUT /api/v1/orgs/{org}/actions/secrets/{secretname}
- ep-041.md: DELETE /api/v1/orgs/{org}/actions/secrets/{secretname}
- ep-042.md: POST /api/v1/orgs/{org}/actions/runners/registration-token
- ep-053.md: GET /api/v1/orgs/{org}/actions/runs
- ep-055.md: GET /api/v1/user/teams
- ep-056.md: GET /api/v1/teams/{id}
- ep-057.md: POST /api/v1/orgs/{org}/teams
- ep-059.md: DELETE /api/v1/teams/{id}
- ep-060.md: GET /api/v1/teams/{id}/members
- ep-061.md: GET /api/v1/teams/{id}/members/{username}
- ep-062.md: PUT /api/v1/teams/{id}/members/{username}
- ep-063.md: DELETE /api/v1/teams/{id}/members/{username}
- ep-064.md: GET /api/v1/teams/{id}/repos
- ep-065.md: GET /api/v1/teams/{id}/repos/{org}/{repo}
- ep-066.md: PUT /api/v1/teams/{id}/repos/{org}/{repo}
- ep-067.md: DELETE /api/v1/teams/{id}/repos/{org}/{repo}
- ep-068.md: GET /api/v1/orgs/{org}/teams/search
- ep-069.md: GET /api/v1/teams/{id}/activities/feeds
- ep-070.md: GET /api/v1/orgs/{org}/members
- ep-071.md: GET /api/v1/orgs/{org}/public_members
- ep-072.md: GET /api/v1/orgs/{org}/members/{username}
- ep-073.md: GET /api/v1/orgs/{org}/public_members/{username}
- ep-074.md: PUT /api/v1/orgs/{org}/public_members/{username}
- ep-075.md: DELETE /api/v1/orgs/{org}/public_members/{username}
- ep-076.md: DELETE /api/v1/orgs/{org}/members/{username}
- ep-077.md: GET /api/v1/orgs/{org}/hooks
- ep-087.md: GET /api/v1/orgs/{org}/blocks
- ep-088.md: GET /api/v1/orgs/{org}/blocks/{username}
- ep-089.md: PUT /api/v1/orgs/{org}/blocks/{username}
- ep-090.md: DELETE /api/v1/orgs/{org}/blocks/{username}
- ep-096.md: POST /api/v1/admin/users/{username}/orgs
- ep-097.md: GET /api/v1/admin/orgs
- ep-098.md: POST /api/v1/admin/users
- ep-099.md: PATCH /api/v1/admin/users/{username}
- ep-100.md: DELETE /api/v1/admin/users/{username}
- ep-101.md: POST /api/v1/admin/users/{username}/keys
- ep-102.md: DELETE /api/v1/admin/users/{username}/keys/{id}
- ep-103.md: GET /api/v1/admin/users
- ep-104.md: POST /api/v1/admin/users/{username}/rename
- ep-106.md: GET /api/v1/admin/actions/runs
- ep-107.md: GET /api/v1/admin/unadopted
- ep-108.md: POST /api/v1/admin/unadopted/{owner}/{repo}
- ep-109.md: DELETE /api/v1/admin/unadopted/{owner}/{repo}
- ep-112.md: POST /api/v1/admin/users/{username}/repos
- ep-118.md: GET /api/v1/admin/emails
- ep-119.md: GET /api/v1/admin/emails/search
- ep-120.md: GET /api/v1/admin/users/{username}/badges
- ep-121.md: POST /api/v1/admin/users/{username}/badges
- ep-122.md: DELETE /api/v1/admin/users/{username}/badges
- ep-123.md: GET /api/v1/users/search
- ep-124.md: GET /api/v1/users/{username}
- ep-125.md: GET /api/v1/user
- ep-126.md: GET /api/v1/users/{username}/heatmap
- ep-127.md: GET /api/v1/users/{username}/activities/feeds
- ep-128.md: POST /api/v1/user/avatar
- ep-129.md: DELETE /api/v1/user/avatar
- ep-130.md: PUT /api/v1/user/actions/secrets/{secretname}
- ep-131.md: DELETE /api/v1/user/actions/secrets/{secretname}
- ep-132.md: POST /api/v1/user/actions/variables/{variablename}
- ep-133.md: PUT /api/v1/user/actions/variables/{variablename}
- ep-134.md: DELETE /api/v1/user/actions/variables/{variablename}
- ep-135.md: GET /api/v1/user/actions/variables/{variablename}
- ep-136.md: GET /api/v1/user/actions/variables
- ep-137.md: GET /api/v1/user/actions/runs
- ep-138.md: GET /api/v1/user/actions/jobs
- ep-139.md: GET /api/v1/user/followers
- ep-140.md: GET /api/v1/users/{username}/followers
- ep-141.md: GET /api/v1/user/following
- ep-142.md: GET /api/v1/users/{username}/following
- ep-143.md: GET /api/v1/user/following/{username}
- ep-144.md: GET /api/v1/users/{username}/following/{target}
- ep-145.md: PUT /api/v1/user/following/{username}
- ep-146.md: DELETE /api/v1/user/following/{username}
- ep-147.md: GET /api/v1/user/hooks
- ep-148.md: GET /api/v1/user/hooks/{id}
- ep-149.md: POST /api/v1/user/hooks
- ep-150.md: PATCH /api/v1/user/hooks/{id}
- ep-151.md: DELETE /api/v1/user/hooks/{id}
- ep-152.md: GET /api/v1/users/{username}/starred
- ep-153.md: GET /api/v1/user/starred
- ep-154.md: GET /api/v1/user/starred/{owner}/{repo}
- ep-155.md: PUT /api/v1/user/starred/{owner}/{repo}
- ep-156.md: DELETE /api/v1/user/starred/{owner}/{repo}
- ep-157.md: GET /api/v1/user/keys
- ep-158.md: GET /api/v1/users/{username}/keys
- ep-159.md: GET /api/v1/user/keys/{id}
- ep-160.md: POST /api/v1/user/keys
- ep-161.md: DELETE /api/v1/user/keys/{id}
- ep-162.md: GET /api/v1/user/settings
- ep-163.md: PATCH /api/v1/user/settings
- ep-164.md: GET /api/v1/users/{username}/tokens
- ep-165.md: POST /api/v1/users/{username}/tokens
- ep-166.md: DELETE /api/v1/users/{username}/tokens/{token}
- ep-167.md: POST /api/v1/user/applications/oauth2
- ep-168.md: GET /api/v1/user/applications/oauth2
- ep-169.md: DELETE /api/v1/user/applications/oauth2/{id}
- ep-170.md: GET /api/v1/user/applications/oauth2/{id}
- ep-171.md: PATCH /api/v1/user/applications/oauth2/{id}
- ep-172.md: GET /api/v1/users/{username}/repos
- ep-173.md: GET /api/v1/user/repos
- ep-174.md: GET /api/v1/orgs/{org}/repos
- ep-175.md: POST /api/v1/user/actions/runners/registration-token
- ep-176.md: GET /api/v1/user/actions/runners
- ep-177.md: GET /api/v1/user/actions/runners/{runner_id}
- ep-178.md: DELETE /api/v1/user/actions/runners/{runner_id}
- ep-179.md: PATCH /api/v1/user/actions/runners/{runner_id}
- ep-180.md: GET /api/v1/user/emails
- ep-181.md: POST /api/v1/user/emails
- ep-182.md: DELETE /api/v1/user/emails
- ep-183.md: GET /api/v1/users/{username}/gpg_keys
- ep-184.md: GET /api/v1/user/gpg_keys
- ep-185.md: GET /api/v1/user/gpg_keys/{id}
- ep-186.md: GET /api/v1/user/gpg_key_token
- ep-187.md: POST /api/v1/user/gpg_key_verify
- ep-188.md: POST /api/v1/user/gpg_keys
- ep-189.md: DELETE /api/v1/user/gpg_keys/{id}
- ep-190.md: GET /api/v1/user/blocks
- ep-191.md: GET /api/v1/user/blocks/{username}
- ep-192.md: PUT /api/v1/user/blocks/{username}
- ep-193.md: DELETE /api/v1/user/blocks/{username}
- ep-194.md: GET /api/v1/users/{username}/subscriptions
- ep-195.md: GET /api/v1/user/subscriptions
- ep-196.md: GET /api/v1/repos/{owner}/{repo}/subscription
- ep-197.md: PUT /api/v1/repos/{owner}/{repo}/subscription
- ep-198.md: DELETE /api/v1/repos/{owner}/{repo}/subscription
- ep-199.md: GET /api/v1/packages/{owner}
- ep-200.md: GET /api/v1/packages/{owner}/{type}/{name}/{version}
- ep-202.md: DELETE /api/v1/packages/{owner}/{type}/{name}/{version}
- ep-203.md: GET /api/v1/packages/{owner}/{type}/{name}/{version}/files
- ep-204.md: GET /api/v1/packages/{owner}/{type}/{name}
- ep-205.md: GET /api/v1/packages/{owner}/{type}/{name}/-/latest
- ep-206.md: POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}
- ep-207.md: POST /api/v1/packages/{owner}/{type}/{name}/-/unlink
- ep-214.md: GET /api/v1/repos/{owner}/{repo}/git/commits/{sha}
- ep-215.md: GET /api/v1/repos/{owner}/{repo}/commits
- ep-218.md: PUT /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}
- ep-219.md: DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}
- ep-220.md: GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions/check
- ep-221.md: GET /api/v1/repos/{owner}/{repo}/issues/{index}/subscriptions
- ep-222.md: GET /api/v1/repos/{owner}/{repo}/pulls
- ep-226.md: POST /api/v1/repos/{owner}/{repo}/pulls
- ep-230.md: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/update
- ep-231.md: DELETE /api/v1/repos/{owner}/{repo}/pulls/{index}/merge
- ep-232.md: GET /api/v1/repos/{owner}/{repo}/pulls/{index}/commits
- ep-240.md: GET /api/v1/repos/{owner}/{repo}/releases/{id}
- ep-241.md: GET /api/v1/repos/{owner}/{repo}/releases/latest
- ep-242.md: GET /api/v1/repos/{owner}/{repo}/releases
- ep-244.md: PATCH /api/v1/repos/{owner}/{repo}/releases/{id}
- ep-245.md: DELETE /api/v1/repos/{owner}/{repo}/releases/{id}
- ep-250.md: GET /api/v1/repos/{owner}/{repo}/collaborators
- ep-251.md: GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}
- ep-252.md: PUT /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}
- ep-253.md: DELETE /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}
- ep-254.md: GET /api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission
- ep-255.md: GET /api/v1/repos/{owner}/{repo}/reviewers
- ep-256.md: GET /api/v1/repos/{owner}/{repo}/assignees
- ep-259.md: POST /api/v1/repos/{owner}/{repo}/issues/{index}/assets
- ep-278.md: GET /api/v1/repos/{owner}/{repo}/actions/runs
- ep-283.md: POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches
- ep-285.md: GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}
- ep-286.md: GET /api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}
- ep-299.md: GET /api/v1/repos/{owner}/{repo}/git/notes/{sha}
- ep-300.md: GET /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions
- ep-301.md: POST /api/v1/repos/{owner}/{repo}/issues/comments/{id}/reactions
- ep-303.md: GET /api/v1/repos/{owner}/{repo}/issues/{index}/reactions
- ep-304.md: POST /api/v1/repos/{owner}/{repo}/issues/{index}/reactions
- ep-306.md: GET /api/v1/repos/{owner}/{repo}/branches/{branch}
- ep-312.md: GET /api/v1/repos/{owner}/{repo}/branch_protections/{name}
- ep-314.md: POST /api/v1/repos/{owner}/{repo}/branch_protections
- ep-315.md: PATCH /api/v1/repos/{owner}/{repo}/branch_protections/{name}
- ep-327.md: GET /api/v1/repos/{owner}/{repo}/stargazers
- ep-328.md: GET /api/v1/repos/{owner}/{repo}/subscribers
- ep-333.md: GET /api/v1/repos/{owner}/{repo}/forks
- ep-334.md: POST /api/v1/repos/{owner}/{repo}/forks
- ep-344.md: GET /api/v1/repos/{owner}/{repo}/releases/tags/{tag}
- ep-362.md: GET /api/v1/repos/search
- ep-363.md: POST /api/v1/user/repos
- ep-364.md: POST /api/v1/repos/{template_owner}/{template_repo}/generate
- ep-365.md: POST /api/v1/org/{org}/repos
- ep-366.md: POST /api/v1/orgs/{org}/repos
- ep-368.md: GET /api/v1/repositories/{id}
- ep-370.md: DELETE /api/v1/repos/{owner}/{repo}
- ep-374.md: GET /api/v1/repos/{owner}/{repo}/activities/feeds
- ep-385.md: GET /api/v1/user/stopwatches
- ep-413.md: GET /api/v1/user/times