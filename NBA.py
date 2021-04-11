import streamlit as st
import config
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
      # Sidebar - Position selection
      unique_pos= ['C','PF','SF','PG','SG']
      selected_pos= st.sidebar.multiselect('Position', unique_pos, unique_pos)
      #File Upload
      st.subheader("Dataset")
      st.file_uploader("Upload CSV",type=['csv'])







