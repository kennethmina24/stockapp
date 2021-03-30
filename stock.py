import streamlit as st

st.write("""
## Closing Price
""")

option = st.sidebar.selectbox('Select one symbol', ( 'AAPL', 'MSFT',"SPY",'WMT'))
