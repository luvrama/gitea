# Performance Analysis

**381 endpoints analyzed** · **198 issues found**

## Issues by Severity

### CRITICAL (2)

- **unbounded_queries**: db.Find called without ListOptions (no pagination), loading ALL matching notifications for the repo into memory — `routers/api/v1/notify/repo.go`
- **n_plus_1_queries**: For each notification: SetNotificationStatus does SELECT+UPDATE (2 queries), LoadAttributes does 4 SELECTs (repo, issue, user, comment), ToNotificationThread does GetIndividualUserRepoPermission + GetLastComment (2 more). Total: ~8 DB round-trips per notification. — `routers/api/v1/notify/repo.go`

### HIGH (36)

- **n_plus_1_queries**: SetNotificationStatus is called in a loop: each iteration does SELECT by ID + UPDATE. Then LoadAttributes does 4 individual queries per notification. — `routers/api/v1/notify/user.go`
- **unbounded_queries**: The initial db.Find has no pagination (ListOptions is zero-value). All matching notifications are loaded into memory. — `routers/api/v1/notify/user.go`
- **n_plus_1_queries**: convert.ToActivity calls GetDoerRepoPermission for each action in the result set — `services/convert/activity.go`
- **n_plus_1_queries**: convert.ToActionWorkflowJob loads task, steps, and runner individually per job in a loop — `services/convert/convert.go`
- **n_plus_1_queries**: When auth changes, RecalculateTeamAccesses is called per repo in a loop — `services/org/team.go`
- **n_plus_1_queries**: RemoveAllRepositoriesFromTeam iterates all team repos, calling RecalculateTeamAccesses per repo, then iterates all members per repo for watch cleanup — `services/repository/repo_team.go`
- **n_plus_1_queries**: Per-repo loop calling RecalculateUserAccess, ReconsiderWatches, and ReconsiderRepoIssuesAssignee — `services/org/team.go`
- **n_plus_1_queries**: For each repository in the team, GetDoerRepoPermission is called individually, resulting in N+1 database queries — `routers/api/v1/org/team.go`
- **n_plus_1_queries**: For each team member, HasAnyUnitAccess is called individually to check if they still have access, then WatchRepo/RemoveIssueWatchersByRepoID if not — `services/repository/repo_team.go`
- **n_plus_1_queries**: RemoveOrgUser iterates over all user's repos calling WatchRepo per repo, then iterates over all teams calling removeTeamMember per team. Each removeTeamMember itself iterates over team repos calling RecalculateUserAccess per repo. — `services/org/user.go`
- **n_plus_1_queries**: unstarRepos, unwatchRepos, unassignIssues, removeCollaborations all loop with page-by-page fetches and individual operations per item — `services/user/block.go`
- **n_plus_1_queries**: Branch protection cleanup iterates ALL protected branches in batches, checking each for user ID — `services/user/delete.go`
- **synchronous_blocking**: Walks entire filesystem tree synchronously on each request — `services/repository/adopt.go`
- **n_plus_1_queries**: ToActivities calls GetDoerRepoPermission for each action's repo individually — `services/convert/activity.go`
- **n_plus_1_queries**: For each starred repo, GetIndividualUserRepoPermission is called individually, loading units, checking collaborator status, and loading owner — `routers/api/v1/user/star.go`
- **n_plus_1_queries**: Same N+1 pattern as ep-152 - individual permission check per starred repo — `routers/api/v1/user/star.go`
- **synchronous_blocking**: RewriteAllPublicKeys rewrites the entire authorized_keys file from all keys in DB after every single key deletion — `services/asymkey/ssh_key_authorized_keys.go`
- **n_plus_1_queries**: GetDoerRepoPermission called in a loop for each repository in the page — `routers/api/v1/user/repo.go`
- **n_plus_1_queries**: LoadOwner and GetDoerRepoPermission called in loop for each repo — `routers/api/v1/user/repo.go`
- **n_plus_1_queries**: GetDoerRepoPermission called in a loop for each repository — `routers/api/v1/user/repo.go`
- **n_plus_1_queries**: Multiple paginated loops (unstarRepos, unwatchRepos, unassignIssues, removeCollaborations) each perform per-item operations inside loops — `services/user/block.go`
- **n_plus_1_queries**: GetIndividualUserRepoPermission is called per repo in a loop, each call triggers LoadUnits, IsCollaborator, and LoadOwner queries — `routers/api/v1/user/watch.go`
- **n_plus_1_queries**: GetIndividualUserRepoPermission is called per repo in a loop, each call triggers LoadUnits, IsCollaborator, and LoadOwner queries — `routers/api/v1/user/watch.go`
- **n_plus_1_queries**: GetPackageDescriptors iterates over each version and loads full descriptor individually — `models/packages/descriptor.go`
- **unbounded_queries**: BlockingDependencies() fetches ALL issues blocked by this issue without any DB-level pagination. Manual pagination is applied after fetching all results into memory. — `models/issues/issue.go`
- **n_plus_1_queries**: For each commit in the page, ToCommit is called which may trigger file status and diff stat git operations — `routers/api/v1/repo/commits.go`
- **n_plus_1_queries**: ToAPIPullRequests opens a git repository and iterates over PRs to get base branch SHA, checking branch existence for each head repo — `services/convert/pull.go`
- **unbounded_queries**: GetDiffForAPI loads ALL files (MaxFiles=-1) into memory before pagination is applied — `routers/api/v1/repo/pull.go`
- **synchronous_blocking**: Push mirror sync is done synchronously in the HTTP request handler, blocking the request thread for each mirror's git push operation — `routers/api/v1/repo/mirror.go`
- **unbounded_queries**: ListIssueAttachments calls issue.LoadAttributes which loads ALL issue data (comments, labels, milestones, reactions, etc.) just to extract attachments — `routers/api/v1/repo/issue_attachment.go`
- **n_plus_1_queries**: For each job, ToActionWorkflowJob loads task by ID, then loads task steps, then loads runner by ID - all individually per job — `services/convert/convert.go`
- **n_plus_1_queries**: For each branch in the page, GetBranchCommit is called individually to get the git commit, and convert.ToBranch makes individual permission checks — `routers/api/v1/repo/branch.go`
- **synchronous_blocking**: Git clone operation blocks the request thread with 10-minute timeout — `services/repository/fork.go`
- **n_plus_1_queries**: clearIssueLabels loops through all labels calling deleteIssueLabel individually, each creating a comment and updating label counts — `models/issues/issue_label.go`
- **synchronous_blocking**: RewriteAllPublicKeys reads ALL public keys from DB and rewrites the entire authorized_keys file on every single key deletion — `services/asymkey/ssh_key_authorized_keys.go`
- **n_plus_1_queries**: For each search result, LoadOwner and GetDoerRepoPermission are called individually in a loop — `routers/api/v1/repo/repo.go`

