# Configuration

**109 properties**

### API.DefaultPagingNum

- **Type:** Integer · **Default:** `30`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-084](../endpoints/ep-084.md), [ep-087](../endpoints/ep-087.md), [ep-123](../endpoints/ep-123.md), [ep-127](../endpoints/ep-127.md), [ep-135](../endpoints/ep-135.md), [ep-136](../endpoints/ep-136.md), [ep-137](../endpoints/ep-137.md), [ep-138](../endpoints/ep-138.md), [ep-139](../endpoints/ep-139.md), [ep-140](../endpoints/ep-140.md), [ep-141](../endpoints/ep-141.md), [ep-142](../endpoints/ep-142.md), [ep-147](../endpoints/ep-147.md), [ep-221](../endpoints/ep-221.md), [ep-222](../endpoints/ep-222.md)

### API.MaxResponseItems

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-084](../endpoints/ep-084.md), [ep-087](../endpoints/ep-087.md), [ep-123](../endpoints/ep-123.md), [ep-127](../endpoints/ep-127.md), [ep-135](../endpoints/ep-135.md), [ep-136](../endpoints/ep-136.md), [ep-137](../endpoints/ep-137.md), [ep-138](../endpoints/ep-138.md), [ep-139](../endpoints/ep-139.md), [ep-140](../endpoints/ep-140.md), [ep-141](../endpoints/ep-141.md), [ep-142](../endpoints/ep-142.md), [ep-147](../endpoints/ep-147.md)

### APP_VER

- **Type:** String · **Default:** `dev`
- **Source:** `modules/setting/setting.go`
- **Affects:** [ep-001](../endpoints/ep-001.md)

### AVATAR_MAX_HEIGHT

- **Type:** Integer · **Default:** `4096`
- **Source:** `app.ini [picture]`
- **Affects:** [ep-037](../endpoints/ep-037.md)

### AVATAR_MAX_ORIGIN_SIZE

- **Type:** Integer · **Default:** `262144`
- **Source:** `app.ini [picture]`
- **Affects:** [ep-037](../endpoints/ep-037.md)

### AVATAR_MAX_WIDTH

- **Type:** Integer · **Default:** `4096`
- **Source:** `app.ini [picture]`
- **Affects:** [ep-037](../endpoints/ep-037.md)

### AVATAR_RENDERED_SIZE_FACTOR

- **Type:** Integer · **Default:** `2`
- **Source:** `app.ini [picture]`
- **Affects:** [ep-037](../endpoints/ep-037.md)

### AppURL

- **Type:** String · **Default:** `http://localhost:3000/`
- **Source:** `modules/setting/server.go`
- **Affects:** [ep-091](../endpoints/ep-091.md), [ep-094](../endpoints/ep-094.md)

### Avatar.MaxHeight

- **Type:** Integer · **Default:** `4096`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-128](../endpoints/ep-128.md)

### Avatar.MaxOriginSize

- **Type:** Integer · **Default:** `262144`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-128](../endpoints/ep-128.md)

### Avatar.MaxWidth

- **Type:** Integer · **Default:** `4096`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-128](../endpoints/ep-128.md)

### MIN_PASSWORD_LENGTH

- **Type:** Integer · **Default:** `6`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-099](../endpoints/ep-099.md)

### MinPasswordLength

- **Type:** Integer · **Default:** `6`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-098](../endpoints/ep-098.md)

### OAuth2.CustomSchemes

- **Type:** []string · **Default:** `[]`
- **Source:** `modules/setting/oauth2.go`
- **Affects:** [ep-171](../endpoints/ep-171.md)

### OAuth2.DefaultApplications

- **Type:** []string · **Default:** `["git-credential-oauth", "git-credential-manager", "tea"]`
- **Source:** `modules/setting/oauth2.go`
- **Affects:** [ep-169](../endpoints/ep-169.md), [ep-171](../endpoints/ep-171.md)

### PASSWORD_CHECK_PWN

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-099](../endpoints/ep-099.md)

### PasswordCheckPwn

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-098](../endpoints/ep-098.md)

### SECRET_KEY

- **Type:** String · **Default:** `auto-generated`
- **Source:** `app.ini [security]`
- **Affects:** [ep-040](../endpoints/ep-040.md), [ep-130](../endpoints/ep-130.md)

