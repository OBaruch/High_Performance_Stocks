 
# Historical Stock Returns Analysis

This repository contains a Python script to analyze the historical annual returns of all stocks listed on the US Stock Exchange. The script calculates the annual percentage return for each year in a stock's history and identifies stocks with an **average annual return greater than 10%**.

---

## Features

- Fetches historical stock data for all US-listed stocks.
- Calculates **annual returns** for each stock year by year.
- Filters and outputs stocks with an **average annual return exceeding 10%**.
- Saves the results to a CSV file for further analysis.

---

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries:
  - `yfinance`
  - `pandas`
  - `numpy`

Install dependencies using pip:

```bash
pip install yfinance pandas numpy
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/historical-stock-returns-analysis.git
   cd historical-stock-returns-analysis
   ```

2. Run the script:
   ```bash
   python stock_returns_analysis.py
   ```

3. The script will:
   - Fetch a list of US-listed stocks.
   - Calculate their annual returns.
   - Filter stocks with an average annual return greater than 10%.
   - Save the results to `high_performance_stocks.csv`.

---

## Output

The script generates a CSV file (`high_performance_stocks.csv`) with the following columns:

- **Ticker**: The stock's ticker symbol.
- **Average Annual Return (%)**: The stock's average annual return since its inception.

Example output:

| Ticker | Average Annual Return (%) |
|--------|----------------------------|
| AAPL   | 15.6                       |
| TSLA   | 20.3                       |
| NVDA   | 18.7                       |

---

## Technical Details

### Analysis Process

1. **Fetch Stock Data**:
   - The script uses `yfinance` to fetch historical data for each stock.

2. **Calculate Annual Returns**:
   - Yearly returns are calculated using:
     \[
     	ext{Annual Return (\%)} = rac{	ext{Close Price (Year End)}}{	ext{Close Price (Previous Year End)}} - 1
     \]

3. **Filter Stocks**:
   - Stocks with an average annual return exceeding 10% are selected for the final output.

### Limitations

- **Data Accuracy**:
  - Data fetched from Yahoo Finance may have limitations or inaccuracies.
- **Execution Time**:
  - Analyzing all listed stocks can take significant time due to the large dataset.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, feel free to visit:

- **Website**: [baruchlopez.com](https://baruchlopez.com)
- **LinkedIn**: [Baruch Lopez](https://baruchlopez.com)