### MEDIUM (105)

- **no_caching**: Every request executes git config commands and gpg --export process — `services/asymkey/sign.go`
- **no_timeout**: gpg --export is called with timeout=-1 (no timeout) — `services/asymkey/sign.go`
- **no_caching**: Same as ep-004: gpg process spawned per request — `services/asymkey/sign.go`
- **no_timeout**: Same as ep-004: no timeout on gpg execution — `services/asymkey/sign.go`
- **synchronous_blocking**: Markup rendering is CPU-intensive and runs synchronously on the request goroutine with no size limit on input — `routers/api/v1/misc/markup.go`
- **no_timeout**: No timeout on markdown rendering - large or malicious input could consume CPU indefinitely — `routers/common/markup.go`
- **no_timeout**: No timeout or size limit on raw body reading and rendering — `routers/api/v1/misc/markup.go`
- **n_plus_1_queries**: ToNotificationThread calls GetIndividualUserRepoPermission and GetLastComment per notification in the convert layer — `services/convert/notification.go`
- **n_plus_1_queries**: Same N+1 pattern in ToNotificationThread as ep-019 (permission check + GetLastComment per notification) — `services/convert/notification.go`
- **synchronous_blocking**: Filesystem directory rename is performed inside the transaction commit path. If the filesystem is slow (NFS), this blocks the request. — `services/user/user.go`
- **unbounded_queries**: GetOrgRepositoryIDs loads ALL repo IDs without pagination — `models/repo/org_repo.go`
- **n_plus_1_queries**: Background deletion loops through repos one-by-one: GetRepositoryByID then DeleteRepository — `routers/api/v1/org/org.go`
- **n_plus_1_queries**: ToActionWorkflowRun calls run.GetLatestAttempt per run, which queries action_run_attempt individually — `services/convert/convert.go`
- **n_plus_1_queries**: ToTeams calls LoadUnits per team individually in a loop — `services/convert/convert.go`
- **n_plus_1_queries**: ToTeams calls LoadUnits per team individually, and GetOrgByID per unique org (mitigated by in-memory cache) — `services/convert/convert.go`
- **unbounded_queries**: When IncludesAllRepositories=true, AddAllRepositoriesToTeam loads ALL org repos and iterates them — `services/repository/repo_team.go`
- **n_plus_1_queries**: RemoveTeamIDFromProtectedBranch is called per branch protection in a loop — `services/org/team.go`
- **n_plus_1_queries**: removeInvalidOrgUser called per team member after deletion — `services/org/team.go`
- **n_plus_1_queries**: Auto-watch goroutine calls WatchRepo per team repository with no batching — `services/org/team.go`
- **n_plus_1_queries**: When AutoWatchNewRepos is enabled, WatchRepo is called individually for each team member inside the transaction — `services/repository/repo_team.go`
- **n_plus_1_queries**: convert.ToTeams calls LoadUnits for each team individually — `services/convert/convert.go`
- **unbounded_queries**: AccessibleTeamReposEnv.RepoIDs fetches all repo IDs for the team without limit, which are then used in an IN clause for the action query — `models/activities/action.go`
- **synchronous_blocking**: The entire member removal (including all team removals and access recalculations) runs in a single long-running database transaction — `services/org/user.go`
- **missing_indexes**: DELETE FROM comment WHERE label_id = ? may be slow without index on comment.label_id — `models/issues/label.go`
- **synchronous_blocking**: Entire block operation runs in a single large transaction with many sequential operations — `services/user/block.go`
- **no_timeout**: HaveIBeenPwned API call uses http.DefaultClient with no timeout configured — `modules/auth/password/pwn/pwn.go`
- **no_timeout**: HaveIBeenPwned API call has no explicit timeout configured — `modules/auth/password/pwn/pwn.go`
- **n_plus_1_queries**: Comment deletion in purge mode iterates comments in batches of 50, deleting one by one — `services/user/delete.go`
- **synchronous_blocking**: Purge mode deletes all repos synchronously before user deletion — `services/user/user.go`
- **synchronous_blocking**: RewriteAllPublicKeys regenerates entire authorized_keys file on every single key deletion — `services/asymkey/ssh_key.go`
- **n_plus_1_queries**: LoadAttributes loads run and repo for each job individually via jobList.LoadAttributes — `routers/api/v1/shared/action.go`
- **n_plus_1_queries**: ToActionWorkflowRun is called per-run in a loop; each may load run attempts individually — `routers/api/v1/shared/action.go`
- **n_plus_1_queries**: For each user directory, makes a GetUserByName query and a GetUserRepositories query — `services/repository/adopt.go`
- **missing_indexes**: LIKE search on lower(full_name) uses function call which may not use index — `models/user/email_address.go`
- **unbounded_queries**: GetUserBadges has no pagination - returns all badges for a user without limit — `models/user/badge.go`
- **n_plus_1_queries**: AddUserBadges loops through each badge slug doing 3 individual queries per badge (SELECT + EXISTS + INSERT) — `models/user/badge.go`
- **missing_indexes**: LIKE query on LOWER(full_name) cannot use index efficiently — `models/user/search.go`
- **no_caching**: Heatmap data is computed on every request with a heavy aggregation query over ~1 year of action data — `models/activities/user_heatmap.go`
- **no_caching**: Activity feeds are queried from DB on every request with no caching layer — `models/activities/action_list.go`
- **n_plus_1_queries**: convert.ToActionWorkflowRun is called per-run in a loop; each call may load run attempts individually — `routers/api/v1/shared/action.go`
- **n_plus_1_queries**: convert.ToActionWorkflowJob is called per-job in a loop after LoadAttributes; each conversion may trigger additional queries — `routers/api/v1/shared/action.go`
- **n_plus_1_queries**: appendPrivateInformation may fetch user by ID for each key if owner differs from default user — `routers/api/v1/user/key.go`
- **synchronous_blocking**: appendAuthorizedKeysToFile performs filesystem I/O synchronously during the request, writing to the authorized_keys file — `models/asymkey/ssh_key.go`
- **synchronous_blocking**: bcrypt.GenerateFromPassword with DefaultCost (10) is CPU-intensive, blocking the request goroutine for ~100ms — `models/auth/oauth2.go`
- **n_plus_1_queries**: Each email in the list triggers a separate SELECT to check existence and a separate INSERT — `services/user/email.go`
- **n_plus_1_queries**: Each email deletion triggers a separate SELECT and DELETE — `services/user/email.go`
- **synchronous_blocking**: All cleanup operations (unstar, unwatch, unassign, remove collaborations, cancel transfers) run synchronously in a single transaction — `services/user/block.go`
- **n_plus_1_queries**: GetPackageDescriptors iterates over each version and performs multiple queries per version (properties, files, blobs), though mitigated by EphemeralCache for shared entities — `models/packages/descriptor.go`
- **n_plus_1_queries**: GetAllPackageDescriptors loads all versions then builds descriptor for each one individually — `models/packages/descriptor.go`
- **n_plus_1_queries**: PackageDescriptor loading fetches blob for each file individually via cache.GetWithEphemeralCache — `models/packages/descriptor.go`
- **n_plus_1_queries**: Middleware loads blob for each file individually when building PackageDescriptor — `models/packages/descriptor.go`
- **n_plus_1_queries**: For each unique repo in the dependency list, a separate permission query is made. Mitigated by caching in repoPerms map, but still N queries for N unique repos. — `routers/api/v1/repo/issue_dependency.go`
- **n_plus_1_queries**: For each unique repo in the blocking list, a separate permission query is made (cached per repo) — `routers/api/v1/repo/issue_dependency.go`
- **no_caching**: User lookup by email is done on every request without caching (no userCache passed for single commit) — `services/convert/git_commit.go`
- **no_caching**: CommitsCount runs git rev-list --count on every request without caching — `modules/gitrepo/commit.go`
- **unbounded_queries**: Diff output is streamed without size limit - large commits could produce very large responses — `modules/git/diff.go`
- **missing_indexes**: Query on pull_request.merged_commit_id may not have a dedicated index — `models/issues/pull.go`
- **n_plus_1_queries**: GetIssueWatchers returns user IDs, then GetUsersByIDs fetches users separately. The watcher query already JOINs user table but doesn't return user data. — `routers/api/v1/repo/issue_subscription.go`
- **no_caching**: Multiple sequential DB queries to load related data (labels, posters, milestones, assignees, reviews) without caching — `services/convert/pull.go`
- **unbounded_queries**: Diff/patch output is streamed directly to response with no size limit. Large PRs with many changes can produce very large responses. — `services/pull/patch.go`
- **n_plus_1_queries**: Assignee validation loops through each assignee ID calling GetUserByID and CanBeAssigned individually — `routers/api/v1/repo/pull.go`
- **n_plus_1_queries**: Each field update is a separate DB operation without transaction wrapping all mutations — `routers/api/v1/repo/pull.go`
- **unbounded_queries**: All commits are loaded into memory via ShowPrettyFormatLogToList before pagination is applied — `routers/api/v1/repo/pull.go`
- **n_plus_1_queries**: Each SyncPushMirror call loads the push mirror by ID again from DB, even though it was already loaded in the list — `services/mirror/mirror_push.go`
- **no_timeout**: IsMigrateURLAllowed performs DNS lookup (net.LookupIP) without explicit timeout — `services/migrations/migrate.go`
- **writes_on_reads**: Delete does not remove the git remote from the repository, leaving orphaned git config — `routers/api/v1/repo/mirror.go`
- **n_plus_1_queries**: LoadAttributes is called in a loop for each release, causing separate queries for publisher and attachments per release — `routers/api/v1/repo/release.go`
- **unbounded_queries**: ListEntriesRecursiveWithSize can return very large result sets for repos with many files — `services/repository/files/tree.go`
- **unbounded_queries**: Returns all refs without pagination — `routers/api/v1/repo/git_ref.go`
- **synchronous_blocking**: Creates temporary repository clone, applies patch, and pushes - all synchronous on request thread — `services/repository/files/patch.go`
- **no_caching**: GetIndividualUserRepoPermission executes 4-6 DB queries per call with no caching — `models/perm/access/repo_permission.go`
- **n_plus_1_queries**: CanDoerChangeReviewRequests iterates over teams and calls IsTeamMember per team — `services/issue/review_request.go`
- **synchronous_blocking**: Image processing (decode, crop, resize, encode) happens synchronously on request thread — `modules/avatar/avatar.go`
- **n_plus_1_queries**: ToActionWorkflowRun calls run.GetLatestAttempt(ctx) individually for each run in the list — `services/convert/convert.go`
- **n_plus_1_queries**: ToActionTask calls LoadJob then LoadRun then LoadRepo individually per task — `services/convert/convert.go`
- **synchronous_blocking**: For each workflow entry, GetContentFromEntry reads blob content to parse workflow name - this is a git I/O operation per file — `services/convert/convert.go`
- **synchronous_blocking**: YAML unmarshal and concurrency evaluation happen before the DB transaction but still on the request thread — `services/actions/rerun.go`
- **n_plus_1_queries**: ToActionWorkflowJob loads task and steps individually per job in the convert loop — `services/convert/convert.go`
- **n_plus_1_queries**: Same N+1 task/step loading as ep-290 — `services/convert/convert.go`
- **synchronous_blocking**: Storage file deletions (logs + artifacts) happen synchronously after DB transaction, blocking the response — `services/actions/cleanup.go`
- **unbounded_queries**: All jobs, tasks, and artifacts for a run are loaded into memory without limit — `services/actions/cleanup.go`
- **no_caching**: Git note lookup involves multiple git operations (resolve ref, tree traversal, blob read) with no caching — `modules/git/notes_nogogit.go`
- **unbounded_queries**: FindCommentReactions has no pagination - returns all reactions for a comment — `models/issues/reaction.go`
- **synchronous_blocking**: SyncRepoBranches is called synchronously if branch count is 0, which walks all git refs — `routers/api/v1/repo/branch.go`
- **unbounded_queries**: checkBranchName walks ALL refs in the repository to check for name conflicts — `services/repository/branch.go`
- **n_plus_1_queries**: ToBranchProtection is called per rule, each call queries users with unit access and teams with repo access — `services/convert/convert.go`
- **n_plus_1_queries**: updateUserWhitelist calls GetUserByID and GetIndividualUserRepoPermission for each user in the whitelist — `models/git/protected_branch.go`
- **n_plus_1_queries**: Same N+1 pattern in updateUserWhitelist as ep-314, plus CheckPRsForBaseBranch iterates matched branches — `routers/api/v1/repo/branch.go`
- **synchronous_blocking**: Git push and merge operations are synchronous and can be slow for large repos — `services/repository/merge_upstream.go`
- **unbounded_queries**: When page=0, query returns all stargazers without limit — `models/repo/star.go`
- **unbounded_queries**: When page=0, query returns all watchers without limit — `models/repo/watch.go`
- **n_plus_1_queries**: LoadUnits is called for each team individually in convert.ToTeams loop — `services/convert/convert.go`
- **n_plus_1_queries**: Auto-watch iterates over team members and calls WatchRepo individually — `services/repository/repo_team.go`
- **n_plus_1_queries**: Iterates over team members checking HasAnyUnitAccess and removing watches individually — `services/repository/repo_team.go`
- **n_plus_1_queries**: GetDoerRepoPermission called in a loop for each fork — `routers/api/v1/repo/fork.go`
- **n_plus_1_queries**: HasIssueLabel is called per label in newIssueLabels loop, plus newIssueLabel inserts per label — `models/issues/issue_label.go`
- **n_plus_1_queries**: GetContent calls GetPublicKeyByID per deploy key in a loop to fetch SSH key content — `routers/api/v1/repo/key.go`
- **n_plus_1_queries**: SaveTopics iterates over added/removed topics, performing individual INSERT/UPDATE/DELETE per topic — `models/repo/topic.go`
- **no_caching**: LoadAttributes loads full release data (repo, publisher, all attachments) when only attachments are needed — `routers/api/v1/repo/release_attachment.go`
- **no_timeout**: Storage write operation has no explicit timeout configured — `services/attachment/attachment.go`
- **no_caching**: High-frequency search endpoint hits DB directly with no caching layer — `routers/api/v1/repo/repo.go`
- **synchronous_blocking**: Template generation copies git content synchronously which can be slow for large repos — `services/repository/template.go`
- **no_caching**: ToRepo performs 7+ DB queries per call with no caching for frequently accessed repo data — `services/convert/repository.go`
- **unbounded_queries**: Default pagination applies but action table can be very large; query relies on index — `models/activities/action_list.go`
- **n_plus_1_queries**: For each pinned PR, LoadAttributes and LoadBaseRepo/LoadHeadRepo are called individually in a loop — `routers/api/v1/repo/issue_pin.go`

