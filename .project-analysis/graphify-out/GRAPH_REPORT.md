# Graph Report - /Users/relumalai/workshop/gitea  (2026-05-12)

## Corpus Check
- 0 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2553 nodes · 5233 edges · 111 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M` - 125 edges
2. `Pin order is assigned as max existing order + 1 when pinning` - 91 edges
3. `Unpinning creates a comment of type CommentTypeUnpin in issue history` - 90 edges
4. `Pinned issues are separated by type (issues vs pull requests)` - 88 edges
5. `Pin position must be >= 1` - 86 edges
6. `Moving pin reorders other pins - shifts up or down depending on direction` - 78 edges
7. `IsNewPinAllowed compares current pin count against MaxPinned setting` - 76 edges
8. `Language stats response is a custom JSON object mapping language name to byte co` - 70 edges
9. `Issue templates are parsed from multiple candidate directories in priority order` - 63 edges
10. `Unarchiving a repo re-detects action schedules` - 62 edges
11. `user_model.User` - 58 edges
12. `repository` - 36 edges
13. `convert.ToUser` - 28 edges
14. `repo_model.Repository` - 27 edges
15. `reqOrgOwnership` - 27 edges

## Surprising Connections (you probably didn't know these)
- `GET /api/v1/users/search` --data_flow--> `user.Search`  [EXTRACTED]
  session_18/api_contracts.json → routers/api/v1/user/user.go
- `DELETE /api/v1/user/actions/variables/{variablename}` --data_flow--> `user.DeleteVariable`  [EXTRACTED]
  session_19/api_contracts.json → routers/api/v1/user/action.go
- `GET /api/v1/user/actions/runs` --data_flow--> `user.ListWorkflowRuns`  [EXTRACTED]
  session_20/api_contracts.json → routers/api/v1/user/action.go
- `GET /api/v1/repos/{owner}/{repo}/actions/variables/{variablename}` --data_flow--> `Action.GetVariable`  [EXTRACTED]
  session_39/api_contracts.json → routers/api/v1/repo/action.go
- `user.ListWorkflowJobs` --calls--> `shared.ListJobs`  [EXTRACTED]
  routers/api/v1/user/action.go → session_42/impact_analysis_index.json
- `user.GetContextUserByPathParam` --calls--> `org_service.AddTeamMember`  [EXTRACTED]
  routers/api/v1/user/helper.go → session_9/impact_analysis_index.json
- `user.GetContextUserByPathParam` --calls--> `org_service.RemoveTeamMember`  [EXTRACTED]
  routers/api/v1/user/helper.go → session_9/impact_analysis_index.json
- `miscellaneous` --serves--> `GET /api/v1/version`  [EXTRACTED]
  routers/api/v1/misc/version.go → session_1/api_contracts.json
- `GET /api/v1/version` --data_flow--> `misc.Version`  [EXTRACTED]
  session_1/api_contracts.json → routers/api/v1/misc/version.go
- `GET /api/v1/version` --configured_by--> `APP_VER`  [EXTRACTED]
  session_1/api_contracts.json → modules/setting/setting.go

## Communities

### Community 0 - "Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M"
Cohesion: 0.02
Nodes (189): SECRET_KEY (general token signing), actions.MAX_RERUN_ATTEMPTS, actions.artifact_storage.SERVE_DIRECT, actions.artifact_storage.STORAGE_TYPE, setting.PanicInDevOrTesting, Action.DeleteRunner, Action.GetRunner, Action.ListRunners (+181 more)

### Community 1 - "Controller: user_model.User"
Cohesion: 0.02
Nodes (151): API.DefaultPagingNum, API.MaxResponseItems, setting.API.DefaultPagingNum, setting.API.MaxResponseItems, org.Action.ListVariables, org.ConcealMember, org.DeleteMember, org.GetLabel (+143 more)

### Community 2 - "Endpoint: routers"
Cohesion: 0.01
Nodes (148): APP_VER, api.DefaultGitTreesPerPage, repository.PREFERRED_LICENSES, issue, issue, issue, issue, issue (+140 more)

### Community 3 - "Controller: convert"
Cohesion: 0.03
Nodes (135): attachment.ALLOWED_TYPES, attachment.ENABLED, attachment.MAX_SIZE, repository.release.ALLOWED_TYPES, repository.release.FILE_MAX_SIZE, server.APP_URL, issue, repo.CreateIssueAttachment (+127 more)

### Community 4 - "Controller: IsNewPinAllowed compares current pin count against MaxPinned setting"
Cohesion: 0.03
Nodes (133): mirror.MinInterval, repository.ForcePrivate, service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES, service.DEFAULT_ENABLE_DEPENDENCIES, admin.ListCronTasks, admin, issue, issue (+125 more)

### Community 5 - "Controller: POST /api/v1/orgs"
Cohesion: 0.03
Nodes (128): SECRET_KEY, Service.DefaultOrgMemberVisible, api.default_paging_num, api.max_response_items, service.default_org_member_visible, setting.Admin.DisableRegularOrgCreation, setting.Service.DefaultOrgMemberVisible, Action.CreateOrUpdateSecret (+120 more)

### Community 6 - "Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels"
Cohesion: 0.03
Nodes (116): issue, issue, issue, org.CreateLabel, org.DeleteLabel, org.EditLabel, org.ListLabels, organization (+108 more)

### Community 7 - "Controller: Pin order is assigned as max existing order + 1 when pinning"
Cohesion: 0.04
Nodes (113): actions.workflow_dirs, git.HOME_PATH, repository.SIGNING_FORMAT, repository.SIGNING_KEY, service.auto_watch_on_changes, Action.CreateVariable, Action.ListVariables, Action.UpdateVariable (+105 more)

### Community 8 - "Controller: webhook_service.ToHook"
Cohesion: 0.03
Nodes (112): AppURL, SecretKey, setting.DisableWebhooks, setting.SecretKey, admin.DeleteHook, admin.EditHook, admin.GetHook, admin.ListHooks (+104 more)

### Community 9 - "Controller: reqOrgOwnership"
Cohesion: 0.04
Nodes (109): service.AUTO_WATCH_NEW_REPOS, service.AutoWatchNewRepos, org.AddTeamMember, org.AddTeamRepository, org.CreateTeam, org.DeleteTeam, org.EditTeam, org.GetTeam (+101 more)

### Community 10 - "Controller: Unarchiving a repo re-detects action schedules"
Cohesion: 0.03
Nodes (108): api.DefaultPagingNum, api.MaxResponseItems, repository.FORCE_PRIVATE, repository.force_private, admin.CreateRepo, admin.PostCronTask, admin, org.BlockUser (+100 more)

### Community 11 - "Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge"
Cohesion: 0.03
Nodes (105): git.MAX_GIT_DIFF_LINES, git.MAX_GIT_DIFF_LINE_CHARACTERS, repository.PULL_REQUEST_DEFAULT_MERGE_STYLE, setting.IsInTesting, admin.RenameUser, repo.CancelScheduledAutoMerge, repo.CreatePullRequest, repo.DownloadPullDiffOrPatch (+97 more)

### Community 12 - "Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections"
Cohesion: 0.03
Nodes (101): repo.CreateBranch, repo.CreateBranchProtection, repo.DeleteBranch, repo.DeleteBranchProtection, repo.EditBranchProtection, repo.GetBranch, repo.GetBranchProtection, repo.ListBranchProtections (+93 more)

### Community 13 - "Controller: Pinned issues are separated by type (issues vs pull requests)"
Cohesion: 0.03
Nodes (100): api.DEFAULT_GIT_TREES_PER_PAGE, api.DEFAULT_MAX_BLOB_SIZE, api.DEFAULT_MAX_RESPONSE_SIZE, api.DEFAULT_PAGING_NUM, api.MAX_RESPONSE_ITEMS, service.RegisterEmailConfirm, Action.ListActionsSecrets, admin.GetAllEmails (+92 more)

### Community 14 - "Controller: Issue templates are parsed from multiple candidate directories in priority order"
Cohesion: 0.04
Nodes (85): OAuth2.CustomSchemes, OAuth2.DefaultApplications, setting.OAuth2.CustomSchemes, setting.SuccessfulTokensCacheSize, Action.DeleteVariable, Action.GetVariable, admin.AddUserBadges, admin.DeleteUserBadges (+77 more)

### Community 15 - "Controller: POST /api/v1/user/keys"
Cohesion: 0.04
Nodes (83): SSH.MinimumKeySizeCheck, SSH.StartBuiltinServer, USER_DELETE_WITH_COMMENTS_MAX_TIME, admin.EXTERNAL_USER_DISABLE_FEATURES, admin.USER_DISABLED_FEATURES, ssh.MINIMUM_KEY_SIZE_CHECK, ssh.START_BUILTIN_SERVER, admin.CreatePublicKey (+75 more)

### Community 16 - "Controller: issues_model.Issue"
Cohesion: 0.05
Nodes (68): repository.issue.MAX_PINNED, ui.REACTIONS, issue, issue, repo.AreNewIssuePinsAllowed, repo.DeleteIssueCommentReaction, repo.DeleteIssueReaction, repo.GetIssueCommentReactions (+60 more)

### Community 17 - "Controller: GET /api/v1/packages/{owner}"
Cohesion: 0.06
Nodes (64): Cache: EphemeralCache, packages.ENABLED, packages.limit_total_owner_count, service.REQUIRE_SIGNIN_VIEW, service.require_signin_view_strict, package, packages.DeletePackage, packages.DeletePackageVersion (+56 more)

### Community 18 - "Controller: POST /api/v1/repos/{owner}/{repo}/avatar"
Cohesion: 0.05
Nodes (54): AVATAR_MAX_HEIGHT, AVATAR_MAX_ORIGIN_SIZE, AVATAR_MAX_WIDTH, AVATAR_RENDERED_SIZE_FACTOR, Avatar.MaxHeight, Avatar.MaxOriginSize, Avatar.MaxWidth, avatar.MAX_HEIGHT (+46 more)

### Community 19 - "Controller: POST /api/v1/user/gpg_keys"
Cohesion: 0.06
Nodes (51): admin.USER_DISABLED_FEATURES / admin.EXTERNAL_USER_DISABLE_FEATURES, setting.UserFeatureManageGPGKeys, user.CreateGPGKey, user.DeleteGPGKey, user.GetGPGKey, user.GetVerificationToken, user.ListGPGKeys, user.ListMyGPGKeys (+43 more)

### Community 20 - "Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors"
Cohesion: 0.06
Nodes (50): git.TIMEOUT.MIRROR, lfs.START_SERVER, mirror.ENABLED, mirror.MIN_INTERVAL, repository.DISABLE_HTTP_GIT, ui.CUSTOM_EMOJIS, ui.DEFAULT_THEME, repo.AddPushMirror (+42 more)

### Community 21 - "Controller: Org repo creation requires user to have create permission in org"
Cohesion: 0.07
Nodes (42): Action.CreateRegistrationToken, admin.CreateRegistrationToken, org.Action.CreateRegistrationToken, repo.AddTopic, repo.DeleteTopic, repo.ListTopics, repo.TopicSearch, repo.UpdateTopics (+34 more)

### Community 22 - "Error Scenario: POST /api/v1/admin/users"
Cohesion: 0.06
Nodes (41): MIN_PASSWORD_LENGTH, MinPasswordLength, PASSWORD_CHECK_PWN, PasswordCheckPwn, admin.CreateUser, admin.EditUser, user.GetUserSettings, user.UpdateUserSettings (+33 more)

### Community 23 - "Controller: GET /api/v1/repos/{owner}/{repo}/commits"
Cohesion: 0.08
Nodes (38): api.SwaggerURL, git.CommitsRangeSize, repo.DownloadCommitDiffOrPatch, repo.GetAllCommits, repo.GetNote, repo.GetSingleCommit, repository, repository (+30 more)

### Community 24 - "Controller: GET /api/v1/repos/search"
Cohesion: 0.1
Nodes (28): repository.issue.MaxPinned, repo.Delete, repo.GetIssueConfig, repo.GetIssueTemplates, repo.Search, repo.ValidateIssueConfig, repository, GET /api/v1/repos/search (+20 more)

### Community 25 - "Controller: PUT /api/v1/user/starred/{owner}/{repo}"
Cohesion: 0.11
Nodes (26): setting.Repository.DisableStars, user.GetMyStarredRepos, user.GetStarredRepos, user.IsStarring, user.Star, user.Unstar, user, GET /api/v1/users/{username}/starred (+18 more)

### Community 26 - "Controller: GET /api/v1/gitignore/templates/{name}"
Cohesion: 0.1
Nodes (25): setting.AppURL, setting.CustomPath, setting.Repository.PreferredLicenses, misc.GetGitignoreTemplateInfo, misc.GetLicenseTemplateInfo, misc.ListGitignoresTemplates, misc.ListLicenseTemplates, miscellaneous (+17 more)

### Community 27 - "Controller: POST /api/v1/markdown"
Cohesion: 0.11
Nodes (23): setting.AppSubURL, misc.Markdown, misc.MarkdownRaw, misc.Markup, miscellaneous, POST /api/v1/markup, POST /api/v1/markdown, POST /api/v1/markdown/raw (+15 more)

### Community 28 - "Controller: POST /api/v1/admin/unadopted/{owner}/{repo}"
Cohesion: 0.15
Nodes (19): database.iterate_buffer_size, repository.root_path, admin.AdoptRepository, admin.DeleteUnadoptedRepository, admin.ListUnadoptedRepositories, admin, GET /api/v1/admin/unadopted, POST /api/v1/admin/unadopted/{owner}/{repo} (+11 more)

### Community 29 - "Controller: POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
Cohesion: 0.16
Nodes (16): repo.ActionsDisableWorkflow, repo.ActionsDispatchWorkflow, repo.ActionsEnableWorkflow, PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable, POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches, PUT /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable, 403 workflow is disabled in repo config, 404 git ref doesn't exist (+8 more)

### Community 30 - "Controller: GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}"
Cohesion: 0.29
Nodes (11): repo.GetGitAllRefs, repo.GetGitRefs, repository, GET /api/v1/repos/{owner}/{repo}/git/refs, GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}, 404 Empty refs list, api.Reference, repo.GetGitAllRefs (+3 more)

### Community 31 - "Module: cmd"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "Module: models"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Module: modules"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "Module: services"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Module: web_src"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "Library: code.gitea.io/actions-proto-go"
Cohesion: 1.0
Nodes (1): code.gitea.io/actions-proto-go

### Community 37 - "Library: code.gitea.io/sdk/gitea"
Cohesion: 1.0
Nodes (1): code.gitea.io/sdk/gitea

### Community 38 - "Library: connectrpc.com/connect"
Cohesion: 1.0
Nodes (1): connectrpc.com/connect

### Community 39 - "Library: gitea.com/go-chi/binding"
Cohesion: 1.0
Nodes (1): gitea.com/go-chi/binding

### Community 40 - "Library: gitea.com/go-chi/cache"
Cohesion: 1.0
Nodes (1): gitea.com/go-chi/cache

### Community 41 - "Library: gitea.com/go-chi/captcha"
Cohesion: 1.0
Nodes (1): gitea.com/go-chi/captcha

### Community 42 - "Library: gitea.com/go-chi/session"
Cohesion: 1.0
Nodes (1): gitea.com/go-chi/session

### Community 43 - "Library: gitea.com/lunny/levelqueue"
Cohesion: 1.0
Nodes (1): gitea.com/lunny/levelqueue

### Community 44 - "Library: github.com/42wim/httpsig"
Cohesion: 1.0
Nodes (1): github.com/42wim/httpsig

### Community 45 - "Library: github.com/42wim/sshsig"
Cohesion: 1.0
Nodes (1): github.com/42wim/sshsig

### Community 46 - "Library: github.com/Azure/azure-sdk-for-go/sdk/storage/azblob"
Cohesion: 1.0
Nodes (1): github.com/Azure/azure-sdk-for-go/sdk/storage/azblob

### Community 47 - "Library: github.com/ProtonMail/go-crypto"
Cohesion: 1.0
Nodes (1): github.com/ProtonMail/go-crypto

### Community 48 - "Library: github.com/PuerkitoBio/goquery"
Cohesion: 1.0
Nodes (1): github.com/PuerkitoBio/goquery

### Community 49 - "Library: github.com/alecthomas/chroma/v2"
Cohesion: 1.0
Nodes (1): github.com/alecthomas/chroma/v2

### Community 50 - "Library: github.com/aws/aws-sdk-go-v2/credentials"
Cohesion: 1.0
Nodes (1): github.com/aws/aws-sdk-go-v2/credentials

### Community 51 - "Library: github.com/aws/aws-sdk-go-v2/service/codecommit"
Cohesion: 1.0
Nodes (1): github.com/aws/aws-sdk-go-v2/service/codecommit

### Community 52 - "Library: github.com/blevesearch/bleve/v2"
Cohesion: 1.0
Nodes (1): github.com/blevesearch/bleve/v2

### Community 53 - "Library: github.com/caddyserver/certmagic"
Cohesion: 1.0
Nodes (1): github.com/caddyserver/certmagic

### Community 54 - "Library: github.com/go-chi/chi/v5"
Cohesion: 1.0
Nodes (1): github.com/go-chi/chi/v5

### Community 55 - "Library: github.com/go-chi/cors"
Cohesion: 1.0
Nodes (1): github.com/go-chi/cors

### Community 56 - "Library: github.com/go-co-op/gocron/v2"
Cohesion: 1.0
Nodes (1): github.com/go-co-op/gocron/v2

### Community 57 - "Library: github.com/go-enry/go-enry/v2"
Cohesion: 1.0
Nodes (1): github.com/go-enry/go-enry/v2

### Community 58 - "Library: github.com/go-git/go-git/v5"
Cohesion: 1.0
Nodes (1): github.com/go-git/go-git/v5

### Community 59 - "Library: github.com/go-ldap/ldap/v3"
Cohesion: 1.0
Nodes (1): github.com/go-ldap/ldap/v3

### Community 60 - "Library: github.com/go-redsync/redsync/v4"
Cohesion: 1.0
Nodes (1): github.com/go-redsync/redsync/v4

### Community 61 - "Library: github.com/go-sql-driver/mysql"
Cohesion: 1.0
Nodes (1): github.com/go-sql-driver/mysql

### Community 62 - "Library: github.com/go-webauthn/webauthn"
Cohesion: 1.0
Nodes (1): github.com/go-webauthn/webauthn

### Community 63 - "Library: github.com/golang-jwt/jwt/v5"
Cohesion: 1.0
Nodes (1): github.com/golang-jwt/jwt/v5

### Community 64 - "Library: github.com/google/go-github/v85"
Cohesion: 1.0
Nodes (1): github.com/google/go-github/v85

### Community 65 - "Library: github.com/google/uuid"
Cohesion: 1.0
Nodes (1): github.com/google/uuid

### Community 66 - "Library: github.com/gorilla/feeds"
Cohesion: 1.0
Nodes (1): github.com/gorilla/feeds

### Community 67 - "Library: github.com/gorilla/sessions"
Cohesion: 1.0
Nodes (1): github.com/gorilla/sessions

### Community 68 - "Library: github.com/hashicorp/golang-lru/v2"
Cohesion: 1.0
Nodes (1): github.com/hashicorp/golang-lru/v2

### Community 69 - "Library: github.com/lib/pq"
Cohesion: 1.0
Nodes (1): github.com/lib/pq

### Community 70 - "Library: github.com/markbates/goth"
Cohesion: 1.0
Nodes (1): github.com/markbates/goth

### Community 71 - "Library: github.com/mattn/go-sqlite3"
Cohesion: 1.0
Nodes (1): github.com/mattn/go-sqlite3

### Community 72 - "Library: github.com/meilisearch/meilisearch-go"
Cohesion: 1.0
Nodes (1): github.com/meilisearch/meilisearch-go

### Community 73 - "Library: github.com/microcosm-cc/bluemonday"
Cohesion: 1.0
Nodes (1): github.com/microcosm-cc/bluemonday

### Community 74 - "Library: github.com/microsoft/go-mssqldb"
Cohesion: 1.0
Nodes (1): github.com/microsoft/go-mssqldb

### Community 75 - "Library: github.com/minio/minio-go/v7"
Cohesion: 1.0
Nodes (1): github.com/minio/minio-go/v7

### Community 76 - "Library: github.com/opencontainers/go-digest"
Cohesion: 1.0
Nodes (1): github.com/opencontainers/go-digest

### Community 77 - "Library: github.com/opencontainers/image-spec"
Cohesion: 1.0
Nodes (1): github.com/opencontainers/image-spec

### Community 78 - "Library: github.com/pquerna/otp"
Cohesion: 1.0
Nodes (1): github.com/pquerna/otp

### Community 79 - "Library: github.com/prometheus/client_golang"
Cohesion: 1.0
Nodes (1): github.com/prometheus/client_golang

### Community 80 - "Library: github.com/redis/go-redis/v9"
Cohesion: 1.0
Nodes (1): github.com/redis/go-redis/v9

### Community 81 - "Library: github.com/robfig/cron/v3"
Cohesion: 1.0
Nodes (1): github.com/robfig/cron/v3

### Community 82 - "Library: github.com/stretchr/testify"
Cohesion: 1.0
Nodes (1): github.com/stretchr/testify

### Community 83 - "Library: github.com/syndtr/goleveldb"
Cohesion: 1.0
Nodes (1): github.com/syndtr/goleveldb

### Community 84 - "Library: github.com/urfave/cli/v3"
Cohesion: 1.0
Nodes (1): github.com/urfave/cli/v3

### Community 85 - "Library: github.com/wneessen/go-mail"
Cohesion: 1.0
Nodes (1): github.com/wneessen/go-mail

### Community 86 - "Library: github.com/yuin/goldmark"
Cohesion: 1.0
Nodes (1): github.com/yuin/goldmark

### Community 87 - "Library: gitlab.com/gitlab-org/api/client-go/v2"
Cohesion: 1.0
Nodes (1): gitlab.com/gitlab-org/api/client-go/v2

### Community 88 - "Library: golang.org/x/crypto"
Cohesion: 1.0
Nodes (1): golang.org/x/crypto

### Community 89 - "Library: golang.org/x/oauth2"
Cohesion: 1.0
Nodes (1): golang.org/x/oauth2

### Community 90 - "Library: golang.org/x/net"
Cohesion: 1.0
Nodes (1): golang.org/x/net

### Community 91 - "Library: google.golang.org/grpc"
Cohesion: 1.0
Nodes (1): google.golang.org/grpc

### Community 92 - "Library: google.golang.org/protobuf"
Cohesion: 1.0
Nodes (1): google.golang.org/protobuf

### Community 93 - "Library: xorm.io/xorm"
Cohesion: 1.0
Nodes (1): xorm.io/xorm

### Community 94 - "Library: xorm.io/builder"
Cohesion: 1.0
Nodes (1): xorm.io/builder

### Community 95 - "Library: modernc.org/sqlite"
Cohesion: 1.0
Nodes (1): modernc.org/sqlite

### Community 96 - "Library: github.com/emersion/go-imap"
Cohesion: 1.0
Nodes (1): github.com/emersion/go-imap

### Community 97 - "Library: github.com/gliderlabs/ssh"
Cohesion: 1.0
Nodes (1): github.com/gliderlabs/ssh

### Community 98 - "Library: github.com/editorconfig/editorconfig-core-go/v2"
Cohesion: 1.0
Nodes (1): github.com/editorconfig/editorconfig-core-go/v2

### Community 99 - "Library: github.com/klauspost/compress"
Cohesion: 1.0
Nodes (1): github.com/klauspost/compress

### Community 100 - "Library: github.com/niklasfasching/go-org"
Cohesion: 1.0
Nodes (1): github.com/niklasfasching/go-org

### Community 101 - "Library: github.com/google/licenseclassifier/v2"
Cohesion: 1.0
Nodes (1): github.com/google/licenseclassifier/v2

### Community 102 - "Library: github.com/msteinert/pam/v2"
Cohesion: 1.0
Nodes (1): github.com/msteinert/pam/v2

### Community 103 - "Library: github.com/quasoft/websspi"
Cohesion: 1.0
Nodes (1): github.com/quasoft/websspi

### Community 104 - "Library: github.com/sassoftware/go-rpmutils"
Cohesion: 1.0
Nodes (1): github.com/sassoftware/go-rpmutils

### Community 105 - "Library: github.com/yohcop/openid-go"
Cohesion: 1.0
Nodes (1): github.com/yohcop/openid-go

### Community 106 - "Model Class: MarkupOption"
Cohesion: 1.0
Nodes (1): MarkupOption

### Community 107 - "Config Key: packages.LIMIT_TOTAL_OWNER_COUNT"
Cohesion: 1.0
Nodes (1): packages.LIMIT_TOTAL_OWNER_COUNT

### Community 108 - "Config Key: actions.max_rerun_attempts"
Cohesion: 1.0
Nodes (1): actions.max_rerun_attempts

### Community 109 - "Config Key: ui.REACTION_MAX_USER_NUM"
Cohesion: 1.0
Nodes (1): ui.REACTION_MAX_USER_NUM

### Community 110 - "Cache Store: Cache: branch_divergence_cache"
Cohesion: 1.0
Nodes (1): Cache: branch_divergence_cache

## Knowledge Gaps
- **1094 isolated node(s):** `POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start`, `POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop`, `DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete`, `GET /api/v1/user/stopwatches`, `GET /api/v1/repos/{owner}/{repo}/hooks/git` (+1089 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Module: cmd`** (1 nodes): `cmd`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Module: models`** (1 nodes): `models`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Module: modules`** (1 nodes): `modules`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Module: services`** (1 nodes): `services`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Module: web_src`** (1 nodes): `web_src`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: code.gitea.io/actions-proto-go`** (1 nodes): `code.gitea.io/actions-proto-go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: code.gitea.io/sdk/gitea`** (1 nodes): `code.gitea.io/sdk/gitea`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: connectrpc.com/connect`** (1 nodes): `connectrpc.com/connect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitea.com/go-chi/binding`** (1 nodes): `gitea.com/go-chi/binding`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitea.com/go-chi/cache`** (1 nodes): `gitea.com/go-chi/cache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitea.com/go-chi/captcha`** (1 nodes): `gitea.com/go-chi/captcha`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitea.com/go-chi/session`** (1 nodes): `gitea.com/go-chi/session`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitea.com/lunny/levelqueue`** (1 nodes): `gitea.com/lunny/levelqueue`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/42wim/httpsig`** (1 nodes): `github.com/42wim/httpsig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/42wim/sshsig`** (1 nodes): `github.com/42wim/sshsig`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/Azure/azure-sdk-for-go/sdk/storage/azblob`** (1 nodes): `github.com/Azure/azure-sdk-for-go/sdk/storage/azblob`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/ProtonMail/go-crypto`** (1 nodes): `github.com/ProtonMail/go-crypto`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/PuerkitoBio/goquery`** (1 nodes): `github.com/PuerkitoBio/goquery`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/alecthomas/chroma/v2`** (1 nodes): `github.com/alecthomas/chroma/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/aws/aws-sdk-go-v2/credentials`** (1 nodes): `github.com/aws/aws-sdk-go-v2/credentials`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/aws/aws-sdk-go-v2/service/codecommit`** (1 nodes): `github.com/aws/aws-sdk-go-v2/service/codecommit`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/blevesearch/bleve/v2`** (1 nodes): `github.com/blevesearch/bleve/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/caddyserver/certmagic`** (1 nodes): `github.com/caddyserver/certmagic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-chi/chi/v5`** (1 nodes): `github.com/go-chi/chi/v5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-chi/cors`** (1 nodes): `github.com/go-chi/cors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-co-op/gocron/v2`** (1 nodes): `github.com/go-co-op/gocron/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-enry/go-enry/v2`** (1 nodes): `github.com/go-enry/go-enry/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-git/go-git/v5`** (1 nodes): `github.com/go-git/go-git/v5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-ldap/ldap/v3`** (1 nodes): `github.com/go-ldap/ldap/v3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-redsync/redsync/v4`** (1 nodes): `github.com/go-redsync/redsync/v4`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-sql-driver/mysql`** (1 nodes): `github.com/go-sql-driver/mysql`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/go-webauthn/webauthn`** (1 nodes): `github.com/go-webauthn/webauthn`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/golang-jwt/jwt/v5`** (1 nodes): `github.com/golang-jwt/jwt/v5`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/google/go-github/v85`** (1 nodes): `github.com/google/go-github/v85`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/google/uuid`** (1 nodes): `github.com/google/uuid`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/gorilla/feeds`** (1 nodes): `github.com/gorilla/feeds`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/gorilla/sessions`** (1 nodes): `github.com/gorilla/sessions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/hashicorp/golang-lru/v2`** (1 nodes): `github.com/hashicorp/golang-lru/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/lib/pq`** (1 nodes): `github.com/lib/pq`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/markbates/goth`** (1 nodes): `github.com/markbates/goth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/mattn/go-sqlite3`** (1 nodes): `github.com/mattn/go-sqlite3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/meilisearch/meilisearch-go`** (1 nodes): `github.com/meilisearch/meilisearch-go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/microcosm-cc/bluemonday`** (1 nodes): `github.com/microcosm-cc/bluemonday`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/microsoft/go-mssqldb`** (1 nodes): `github.com/microsoft/go-mssqldb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/minio/minio-go/v7`** (1 nodes): `github.com/minio/minio-go/v7`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/opencontainers/go-digest`** (1 nodes): `github.com/opencontainers/go-digest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/opencontainers/image-spec`** (1 nodes): `github.com/opencontainers/image-spec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/pquerna/otp`** (1 nodes): `github.com/pquerna/otp`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/prometheus/client_golang`** (1 nodes): `github.com/prometheus/client_golang`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/redis/go-redis/v9`** (1 nodes): `github.com/redis/go-redis/v9`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/robfig/cron/v3`** (1 nodes): `github.com/robfig/cron/v3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/stretchr/testify`** (1 nodes): `github.com/stretchr/testify`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/syndtr/goleveldb`** (1 nodes): `github.com/syndtr/goleveldb`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/urfave/cli/v3`** (1 nodes): `github.com/urfave/cli/v3`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/wneessen/go-mail`** (1 nodes): `github.com/wneessen/go-mail`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/yuin/goldmark`** (1 nodes): `github.com/yuin/goldmark`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: gitlab.com/gitlab-org/api/client-go/v2`** (1 nodes): `gitlab.com/gitlab-org/api/client-go/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: golang.org/x/crypto`** (1 nodes): `golang.org/x/crypto`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: golang.org/x/oauth2`** (1 nodes): `golang.org/x/oauth2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: golang.org/x/net`** (1 nodes): `golang.org/x/net`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: google.golang.org/grpc`** (1 nodes): `google.golang.org/grpc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: google.golang.org/protobuf`** (1 nodes): `google.golang.org/protobuf`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: xorm.io/xorm`** (1 nodes): `xorm.io/xorm`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: xorm.io/builder`** (1 nodes): `xorm.io/builder`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: modernc.org/sqlite`** (1 nodes): `modernc.org/sqlite`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/emersion/go-imap`** (1 nodes): `github.com/emersion/go-imap`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/gliderlabs/ssh`** (1 nodes): `github.com/gliderlabs/ssh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/editorconfig/editorconfig-core-go/v2`** (1 nodes): `github.com/editorconfig/editorconfig-core-go/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/klauspost/compress`** (1 nodes): `github.com/klauspost/compress`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/niklasfasching/go-org`** (1 nodes): `github.com/niklasfasching/go-org`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/google/licenseclassifier/v2`** (1 nodes): `github.com/google/licenseclassifier/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/msteinert/pam/v2`** (1 nodes): `github.com/msteinert/pam/v2`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/quasoft/websspi`** (1 nodes): `github.com/quasoft/websspi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/sassoftware/go-rpmutils`** (1 nodes): `github.com/sassoftware/go-rpmutils`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Library: github.com/yohcop/openid-go`** (1 nodes): `github.com/yohcop/openid-go`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Model Class: MarkupOption`** (1 nodes): `MarkupOption`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Config Key: packages.LIMIT_TOTAL_OWNER_COUNT`** (1 nodes): `packages.LIMIT_TOTAL_OWNER_COUNT`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Config Key: actions.max_rerun_attempts`** (1 nodes): `actions.max_rerun_attempts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Config Key: ui.REACTION_MAX_USER_NUM`** (1 nodes): `ui.REACTION_MAX_USER_NUM`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Cache Store: Cache: branch_divergence_cache`** (1 nodes): `Cache: branch_divergence_cache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M` connect `Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M` to `Controller: user_model.User`, `Endpoint: routers`, `Controller: convert`, `Controller: IsNewPinAllowed compares current pin count against MaxPinned setting`, `Controller: POST /api/v1/orgs`, `Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels`, `Controller: Pin order is assigned as max existing order + 1 when pinning`, `Controller: webhook_service.ToHook`, `Controller: reqOrgOwnership`, `Controller: Unarchiving a repo re-detects action schedules`, `Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge`, `Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections`, `Controller: Pinned issues are separated by type (issues vs pull requests)`, `Controller: Issue templates are parsed from multiple candidate directories in priority order`, `Controller: issues_model.Issue`, `Controller: GET /api/v1/packages/{owner}`, `Controller: POST /api/v1/repos/{owner}/{repo}/avatar`, `Controller: POST /api/v1/user/gpg_keys`, `Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors`, `Controller: Org repo creation requires user to have create permission in org`, `Error Scenario: POST /api/v1/admin/users`, `Controller: GET /api/v1/repos/{owner}/{repo}/commits`, `Controller: GET /api/v1/repos/search`, `Controller: PUT /api/v1/user/starred/{owner}/{repo}`, `Controller: POST /api/v1/markdown`, `Controller: POST /api/v1/admin/unadopted/{owner}/{repo}`?**
  _High betweenness centrality (0.172) - this node is a cross-community bridge._
- **Why does `Pinned issues are separated by type (issues vs pull requests)` connect `Controller: Pinned issues are separated by type (issues vs pull requests)` to `Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M`, `Controller: user_model.User`, `Controller: convert`, `Controller: IsNewPinAllowed compares current pin count against MaxPinned setting`, `Controller: POST /api/v1/orgs`, `Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels`, `Controller: Pin order is assigned as max existing order + 1 when pinning`, `Controller: webhook_service.ToHook`, `Controller: reqOrgOwnership`, `Controller: Unarchiving a repo re-detects action schedules`, `Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge`, `Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections`, `Controller: Issue templates are parsed from multiple candidate directories in priority order`, `Controller: POST /api/v1/user/keys`, `Controller: issues_model.Issue`, `Controller: GET /api/v1/packages/{owner}`, `Controller: POST /api/v1/repos/{owner}/{repo}/avatar`, `Controller: POST /api/v1/user/gpg_keys`, `Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors`, `Controller: Org repo creation requires user to have create permission in org`, `Controller: GET /api/v1/repos/search`, `Controller: PUT /api/v1/user/starred/{owner}/{repo}`, `Controller: GET /api/v1/gitignore/templates/{name}`, `Controller: POST /api/v1/markdown`, `Controller: POST /api/v1/admin/unadopted/{owner}/{repo}`, `Controller: POST /api/v1/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Why does `Pin order is assigned as max existing order + 1 when pinning` connect `Controller: Pin order is assigned as max existing order + 1 when pinning` to `Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M`, `Controller: user_model.User`, `Controller: convert`, `Controller: IsNewPinAllowed compares current pin count against MaxPinned setting`, `Controller: POST /api/v1/orgs`, `Controller: POST /api/v1/repos/{owner}/{repo}/issues/{index}/labels`, `Controller: webhook_service.ToHook`, `Controller: reqOrgOwnership`, `Controller: Unarchiving a repo re-detects action schedules`, `Controller: POST /api/v1/repos/{owner}/{repo}/pulls/{index}/merge`, `Controller: POST /api/v1/repos/{owner}/{repo}/branch_protections`, `Controller: Pinned issues are separated by type (issues vs pull requests)`, `Controller: Issue templates are parsed from multiple candidate directories in priority order`, `Controller: POST /api/v1/user/keys`, `Controller: issues_model.Issue`, `Controller: GET /api/v1/packages/{owner}`, `Controller: POST /api/v1/repos/{owner}/{repo}/avatar`, `Controller: POST /api/v1/user/gpg_keys`, `Controller: POST /api/v1/repos/{owner}/{repo}/push_mirrors`, `Error Scenario: POST /api/v1/admin/users`, `Controller: GET /api/v1/repos/{owner}/{repo}/commits`, `Controller: POST /api/v1/markdown`, `Controller: POST /api/v1/admin/unadopted/{owner}/{repo}`, `Controller: GET /api/v1/repos/{owner}/{repo}/git/refs/{ref}`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **What connects `POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/start`, `POST /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/stop`, `DELETE /api/v1/repos/{owner}/{repo}/issues/{index}/stopwatch/delete` to the rest of the system?**
  _1094 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Controller: Maximum pin limit check - cannot pin more issues than setting.Repository.Issue.M` be split into smaller, more focused modules?**
  _Cohesion score 0.02 - nodes in this community are weakly interconnected._
- **Should `Controller: user_model.User` be split into smaller, more focused modules?**
  _Cohesion score 0.02 - nodes in this community are weakly interconnected._
- **Should `Endpoint: routers` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._