# Project Context

This document pieces together what can be learned about where the project came from. Each statement is tagged:

- **Confirmed**: backed directly by a file or by git history.
- **Inferred**: a reasonable deduction from the evidence, not proven.
- **Unknown**: the repository does not provide enough information to determine this.

## Sources Examined

The original repository had only three files and four commits:

| File | Kind | Notes |
|---|---|---|
| `high_performance_stocks.py` | Source code | 80 lines of Python, the only code file. Now at `src/`. |
| `README.md` | Documentation | Original project description. Now at `docs/original/README.original.md`. |
| `LICENSE` | License | Custom "Open Public License with Contribution Requirement (OPLCR)". |

There were no PDFs, Word documents, presentations, images, diagrams, notebooks, datasets or generated outputs to analyze.

Git history (Confirmed):

| Commit | Date | Message | Content |
|---|---|---|---|
| `bac0a7a` | 2024-11-18 14:29 (-06:00) | Initial commit | Adds `high_performance_stocks.py` |
| `afb3ec9` | 2024-11-18 14:35 | Update README.md | Adds README |
| `312a0ce` | 2024-11-18 14:36 | Update README.md | Edits README |
| `f8b343e` | 2024-11-18 14:39 | Add LICENSE | Adds LICENSE |

All commits are by **Baruch Lopez** and were made within about ten minutes of each other. The commit messages match GitHub's web-interface defaults, which suggests the files were uploaded through the browser (Inferred).

## Origin

| Aspect | Finding | Status |
|---|---|---|
| Project type | Personal Project / Technical Experiment | Inferred |
| Academic context (university, course, assignment) | No evidence of any | Unknown |
| Author | Baruch Lopez | Confirmed (git history, README contact section) |
| Date | November 2024 | Confirmed (commit dates) |
| Development time before publication | Not visible; the code arrived fully formed in one commit | Unknown |

Why "personal" rather than academic (Inferred):

- None of the files mention a university, course, professor or assignment.
- The README ends with the author's personal website and LinkedIn, which fits a portfolio or personal project.
- The custom license covers commercial use and asks for a revenue share. That concern belongs to an independent author, not to a class assignment.

## Motivation and Objective

- **Stated objective (Confirmed, original README):** "analyze the historical annual returns of all stocks listed on the US Stock Exchange" and "identify stocks with an average annual return greater than 10%".
- **Likely motivation (Inferred):** an investment-screening curiosity. The idea was to find stocks that have historically beaten a 10% yearly threshold, a common rule-of-thumb benchmark for long-run equity returns. The repository never states this motivation directly.

## Scope

In scope (Confirmed from code):

- Download a ticker list from a public CSV.
- Download the maximum available daily price history per ticker from Yahoo Finance.
- Compute calendar-year returns and their arithmetic mean.
- Filter (> 10%), sort, save to CSV and print.

Out of scope (not present in the code):

- Risk metrics, volatility, dividends-adjusted analysis beyond what `yfinance` returns by default, CAGR, charts, persistence/caching, parallelism, CLI options, tests.

## Contradictions Between Sources

These are documented as found, not resolved:

1. **Script name:** the README says `stock_returns_analysis.py`, but the file is `high_performance_stocks.py`.
2. **Market coverage:** the README says "all stocks listed on the US Stock Exchange", but the code downloads `nyse-listed.csv` only, so NASDAQ and other exchanges are not included.
3. **Dependencies:** the README lists `numpy`, which the code does not import.
4. **Output column name:** the README says `Average Annual Return (%)`, but the code writes `Average Annual Return`.
5. **License:** the README says MIT, but the `LICENSE` file is the custom OPLCR.
6. **Clone URL:** the README's clone instructions point to a placeholder (`your-username/historical-stock-returns-analysis`), not to this repository.

## Historical Artifacts

- No outputs (`high_performance_stocks.csv`) were ever committed.
- The example output table in the original README (AAPL 15.6, TSLA 20.3, NVDA 18.7) is illustrative. The repository has no evidence that these numbers came from a real run.
