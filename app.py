import streamlit as st
import stock,NBA
from multiapp import MultiApp 

app = MultiApp()

st.markdown("""
Computer Science-Automate My Life
""")

# Add all your application here
app.add_app("Stock", stock.app)
app.add_app("NBA", NBA.app)
# The main app
app.run()
