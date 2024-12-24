# Bitcoin Price Tracker

A Python script to fetch and visualize Bitcoin prices using the CoinGecko API.

## Features
- Fetches current Bitcoin prices in USD and UYU
- Shows 24-hour price changes
- Generates a price history chart
- Handles multiple currencies with fallback conversion

## Setup

1. Clone the repository:
```bash
git clone https://github.com/glieutier/bt_price.git
cd bt_price
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Get a CoinGecko API key:
   - Go to https://www.coingecko.com/api/pricing
   - Sign up for a free account
   - Generate an API key

4. Set up your API key:
   - Create a `.env` file in the project directory
   - Add your API key:
     ```
     COINGECKO_API_KEY=your_api_key_here
     ```

## Usage

Run the script:
```bash
python btc_price.py
```

The script will:
- Show current Bitcoin prices in USD and UYU
- Display 24-hour price changes
- Generate a price history chart as 'btc_price_history.png'

## Error Handling
- Handles API authentication errors
- Provides fallback for unsupported currencies
- Shows clear error messages and warnings