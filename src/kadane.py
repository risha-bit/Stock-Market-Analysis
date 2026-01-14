def kadane(prices):
    max_profit =0
    current_profit =0
    buy = sell = temp_buy =0
    
    for i in range(1, len(prices)):
        diff =prices[i] - prices[i-1]

        if current_profit  + diff > 0:
            current_profit += diff
        else:
            current_profit =0
            temp_buy = i

        if current_profit > max_profit :
            max_profit = current_profit 
            buy = temp_buy
            sell =i
    return max_profit , buy , sell 