### SECRET_KEY (general token signing)

- **Type:** String · **Default:** `generated`
- **Source:** `app.ini`
- **Affects:** [ep-298](../endpoints/ep-298.md)

### SSH.MinimumKeySizeCheck

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/ssh.go`
- **Affects:** [ep-342](../endpoints/ep-342.md)

### SSH.StartBuiltinServer

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/ssh.go`
- **Affects:** [ep-343](../endpoints/ep-343.md)

### SecretKey

- **Type:** String · **Default:** `auto-generated`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-147](../endpoints/ep-147.md), [ep-148](../endpoints/ep-148.md), [ep-149](../endpoints/ep-149.md)

### Service.DefaultOrgMemberVisible

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-096](../endpoints/ep-096.md)

### USER_DELETE_WITH_COMMENTS_MAX_TIME

- **Type:** Duration · **Default:** `0`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-100](../endpoints/ep-100.md)

### actions.MAX_RERUN_ATTEMPTS

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/actions.go`
- **Affects:** [ep-287](../endpoints/ep-287.md), [ep-288](../endpoints/ep-288.md), [ep-289](../endpoints/ep-289.md)

### actions.artifact_storage.SERVE_DIRECT

- **Type:** Boolean · **Default:** `false`
- **Source:** `app.ini`
- **Affects:** [ep-298](../endpoints/ep-298.md)

### actions.artifact_storage.STORAGE_TYPE

- **Type:** String · **Default:** `local`
- **Source:** `app.ini`
- **Affects:** [ep-294](../endpoints/ep-294.md), [ep-298](../endpoints/ep-298.md)

### actions.max_rerun_attempts

- **Type:** int64 · **Default:** `10`
- **Source:** `modules/setting/actions.go`
- **Affects:** 

### actions.workflow_dirs

- **Type:** []string · **Default:** `[".gitea/workflows", ".github/workflows"]`
- **Source:** `modules/setting/actions.go`
- **Affects:** [ep-280](../endpoints/ep-280.md), [ep-281](../endpoints/ep-281.md), [ep-283](../endpoints/ep-283.md)

### admin.EXTERNAL_USER_DISABLE_FEATURES

- **Type:** []string · **Default:** `empty`
- **Source:** `modules/setting/admin.go`
- **Affects:** [ep-160](../endpoints/ep-160.md), [ep-161](../endpoints/ep-161.md)

### admin.USER_DISABLED_FEATURES

- **Type:** []string · **Default:** `empty`
- **Source:** `modules/setting/admin.go`
- **Affects:** [ep-160](../endpoints/ep-160.md), [ep-161](../endpoints/ep-161.md)

### admin.USER_DISABLED_FEATURES / admin.EXTERNAL_USER_DISABLE_FEATURES

- **Type:** container.Set[string] · **Default:** `empty set`
- **Source:** `modules/setting/admin.go`
- **Affects:** [ep-188](../endpoints/ep-188.md), [ep-189](../endpoints/ep-189.md)

### api.DEFAULT_GIT_TREES_PER_PAGE

- **Type:** Integer · **Default:** `1000`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-016](../endpoints/ep-016.md)

### api.DEFAULT_MAX_BLOB_SIZE

- **Type:** Integer (int64) · **Default:** `10485760 (10MB)`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-016](../endpoints/ep-016.md)

### api.DEFAULT_MAX_RESPONSE_SIZE

- **Type:** Integer (int64) · **Default:** `104857600 (100MB)`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-016](../endpoints/ep-016.md)

### api.DEFAULT_PAGING_NUM

- **Type:** Integer · **Default:** `30`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-016](../endpoints/ep-016.md), [ep-019](../endpoints/ep-019.md), [ep-022](../endpoints/ep-022.md), [ep-208](../endpoints/ep-208.md), [ep-211](../endpoints/ep-211.md), [ep-242](../endpoints/ep-242.md), [ep-264](../endpoints/ep-264.md)

### api.DefaultGitTreesPerPage

- **Type:** Integer · **Default:** `1000`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-246](../endpoints/ep-246.md)

### api.DefaultPagingNum

- **Type:** Integer · **Default:** `30`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-250](../endpoints/ep-250.md)

### api.MAX_RESPONSE_ITEMS

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-016](../endpoints/ep-016.md), [ep-019](../endpoints/ep-019.md), [ep-022](../endpoints/ep-022.md), [ep-242](../endpoints/ep-242.md)

### api.MaxResponseItems

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-250](../endpoints/ep-250.md)

### api.SwaggerURL

- **Type:** String · **Default:** ``
- **Source:** `modules/setting/api.go`
- **Affects:** [ep-215](../endpoints/ep-215.md)

### api.default_paging_num

- **Type:** Integer · **Default:** `30`
- **Source:** `custom/conf/app.ini [api]`
- **Affects:** [ep-026](../endpoints/ep-026.md), [ep-027](../endpoints/ep-027.md)

### api.max_response_items

- **Type:** Integer · **Default:** `50`
- **Source:** `custom/conf/app.ini [api]`
- **Affects:** [ep-026](../endpoints/ep-026.md), [ep-027](../endpoints/ep-027.md)

### attachment.ALLOWED_TYPES

- **Type:** String · **Default:** `.avif,.cpuprofile,.csv,.dmp,.docx,.fodg,.fodp,.fods,.fodt,.gif,.gz,.jpeg,.jpg,.json,.jsonc,.log,.md,.mov,.mp4,.odf,.odg,.odp,.ods,.odt,.patch,.pdf,.png,.pptx,.svg,.tgz,.txt,.webm,.webp,.xls,.xlsx,.zip`
- **Source:** `modules/setting/attachment.go`
- **Affects:** [ep-259](../endpoints/ep-259.md), [ep-260](../endpoints/ep-260.md)

### attachment.ENABLED

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/attachment.go`
- **Affects:** [ep-018](../endpoints/ep-018.md), [ep-259](../endpoints/ep-259.md), [ep-260](../endpoints/ep-260.md), [ep-261](../endpoints/ep-261.md), [ep-354](../endpoints/ep-354.md)

