import streamlit as st
import stock
import NBA
from multiapp import MultiApp 

app = MultiApp()

st.set_page_config(page_title="Coexist",page_icon="☮️")
st.markdown("""
Computer Science-Automate My Life
""")

# Add all your application here
app.add_app("Stock Market", stock.app)
app.add_app("DraftKings", NBA.app)
# The main app
app.run()
