# Stock Trading Program

This project is a Python-based stock trading bot that uses Alpha Vantage API to fetch real-time market data and make trading decisions based on predefined strategies.

## Features
- Fetches real-time stock data using Alpha Vantage.
- Implements a basic trading strategy (e.g., Moving Average Crossover).
- Visualizes stock data with Matplotlib.
- Logs trades and stock performance.

## Getting Started

### Prerequisites
- Python 3.x
- Alpha Vantage API Key ([Get one here](https://www.alphavantage.co/support/#api-key))

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Stock-Trading-Program.git
   cd Stock-Trading-Program
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables for the API Key:
   ```bash
   export ALPHA_VANTAGE_API_KEY="your_api_key"
   ```

### Running the Program
To start the trading bot:
```bash
python stock_trading_bot.py
