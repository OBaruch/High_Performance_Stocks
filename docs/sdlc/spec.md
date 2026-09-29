# Specification (As-Built)

> Part of the [intent](intent.md) → spec → [plan](plan.md) chain.
> This is a **reverse-engineered specification** of the existing implementation. It describes what `src/high_performance_stocks.py` *does*, not what it ideally should do. Where the code and the original README disagree, the code is the reference and the difference is noted.

Status labels: **C** = Confirmed from code · **I** = Inferred · **U** = Unknown.

## 1. System Overview

| Property | Value | Status |
|---|---|---|
| Form | Single Python module, run as a script | C |
| Interface | Command line, no arguments | C |
| Execution model | Batch, sequential, single process | C |
| State | None persisted between runs | C |
| External services | datahub.io (ticker list), Yahoo Finance through `yfinance` (prices) | C |
| Runtime dependencies | `pandas`, `yfinance` (unpinned) | C |
| Python version | 3.6+ required by f-strings; original version unknown | C / U |

## 2. Functional Requirements

### FR-1 Ticker universe
- **FR-1.1** The system shall download `https://datahub.io/core/nyse-other-listings/r/nyse-listed.csv`. *(C)*
- **FR-1.2** The system shall use the values of column `ACT Symbol` as the list of tickers, in file order. *(C)*
- **FR-1.3** If the download or parsing fails, execution ends with an unhandled exception. *(C)*

### FR-2 Annual returns per ticker
- **FR-2.1** For each ticker, the system shall request the maximum available daily history via `yf.Ticker(symbol).history(period="max")`. *(C)*
- **FR-2.2** If the history is empty, the ticker is skipped. *(C)*
- **FR-2.3** The annual return for year *Y* is `(Close_lastTradingDay(Y) / Close_lastTradingDay(Y-1) − 1) × 100`, computed using calendar-year resampling (`resample('Y').last()` then `pct_change()`). *(C)*
- **FR-2.4** The first year, which has no previous year, is dropped. The current incomplete year is **included** as a year-to-date value. *(C from logic; I that this was unintended)*
- **FR-2.5** Any exception while fetching or computing is printed as `Error fetching data for <symbol>: <error>` and the ticker is skipped. *(C)*

### FR-3 Screening
- **FR-3.1** The average annual return is the arithmetic mean of the yearly returns from FR-2. *(C)*
- **FR-3.2** A ticker qualifies when that mean is strictly greater than `10` (percent). *(C)*
- **FR-3.3** There is no minimum number of years. *(C)*

### FR-4 Output
- **FR-4.1** While running, the system prints `Processing <ticker>...` for every ticker. *(C)*
- **FR-4.2** If at least one ticker qualifies, the system writes `high_performance_stocks.csv` to the current working directory, without an index. *(C)*
- **FR-4.3** CSV columns: `Ticker` (string), `Average Annual Return` (float, percent, not rounded). *(C)*
- **FR-4.4** Rows are sorted by `Average Annual Return`, descending. *(C)*
- **FR-4.5** The same table is printed after the heading `Top-performing stocks:`. *(C)*
- **FR-4.6** If nothing qualifies, the system prints `No stocks met the criteria.` and writes no file. *(C)*

## 3. Non-Functional Characteristics (observed, not designed)

| ID | Characteristic | Status |
|---|---|---|
| NF-1 | Run time grows linearly with the number of tickers (one network request per ticker, no concurrency). | C |
| NF-2 | There is no retry, rate limiting or caching. Results may vary between runs if the data source throttles or changes. | C / I |
| NF-3 | Results depend on the installed `yfinance` defaults (for example price adjustment) and on `pandas` resampling behavior. | I |
| NF-4 | Nothing is logged except stdout. Failed tickers are not collected. | C |

## 4. Data Contract

**Input (ticker list CSV):** must contain the column `ACT Symbol`. Other columns are ignored. *(C)*
**Input (price history):** a DataFrame indexed by datetime with a `Close` column, as returned by `yfinance`. *(C)*
**Output (CSV):**

```csv
Ticker,Average Annual Return
<symbol>,<float>
...
```

## 5. Discrepancies with the Original README

| Topic | Original README | As-built |
|---|---|---|
| Script name | `stock_returns_analysis.py` | `high_performance_stocks.py` |
| Universe | All US stocks | NYSE listings only |
| Dependencies | yfinance, pandas, numpy | yfinance, pandas |
| Output column | `Average Annual Return (%)` | `Average Annual Return` |
| License | MIT | Custom OPLCR (`LICENSE`) |

## 6. Out of Scope

Anything not listed above, for example a CLI, configuration, persistence, visualization, tests or packaging, is not part of the as-built system.
