import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
      # Sidebar - Position selection
      st.title('NBA Player Explorer')
      unique_pos= ['C','PF','SF','PG','SG']
      selected_pos= st.sidebar.multiselect('Position', unique_pos, unique_pos)
      #File Upload
      st.subheader("DataFrame")
      st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])







