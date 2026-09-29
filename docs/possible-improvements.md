# Possible Improvements

> **None of these improvements have been applied.** The source code in `src/` is kept exactly as originally written, so that the historical context and the original development approach are preserved. This document is only a set of review notes, kept separate from the implementation.

Each item is labeled **Confirmed** (visible directly in the code) or **Inferred** (likely, but not verified by running the script; the reorganization environment had no network access).

## Correctness of the Analysis

| # | Observation | Status |
|---|---|---|
| 1 | The mean includes the **current partial year** (year-to-date), which can skew the average up or down. | Confirmed (from the logic) |
| 2 | The first computed return may compare against a **partial IPO year**. | Confirmed (from the logic) |
| 3 | An **arithmetic mean** of yearly returns overstates compound growth when returns are volatile. A CAGR (`(last/first)^(1/years) - 1`) would measure long-run growth more accurately. | Confirmed |
| 4 | Stocks with only 1–2 years of history can pass the filter. A minimum `Data Points` threshold would make the screen more robust. | Confirmed |
| 5 | Only NYSE listings are screened, even though the docstring and README talk about all US tickers. Adding a NASDAQ/other listings source would match the stated goal. | Confirmed |
| 6 | Some ticker symbols in the listings file may use a different notation from Yahoo Finance (for example share classes such as `BRK.B` vs `BRK-B`). Those tickers would fail silently. | Inferred |

## Compatibility and Maintenance

| # | Observation | Status |
|---|---|---|
| 7 | `resample('Y')` uses a frequency alias that pandas deprecated in 2.2 in favor of `'YE'`. Newer pandas versions may warn or reject it. | Inferred (depends on installed version) |
| 8 | Dependency versions are not pinned anywhere, so results and behavior depend on whichever `pandas`/`yfinance` versions are installed. | Confirmed |
| 9 | The datahub.io URL is an external dependency with no fallback. If it moves or changes its schema (`ACT Symbol`), the script stops with an error. The URL could not be checked during the reorganization. | Confirmed / Unknown availability |
| 10 | `datetime` is imported but not used. `data['Year']` is assigned but not used. | Confirmed |
| 11 | The README and the code disagree on the script name, market coverage, output column name and license (see [project-context.md](project-context.md#contradictions-between-sources)). | Confirmed |

## Performance and Robustness

| # | Observation | Status |
|---|---|---|
| 12 | Requests run one after another, one per ticker. Batching (`yf.download` with many tickers) or concurrency would cut the run time a lot. | Confirmed |
| 13 | There is no caching, so every run downloads the whole history again. | Confirmed |
| 14 | There is no rate limiting or retry logic, so Yahoo Finance throttling may cause many silent failures. | Inferred |
| 15 | The catch-all `except Exception` prints the error but does not record which tickers failed. | Confirmed |
| 16 | The output path is relative to the current working directory, not to the project. | Confirmed |

## Usability

| # | Observation | Status |
|---|---|---|
| 17 | The threshold (`10`), source URL and output filename are hard-coded. CLI arguments would make them configurable. | Confirmed |
| 18 | Collected details (`Data Points`, yearly returns) are thrown away. Adding them to the CSV would make the results easier to audit. | Confirmed |
| 19 | There are no tests. The return calculation is a pure function of a price series and could be unit-tested with fixed data. | Confirmed |
