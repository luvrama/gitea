# Q1 Expected Answer: Repository Management Endpoints

Source: modules/routers.md → repository section

### repository
repository

| Method | Path | Description |
|--------|------|-------------|
| POST | [/api/v1/repos/migrate](../endpoints/ep-444.md) |  |
| GET | [/api/v1/repos/search](../endpoints/ep-362.md) | Search for repositories |
| GET | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-367.md) | Get a repository by owner and name |
| PATCH | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-369.md) | Edit a repository's properties. Only fields that are set will be changed. |
| DELETE | [/api/v1/repos/{owner}/{repo}](../endpoints/ep-370.md) | Delete a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts](../endpoints/ep-295.md) | Lists all artifacts for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}](../endpoints/ep-296.md) | Gets a specific artifact by ID for a workflow run (v4 only) |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}](../endpoints/ep-297.md) | Marks a specific artifact for deletion (v4 only) |
| GET | [/api/v1/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/zip](../endpoints/ep-298.md) | Downloads a specific artifact, redirecting to blob URL or serving directly |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs](../endpoints/ep-277.md) | Lists all jobs for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}](../endpoints/ep-292.md) | Gets a specific workflow job for a workflow run |
| GET | [/api/v1/repos/{owner}/{repo}/actions/jobs/{job_id}/logs](../endpoints/ep-403.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runners](../endpoints/ep-273.md) | Get repo-level runners |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runners/registration-token](../endpoints/ep-272.md) | Get a repository's actions runner registration token |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-274.md) | Get a repo-level runner |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-275.md) | Delete a repo-level runner |
| PATCH | [/api/v1/repos/{owner}/{repo}/actions/runners/{runner_id}](../endpoints/ep-276.md) | Update a repo-level runner (enable/disable) |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs](../endpoints/ep-278.md) | Lists all runs for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}](../endpoints/ep-285.md) | Gets a specific workflow run by ID |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}](../endpoints/ep-294.md) | Deletes a workflow run including all logs and artifacts |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/artifacts](../endpoints/ep-293.md) | Lists all artifacts for a specific workflow run in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}](../endpoints/ep-286.md) | Gets a specific workflow run attempt by run ID and attempt number |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/attempts/{attempt}/jobs](../endpoints/ep-291.md) | Lists all jobs for a specific workflow run attempt |
| GET | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs](../endpoints/ep-290.md) | Lists all jobs for a workflow run (latest attempt) |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/jobs/{job_id}/rerun](../endpoints/ep-289.md) | Reruns a specific workflow job in a run |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun](../endpoints/ep-287.md) | Reruns an entire workflow run creating a new attempt |
| POST | [/api/v1/repos/{owner}/{repo}/actions/runs/{run}/rerun-failed-jobs](../endpoints/ep-288.md) | Reruns all failed or cancelled jobs in a workflow run |
| GET | [/api/v1/repos/{owner}/{repo}/actions/secrets](../endpoints/ep-264.md) | List repository actions secrets (names only, not values) |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}](../endpoints/ep-265.md) | Create or update a secret value in a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/secrets/{secretname}](../endpoints/ep-266.md) | Delete a secret in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/actions/tasks](../endpoints/ep-279.md) | List a repository's action tasks |
| GET | [/api/v1/repos/{owner}/{repo}/actions/variables](../endpoints/ep-271.md) | Get repo-level variables list |
| GET | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-267.md) | Get a repo-level variable by name |
| DELETE | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-268.md) | Delete a repo-level variable by name |
| POST | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-269.md) | Create a repo-level variable |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/variables/{variablename}](../endpoints/ep-270.md) | Update a repo-level variable |
| GET | [/api/v1/repos/{owner}/{repo}/actions/workflows](../endpoints/ep-280.md) | List repository workflows from default branch |
| GET | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}](../endpoints/ep-281.md) | Get a specific workflow by ID (filename) |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable](../endpoints/ep-282.md) | Disable a workflow |
| POST | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches](../endpoints/ep-283.md) | Create a workflow dispatch event to trigger a workflow run |
| PUT | [/api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable](../endpoints/ep-284.md) | Enable a workflow |
| GET | [/api/v1/repos/{owner}/{repo}/activities/feeds](../endpoints/ep-374.md) | List a repository's activity feeds |
| GET | [/api/v1/repos/{owner}/{repo}/archive/{archive}](../endpoints/ep-392.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/assignees](../endpoints/ep-256.md) | Return all users that have write access and can be assigned to issues |
| POST | [/api/v1/repos/{owner}/{repo}/avatar](../endpoints/ep-262.md) | Update repository avatar image |
| DELETE | [/api/v1/repos/{owner}/{repo}/avatar](../endpoints/ep-263.md) | Delete repository custom avatar |
| GET | [/api/v1/repos/{owner}/{repo}/branch_protections](../endpoints/ep-313.md) | List all branch protection rules for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/branch_protections](../endpoints/ep-314.md) | Create a branch protection rule for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/branch_protections/priority](../endpoints/ep-317.md) | Update the priorities of branch protection rules for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-312.md) | Get a specific branch protection rule for the repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-315.md) | Edit a branch protection rule for a repository. Only fields that are set will be changed |
| DELETE | [/api/v1/repos/{owner}/{repo}/branch_protections/{name}](../endpoints/ep-316.md) | Delete a specific branch protection rule for the repository |
| POST | [/api/v1/repos/{owner}/{repo}/branches](../endpoints/ep-308.md) | Create a new branch in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/branches](../endpoints/ep-309.md) | List a repository's branches with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-306.md) | Retrieve a specific branch from a repository, including its effective branch protection |
| DELETE | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-307.md) | Delete a specific branch from a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-310.md) | Update a branch reference to a new commit |
| PATCH | [/api/v1/repos/{owner}/{repo}/branches/{branch}](../endpoints/ep-311.md) | Rename a branch in a repository |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators](../endpoints/ep-250.md) | List all collaborators of a repository with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-251.md) | Check if a user is a collaborator of a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-252.md) | Add or update a collaborator to a repository with specified permission level |
| DELETE | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}](../endpoints/ep-253.md) | Remove a collaborator from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/collaborators/{collaborator}/permission](../endpoints/ep-254.md) | Get repository permissions for a user |
| GET | [/api/v1/repos/{owner}/{repo}/commits](../endpoints/ep-215.md) | Get a list of all commits from a repository with pagination |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{ref}/status](../endpoints/ep-432.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{ref}/statuses](../endpoints/ep-431.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/commits/{sha}/pull](../endpoints/ep-217.md) | Get the merged pull request associated with a commit SHA |
| GET | [/api/v1/repos/{owner}/{repo}/compare/{basehead}](../endpoints/ep-434.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/contents](../endpoints/ep-394.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents](../endpoints/ep-400.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents-ext/{filepath}](../endpoints/ep-398.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-395.md) |  |
| PUT | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-396.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-397.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/contents/{filepath}](../endpoints/ep-399.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/diffpatch](../endpoints/ep-249.md) | Apply a diff patch to the repository, creating a new commit |
| GET | [/api/v1/repos/{owner}/{repo}/editorconfig/{filepath}](../endpoints/ep-393.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/file-contents](../endpoints/ep-401.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/file-contents](../endpoints/ep-402.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/forks](../endpoints/ep-333.md) | List a repository's forks |
| POST | [/api/v1/repos/{owner}/{repo}/forks](../endpoints/ep-334.md) | Fork a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/blobs/{sha}](../endpoints/ep-433.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/git/commits/{sha}](../endpoints/ep-214.md) | Get a single commit from a repository by SHA or ref |
| GET | [/api/v1/repos/{owner}/{repo}/git/commits/{sha}.{diffType}](../endpoints/ep-216.md) | Get a commit's diff or patch output as plain text |
| GET | [/api/v1/repos/{owner}/{repo}/git/notes/{sha}](../endpoints/ep-299.md) | Get a note corresponding to a single commit from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/refs](../endpoints/ep-247.md) | List all git references (branches, tags) of a repository |
| GET | [/api/v1/repos/{owner}/{repo}/git/refs/{ref}](../endpoints/ep-248.md) | Get specified ref or filtered list of refs by prefix |
| GET | [/api/v1/repos/{owner}/{repo}/git/tags/{sha}](../endpoints/ep-415.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/git/trees/{sha}](../endpoints/ep-246.md) | Gets the tree of a repository by SHA hash with pagination support |
| GET | [/api/v1/repos/{owner}/{repo}/hooks](../endpoints/ep-321.md) | List all webhooks configured for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/hooks](../endpoints/ep-324.md) | Create a webhook for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/git](../endpoints/ep-386.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-387.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-388.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/hooks/git/{id}](../endpoints/ep-389.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-322.md) | Get a specific webhook by ID for a repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-325.md) | Edit a webhook in a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/hooks/{id}](../endpoints/ep-326.md) | Delete a webhook from a repository |
| POST | [/api/v1/repos/{owner}/{repo}/hooks/{id}/tests](../endpoints/ep-323.md) | Test a push webhook by sending a test push payload |
| GET | [/api/v1/repos/{owner}/{repo}/issue_config](../endpoints/ep-372.md) | Returns the issue config for a repo |
| GET | [/api/v1/repos/{owner}/{repo}/issue_config/validate](../endpoints/ep-373.md) | Returns validation information for the issue config |
| GET | [/api/v1/repos/{owner}/{repo}/issue_templates](../endpoints/ep-371.md) | Get available issue templates for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/issues/pinned](../endpoints/ep-379.md) | List a repository's pinned issues (non-pull requests) |
| GET | [/api/v1/repos/{owner}/{repo}/keys](../endpoints/ep-340.md) | List a repository's deploy keys |
| POST | [/api/v1/repos/{owner}/{repo}/keys](../endpoints/ep-342.md) | Add a deploy key to a repository |
| GET | [/api/v1/repos/{owner}/{repo}/keys/{id}](../endpoints/ep-341.md) | Get a repository's deploy key by id |
| DELETE | [/api/v1/repos/{owner}/{repo}/keys/{id}](../endpoints/ep-343.md) | Delete a deploy key from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/languages](../endpoints/ep-375.md) | Get languages and number of bytes of code written in the repository |
| GET | [/api/v1/repos/{owner}/{repo}/licenses](../endpoints/ep-346.md) | Get the detected licenses for a repository |
| GET | [/api/v1/repos/{owner}/{repo}/media/{filepath}](../endpoints/ep-391.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/merge-upstream](../endpoints/ep-318.md) | Merge a branch from the upstream (base) repository into the fork |
| POST | [/api/v1/repos/{owner}/{repo}/mirror-sync](../endpoints/ep-234.md) | Adds a mirrored (pull) repository to the sync queue |
| GET | [/api/v1/repos/{owner}/{repo}/new_pin_allowed](../endpoints/ep-381.md) | Returns whether new issue/PR pins are allowed (based on max pin limit) |
| GET | [/api/v1/repos/{owner}/{repo}/pulls](../endpoints/ep-222.md) | List a repo's pull requests with filtering and pagination |
| POST | [/api/v1/repos/{owner}/{repo}/pulls](../endpoints/ep-226.md) | Create a new pull request |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/comments/{id}/resolve](../endpoints/ep-455.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/comments/{id}/unresolve](../endpoints/ep-456.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/pinned](../endpoints/ep-380.md) | List a repository's pinned pull requests |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{base}/{head}](../endpoints/ep-224.md) | Get a pull request by base and head branch references |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}](../endpoints/ep-223.md) | Get a single pull request by index |
| PATCH | [/api/v1/repos/{owner}/{repo}/pulls/{index}](../endpoints/ep-227.md) | Update a pull request (title, body, assignees, labels, milestone, state, base branch, deadline, allow_maintainer_edit) |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}.{diffType}](../endpoints/ep-225.md) | Get a pull request diff or patch file |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/comments/{id}/replies](../endpoints/ep-454.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/commits](../endpoints/ep-232.md) | Get commits for a pull request |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/files](../endpoints/ep-233.md) | Get changed files for a pull request |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-228.md) | Check if a pull request has been merged |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-229.md) | Merge a pull request or schedule auto-merge |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/merge](../endpoints/ep-231.md) | Cancel a scheduled auto-merge for a pull request |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers](../endpoints/ep-460.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/requested_reviewers](../endpoints/ep-461.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews](../endpoints/ep-451.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews](../endpoints/ep-458.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-452.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-457.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}](../endpoints/ep-459.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments](../endpoints/ep-453.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals](../endpoints/ep-462.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals](../endpoints/ep-463.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/pulls/{index}/update](../endpoints/ep-230.md) | Merge PR's base branch into head branch (update PR) |
| GET | [/api/v1/repos/{owner}/{repo}/push_mirrors](../endpoints/ep-236.md) | Lists all push mirrors of a repository with pagination |
| POST | [/api/v1/repos/{owner}/{repo}/push_mirrors](../endpoints/ep-238.md) | Creates a new push mirror for a repository |
| POST | [/api/v1/repos/{owner}/{repo}/push_mirrors-sync](../endpoints/ep-235.md) | Syncs all push mirrors of a repository by triggering each one |
| GET | [/api/v1/repos/{owner}/{repo}/push_mirrors/{name}](../endpoints/ep-237.md) | Gets a specific push mirror by its remote name |
| DELETE | [/api/v1/repos/{owner}/{repo}/push_mirrors/{name}](../endpoints/ep-239.md) | Deletes a push mirror from a repository by its remote name |
| GET | [/api/v1/repos/{owner}/{repo}/raw/{filepath}](../endpoints/ep-390.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/releases](../endpoints/ep-242.md) | List a repository's releases with pagination and optional draft/pre-release filters |
| POST | [/api/v1/repos/{owner}/{repo}/releases](../endpoints/ep-243.md) | Create a new release or convert an existing tag to a release |
| GET | [/api/v1/repos/{owner}/{repo}/releases/latest](../endpoints/ep-241.md) | Get the most recent non-prerelease, non-draft release sorted by created_at |
| GET | [/api/v1/repos/{owner}/{repo}/releases/tags/{tag}](../endpoints/ep-344.md) | Get a single release of a repository by tag name |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/tags/{tag}](../endpoints/ep-345.md) | Delete a release from a repository by tag name |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-240.md) | Get a single release by ID for a repository |
| PATCH | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-244.md) | Update a release's metadata (tag name, target, title, note, draft/prerelease status) |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/{id}](../endpoints/ep-245.md) | Delete a release (keeps the git tag, deletes attachments from storage) |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets](../endpoints/ep-353.md) | List all attachments of a release |
| POST | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets](../endpoints/ep-354.md) | Upload a file attachment to a release |
| GET | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-352.md) | Get a single attachment of a release by its ID |
| PATCH | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-355.md) | Update the name of a release attachment |
| DELETE | [/api/v1/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}](../endpoints/ep-356.md) | Delete a release attachment and its file from storage |
| GET | [/api/v1/repos/{owner}/{repo}/reviewers](../endpoints/ep-255.md) | Return all users that can be requested to review in this repo |
| GET | [/api/v1/repos/{owner}/{repo}/signing-key.gpg](../endpoints/ep-005.md) | Returns the GPG signing key for a given repository |
| GET | [/api/v1/repos/{owner}/{repo}/signing-key.pub](../endpoints/ep-007.md) | Returns the SSH signing key for a given repository |
| GET | [/api/v1/repos/{owner}/{repo}/stargazers](../endpoints/ep-327.md) | List users who starred the repository |
| POST | [/api/v1/repos/{owner}/{repo}/statuses/{sha}](../endpoints/ep-429.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/statuses/{sha}](../endpoints/ep-430.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/subscribers](../endpoints/ep-328.md) | List users watching (subscribed to) the repository |
| GET | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-196.md) | Check if the current user is watching a repo |
| PUT | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-197.md) | Watch a repo (subscribe to notifications) |
| DELETE | [/api/v1/repos/{owner}/{repo}/subscription](../endpoints/ep-198.md) | Unwatch a repo (unsubscribe from notifications) |
| GET | [/api/v1/repos/{owner}/{repo}/tag_protections](../endpoints/ep-419.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/tag_protections](../endpoints/ep-421.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-420.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-422.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/tag_protections/{id}](../endpoints/ep-423.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tags](../endpoints/ep-414.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/tags](../endpoints/ep-417.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/tags/{tag}](../endpoints/ep-416.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/tags/{tag}](../endpoints/ep-418.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/teams](../endpoints/ep-329.md) | List teams that have access to the repository (org repos only) |
| GET | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-330.md) | Check if a team is assigned to a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-331.md) | Add a team to a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/teams/{team}](../endpoints/ep-332.md) | Delete a team from a repository |
| GET | [/api/v1/repos/{owner}/{repo}/times](../endpoints/ep-412.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/times/{user}](../endpoints/ep-411.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/topics](../endpoints/ep-347.md) | Get list of topics that a repository has |
| PUT | [/api/v1/repos/{owner}/{repo}/topics](../endpoints/ep-348.md) | Replace list of topics for a repository |
| PUT | [/api/v1/repos/{owner}/{repo}/topics/{topic}](../endpoints/ep-349.md) | Add a topic to a repository |
| DELETE | [/api/v1/repos/{owner}/{repo}/topics/{topic}](../endpoints/ep-350.md) | Delete a topic from a repository |
| POST | [/api/v1/repos/{owner}/{repo}/transfer](../endpoints/ep-404.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/transfer/accept](../endpoints/ep-405.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/transfer/reject](../endpoints/ep-406.md) |  |
| POST | [/api/v1/repos/{owner}/{repo}/wiki/new](../endpoints/ep-445.md) |  |
| PATCH | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-446.md) |  |
| DELETE | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-447.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/page/{pageName}](../endpoints/ep-449.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/pages](../endpoints/ep-448.md) |  |
| GET | [/api/v1/repos/{owner}/{repo}/wiki/revisions/{pageName}](../endpoints/ep-450.md) |  |
| POST | [/api/v1/repos/{template_owner}/{template_repo}/generate](../endpoints/ep-364.md) | Create a repository using a template |
| GET | [/api/v1/repositories/{id}](../endpoints/ep-368.md) | Get a repository by its numeric ID |
| GET | [/api/v1/topics/search](../endpoints/ep-351.md) | Search topics via keyword |
| POST | [/api/v1/user/repos](../endpoints/ep-363.md) | Create a repository for the authenticated user |

