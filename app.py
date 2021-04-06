import streamlit as st
import stock,NBA
from multiapp import MultiApp 

app = MultiApp()

st.markdown("""
Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Stock", stock)
app.add_app("NBA", NBA)
# The main app
app.run()
