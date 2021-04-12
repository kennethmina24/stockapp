import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def app():
      # Sidebar - Position selection
      st.title('NBA Player Explorer')
      unique_pos= ['C','PF','SF','PG','SG']
      selected_pos= st.sidebar.multiselect('Position', unique_pos, unique_pos)
      #File Upload
      st.subheader("DataFrame")
      data_file=st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])
      if data_file is None:
            st.write("Enter File, the data set is empty")
      if data_file is not None:
            df = pd.read_csv(data_file)
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
                     #Show Data
            st.write(file_details)
            st.dataframe(df)
      
      
      
      







