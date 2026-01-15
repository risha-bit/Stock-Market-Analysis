# File: src/yahoo_loader.py
import yfinance as yf
import pandas as pd

def load_prices_from_yahoo(symbol, start_date, end_date):
    try:
        # Download data
        stock = yf.download(symbol, start=start_date, end=end_date, progress=False)

        if stock.empty:
            return None, None

     
        # Handle cases where stock["Close"] is a DataFrame (common in new yfinance versions)
        # .values converts to numpy array, .flatten() ensures it's 1D, .tolist() makes it a Python list
        prices = stock["Close"].values.flatten().tolist()

        dates = stock.index.tolist()
        return prices, dates

    except Exception as e:
        print(f"Error loading data: {e}")
        return None, None