import numpy as np 
import pandas as pd 
import yfinance
import streamlit as st 
import datetime
import requests
import random


# HELPER FUNCITONS
def get_symbol(symbol):
    """
    inp: str
    out: str
    return company name of the ticker given
    """
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            return x['name']


    return "NOT FOUND"





#   MAIN APP START



st.write("""
# Stock app 

#### Powered by Yahoo Finance 
 

""")


#--------------------------
#getting the tickers for stock
# pip install pip install get-all-tickers
from get_all_tickers import get_tickers as gt

list_of_tickers = gt.get_tickers()

#--------------------------



tickerSymbol = "GOOGL"  #default
list_of_tickers=list_of_tickers[:10]


tickerNameDf=[]
for ticker in list_of_tickers:
    companyName = get_symbol(ticker)
    temp = [ticker, companyName]
    tickerNameDf.append(temp)
tickerNameDf = pd.DataFrame(tickerNameDf, columns=["Ticker", "Company"])
    


tickerSymbol = st.selectbox('Please select a ticker ', options=list_of_tickers)

if st.button('Press after selection '):
    st.write("## The stock selected is :{}".format(tickerSymbol))


    tickerData = yfinance.Ticker(tickerSymbol) # gets that respective data 

    currDate = datetime.datetime.today().date()

    tickerDf = tickerData.history(period='1d',start="2018-01-01", end="2021-01-07") # pass parameters as mentioned

    st.write("## Opening value")
    st.line_chart(tickerDf.Open)
    st.write("## Close value")
    st.line_chart(tickerDf.Close)
    st.write("## Volume value")
    st.line_chart(tickerDf.Volume)



