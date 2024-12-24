# Bitcoin Price Tracker

A Python-based tool that fetches and visualizes Bitcoin price data in both USD and UYU (Uruguayan Peso) using the CoinGecko API.

## Features

- Real-time Bitcoin price tracking in USD and UYU
- 24-hour price change percentage
- Historical price visualization for the last 24 hours
- Automatic generation of price history charts
- Data sourced from CoinGecko's reliable API

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

## API Information

This project uses the CoinGecko API to fetch Bitcoin price data. The API is free to use and doesn't require authentication for basic endpoints.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Author

[glieutier](https://github.com/glieutier)

## Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing the free cryptocurrency API
- Contributors and maintainers of the requests and matplotlib libraries
