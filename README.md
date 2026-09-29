# High Performance Stocks

A small Python script that downloads the full price history of a list of US-listed stocks from Yahoo Finance, computes each stock's year-over-year returns, and reports the stocks whose **average annual return is greater than 10%**.

> **Original implementation notice**
> This repository preserves the original implementation of the project. The source code has intentionally not been refactored or modernized in order to retain the historical context and original development approach.
> The source code represents the original implementation developed as a personal project.

---

## Project Overview

| | |
|---|---|
| **Type** | Single-file Python script (command-line, batch) |
| **Project origin** | Personal Project *(inferred — see [Project Context](#project-context))* |
| **Original date** | November 18, 2024 (date of the initial commit) |
| **Author** | Baruch Lopez |
| **Main file** | [`src/high_performance_stocks.py`](src/high_performance_stocks.py) |
| **Status** | Historical / archived. Preserved as written. |

## Project Context

The repository contains no course names, assignment statements, university references, or reports, so there is no evidence that this was academic work. The evidence that does exist points to a personal project:

- the author's personal website and LinkedIn were listed as contact in the original README;
- the project ships with a custom, author-written license ([`LICENSE`](LICENSE)) aimed at personal, educational and commercial use;
- the whole project is one script plus documentation, published in a single day.

**Classification:** Personal Project / Technical Experiment. This is **inferred**, not confirmed. Details are in [`docs/project-context.md`](docs/project-context.md).

## Problem Statement

Which publicly listed US stocks have historically averaged more than 10% return per year? The script answers this with a brute-force screen: it checks every ticker in a public listings file against its full Yahoo Finance history.

## Objective

To produce a ranked list (CSV) of tickers whose arithmetic mean of calendar-year returns, over their whole available history, exceeds 10%.

## Repository Structure

```
.
├── README.md                     # This file
├── LICENSE                       # Original license (unchanged)
├── AGENTS.md                     # Working rules for contributors and automation (read before changing anything)
├── .gitignore
├── src/
│   └── high_performance_stocks.py  # Original source code (unchanged)
└── docs/
    ├── project-context.md        # Origin, scope and historical information
    ├── code-overview.md          # Walkthrough of the original script
    ├── possible-improvements.md  # Observations only; NOT applied
    ├── sdlc/
    │   ├── intent.md             # Why this repository exists and what the refactor aimed for
    │   ├── spec.md               # As-built specification of the original behavior
    │   └── plan.md               # Plan and verification of the repository refactor
    └── original/
        └── README.original.md    # The README as originally published (unchanged)
```

## Original Implementation

`src/high_performance_stocks.py` is byte-for-byte identical to the file from the initial commit (`bac0a7a`). The only change is where it lives: it was moved from the repository root to `src/` with `git mv`. Its logic, style, comments, naming, known issues and dependencies have not been touched.

Any bugs, deprecated APIs or improvement ideas are written down separately in [`docs/possible-improvements.md`](docs/possible-improvements.md). None of them have been applied.

## Technologies

Confirmed from the source code imports:

- **Python 3** (the f-strings mean it needs Python 3.6 or later; the exact version used originally is unknown)
- **pandas**: CSV reading, time-series resampling, result table
- **yfinance**: Yahoo Finance price history
- `datetime` (standard library): imported but not used

External data sources referenced in the code:

- `https://datahub.io/core/nyse-other-listings/r/nyse-listed.csv`: the ticker list (column `ACT Symbol`)
- Yahoo Finance, through `yfinance`

## How It Works

```
fetch_all_us_tickers()          ──► list of ticker symbols (NYSE listings CSV)
        │
        ▼
analyze_tickers(tickers)        ──► for each ticker, sequentially:
        │                              get_stock_annual_returns(ticker)
        │                                ├─ yfinance history(period="max")
        │                                ├─ last Close of each calendar year
        │                                └─ year-over-year % change
        │                              keep if mean(annual returns) > 10
        ▼
main()                          ──► sort descending, write high_performance_stocks.csv, print table
```

For more detail, see [`docs/code-overview.md`](docs/code-overview.md) and [`docs/sdlc/spec.md`](docs/sdlc/spec.md).

## Inputs and Outputs

| | Description |
|---|---|
| **Input** | No user input or CLI arguments. The ticker list and price data are downloaded at runtime. |
| **Output file** | `high_performance_stocks.csv`, written to the **current working directory**, with columns `Ticker` and `Average Annual Return`, sorted from highest to lowest. |
| **Console output** | A `Processing <TICKER>...` line for each ticker, error messages for failed tickers, and the final table (or `No stocks met the criteria.`). |

No output files were committed to the original repository, so there is no historical result to show. The example table in the original README (AAPL / TSLA / NVDA) was illustrative. It was not produced by the script.

## Running the Project

These steps follow from the code. They were **not** re-run during the repository reorganization, because the environment had no network access. Library versions were never pinned, so current versions of `pandas`/`yfinance` may behave differently (see [`docs/possible-improvements.md`](docs/possible-improvements.md)).

```bash
pip install pandas yfinance
python src/high_performance_stocks.py
```

Network access to `datahub.io` and Yahoo Finance is required. The script processes thousands of tickers one after another, so expect a long run time.

## Documentation

- [Project context](docs/project-context.md)
- [Code overview](docs/code-overview.md)
- [Possible improvements (not applied)](docs/possible-improvements.md)
- [Intent](docs/sdlc/intent.md) · [Spec](docs/sdlc/spec.md) · [Plan](docs/sdlc/plan.md)
- [Original README](docs/original/README.original.md)

## Known Discrepancies in the Original Documentation

The original README (kept unchanged in [`docs/original/`](docs/original/README.original.md)) does not fully match the code. These mismatches are documented here and have not been "fixed" in either file:

| Original README says | Code actually does |
|---|---|
| Run `python stock_returns_analysis.py` | The file is named `high_performance_stocks.py` |
| Analyzes *all* US-listed stocks | Uses the **NYSE**-listed file only (`nyse-listed.csv`) |
| Requires `numpy` | `numpy` is not imported directly (pandas depends on it) |
| Output column `Average Annual Return (%)` | Output column is `Average Annual Return` |
| Licensed under **MIT** | The `LICENSE` file contains a custom **OPLCR** license |

## License

See [`LICENSE`](LICENSE). Note that the original README described the project as MIT-licensed, but the actual license file is a custom "Open Public License with Contribution Requirement (OPLCR)". The `LICENSE` file is the authoritative text and has been kept as it was.

## Historical Note

This repository was later reorganized and documented to improve readability and preserve the historical context of the original project. The original source code remains unchanged.

## Contact

- Website: [baruchlopez.com](https://baruchlopez.com)