### LOW (55)

- **no_caching**: Label template file is read from disk on every request (via label.LoadTemplateFile) — `modules/repository/init.go`
- **no_caching**: SSH key file is read from disk on every request — `services/asymkey/sign.go`
- **no_caching**: Same as ep-006: SSH key file read per request — `services/asymkey/sign.go`
- **no_caching**: Gitignore template files are read from disk on every request with no in-memory caching — `modules/assetfs/layered.go`
- **no_caching**: License template files are read from disk on every request with no in-memory caching — `modules/assetfs/layered.go`
- **n_plus_1_queries**: GetNotificationByID is called twice: once in getThread and once inside SetNotificationStatus — `models/activities/notification.go`
- **synchronous_blocking**: Filesystem removal (util.RemoveAll) and avatar storage deletion happen synchronously after the transaction commits — `services/org/org.go`
- **synchronous_blocking**: Image processing (decode, crop, resize) happens synchronously on request thread — `modules/avatar/avatar.go`
- **no_caching**: Existence check before insert could be replaced by unique constraint handling — `routers/api/v1/org/action.go`
- **n_plus_1_queries**: DeleteRunner re-fetches the runner by ID before deleting, even though it was already fetched by getRunnerByID — `models/actions/runner.go`
- **n_plus_1_queries**: After updating, GetRunner re-fetches the runner from DB instead of using the already-modified in-memory object — `routers/api/v1/shared/runners.go`
- **n_plus_1_queries**: ToTeam calls LoadUnits which queries team_unit per team, but for single team this is acceptable — `services/convert/convert.go`
- **writes_on_reads**: Re-fetches webhook after update instead of returning the already-modified in-memory object — `routers/api/v1/utils/hook.go`
- **synchronous_blocking**: UpdateLabel recalculates num_issues and num_closed_issues via subqueries on every update, even if only name/color changed — `models/issues/label.go`
- **synchronous_blocking**: Loop decrypts authorization header for each webhook using secret.DecryptSecret — `services/webhook/general.go`
- **writes_on_reads**: EditSystemHook re-fetches the webhook after update instead of returning the mutated object — `routers/api/v1/utils/hook.go`
- **no_caching**: Organization list is fetched from DB on every request with no caching — `routers/api/v1/admin/org.go`
- **missing_indexes**: 2FA filter uses LEFT JOIN on two_factor table which may be slow for large user bases — `models/user/search.go`
- **n_plus_1_queries**: DeleteRunner model function re-fetches the runner by ID even though it was already fetched in the handler — `models/actions/runner.go`
- **n_plus_1_queries**: After updating, GetRunner is called which re-fetches the runner from DB instead of returning the already-modified in-memory object — `routers/api/v1/shared/runners.go`
- **missing_indexes**: The heatmap query filters on created_unix with a range condition but also needs user_id filter from the ActivityQueryCondition — `models/activities/user_heatmap.go`
- **synchronous_blocking**: Image processing (decode, crop, resize, encode) happens synchronously on the request thread — `modules/avatar/avatar.go`
- **missing_indexes**: The visibility condition uses subqueries on follow and team_user tables which may be slow for users with many org memberships — `models/user/user.go`
- **missing_indexes**: Same visibility subquery concern as ep-139 — `models/user/user.go`
- **missing_indexes**: Same visibility subquery concern as ep-139 — `models/user/user.go`
- **writes_on_reads**: IsFollowing is called before the transaction, creating a TOCTOU race condition where two concurrent follow requests could both pass the check — `models/user/follow.go`
- **synchronous_blocking**: Each webhook's HeaderAuthorization is decrypted synchronously in a loop during ToHook conversion — `services/webhook/general.go`
- **missing_indexes**: Token name lookup (when deleting by name) queries by name+uid but name column is not indexed — `models/auth/access_token.go`
- **synchronous_blocking**: bcrypt.GenerateFromPassword with DefaultCost is CPU-intensive (~100ms) — `models/auth/oauth2.go`
- **n_plus_1_queries**: DeleteRunner internally calls GetRunnerByID again even though the runner was already fetched by getRunnerByID — `models/actions/runner.go`
- **unbounded_queries**: No pagination on email listing - returns all emails for user without limit — `routers/api/v1/user/email.go`
- **synchronous_blocking**: Cryptographic signature verification (hashAndVerifyWithSubKeys) is CPU-intensive and runs synchronously, tried up to 3 times with different line endings — `models/asymkey/gpg_key_verify.go`
- **synchronous_blocking**: OpenPGP key parsing and optional signature verification are CPU-intensive operations performed synchronously — `models/asymkey/gpg_key_add.go`
- **writes_on_reads**: StartPullRequestCheckOnView triggers a background queue task on GET request when PR status is 'checking' — `services/pull/check.go`
- **synchronous_blocking**: Git merge operation is synchronous and holds a global lock on the PR — `services/pull/merge.go`
- **synchronous_blocking**: Holds global lock during merge/rebase operation — `services/pull/update.go`
- **n_plus_1_queries**: ToPushMirror calls GetRepository for each push mirror to get repo name, but repo is already available in ctx.Repo.Repository — `services/convert/mirror.go`
- **synchronous_blocking**: Attachment file deletion from storage happens synchronously in the request path — `services/release/release.go`
- **synchronous_blocking**: Multiple cascading deletes in a single transaction could be slow for users with many issue assignments — `services/repository/collaboration.go`
- **synchronous_blocking**: ChangeContent is called after upload to trigger notifications, but it re-loads the repo and updates issue content even though content hasn't changed — `routers/api/v1/repo/issue_attachment.go`
- **no_caching**: Runner list is queried from DB on every request with no caching — `routers/api/v1/shared/runners.go`
- **n_plus_1_queries**: DeleteRunner in model re-fetches runner by ID before deleting (redundant with getRunnerByID) — `models/actions/runner.go`
- **n_plus_1_queries**: After updating, GetRunner is called again to return the updated runner (re-fetches from DB) — `routers/api/v1/shared/runners.go`
- **no_caching**: Lists all workflow entries to find one by name, reading all entries even though only one is needed — `services/convert/convert.go`
- **no_timeout**: Storage.ServeDirectURL and Storage.Open calls have no explicit timeout — `services/actions/artifacts.go`
- **n_plus_1_queries**: Each priority update is a separate UPDATE statement within the transaction — `models/git/protected_branch.go`
- **no_caching**: Webhook list is fetched from DB on every request with no caching — `routers/api/v1/repo/hook.go`
- **no_caching**: Re-fetches webhook after update instead of using the already-updated in-memory object — `routers/api/v1/utils/hook.go`
- **unbounded_queries**: LoadAttributes loads all issue relations (labels, assignees, etc.) when only labels are needed — `routers/api/v1/repo/issue_label.go`
- **n_plus_1_queries**: Redundant permission check: handler checks CanWriteIssuesOrPulls, then service re-checks via GetDoerRepoPermission — `services/issue/label.go`
- **missing_indexes**: Topic search uses LIKE '%keyword%' which cannot use standard B-tree indexes efficiently — `models/repo/topic.go`
- **synchronous_blocking**: Storage file deletion is synchronous on the request path — `models/repo/attachment.go`
- **writes_on_reads**: UpdateLabel recalculates num_issues and num_closed_issues via subqueries on every update, even if only name/color changed — `models/issues/label.go`
- **no_caching**: Parses template files from git on every request — `services/issue/template.go`
- **unbounded_queries**: No pagination - returns all pinned issues. However, max is limited by MaxPinned setting (default 3) — `models/issues/issue_pin.go`

