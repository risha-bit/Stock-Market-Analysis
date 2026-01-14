def calculate_daily_changes(prices):
    return [prices[i] - prices[i-1] 
    for i in range(1, len(prices))]