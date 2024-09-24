import os
import time
import csv
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from datetime import datetime

# Load API key from environment variables
api_key = 'BH4RYJPPB7BF9EF4'

# Initialize Alpha Vantage TimeSeries API
ts = TimeSeries(key=api_key, output_format='pandas')

# Function to log a trade
def log_trade(asset, action, price, quantity, notes=""):
    folder_name = "trade_logs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    file_path = os.path.join(folder_name, "trades.csv")
    
    trade_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "asset": asset,
        "action": action,
        "quantity": quantity,
        "price": price,
        "notes": notes
    }
    
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=trade_data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(trade_data)

# Function to fetch stock data
def get_stock_data(symbol):
    data, meta_data = ts.get_intraday(symbol=symbol, interval='1min', outputsize='compact')
    return data

# Function to implement a basic Moving Average Crossover strategy
def moving_average_strategy(data, symbol):
    data['SMA_10'] = data['4. close'].rolling(window=10).mean()
    data['SMA_30'] = data['4. close'].rolling(window=30).mean()

    plt.figure(figsize=(12, 6))
    plt.plot(data['4. close'], label='Stock Price')
    plt.plot(data['SMA_10'], label='10-period SMA')
    plt.plot(data['SMA_30'], label='30-period SMA')
    plt.title(f'Moving Average Crossover Strategy for {symbol}')
    plt.legend()
    plt.show()

    last_row = data.iloc[-1]
    
    # Trade signals
    if last_row['SMA_10'] > last_row['SMA_30']:
        print("Buy signal")
        log_trade(symbol, "Buy", last_row['4. close'], 1, "Generated buy signal")
    else:
        print("Sell signal")
        log_trade(symbol, "Sell", last_row['4. close'], 1, "Generated sell signal")

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., 'AAPL'): ").upper()
    print(f"Fetching data for {symbol}...")
    data = get_stock_data(symbol)
    moving_average_strategy(data, symbol)
