import streamlit as st 
from datetime import date 
import pandas as pd 

from src.yahoo_loader import load_prices_from_yahoo
from src.kadane import kadane 
from src.analysis  import calculate_daily_changes
from src.visualize import plot_stock_analysis


#------------page configuration -------------
st.set_page_config(page_title = "Stock Market Analyzer",
        layout = "wide")
st.title("Stock Market Profit Analyzer")
st.write(" Use **kadane's Algorithm** to find the optimal Buy & Sell points")
#-----------user input----------------------
symbol = st.text_input("Enter Stock Symbol:", value = "AAPL").upper()
st.caption("Examples : AAPL , TSLA , MSFT , INFY.NS ,TCS.NS, RELIANCE.NS")

Start_date = st.date_input("start Date :" , date(2023,1,1))
end_date = st.date_input("End Date :", date.today() )
#-----------Analysis Button --------------------
if st.button ("Analysis Stock "):
    with st.spinner("Fetching data & Analyzing..."):

        #------load stock data ---------------
        prices , dates =load_prices_from_yahoo(symbol.upper() , start_date , end_date)

        if prices is None or len(prices) == 0:
            st.error("No data found . Check the stock symbol or yahoo finance (e,g : AAPL , TSLA , INFY.NS,TCS.NS, RELIANCE.NS )")
        else:
            #----Run kadane Algorithm 
            max_profit , buy_day , sell_day = kadane(prices)

            #-----calculate dependent metrics 
            if buy_day is not None and sell_day is not None :
                holding_days = sell_day  - buy_day 
                prices_series = pd.Series(prices)
                profit_percentage = ((prices[sell_day] - prices[buy_day]) / prices[buy_day]) * 100
                volatility = prices_series.std()
            else:
                st.warning("No profitable trade found")

            #------show results -----------------
            if max_profit > 0 :
                st.success(f"Maximum Profits : ${max_profit:.2f}")
                st.write(f"Buy day Index :{buy_day}")
                st.write(f"Sell Day Index:{sell_day}")
                st.metric("Profit %", f"{profit_percentage:.2f}%")
                st.metric("Holding Days (Days)", holding_days)
                st.metric("Risk (Volatility)", f"{volatility:.2f}")
            else:
                st.warning("No profitable buy/sell opportunity found")
            
            #--------Plot stock chart ------------------
            plot_stock_analysis(prices , dates , buy_day , sell_day , symbol)
