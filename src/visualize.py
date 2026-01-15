import matplotlib.pyplot as plt 
import streamlit as st
import pandas as pd 

def plot_stock_analysis(prices , dates  , buy_day , sell_day , symbol , sma_20=None, sma_50= None):
    fig, ax =plt.subplots(figsize =(10,5))

    ax.plot(dates , prices , label ="Stock Price")

    #Buy / Sell points
    ax.scatter(dates[buy_day] , prices[buy_day] , color="green" , label="Buy")
    ax.scatter(dates[sell_day] , prices[sell_day] , color="red" , label ="Sell")

    #moving averages(optional)
    if sma_20 is not None:
        ax.plot(dates , sma_20 , label ="SMA 20")
    if sma_50 is not None :
        ax.plot(dates , sma_50 , label ="SMA 50")

    ax.set_title(f"{symbol} Stock Price Analysis")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)