### attachment.MAX_SIZE

- **Type:** Integer (int64) · **Default:** `100`
- **Source:** `modules/setting/attachment.go`
- **Affects:** [ep-018](../endpoints/ep-018.md), [ep-259](../endpoints/ep-259.md)

### avatar.MAX_HEIGHT

- **Type:** Integer · **Default:** `4096`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-262](../endpoints/ep-262.md)

### avatar.MAX_ORIGIN_SIZE

- **Type:** Integer · **Default:** `262144`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-262](../endpoints/ep-262.md)

### avatar.MAX_WIDTH

- **Type:** Integer · **Default:** `4096`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-262](../endpoints/ep-262.md)

### avatar.RENDERED_SIZE_FACTOR

- **Type:** Integer · **Default:** `2`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-262](../endpoints/ep-262.md)

### avatar.STORAGE_TYPE

- **Type:** String · **Default:** `local`
- **Source:** `modules/setting/picture.go`
- **Affects:** [ep-129](../endpoints/ep-129.md)

### database.iterate_buffer_size

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/database.go`
- **Affects:** [ep-107](../endpoints/ep-107.md)

### git.CommitsRangeSize

- **Type:** Integer · **Default:** `50`
- **Source:** `modules/setting/git.go`
- **Affects:** [ep-215](../endpoints/ep-215.md)

### git.HOME_PATH

- **Type:** String · **Default:** ``
- **Source:** `modules/setting/git.go`
- **Affects:** [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md)

### git.MAX_GIT_DIFF_LINES

- **Type:** Integer · **Default:** `1000`
- **Source:** `modules/setting/git.go`
- **Affects:** [ep-233](../endpoints/ep-233.md)

### git.MAX_GIT_DIFF_LINE_CHARACTERS

- **Type:** Integer · **Default:** `5000`
- **Source:** `modules/setting/git.go`
- **Affects:** [ep-233](../endpoints/ep-233.md)

### git.TIMEOUT.MIRROR

- **Type:** Integer (seconds) · **Default:** `300`
- **Source:** `modules/setting/git.go`
- **Affects:** [ep-235](../endpoints/ep-235.md)

### lfs.START_SERVER

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/lfs.go`
- **Affects:** [ep-235](../endpoints/ep-235.md)

