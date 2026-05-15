# Global Error Handlers

**3 handlers**

## APIContext

`services/context/api.go`

| Exception | Status | Response |
|-----------|--------|----------|
| internal_error | 500 | APIError |
| not_found | 404 | map[message,url,errors] |
| generic_error | variable | APIError |

## context.APIContext

`services/context/api.go`

| Exception | Status | Response |
|-----------|--------|----------|
| generic error | 500 | APIError JSON |
| validation error | 422 | APIError JSON |
| not found | 404 | APIError JSON |
| forbidden | 403 | APIError JSON |
| unauthorized | 401 | APIError JSON |

## handleChangeRepoFilesError

`routers/api/v1/repo/file.go`

| Exception | Status | Response |
|-----------|--------|----------|
| git.ErrPushRejected | 403 | error |
| files_service.ErrUserCannotCommit | 403 | error |
| pull_service.IsErrFilePathProtected | 403 | error |
| git_model.ErrBranchAlreadyExists | 422 | error |
| files_service.ErrCommitIDDoesNotMatch | 422 | error |
| util.ErrNotExist | 404 | error |
