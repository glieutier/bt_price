import requests
import json
from datetime import datetime

def get_bitcoin_price():
    """Fetch current Bitcoin price from CoinGecko API"""
    try:
        # CoinGecko API endpoint for Bitcoin price in USD
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
        }
        
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        data = response.json()
        
        # Extract price and 24h change
        current_price = data['bitcoin']['usd']
        price_change = data['bitcoin']['usd_24h_change']
        
        return current_price, price_change
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price: {e}')
        return None, None

def main():
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Fetch Bitcoin price
    price, change = get_bitcoin_price()
    
    if price and change:
        print(f'\nBitcoin Price ({timestamp})')
        print('-' * 30)
        print(f'Current Price: ${price:,.2f}')
        print(f'24h Change: {change:.2f}%\n')

if __name__ == '__main__':
    main()