### mirror.ENABLED

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/mirror.go`
- **Affects:** [ep-017](../endpoints/ep-017.md), [ep-234](../endpoints/ep-234.md), [ep-235](../endpoints/ep-235.md), [ep-236](../endpoints/ep-236.md), [ep-237](../endpoints/ep-237.md), [ep-238](../endpoints/ep-238.md), [ep-239](../endpoints/ep-239.md)

### mirror.MIN_INTERVAL

- **Type:** Duration · **Default:** `10m`
- **Source:** `modules/setting/mirror.go`
- **Affects:** [ep-238](../endpoints/ep-238.md)

### mirror.MinInterval

- **Type:** Duration · **Default:** `10m0s`
- **Source:** `modules/setting/mirror.go`
- **Affects:** [ep-369](../endpoints/ep-369.md)

### packages.ENABLED

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/packages.go`
- **Affects:** [ep-202](../endpoints/ep-202.md), [ep-203](../endpoints/ep-203.md), [ep-204](../endpoints/ep-204.md), [ep-205](../endpoints/ep-205.md), [ep-206](../endpoints/ep-206.md), [ep-207](../endpoints/ep-207.md)

### packages.LIMIT_TOTAL_OWNER_COUNT

- **Type:** Integer · **Default:** `-1 (no limit)`
- **Source:** `modules/setting/packages.go`
- **Affects:** 

### packages.limit_total_owner_count

- **Type:** Integer · **Default:** `-1`
- **Source:** `modules/setting/packages.go`
- **Affects:** [ep-201](../endpoints/ep-201.md)

### repository.DISABLE_HTTP_GIT

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-017](../endpoints/ep-017.md)

### repository.FORCE_PRIVATE

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-363](../endpoints/ep-363.md), [ep-364](../endpoints/ep-364.md), [ep-365](../endpoints/ep-365.md), [ep-366](../endpoints/ep-366.md)

### repository.ForcePrivate

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-369](../endpoints/ep-369.md)

### repository.PREFERRED_LICENSES

- **Type:** []String · **Default:** `[]`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-002](../endpoints/ep-002.md)

### repository.PULL_REQUEST_DEFAULT_MERGE_STYLE

- **Type:** String · **Default:** `merge`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-229](../endpoints/ep-229.md)

### repository.SIGNING_FORMAT

- **Type:** String · **Default:** `openpgp`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md), [ep-006](../endpoints/ep-006.md), [ep-007](../endpoints/ep-007.md)

### repository.SIGNING_KEY

- **Type:** String · **Default:** `default`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-004](../endpoints/ep-004.md), [ep-005](../endpoints/ep-005.md), [ep-006](../endpoints/ep-006.md), [ep-007](../endpoints/ep-007.md)

### repository.force_private

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-112](../endpoints/ep-112.md)

### repository.issue.MAX_PINNED

- **Type:** Integer · **Default:** `3`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-376](../endpoints/ep-376.md), [ep-381](../endpoints/ep-381.md)

### repository.issue.MaxPinned

- **Type:** Integer · **Default:** `3`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-371](../endpoints/ep-371.md)

### repository.release.ALLOWED_TYPES

- **Type:** String · **Default:** ``
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-354](../endpoints/ep-354.md), [ep-355](../endpoints/ep-355.md)

### repository.release.FILE_MAX_SIZE

- **Type:** Integer (MB) · **Default:** `2048`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-354](../endpoints/ep-354.md)

### repository.root_path

- **Type:** String · **Default:** `data/gitea-repositories`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-107](../endpoints/ep-107.md), [ep-108](../endpoints/ep-108.md), [ep-109](../endpoints/ep-109.md)

### server.APP_URL

- **Type:** String · **Default:** `http://localhost:3000/`
- **Source:** `modules/setting/server.go`
- **Affects:** [ep-008](../endpoints/ep-008.md), [ep-352](../endpoints/ep-352.md), [ep-353](../endpoints/ep-353.md), [ep-354](../endpoints/ep-354.md), [ep-355](../endpoints/ep-355.md)

