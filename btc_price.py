import requests
import json
from datetime import datetime

def get_bitcoin_price():
    """Fetch current Bitcoin price from CoinGecko API in USD and UYU"""
    try:
        # CoinGecko API endpoint for Bitcoin price in USD and UYU
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd,uyu',
            'include_24hr_change': 'true'
        }
        
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        data = response.json()
        
        # Extract prices and 24h changes
        current_price_usd = data['bitcoin']['usd']
        current_price_uyu = data['bitcoin']['uyu']
        price_change_usd = data['bitcoin'].get('usd_24h_change', 0)  # Default to 0 if not available
        
        return current_price_usd, current_price_uyu, price_change_usd
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price: {e}')
        return None, None, None

def main():
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Fetch Bitcoin prices
    price_usd, price_uyu, change_usd = get_bitcoin_price()
    
    if price_usd and price_uyu:
        print(f'\nBitcoin Price ({timestamp})')
        print('-' * 40)
        print(f'USD Price: ${price_usd:,.2f}')
        print(f'UYU Price: ${price_uyu:,.2f}')
        print(f'24h Change (USD): {change_usd:.2f}%\n')

if __name__ == '__main__':
    main()