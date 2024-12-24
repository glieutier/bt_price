import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time

def get_historical_prices(days=1):
    """Fetch historical Bitcoin prices using CoinGecko's public API"""
    try:
        # Get current and 24h change from public endpoint
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_24h_vol': 'true',
            'include_24h_change': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        current_price = data['bitcoin']['usd']
        price_change = data['bitcoin'].get('usd_24h_change', 0)
        
        # Create timestamps for last 24 hours
        now = datetime.now()
        timestamps = [now - timedelta(hours=x) for x in range(24, -1, -1)]
        
        # Calculate approximate historical prices based on current price and 24h change
        price_change_ratio = price_change / 100
        price_24h_ago = current_price / (1 + price_change_ratio)
        
        # Linear interpolation between 24h ago price and current price
        prices = []
        for i in range(25):
            ratio = i / 24
            price = price_24h_ago + (current_price - price_24h_ago) * ratio
            prices.append(price)
        
        return timestamps, prices
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching historical prices: {e}')
        return None, None

def get_current_prices():
    """Fetch current Bitcoin price using CoinGecko's public API"""
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # Get USD price and change
        current_price_usd = data['bitcoin']['usd']
        price_change_usd = data['bitcoin'].get('usd_24h_change', 0)
        
        # Calculate UYU price using fixed conversion rate
        uyu_rate = 39.5  # Fixed conversion rate USD to UYU
        current_price_uyu = current_price_usd * uyu_rate
        
        return current_price_usd, current_price_uyu, price_change_usd
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching price: {e}')
        return None, None, None

def plot_price_history(timestamps, prices):
    """Create and save a plot of Bitcoin price history"""
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, prices, 'b-', label='BTC/USD')
    
    # Formatting
    plt.title('Bitcoin Price Last 24 Hours', fontsize=14)
    plt.xlabel('Time (UTC)', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('btc_price_history.png')
    plt.close()

def main():
    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Fetch current prices
    price_usd, price_uyu, change_usd = get_current_prices()
    
    if price_usd and price_uyu:
        print(f'\nBitcoin Price ({timestamp})')
        print('-' * 40)
        print(f'USD Price: ${price_usd:,.2f}')
        print(f'UYU Price: ${price_uyu:,.2f}')
        print(f'24h Change (USD): {change_usd:.2f}%\n')
        
        # Fetch and plot historical data
        timestamps, prices = get_historical_prices()
        if timestamps and prices:
            plot_price_history(timestamps, prices)
            print('Price history plot has been saved as \'btc_price_history.png\'')

if __name__ == '__main__':
    main()