import matplotlib.pyplot as plt 
import streamlit as st

def plot_stock_analysis(prices , dates  , buy_day , sell_day , symbol):
    fig, ax =plt.subplots(figsize =(10,5))

    ax.plot(dates , prices , label ="Stock Price")
    ax.scatter(dates[buy_day] , prices[buy_day] , color="green" , label="Buy")
    ax.scatter(dates[sell_day] , prices[sell_day] , color="red" , label ="Sell")

    ax.set_title(f"{symbol} Stock Price Analysis")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)