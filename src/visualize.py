import matplotlib.pyplot as plt 
def plot_stock_analysis(prices , dates , buy_day , sell_day , symbol):
    plt.figure(figsize=(12,6))

    # stock price line 
    plt.plot(dates , prices , label = "Stock Prices ")

    # buy & sell points 
    plt.scatter(dates[buy_day] , prices[buy_day] , color="green" , s=100 , label ="Buy")
    plt.scatter(dates[sell_day] , prices[sell_day] , color = "red" , s=100 , label ="Sell")

    # Labels & Title 
    plt.title(f"{symbol} ,  STOCK PRIZE ANALYSIS")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()