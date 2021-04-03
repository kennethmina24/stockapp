import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

##############
#Test SideBar#
# Retrieving tickers data
ticker_list = pd.read_csv('https://raw.githubusercontent.com/kennethmina24/stockapp/master/List%20of%20Names%20(Stocks)')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data


#Side Function
option = st.sidebar.selectbox('Select one symbol', ( 'AAPL', 'MSFT',"SPY",'WMT'))
#Heading Info

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)

###########
# sidebar #
###########
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=1825)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('End date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error('Error: End date must fall after start date.')
###############
#Download Data#
###############
df = yf.download(ticker_list, start= start_date,end= end_date, progress=False)
#Indicators#
# Bollinger Bands#
indicator_bb = BollingerBands(df['Low'])
bb = df
bb['bb_h'] = indicator_bb.bollinger_hband()
bb['bb_l'] = indicator_bb.bollinger_lband()
bb = bb[['Low','bb_h','bb_l']]

# Resistence Strength Indicator
rsi = RSIIndicator(df['Low']).rsi()

###################
# Set up main app #
###################

# Plot the prices and the bolinger bands
st.write('Stock Bollinger Bands')
st.line_chart(bb)


progress_bar = st.progress(0)

# Plot RSI
st.write('Stock RSI ')
st.line_chart(rsi)

# Data of recent days
st.write('Recent data ')
st.dataframe(df.tail(30))


