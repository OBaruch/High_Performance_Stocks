# Code Overview

This is a walkthrough of the original script, [`src/high_performance_stocks.py`](../src/high_performance_stocks.py). The code is described as it is. It has not been modified.

## File Summary

| Item | Value |
|---|---|
| Lines | 80 |
| Language | Python 3 |
| Imports | `yfinance as yf`, `pandas as pd`, `datetime` (unused) |
| Entry point | `if __name__ == "__main__": main()` |
| Functions | `fetch_all_us_tickers`, `get_stock_annual_returns`, `analyze_tickers`, `main` |
| Classes | None |
| Configuration | None; all values are hard-coded |

## Execution Flow

```
main()
 ├─ fetch_all_us_tickers()                # 1 HTTP request (datahub.io)
 ├─ analyze_tickers(tickers)
 │    └─ for ticker in tickers:           # sequential loop
 │         ├─ print "Processing <ticker>..."
 │         └─ get_stock_annual_returns()  # 1 Yahoo Finance request per ticker
 │              └─ mean(Return) > 10 ? append to results
 └─ results ?
      ├─ yes → DataFrame(Ticker, Average Annual Return)
      │        → sort desc → high_performance_stocks.csv → print
      └─ no  → print "No stocks met the criteria."
```

## Functions

### `fetch_all_us_tickers()`

- Reads `https://datahub.io/core/nyse-other-listings/r/nyse-listed.csv` with `pd.read_csv`.
- Returns the `ACT Symbol` column as a Python list.
- The docstring says a CSV of "NASDAQ and NYSE" tickers could be used, but the URL only covers NYSE listings.
- Exceptions are not handled, so if the download fails the whole script stops.

### `get_stock_annual_returns(stock_symbol)`

1. `yf.Ticker(stock_symbol).history(period="max")` gets the full daily history.
2. If the DataFrame is empty it returns `None`.
3. Adds a `Year` column to `data`. This column is never used afterwards.
4. `data['Close'].resample('Y').last()` takes the last close of each calendar year.
5. `.pct_change() * 100` gives the year-over-year return in percent. `dropna()` removes the first year, which has no previous value.
6. Resets the index, renames the columns to `['Year', 'Return']`, and converts `Year` from a timestamp to an integer.
7. Any exception is printed as `Error fetching data for <symbol>: <e>` and the function returns `None`.

Behavior worth noting (these follow from the code; they were not verified by running it):

- The **first** return compares the second year-end with the first year-end. The first year may be a partial year (IPO date to December 31).
- The **last** "year" is the latest available close in the current, unfinished year, so it is a year-to-date return.
- The average is an **arithmetic mean** of yearly returns, not a compound annual growth rate (CAGR).
- Prices come from `yfinance`'s `Close` column. Whether that column is split/dividend-adjusted depends on the `yfinance` version's defaults.

### `analyze_tickers(tickers)`

- Loops over every ticker one at a time.
- For each successful, non-empty result, computes `annual_returns['Return'].mean()`.
- Keeps tickers where the mean is `> 10`. Each kept entry is a dict with `Ticker`, `Average Annual Return`, `Data Points` (number of yearly returns) and `Annual Returns` (the full DataFrame).
- `Data Points` and `Annual Returns` are collected but never written or printed.

### `main()`

- Runs the steps above.
- If there are results, it builds a two-column DataFrame (`Ticker`, `Average Annual Return`), sorts it in descending order, writes `high_performance_stocks.csv` with no index to the current working directory, and prints it.
- Otherwise it prints `No stocks met the criteria.`

## Dependencies Observed

| Dependency | Used for | Declared anywhere? |
|---|---|---|
| `pandas` | CSV I/O, resampling, result table | Only in the original README (unpinned) |
| `yfinance` | Price history | Only in the original README (unpinned) |
| `datetime` | Not used | Standard library |

There is no `requirements.txt`, `setup.py` or `pyproject.toml` in the original project. None were added, because adding one would mean choosing dependency versions the original never specified.
