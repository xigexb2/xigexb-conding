# Git, collaboration, commits, and releases

**English** | [简体中文](../zh-CN/engineering/git.md) | [Standards index](../translations.md)

## VCS01 Authorization and scope

- Reading history/status/diffs is development preparation; commits, pushes, merges, tags/releases, deployments follow their respective authorization
- A request to commit authorizes a local commit only; push when explicitly requested, with prior session authorization remaining valid
- Preparing GitHub-ready material does not itself authorize creating remotes or publishing code
- Inspect git status --short and target diffs to distinguish user work, other tasks, generated and untracked files
- Do not reset, clean, restore, overwrite through checkout, delete branches, or discard user changes without authorization
- Use a suitable branch/worktree when isolation is needed; preserve provenance when moving changes and exclude unrelated commits

## VCS02 Branches and commits

- Follow team branching practices; short-lived branches/trunk integration are valid for small teams without imposing GitFlow
- Name branches by purpose and use actual requirement/defect identifiers
- Each commit expresses an independently understandable/revertible change; avoid unrelated refactoring/formatting
- Code, documentation, necessary tests can form one atomic change rather than being split mechanically by file type
- Stage explicit paths and use hunks for mixed-origin files while preserving preexisting staging
- Avoid accidentally including unrelated changes through git add . or git add -A

## VCS03 Conventional Commits

```text
type(scope): 简体中文摘要
```

- Scope is optional; type/scope use lowercase English, summaries use concise Simplified Chinese; first line at most 72 characters, no final period
- Types: feat, fix, refactor, perf, docs, style, test, build, ci, chore, revert
- Mark breaking changes with ! and explain impact/migration under BREAKING CHANGE: in the body
- Describe behavior and purpose rather than vague summaries such as update or fix issue
- Do not fabricate authorship, signatures, issue associations, review approval; follow repository signing policy

## VCS04 Before and after commits

```text
git status --short
git diff --cached --name-status
git diff --cached
git diff --cached --check
```

- Inspect verification evidence, secrets, artifacts, unrelated changes, deletions
- After committing, inspect git show --stat --oneline HEAD and working-tree state
- Report commit hash, summary, verification, remaining work; an unpushed commit is not present remotely
- Before pushing, verify remote, branch, target history; afterward verify the remote reference points to the intended commit
- Prevent private-source publication to public remotes; similar names do not establish repository identity

## VCS05 PRs, reviews, and conflicts

- PRs describe the final problem/behavior, key tradeoffs, validation, uncovered boundaries without unrelated process history
- Review findings state triggers, consequences, location, feasible fixes; distinguish defects from preferences
- Resolve conflicts by understanding both sides and current contracts rather than selecting whole-file ours/theirs
- Rebase/amend changes commit identity; do not rewrite shared history without authorization
- Respect protection/force-push policies; verify explicit authorization and remote state for required rewrites
- Creating a PR or draft does not authorize approval/merge

## VCS06 Versions, tags, releases

- Use suitable SemVer or existing version schemes and explain compatibility, deprecation, migration
- Keep versions, build numbers, tags, manifests, artifacts consistent; never publish a manifest for nonexistent packages
- Release records include verifiable builds, checksums, signatures/provenance, necessary rollback steps
- Git tags, Releases, registries, app stores, production deployment are distinct publication actions
- Revoke/rotate leaked secrets; history rewrites do not replace incident response