## Issues by Type

| Type | Count | Severity |
|------|-------|----------|
| n_plus_1_queries | 88 | critical, high, low, medium |
| synchronous_blocking | 37 | high, low, medium |
| no_caching | 24 | low, medium |
| unbounded_queries | 23 | critical, high, low, medium |
| missing_indexes | 11 | low, medium |
| no_timeout | 9 | low, medium |
| writes_on_reads | 6 | low, medium |

## Optimization Recommendations

### P0

- **query_optimization**: Replace per-notification SetNotificationStatus loop with bulk UPDATE — *Reduce N*2 queries to 1 bulk UPDATE + 1 bulk SELECT*
- **query_optimization**: Replace per-item SetNotificationStatus loop with a single batch UPDATE — *Reduce N*2 queries to 1 query for the status update*
- **pagination**: Add pagination or a hard limit to the initial find query — *Prevent unbounded memory usage and query time*
- **query_optimization**: Only load attachments instead of full issue attributes — *Reduce from 12+ queries to 2 queries (issue + attachments)*

### P1

- **timeout**: Add timeout to gpg process execution — *Prevent request hangs when gpg is unresponsive*
- **timeout**: Add timeout to gpg process execution — *Prevent hangs*
- **pagination**: Add a limit to the unbounded find query or process in batches — *Prevent memory exhaustion and timeout for users with many notifications*
- **query_optimization**: For repo-scoped notifications, compute repo permission once since all notifications share the same repo — *Eliminate N-1 redundant permission queries*
- **query_optimization**: Batch permission checks for unique repos in activity list — *Reduce N+1 permission queries to 1 batch query for unique repos*
- **query_optimization**: Batch-load action_task, action_task_step, and action_runner for all jobs in a single query each — *Reduce queries from O(3N) to O(3) for the conversion phase*
- **query_optimization**: Batch access recalculation when team permissions change — *Could reduce from O(N*M) queries to O(N) where M = team members*
- **query_optimization**: Batch all cleanup operations in DeleteTeam — *Could reduce from O(R*M + P + M) to O(R + M + P) queries*
- **query_optimization**: Batch per-repo cleanup when removing team member — *Could reduce from O(3*N) to O(3) queries for N repos*
- **query_optimization**: Batch permission resolution for team repos — *Reduce from N+1 queries to 2 queries for listing team repos*
- **query_optimization**: Batch access check and unwatch for team members on repo removal — *Reduce from 2*M queries to 2-3 queries total*
- **query_optimization**: Batch load repos instead of per-ID GetRepositoryByID calls in the unwatch loop — *Reduce N repo queries to 1 batch query*
- **query_optimization**: Replace iterative unstar/unwatch/unassign loops with bulk DELETE statements — *Reduce DB operations from O(n) per relationship type to O(1)*
- **timeout**: Add HTTP client timeout for HaveIBeenPwned API calls — *Prevents request thread from blocking indefinitely on external API failure*
- **async**: Move purge operations to background job — *Prevent long-running HTTP requests for users with many repos*
- **caching**: Cache the unadopted repository list with a TTL — *Avoid repeated filesystem walks for the same data*
- **caching**: Cache heatmap results per user with 5-15 minute TTL — *Eliminate repeated expensive aggregation queries*
- **query_optimization**: Batch repo permission checks in ToActivities instead of per-action — *Reduce N permission queries to 1 batch query for unique repos*
- **query_optimization**: Batch permission loading for starred repos — *Reduce from ~150 queries to ~3-5 queries per request*
- **query_optimization**: Batch permission loading for starred repos — *Reduce from ~150 queries to ~3-5 queries per request*
- **query_optimization**: Batch permission loading for repository list — *Reduce DB queries from N+2 to 3 for a page of N repos*
- **query_optimization**: Batch load owners and permissions for repo list — *Reduce from 2N+2 queries to ~4 queries*
- **query_optimization**: Batch permission loading for org repo list — *Reduce from N+2 to 3 queries*
- **query_optimization**: Replace paginated per-item loops with batch DELETE statements — *Reduce from O(n) queries to O(1) per cleanup type*
- **query_optimization**: Batch load permissions for all repos in the page — *Reduce from 1+3N queries to ~4 queries total*
- **query_optimization**: Batch load permissions for all repos in the page — *Reduce from 1+3N queries to ~4 queries total*
- **query_optimization**: Batch load all files and properties for all versions in the page at once — *Reduce from O(N*5) queries to O(5) queries for a page of N versions*
- **pagination**: Add DB-level pagination to BlockingDependencies method — *Prevent loading unbounded results into memory*
- **query_optimization**: Batch git operations for file status and diff stats instead of per-commit subprocess calls — *Could reduce git subprocess calls from 100+ to 2-3 per request*
- **indexing**: Add index on pull_request(base_repo_id, merged_commit_id) — *Converts full scan to index lookup for PR-by-commit queries*
- **caching**: Add short-lived cache for PR list responses on high-traffic repos — *Reduce DB load by 80%+ for repeated list requests*
- **query_optimization**: Wrap all edit mutations in a single transaction to prevent partial writes — *Prevents inconsistent state on partial failure*
- **pagination**: Limit files loaded from git diff to the requested page instead of loading all — *Significant memory reduction for large PRs*
- **async**: Make push mirror sync asynchronous by queuing each mirror sync — *Reduce request latency from O(N * timeout) to O(1)*
- **query_optimization**: Use batch GetReleaseAttachments for all releases at once instead of per-release LoadAttributes — *Reduce N attachment queries to 1 batch query*
- **query_optimization**: Batch load tasks and runners for all jobs instead of per-job queries — *Reduce queries from O(3n) to O(3) for n jobs*
- **query_optimization**: Batch load latest attempts for all runs in a single query using run.LatestAttemptID — *Reduce from O(n) to O(1) queries for attempts*
- **query_optimization**: Use TaskList.LoadAttributes batch loading instead of per-task loading — *Reduce from O(3n) to O(3) queries*
- **query_optimization**: Batch-load ActionTask and ActionTaskStep for all jobs in one query — *Reduces queries from 2N to 2 for task/step loading*
- **query_optimization**: Batch git commit lookups for all branches in the page — *Reduce git operations from N to 1 batch operation*
- **async**: Fork creation could be fully async since it already returns 202 — *Free up request goroutine immediately for large repos*
- **query_optimization**: Replace per-label deletion loop with batch DELETE and single comment — *Reduce 3N queries to ~3 queries regardless of label count*
- **async**: Defer authorized_keys rewrite or use incremental update — *Reduce O(total_keys) to O(1) for single key deletion*
- **query_optimization**: Batch load owners and permissions instead of N+1 pattern — *Reduce queries from 2+2N to ~4 total*

