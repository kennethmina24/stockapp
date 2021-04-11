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
      def main():
            st.subheader("DataFrame")
            data_file=st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])
            df = pd.read_csv(data_file)
            st.dataframe(df)
      
      







