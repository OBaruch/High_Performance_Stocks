# Working Rules for Contributors and Automated Agents

This repository is a **historical archive** of a small 2024 personal project. Read these rules before making any change.

## Non-negotiable

1. **`src/` is read-only.** Do not edit, reformat, lint, rename or "fix" `src/high_performance_stocks.py`. Its SHA-256 must stay `1e8b804f33a6dda5be07513530468c64c4d858c8ed273cc97dba5801eb20f9c9`.
2. **`docs/original/` and `LICENSE` are read-only.** They are kept verbatim as historical records.
3. **Do not add infrastructure** the project never had (CI, Docker, package managers, linters, test frameworks, Makefiles) unless the maintainer explicitly asks for it.
4. **Do not invent facts.** Mark claims as *Confirmed*, *Inferred* or *Unknown*.

## Where changes go

| Change | Location |
|---|---|
| Improvement ideas, bug notes | `docs/possible-improvements.md` (documentation only) |
| Context or history corrections | `docs/project-context.md` |
| Behavior descriptions | `docs/sdlc/spec.md`, `docs/code-overview.md` |
| New work (for example a modernized version) | Start with a new intent → spec → plan in `docs/sdlc/`, and keep the new code clearly separate from `src/` |

## Workflow

Intent → Spec → Plan → Implement → Verify. See [`docs/sdlc/`](docs/sdlc/).

Before submitting any change, check that the source is intact:

```bash
sha256sum src/high_performance_stocks.py
```