### P2

- **caching**: Cache GPG public key export result — *Eliminate process spawn on every request*
- **timeout**: Add render timeout to prevent DoS via large documents — *Prevent CPU exhaustion from malicious large inputs*
- **timeout**: Add request body size limit and rendering timeout — *Prevents resource exhaustion from oversized inputs*
- **timeout**: Limit request body size and add rendering timeout — *Prevents memory exhaustion and CPU starvation*
- **query_optimization**: Batch permission checks for all unique repos in the notification list — *Reduce per-notification permission queries from N to 1 batch query*
- **query_optimization**: Batch-load action_run_attempt records for all runs using IN(latest_attempt_id) query — *Reduce N queries to 1 for attempt loading*
- **query_optimization**: Batch-load team_unit for all teams using WHERE team_id IN (...) — *Reduce N queries to 1 for unit loading*
- **query_optimization**: Batch-load team_unit and organizations for all teams — *Reduce N+M queries to 2 queries*
- **query_optimization**: Batch insert team_repo records instead of per-repo addRepositoryToTeam calls — *Reduces DB round-trips from O(N) to O(1) for IncludesAllRepositories*
- **query_optimization**: Batch watch insertion for team members — *Reduce M individual inserts to 1 batch insert*
- **query_optimization**: Batch LoadUnits for multiple teams — *Reduce from N+1 to 2 queries for team search*
- **query_optimization**: Use subquery for team repo IDs in activity feed query — *Avoid materializing large ID lists in memory and SQL*
- **query_optimization**: Batch delete access records and unwatch in single queries instead of per-repo operations — *Reduce 2N queries to 2 queries for repos*
- **timeout**: Add timeout to HaveIBeenPwned API call — *Prevent request hangs when external API is unavailable*
- **query_optimization**: Batch comment deletion instead of one-by-one — *Reduce DB round-trips for users with many comments*
- **async**: Debounce authorized_keys file regeneration — *Reduce filesystem I/O for bulk key operations*
- **query_optimization**: Batch load job attributes instead of N+1 — *Reduce DB queries from O(n) to O(1) for attribute loading*
- **query_optimization**: Batch load run attempts instead of per-run loading — *Reduce N+1 queries to 1 batch query*
- **indexing**: Consider adding index on lower(full_name) for email search performance — *Significant improvement for large instances with many users*
- **query_optimization**: Batch the badge lookups and existence checks into single queries — *Reduces from 3N queries to 3 queries for N badges*
- **query_optimization**: Add index on lower(full_name) for keyword search performance — *Faster keyword searches on large user tables*
- **indexing**: Add composite index on action(user_id, created_unix) — *Faster heatmap aggregation queries*
- **caching**: Cache activity feed results with short TTL — *Reduce DB load for frequently accessed user profiles*
- **query_optimization**: Batch-load run attempts instead of per-run loading — *Reduce N additional queries to 1 batch query*
- **query_optimization**: Verify LoadAttributes loads all data needed by ToActionWorkflowJob to avoid hidden N+1 — *Prevent potential N additional queries*
- **async**: Queue authorized_keys rewrite as async task instead of blocking the API response — *Reduces DELETE latency from O(n) file rewrite to O(1) DB delete*
- **query_optimization**: Batch email existence check and insertion — *Reduce from 2N+1 to 3 queries for N emails*
- **query_optimization**: Batch email lookup and deletion — *Reduce from 2N to 2 queries for N emails*
- **async**: Move cleanup operations to background job — *Reduce API response time from potentially seconds to milliseconds*
- **query_optimization**: Batch-load package_property and package_file records for all version IDs returned by SearchVersions — *Reduce DB round-trips from O(N*3) to O(3) for N results*
- **query_optimization**: Batch load package file blobs instead of individual lookups — *Reduce N queries to 1 for file blob loading*
- **caching**: File list for a version rarely changes; could cache the response — *Eliminate DB queries for repeated requests*
- **query_optimization**: Batch permission checks for all unique repos in the dependency list — *Reduce N permission queries to 1 batch query*
- **query_optimization**: Batch permission checks for all unique repos — *Reduce N permission queries to 1 batch query*
- **caching**: Disable stat/files/verification by default for high-frequency API consumers — *Eliminates git diff-tree and GPG verification per request*
- **caching**: Cache commit count for default branch — *Eliminates expensive rev-list --count for common case*
- **query_optimization**: Combine watcher query and user fetch into single query returning user data — *Eliminate 1 DB round-trip per request*
- **query_optimization**: Batch load all branch SHAs needed for the page in one query — *Reduce branch lookups from N to 1*
- **pagination**: Add optional size limit parameter for diff downloads — *Prevent OOM on extremely large PRs*
- **pagination**: Use git log --skip/--max-count for server-side pagination instead of loading all commits — *Reduce memory usage for large PRs from O(N) to O(page_size)*
- **query_optimization**: Add git remote cleanup on delete — *Prevent git config bloat from orphaned remotes*
- **pagination**: Apply pagination at git level rather than loading all entries first — *Reduce memory usage for large trees from O(n) to O(page_size)*
- **pagination**: Add page/limit query params to refs listing — *Prevent large responses for repos with many refs*
- **caching**: Cache permission results per user+repo for short TTL — *Reduce 4-6 queries to 1 cache lookup for repeated permission checks*
- **query_optimization**: Replace per-team IsTeamMember loop with batch query — *Reduce N queries to 1 for team membership check*
- **caching**: Cache workflow metadata (name, state) keyed by commit SHA + workflow path — *Avoid repeated git blob reads for unchanged workflows*
- **query_optimization**: Batch insert cloned jobs instead of inserting one-by-one in loop — *Reduces DB round-trips from N to 1 for job creation*
- **async**: Move storage file deletions to background after DB transaction completes — *Reduce response time by eliminating storage I/O from request path*
- **caching**: Cache the notes ref commit resolution to avoid repeated git operations — *Reduce git operations by 50% for repeated note lookups*
- **pagination**: Add page/limit query params to comment reactions endpoint — *Prevent large response payloads for popular comments*
- **query_optimization**: Replace full ref walk with targeted git ref existence check — *Reduce branch creation time for large repos from O(n) to O(1)*
- **caching**: Cache user permission results since they don't change per-request — *Reduce DB queries for permission checks from N to 1*
- **query_optimization**: Batch the user/team access queries outside the loop — *Reduce from 2*N+1 queries to 3 queries for listing*
- **query_optimization**: Batch user lookups and permission checks in updateUserWhitelist — *Reduce from 2*M queries to 2 queries per whitelist type*
- **query_optimization**: Batch PR checks for multiple matched branches — *Reduce from N queries to 1 query for glob rules matching many branches*
- **async**: Consider making merge-upstream async for large repos — *Prevent request timeouts on large repositories*
- **pagination**: Enforce default pagination when page param is 0 — *Prevents unbounded result sets for popular repos*
- **pagination**: Enforce default pagination when page param is 0 — *Prevents unbounded result sets for popular repos*
- **query_optimization**: Batch load team units instead of per-team queries — *Reduces N+1 to 2 queries total*
- **query_optimization**: Batch watch insertions for team members — *Reduce N individual inserts to 1 batch insert for large teams*
- **query_optimization**: Batch access check and watch removal for team members — *Reduce 2N queries to 2 batch queries for large teams*
- **query_optimization**: Batch permission loading for fork list — *Reduce N permission queries to 1 batch query*
- **query_optimization**: Batch-check existing issue_label relations before per-label loop — *Reduce N SELECT queries to 1 for existence check*
- **query_optimization**: Join public_key table in FindAndCount query to load content in one query — *Reduce N+1 to 1 query*
- **query_optimization**: Batch topic add/remove operations instead of per-topic queries — *Reduce from O(n) queries to O(1) for bulk topic replacement*
- **query_optimization**: Replace LoadAttributes with direct attachment query for this endpoint — *Eliminate 1-2 unnecessary DB queries per request*
- **timeout**: Add timeout to storage save operation — *Prevent request thread blocking on slow storage*
- **caching**: Cache release count and branch count per repo — *Reduce 2 COUNT queries per request*
- **indexing**: Ensure index on action(repo_id, created_unix DESC) for repo feed queries — *Faster pagination for repo activity feeds*