### service.ALLOW_CROSS_REPOSITORY_DEPENDENCIES

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-209](../endpoints/ep-209.md), [ep-210](../endpoints/ep-210.md), [ep-212](../endpoints/ep-212.md), [ep-213](../endpoints/ep-213.md)

### service.AUTO_WATCH_NEW_REPOS

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-066](../endpoints/ep-066.md), [ep-331](../endpoints/ep-331.md)

### service.AutoWatchNewRepos

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-062](../endpoints/ep-062.md)

### service.DEFAULT_ENABLE_DEPENDENCIES

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-208](../endpoints/ep-208.md), [ep-209](../endpoints/ep-209.md), [ep-210](../endpoints/ep-210.md), [ep-212](../endpoints/ep-212.md), [ep-213](../endpoints/ep-213.md)

### service.REQUIRE_SIGNIN_VIEW

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-202](../endpoints/ep-202.md), [ep-203](../endpoints/ep-203.md), [ep-204](../endpoints/ep-204.md), [ep-205](../endpoints/ep-205.md), [ep-206](../endpoints/ep-206.md), [ep-207](../endpoints/ep-207.md)

### service.RegisterEmailConfirm

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-181](../endpoints/ep-181.md)

### service.auto_watch_on_changes

- **Type:** Boolean · **Default:** `true`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-197](../endpoints/ep-197.md)

### service.default_org_member_visible

- **Type:** Boolean · **Default:** `false`
- **Source:** `custom/conf/app.ini [service]`
- **Affects:** [ep-026](../endpoints/ep-026.md), [ep-027](../endpoints/ep-027.md)

### service.require_signin_view_strict

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/service.go`
- **Affects:** [ep-199](../endpoints/ep-199.md), [ep-200](../endpoints/ep-200.md)

### setting.API.DefaultPagingNum

- **Type:** Integer · **Default:** `20`
- **Source:** `custom/conf/app.ini [api]`
- **Affects:** [ep-029](../endpoints/ep-029.md), [ep-043](../endpoints/ep-043.md), [ep-048](../endpoints/ep-048.md), [ep-070](../endpoints/ep-070.md), [ep-071](../endpoints/ep-071.md), [ep-077](../endpoints/ep-077.md), [ep-082](../endpoints/ep-082.md), [ep-190](../endpoints/ep-190.md), [ep-194](../endpoints/ep-194.md), [ep-195](../endpoints/ep-195.md)

### setting.API.MaxResponseItems

- **Type:** Integer · **Default:** `50`
- **Source:** `custom/conf/app.ini [api]`
- **Affects:** [ep-029](../endpoints/ep-029.md), [ep-043](../endpoints/ep-043.md), [ep-048](../endpoints/ep-048.md), [ep-070](../endpoints/ep-070.md), [ep-071](../endpoints/ep-071.md), [ep-077](../endpoints/ep-077.md), [ep-082](../endpoints/ep-082.md), [ep-190](../endpoints/ep-190.md), [ep-194](../endpoints/ep-194.md), [ep-195](../endpoints/ep-195.md)

### setting.Admin.DisableRegularOrgCreation

- **Type:** Boolean · **Default:** `false`
- **Source:** `custom/conf/app.ini [admin]`
- **Affects:** [ep-030](../endpoints/ep-030.md)

### setting.AppSubURL

- **Type:** String · **Default:** ``
- **Source:** `modules/setting/server.go`
- **Affects:** [ep-009](../endpoints/ep-009.md)

### setting.AppURL

- **Type:** String · **Default:** `protocol://domain:port/`
- **Source:** `modules/setting/server.go`
- **Affects:** [ep-013](../endpoints/ep-013.md), [ep-014](../endpoints/ep-014.md)

### setting.CustomPath

- **Type:** String · **Default:** `custom`
- **Source:** `modules/setting/setting.go`
- **Affects:** [ep-012](../endpoints/ep-012.md), [ep-014](../endpoints/ep-014.md)

### setting.DisableWebhooks

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/webhook.go`
- **Affects:** [ep-150](../endpoints/ep-150.md), [ep-151](../endpoints/ep-151.md)

### setting.IsInTesting

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/testenv.go`
- **Affects:** [ep-223](../endpoints/ep-223.md), [ep-224](../endpoints/ep-224.md)

