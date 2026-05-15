One or more mcp server did not load correctly. See $TMPDIR/kiro-log/kiro-chat.log for more details.
------
All tools are now trusted (!). Kiro will execute tools without asking for confirmation.
Agents can sometimes do unexpected things so understand the risks.

Learn more at https://kiro.dev/docs/cli/chat/security/#using-tools-trust-all-safely


📷 Checkpoints are enabled! (took 7.42s)


I'll share my reasoning process (using tool: thinking): The user wants me to list all API endpoints related to repository management from the provided wiki context. Let me extract what's available from the context provided. I should only use the information given - no tool calls.

From the context, I have details on these endpoints:
1. ep-017: GET /api/v1/settings/repository
2. ep-108: POST /api/v1/admin/unadopted/{owner}/{repo}
3. ep-109: DELETE /api/v1/admin/unadopted/{owner}/{repo}
4. ep-249: POST /api/v1/repos/{owner}/{repo}/diffpatch
5. ep-005: GET /api/v1/repos/{owner}/{repo}/signing-key.gpg
6. ep-006: GET /api/v1/signing-key.pub
7. ep-007: GET /api/v1/repos/{owner}/{repo}/signing-key.pub

The project overview mentions 475 endpoints total, but I only have detailed wiki pages for these 7. I should present what's available and note the limitation.

 - Completed in 0.149s

> Based on the provided wiki context, here are the repository-related API endpoints with full details:

## Repository Management Endpoints

| # | Method | Path | Handler | Auth/Permissions |
|---|--------|------|---------|-----------------|
| 1 | GET | /api/v1/settings/repository | settings.GetGeneralRepoSettings | None |
| 2 | POST | /api/v1/admin/unadopted/{owner}/{repo} | admin.AdoptRepository → repo_service.AdoptRepository | Bearer token (AccessTokenScopeCategoryAdmin); must be site admin |
| 3 | DELETE | /api/v1/admin/unadopted/{owner}/{repo} | admin.DeleteUnadoptedRepository → repo_service.DeleteUnadoptedRepository | Bearer token (AccessTokenScopeCategoryAdmin); must be site admin |
| 4 | POST | /api/v1/repos/{owner}/{repo}/diffpatch | repo.ApplyDiffPatch → files.ApplyDiffPatch | Bearer token; write permission to target branch (or site admin) |
| 5 | GET | /api/v1/repos/{owner}/{repo}/signing-key.gpg | misc.SigningKeyGPG → asymkey_service.PublicSigningKey | Bearer token |
| 6 | GET | /api/v1/signing-key.pub | misc.SigningKeySSH → asymkey_service.PublicSigningKey | None |
| 7 | GET | /api/v1/repos/{owner}/{repo}/signing-key.pub | misc.SigningKeySSH → asymkey_service.PublicSigningKey | Bearer token |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


### Detailed Breakdown

1. GET /api/v1/settings/repository (ep-017)
- **Handler:** settings.GetGeneralRepoSettings (routers module)
- **Auth:** None required
- **Purpose:** Returns global repository feature flags (mirrors, HTTP git, migrations, stars, time tracking, LFS disabled status)
- **Risk:** Low — pure in-memory config read

2. POST /api/v1/admin/unadopted/{owner}/{repo} (ep-108)
- **Handler:** admin.AdoptRepository → repo_service.AdoptRepository
- **Auth:** Bearer token with AccessTokenScopeCategoryAdmin; reqSiteAdmin middleware enforces site admin
- **Purpose:** Adopts unadopted files on disk as a tracked repository (creates DB record, syncs branches/releases, creates hooks)
- **DB operations:** SELECT on user, SELECT + INSERT on repository, INSERT on branch, INSERT on release
- **Risk:** Medium — non-atomic (DB record created first, git ops follow; deferred cleanup on failure)

3. DELETE /api/v1/admin/unadopted/{owner}/{repo} (ep-109)
- **Handler:** admin.DeleteUnadoptedRepository → repo_service.DeleteUnadoptedRepository
- **Auth:** Bearer token with AccessTokenScopeCategoryAdmin; reqSiteAdmin middleware enforces site admin
- **Purpose:** Deletes unadopted repository files from filesystem (repo must NOT exist in DB but MUST exist on disk)
- **DB operations:** SELECT on user, SELECT on repository (existence check)

4. POST /api/v1/repos/{owner}/{repo}/diffpatch (ep-249)
- **Handler:** repo.ApplyDiffPatch → repo.ReqChangeRepoFileOptionsAndCheck → files.ApplyDiffPatch
- **Auth:** Bearer token; user must have write permission to target branch OR be site admin; protected branch rules apply
- **Purpose:** Applies a diff patch creating a new commit (clone → apply → commit → push)
- **DB operations:** SELECT on branch (old/new branch check), SELECT on protected_branch
- **Risk:** Medium — synchronous blocking, no timeout on git apply, temp repo disk usage

5. GET /api/v1/repos/{owner}/{repo}/signing-key.gpg (ep-005)
- **Handler:** misc.SigningKeyGPG → asymkey_service.PublicSigningKey
- **Auth:** Bearer token
- **Purpose:** Returns the GPG signing key for a repository (spawns gpg --export -a <keyID>)
- **External call:** GPG binary via process.GetManager().ExecDir
- **Risk:** Medium — no timeout on gpg execution

6. GET /api/v1/signing-key.pub (ep-006)
- **Handler:** misc.SigningKeySSH → asymkey_service.PublicSigningKey
- **Auth:** None required
- **Purpose:** Returns the SSH public key of the default signing key (reads file from disk)
- **Risk:** Low — local file read

7. GET /api/v1/repos/{owner}/{repo}/signing-key.pub (ep-007)
- **Handler:** misc.SigningKeySSH → asymkey_service.PublicSigningKey
- **Auth:** Bearer token
- **Purpose:** Returns the SSH signing key for a specific repository
- **Risk:** Low — local file read

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


### Authentication Summary

| Level | Endpoints |
|-------|-----------|
| No auth | ep-017 (settings/repository), ep-006 (signing-key.pub global) |
| Bearer token | ep-005, ep-007 (signing keys per-repo), ep-249 (diffpatch) |
| Site admin | ep-108, ep-109 (unadopted repo adopt/delete) |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


│ **Note:** The project has 475 total endpoints. The wiki context provided covers only 7 of them. The full repository management surface (CRUD repos, forks, transfers, collaborators, branches, tags, releases, etc.) is documented in additional endpoint files not included here.

 ▸ Credits: 0.35 • Time: 29s

