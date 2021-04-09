import streamlit as st
import config
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
   st.set_page_config(layout="wide")
   sidebar = st.sidebar
   leftpanel, rightpanel = st.beta_columns([7, 3])

   Players = pd.DataFrame(config.Players, columns=['Name', 'Url'])
   Player_list = Players.Name.tolist()

   




