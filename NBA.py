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
      If data_file is False:
	print(Upload File)
      elif:
	data_file=st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])
        df = pd.read_csv(data_file)
        file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
	#Show Data
      st.write(file_details)
      st.dataframe(df)
      
      