### setting.OAuth2.CustomSchemes

- **Type:** []string · **Default:** `[]`
- **Source:** `custom/conf/app.ini [oauth2]`
- **Affects:** [ep-167](../endpoints/ep-167.md)

### setting.PanicInDevOrTesting

- **Type:** function · **Default:** `panics in dev/test mode only`
- **Source:** `modules/setting/setting.go`
- **Affects:** [ep-050](../endpoints/ep-050.md), [ep-051](../endpoints/ep-051.md), [ep-052](../endpoints/ep-052.md), [ep-053](../endpoints/ep-053.md), [ep-114](../endpoints/ep-114.md), [ep-115](../endpoints/ep-115.md), [ep-116](../endpoints/ep-116.md), [ep-117](../endpoints/ep-117.md), [ep-176](../endpoints/ep-176.md), [ep-177](../endpoints/ep-177.md), [ep-178](../endpoints/ep-178.md), [ep-179](../endpoints/ep-179.md)

### setting.Repository.DisableStars

- **Type:** Boolean · **Default:** `false`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-152](../endpoints/ep-152.md), [ep-153](../endpoints/ep-153.md), [ep-154](../endpoints/ep-154.md), [ep-155](../endpoints/ep-155.md)

### setting.Repository.PreferredLicenses

- **Type:** []string · **Default:** `["Apache License 2.0", "MIT License"]`
- **Source:** `modules/setting/repository.go`
- **Affects:** [ep-013](../endpoints/ep-013.md)

### setting.SecretKey

- **Type:** String · **Default:** `auto-generated`
- **Source:** `modules/setting/security.go`
- **Affects:** [ep-077](../endpoints/ep-077.md), [ep-078](../endpoints/ep-078.md), [ep-079](../endpoints/ep-079.md), [ep-080](../endpoints/ep-080.md)

### setting.Service.DefaultOrgMemberVisible

- **Type:** Boolean · **Default:** `false`
- **Source:** `custom/conf/app.ini [service]`
- **Affects:** [ep-030](../endpoints/ep-030.md)

### setting.SuccessfulTokensCacheSize

- **Type:** int · **Default:** `20`
- **Source:** `custom/conf/app.ini`
- **Affects:** [ep-164](../endpoints/ep-164.md), [ep-165](../endpoints/ep-165.md), [ep-166](../endpoints/ep-166.md)

### setting.UserFeatureManageGPGKeys

- **Type:** string constant · **Default:** `manage_gpg_keys`
- **Source:** `modules/setting/admin.go`
- **Affects:** [ep-188](../endpoints/ep-188.md), [ep-189](../endpoints/ep-189.md)

### ssh.MINIMUM_KEY_SIZE_CHECK

- **Type:** bool · **Default:** `true`
- **Source:** `modules/setting/ssh.go`
- **Affects:** [ep-160](../endpoints/ep-160.md)

### ssh.START_BUILTIN_SERVER

- **Type:** bool · **Default:** `false`
- **Source:** `modules/setting/ssh.go`
- **Affects:** [ep-161](../endpoints/ep-161.md)

### ui.CUSTOM_EMOJIS

- **Type:** []String · **Default:** `[git, gitea, codeberg, gitlab, github, gogs]`
- **Source:** `modules/setting/ui.go`
- **Affects:** [ep-015](../endpoints/ep-015.md)

### ui.DEFAULT_THEME

- **Type:** String · **Default:** `gitea-auto`
- **Source:** `modules/setting/ui.go`
- **Affects:** [ep-015](../endpoints/ep-015.md)

### ui.REACTIONS

- **Type:** []String · **Default:** `[+1, -1, laugh, hooray, confused, heart, rocket, eyes]`
- **Source:** `modules/setting/ui.go`
- **Affects:** [ep-015](../endpoints/ep-015.md), [ep-300](../endpoints/ep-300.md), [ep-301](../endpoints/ep-301.md), [ep-303](../endpoints/ep-303.md), [ep-304](../endpoints/ep-304.md)

### ui.REACTION_MAX_USER_NUM

- **Type:** int · **Default:** `10`
- **Source:** `modules/setting/ui.go`
- **Affects:** 
