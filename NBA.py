import yfinance as yf
import streamlit as st

def app():
  st.write("""# Simple Stock Price App Shown are the stock closing price and volume of Google!""")
  tickerSymbol = 'GOOGL'
  tickerData = yf.Ticker(tickerSymbol)
  tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
  st.line_chart(tickerDf.Close)
  st.line_chart(tickerDf.Volume)

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

#get data on this ticker

#get the historical prices for this ticker

# Open	High	Low	Close	Volume	Dividends	Stock Splits



