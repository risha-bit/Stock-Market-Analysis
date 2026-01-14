#CLI version(optional)
from src.yahoo_loader import load_prices_from_yahoo
from src.analysis import calculate_daily_changes 
from src.kadane import kadane 
from src.visualize import plot_stock_analysis

#yahoo finance inputs 
symbol = input("Enter stock symbol (e.g: AAPL):").upper()
start_date = input("Enter start Date (YYYY-MM-DD):")
end_date = input("Enter the End Date (YYYY-MM-DD):")


prices ,dates = load_prices_from_yahoo(symbol , start_date , end_date)
changes = calculate_daily_changes(prices)

max_profit , buy_day , sell_day = kadane(changes)

print("-- STOCK -- : " , symbol)
print("Expected Profit per share :" , round(max_profit , 2))
print("Optimal Buy Day :" , buy_day +1 )
print("Optimal Sell Day :" , sell_day +1)

plot_stock_analysis(prices , dates , buy_day , sell_day , symbol)