# Intent

> Part of the intent → spec → plan chain for this repository.
> **Intent** answers *why* and *what outcome*. [Spec](spec.md) describes *what the system does*. [Plan](plan.md) describes *how the change is carried out and verified*.

## 1. Original Product Intent (reconstructed)

*Source: original README and source code. Status: Confirmed unless marked otherwise.*

**Problem.** An investor wants to know which listed US stocks have historically delivered strong returns year after year.

**Desired outcome.** A ranked list of stock tickers whose average annual return, across their whole available price history, is **greater than 10%**, saved as a CSV for further analysis.

**User.** The author, working on a personal research/screening exercise (Inferred; see [project-context.md](../project-context.md)).

**Success looked like:**

- One command runs the whole screen without manual steps.
- Public, free data sources only (a listings CSV plus Yahoo Finance).
- The output is a simple CSV that can be opened in a spreadsheet.

**Non-goals (Inferred from what is absent):** investment advice, risk-adjusted metrics, real-time data, a UI, and production-grade reliability.

## 2. Repository Modernization Intent

*The goal of the 2026 reorganization.*

**Why.** The repository is kept as part of a technical portfolio. It had a single script at the root and a README that contradicted the code, and there was no record of context. A reader could not tell quickly what the project was, what it really did, or what state it was in.

**Outcome wanted.** A repository that someone can understand in a few minutes without reading the code, and that still presents the project honestly as the small 2024 script it is.

**Guiding principle.** *Modernize the repository, not the project.*

### Hard constraints

1. The source code is not modified in any way: logic, style, names, comments, bugs and dependencies all stay as they are. Only the file location may change.
2. Original documents (README, LICENSE) are kept verbatim.
3. Nothing is invented. Every claim is marked Confirmed / Inferred / Unknown.
4. No infrastructure the project never had: no CI, Docker, package managers, linters or test frameworks.
5. Everything is written in English.

### Success criteria

- `src/high_performance_stocks.py` has the same SHA-256 as the initial commit.
- A new README explains overview, context, behavior, inputs/outputs and how to run the script, and states the known discrepancies.
- The project's origin is classified from evidence and labeled as inferred.
- Improvement ideas are recorded apart from the code and are clearly marked as not applied.
- Contributors and automated coding agents have explicit working rules ([AGENTS.md](../../AGENTS.md)) that protect the original code.