### P3

- **caching**: Cache parsed label template results in memory — *Eliminate disk reads for repeated requests*
- **caching**: Cache SSH public key file content — *Eliminate file read per request*
- **caching**: Add HTTP caching headers since gitignore templates rarely change — *Reduces redundant requests from clients*
- **caching**: Response could be cached since license list is static after startup — *Eliminates per-request allocation of response array*
- **caching**: Add HTTP caching headers since license templates rarely change — *Reduces redundant requests and filesystem reads from clients*
- **caching**: This is likely a high-frequency polling endpoint. Consider short-lived cache. — *Reduce DB load from polling clients*
- **caching**: Consider caching org list for anonymous users since public org list changes infrequently — *Reduce DB load for unauthenticated listing requests*
- **query_optimization**: Email and other fields are updated in two separate UPDATE statements; could be combined into one — *Save 1 DB round-trip per request*
- **async**: Already uses async background deletion - good pattern — *Request returns immediately (202), deletion happens in background*
- **query_optimization**: Batch WatchRepo calls in auto-watch goroutine — *Reduces background DB load from O(N) to O(1)*
- **query_optimization**: Avoid re-fetching webhook after update — *Saves 1 DB query per edit operation*
- **query_optimization**: Optimize 2FA filter query — *Faster admin user search when filtering by 2FA status*
- **query_optimization**: Eliminate redundant GetRunnerByID call in model layer since handler already validated existence — *Saves 1 DB query per delete*
- **query_optimization**: Return the in-memory runner after update instead of re-fetching from DB — *Saves 1 DB query per update*
- **pagination**: Add pagination to GetUserBadges — *Low impact since badge count per user is typically small*
- **caching**: Consider caching following list for popular users — *Reduce DB load for frequently accessed profiles*
- **indexing**: Add composite index on access_token(uid, name) — *Faster name-based token lookups*
- **query_optimization**: Avoid redundant GetRunnerByID call in DeleteRunner since caller already validated existence — *Saves 1 DB query per delete*
- **query_optimization**: For deletion, only minimal descriptor info is needed for notifications. Use a lighter query that doesn't load all files/blobs/properties — *Reduce pre-deletion query load significantly for packages with many versions*
- **caching**: Latest version changes infrequently; could be cached with short TTL — *Reduce DB load for frequently accessed latest version*
- **query_optimization**: Pre-set Repo field on PushMirror objects before conversion — *Eliminate N redundant repository lookups*
- **async**: Move attachment file deletion to a background job — *Faster DELETE response when releases have many attachments*
- **timeout**: Add timeout for git apply operations — *Prevent hung requests from consuming resources indefinitely*
- **query_optimization**: Use dedicated notification instead of ChangeContent hack — *Save 2 DB queries per attachment upload*
- **caching**: Avatar hash check prevents re-upload of same image — *Already optimized - skips processing if same image*
- **caching**: Secrets list rarely changes, could benefit from short TTL cache — *Minimal - secrets are not frequently listed*
- **query_optimization**: Directly access workflow file by path instead of listing all entries — *Minor improvement - avoids listing all entries*
- **query_optimization**: Use a single UPDATE with CASE WHEN for all priority values — *Reduce from N queries to 1 query*
- **query_optimization**: Avoid re-fetching webhook after update — *Eliminates 1 SELECT per edit request*
- **query_optimization**: Load only labels instead of all attributes — *Eliminate 4-5 unnecessary queries per request*
- **caching**: Cache release data for frequently accessed releases — *Reduce DB load for popular releases*
- **indexing**: Add trigram index on topic.name for PostgreSQL or use prefix matching — *Faster topic search for large datasets*
- **async**: Perform storage file deletion asynchronously — *Faster delete response times*
- **caching**: Language stats are computed by background indexer and rarely change - could cache response — *Reduce DB load for frequently accessed repos*
- **query_optimization**: Batch load PR attributes instead of per-item loading — *Reduce queries from ~9 to ~3 for default MaxPinned=3*
