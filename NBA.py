import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def app():
      # Sidebar - Position selection
      st.title('NBA Player Explorer')
      #File Upload
      st.subheader("DataFrame")
      st.sidebar.header('User Input Features')
      selected_year = st.sidebar.selectbox('Year', list(reversed(range(2019,2021))))

      # Web scraping of NBA player stats
      @st.cache
      def load_data(year):
          url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
          html = pd.read_html(url, header = 0)
          df = html[0]
          raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
          raw = raw.fillna(0)
          playerstats = raw.drop(['Rk','Age','G','GS'], axis=1)
          playerstats=playerstats.rename(columns={'Player':'Name'})
          playerstats=playerstats.drop_duplicates(subset=(['Name']))
          return playerstats
      playerstats = load_data(selected_year)
      
      # Sidebar - Team selection
      sorted_unique_team = sorted(playerstats.Tm.unique())
      selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)

      # Sidebar - Position selection
      unique_pos = ['C','PF','SF','PG','SG']
      selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

      # Filtering data
      df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]

      st.header('Display Player Stats of Selected Team(s)')
      st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
      st.dataframe(df_selected_team)
      # Heatmap
      if st.button('Intercorrelation Heatmap'):
            st.header('Intercorrelation Matrix Heatmap')
            df_selected_team.to_csv('output.csv',index=False)
            df = pd.read_csv('output.csv')

            corr = df.corr()
            mask = np.zeros_like(corr)
            mask[np.triu_indices_from(mask)] = True
            with sns.axes_style("white"):
                  f, ax = plt.subplots(figsize=(7, 5))
                  ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

      
      data_file=st.file_uploader("Upload File",type=['csv','txt','docx','pdf'])
      if data_file is None:
            st.write("Enter File, the data set is empty")
      if data_file is not None:
            pf = pd.read_csv(data_file)
            pf=pf.drop(columns=['TeamAbbrev','Name + ID','Game Info','Roster Position','ID'])
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize":data_file.size}
            pf=pf.rename(columns={'Position':'Pos'})
                   #Show Data
            st.write(file_details)
                     # Filtering data    
            #Combine List
            Combined_DK_Website=pf.merge( df_selected_team,how='outer',on='Name')
            Combined_DK_Website=Combined_DK_Website.drop(columns= ['Pos_x'])
            Combined_DK_Website=Combined_DK_Website.fillna(0)
            #Combined_DK_Website=[(Combined_DK_Website.Salary != 0)]

           
            
            st.dataframe(Combined_DK_Website)
       
      
      
      







