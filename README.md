# Bitcoin Price Tracker

A Python-based Bitcoin price tracking tool that fetches real-time and historical price data using the CoinGecko API. The tool displays current Bitcoin prices in USD and UYU (Uruguayan Peso), along with a 24-hour price history visualization.

## Features

- Real-time Bitcoin price tracking in USD and UYU
- 24-hour price change percentage
- Historical price data visualization
- Automated graph generation saved as PNG
- Data sourced from CoinGecko API
- Hourly price data points for accurate tracking

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - requests >= 2.25.1
  - matplotlib >= 3.4.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/glieutier/bt_price.git
cd bt_price
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:
```bash
python btc_price.py
```

The script will:
1. Display current Bitcoin prices in USD and UYU
2. Show the 24-hour price change percentage
3. Generate a price history graph saved as 'btc_price_history.png'

## Output Example

```
Bitcoin Price (2024-12-24 12:30:45)
----------------------------------------
USD Price: $42,000.00
UYU Price: $1,680,000.00
24h Change (USD): 2.50%

Price history plot has been saved as 'btc_price_history.png'
```

## API Reference

This project uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch Bitcoin price data. The following endpoints are utilized:
- `/simple/price`: For current price data
- `/coins/bitcoin/market_chart`: For historical price data

## Error Handling

The script includes robust error handling for:
- API request failures
- Connection issues
- Data parsing errors

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.