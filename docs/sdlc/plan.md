# Plan: Repository Reorganization

> Part of the [intent](intent.md) → [spec](spec.md) → plan chain.
> This plan covers the **repository** refactor only. It has no tasks that change the behavior of the original code.

## 1. Scope

| In scope | Out of scope |
|---|---|
| Moving files into a clear layout | Any edit to `high_performance_stocks.py` |
| New README and technical docs | Fixing bugs, deprecated APIs or docstrings |
| Intent / spec / plan artifacts | Adding dependencies, `requirements.txt`, packaging |
| Contributor/agent rules (`AGENTS.md`) | CI/CD, Docker, linters, tests, Makefile |
| `.gitignore` | Changing the license |

## 2. Discovery Findings (input to the plan)

- 3 files: one 80-line Python script, a README and a custom license.
- 4 commits on 2024-11-18 by Baruch Lopez.
- No PDFs, Word files, images, datasets, notebooks or outputs.
- The README contradicts the code in 5 places ([spec §5](spec.md#5-discrepancies-with-the-original-readme)).
- Origin: no academic evidence. Classified as a Personal Project (inferred).

## 3. Target Layout

```
README.md               new — portfolio-grade overview
LICENSE                 unchanged
AGENTS.md               new — working rules (source code is read-only)
.gitignore              new — Python caches, virtualenvs, generated CSV
src/high_performance_stocks.py      moved, unchanged
docs/project-context.md             new
docs/code-overview.md               new
docs/possible-improvements.md       new — not applied
docs/sdlc/{intent,spec,plan}.md     new
docs/original/README.original.md    moved, unchanged
```

Design decisions:

- **`src/` for a single file.** This keeps code apart from documentation at the root. No package structure (`__init__.py`) was added, because the original is a script and not a package.
- **No `data/` or `assets/`.** The project has no committed data or images, so creating empty folders would be artificial.
- **No `architecture.md`.** Four functions in one file do not justify a separate architecture document. The flow is covered in [code-overview.md](../code-overview.md).
- **Original README preserved** under `docs/original/`, so the historical description can still be read next to the corrected one.
- **Generated CSV is git-ignored**, because it is a runtime output and none was ever committed.

## 4. Tasks

| # | Task | Result |
|---|---|---|
| T1 | Inspect every file and the git history | Done |
| T2 | Record the SHA-256 of the source file before any change | Done |
| T3 | `git mv` the script to `src/`, and the README to `docs/original/` | Done |
| T4 | Write the README (overview, context, structure, run, discrepancies, historical note) | Done |
| T5 | Write the project context, code overview and possible improvements | Done |
| T6 | Write intent / spec / plan | Done |
| T7 | Add `AGENTS.md` and `.gitignore` | Done |
| T8 | Verify (see §5) and open a pull request | Done |

## 5. Verification

| Check | Method | Expected |
|---|---|---|
| Source unchanged | `sha256sum src/high_performance_stocks.py` | `1e8b804f33a6dda5be07513530468c64c4d858c8ed273cc97dba5801eb20f9c9` (same as commit `bac0a7a`) |
| Original README unchanged | `sha256sum docs/original/README.original.md` | `adf70afa78e38c9c418bddb00a2c616b91b3a424ea4ca992705ab610adafb22f` |
| Git sees pure renames | `git diff --stat -M main` | `R100` for both moved files |
| LICENSE untouched | `git diff main -- LICENSE` | empty |
| Relative links resolve | Scripted check of every Markdown link | All targets exist, except the `LICENSE` link inside `docs/original/README.original.md`: it was relative to the root and is left unchanged on purpose to keep the file verbatim |

Not verified: running the script end to end, because the environment had no network access to datahub.io or Yahoo Finance. The README says so.

## 6. Risks

| Risk | Mitigation |
|---|---|
| Documentation overstates what is known | Confirmed / Inferred / Unknown labels throughout |
| A future contributor "fixes" the original code | `AGENTS.md` rules. Improvements go in `docs/possible-improvements.md`, or in a separate, clearly labeled file |
| Run command changes because of the move | README documents `python src/high_performance_stocks.py`. The output file is still written to the current working directory |
