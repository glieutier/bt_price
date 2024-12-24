import requests
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import time

def get_historical_prices(days=1):
    """Fetch historical Bitcoin prices from CoinGecko API"""
    try:
        # CoinGecko API endpoint for historical data
        url = f'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': 'hourly'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        prices = data['prices']  # [[timestamp, price], ...]
        
        # Convert to lists of timestamps and prices
        timestamps = [datetime.fromtimestamp(price[0]/1000) for price in prices]
        price_values = [price[1] for price in prices]
        
        return timestamps, price_values
    
    except requests.exceptions.RequestException as e:
        print(f'Error fetching historical prices: {e}')
        return None, None

def get_current_prices():
    """Fetch current Bitcoin price from CoinGecko API in USD and UYU"""
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd,uyu',
            'include_24hr_change': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        current_price_usd = data['bitcoin']['usd']
        current_price_uyu = data['bitcoin']['uyu']
        price_change_usd = data['bitcoin'].get('usd_24h_change', 0)
        
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