import streamlit as st
import datetime
import yfinance as yf
import pandas as pd
from ta.volatility import BollingerBands
from ta.trend import MACD
from ta.momentum import RSIIndicator

##############
# Retrieving tickers data
def app():
    ticker_list = pd.read_csv('https://raw.githubusercontent.com/kennethmina24/stockapp/master/List%20of%20Names%20(Stocks)')
    #Heading Info
    tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
    tickerData = yf.Ticker(tickerSymbol) # Get ticker data

    #Ticker information
    string_logo = '<img src=%s>' % tickerData.info['logo_url']
    st.markdown(string_logo, unsafe_allow_html=True)

    string_name = tickerData.info['longName']
    st.header('**%s**' % string_name)

    string_summary = tickerData.info['longBusinessSummary']
    st.info(string_summary)
    
        # Function to display values and their names
    def display_summary(tickerSymbol):
        # scrape info on the ticker
        info = get_info(tickerSymbol)
        info_names = ["Name: ", "Close Price: ", "Open Price: ", "52-Week Range: ", "Dividend Rate & Yield: ", \
            "Market Cap: ", "PE Ratio: ", "EPS: "]
        # print out info in sidebar
        for name,infoValue in zip(info_names, info):
            row = \
            f"""<div> 
                    <span style='float: left;'><b>{name}</b></span>
                    <span style='float: right;'> {infoValue}</span>
                </div>
            """
            st.sidebar.markdown(row, unsafe_allow_html=True)
        st.sidebar.markdown("---")

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
    df = yf.download(tickerSymbol, start= start_date,end= end_date, progress=False)
    #Indicators#
    # Bollinger Bands#
    indicator_bb = BollingerBands(df['Low'])
    bb = df
    bb['bb_h'] = indicator_bb.bollinger_hband()
    bb['bb_l'] = indicator_bb.bollinger_lband()
    bb = bb[['Low','bb_h','bb_l']]
    bb=bb.tail(5)

    # Resistence Strength Indicator
    rsi = RSIIndicator(df['Low']).rsi()
     # Plot RSI
    st.header('Stock RSI ')
    st.write("Overbought(Selling Pressure) above 70 /// Oversold(Buying Pressure) below 30")
    st.dataframe(rsi.tail(3))

    ###################
    # Set up main app #
    ###################
    # Data of recent days
    # Plot the prices and the bolinger bands
    st.write('Recent Data')
    st.dataframe(bb)
    progress_bar = st.progress(0)
