
import yfinance as yf
import pandas as pd
import datetime

def fetch_all_us_tickers():
    """
    Fetch a comprehensive list of US tickers.
    For simplicity, you may use a CSV file of all US tickers (e.g., NASDAQ and NYSE).
    """
    url = "https://datahub.io/core/nyse-other-listings/r/nyse-listed.csv"
    tickers_df = pd.read_csv(url)
    return tickers_df['ACT Symbol'].tolist()

def get_stock_annual_returns(stock_symbol):
    """
    Fetch historical data for a stock and calculate its annual returns.
    """
    try:
        # Fetch historical data
        stock = yf.Ticker(stock_symbol)
        data = stock.history(period="max")
        
        if data.empty:
            return None
        
        # Calculate annual returns
        data['Year'] = data.index.year
        annual_returns = data['Close'].resample('Y').last().pct_change() * 100
        annual_returns = annual_returns.dropna()  # Remove NaN years
        annual_returns = annual_returns.reset_index()
        annual_returns.columns = ['Year', 'Return']
        annual_returns['Year'] = annual_returns['Year'].dt.year  # Convert year to integer
        return annual_returns
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return None

def analyze_tickers(tickers):
    """
    Analyze all tickers and calculate their average annual return.
    """
    results = []
    for ticker in tickers:
        print(f"Processing {ticker}...")
        annual_returns = get_stock_annual_returns(ticker)
        if annual_returns is not None and not annual_returns.empty:
            # Calculate average annual return
            average_return = annual_returns['Return'].mean()
            if average_return > 10:  # Filter for average returns > 10%
                results.append({
                    "Ticker": ticker,
                    "Average Annual Return": average_return,
                    "Data Points": len(annual_returns),
                    "Annual Returns": annual_returns
                })
    return results

def main():
    # Fetch all US tickers
    tickers = fetch_all_us_tickers()
    
    # Analyze each ticker
    results = analyze_tickers(tickers)
    
    # Save results to a CSV
    if results:
        summary = pd.DataFrame([{"Ticker": res["Ticker"], 
                                 "Average Annual Return": res["Average Annual Return"]} for res in results])
        summary = summary.sort_values(by="Average Annual Return", ascending=False)
        summary.to_csv("high_performance_stocks.csv", index=False)
        
        # Display top performers
        print("Top-performing stocks:")
        print(summary)
    else:
        print("No stocks met the criteria.")

if __name__ == "__main__":
    main()
