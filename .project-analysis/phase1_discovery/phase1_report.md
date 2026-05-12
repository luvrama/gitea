# Phase 1 Discovery Report: Gitea

## Project Overview

| Property | Value |
|----------|-------|
| Project | Gitea (self-hosted Git service) |
| Language | Go 1.26.3 |
| Framework | go-chi/chi v5.2.5 (HTTP router) + XORM v1.3.11 (ORM) |
| Build Tool | Make + Go modules |
| Source Files | 1,996 Go files (excluding tests) |
| Database | SQL (MySQL, PostgreSQL, SQLite3, MSSQL - configurable) |
| API Style | REST (Swagger-documented) |

## Architecture Pattern

**Layered Architecture** with clear separation:

```
cmd/           → CLI entry points (urfave/cli)
routers/       → HTTP route handlers (controllers)
  ├── api/     → REST API v1 (JSON)
  ├── web/     → Web UI handlers (HTML templates)
  ├── private/ → Internal API (node-to-node)
  └── install/ → Installation wizard
services/      → Business logic layer
models/        → Data access layer (XORM entities + queries)
modules/       → Shared utilities and infrastructure
```

## API Summary

**Total REST API Endpoints: 475**

| HTTP Method | Count |
|-------------|-------|
| GET | 239 |
| POST | 96 |
| DELETE | 81 |
| PATCH | 32 |
| PUT | 27 |

### Endpoints by Resource/Tag

| Resource | Endpoints |
|----------|-----------|
| Repository | 200 |
| User | 75 |
| Issue | 69 |
| Organization | 67 |
| Admin | 32 |
| Miscellaneous | 12 |
| Package | 9 |
| Notification | 7 |
| Settings | 4 |

## Database Summary

**Total Database Entities: 112**

Key entity groups:
- **User Management**: User, EmailAddress, Follow, Blocking, UserSetting, ExternalLoginUser, OpenID, Badge
- **Repository**: Repository, Star, Watch, Topic, Collaboration, Fork, Mirror, PushMirror, Release, Attachment, Upload
- **Issues & Pull Requests**: Issue, Comment, Label, Milestone, PullRequest, Review, Reaction, Stopwatch, TrackedTime, IssueWatch, IssueDependency
- **Git**: Branch, ProtectedBranch, ProtectedTag, CommitStatus, LFSMetaObject, LFSLock
- **Authentication**: AccessToken, OAuth2Application, OAuth2Grant, OAuth2AuthorizationCode, TwoFactor, WebAuthnCredential, AuthSource, Session
- **Organization**: Organization, Team, TeamUser, TeamRepo, TeamUnit, TeamInvite, OrgUser
- **Actions (CI/CD)**: ActionRun, ActionRunJob, ActionRunner, ActionRunnerToken, ActionTask, ActionTaskStep, ActionSchedule, ActionVariable, ActionArtifact
- **Packages**: Package, PackageVersion, PackageFile, PackageBlob, PackageBlobUpload, PackageProperty, PackageCleanupRule
- **Webhooks**: Webhook, HookTask
- **System**: Notice, AppState, Setting
- **Projects**: Project, ProjectColumn, ProjectIssue

## External Integrations Summary

**17 External API Integrations:**

1. **Migration Sources**: GitHub, GitLab, Gitea, AWS CodeCommit, OneDev
2. **Webhook Targets**: Slack, Discord, Telegram, Matrix, MS Teams, DingTalk, Feishu/Lark
3. **Authentication**: LDAP, OAuth2 (via Goth - supports 20+ providers), WebAuthn, PAM, SSPI
4. **Storage**: MinIO/S3, Azure Blob Storage, Local filesystem
5. **Search**: Bleve (embedded), Meilisearch (external)
6. **Email**: SMTP (outbound), IMAP (incoming)
7. **Monitoring**: Prometheus metrics

**70 Direct Go Dependencies** (120 total including indirect)

## Key Observations

1. **Massive codebase**: ~2000 Go source files with 475 API endpoints and 112 database entities. This is a mature, feature-rich application.

2. **Multi-database support**: Supports 4 SQL databases via XORM, making it highly portable but adding complexity to testing and migrations.

3. **Internal queue system**: Uses a custom queue abstraction (`modules/queue/`) backed by LevelDB, Redis, or in-memory channels - not an external message broker.

4. **Comprehensive package registry**: Supports 20+ package formats (npm, PyPI, Maven, Docker/OCI, Cargo, NuGet, Helm, etc.) via `routers/api/packages/`.

5. **CI/CD system (Actions)**: Full GitHub Actions-compatible CI/CD system with runners, workflows, artifacts.

6. **Federation support**: ActivityPub integration (partially implemented).

7. **Frontend**: Vue.js 3 + Vite + TailwindCSS for the web UI (separate from Go backend).

## Potential Concerns

- **Database migration complexity**: With 112 entities across 4 DB engines, schema migrations require careful testing.
- **Large attack surface**: 475 API endpoints with various auth mechanisms (token, OAuth2, basic, reverse proxy).
- **Tight coupling in models**: Models layer contains both entity definitions and query logic (no separate repository pattern).
- **Queue reliability**: Internal queue system may not provide the durability guarantees of dedicated message brokers.

## Recommendations for Phase 2

Given the project size (>500 files), Phase 2 analysis should be run per-module:

1. **Priority 1**: `routers/api/v1/` - Full API endpoint analysis with request/response schemas
2. **Priority 2**: `models/` - Complete entity relationship mapping
3. **Priority 3**: `services/` - Business logic flow analysis
4. **Priority 4**: `modules/` - Infrastructure and utility analysis
5. **Priority 5**: `routers/web/` - Web UI route analysis (184 handler files)

Each module should be analyzed in a separate session to avoid context overflow.
