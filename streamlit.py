import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf 

##############
# Stock data #
##############

# Download data
df = yf.download(option,start= start_date,end= end_date, progress=False)

# Bollinger Bands
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
