import yfinance as yf 

def load_prices_from_yahoo(symbol , start_date , end_date ):
    stock = yf.download(symbol , start = start_date , end = end_date)
    if stock.empty:
        return None , None
        
    prices = stock["Close"].squeeze().tolist()
    dates =stock.index.tolist()

    return prices , dates 