# Phase 2 Session Report

**Session:** 38
**Endpoints Analyzed:** ep-254 to ep-261
**Total Endpoints:** 8
**Traffic Data:** not available

## Summary
- Endpoints analyzed: 8
- Business rules extracted: 12
- Database operations documented: 6 tables
- External integrations used: 1 (Object Storage)
- Performance issues found: 4
- Average workflow depth: 4 steps

## Endpoints Analyzed

| Endpoint ID | Method | Path | Workflow Depth | Files Read | Perf Issues |
|-------------|--------|------|----------------|------------|-------------|
| ep-254 | GET | /repos/{owner}/{repo}/collaborators/{collaborator}/permission | 4 steps | 4 files | 1 |
| ep-255 | GET | /repos/{owner}/{repo}/reviewers | 4 steps | 3 files | 1 |
| ep-256 | GET | /repos/{owner}/{repo}/assignees | 3 steps | 2 files | 0 |
| ep-257 | GET | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 5 steps | 3 files | 0 |
| ep-258 | GET | /repos/{owner}/{repo}/issues/{index}/assets | 4 steps | 4 files | 1 |
| ep-259 | POST | /repos/{owner}/{repo}/issues/{index}/assets | 5 steps | 5 files | 1 |
| ep-260 | PATCH | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 3 steps | 4 files | 0 |
| ep-261 | DELETE | /repos/{owner}/{repo}/issues/{index}/assets/{attachment_id} | 3 steps | 3 files | 0 |

## Performance Issues Found

1. **HIGH - ep-258**: ListIssueAttachments calls issue.LoadAttributes which loads ALL issue data (comments, labels, milestones, reactions) just to extract attachments. Should use LoadAttachments directly.
2. **MEDIUM - ep-254**: GetIndividualUserRepoPermission executes 4-6 DB queries per call with no caching.
3. **MEDIUM - ep-255**: CanDoerChangeReviewRequests iterates over teams calling IsTeamMember per team (N+1 pattern).
4. **LOW - ep-259**: ChangeContent called with unchanged content just to trigger notifications, adding 2 unnecessary DB queries.

## Files Read
- routers/api/v1/repo/collaborators.go
- routers/api/v1/repo/issue_attachment.go
- models/perm/access/repo_permission.go
- models/repo/attachment.go
- models/repo/user_repo.go
- models/issues/issue.go
- services/pull/reviewer.go
- services/issue/review_request.go
- services/issue/content.go
- services/attachment/attachment.go
- services/convert/attachment.go
- services/convert/user.go
- services/convert/issue.go
- services/context/upload/upload.go
- modules/setting/attachment.go
- modules/structs/attachment.go
- modules/structs/repo_collaborator.go
