#streamlit runs here 
import streamlit as st 
from datetime import date 

from src.yahoo_loader import load_prices_from_yahoo
from src.kadane import kadane 
from src.visualize import plot_stock_analysis

st.set_page_config(page_title = "Stock Market Analyzer" , layout = "wide")
st.title("Stock Market Profit Analyzer")
st.write("Using **Kadane's Algorithm** to find the best Buy & Sell points")
#------ input -----------
symbol = st.text_input(label = "Enter the stock Symbol:" ,
                       value ="AAPL")
st.caption("Examples : AAPL , TSLA , MSFT , INFYS.NS , RELIANCE.NS")

start_date  = st.date_input("Start Date :" , date(2023 , 1, 1))
end_date = st.date_input("End date:", date.today())

#------ Button ------------
if st.button("Analyze Stock "):
    with st.spinner("Fetching Data & Analyzing ..."):
        prices , dates = load_prices_from_yahoo(symbol.upper() , start_date , end_date)

        if prices is None:
            st.error("No Data Found\n, Check the Stock Symbol\n use YAHOO finance formte(e.g AAPL , TSLA , INFYS.NS ")
        else:
            max_profit , buy_day , sell_day = kadane(prices)
        if max_profit ==0:
            st.warning("No Profitable buy/seel oppurtunity found ")

        #--------  Result ------------
        st.success(f"Maximum Profits :${ max_profit:.2f}")
        st.write(f"Buy Day Index : {buy_day}")
        st.write(f"Sell Day Index : {sell_day}")

        #------- plot ---------------
        
        plot_stock_analysis(prices, dates , buy_day , sell_day , symbol)